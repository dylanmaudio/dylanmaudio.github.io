#!/usr/bin/env python3
"""Generate the free LTC WAV download page -> ltc-wav/index.html, served at
dylanmaudio.com/ltc-wav.

One hour of SMPTE LTC at every frame rate Time Code Tool supports, at 48
and 44.1 kHz, free and with no sign-up, with the app one click away. The
"LTC wav" searches are answered by free browser generators; this page
competes for them without paying per click (dylanmaudio-marketing,
briefs/paid-advertising.md §6, operator go-ahead 4 Oct 2026).

The files in downloads/ltc/ are rendered by the marketing repo's
tools/build_ltc_downloads.py with Time Code Tool's own encoder, and each is
decoded frame by frame before it is copied here. Its RATES, SAMPLE_RATES and
file_name() match FILES and name() below. The build fails if a file is
missing, so the page never links to a 404.

Indexed and in sitemap.xml; the Time Code Tool page links here from its FAQ.
"""
import html as htmlmod

import common as C
import build_products as P

SLUG = "ltc-wav"
TCT = C.PRODUCTS["time-code-tool"]
DIR = "downloads/ltc"

# (rate key in the file name, label, frames in the hour, real running time)
FILES = [
    ("23.976fps", "23.976", "86,400", "1:00:03.6"),
    ("24fps", "24", "86,400", "1:00:00"),
    ("25fps", "25", "90,000", "1:00:00"),
    ("29.97df", "29.97 drop-frame", "107,892", "1:00:00"),
    ("29.97nd", "29.97 non-drop", "108,000", "1:00:03.6"),
    ("30fps", "30", "108,000", "1:00:00"),
]
SAMPLE_RATES = [("48k", "48 kHz"), ("44.1k", "44.1 kHz")]


def name(key, sr):
    return f"LTC_{key}_{sr}_1h.zip"


def size_mb(rel):
    path = C.ROOT / rel
    if not path.exists():
        raise SystemExit(f"build_ltc: {rel} is missing - run dylanmaudio-marketing "
                         "tools/build_ltc_downloads.py first")
    return f"{path.stat().st_size / 1e6:.1f} MB"


WHICH = [
    ("Use the rate the rest of the show uses.",
     "Timecode only works if everything reading it agrees on the frame rate, so ask the lighting, video or "
     "show-control department before you choose. If nobody has decided yet, the usual choices are below."),
    ("25 &mdash; Europe, the UK, Australia and other PAL regions.",
     "The default for live shows and video in 50 Hz countries."),
    ("30 &mdash; audio and lighting shows elsewhere.",
     "Common when there is no video to match. Most lighting consoles and media servers take it."),
    ("29.97 drop-frame &mdash; NTSC video and broadcast.",
     "Matches 29.97 fps video and keeps the timecode in step with the clock on the wall. Non-drop 29.97 counts "
     "every frame instead, so an hour of it takes 3.6 seconds longer than an hour."),
    ("24 and 23.976 &mdash; film and cinema cameras.",
     "When the show is cut to footage shot at those rates."),
]

USING = [
    ("Unzip it.",
     "Double-click the zip. The WAV inside is mono, 16-bit, and about 350 MB for the hour."),
    ("Match the session&rsquo;s sample rate.",
     "Take the 48 kHz file for a 48 kHz session and the 44.1 kHz file for a 44.1 kHz one, so nothing resamples "
     "the timecode on the way out."),
    ("Put it on its own track, with nothing on it.",
     "No effects, no fades, no time-stretch &mdash; in Ableton Live, switch Warp off for the clip. Line up "
     "00:00:00:00 with the start of the show, or wherever the timecode should begin."),
    ("Send that track to its own output.",
     "A dedicated interface output, at unity, not summed with anything else. The file peaks at &minus;18 dBFS, "
     "about 0 dBu on most interfaces &mdash; a level timecode readers are happy with."),
]

FAQ = [
    ("Are they really free?",
     "Yes. No sign-up, no email, no watermark. Use them in any show, paid or not."),
    ("Why a zip?",
     "An hour of WAV is about 350 MB. Timecode is a very regular signal, so it zips to a few MB; double-click to "
     "get the WAV back."),
    ("Why do the 23.976 and 29.97 non-drop files run 3.6 seconds over the hour?",
     "Each file holds one hour of timecode, 00:00:00:00 up to 01:00:00:00. At those rates every frame is counted "
     "but the frames are slightly longer than the rate&rsquo;s name suggests, so an hour of timecode takes an hour "
     "and 3.6 seconds. Drop-frame 29.97 skips frame numbers to stay on the clock instead."),
    ("Are the files any good?",
     "They come from the encoder inside <a href=\"/products/time-code-tool/\">Time Code Tool</a>, and every file "
     "is read back and decoded frame by frame before it goes up here: all frames present, in order, with the "
     "right drop-frame flag."),
    ("I need a different start time, length or level.",
     "Time Code Tool renders LTC WAVs with any start, length, frame rate, sample rate, bit depth and level. Its "
     "free trial does it too."),
    ("My timecode reader won&rsquo;t lock.",
     "Check the frame rate matches, the track isn&rsquo;t time-stretched or processed, and the output isn&rsquo;t "
     "summed with anything else. If it still drops frames, "
     "<a href=\"/products/time-code-tool/\">Time Code Tool</a> shows exactly what is arriving: the detected rate, "
     "and every missed, misread or jumped frame."),
]

CSS = """
  .lf a, .p-band p a, .ltc-note a{color:var(--blue);} .lf a:hover{text-decoration:underline;}
  .ltc-note{margin-top:18px;max-width:62ch;font-size:0.95rem;color:var(--muted);}
  .dl{border-top:1px solid var(--hairline);margin:0 0 18px;}
  .dl-row{display:grid;grid-template-columns:minmax(150px,1fr) auto auto;gap:12px 18px;align-items:center;
    padding:14px 0;border-bottom:1px solid var(--hairline);}
  .dl-rate{font-weight:600;color:var(--text);font-size:1.05rem;}
  .dl-rate small{display:block;font-weight:400;color:var(--muted);font-size:0.85rem;margin-top:2px;}
  .dl-row .btn{padding:9px 14px;font-size:0.92rem;white-space:nowrap;}
  .dl-row .btn small{color:var(--muted);font-weight:400;margin-left:6px;}
  @media (max-width:620px){.dl-row{grid-template-columns:1fr 1fr;}.dl-rate{grid-column:1 / -1;}
    .dl-row .btn{justify-content:center;}}
"""


def kick(t):
    return f'<div class="kicker p-sec-k"><span class="tick">//</span>&nbsp; {t}</div>'


def items(rows):
    return "".join(f'<div class="lf-item"><h3>{h}</h3><p>{d}</p></div>' for h, d in rows)


def downloads():
    rows = []
    for key, label, frames, runs in FILES:
        btns = "".join(
            f'<a class="btn btn-ghost" href="/{DIR}/{name(key, sr)}" download>{sr_label} '
            f'<small>{size_mb(f"{DIR}/{name(key, sr)}")}</small></a>'
            for sr, sr_label in SAMPLE_RATES)
        rows.append(f'<div class="dl-row"><div class="dl-rate">{label} fps'
                    f'<small>{frames} frames &middot; runs {runs}</small></div>{btns}</div>')
    return f'<div class="dl">{"".join(rows)}</div>'


def tct_ctas():
    return (f'<a href="{TCT["trial_store"]}" target="_blank" rel="noopener" class="btn btn-primary">'
            f'Try Time Code Tool free <span class="arw">&rarr;</span></a>'
            f'<a href="/products/time-code-tool/" class="btn btn-ghost">What it does</a>')


def build():
    title = "Free LTC WAV files &mdash; SMPTE timecode at every frame rate &mdash; Dylan [M] Audio"
    desc = ("Download an hour of SMPTE LTC timecode as a WAV: 23.976, 24, 25, 29.97 drop-frame and non-drop, "
            "and 30 fps, at 48 or 44.1 kHz. Free, no sign-up.")
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": htmlmod.unescape(q),
         "acceptedAnswer": {"@type": "Answer", "text": htmlmod.unescape(a)}} for q, a in FAQ]}
    seo = C.seo_head(f"{SLUG}/", htmlmod.unescape(title), desc, ld=ld)

    guide = "".join(f'<div class="lf-block"{a}>{b}</div>' for a, b in [
        (' id="which"', kick("Which frame rate?") + items(WHICH)),
        (' id="use"', kick("Using it in a playback session")
         + '<ol class="lf-steps">' + "".join(f"<li><h3>{h}</h3><p>{d}</p></li>" for h, d in USING) + "</ol>"),
        (' id="faq"', kick("Questions") + items(FAQ)),
    ])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon-16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/favicon-180.png">
<link rel="icon" href="/assets/logo.png">
<title>{title}</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
{seo}
<style>{P.CSS}{CSS}</style>
</head>
<body class="product">
{P.nav("software")}

<section class="p-hero">
  <div class="p-hero-inner">
    <a class="crumb" href="/products/time-code-tool/">&larr; Time Code Tool</a>
    <h1>Free LTC timecode WAV files</h1>
    <p class="p-tagline">An hour of SMPTE linear timecode at every common frame rate, ready to drop on a track.
      Free, no sign-up.</p>
    <p class="ltc-note">Each file starts at 00:00:00:00 and runs one hour of timecode. Mono, 16-bit WAV, peaking at
      &minus;18 dBFS, zipped. Not sure which rate? See <a href="#which">which frame rate</a>.</p>
  </div>
</section>

<section><div class="wrap">
  {kick("Download")}
  {downloads()}
  <p class="ltc-note">Need a different start time, length, sample rate or level? <a href="/products/time-code-tool/">Time
    Code Tool</a> renders any of them on your Mac, and its free trial does it too.</p>
</div></section>

<section class="lf"><div class="wrap">{guide}</div></section>

<section class="p-band"><div class="wrap"><div class="kicker" style="display:inline-block;">
  <span class="tick">//</span>&nbsp; Time Code Tool</div>
  <h2>Timecode you can see.</h2>
  <p>{TCT['tagline']} Read incoming LTC or MTC and see how healthy it is, convert between them at any frame rate,
    or be the timecode master. For Apple Silicon Macs; a full-featured 20-minute trial is free.</p>
  <div class="p-cta-row">{tct_ctas()}</div>
</div></section>

{P.FOOTER}

<script>
  {C.UTM_PASS_JS}
</script>
</body>
</html>"""
    C.write(f"{SLUG}/index.html", C.inject_analytics(html))


if __name__ == "__main__":
    build()
