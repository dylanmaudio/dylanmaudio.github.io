#!/usr/bin/env python3
"""Generate short-link redirect pages -> <slug>/index.html.

GitHub Pages serves static files only — there are no server-side 301s — so a
short link is a tiny HTML page that bounces the browser onward. Each one uses
a <meta http-equiv="refresh"> (works with JS off) plus location.replace() (fires
sooner and keeps the short link out of the back-button history), and carries a
visible fallback link in case both are blocked.

Redirect pages are noindex and stay out of sitemap.xml: the destination is the
page worth indexing, not the bounce. No analytics beacon either — it loads
deferred, so the redirect always wins the race and it would only cost latency.

Add a short link by adding a row to REDIRECTS below, then rebuild.
"""
import common as C

# slug -> (destination URL, human label shown for the half-second it renders)
# Site-relative destinations ("/", "/#book", "/about.html") are checked below
# against the generated HTML, so a renamed section id breaks the build instead
# of silently dumping visitors at the top of the page.
REDIRECTS = {
    "discord":  (C.DISCORD_URL, "the dylanmaudio Discord"),
    "sessions": ("/#book", "sessions &amp; consults"),
}

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, follow">
<meta http-equiv="refresh" content="0; url=__DEST__">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon-16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/favicon-180.png">
<link rel="icon" href="/assets/logo.png">
<title>Redirecting to __LABEL__ — Dylan [M] Audio</title>
<style>
  :root { --bg:#0b0e12; --text:#e6edf3; --muted:#8b949e; --blue:#4fa3f7;
    --sans:-apple-system,BlinkMacSystemFont,"SF Pro Display","SF Pro Text","Helvetica Neue",Arial,sans-serif;
    --mono:ui-monospace,"SF Mono",Menlo,Monaco,Consolas,monospace; }
  html,body { margin:0; height:100%; }
  body { background:var(--bg); color:var(--text); font-family:var(--sans); font-size:16px;
    -webkit-font-smoothing:antialiased; display:flex; align-items:center; justify-content:center;
    text-align:center; padding:24px; }
  .logo-mark { width:44px; height:44px; border-radius:50%; display:block; margin:0 auto 20px; }
  .kicker { font-family:var(--mono); font-size:12px; letter-spacing:0.14em; text-transform:uppercase;
    color:var(--blue); margin:0 0 10px; }
  p { margin:0; color:var(--muted); line-height:1.6; }
  a { color:var(--blue); text-decoration:none; }
  a:hover { text-decoration:underline; }
</style>
</head>
<body>
<main>
  <img class="logo-mark" src="/assets/logo.png" alt="" width="44" height="44">
  <p class="kicker">Redirecting</p>
  <p>Taking you to __LABEL__.<br>
  Not moving? <a href="__DEST__" rel="noopener">Open it here</a>.</p>
</main>
<script>location.replace("__DEST__");</script>
</body>
</html>
"""


def check_internal(dest: str):
    """Fail the build if a site-relative destination (or its #anchor) is missing."""
    path, _, frag = dest.lstrip("/").partition("#")
    target = C.ROOT / (path or "index.html")
    if target.is_dir():
        target = target / "index.html"
    if not target.exists():
        raise SystemExit(f"redirect target missing: {dest} -> {target}")
    if frag and f'id="{frag}"' not in target.read_text(encoding="utf-8"):
        raise SystemExit(f"redirect anchor missing: {dest} (no id=\"{frag}\" in {target.name})")


def build():
    for slug, (dest, label) in REDIRECTS.items():
        if dest.startswith("/"):
            check_internal(dest)
        html = (HTML.replace("__DEST__", dest).replace("__LABEL__", label))
        C.write(f"{slug}/index.html", html)


if __name__ == "__main__":
    build()
