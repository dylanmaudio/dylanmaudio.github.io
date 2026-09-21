# Build

The site is generated from these scripts so the deployed HTML is never hand-edited.
Everything they need is committed in this repo (`/assets`), so the build is fully
reproducible — no machine-specific paths, no external repos.

```bash
python3 build/build_all.py     # regenerate index.html, about.html, product pages
```

Then commit + push; GitHub Pages serves `main` at dylanmaudio.com.

## Files

| File | Generates | Notes |
|---|---|---|
| `common.py` | — | Shared constants (Discord/store/calendar/Web3Forms), the `PRODUCTS` data, the Discord glyph, the non-affiliation line, and `write()`. **Edit product copy, links, and the Discord URL here.** |
| `build_site.py` | `index.html` | Home. Hero, Software (Console Control flagship + utility grid + bundles), About teaser, Book, Contact, Community (Discord). |
| `build_about.py` | `about.html` | Bio, credentials, what-I-do, training, CTA. |
| `build_products.py` | `products/<slug>/index.html` | Data-driven per-product pages. |
| `build_404.py` | `404.html` | Not-found page. GitHub Pages serves it for any missing path, at any depth, so it uses site-root paths only. `noindex`, not in the sitemap. Its app links follow `build_products.BUILD`. |
| `build_redirects.py` | `<slug>/index.html` | Short links (e.g. `/discord`). Add a row to `REDIRECTS`. |

## Product pages

`build_products.py` has a `BUILD = [...]` list controlling which product pages are
generated. All products are defined in `common.PRODUCTS`; add a slug to `BUILD`
when its page is ready to ship.

- **Intro videos:** set a product's `youtube` field in `common.py` to the 11-char
  YouTube id. The page's placeholder turns into a lazy-loaded, click-to-play
  `youtube-nocookie` embed automatically (no id = "Intro video coming soon").
- **When a product page goes live,** switch its home-page card CTA from the
  `Coming soon` badge / Download link to a `Learn more →` link pointing at
  `/products/<slug>/` (in `build_site.py`).

## Short links

GitHub Pages is static — there are no server-side 301s — so `dylanmaudio.com/discord`
is a real page that bounces the browser onward via `<meta http-equiv="refresh">`
(works with JS off) plus `location.replace()` (fires sooner, and keeps the short
link out of the back-button history). A visible fallback link covers the case
where both are blocked.

Add one by adding a `slug -> (url, label)` row to `REDIRECTS` in
`build_redirects.py` and rebuilding. `/discord` reads `common.DISCORD_URL`, so
changing the invite in one place updates the site links *and* the short link.

Destinations can be external (`/discord` → discord.gg) or site-relative
(`/sessions` → `/#book`, the Sessions & consults section on the home page).
Site-relative ones are verified at build time — a missing page or a renamed
section id fails the build rather than quietly landing visitors at the top of
the home page. So if you rename a `<section id="...">` that a short link points
at, the build tells you.

Redirect pages are `noindex` and stay out of `sitemap.xml` — the destination is
what deserves indexing, not the bounce. They also skip the analytics beacon: it
loads deferred, so the redirect always wins the race and it would only add latency.

## Analytics

Cloudflare Web Analytics (cookieless, no consent banner). Paste the beacon token
into `CF_BEACON_TOKEN` in `common.py`, rebuild, and it's injected before `</body>`
on every page. Empty token = analytics off (pages build identically without it).

## SEO

`build_seo.py` writes `sitemap.xml` (only the pages in `PAGES` — live pages only)
and `robots.txt`. `common.seo_head()` adds canonical + Open Graph + Twitter + JSON-LD
to every page. `build_og.py` renders the 1200×630 share card (`assets/og-cover.png`)
— run it separately (needs Chrome) when branding changes. Parked product pages are
`noindex` and excluded from the sitemap until their slug is added to
`build_products.INDEXED` **and** `build_seo.PAGES` at launch.

## Assets

`/assets/*.png` (logo, favicons, app icons incl. `console-control.png`, the FOH
photo) are the build inputs and are committed. App icons are the 256px exports;
regenerate with `sips -z 256 256 <1024-master> --out assets/<slug>.png`.

**Brand mark / favicons:** `build_icons.py` renders `assets/logo.png` (1024) and
`favicon-16/32/180.png` from `build/assets-src/logo.svg` — the crisp white-M/bars
mark (recolored from `logo-original-black.svg`: black strokes → white, their halos
→ disc grey). Run `python3 build/build_icons.py` then `python3 build/build_og.py`
after any change to the mark. Favicons are cached hard by browsers — expect a delay
(or hard-refresh) before a changed favicon shows in the tab.

## Paths

Home and About use root-relative-to-file links (`assets/…`, `about.html`); product
pages live a folder deep and use site-root paths (`/assets/…`, `/`, `/about.html`).
All work because the site is served at the domain root.
