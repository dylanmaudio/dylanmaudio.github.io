#!/usr/bin/env python3
"""Generate the not-found page -> 404.html.

GitHub Pages serves a root-level 404.html (with a 404 status) for any path that
doesn't exist, at any depth — so every link and asset here uses a site-root
path (/assets/…, /about.html), never a relative one. The page is noindex and
stays out of sitemap.xml.

The product links come from build_products.BUILD, so a page that isn't live
(Console Control until launch) is never offered here.
"""
import common as C
import build_products as P

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex, follow">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon-16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/favicon-180.png">
<link rel="icon" href="/assets/logo.png">
<title>Page not found — Dylan [M] Audio</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<style>
  :root {
    --bg:#0b0e12; --surface:#12171d; --surface-2:#161b21; --border:#232b34; --hairline:#1a212a;
    --text:#e6edf3; --muted:#8b949e; --dim:#5a6573;
    --blue:#4fa3f7; --green:#62d27a; --amber:#e89e3c; --red:#e85c5c; --blue-soft:rgba(79,163,247,0.10);
    --sans:-apple-system,BlinkMacSystemFont,"SF Pro Display","SF Pro Text","Helvetica Neue",Arial,sans-serif;
    --mono:ui-monospace,"SF Mono",Menlo,Monaco,Consolas,monospace;
    --maxw:1120px; --pad:clamp(20px,5vw,48px);
  }
  * { box-sizing:border-box; }
  html,body { margin:0; }
  body { background:var(--bg); color:var(--text); font-family:var(--sans); font-size:16px; line-height:1.6;
    -webkit-font-smoothing:antialiased; text-rendering:optimizeLegibility; overflow-x:hidden;
    min-height:100vh; display:flex; flex-direction:column; }
  a { color:inherit; text-decoration:none; }
  ::selection { background:rgba(79,163,247,0.28); }
  .kicker { font-family:var(--mono); font-size:12px; letter-spacing:0.14em; text-transform:uppercase; color:var(--blue); }
  .kicker .tick { color:var(--dim); }

  /* Toolbar */
  header.bar { position:sticky; top:0; z-index:50; background:rgba(11,14,18,0.82);
    backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px); border-bottom:1px solid var(--hairline); }
  .bar-inner { max-width:var(--maxw); margin:0 auto; padding:12px var(--pad); display:flex; align-items:center; gap:20px; }
  .wordmark { font-weight:600; font-size:15px; letter-spacing:0.09em; text-transform:uppercase; display:flex; align-items:center; gap:10px; white-space:nowrap; }
  .wordmark .logo-mark { width:26px; height:26px; border-radius:50%; display:block; }
  .wordmark .br { color:var(--blue); font-weight:700; letter-spacing:0; margin:0 -0.18em; }
  .bar nav { margin-left:auto; display:flex; align-items:center; gap:6px; }
  .bar nav a { font-size:13px; color:var(--muted); padding:6px 12px; border-radius:7px; transition:color .15s, background .15s; }
  .bar nav a:hover { color:var(--text); background:var(--surface-2); }
  .nav-icon { display:inline-flex; align-items:center; padding:6px 9px; }
  .nav-icon:hover { color:#5865F2; background:var(--surface-2); }
  .bar .store-btn { font-family:var(--mono); font-size:12px; letter-spacing:0.03em; color:var(--text);
    border:1px solid var(--border); padding:7px 13px; border-radius:8px; margin-left:6px; transition:border-color .15s, color .15s; }
  .bar .store-btn:hover { border-color:var(--blue); color:var(--blue); }
  @media (max-width:760px) { .bar nav a:not(.store-btn):not(.nav-icon) { display:none; } }

  /* Not found */
  main { flex:1; display:flex; align-items:center; position:relative; overflow:hidden; }
  main::after { content:""; position:absolute; inset:0; pointer-events:none;
    background:radial-gradient(90% 60% at 15% 0%, rgba(79,163,247,0.10), transparent 55%); }
  .nf { position:relative; z-index:2; width:100%; max-width:var(--maxw); margin:0 auto; padding:clamp(56px,9vw,104px) var(--pad); }
  .nf .code { font-family:var(--mono); font-size:clamp(4rem,14vw,8.5rem); line-height:1; letter-spacing:-0.04em;
    font-weight:600; color:#1b222b; -webkit-text-stroke:1px #33404d; margin:18px 0 0; }
  .nf h1 { font-size:clamp(1.9rem,4.2vw,2.9rem); line-height:1.1; letter-spacing:-0.02em; font-weight:650; margin:18px 0 0; text-wrap:balance; }
  .nf .lede { margin:16px 0 0; max-width:54ch; color:var(--muted); font-size:clamp(1.02rem,1.5vw,1.16rem); }
  .nf .path { font-family:var(--mono); font-size:13px; color:var(--dim); margin:14px 0 0; word-break:break-all; }
  .nf .path b { color:var(--muted); font-weight:500; }
  .cta-row { margin-top:30px; display:flex; flex-wrap:wrap; gap:12px; }

  .btn { display:inline-flex; align-items:center; gap:9px; font-size:14px; font-weight:500; padding:11px 18px;
    border-radius:9px; border:1px solid transparent; cursor:pointer; transition:all .15s; font-family:inherit; }
  .btn .arw { transition:transform .18s; }
  .btn:hover .arw { transform:translateX(3px); }
  .btn-primary { background:var(--blue); color:#06121f; font-weight:600; }
  .btn-primary:hover { background:#6cb4fa; }
  .btn-ghost { border-color:var(--border); color:var(--text); }
  .btn-ghost:hover { border-color:var(--muted); background:var(--surface); }

  /* Product shortcuts */
  .apps { margin-top:44px; padding-top:26px; border-top:1px solid var(--hairline); }
  .app-row { margin-top:14px; display:flex; flex-wrap:wrap; gap:10px; }
  .app { display:inline-flex; align-items:center; gap:10px; background:var(--surface); border:1px solid var(--border);
    border-radius:999px; padding:6px 14px 6px 6px; font-size:14px; transition:border-color .18s, transform .18s; }
  .app:hover { border-color:color-mix(in srgb, var(--blue) 45%, var(--border)); transform:translateY(-2px); }
  .app img { width:26px; height:26px; border-radius:7px; display:block; }

  footer.site { border-top:1px solid var(--hairline); padding:34px var(--pad); }
  .foot-inner { max-width:var(--maxw); margin:0 auto; display:flex; align-items:center; justify-content:space-between; gap:16px; flex-wrap:wrap; font-size:13px; color:var(--dim); }
  .foot-inner .fl { display:flex; gap:20px; flex-wrap:wrap; }
  .foot-inner a:hover { color:var(--text); }
  .foot-inner .fl .di:hover { color:#5865F2; }
  .foot-mono { font-family:var(--mono); font-size:12px; }
  .foot-legal { max-width:78ch; margin:20px auto 0; padding-top:18px; border-top:1px solid var(--hairline); font-size:11.5px; line-height:1.5; color:var(--dim); }

  @media (prefers-reduced-motion:reduce) { *{animation:none !important; transition:none !important;} }
</style>
</head>
<body>
<header class="bar">
  <div class="bar-inner">
    <a href="/" class="wordmark"><img class="logo-mark" src="/assets/logo.png" alt="" width="26" height="26" /> Dylan <span class="br">[M]</span> Audio</a>
    <nav>
      <a href="/#software">Software</a>
      <a href="/about.html">About</a>
      <a href="/#book">Book</a>
      <a href="/#contact">Contact</a>
      <a href="__DISCORD_URL__" class="nav-icon" aria-label="Join the Discord" target="_blank" rel="noopener">__DISCORD_SVG__</a>
      <a href="__STORE_URL__" class="store-btn">Store&nbsp;&#8599;</a>
    </nav>
  </div>
</header>

<main>
  <div class="nf">
    <div class="kicker"><span class="tick">//</span>&nbsp; No signal</div>
    <div class="code" aria-hidden="true">404</div>
    <h1>Nothing patched to this address.</h1>
    <p class="lede">The page you&rsquo;re after has moved, been renamed, or never existed. The software, booking and contact are all a click away.</p>
    <p class="path" id="nf-path" hidden><b>Requested:</b> <span></span></p>
    <div class="cta-row">
      <a href="/" class="btn btn-primary">Back to home <span class="arw">&rarr;</span></a>
      <a href="/#software" class="btn btn-ghost">Explore the software</a>
      <a href="/#contact" class="btn btn-ghost">Report a broken link</a>
    </div>
    <div class="apps">
      <div class="kicker"><span class="tick">//</span>&nbsp; Looking for an app?</div>
      <div class="app-row">
__APPS__
      </div>
    </div>
  </div>
</main>

<footer class="site">
  <div class="foot-inner">
    <div class="wordmark"><img class="logo-mark" src="/assets/logo.png" alt="" width="26" height="26" /> Dylan <span class="br">[M]</span> Audio</div>
    <div class="fl"><a href="/#software">Software</a><a href="/about.html">About</a><a href="/#book">Book</a><a href="/#contact">Contact</a><a class="di" href="__DISCORD_URL__" target="_blank" rel="noopener">Discord</a><a href="__STORE_URL__">Store &#8599;</a></div>
    <div class="foot-mono">&copy; 2026 Dylan Mitrovich</div>
  </div>
  <div class="foot-legal">__NONAFFIL__</div>
</footer>
<script>(function(){var p=document.getElementById('nf-path');if(!p)return;
p.querySelector('span').textContent=location.pathname;p.hidden=false;})();</script>
</body>
</html>"""


def apps():
    return "\n".join(
        f'        <a class="app" href="/products/{slug}/"><img src="/assets/{C.PRODUCTS[slug]["icon"]}" '
        f'alt="" width="26" height="26" />{C.PRODUCTS[slug]["name"]}</a>'
        for slug in P.BUILD
    )


def build():
    # The in-page anchors the 404 sends people to live on the home page.
    home = (C.ROOT / "index.html").read_text(encoding="utf-8")
    for frag in ("software", "book", "contact"):
        if f'id="{frag}"' not in home:
            raise SystemExit(f'404 page links to /#{frag}, but index.html has no id="{frag}"')
    out = (HTML.replace("__APPS__", apps())
               .replace("__DISCORD_URL__", C.DISCORD_URL)
               .replace("__DISCORD_SVG__", C.DISCORD_SVG)
               .replace("__STORE_URL__", C.STORE_URL)
               .replace("__NONAFFIL__", C.NONAFFIL))
    C.write("404.html", C.inject_analytics(out))


if __name__ == "__main__":
    build()
