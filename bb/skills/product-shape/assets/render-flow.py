#!/usr/bin/env python3
"""Render a mermaid flowchart into an HTML fragment for the product-shape artifact.

Why this exists: a published Artifact will not always render a `<pre class="mermaid">`
block, and when it fails it silently shows the diagram source as plain text. Inlining
pre-rendered SVG cannot fail that way. Two variants are produced so the diagram follows
the viewer's theme, and every internal id is namespaced — without that, the two copies
collide on ~60 ids and the dark variant's arrowheads resolve to the light variant's
markers.

Usage:
    python3 render-flow.py flow.mmd > fragment.html

Then paste fragment.html where the template says to. Requires npx (mermaid-cli is
fetched on demand) and a writable temp directory.
"""

import json
import pathlib
import re
import subprocess
import sys
import tempfile

THEMES = {
    "flow-light": {
        "prefix": "fl-",
        "vars": {
            "background": "#ffffff", "primaryColor": "#E6EEF8", "primaryTextColor": "#0E1620",
            "primaryBorderColor": "#0B4F9E", "lineColor": "#5A6675", "secondaryColor": "#F1F4F8",
            "tertiaryColor": "#F1F4F8",
        },
    },
    "flow-dark": {
        "prefix": "fd-",
        "vars": {
            "background": "#141C26", "primaryColor": "#1A2839", "primaryTextColor": "#E7EDF4",
            "primaryBorderColor": "#6FA8E8", "lineColor": "#93A1B2", "secondaryColor": "#1B2534",
            "tertiaryColor": "#1B2534",
        },
    },
}

FONT = "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, system-ui, sans-serif"


def render(src: pathlib.Path, out_dir: pathlib.Path, cls: str, spec: dict) -> str:
    config = out_dir / f"{cls}.json"
    config.write_text(json.dumps({
        "theme": "base",
        "themeVariables": {**spec["vars"], "fontSize": "14px", "fontFamily": FONT},
    }))
    svg_path = out_dir / f"{cls}.svg"
    subprocess.run(
        ["npx", "-y", "@mermaid-js/mermaid-cli", "-i", str(src), "-o", str(svg_path),
         "-c", str(config), "-b", "transparent"],
        check=True, capture_output=True,
    )
    svg = svg_path.read_text()
    svg = svg[svg.index("<svg"):]

    # Namespace every id, and every reference to it, so the two variants cannot collide.
    prefix = spec["prefix"]
    for ident in sorted(set(re.findall(r'id="([^"]+)"', svg)), key=len, reverse=True):
        svg = svg.replace(f'id="{ident}"', f'id="{prefix}{ident}"')
        svg = svg.replace(f"url(#{ident})", f"url(#{prefix}{ident})")
        svg = svg.replace(f"#{ident} ", f"#{prefix}{ident} ")
        svg = svg.replace(f"#{ident}{{", f"#{prefix}{ident}{{")
        svg = svg.replace(f'xlink:href="#{ident}"', f'xlink:href="#{prefix}{ident}"')

    # mermaid emits some ids twice within one diagram; nothing references those, so
    # de-duplicate them to keep the host document valid.
    seen: dict[str, int] = {}

    def once(match: re.Match) -> str:
        value = match.group(1)
        seen[value] = seen.get(value, 0) + 1
        return f'id="{value}"' if seen[value] == 1 else f'id="{value}-{seen[value]}"'

    svg = re.sub(r'id="([^"]+)"', once, svg)

    # Let the page size it.
    svg = re.sub(r'style="[^"]*max-width:[^"]*"', 'style="max-width:100%;height:auto"', svg, count=1)
    svg = re.sub(r'\swidth="[\d.]+"', "", svg, count=1)
    return svg


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    src = pathlib.Path(sys.argv[1])
    if not src.is_file():
        print(f"no such file: {src}", file=sys.stderr)
        return 1

    label = ("Service flow: solid paths are week one on fallbacks, "
             "dashed paths are the deferred upgrades")
    parts = []
    with tempfile.TemporaryDirectory() as tmp:
        out_dir = pathlib.Path(tmp)
        for cls, spec in THEMES.items():
            svg = render(src, out_dir, cls, spec)
            parts.append(f'<div class="diagram {cls}" role="img" aria-label="{label}">\n{svg}\n</div>')

    fragment = "\n".join(parts)
    ids = re.findall(r'id="([^"]+)"', fragment)
    assert len(ids) == len(set(ids)), "duplicate ids survived namespacing"
    unresolved = {u for u in re.findall(r"url\(#([^)]+)\)", fragment) if f'id="{u}"' not in fragment}
    assert not unresolved, f"unresolved references: {sorted(unresolved)}"

    print(fragment)
    print(f"\n<!-- rendered {len(THEMES)} theme variants, {len(ids)} namespaced ids -->", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
