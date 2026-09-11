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

## Assets

`/assets/*.png` (logo, favicons, app icons incl. `console-control.png`, the FOH
photo) are the build inputs and are committed. App icons are the 256px exports;
regenerate with `sips -z 256 256 <1024-master> --out assets/<slug>.png`.

## Paths

Home and About use root-relative-to-file links (`assets/…`, `about.html`); product
pages live a folder deep and use site-root paths (`/assets/…`, `/`, `/about.html`).
All work because the site is served at the domain root.
