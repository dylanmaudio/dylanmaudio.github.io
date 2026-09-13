#!/usr/bin/env python3
"""Render the 1200x630 social share image -> assets/og-cover.png.

Self-contained: base64-embeds the logo + app icons and rasterises with headless
Chrome (no server needed). Re-run whenever the branding or line-up changes.
"""
import base64, pathlib, subprocess, tempfile
import common as C

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ASSETS = C.ROOT / "assets"
ICONS = ["console-control.png", "midi-bridge.png", "talk-light-trigger.png",
         "pilot-tone-trigger.png", "time-code-tool.png"]

def uri(name):
    return "data:image/png;base64," + base64.b64encode((ASSETS / name).read_bytes()).decode()

def build():
    logo = uri("logo.png")
    icons = "".join(f'<img class="ic" src="{uri(n)}">' for n in ICONS)
    html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
      *{{margin:0;padding:0;box-sizing:border-box;}}
      html,body{{width:1200px;height:630px;overflow:hidden;}}
      body{{background:radial-gradient(900px 520px at 50% -12%,rgba(79,163,247,0.18),transparent 60%),#0b0e12;
        font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display","Helvetica Neue",Arial,sans-serif;
        color:#e6edf3;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;position:relative;}}
      .frame{{position:absolute;inset:40px;border:1px solid #202832;border-radius:26px;}}
      .wm{{display:flex;align-items:center;gap:20px;}}
      .wm img{{width:84px;height:84px;border-radius:50%;}}
      .wm .t{{font-size:52px;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;}}
      .wm .br{{color:#4fa3f7;font-weight:700;margin:0 -0.18em;letter-spacing:0;}}
      .tag{{margin-top:38px;font-size:38px;color:#aeb6c0;font-weight:400;max-width:900px;line-height:1.3;}}
      .tag b{{color:#4fa3f7;font-weight:500;}}
      .icons{{margin-top:52px;display:flex;gap:22px;}}
      .icons .ic{{width:76px;height:76px;border-radius:18px;filter:drop-shadow(0 12px 24px rgba(0,0,0,0.5));}}
      .url{{position:absolute;bottom:66px;font-family:ui-monospace,"SF Mono",Menlo,monospace;font-size:22px;color:#5a6573;letter-spacing:0.06em;}}
    </style></head><body>
      <div class="frame"></div>
      <div class="wm"><img src="{logo}"><span class="t">Dylan <span class="br">[M]</span> Audio</span></div>
      <div class="tag">macOS software for the Allen&nbsp;&amp;&nbsp;Heath <b>dLive</b></div>
      <div class="icons">{icons}</div>
      <div class="url">dylanmaudio.com</div>
    </body></html>"""

    tmp = pathlib.Path(tempfile.gettempdir()) / "og-cover.html"
    tmp.write_text(html, encoding="utf-8")
    out = ASSETS / "og-cover.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=1", "--window-size=1200,630",
                    f"--screenshot={out}", f"file://{tmp}"], check=True, capture_output=True)
    tmp.unlink(missing_ok=True)
    print("wrote", out.relative_to(C.ROOT))


if __name__ == "__main__":
    build()
