#!/usr/bin/env python3
"""Read a calendar export (.ics, a Google Calendar export .zip, or a secret iCal
URL) and print the user's meetings in a window as JSON. Standard library only.

Handles the parts of iCalendar a work calendar actually uses: TZID and UTC
times, all-day events, recurring events (RRULE with DAILY/WEEKLY/MONTHLY/YEARLY,
INTERVAL, BYDAY, UNTIL, COUNT), EXDATE, and moved or cancelled single
occurrences (RECURRENCE-ID).

Dropped here so the caller never sees them: cancelled events, events the user
declined, all-day events (out of office, holidays, reminders) and events marked
free (TRANSP:TRANSPARENT). Judging which remaining events are placeholders
("Focus time", "Lunch") is left to the caller.

Usage: calendar_events.py --source <file|zip|url> --since 2026-09-23 --until 2026-10-23 --me first.last@govtech.bb
  --until is exclusive. --me is the user's calendar email; it finds their RSVP.
"""
import argparse
import io
import json
import re
import urllib.request
import zipfile
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

LOCAL = datetime.now().astimezone().tzinfo
DAYS = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]


def load_text(source):
    if source.startswith(("http://", "https://")):
        with urllib.request.urlopen(source, timeout=60) as response:
            data = response.read()
    else:
        with open(source, "rb") as handle:
            data = handle.read()
    if data[:2] == b"PK":  # Google's "Export" gives a zip of one .ics per calendar
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            return [archive.read(n).decode("utf-8", "replace") for n in archive.namelist() if n.endswith(".ics")]
    return [data.decode("utf-8", "replace")]


def parse_events(text):
    lines = []
    for raw in text.splitlines():  # unfold continuation lines
        if raw[:1] in (" ", "\t") and lines:
            lines[-1] += raw[1:]
        else:
            lines.append(raw)
    events, current = [], None
    for line in lines:
        if line == "BEGIN:VEVENT":
            current = defaultdict(list)
        elif line == "END:VEVENT" and current is not None:
            events.append(current)
            current = None
        elif current is not None and ":" in line:
            head, value = line.split(":", 1)
            name, *params = head.split(";")
            current[name.upper()].append((dict(p.split("=", 1) for p in params if "=" in p), value))
    return events


def unescape(value):
    return value.replace("\\n", "\n").replace("\\N", "\n").replace("\\,", ",").replace("\\;", ";").replace("\\\\", "\\")


def parse_time(params, value):
    """Return (aware datetime, is_all_day)."""
    if params.get("VALUE") == "DATE" or re.fullmatch(r"\d{8}", value):
        return datetime.strptime(value, "%Y%m%d").replace(tzinfo=LOCAL), True
    moment = datetime.strptime(value.rstrip("Z"), "%Y%m%dT%H%M%S")
    if value.endswith("Z"):
        return moment.replace(tzinfo=timezone.utc), False
    if "TZID" in params:
        try:
            return moment.replace(tzinfo=ZoneInfo(params["TZID"].strip('"'))), False
        except Exception:
            pass
    return moment.replace(tzinfo=LOCAL), False


def first(event, name):
    return event[name][0] if event.get(name) else ({}, "")


def parse_duration(value):
    match = re.fullmatch(r"P(?:(\d+)W)?(?:(\d+)D)?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?)?", value or "")
    if not match:
        return None
    w, d, h, m, s = (int(x or 0) for x in match.groups())
    return timedelta(weeks=w, days=d, hours=h, minutes=m, seconds=s)


def add_months(moment, months):
    index = moment.year * 12 + moment.month - 1 + months
    year, month = divmod(index, 12)
    try:
        return moment.replace(year=year, month=month + 1)
    except ValueError:
        return None  # e.g. the 31st in a 30-day month: RFC 5545 skips it


def occurrences(start, rule, window_end):
    """Yield start times for an RRULE, up to window_end."""
    parts = dict(p.split("=", 1) for p in rule.split(";") if "=" in p)
    freq = parts.get("FREQ")
    interval = int(parts.get("INTERVAL", 1))
    count = int(parts["COUNT"]) if "COUNT" in parts else None
    until = None
    if "UNTIL" in parts:
        until, _ = parse_time({}, parts["UNTIL"])
    byday = [d[-2:] for d in parts.get("BYDAY", "").split(",") if d]
    produced = 0

    def emit(moment):
        nonlocal produced
        if until and moment > until:
            return False
        if count is not None and produced >= count:
            return False
        produced += 1
        return True

    if freq == "WEEKLY" and byday:
        week_start = start - timedelta(days=start.weekday())
        step = 0
        while True:
            base = week_start + timedelta(weeks=step * interval)
            if base > window_end:
                return
            for day in sorted(DAYS.index(d) for d in byday):
                moment = base + timedelta(days=day)
                if moment < start:
                    continue
                if not emit(moment):
                    return
                yield moment
            step += 1
    else:
        step = 0
        while True:
            if freq == "DAILY":
                moment = start + timedelta(days=step * interval)
            elif freq == "WEEKLY":
                moment = start + timedelta(weeks=step * interval)
            elif freq == "MONTHLY":
                moment = add_months(start, step * interval)
            elif freq == "YEARLY":
                moment = add_months(start, 12 * step * interval)
            else:
                yield start
                return
            step += 1
            if moment is None:
                continue
            if moment > window_end:
                return
            if freq == "DAILY" and byday and DAYS[moment.weekday()] not in byday:
                continue
            if not emit(moment):
                return
            yield moment


def my_status(event, me):
    for params, value in event.get("ATTENDEE", []):
        if value.lower().replace("mailto:", "") == me:
            return params.get("PARTSTAT", "NEEDS-ACTION").upper()
    return "ORGANIZER" if me and me in first(event, "ORGANIZER")[1].lower() else None


JOINING_TEXT = re.compile(
    r"-::~:~::~.*?::-|Join (with )?(Google Meet|Zoom).*|is inviting you to a scheduled Zoom meeting.*|<[^>]+>",
    re.S | re.I)


def clean_description(text):
    """Strip video-call joining blocks and HTML so the purpose of the meeting shows."""
    return re.sub(r"\s+", " ", JOINING_TEXT.sub(" ", unescape(text))).strip()


def describe(event, start, end, me):
    attendees = [v.lower().replace("mailto:", "") for _, v in event.get("ATTENDEE", [])]
    domains = sorted({a.split("@")[-1] for a in attendees if "@" in a and "resource.calendar" not in a})
    return {
        "title": unescape(first(event, "SUMMARY")[1]) or "(no title)",
        "start": start.astimezone(LOCAL).strftime("%Y-%m-%d %a %H:%M"),
        "minutes": int((end - start).total_seconds() // 60),
        "recurring": bool(event.get("RRULE")) or bool(event.get("RECURRENCE-ID")),
        "series": first(event, "UID")[1],
        "my_status": my_status(event, me),
        "organiser": first(event, "ORGANIZER")[1].lower().replace("mailto:", ""),
        "attendee_count": len(attendees),
        "attendee_domains": domains,
        "description": clean_description(first(event, "DESCRIPTION")[1])[:300],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--since", required=True)
    parser.add_argument("--until", required=True, help="exclusive")
    parser.add_argument("--me", default="")
    args = parser.parse_args()
    me = args.me.lower()
    window_start = datetime.combine(date.fromisoformat(args.since), datetime.min.time(), LOCAL)
    window_end = datetime.combine(date.fromisoformat(args.until), datetime.min.time(), LOCAL)

    events = [e for text in load_text(args.source) for e in parse_events(text)]
    overrides = {}  # (uid, original start) -> replacement event
    for event in events:
        if event.get("RECURRENCE-ID"):
            moment, _ = parse_time(*first(event, "RECURRENCE-ID"))
            overrides[(first(event, "UID")[1], moment)] = event

    meetings, all_day_events, seen = [], [], set()

    def consider(event, start, end, all_day):
        if start >= window_end or end <= window_start:
            return
        if all_day:  # not meetings, but leave and holidays matter for an invoice
            if first(event, "STATUS")[1].upper() != "CANCELLED":
                last = max(start, end - timedelta(days=1))
                all_day_events.append({"title": unescape(first(event, "SUMMARY")[1]),
                                       "from": start.strftime("%Y-%m-%d"), "to": last.strftime("%Y-%m-%d")})
            return
        if first(event, "STATUS")[1].upper() == "CANCELLED":
            return
        if first(event, "TRANSP")[1].upper() == "TRANSPARENT":
            return
        if my_status(event, me) == "DECLINED":
            return
        key = (first(event, "UID")[1], start)
        if key in seen:  # the same event exported from two calendars
            return
        seen.add(key)
        meetings.append(describe(event, start, end, me))

    for event in events:
        if not event.get("DTSTART"):
            continue
        start, all_day = parse_time(*first(event, "DTSTART"))
        if event.get("DTEND"):
            end, _ = parse_time(*first(event, "DTEND"))
        else:
            end = start + (parse_duration(first(event, "DURATION")[1]) or timedelta(0))
        length = end - start
        if event.get("RECURRENCE-ID"):
            consider(event, start, end, all_day)
            continue
        if not event.get("RRULE"):
            consider(event, start, end, all_day)
            continue
        excluded = set()
        for params, value in event.get("EXDATE", []):
            for item in value.split(","):
                excluded.add(parse_time(params, item)[0])
        uid = first(event, "UID")[1]
        for moment in occurrences(start, first(event, "RRULE")[1], window_end):
            if moment in excluded or (uid, moment) in overrides:
                continue
            consider(event, moment, moment + length, all_day)

    meetings.sort(key=lambda m: m["start"])
    # Google splits a series into several UIDs each time it's edited ("this and
    # following events"), so group recurring meetings by their title instead.
    series = defaultdict(list)
    for m in meetings:
        if m["recurring"]:
            series[re.sub(r"\s+", " ", m["title"]).strip().lower()].append(m)
    print(json.dumps({
        "window": {"since": args.since, "until_exclusive": args.until},
        "meeting_count": len(meetings),
        "total_hours": round(sum(m["minutes"] for m in meetings) / 60, 1),
        "recurring_series": sorted(
            ({"title": items[0]["title"], "times": len(items),
              "hours": round(sum(i["minutes"] for i in items) / 60, 1),
              "max_attendees": max(i["attendee_count"] for i in items)}
             for items in series.values()),
            key=lambda s: -s["times"]),
        "one_off_meetings": [m for m in meetings if not m["recurring"]],
        "all_day_events": sorted(all_day_events, key=lambda e: e["from"]),
    }, indent=1))


if __name__ == "__main__":
    main()
