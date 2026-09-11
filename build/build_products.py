#!/usr/bin/env python3
"""Generate per-product pages at products/<slug>/index.html.

Data-driven from common.PRODUCTS. Set BUILD to the slugs to generate (others
are scaffolded later once their videos/copy are ready). Drop a YouTube id into a
product's `youtube` field in common.py and the facade becomes a lazy-loaded,
privacy-mode embed automatically.
"""
import common as C

# Which product pages to generate this run.
BUILD = ["midi-bridge"]

CSS = """
  :root{--bg:#0b0e12;--surface:#12171d;--surface-2:#161b21;--border:#232b34;--hairline:#1a212a;
    --text:#e6edf3;--muted:#8b949e;--dim:#5a6573;--blue:#4fa3f7;--green:#62d27a;--amber:#e89e3c;--red:#e85c5c;
    --sans:-apple-system,BlinkMacSystemFont,"SF Pro Display","SF Pro Text","Helvetica Neue",Arial,sans-serif;
    --mono:ui-monospace,"SF Mono",Menlo,Monaco,Consolas,monospace;--maxw:1120px;--pad:clamp(20px,5vw,48px);}
  *{box-sizing:border-box;} html{scroll-behavior:smooth;} html,body{margin:0;}
  body{background:var(--bg);color:var(--text);font-family:var(--sans);font-size:16px;line-height:1.6;
    -webkit-font-smoothing:antialiased;overflow-x:hidden;}
  a{color:inherit;text-decoration:none;} ::selection{background:rgba(79,163,247,0.28);}
  .wrap{max-width:var(--maxw);margin:0 auto;padding-inline:var(--pad);}
  .kicker{font-family:var(--mono);font-size:12px;letter-spacing:0.14em;text-transform:uppercase;color:var(--blue);}
  .kicker .tick{color:var(--dim);}
  /* toolbar */
  header.bar{position:sticky;top:0;z-index:50;background:rgba(11,14,18,0.82);backdrop-filter:blur(12px);
    -webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--hairline);}
  .bar-inner{max-width:var(--maxw);margin:0 auto;padding:12px var(--pad);display:flex;align-items:center;gap:20px;}
  .wordmark{font-weight:600;font-size:15px;letter-spacing:0.09em;text-transform:uppercase;display:flex;align-items:center;gap:10px;white-space:nowrap;}
  .wordmark .logo-mark{width:26px;height:26px;border-radius:50%;display:block;}
  .wordmark .br{color:var(--blue);font-weight:700;letter-spacing:0;margin:0 -0.18em;}
  .bar nav{margin-left:auto;display:flex;align-items:center;gap:6px;}
  .bar nav a{font-size:13px;color:var(--muted);padding:6px 12px;border-radius:7px;transition:color .15s,background .15s;}
  .bar nav a:hover{color:var(--text);background:var(--surface-2);} .bar nav a.active{color:var(--text);}
  .nav-icon{display:inline-flex;align-items:center;padding:6px 9px;}
  .nav-icon:hover{color:#5865F2;background:var(--surface-2);}
  .bar .store-btn{font-family:var(--mono);font-size:12px;letter-spacing:0.03em;color:var(--text);border:1px solid var(--border);
    padding:7px 13px;border-radius:8px;margin-left:6px;transition:border-color .15s,color .15s;}
  .bar .store-btn:hover{border-color:var(--blue);color:var(--blue);}
  @media (max-width:760px){.bar nav a:not(.store-btn):not(.nav-icon){display:none;}}
  /* buttons */
  .btn{display:inline-flex;align-items:center;gap:9px;font-size:14px;font-weight:500;padding:11px 18px;border-radius:9px;
    border:1px solid transparent;cursor:pointer;transition:all .15s;font-family:inherit;}
  .btn .arw{transition:transform .18s;} .btn:hover .arw{transform:translateX(3px);}
  .btn-primary{background:var(--blue);color:#06121f;font-weight:600;} .btn-primary:hover{background:#6cb4fa;}
  .btn-ghost{border-color:var(--border);color:var(--text);} .btn-ghost:hover{border-color:var(--muted);background:var(--surface);}
  .btn-discord{background:#5865F2;color:#fff;font-weight:600;} .btn-discord:hover{background:#6b76f0;}
  .btn.disabled{opacity:.55;pointer-events:none;}
  section{padding-block:clamp(52px,8vw,96px);}
  /* product hero */
  .p-hero{border-bottom:1px solid var(--hairline);position:relative;overflow:hidden;}
  .p-hero::after{content:"";position:absolute;inset:0;pointer-events:none;
    background:radial-gradient(90% 60% at 20% 0%,rgba(79,163,247,0.10),transparent 55%);}
  .p-hero-inner{position:relative;z-index:2;max-width:var(--maxw);margin:0 auto;padding:clamp(40px,6vw,64px) var(--pad) clamp(36px,5vw,56px);}
  .crumb{font-family:var(--mono);font-size:12px;color:var(--dim);display:inline-flex;gap:7px;align-items:center;letter-spacing:0.03em;}
  .crumb:hover{color:var(--blue);}
  .p-id{display:flex;align-items:center;gap:18px;margin-top:22px;}
  .p-id img{width:72px;height:72px;border-radius:16px;box-shadow:0 6px 18px rgba(0,0,0,0.45);flex-shrink:0;}
  .p-id h1{margin:0;font-size:clamp(2rem,4.6vw,3rem);letter-spacing:-0.02em;font-weight:650;}
  .p-id .abbr{color:var(--dim);font-weight:500;font-size:0.5em;margin-left:8px;letter-spacing:0.04em;}
  .p-badges{display:flex;gap:8px;margin-top:10px;flex-wrap:wrap;}
  .tag{font-family:var(--mono);font-size:10.5px;letter-spacing:0.08em;text-transform:uppercase;padding:3px 9px;border-radius:999px;
    border:1px solid color-mix(in srgb,var(--blue) 32%,var(--border));color:var(--blue);background:rgba(79,163,247,0.08);}
  .tag.free{border-color:color-mix(in srgb,var(--green) 38%,var(--border));color:var(--green);background:rgba(98,210,122,0.08);}
  .soon{font-family:var(--mono);font-size:11px;letter-spacing:0.06em;text-transform:uppercase;color:var(--amber);
    border:1px solid color-mix(in srgb,var(--amber) 38%,var(--border));background:rgba(232,158,60,0.09);border-radius:999px;padding:4px 10px;}
  .p-tagline{margin:24px 0 0;max-width:56ch;font-size:clamp(1.15rem,2vw,1.4rem);line-height:1.4;color:var(--text);}
  .p-cta-row{margin-top:30px;display:flex;flex-wrap:wrap;gap:12px;align-items:center;}
  /* video */
  .video-wrap{max-width:var(--maxw);margin:0 auto;padding-inline:var(--pad);}
  .video-frame{position:relative;aspect-ratio:16/9;border-radius:16px;overflow:hidden;border:1px solid var(--border);
    background:linear-gradient(180deg,#10151b,#0b0e12);}
  .video-frame iframe{position:absolute;inset:0;width:100%;height:100%;border:0;}
  .video-facade{position:absolute;inset:0;display:grid;place-items:center;cursor:pointer;}
  .video-facade img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}
  .video-facade .play{position:relative;z-index:2;width:76px;height:76px;border-radius:50%;display:grid;place-items:center;
    background:rgba(11,14,18,0.7);border:1px solid rgba(255,255,255,0.25);backdrop-filter:blur(4px);}
  .video-facade .play svg{width:30px;height:30px;fill:#fff;margin-left:4px;}
  .video-soon{position:absolute;inset:0;display:flex;flex-direction:column;gap:14px;align-items:center;justify-content:center;color:var(--dim);}
  .video-soon .ring{width:64px;height:64px;border-radius:50%;border:1px solid var(--border);display:grid;place-items:center;color:var(--muted);}
  .video-soon .ring svg{width:26px;height:26px;fill:currentColor;margin-left:3px;}
  .video-soon .lbl{font-family:var(--mono);font-size:12px;letter-spacing:0.08em;text-transform:uppercase;}
  /* overview */
  .p-grid{display:grid;grid-template-columns:1.1fr 0.9fr;gap:clamp(28px,5vw,60px);align-items:start;}
  @media (max-width:820px){.p-grid{grid-template-columns:1fr;gap:28px;}}
  .p-lead{font-size:1.14rem;line-height:1.55;color:var(--text);margin:0 0 22px;}
  .p-body p{color:var(--muted);margin:0 0 16px;max-width:60ch;}
  .p-sec-k{margin-bottom:16px;}
  .feature-list{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:14px;}
  .feature-list li{display:flex;gap:12px;align-items:flex-start;color:var(--text);font-size:0.98rem;}
  .feature-list .ck{color:var(--green);flex-shrink:0;margin-top:2px;}
  .feature-list .ck svg{width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:2.4;}
  .side{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:22px;font-family:var(--mono);font-size:13px;}
  .side .h{color:var(--dim);font-size:11px;letter-spacing:0.1em;text-transform:uppercase;padding-bottom:12px;margin-bottom:12px;border-bottom:1px solid var(--hairline);}
  .srow{display:flex;justify-content:space-between;gap:14px;padding:6px 0;}
  .srow .k{color:var(--dim);} .srow .v{color:var(--text);text-align:right;} .srow .v.g{color:var(--green);}
  .chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:14px;}
  .chips .spec{font-family:var(--mono);font-size:11px;color:var(--dim);border:1px solid var(--hairline);border-radius:6px;padding:3px 8px;background:var(--bg);}
  /* cta band */
  .p-band{border-top:1px solid var(--hairline);text-align:center;}
  .p-band h2{font-size:clamp(1.6rem,3.4vw,2.3rem);letter-spacing:-0.02em;font-weight:640;margin:14px 0 0;text-wrap:balance;}
  .p-band p{color:var(--muted);margin:14px auto 0;max-width:46ch;}
  .p-band .p-cta-row{justify-content:center;}
  /* footer */
  footer.site{border-top:1px solid var(--hairline);padding:34px var(--pad);}
  .foot-inner{max-width:var(--maxw);margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;font-size:13px;color:var(--dim);}
  .foot-inner .fl{display:flex;gap:20px;flex-wrap:wrap;} .foot-inner a:hover{color:var(--text);}
  .foot-inner .fl .di:hover{color:#5865F2;}
  .foot-mono{font-family:var(--mono);font-size:12px;}
  .foot-legal{max-width:78ch;margin:20px auto 0;padding-top:18px;border-top:1px solid var(--hairline);font-size:11.5px;line-height:1.5;color:var(--dim);}
  @media (prefers-reduced-motion:reduce){*{animation:none!important;scroll-behavior:auto!important;}}
"""

def nav(active="software"):
    def cls(k): return ' class="active"' if k == active else ""
    return f"""<header class="bar">
  <div class="bar-inner">
    <a href="/" class="wordmark"><img class="logo-mark" src="/assets/logo.png" alt="" width="26" height="26" /> Dylan <span class="br">[M]</span> Audio</a>
    <nav>
      <a href="/#software"{cls('software')}>Software</a>
      <a href="/about.html"{cls('about')}>About</a>
      <a href="/#book">Book</a>
      <a href="/#contact">Contact</a>
      <a href="{C.DISCORD_URL}" class="nav-icon" aria-label="Join the Discord" target="_blank" rel="noopener">{C.DISCORD_SVG}</a>
      <a href="{C.STORE_URL}" class="store-btn">Store&nbsp;&#8599;</a>
    </nav>
  </div>
</header>"""

FOOTER = f"""<footer class="site">
  <div class="foot-inner">
    <div class="wordmark"><img class="logo-mark" src="/assets/logo.png" alt="" width="26" height="26" /> Dylan <span class="br">[M]</span> Audio</div>
    <div class="fl"><a href="/#software">Software</a><a href="/about.html">About</a><a href="/#book">Book</a><a href="/#contact">Contact</a><a class="di" href="{C.DISCORD_URL}" target="_blank" rel="noopener">Discord</a><a href="{C.STORE_URL}">Store &#8599;</a></div>
    <div class="foot-mono">&copy; 2026 Dylan Mitrovich</div>
  </div>
  <div class="foot-legal">{C.NONAFFIL}</div>
</footer>"""

CK = '<span class="ck"><svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></span>'
PLAY = '<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>'


def video_block(p):
    if p["youtube"]:
        yt = p["youtube"]
        facade = (f'<div class="video-facade" data-yt="{yt}" role="button" tabindex="0" aria-label="Play intro video">'
                  f'<img src="https://i.ytimg.com/vi/{yt}/maxresdefault.jpg" alt="{p["name"]} intro video" loading="lazy" />'
                  f'<span class="play">{PLAY}</span></div>')
    else:
        facade = (f'<div class="video-soon"><span class="ring">{PLAY}</span>'
                  f'<span class="lbl">Intro video coming soon</span></div>')
    return f'<section><div class="video-wrap"><div class="video-frame">{facade}</div></div></section>'


def hero_cta(p):
    if p["status"] == "free":
        return (f'<a href="{p["store"]}" class="btn btn-primary">Download &mdash; Free <span class="arw">&rarr;</span></a>'
                f'<a href="{C.DISCORD_URL}" class="btn btn-discord" target="_blank" rel="noopener">{C.DISCORD_SVG} Get help</a>')
    if p["status"] == "buy":
        return f'<a href="{p["store"]}" class="btn btn-primary">View in store <span class="arw">&rarr;</span></a>'
    # coming
    return ('<span class="btn btn-ghost disabled">Coming soon</span>'
            f'<a href="{C.DISCORD_URL}" class="btn btn-discord" target="_blank" rel="noopener">{C.DISCORD_SVG} Get notified</a>')


def band(p):
    if p["status"] == "free":
        h, sub = f"{p['name']} is free.", "Download it, and drop into the Discord if you hit a snag or have a request."
        cta = (f'<a href="{p["store"]}" class="btn btn-primary">Download &mdash; Free <span class="arw">&rarr;</span></a>'
               f'<a href="{C.DISCORD_URL}" class="btn btn-discord" target="_blank" rel="noopener">{C.DISCORD_SVG} Join the Discord</a>')
    else:
        h, sub = f"{p['name']} is coming soon.", "Join the Discord to hear the moment it lands — and help shape it."
        cta = (f'<a href="{C.DISCORD_URL}" class="btn btn-discord" target="_blank" rel="noopener">{C.DISCORD_SVG} Get notified</a>'
               f'<a href="/#contact" class="btn btn-ghost">Contact</a>')
    return (f'<section class="p-band"><div class="wrap"><div class="kicker" style="display:inline-block;">'
            f'<span class="tick">//</span>&nbsp; {p["name"]}</div><h2>{h}</h2><p>{sub}</p>'
            f'<div class="p-cta-row">{cta}</div></div></section>')


def status_row(p):
    if p["status"] == "free":
        return '<div class="srow"><span class="k">Price</span><span class="v g">Free</span></div>'
    if p["status"] == "buy":
        return '<div class="srow"><span class="k">Price</span><span class="v">In store</span></div>'
    return '<div class="srow"><span class="k">Status</span><span class="v">Coming soon</span></div>'


def build_page(slug, p):
    tagcls = " free" if p["tag"] == "Free" else ""
    abbr = f'<span class="abbr">{p["abbr"]}</span>' if p["abbr"] else ""
    features = "".join(f'<li>{CK}<span>{f}</span></li>' for f in p["features"])
    chips = "".join(f'<span class="spec">{s}</span>' for s in p["specs"])
    trial = ('<div class="srow"><span class="k">Trial</span><span class="v">20-min sessions</span></div>'
             if p["status"] != "free" else "")
    affil = ("" if p["affiliated"] is False else
             '<div class="srow"><span class="k">Maker</span><span class="v">dylanmaudio</span></div>')

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="description" content="{p['name']} — {p['tagline']}">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon-16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/favicon-180.png">
<link rel="icon" href="/assets/logo.png">
<title>{p['name']} — Dylan [M] Audio</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<style>{CSS}</style>
</head>
<body class="product">
{nav("software")}

<section class="p-hero">
  <div class="p-hero-inner">
    <a class="crumb" href="/#software">&larr; All software</a>
    <div class="p-id">
      <img src="/assets/{p['icon']}" alt="{p['name']} app icon" width="72" height="72" />
      <div>
        <h1>{p['name']}{abbr}</h1>
        <div class="p-badges"><span class="tag{tagcls}">{p['tag']}</span></div>
      </div>
    </div>
    <p class="p-tagline">{p['tagline']}</p>
    <div class="p-cta-row">{hero_cta(p)}</div>
  </div>
</section>

{video_block(p)}

<section><div class="wrap p-grid">
  <div class="p-body">
    <div class="kicker p-sec-k"><span class="tick">//</span>&nbsp; What it does</div>
    <p class="p-lead">{p['lead']}</p>
  </div>
  <div>
    <ul class="feature-list">{features}</ul>
    <div class="side" style="margin-top:24px;">
      <div class="h">// At a glance</div>
      {status_row(p)}
      <div class="srow"><span class="k">Platform</span><span class="v">macOS 11+</span></div>
      <div class="srow"><span class="k">Chip</span><span class="v">Apple Silicon</span></div>
      {trial}
      {affil}
      <div class="chips">{chips}</div>
    </div>
  </div>
</div></section>

{band(p)}

{FOOTER}

<script>
  // Lazy-load the YouTube embed only when the facade is activated.
  document.querySelectorAll(".video-facade[data-yt]").forEach(function (f) {{
    function load() {{
      var id = f.getAttribute("data-yt");
      var ifr = document.createElement("iframe");
      ifr.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0";
      ifr.title = "Intro video";
      ifr.allow = "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture";
      ifr.allowFullscreen = true;
      f.parentNode.replaceChild(ifr, f);
    }}
    f.addEventListener("click", load);
    f.addEventListener("keydown", function (e) {{ if (e.key === "Enter" || e.key === " ") {{ e.preventDefault(); load(); }} }});
  }});
</script>
</body>
</html>"""
    C.write(f"products/{slug}/index.html", html)


if __name__ == "__main__":
    for slug in BUILD:
        build_page(slug, C.PRODUCTS[slug])
