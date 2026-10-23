#!/usr/bin/env python3
"""Work out invoice periods from the invoice day of the month.

A period runs from the invoice day in one month up to (not including) the
invoice day in the next, e.g. day 23 -> 23 Sep .. 22 Oct. Days past the end of
a short month clamp to its last day (day 31 in February -> 28 or 29).

Prints JSON with two periods so the caller can choose and say which it used:
  latest_complete  the most recent period whose last day is today or earlier
  current          the period that contains today (still open)
Times carry the machine's real local UTC offset; no timezone is hardcoded.

Usage: period.py --day 23 [--today 2026-10-12] [--ending 2026-10-22]
  --ending  pick the period whose last day is this date instead (for back-filling)
"""
import argparse
import calendar
import json
from datetime import date, datetime, timedelta


def anchor(year, month, day):
    """The invoice day in a given month, clamped to the month's length."""
    return date(year, month, min(day, calendar.monthrange(year, month)[1]))


def shift(year, month, delta):
    index = year * 12 + (month - 1) + delta
    return index // 12, index % 12 + 1


def period_starting(start, day):
    next_year, next_month = shift(start.year, start.month, 1)
    end_exclusive = anchor(next_year, next_month, day)
    return start, end_exclusive


def describe(start, end_exclusive):
    last = end_exclusive - timedelta(days=1)
    offset = datetime.now().astimezone().strftime("%z")
    offset = offset[:3] + ":" + offset[3:]
    if start.year == last.year:
        label = f"{start.day} {start:%b} – {last.day} {last:%b %Y}"
    else:
        label = f"{start.day} {start:%b %Y} – {last.day} {last:%b %Y}"
    return {
        "label": label,
        "start_date": start.isoformat(),
        "last_date": last.isoformat(),
        "end_exclusive_date": end_exclusive.isoformat(),
        "since": f"{start.isoformat()}T00:00:00{offset}",
        "until": f"{end_exclusive.isoformat()}T00:00:00{offset}",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", type=int, required=True)
    parser.add_argument("--today")
    parser.add_argument("--ending")
    args = parser.parse_args()
    if not 1 <= args.day <= 31:
        parser.error("--day must be between 1 and 31")

    today = date.fromisoformat(args.today) if args.today else date.today()

    if args.ending:
        last = date.fromisoformat(args.ending)
        end_exclusive = last + timedelta(days=1)
        year, month = shift(end_exclusive.year, end_exclusive.month, -1)
        start = anchor(year, month, args.day)
        print(json.dumps({"requested": describe(start, end_exclusive)}, indent=2))
        return

    # The current period starts on the latest invoice day on or before today.
    this_month = anchor(today.year, today.month, args.day)
    if this_month <= today:
        current_start = this_month
    else:
        year, month = shift(today.year, today.month, -1)
        current_start = anchor(year, month, args.day)
    current = period_starting(current_start, args.day)

    # A period whose last day is today counts as complete: people invoice on it.
    if current[1] - timedelta(days=1) <= today:
        latest = current
    else:
        year, month = shift(current_start.year, current_start.month, -1)
        latest = period_starting(anchor(year, month, args.day), args.day)

    print(json.dumps({
        "today": today.isoformat(),
        "latest_complete": describe(*latest),
        "current": describe(*current),
    }, indent=2))


if __name__ == "__main__":
    main()
