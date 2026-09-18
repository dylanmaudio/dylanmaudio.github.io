# dylanmaudio.com — working notes for Claude

The public site for **dylanmaudio** — Dylan Mitrovich's commercial macOS
software for live sound, aimed at Allen & Heath dLive consoles. GitHub Pages
serves `main` at dylanmaudio.com (see `CNAME`). Also hosts the Quick
Reference PDFs each app's in-app footer links to, under `guides/`.

## The rule that matters here

**The deployed HTML is generated, never hand-edited.** Everything comes from
`build/`:

```bash
python3 build/build_all.py     # regenerate index.html, about.html, product pages
```

then commit + push. Editing `index.html`, `about.html` or
`products/<slug>/index.html` directly will be overwritten by the next build.

- **Product copy, links, the Discord URL, store URLs** → `build/common.py`
  (`PRODUCTS` and the shared constants).
- **Home page layout** → `build/build_site.py`. **About** →
  `build_about.py`. **Per-product pages** → `build_products.py` (its
  `BUILD = [...]` list controls which pages ship). **Short links** →
  `build_redirects.py` (static Pages has no server-side 301s, so these are
  real pages using `<meta http-equiv="refresh">` plus `location.replace()`).
- See [build/README.md](build/README.md) for the full table, including how
  intro videos and "coming soon" → "Learn more" CTAs are switched over.

## What is actually public

**Public on the Lemon Squeezy store** (`store.dylanmaudio.com`): MIDI Bridge
(free), Talk Light Trigger ($19), Pilot Tone Trigger ($59) and Time Code Tool
($69), plus both bundles (TLT+PTT, and the same plus Time Code Tool).

**Not public:** Console Control (`status="coming"` in `PRODUCTS`) and the
Bitfocus Companion module. Their pages and CTAs must not imply availability
unless the operator says an item has shipped.

Current DMGs are Apple-Silicon-only — `REQUIREMENTS` in `build/common.py`
declares *"macOS 11 or later · Apple Silicon"* until the universal2 rebuild
lands. Don't drop that line.

## Sibling repos

- **`dLive-Utility-Apps`** — the monorepo behind the products. It is the
  source of the Quick Reference PDFs (`tools/publish_quick_reference.py`
  stages them; committing and pushing them here stays a reviewed manual
  step, like notarization), and `shared/links.py` there is the single source
  for the guide URLs — so a guide's filename is not ours to rename freely.
- **`companion-module-dylanmaudio`** — the Bitfocus Companion module.
- **`automation-pack`** — the older Reaper-based pack, NDA-only, not
  mentioned publicly.

## Analytics — the site and the apps differ

**The apps carry no telemetry or analytics, ever** — that is a product
promise in `PRIVACY.txt` and the EULA. **The site is not the apps:** it runs
Cloudflare Web Analytics (cookieless, no consent banner), switched by
`CF_BEACON_TOKEN` in `build/common.py` and injected by `inject_analytics()`.
Empty token = off, and pages then build byte-identical. Don't conflate the
two when writing copy, and don't add any *other* tracking without asking.

## The Allen & Heath non-affiliation line

`NONAFFIL` in `build/common.py`, rendered into the `foot-legal` footer of
every generated page by `build_site.py`, `build_about.py` and
`build_products.py`.

**Operator directive (2026-09-18): it stays on the website exactly where it
is — don't remove or relocate it — but it is NOT a requirement elsewhere.**
Marketing material, generated imagery, social/OG cards, store copy and
screenshots don't need to carry it. Treat it as optional on anything that
isn't the site footer, rather than a line to be propagated.

Two things it is not, so nobody removes the wrong one:

- The **EULA (`LICENSE` §1, "NOT AFFILIATED WITH ALLEN & HEATH")** is a
  legal clause and unaffected by this.
- The per-product `affiliated` flag in `PRODUCTS` (`True` for the dLive
  apps, `False` for the console-agnostic Time Code Tool) is separate from
  `NONAFFIL` — check what it gates before touching either.
