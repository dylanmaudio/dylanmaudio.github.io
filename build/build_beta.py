#!/usr/bin/env python3
"""Generate the Console Control beta page -> cc-beta/index.html, served at
dylanmaudio.com/cc-beta.

For the beta testers, and the engineers the operator invites into the beta
for its last month (operator, 30 Sept 2026): what the app does, how to get
the beta, what's new in it, and how to use it - the getting-started guide as
a web page. /cc-beta was a redirect straight to the checkout until this page
replaced it (30 Sept); the testers' existing link now lands here.

Unlisted: noindex, left out of sitemap.xml, and nothing on the site links
here. The operator sends the link. Console Control itself is announced (26
Sept), so nothing on this page is secret - but the download is meant to go
to invited testers, not to search traffic.

What comes from where:
- The name, icon, lead and feature list are the public product page's
  (common.PRODUCTS["console-control"]), so the two pages can't disagree.
- The carousel is the beta product's store set (hero, what's new, the guide,
  Stream Deck, the beta's terms), in assets/cards/console-control-beta/ -
  rendered by the marketing repo's build_cxc_beta_slides.py and copied by its
  publish_site_cards.py. Re-render and re-copy with each beta.
- VERSION, NEW, the keys and the guide describe the build on the beta
  product: from the apps repo's apps/console-control/CHANGELOG.md (top
  entry), docs/QUICK-REFERENCE.md and docs/REFERENCE.md. Redo them with each
  beta that goes out.
- The guide is the same copy as those slides; change both.
"""
import common as C
import build_products as P

SLUG = "cc-beta"
PRODUCT = C.PRODUCTS["console-control"]
VERSION = "0.2.1 BETA"
BETA_UNTIL = "31 October 2026"
DOWNLOAD = C.CHECKOUT["console-control-beta"]
# The carousel: the beta product's own store set, in assets/cards/console-control-beta/,
# copied there by dylanmaudio-marketing store-assets/publish_site_cards.py.
CARDS = "console-control-beta"
FEEDBACK = "mailto:dylan@dylanmaudio.com?subject=Console%20Control%20beta"

# ---------------------------------------------------------------- the guide
# (heading, detail) - detail may carry HTML.

NEW = [  # 0.2.1 against 0.1.19, the build the first testers had
    ("The keys are laid out afresh.",
     "Single keys are cue programming and getting around; <kbd>⇧</kbd> is the pair of a single key; "
     "<kbd>⌥</kbd> is markers and regions; <kbd>⌘</kbd> is files, clipboard, undo and zoom; <kbd>⌃⌥</kbd> is the "
     "console and the view. If you used 0.1.19, many have moved &mdash; the <a href=\"#keys\">keys below</a> are "
     "the new ones, and every button shows its key when you hover over it."),
    ("Show Mode shows what&rsquo;s coming next.",
     "The region you&rsquo;re in and how long is left of it, then the next cues, markers and regions, each with a "
     "countdown and its timecode. The countdown turns amber inside ten seconds and red inside three."),
    ("Sync from Console.",
     "Reads every channel&rsquo;s name and colour from the desk through MIDI Bridge, and shows what would change "
     "before anything does. New console channels are offered as tracks; nothing is added or deleted unless you "
     "say so."),
    ("A Mixer with EQ, compressor and limiter.",
     "For the reference audio: an equaliser and an SSL-style bus compressor on every track, and a limiter on the "
     "master. Saved with the show and in every export."),
    ("Export Audio built for a show.",
     "Master and timecode as separate files or one two-channel file, or every reference track; WAV up to 96 kHz "
     "and 32-bit float, or MP3; one region, every region, or the time selection. Timecode is generated at the "
     "export&rsquo;s own sample rate."),
    ("Tempo detection follows the click.",
     "A click that changes tempo gets a span for each steady stretch, and a ramp is followed beat by beat. Clicks "
     "are placed to a fraction of a frame."),
    ("Faster, sharper, more precise editing.",
     "Select and move audio clips with a preview of where they land, zoom down to single frames, sharp waveforms "
     "on recordings hours long, and clip moves heard straight away instead of after a pause."),
    ("Runs on macOS 11 Big Sur or later.",
     "Earlier betas needed macOS 13.3."),
]

FIRST_SESSION = [
    ("Start the dLive MIDI Bridge",
     'Console Control talks to the console through the free <a href="/products/midi-bridge/">MIDI Bridge</a> '
     "(1.1 or later). Wait for the green line at the bottom of the window."),
    ("Match the base MIDI channel",
     "Settings (<kbd>⌘,</kbd>) &mdash; the same number as Utility &rarr; Control &rarr; MIDI on the console."),
    ("Add your tracks",
     "<b>+ Track</b> (<kbd>⌘T</kbd>), pick a type and a range. &ldquo;1-16&rdquo; makes sixteen input tracks in "
     "one step."),
    ("Bring in the console&rsquo;s names",
     "Sync from Console (<kbd>⌃⌥R</kbd>) for channel names and colours, straight from the desk. File &rarr; Import "
     "Console Show File for Scene names and Actions."),
    ("Import a show recording",
     "<kbd>⌘I</kbd>. With an LTC track present, every song is placed at its own timecode and outlined as a region."),
    ("Place cues",
     "Select a track, then <kbd>U</kbd>, <kbd>I</kbd> or <kbd>V</kbd> for fader cues, <kbd>M</kbd> for mute, "
     "<kbd>S</kbd> for a Scene, <kbd>A</kbd> for an Action."),
    ("Run Preflight",
     "<kbd>⌃⌥P</kbd> checks the bridge, the base channel, chase and routing, and says exactly what is wrong."),
    ("Arm SYNC, press play",
     "The timeline waits for timecode and follows it when it locks. Then <kbd>⌘⇧L</kbd> for Show Mode."),
]

IDEAS = [
    ("Time, not bars &mdash; cues sit at a timecode position.",
     "Live shows drift, drop the click and vamp. Tempo exists only for beat snapping and the grid &mdash; the "
     "ruler is always time."),
    ("Chase &mdash; move the playhead and the desk follows.",
     "Scrub, locate or play: every lane&rsquo;s value at that position is worked out and sent. Chase can be "
     "switched off for everything (<kbd>⇧C</kbd>) or per lane (<kbd>C</kbd>)."),
    ("Fired vs pending &mdash; plain text was sent, a dot was not.",
     "A dot beside a readout means &ldquo;the console should be here, but it hasn&rsquo;t been sent&rdquo;. "
     "Conform Console sends everything pending in one pass."),
    ("One console path &mdash; everything goes through MIDI Bridge.",
     "Console Control never opens its own connection to the desk, so your DAW, Companion and the other apps keep "
     "working beside it."),
]

# (colour, state, meaning)
SYNC = [
    ("var(--dim)", "Dimmed", "Sync off. Internal clock, for programming and loop playback."),
    ("#6f93b8", "Lit steel-blue", "Armed. Press play to latch."),
    ("var(--amber)", "Pulsing amber", "Play pressed, awaiting timecode."),
    ("var(--green)", "Green", "Locked to incoming timecode. Locate and scrub belong to the source."),
    ("var(--amber)", "Steady amber", "Freewheeling &mdash; the signal dropped and the timeline is coasting."),
]
SYNC_NOTE = ("<b>Right-click SYNC</b> for the source (LTC or MTC), the LTC input channel, the MTC port, freewheel "
             "time, drift tolerance and offset. <b>Still pulsing while code plays?</b> It is listening to the wrong "
             "input.")

KEYS = [  # 0.2.1's - docs/QUICK-REFERENCE.md in the apps repo has them all
    (["Space"], "Play / stop"),
    (["⌘⇧Esc"], "Panic"),
    (["⌘⇧L"], "Show Mode"),
    (["⌃⌥C"], "Conform Console"),
    (["⌃⌥P"], "Preflight"),
    (["⌃⌥R"], "Sync from Console"),
    (["U", "I", "V"], "Fader cue: unity / &minus;&infin; / a value"),
    (["M", "⇧M"], "Mute / unmute cue"),
    (["S", "A"], "Scene / Action cue"),
    (["C", "⇧C"], "Chase this lane / everything"),
    (["[", "]"], "Previous / next marker, region or clip edge"),
    (["1", "…", "0"], "Regions 1 to 10"),
    (["T"], "Go to a timecode"),
    (["⌥M", "⌥R"], "Marker at playhead / region from selection"),
    (["⌥←", "⌥→"], "Nudge the selection"),
    (["⌃⌥Space"], "Record armed reference tracks"),
    (["⌃⌥X"], "Mixer"),
    (["⌘Z", "⌘⇧Z"], "Undo / redo"),
]

SHOW_DAY = [
    ("Preflight &mdash; <kbd>⌃⌥P</kbd>",
     "Flags problems before the show: bridge and console link, base-channel mismatches, chase switched off, "
     "send lanes the console can&rsquo;t route."),
    ("Show Mode &mdash; <kbd>⌘⇧L</kbd>",
     "Locks editing and undo. Huge timecode, sync, chase, bridge health and live per-track readouts &mdash; and "
     "what&rsquo;s coming next, with countdowns. Asks before it enters and before it leaves."),
    ("Conform Console &mdash; <kbd>⌃⌥C</kbd>",
     "A one-shot chase you can use at any moment. Play always conforms first, so the console enters playback in "
     "the right state."),
    ("Panic &mdash; <kbd>⌘⇧Esc</kbd>",
     "Always available, even with everything else locked."),
]

STREAM_DECK = [
    ("Every shortcut is a key.",
     'Through the free <a href="/products/companion/">Companion module</a>, Console Control&rsquo;s commands are '
     "Companion actions &mdash; play, Conform, Show Mode, Panic, cue programming &mdash; with sync lock and chase "
     "shown on the keys. A Stream Deck is the nicest way to press them; Companion&rsquo;s web buttons on a phone or "
     "tablet work too."),
    ("Set it up once.",
     'Install Companion on the same Mac and add the dylanmaudio module &mdash; the steps are on the '
     '<a href="/products/companion/#install">Companion page</a>. Console Control appears beside your other '
     "dylanmaudio apps."),
    ("You decide what it can touch.",
     "Settings &rarr; Companion: allow Companion control or switch it off, and lock the show-critical controls "
     "&mdash; Stop, Record, Conform and Show Mode are refused while locked. Panic always works."),
]

TROUBLE = [
    ("var(--green)", "Green", "Console connected through the bridge. Its IP is shown."),
    ("var(--amber)", "Amber", "Bridge running, console unreachable. Check the console IP in the bridge, the network, "
                              "and MIDI-over-TCP on the console."),
    ("var(--red)", "Red", "The dLive MIDI Bridge app isn&rsquo;t running. Start it."),
    ("var(--blue)", "Green, but nothing moves",
     "Check chase for everything (<kbd>⇧C</kbd>), the track&rsquo;s M, the lane&rsquo;s chase badge &mdash; or run "
     "Preflight (<kbd>⌃⌥P</kbd>)."),
    ("var(--blue)", "A track won&rsquo;t edit", "It is locked, or you are in Show Mode."),
]
TROUBLE_NOTE = ("<b>Something went wrong?</b> Click <b>Export log</b> in the footer &mdash; a copy of the session log "
                "lands on your Desktop. Send it with <b>Send feedback</b> beside it, or to "
                '<a href="mailto:dylan@dylanmaudio.com">dylan@dylanmaudio.com</a>. The log already records your '
                "settings, the show, every message you saw and the timecode state.")

THE_BETA = [
    ("Until the date, everything works.",
     "The window shows the end date from first launch, and for the last two weeks it reminds you each time it "
     "opens."),
    ("After the date, it opens and edits but sends nothing.",
     "Your shows stay yours. Console output stops until you install a newer beta."),
    ("A show is never interrupted.",
     "The date is only checked when the app starts, so a show that runs past midnight carries on."),
    ("You need MIDI Bridge and a current Mac.",
     'The free <a href="/products/midi-bridge/">dLive MIDI Bridge</a> (1.1 or later), macOS 11 or later, Apple '
     "Silicon. Companion and a Stream Deck if you want keys. No analytics, no telemetry."),
]

# ---------------------------------------------------------------- page

CSS = """
  .beta-note{margin-top:18px;max-width:62ch;font-size:0.95rem;color:var(--muted);}
  .beta-note b{color:var(--text);font-weight:600;}
  .beta-note a{color:var(--blue);}
  .lf a, .p-band p a{color:var(--blue);} .lf a:hover{text-decoration:underline;}
  .lf b{color:var(--text);font-weight:600;}
  kbd{font-family:var(--mono);font-size:0.82em;color:var(--text);background:var(--surface-2);
    border:1px solid var(--border);border-bottom-width:2px;border-radius:6px;padding:1px 7px;white-space:nowrap;}
  .states{border-top:1px solid var(--hairline);margin:0 0 18px;}
  .state{display:grid;grid-template-columns:14px minmax(150px,210px) 1fr;gap:16px;align-items:baseline;
    padding:13px 0;border-bottom:1px solid var(--hairline);}
  .state .dot{width:12px;height:12px;border-radius:50%;transform:translateY(1px);}
  .state .l{font-weight:600;color:var(--text);}
  .state .d{color:var(--muted);}
  @media (max-width:620px){.state{grid-template-columns:14px 1fr;}.state .d{grid-column:2;}}
  .keys{display:grid;grid-template-columns:1fr 1fr;column-gap:36px;border-top:1px solid var(--hairline);}
  .key{display:flex;gap:14px;align-items:center;padding:10px 0;border-bottom:1px solid var(--hairline);}
  .key .c{flex:none;width:118px;display:flex;gap:5px;flex-wrap:wrap;}
  .key .a{color:var(--muted);font-size:0.95rem;}
  @media (max-width:700px){.keys{grid-template-columns:1fr;}}
"""


def kick(t):
    return f'<div class="kicker p-sec-k"><span class="tick">//</span>&nbsp; {t}</div>'


def block(inner, anchor=""):
    a = f' id="{anchor}"' if anchor else ""
    return f'<div class="lf-block"{a}>{inner}</div>'


def items(rows):
    return "".join(f'<div class="lf-item"><h3>{h}</h3><p>{d}</p></div>' for h, d in rows)


def steps(rows):
    return '<ol class="lf-steps">' + "".join(f"<li><h3>{h}</h3><p>{d}</p></li>" for h, d in rows) + "</ol>"


def states(rows, note):
    body = "".join(f'<div class="state"><span class="dot" style="background:{c}"></span>'
                   f'<span class="l">{l}</span><span class="d">{d}</span></div>' for c, l, d in rows)
    return f'<div class="states">{body}</div><p>{note}</p>'


def keys(rows):
    body = "".join('<div class="key"><div class="c">' + "".join(f"<kbd>{k}</kbd>" for k in ks)
                   + f'</div><div class="a">{a}</div></div>' for ks, a in rows)
    return f'<div class="keys">{body}</div>'


def ctas(discord_label="Beta feedback"):
    return (f'<a href="{DOWNLOAD}" target="_blank" rel="noopener" class="btn btn-primary">Download the beta &mdash; free '
            f'<span class="arw">&rarr;</span></a>'
            f'<a href="/products/midi-bridge/" class="btn btn-ghost">Get MIDI Bridge (free)</a>'
            f'<a href="{C.DISCORD_URL}" class="btn btn-discord" target="_blank" rel="noopener">{C.DISCORD_SVG} '
            f'{discord_label}</a>')


def build():
    p = PRODUCT
    name = p["name"]
    title = f"{name} beta — Dylan [M] Audio"
    desc = (f"The {name} beta: timecode show automation for your console, free until {BETA_UNTIL}. "
            "What it does, what's new, how to get it, and your first session.")
    seo = C.seo_head(f"{SLUG}/", title, desc, image=f"assets/{p['icon']}", noindex=True)
    features = "".join(f"<li>{P.CK}<span>{f}</span></li>" for f in p["features"])
    glance = [("Version", VERSION), ("Beta until", BETA_UNTIL), ("Price", "Free during the beta"),
              ("Platform", "macOS 11+"), ("Chip", "Apple Silicon"), ("Console", "dLive first"),
              ("Needs", '<a href="/products/midi-bridge/" style="color:var(--blue)">MIDI Bridge</a> 1.1+'),
              ("Stream Deck", '<a href="/products/companion/" style="color:var(--blue)">via Companion</a>')]
    glance_rows = "".join(f'<div class="srow"><span class="k">{k}</span><span class="v">{v}</span></div>'
                          for k, v in glance)

    guide = "".join([
        block(kick(f"New in {VERSION.replace(' BETA', '')}")
              + "<p>Since 0.1.19, the build the first testers had. The full list comes with the download.</p>"
              + items(NEW), "new"),
        block(kick("Your first session, in eight steps")
              + "<p>Twenty minutes at the desk, or at home with a show recording. Nothing reaches the console "
                "until the bridge line is green.</p>"
              + steps(FIRST_SESSION), "start"),
        block(kick("Four ideas that explain everything else")
              + "<p>If the app ever surprises you, it is almost always one of these.</p>" + items(IDEAS)),
        block(kick("SYNC arms, play latches, stop disarms")
              + "<p>The button beside Record. Always this way round &mdash; a show never latches on its own when "
                "it opens.</p>" + states(SYNC, SYNC_NOTE)),
        block(kick("The keys worth learning first")
              + "<p>Every shortcut can be changed in View &rarr; Keyboard Shortcuts (<kbd>⌃⌥K</kbd>): click one "
                "and press the keys you want. Hover over any button to see its key.</p>"
              + keys(KEYS), "keys"),
        block(kick("Built for show day") + "<p>Four controls to know before doors.</p>" + items(SHOW_DAY)),
        block(kick("On your Stream Deck")
              + "<p>Beta testers get Stream Deck control too, through Bitfocus Companion.</p>" + items(STREAM_DECK),
              "stream-deck"),
        block(kick("If something is wrong")
              + "<p>Read the line at the bottom of the window. It tells you where the chain is broken, in order.</p>"
              + states(TROUBLE, TROUBLE_NOTE)),
        block(kick(f"The beta, until {BETA_UNTIL}")
              + f"<p>This is {VERSION}: a full-featured beta. Nothing is switched off, and nothing is locked away "
                "afterwards.</p>" + items(THE_BETA), "beta"),
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
    <a class="crumb" href="/products/console-control/">&larr; {name}</a>
    <div class="p-id">
      <img src="/assets/{p['icon']}" alt="{name} app icon" width="72" height="72" />
      <div>
        <h1>{name}</h1>
        <div class="p-badges"><span class="tag">Beta &middot; {VERSION.replace(' BETA', '')}</span></div>
      </div>
    </div>
    <p class="p-tagline">{p['tagline']} Free to try until {BETA_UNTIL}.</p>
    <div class="p-cta-row">{ctas()}</div>
    <p class="beta-note">The download is a free checkout on the store: the link comes by email, and I&rsquo;ll email
      you when a new beta is out. <b>You also need the free MIDI Bridge</b>: every cue reaches the console through it.
      Then see <a href="#new">what&rsquo;s new</a>, or start with <a href="#start">your first session</a>.</p>
  </div>
</section>

{P.gallery_block(CARDS, p)}

<section><div class="wrap p-grid">
  <div class="p-body">
    <div class="kicker p-sec-k"><span class="tick">//</span>&nbsp; What it does</div>
    <p class="p-lead">{p['lead']}</p>
  </div>
  <div>
    <ul class="feature-list">{features}</ul>
    <div class="side" style="margin-top:24px;">
      <div class="h">// The beta</div>
      {glance_rows}
    </div>
  </div>
</div></section>

<section class="lf"><div class="wrap">{guide}</div></section>

<section class="p-band"><div class="wrap"><div class="kicker" style="display:inline-block;">
  <span class="tick">//</span>&nbsp; {name} beta</div>
  <h2>Try it on your next show.</h2>
  <p>Free until {BETA_UNTIL}. Tell me what works, what doesn&rsquo;t and what you&rsquo;d want next &mdash; in the
    Discord, with Send feedback in the app, or at <a href="{FEEDBACK}">dylan@dylanmaudio.com</a>.</p>
  <div class="p-cta-row">{ctas("Join the Discord")}</div>
</div></section>

{P.FOOTER}

<script>
  {C.UTM_PASS_JS}
  {P.GALLERY_JS}
</script>
</body>
</html>"""
    C.write(f"{SLUG}/index.html", C.inject_analytics(html))


if __name__ == "__main__":
    build()
