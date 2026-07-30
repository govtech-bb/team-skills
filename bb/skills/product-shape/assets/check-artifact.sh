#!/usr/bin/env bash
# Verifies an artifact page (or the template it came from) holds together.
# Usage: check-artifact.sh <file.html>
set -euo pipefail
F="$1"

python3 - "$F" <<'PY'
import re, sys, xml.etree.ElementTree as ET
from html.parser import HTMLParser

s = open(sys.argv[1]).read()
fails = []

def need(cond, msg):
    if not cond:
        fails.append(msg)

# ── required panels, in order ──
order = ['The brief', 'Form features required', 'Custom features required',
         'Not ported', 'Phase board', 'Development phases']
pos = -1
for h in order:
    i = s.find(f'<h2>{h}</h2>')
    need(i != -1, f'missing panel: {h}')
    if i != -1:
        need(i > pos, f'panel out of order: {h}')
        pos = i

# ── the board must be a faithful second reading of the phases ──
hrefs = re.findall(r'<a class="card" href="#([^"]+)"', s)
ids   = re.findall(r'id="(phase-\d+)"', s)
need(bool(hrefs), 'no board cards')
need(all(f'id="{h}"' in s for h in hrefs), 'a card links to a missing phase id')
need(sorted(set(hrefs)) == sorted(set(ids)), 'cards and phases do not correspond one to one')

board = s[s.find('<div class="board">'):s.find('<h2>Development phases</h2>')]
lanes = [p for p in re.split(r'(?=<div class="lane)', board) if 'lane-name' in p]
need(bool(lanes), 'no lanes in the board')
for lane in lanes:
    name = re.search(r'lane-name">(.*?)<', lane).group(1)
    declared = re.search(r'lane-count">(.*?)<', lane).group(1)
    cards = lane.count('<a class="card"')
    need(cards > 0, f'empty lane: {name} — drop it instead')
    if declared.isdigit():
        need(int(declared) == cards, f'lane "{name}" declares {declared} but holds {cards} cards')

# each card's lane must match the horizon chip on the phase it points at
HORIZONS = ('Now', 'Next week', 'Later')
for lane in lanes:
    lane_name = re.search(r'lane-name">(.*?)<', lane).group(1)
    horizon = next((h for h in HORIZONS if h.lower() in lane_name.lower()), None)
    for target in re.findall(r'href="#(phase-\d+)"', lane):
        i = s.find(f'id="{target}"')
        if i == -1 or horizon is None:
            continue
        block = s[i: i + max(0, s[i:].find('</dl>'))]
        chips = re.findall(r'<span class="chip \w+">(.*?)</span>', block)
        need(any(horizon.lower() in c.lower() for c in chips),
             f'{target} sits in lane "{lane_name}" but its chips say {chips}')

# exactly one phase may be "Now"
need(s.count('class="phase is-now"') <= 1, 'more than one phase marked is-now')

# ── every in-page link resolves ──
for frag in set(re.findall(r'href="#([^"]+)"', s)):
    need(f'id="{frag}"' in s, f'dangling link: #{frag}')
for ref in set(re.findall(r'url\(#([^)]+)\)', s)):
    need(f'id="{ref}"' in s, f'unresolved url(#{ref})')

# ── ids unique ──
allids = re.findall(r'id="([^"]+)"', s)
dupes = {i for i in allids if allids.count(i) > 1}
need(not dupes, f'duplicate ids: {sorted(dupes)[:5]}')

# ── inlined SVGs are well-formed XML; the HTML shell balances ──
# Entity declarations are refused rather than parsed: stdlib ElementTree resolves them, which is how
# XXE and billion-laughs work. Mermaid never emits a DOCTYPE, so anything carrying one is suspect.
for n, svg in enumerate(re.findall(r'(<svg\b.*?</svg>)', s, re.S)):
    if re.search(r'<!DOCTYPE|<!ENTITY', svg, re.I):
        need(False, f'svg[{n}] carries an entity declaration — refusing to parse it')
        continue
    try:
        ET.fromstring(svg)
    except ET.ParseError as e:
        need(False, f'svg[{n}] is not well-formed: {e}')

shell = re.sub(r'<svg\b.*?</svg>', '<!--svg-->', s, flags=re.S)
VOID = {'br', 'hr', 'img', 'input', 'meta', 'link', 'source', 'wbr', 'col'}

class Balance(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errs = [], []
    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))
    def handle_endtag(self, tag):
        if not self.stack:
            self.errs.append(f'stray </{tag}> line {self.getpos()[0]}')
            return
        top, at = self.stack.pop()
        if top != tag:
            self.errs.append(f'<{top}> line {at[0]} closed by </{tag}> line {self.getpos()[0]}')

b = Balance()
b.feed(shell)
need(not b.stack, f'unclosed: {[f"<{t}> line {p[0]}" for t, p in b.stack][:5]}')
need(not b.errs, f'mismatched: {b.errs[:5]}')

# ── styling completeness and theming ──
used = set(c for m in re.findall(r'class="([^"]+)"', shell) for c in m.split())
css = s[:s.find('</style>')]
defined = set(re.findall(r'\.([A-Za-z][\w-]*)', css))
need(not (used - defined), f'classes used but never styled: {sorted(used - defined)[:5]}')
for token in ('prefers-color-scheme: dark', ':root[data-theme="dark"]', ':root[data-theme="light"]'):
    need(token in css, f'missing theme rule: {token}')
need('prefers-reduced-motion' in css, 'smooth scrolling with no reduced-motion opt-out')
need('.card:focus-visible' in css, 'board cards have no visible focus state')
need('<pre class="mermaid"' not in s, 'raw mermaid block will not reliably render — inline SVG instead')

if fails:
    for f in fails:
        print(f'FAIL {f}')
    raise SystemExit(1)
print('PASS')
PY
