#!/usr/bin/env python3
"""Generate the Show Recorder beta page -> sr-beta/index.html, served at
dylanmaudio.com/sr-beta.

For Show Recorder's beta testers (operator, 23 Oct 2026): what the app does,
how to get the beta, and how to use it - the getting-started guide as a web
page, as /cc-beta is Console Control's.

Unlisted: noindex, left out of sitemap.xml, and nothing on the site links
here. The operator sends the link. Show Recorder is not announced: the
operator chose to publish the page anyway (23 Oct), knowing the site's repo
is public. So the product's details live here, not in common.PRODUCTS,
where the home page, the nav and the other pages would pick them up; and
the page says nothing the copy bank keeps back - no price, no release date,
no free tier, no Stream Deck (the Companion module doesn't support it yet).

What comes from where:
- The tagline, lead and feature list: the marketing repo's copy bank
  (copy/app-descriptions.md, "Show Recorder": Tagline, Short, Store
  bullets; "chase" is "follow" since 0.2.7).
- The carousel is the beta's store set (hero and slides 02-10), in
  assets/cards/show-recorder-beta/: rendered by the marketing repo's
  build_sr_beta_slides.py and copied by its publish_site_cards.py.
- The guide is the same copy as those slides (checked against 0.2.14's
  apps/show-recorder/docs/REFERENCE.md); change both.
- The Quick Reference and Reference Manual are the PDFs the apps repo
  publishes into guides/ with each build.
"""
import common as C
import build_products as P
import build_beta as B          # the guide's building blocks and styles, shared with /cc-beta

SLUG = "sr-beta"
NAME = "Show Recorder"
ICON = "show-recorder.png"
VERSION = "0.2.15 BETA"          # with the MIDI Bridge 1.5.0 beta in the download (ROADMAP's brief, 28 Oct 2026)
BETA_UNTIL = "30 November 2026"
DOWNLOAD = C.CHECKOUT["show-recorder-beta"]
CARDS = "show-recorder-beta"
FEEDBACK = "mailto:dylan@dylanmaudio.com?subject=Show%20Recorder%20beta"
MANUAL = "/guides/show-recorder-reference-manual.pdf"
QUICK_REF = "/guides/show-recorder-quick-reference.pdf"

TAGLINE = "Record the show. Leave with the mix."
LEAD = ("Multitrack recording for live shows, built for FOH. Record every channel from any console, play it back "
        "for a virtual soundcheck, and leave the gig with a finished stereo mix and stems, mixed and mastered "
        "inside the app.")
FEATURES = [
    "Any console, any audio interface: Dante, MADI, USB",
    "Virtual soundcheck: every track back out its own output",
    "The finished mix built in: EQ, compression, tape, clipper and limiter on the buses and master",
    "Find Songs, then export the stereo mix and stems per song, loudness measured",
    "Record at 48 kHz from a 96 kHz system, converted as it records",
    "Show-safe: disk time and FAT32 warnings, crash recovery, dropouts marked, Lock",
    "Timecode in and out: stamped takes, record on timecode, follow in playback",
]

# ---------------------------------------------------------------- the guide
# The beta slides' copy (dylanmaudio-marketing store-assets/build_sr_beta_slides.py).

NEW = [  # 0.2.15 against 0.2.14: its CHANGELOG, in ROADMAP's beta brief's selection (28 Oct 2026)
    ("Four consoles, by their own names.",
     "The header names the console MIDI Bridge is on (&ldquo;v0.2.15 &middot; Wing&rdquo;, &ldquo;&middot; "
     "DiGiCo&rdquo;, &ldquo;&middot; SQ&rdquo;). New Session from the console names a desk&rsquo;s mixes as the desk "
     "does &mdash; a Wing bus is &ldquo;Bus 1&rdquo;, the SQ&rsquo;s main is &ldquo;LR&rdquo; &mdash; and reads the "
     "DiGiCo SD&rsquo;s channels, auxes, groups and matrices. A stereo channel on the SD or the Wing becomes one "
     "stereo track."),
    ("Scene markers that match the desk.",
     "On the Wing a marker carries the scene&rsquo;s name (&ldquo;Scene 4: UP1&rdquo;); on the SD, the "
     "snapshot&rsquo;s number as its screen shows it (&ldquo;Snapshot 1.93: Verse&rdquo;), and Recall in Playback "
     "recalls that snapshot."),
    ("AUTO: record when timecode runs.",
     "A button in the transport row (and Transport &rarr; Record When Timecode Runs) arms recording on timecode for "
     "the session: off for a line check, on for the show."),
    ("Meters for every row.",
     "A stereo track shows two meters, L and R. The Sub-Mixer and Sync rows &mdash; the L/R Mix, desk mixes, ambient "
     "mics, Click and LTC &mdash; follow the inputs."),
    ("And more.",
     "<kbd>⇧E</kbd> makes the time selection from the selected clips; Export can export the selected clips and "
     "remembers your last choices; patching an output during playback no longer drops the audio; LTC picks the code "
     "up again after a pause."),
]

WHAT = [
    ("Every input, its own file.",
     "Broadcast WAV or FLAC, 44.1 to 192 kHz: record at 48 kHz from a 96 kHz system, converted as it records. "
     "Every file is stamped with where it starts."),
    ("Built for the whole show.",
     "Disk time against the show&rsquo;s length before you start, a take recovered after a crash, every dropout "
     "counted and marked."),
    ("The mix, ready at Stop.",
     "Render the mix during each take, WAV and MP3, through the Mixer and the mastering chain: hand it over that "
     "night."),
    ("Songs, mix and stems.",
     "Find Songs splits the show at its gaps; export the stereo mix and the stems for the show, each song or a "
     "selection."),
]

FIRST_SESSION = [
    ("Choose the interfaces",
     "<b>Settings &rarr; Audio</b> (<kbd>⌘,</kbd>): the Multitrack interface every track records from, and "
     "Sub-Mixer and Sync out for the mix, click and timecode."),
    ("Start a session",
     "<b>New Session</b> (<kbd>⌘N</kbd>): empty, from last night&rsquo;s session, from a template, or from the "
     "console."),
    ("Bring in the console&rsquo;s names",
     "<b>Sync from Console</b> (<kbd>⌃⌥R</kbd>) reads every channel&rsquo;s name and colour from a dLive, an SQ, "
     "a Wing or a DiGiCo SD, through the MIDI Bridge 1.5 beta in the download, and shows what would change first."),
    ("Patch",
     "Select tracks, type the first channel, then <b>Inputs</b> to cascade them, or click and drag in the Patch "
     "Matrix."),
    ("Arm",
     "Click <b>Arm</b> at the top of the arm column, or <kbd>⌃⌥A</kbd>. <kbd>⌥</kbd>-click a track&rsquo;s arm "
     "button to make it rec-safe."),
    ("Check before you record",
     "The Recording panel: time left on the disk against the show&rsquo;s length. <b>Before You Record</b> "
     "(<kbd>⌃⌥P</kbd>) lists anything that would make the take wrong."),
    ("Record",
     "<kbd>⌃⌥Space</kbd>, or 3 on the number pad. During a take Space only ever stops. At Stop the take is placed "
     "on its tracks and the session saved."),
    ("Find the songs, export",
     "<b>Find Songs</b> (the Markers menu) makes a region for every song; <b>Export</b> (<kbd>⌘E</kbd>) writes "
     "the mix and the stems."),
]

SHOW_SAFE = [
    ("A take is never lost.",
     "If the app or the Mac stops mid-take, the take is recovered when the session next opens, up to the last "
     "moment written."),
    ("Dropouts, counted and marked.",
     "The counter in the toolbar is zero in a quiet show. Each dropout is a &#9888; marker where it happened."),
    ("Every take, written twice.",
     "<b>Settings &rarr; Recording</b>: a second drive gets the whole session. A slow or unplugged copy never "
     "touches the main recording."),
    ("The downbeat you were late for.",
     "Pre-record: Off, 2, 5 or 10 s. Every take starts with the seconds before you pressed Record."),
]

TIMECODE = [
    ("Every take at its code.",
     "The first take that sees code sets the timeline to the hour; takes land at their code to the sample, so a "
     "run&rsquo;s nights line up."),
    ("Record when timecode runs: AUTO.",
     "The <b>AUTO</b> button in the transport row. A take starts when the code locks and stops when it&rsquo;s been "
     "gone 5 seconds, or keeps recording until you stop it."),
    ("Playback follows the show.",
     "<b>Follow timecode</b> in playback: a virtual soundcheck driven by the show&rsquo;s own code. Never during "
     "a take."),
    ("LTC and MTC for the desk.",
     "Play timecode on the LTC row&rsquo;s output, or MTC out, so a console or show controller can chase Show "
     "Recorder."),
]

SOUNDCHECK = [
    ("Out where it came in.",
     "One click sets every track&rsquo;s output to its input: the virtual soundcheck patch."),
    ("Soundcheck mute and solo.",
     "Beside each output: what plays to the console. They change nothing recorded or exported."),
    ("The desk follows the show.",
     "Scene recalls become markers during a take, named as the desk shows them; <b>Recall scenes in playback</b> "
     "puts the console in the right scene wherever you jump. On a dLive, a Wing or a DiGiCo SD, through MIDI "
     "Bridge."),
    ("Gapless, to the sample.",
     "Drag across the ruler to loop a section; <kbd>⇧L</kbd> switches it off and on. A take always runs straight "
     "through."),
]

AFTER = [
    ("A region for every song.",
     "<b>Find Songs</b> splits at the L/R Mix&rsquo;s quiet gaps, ready to rename. Run it again and the regions "
     "you placed are kept."),
    ("A mastering chain.",
     "EQ, compressor, tape, clipper and limiter on the master; EQ and a compressor on each bus. Every stage heard "
     "live."),
    ("Mix and stems, per song.",
     "WAV or MP3, normalized to a LUFS target under a true-peak ceiling if you like, with a CUE sheet for the "
     "whole show."),
    ("Loudness and phase.",
     "The FOH meter: momentary, short-term and integrated loudness, true peak and correlation, of the L/R Mix as "
     "it comes in, or the master in playback."),
]

KEYS = [  # 0.2.14's defaults (REFERENCE.md, "Keyboard shortcuts"): Console Control's since 0.2.7
    (["Space"], "Play / stop (a take: stop only)"),
    (["⌃⌥Space"], "Record"),
    (["Home"], "Go to start"),
    (["T"], "Go to a timecode or a time"),
    (["⌘N", "⌘O", "⌘S"], "New / open / save"),
    (["⌃⌥A", "⌃⌥D"], "Arm / disarm every track"),
    (["⇧A"], "Arm the selected tracks"),
    (["⌥M", "⌥⇧M"], "Marker / named marker"),
    (["[", "]"], "Previous / next marker or region"),
    (["⇧L"], "Loop off / on"),
    (["S"], "Split clips at the playhead"),
    (["⌃⌥R"], "Sync from Console"),
    (["⌃⌥P"], "Before You Record"),
    (["⌘E"], "Export"),
    (["⇧⌘M"], "Meters"),
    (["0", "3"], "Number pad: play-stop / record"),
]

TROUBLE = [
    ("var(--green)", "Zero", "Nothing lost: the disk, the interface and the engine all kept up."),
    ("var(--amber)", "A number", "Something cost the recording audio. Each is a &#9888; marker where it happened."),
    ("var(--red)", "NOT RECORDING", "The take&rsquo;s time stood still. Stop and start the take; if it happens "
                                    "again, a bigger buffer (Settings &rarr; Audio), and send the log."),
    ("var(--red)", "A red input", "Patched past the interface&rsquo;s inputs: it records nothing. Record names it."),
    ("var(--amber)", "Load amber or red", "The engine is near its deadline: a bigger buffer in Settings &rarr; "
                                          "Audio. It monitors nothing, so you hear no difference."),
]
TROUBLE_NOTE = ("<b>Something went wrong?</b> Click <b>Export log</b> in the footer: a diagnostics zip lands on your "
                "Desktop. Send it with <b>Send feedback</b> beside it, or to "
                f'<a href="{FEEDBACK}">dylan@dylanmaudio.com</a>. Nothing leaves your Mac unless you send it.')

THE_BETA = [
    ("Until the date, everything works.",
     "On any number of tracks. The end date is on the window from the first launch, and the last two weeks warn "
     "at every launch."),
    ("After the date, it opens, plays, edits and exports.",
     "Your sessions stay yours. It starts no new recording until you install the current version."),
    ("A show is never interrupted.",
     "The date is checked once, at launch: a session that runs past midnight on the last day keeps recording."),
    ("You need a Mac and an audio interface.",
     "macOS 11 or later, Apple Silicon. Any interface the Mac sees: Dante, MADI, USB. The MIDI Bridge 1.5 beta, in "
     "the download, for the console features. No analytics, no telemetry."),
]


def ctas(discord_label="Beta feedback"):
    return (f'<a href="{DOWNLOAD}" target="_blank" rel="noopener" class="btn btn-primary">Download the beta &mdash; free '
            f'<span class="arw">&rarr;</span></a>'
            f'<a href="{QUICK_REF}" class="btn btn-ghost" target="_blank" rel="noopener">Quick Reference (PDF) &#8599;</a>'
            f'<a href="{MANUAL}" class="btn btn-ghost" target="_blank" rel="noopener">Reference Manual (PDF) &#8599;</a>'
            f'<a href="{C.DISCORD_URL}" class="btn btn-discord" target="_blank" rel="noopener">{C.DISCORD_SVG} '
            f'{discord_label}</a>')


def build():
    p = dict(name=NAME, icon=ICON, gallery=True)
    title = f"{NAME} beta — Dylan [M] Audio"
    desc = (f"The {NAME} beta: multitrack recording for live shows, free until {BETA_UNTIL}. "
            "What it does, how to get it, and your first session.")
    seo = C.seo_head(f"{SLUG}/", title, desc, image=f"assets/{ICON}", noindex=True)
    features = "".join(f"<li>{P.CK}<span>{f}</span></li>" for f in FEATURES)
    glance = [("Version", VERSION), ("Beta until", BETA_UNTIL), ("Price", "Free during the beta"),
              ("Platform", "macOS 11+"), ("Chip", "Apple Silicon"),
              ("Interfaces", "Any the Mac sees: Dante, MADI, USB"),
              ("Console", "Any; names and scenes from the dLive, SQ, Wing and DiGiCo SD"),
              ("Needs", "MIDI Bridge 1.5 beta, in the download, for the console features")]
    glance_rows = "".join(f'<div class="srow"><span class="k">{k}</span><span class="v">{v}</span></div>'
                          for k, v in glance)

    guide = "".join([
        B.block(B.kick(f"New in {VERSION.replace(' BETA', '')}")
                + "<p>Since 0.2.14. The full list comes with the download.</p>" + B.items(NEW), "new"),
        B.block(B.kick("What it is")
                + "<p>A multitrack recorder for front of house, from any console through any audio interface. Built "
                  "to be left running for a whole show and trusted, with the after-show work in the same window.</p>"
                + B.items(WHAT)),
        B.block(B.kick("Your first session, in eight steps")
                + "<p>Set it up before doors, at the desk or at home with the interface.</p>"
                + B.steps(FIRST_SESSION), "start"),
        B.block(B.kick("Built to be left running all night")
                + "<p>What it does so you can watch the show, not the recorder.</p>" + B.items(SHOW_SAFE)),
        B.block(B.kick("Timecode, built in")
                + "<p>Patch the LTC row to the input carrying code, or follow MTC, and the header shows it: green "
                  "when locked.</p>" + B.items(TIMECODE)),
        B.block(B.kick("Virtual soundcheck, through the desk")
                + "<p>Every track plays back out its patched output: patch them to the console&rsquo;s inputs and "
                  "the show plays through the desk.</p>" + B.items(SOUNDCHECK)),
        B.block(B.kick("The mix and stems, before you leave")
                + "<p>The Mixer is the export mix: it never touches the recording or the console.</p>"
                + B.items(AFTER)),
        B.block(B.kick("The keys worth learning first")
                + "<p>Console Control&rsquo;s keys, since 0.2.7. Change any of them in Keyboard Shortcuts "
                  "(<kbd>⌃⌥K</kbd>), and hover over a button to see its key. All of them are in the "
                  f'<a href="{QUICK_REF}" target="_blank" rel="noopener">Quick Reference</a>.</p>'
                + B.keys(KEYS), "keys"),
        B.block(B.kick("Read the counter at the top of the window")
                + "<p>Zero in a quiet show. Click it for the details, and Reset.</p>"
                + B.states(TROUBLE, TROUBLE_NOTE)),
        B.block(B.kick(f"The beta, until {BETA_UNTIL}")
                + f"<p>This is {VERSION}: a full-featured beta. Every track, nothing switched off.</p>"
                + B.items(THE_BETA), "beta"),
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
<style>{P.CSS}{B.CSS}</style>
</head>
<body class="product">
{P.nav("software")}

<section class="p-hero">
  <div class="p-hero-inner">
    <div class="p-id">
      <img src="/assets/{ICON}" alt="{NAME} app icon" width="72" height="72" />
      <div>
        <h1>{NAME}</h1>
        <div class="p-badges"><span class="tag">Beta &middot; {VERSION.replace(' BETA', '')}</span></div>
      </div>
    </div>
    <p class="p-tagline">{TAGLINE} Free to try until {BETA_UNTIL}.</p>
    <div class="p-cta-row">{ctas()}</div>
    <p class="beta-note">The download is a free checkout on the store: the link comes by email, and <b>Check for
      Updates</b> in the app tells you when a new beta is out. For the console features &mdash; names, colours
      and scenes from the desk &mdash; <b>the MIDI Bridge 1.5 beta comes in the download</b>: install that too.
      Then see <a href="#new">what&rsquo;s new</a>, or start with <a href="#start">your first session</a>. The
      <a href="{QUICK_REF}" target="_blank" rel="noopener">Quick Reference</a> and the full
      <a href="{MANUAL}" target="_blank" rel="noopener">Reference Manual</a> are PDFs, also in the download.</p>
  </div>
</section>

{P.gallery_block(CARDS, p)}

<section><div class="wrap p-grid">
  <div class="p-body">
    <div class="kicker p-sec-k"><span class="tick">//</span>&nbsp; What it does</div>
    <p class="p-lead">{LEAD}</p>
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
  <span class="tick">//</span>&nbsp; {NAME} beta</div>
  <h2>Record your next show with it.</h2>
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
