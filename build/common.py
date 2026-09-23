#!/usr/bin/env python3
"""Shared constants, data, and snippets for the dylanmaudio.com build.

The site is a static, hand-built set of pages. These builders regenerate the
deployed HTML so we never hand-edit the live files directly:

    python3 build/build_all.py     # regenerate everything

Individual builders: build_site.py (home / index.html), build_about.py
(about.html), build_products.py (products/<slug>/index.html).

Design system: dark "instrument-panel" theme, signal-blue accent, the app icons
carry each product's identity. Assets live in /assets and are committed to the
repo (no machine-specific paths), so the build is fully reproducible anywhere.
"""
import json, pathlib

# Repo root = parent of this build/ dir.
ROOT = pathlib.Path(__file__).resolve().parent.parent

# Canonical origin + default share image (used for canonical/OG/sitemap URLs).
SITE_ROOT = "https://dylanmaudio.com"
OG_IMAGE = "assets/og-cover.png"

# --- External services (all public, client-side values) -------------------
DISCORD_URL = "https://discord.gg/zBkPrFhzPQ"
STORE_URL   = "https://store.dylanmaudio.com"
CAL_EMBED   = ("https://calendar.google.com/calendar/appointments/schedules/"
               "AcZssZ0Prpa4yII9D6-eGZGCb-r9gg77xCxOY7JvN0Ds3sARHqH1IINad7mVj0CnI7B6Bieymq1_PFd-?gv=true")
WEB3FORMS_KEY = "d869112c-0f00-4e71-99bb-8bcd1cfe9bf2"

# Lemon Squeezy checkout URLs (per product).
CHECKOUT = {
    "midi-bridge": f"{STORE_URL}/checkout/buy/77778860-577c-4fc6-9f84-59e78db1539b",
    "talk-light-trigger": f"{STORE_URL}/checkout/buy/5700dc17-83ae-4e2a-8534-29eaddbf51b6",
    "pilot-tone-trigger": f"{STORE_URL}/checkout/buy/f1b17f98-2bed-4bef-be31-bf1f0cfb2c5d",
    "time-code-tool": f"{STORE_URL}/checkout/buy/52a61e9a-34cd-4ee7-88ca-c859e14fd365",
    # Bundles
    "dlive-menubar": f"{STORE_URL}/checkout/buy/f6c14f2a-d9f6-4d0f-adbd-9eafec887950",  # TLT+PTT (+free Bridge)
    "all-menubar": f"{STORE_URL}/checkout/buy/7ce181d1-c1c1-4607-8389-88744e958f46",    # + Time Code Tool
}

# Discord glyph (inline SVG, uses currentColor).
DISCORD_SVG = ('<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true">'
               '<path d="M20.317 4.369A19.79 19.79 0 0 0 15.885 3c-.21.375-.45.882-.617 1.283a18.27 18.27 0 0 0-5.535 0'
               'A12.6 12.6 0 0 0 9.11 3 19.74 19.74 0 0 0 4.677 4.37C1.9 8.48 1.14 12.49 1.52 16.44a19.9 19.9 0 0 0 '
               '6.05 3.06c.49-.67.925-1.38 1.3-2.13-.716-.27-1.4-.605-2.045-.998.171-.126.34-.257.5-.39a14.2 14.2 0 0 0 '
               '12.35 0c.163.14.332.27.5.39-.646.394-1.333.728-2.048.998.375.75.81 1.46 1.3 2.13a19.87 19.87 0 0 0 '
               '6.053-3.06c.447-4.58-.766-8.55-3.212-12.07ZM8.02 14.01c-1.183 0-2.157-1.085-2.157-2.42 0-1.336.955-2.42 '
               '2.157-2.42 1.21 0 2.176 1.094 2.157 2.42 0 1.335-.955 2.42-2.157 2.42Zm7.96 0c-1.182 0-2.156-1.085-2.156-2.42 '
               '0-1.336.955-2.42 2.157-2.42 1.21 0 2.176 1.094 2.157 2.42 0 1.335-.946 2.42-2.157 2.42Z"/></svg>')

# --- Products (drives the per-product pages) --------------------------------
# youtube = None until an intro video exists (then set the 11-char video id).
# status: "free" | "coming" | "buy". store = checkout URL or None.
PRODUCTS = {
    "console-control": dict(
        name="Console Control", abbr="", tag="Flagship", accent="blue",
        icon="console-control.png", affiliated=True, status="coming", store=None, youtube=None,
        tagline="A complete timeline-based automation control platform for the dLive.",
        lead=("Console Control turns show automation into a timeline you can see. Lay cues, moves and "
              "recalls on a scrubber-driven timeline, rehearse them against the desk, and fire the whole "
              "show with frame-accurate confidence — a proper automation platform, not a pile of scenes."),
        features=[
            "Timeline-based cue &amp; automation sequencing",
            "Drives the dLive live, in sync with your show",
            "Rehearse, scrub and refine before showtime",
            "Built by a working FOH engineer",
        ],
        specs=["timeline", "automation", "show control", "dLive"],
    ),
    "midi-bridge": dict(
        name="MIDI Bridge", abbr="FREE", tag="Free", accent="green",
        icon="midi-bridge.png", affiliated=True, status="free",
        store=CHECKOUT["midi-bridge"], youtube="2M57Z-v7fs0",
        tagline="Bridge MIDI to your dLive over TCP, with a live decoded message monitor.",
        lead=("MIDI Bridge carries MIDI over TCP to and from your dLive, and ships with a live, decoded "
              "message monitor — every fader, mute and scene crossing the wire in plain language, with "
              "real console descriptions instead of raw MIDI bytes. Free, and the foundation the other apps "
              "build on."),
        features=[
            "MIDI over TCP, to and from the console",
            "Live decoded monitor — real console descriptions, not raw MIDI bytes",
            "Advanced monitor mode for protocol-level detail",
            "At-a-glance menu-bar status indicator",
            "Free — no licence, no trial timer",
        ],
        specs=["MIDI over TCP", "live monitor", "advanced monitor", "menu-bar status", "free"],
    ),
    "talk-light-trigger": dict(
        name="Talk Light Trigger", abbr="TLT", tag="dLive", accent="blue",
        icon="talk-light-trigger.png", affiliated=True, status="buy", trial=True, price="$19",
        store=CHECKOUT["talk-light-trigger"], youtube="jP2Yyvd1uq4",
        sale=dict(now="$9", was="$19", code="TLTINTROSALE",
                  until="2026-10-31", until_label="31 October 2026"),
        tagline="Turn a console channel into a hands-free talkback / cue light.",
        lead=("Talk Light Trigger watches a dLive channel and fires a talkback / cue light the instant "
              "signal crosses your threshold — hands-free tally for the podium, the pit, or the booth, "
              "using the console's own light and no extra hardware."),
        features=[
            "Threshold trigger on any dLive channel",
            "Fires the console's own talkback / cue light — no extra hardware",
            "Set-and-forget menu-bar app",
            "Full-featured 20-minute trial",
        ],
        specs=["signal → trigger", "tally", "menu bar"],
    ),
    "pilot-tone-trigger": dict(
        name="Pilot Tone Trigger", abbr="PTT", tag="dLive", accent="blue",
        icon="pilot-tone-trigger.png", affiliated=True, status="buy", trial=True, price="$59",
        store=CHECKOUT["pilot-tone-trigger"], youtube="GOfFZzGTEuA",
        tagline="Detects a dropped pilot tone and recalls your backup scene — automatically.",
        lead=("Pilot Tone Trigger listens for a pilot tone on any critical audio path and drives automatic "
              "failover the instant it drops — for playback rigs and external processing (Waves and similar) "
              "alike. You've already built the backup scene; PTT recalls it before the audience hears the gap."),
        features=[
            "Detects loss of pilot tone on any critical path",
            "Auto-recalls your backup scene on the console",
            "Fails safe — never leaves the console mid-switch",
            "Full-featured 20-minute trial",
        ],
        specs=["tone detect", "auto-failover", "Waves failover"],
    ),
    "time-code-tool": dict(
        name="Time Code Tool", abbr="TxT", tag="Universal", accent="blue",
        icon="time-code-tool.png", affiliated=False, status="buy", trial=True, price="$69",
        store=CHECKOUT["time-code-tool"], youtube="A6iKjxHxXA4",
        # Search-facing title/description (the page <title> and meta description).
        seo_title="Time Code Tool — LTC &amp; MTC reader and converter for Mac",
        seo_desc=("Read, monitor, convert and generate LTC and MTC timecode on a Mac. LTC to MTC, "
                  "MTC to LTC, frame-rate conversion, LTC to WAV. Free 20-minute trial."),
        tagline="Read, check, convert and generate timecode on your Mac.",
        lead=("An LTC and MTC reader, converter and generator that does the job of a rack timecode "
              "clock — and shows you what your timecode is actually doing. Read incoming LTC or MTC and "
              "see exactly how healthy it is; send it on clean as LTC, MTC or both, at the same frame "
              "rate or a different one; or run it as the timecode master and render sample-accurate "
              "LTC to a WAV. A far steadier endpoint than piping LTC straight into a DAW. Works with "
              "any console."),
        features=[
            "Read + monitor LTC or MTC — lock, frame rate, freewheel, missed / misread / jumped frames",
            "Convert in any direction — LTC → MTC, MTC → LTC, LTC → LTC, MTC → MTC — or both outputs at once",
            "Frame-rate conversion on either output (23.976 / 24 / 25 / 29.97 DF / NDF / 30)",
            "Generate mode — LTC and MTC from one clock; render sample-accurate LTC to a WAV",
            "Virtual audio and MIDI ports, in and out — timecode between apps on one Mac",
            "Works with any console or timecode source",
            "Full-featured 20-minute trial",
        ],
        specs=["LTC → MTC", "MTC → LTC", "frame-rate convert", "timecode monitor", "LTC→WAV", "universal"],
        # Long-form page copy (rendered by build_products.longform). Source:
        # dylanmaudio-marketing, briefs/done/time-code-tool-copy-draft.md §3.
        longform=dict(
            story=dict(
                kicker="Why I built it",
                paras=[
                    "I was sending LTC into my DAW over an audio network driver and it kept dropping the "
                    "odd frame. I fixed it the usual way: a hardware timecode clock in the rack, which "
                    "would freewheel, convert frame rates and turn LTC into MTC. It was rock solid. It was "
                    "also about $1,000 for something that mostly sat there looking nice, and when a tour "
                    "came along where I needed a smaller rack, I wrote the software version. It turned out "
                    "to be better at the part the box couldn&rsquo;t do &mdash; telling me <em>what</em> "
                    "was wrong with the timecode.",
                ],
            ),
            what=dict(
                kicker="In detail",
                items=[
                    ("Reads LTC or MTC, and tells you how healthy it is.",
                     "Linear timecode (LTC, the SMPTE audio signal) from any audio input, or MIDI Time Code "
                     "(MTC) from any MIDI port. A large readout, lock and freewheel state, the detected frame "
                     "rate, and separate counts of missed, misread and jumped frames &mdash; so you can tell a "
                     "bad source from a bad path."),
                    ("Converts in any direction.",
                     "LTC to MTC, MTC to LTC, LTC to LTC, MTC to MTC. Run both outputs together and one "
                     "incoming feed leaves as LTC for video and MTC for lighting."),
                    ("Converts frame rates.",
                     "Each output follows the input or converts to the rate you set: 23.976, 24, 25, 29.97 "
                     "drop-frame and non-drop, 30."),
                    ("Cleans up what it&rsquo;s given.",
                     "A single misread frame is ridden through instead of sending everything downstream to "
                     "the wrong place and back. A dropout is freewheeled. A real relocate still follows, one "
                     "frame later, and is written to the log with the reason."),
                    ("Generates timecode.",
                     "With no input, it free-runs as the timecode master &mdash; LTC and MTC from one clock, "
                     "at the start time, frame rate and level you choose."),
                    ("Renders LTC to a WAV.",
                     "Sample-accurate LTC files with your choice of start, length, frame rate, sample rate, "
                     "bit depth and level. Drop it on a track in your playback session."),
                    ("Passes timecode between apps on one Mac.",
                     "An optional virtual audio device carries LTC in and out, and virtual MIDI ports carry "
                     "MTC in and out. No loopback cables, no separate routing utility. (The virtual audio "
                     "device needs macOS 13 or later.)"),
                ],
            ),
            who=dict(
                kicker="Who uses it",
                paras=[
                    "Anyone who sends or chases timecode from a Mac: playback engineers running Ableton Live "
                    "or Reaper; lighting programmers whose software wants MTC when the show sends LTC; video "
                    "and media-server operators; theatre sound with QLab; pyro and show control; FOH and "
                    "monitor engineers running timecode-driven console automation. It doesn&rsquo;t care what "
                    "console you&rsquo;re on.",
                ],
            ),
            faq=dict(
                kicker="Questions",
                items=[
                    ("My DAW drops or misreads LTC frames arriving over an audio network driver. Will this help?",
                     "That&rsquo;s the problem it was built for. Read the LTC in Time Code Tool instead and give "
                     "the DAW clean MTC on the virtual port, or regenerated LTC. The frame counters will also "
                     "show you whether frames are being lost on the way in."),
                    ("Can it convert LTC to MTC for lighting software that only takes MIDI timecode?",
                     "Yes &mdash; to a virtual MIDI port for software on the same Mac, or to any MIDI interface "
                     "for a console or another computer."),
                    ("Is it a replacement for a hardware timecode clock such as a Rosendahl MIF4 or a CB Electronics TC-5?",
                     "For reading, converting LTC and MTC, frame-rate conversion, freewheeling and regenerating "
                     "clean timecode, on a Mac that&rsquo;s already in your rig &mdash; that&rsquo;s what I use it "
                     "for. Those boxes are excellent, and they do two things this doesn&rsquo;t: word clock and "
                     "video reference. Time Code Tool is LTC and MTC only. If you need those, or timecode with "
                     "no computer involved, buy the box."),
                    ("I used Lockstep. Is this a replacement?",
                     "It does what Lockstep did &mdash; LTC in, MTC out &mdash; and the other directions, "
                     "natively on Apple Silicon, and it&rsquo;s maintained."),
                    ("Can I just make an LTC WAV file?",
                     "Yes, offline, at any frame rate including drop-frame."),
                    ("Windows? Intel Macs?",
                     "macOS 11 or later on Apple Silicon only, for now."),
                    ("Does it phone home?",
                     "No analytics, no telemetry. Activating the licence is the only network call, and a "
                     "licence covers two Macs &mdash; the show machine and the spare."),
                ],
            ),
        ),
    ),
}

REQUIREMENTS = "macOS 11 or later &middot; Apple Silicon"
NONAFFIL = ("Developed independently by dylanmaudio and not affiliated with, endorsed by, or supported by "
            "Allen&nbsp;&amp;&nbsp;Heath Ltd. dLive, Avantis, SQ and Qu are trademarks of Allen&nbsp;&amp;&nbsp;Heath Ltd, "
            "used here for identification only.")


# Cloudflare Web Analytics beacon token (cookieless, no consent banner needed).
# Paste the token from cloudflare.com/web-analytics here, then rebuild + deploy.
# Empty = analytics off (pages build byte-identical without it).
CF_BEACON_TOKEN = "d20d574500344548bef2df8dba76b57d"


def inject_analytics(html_str: str) -> str:
    """Insert the Cloudflare Web Analytics beacon before </body>, if a token is set."""
    if not CF_BEACON_TOKEN:
        return html_str
    snippet = ('<script defer src="https://static.cloudflareinsights.com/beacon.min.js" '
               'data-cf-beacon=\'{"token": "' + CF_BEACON_TOKEN + '"}\'></script>\n')
    return html_str.replace("</body>", snippet + "</body>", 1)


# Self-expiring sale guard: after the date in [data-sale-until], hide every
# .sale-only element and reveal every .sale-reg one (the regular-price fallback),
# so a time-boxed promo reverts on its own without a rebuild. Uses the native
# `hidden` attribute (see the [hidden]{display:none!important} rule in the CSS).
SALE_GUARD_JS = (
    "(function(){var s=document.querySelector('[data-sale-until]');if(!s)return;"
    "var end=new Date(s.getAttribute('data-sale-until')+'T23:59:59');"
    "if(Date.now()>end.getTime()){"
    "document.querySelectorAll('.sale-only').forEach(function(e){e.hidden=true;});"
    "document.querySelectorAll('.sale-reg').forEach(function(e){e.hidden=false;});}})();"
)


def abs_url(path: str) -> str:
    return SITE_ROOT.rstrip("/") + "/" + path.lstrip("/")


def seo_head(canonical: str, title: str, description: str, *, image: str = OG_IMAGE,
             og_type: str = "website", noindex: bool = False, ld=None) -> str:
    """Canonical + Open Graph + Twitter Card (+ optional JSON-LD) tags for one page.

    `canonical` is a site-relative path ("/", "about.html", "products/x/").
    `noindex` keeps a page out of search (parked product pages) — the page stays
    crawlable so Google can *see* the noindex; it's simply left out of sitemap.xml.
    """
    url, img = abs_url(canonical), abs_url(image)
    parts = []
    if noindex:
        parts.append('<meta name="robots" content="noindex, follow">')
    parts += [
        f'<link rel="canonical" href="{url}">',
        f'<meta property="og:type" content="{og_type}">',
        '<meta property="og:site_name" content="Dylan [M] Audio">',
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{description}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{img}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{title}">',
        f'<meta name="twitter:description" content="{description}">',
        f'<meta name="twitter:image" content="{img}">',
    ]
    if ld is not None:
        parts.append('<script type="application/ld+json">'
                     + json.dumps(ld, separators=(",", ":")) + '</script>')
    return "\n".join(parts)


def write(rel_path: str, html: str):
    """Write html to a repo-relative path, creating parent dirs."""
    dest = ROOT / rel_path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    print("wrote", dest.relative_to(ROOT), f"({len(html)} bytes)")
