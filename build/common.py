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
    # Talk Light Trigger: two variants (licence 2024669, free trial 2006006); validated 23 Sept.
    "talk-light-trigger": f"{STORE_URL}/checkout/buy/178c7256-4ba5-4269-9c0f-79876a37aee7?enabled=2024669",
    "talk-light-trigger-trial": f"{STORE_URL}/checkout/buy/5700dc17-83ae-4e2a-8534-29eaddbf51b6?enabled=2006006",
    # Pilot Tone Trigger: two variants (licence 2019975, free trial 2013072); validated 23 Sept.
    "pilot-tone-trigger": f"{STORE_URL}/checkout/buy/cc74ef8c-6c9c-449d-89da-c8ebbeff1d9c?enabled=2019975",
    "pilot-tone-trigger-trial": f"{STORE_URL}/checkout/buy/f1b17f98-2bed-4bef-be31-bf1f0cfb2c5d?enabled=2013072",
    # Time Code Tool: the store product has two variants; `?enabled=<variant>`
    # restricts the checkout to one of them (licence 2024673, free trial 2013074).
    "time-code-tool": f"{STORE_URL}/checkout/buy/a60bb362-a29b-49fa-83c4-e1d65a9d9b6a?enabled=2024673",
    "time-code-tool-trial": f"{STORE_URL}/checkout/buy/52a61e9a-34cd-4ee7-88ca-c859e14fd365?enabled=2013074",
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
        seo_title="MIDI Bridge — free dLive MIDI bridge with a decoded monitor",
        seo_desc=("Free MIDI between your Mac and the dLive, with real connection status, plain-language "
                  "errors and a live MIDI Monitor that decodes what's on the wire."),
        tagline="Free MIDI between your Mac and the dLive — with a status light that means it.",
        lead=("Real connection status, plain-language errors, and a monitor that reads every fader, mute, "
              "Scene, EQ and send in console language instead of hex. One connection your DAW, the other "
              "dylanmaudio apps and Bitfocus Companion all share. The bridging half of Allen &amp; Heath's "
              "MIDI Control app, with the parts it leaves out."),
        features=[
            "\"Connected\" means the console is answering — checked every few seconds, reconnects by itself",
            "Errors in words — base-channel mismatch named with the fix, port clashes named with the program",
            "Live MIDI Monitor in console language, not hex — faders, mutes, Scenes, EQ, HPF, sends, preamp",
            "Colour-coded by the program that sent it; copy any row's raw MIDI",
            "\"dLive Bridge\" virtual ports for any DAW; complete fader moves back through the Return port",
            "One shared console connection for your DAW and the other apps",
            "Free — no licence, no trial timer",
        ],
        specs=["MIDI over TCP", "MIDI monitor", "connection status", "shared connection", "NRPN decoded", "free"],
        # Long-form page copy. Source: dylanmaudio-marketing,
        # briefs/done/midi-bridge-copy-draft.md §3 (written against 1.2.1).
        longform=dict(
            story=dict(
                kicker="Why I built it",
                paras=[
                    "Allen &amp; Heath&rsquo;s own MIDI Control app does the job: it makes the ports and connects "
                    "them to the desk. What it doesn&rsquo;t do is tell you anything. There&rsquo;s no status "
                    "beyond opening the app and looking, no error reporting, and no diagnostics &mdash; a button "
                    "flashes for in and a button flashes for out, and that&rsquo;s the monitoring. I&rsquo;m a "
                    "believer in watching MIDI traffic; as rigs get more complex, with software and hardware "
                    "talking over the same wire, a monitor is how you trace signal flow. But every monitor I "
                    "used showed NRPNs and hex. I like the number structures. Most people, reasonably, "
                    "don&rsquo;t &mdash; and that&rsquo;s where a setup stalls. So this decodes everything into "
                    "console language, tags every message with the program that sent it, tells you the moment "
                    "the connection drops and why, and reconnects on its own. Then, as I built the other apps, "
                    "it made sense for all of them to share this one connection and report through it.",
                ],
            ),
            what=dict(
                kicker="In detail",
                items=[
                    ("Connection status that means something.",
                     "The menu-bar disc shows stopped, connecting, connected or error, with a flash for activity "
                     "&mdash; and &ldquo;Connected&rdquo; only once the console is actually answering. The bridge "
                     "checks straight away and every few seconds, shows &ldquo;Waiting for a reply from &hellip;&rdquo; "
                     "until it does, notices within about 20 seconds if the console stops, and reconnects by itself."),
                    ("Errors in words.",
                     "A base-channel mismatch is named, with the channel to switch to. A port clash names the "
                     "program holding it and how to fix it. The panel says so if the running bridge is on a "
                     "different address from the one in the fields."),
                    ("A MIDI Monitor that speaks console.",
                     "Every fader, mute, Scene and Action crossing the wire in plain language, colour-coded by the "
                     "program that sent it, with a filter to show just one. Parametric EQ, HPF, aux, FX and matrix "
                     "sends, preamp gain, pad and 48V, names, colours and assignments each read as what they are "
                     "&mdash; &ldquo;Input 3 HPF &rarr; ~85 Hz&rdquo; &mdash; with their own filter. Advanced mode "
                     "shows the full detail, and any row&rsquo;s raw MIDI is one Cmd-click to copy."),
                    ("One connection for everything.",
                     "Your DAW, the other dylanmaudio apps and Bitfocus Companion share MIDI Bridge&rsquo;s "
                     "connection to the console instead of each opening their own, so there&rsquo;s one thing to "
                     "check when something goes quiet. The log names every app that connects, when it leaves, and "
                     "any message refused after its connection closed."),
                    ("Works with any DAW, no drivers.",
                     "&ldquo;dLive Bridge&rdquo; MIDI ports that Reaper, Logic, Ableton Live or any MIDI app can use "
                     "straight away. Fader moves made on the desk come back complete through the Return port, so "
                     "automation records what the engineer actually did."),
                    ("A log for afterwards.",
                     "Every session is logged; Export log puts a copy on your Desktop, so &ldquo;it stopped working "
                     "after a couple of minutes&rdquo; has something to show."),
                    ("Set it and forget it.",
                     "Starts at login, an optional Dock icon, Check for updates only when you press it, and the "
                     "Quick Reference installed with the app."),
                    ("Stream Deck control &mdash; coming soon.",
                     "Start, stop and restart the bridge, and run the console, from Bitfocus Companion buttons that "
                     "show the bridge&rsquo;s state."),
                ],
            ),
            who=dict(
                kicker="Who uses it",
                paras=[
                    "Anyone with a dLive and a Mac: engineers recording console automation into a DAW, show-control "
                    "operators, anyone trying to work out why a MIDI setup has gone quiet &mdash; and everyone "
                    "running the other dylanmaudio apps, which connect through it.",
                ],
            ),
            faq=dict(
                kicker="Questions",
                items=[
                    ("Is this a replacement for Allen &amp; Heath MIDI Control?",
                     "For getting MIDI between a Mac and the console, yes &mdash; with connection status, error "
                     "reporting and a decoded monitor that MIDI Control doesn&rsquo;t have. It does not do MIDI "
                     "Control&rsquo;s HUI / Mackie Control emulation for driving a DAW from the desk surface; if you "
                     "use that, keep it."),
                    ("Why does the monitor matter?",
                     "Because a dLive fader move is three NRPN messages, and an EQ change looks the same in hex. "
                     "Reading them by hand is how setups stall. The monitor reads them for you, and tags who sent "
                     "them."),
                    ("Does it work with the other dylanmaudio apps?",
                     "They connect through it, share its console connection and show up by name in the monitor "
                     "and the log."),
                    ("Does it work with other consoles?",
                     "It&rsquo;s built for the dLive, and users report it works on Allen &amp; Heath Avantis as "
                     "well &mdash; I haven&rsquo;t tested that myself yet. Other consoles are being looked into "
                     "&mdash; <a href=\"/#contact\">register your interest</a> and say which desk."),
                    ("Windows? Intel Macs?",
                     "Built for Apple Silicon. From this version the app also installs and runs on Intel Macs &mdash; verified so far in a VM, with testing on Intel hardware in October &mdash; so if you&rsquo;re on Intel, try the free download and tell me how it goes. Windows is being looked into &mdash; <a href=\"/#contact\">register your interest</a>."),
                    ("Does it phone home?",
                     "No analytics, no telemetry. Check for updates runs only when you press it. There&rsquo;s no "
                     "licence and no trial timer."),
                ],
            ),
        ),
    ),
    "talk-light-trigger": dict(
        name="Talk Light Trigger", abbr="TLT", tag="dLive", accent="blue",
        icon="talk-light-trigger.png", affiliated=True, status="buy", trial=True, price="$19",
        store=CHECKOUT["talk-light-trigger"], trial_store=CHECKOUT["talk-light-trigger-trial"], youtube="jP2Yyvd1uq4",
        sale=dict(now="$9", was="$19", code="TLTINTROSALE",
                  until="2026-10-31", until_label="31 October 2026"),
        seo_title="Talk Light Trigger — talkback light for dLive, no hardware",
        seo_desc=("Turn your dLive's own surface lights into a talkback or shout light: someone talks on the "
                  "shout bus, the desk flashes. Cancel from a SoftKey. Free trial."),
        tagline="A talkback light for your dLive, from the console's own lights.",
        lead=("Someone talks on the shout bus, the surface flashes, you put the headphones on. Nothing to rig; "
              "one SoftKey to cancel. Talk Light Trigger watches a talkback mic or the shout bus and flashes "
              "the dLive's own surface lights while someone is talking &mdash; a talkback light, shout light "
              "or call light for the FOH engineer who can't hear the stage until the headphones go on, and "
              "for anyone who talks on cue."),
        features=[
            "The console's own lights flash when someone talks on the talkback mic or shout bus — no extra hardware",
            "Flash Rate and Flash Hold — the lights actually flash, and keep going for a few seconds after a pause",
            "Cancel SoftKey — one press on the desk stops the flash; it resumes if they're still talking",
            "Threshold trigger on any audio input — Dante, SoundGrid, MADI, USB, Thunderbolt, PCIe",
            "Tunable sensitivity — no chattering on breaths and pauses",
            "Recall Filter to illumination only, so nothing else on the console changes",
            "Full-featured 20-minute trial",
        ],
        specs=["talkback light", "shout light", "signal → trigger", "tally", "menu bar"],
        # Long-form page copy. Source: dylanmaudio-marketing,
        # briefs/done/talk-light-trigger-copy-draft.md §3 (written against 1.1.2).
        longform=dict(
            story=dict(
                kicker="Why I built it",
                paras=[
                    "I was mixing FOH without a shout box. The old one hadn&rsquo;t been loud, but it had a "
                    "signal light, and that was the useful part: when the light came on I knew someone on "
                    "stage wanted me, and I&rsquo;d get closer or put the headphones on. Then it broke "
                    "mid-tour. The crew could talk all they liked; I couldn&rsquo;t hear them until the "
                    "headphones went on, and I had no way of knowing when that was &mdash; short of them "
                    "texting me and hoping I&rsquo;d look down. So I sent every talkback mic to a bus, and "
                    "wrote something that watches that bus and flashes the console when there&rsquo;s signal "
                    "on it. The dLive has the lights already. It just needed telling when.",
                ],
            ),
            what=dict(
                kicker="In detail",
                items=[
                    ("Watches the shout bus.",
                     "Any talkback mic, or a bus carrying all of them, on any input of any interface the Mac "
                     "can see &mdash; Dante, SoundGrid, MADI, USB, Thunderbolt, PCIe."),
                    ("Flashes the console&rsquo;s own lights.",
                     "When signal crosses your threshold it recalls a &ldquo;talk&rdquo; Scene; when it stops, a "
                     "&ldquo;quiet&rdquo; Scene. Each Scene carries a different Surface Illumination, and its "
                     "Recall Filter is set to illumination only, so nothing else on the desk changes. Flash "
                     "Rate alternates the two so the lights really flash; Flash Hold keeps them going for a "
                     "few seconds after a pause."),
                    ("Cancel from a SoftKey.",
                     "Assign a SoftKey to Custom MIDI &mdash; the panel shows you the exact string to type "
                     "&mdash; and one press stops the flash the instant you&rsquo;ve seen it. If they&rsquo;re "
                     "still talking after the cooldown, it comes back."),
                    ("Doesn&rsquo;t chatter.",
                     "Threshold, attack, release and a minimum retrigger time, tuned to the voice and the room, "
                     "so breaths and pauses don&rsquo;t set it off."),
                    ("Tells you if the lights stop.",
                     "If Scenes stop reaching the console the panel turns red and says why. Through MIDI Bridge "
                     "it reconnects by itself after a quiet spell. The session log records every Scene sent, "
                     "every failure and every Cancel press, so an exported log shows what happened."),
                    ("Gentle on the show interface.",
                     "One input channel, a large buffer, and it never changes the sample rate."),
                    ("Connects the way you already do.",
                     "Direct TCP to the console with nothing else installed, or through the free MIDI Bridge. "
                     "(The Cancel SoftKey needs a connection that can receive &mdash; Direct TCP, or a two-way "
                     "MIDI port.)"),
                    ("Stream Deck control &mdash; coming soon.",
                     "Run and Threshold as Bitfocus Companion buttons, with the talk state fed back."),
                ],
            ),
            who=dict(
                kicker="Who uses it",
                paras=[
                    "FOH and monitor engineers who can&rsquo;t hear the stage until the headphones go on. Anyone "
                    "running a shout system, or who lost theirs. Podium, pit and booth setups where a mic going "
                    "live should show on the desk. And as a plain call light: any signal on any input, and the "
                    "console lights up.",
                ],
            ),
            faq=dict(
                kicker="Questions",
                items=[
                    ("Does it need a shout box?",
                     "No &mdash; that&rsquo;s the point. It needs a talkback mic (or the bus they&rsquo;re all on) "
                     "reaching an input the Mac can see, and a dLive on the network."),
                    ("Will it change anything else on the console?",
                     "Not if the two Scenes&rsquo; Recall Filters are set to Surface Illumination only, which is "
                     "the setup the Quick Reference walks through. The Scenes then touch the lights and nothing "
                     "else."),
                    ("How do I stop it flashing once I&rsquo;ve seen it?",
                     "A SoftKey. Set it to Custom MIDI with the string the panel shows and one press cancels the "
                     "flash; it resumes after the cooldown if they&rsquo;re still talking."),
                    ("Can I use it as a cue light or a call light?",
                     "Yes. It doesn&rsquo;t know what the signal is &mdash; any input crossing the threshold "
                     "lights the desk."),
                    ("What does it need?",
                     "A dLive; a Mac on the console&rsquo;s network (Direct TCP, or through MIDI Bridge); the "
                     "talkback signal on any audio input; and two Scenes on the console with different Surface "
                     "Illumination."),
                    ("Does it work with other consoles?",
                     "It&rsquo;s built for the dLive, and users report it works on Allen &amp; Heath Avantis as "
                     "well &mdash; I haven&rsquo;t tested that myself yet. Other consoles are being looked into "
                     "&mdash; <a href=\"/#contact\">register your interest</a> and say which desk."),
                    ("Windows? Intel Macs?",
                     "Built for Apple Silicon. From this version the app also installs and runs on Intel Macs &mdash; verified so far in a VM, with testing on Intel hardware in October &mdash; so if you&rsquo;re on Intel, try the free trial and tell me how it goes. Windows is being looked into &mdash; <a href=\"/#contact\">register your interest</a>."),
                    ("Does it phone home?",
                     "No analytics, no telemetry. Activating the licence is the only network call; Check for "
                     "updates runs only when you press it. A licence covers two Macs &mdash; show machine and "
                     "spare."),
                ],
            ),
        ),
    ),
    "pilot-tone-trigger": dict(
        name="Pilot Tone Trigger", abbr="PTT", tag="dLive", accent="blue",
        icon="pilot-tone-trigger.png", affiliated=True, status="buy", trial=True, price="$59",
        store=CHECKOUT["pilot-tone-trigger"], trial_store=CHECKOUT["pilot-tone-trigger-trial"], youtube="GOfFZzGTEuA",
        seo_title="Pilot Tone Trigger — playback &amp; Waves failover for dLive",
        seo_desc=("Automatic failover for Allen & Heath dLive. A pilot tone drops and the console switches to "
                  "your backup rig or pulls the inserts-out scene. Free trial."),
        tagline="Automatic failover for your dLive, in software.",
        lead=("A pilot tone drops — a playback machine, a Waves server, a plugin host — and the console "
              "switches to the backup you already built. No switching hardware. Pilot Tone Trigger listens "
              "for a pilot tone on the path you can't afford to lose and the instant it drops recalls a "
              "Scene, fires an Action, or both: main/backup playback switched at the console, or the "
              "\"inserts out\" scene for a dead Waves server, pulled automatically."),
        features=[
            "Detects loss of a pilot tone on any critical path — playback, Waves / SoundGrid, plugin hosts, outboard",
            "Switches the console to your backup in milliseconds — a Scene, an Action, or both",
            "Main / backup playback with no switching hardware — an Action moves the input source from Preamp A to B",
            "Pulls the \"inserts out\" scene when SuperRack, LiveProfessor, Gig Performer or MainStage dies",
            "Signal Integrity — catches a tone that's present but damaged, and warns or fails over",
            "Automatic failback, latch until you reset, or Flip A/B by hand",
            "Fails safe — stopping the app never fires a failover",
            "Full-featured 20-minute trial",
        ],
        specs=["auto-failover", "redundant playback", "Waves failover", "pilot tone", "signal integrity"],
        # Long-form page copy. Source: dylanmaudio-marketing,
        # briefs/done/pilot-tone-trigger-copy-draft.md §3 (written against 1.1.1).
        longform=dict(
            story=dict(
                kicker="Why I built it",
                paras=[
                    "Playback redundancy has always meant hardware. A Radial SW8 is excellent, but it&rsquo;s "
                    "about $1,400, it&rsquo;s heavy, it switches eight analog channels, and it sits between the "
                    "interfaces and the desk &mdash; and everyone knows D-subs are a pain. The PlayAUDIO boxes do "
                    "a similar job for around $1,200; the Dante-capable DirectOut unit is over $3,000. All of "
                    "them need a hardware interface on each machine, and the analog ones can&rsquo;t switch a "
                    "source that arrives at the console digitally. On a dLive you can already build the backup "
                    "&mdash; an Action that moves each channel&rsquo;s input source to the B machine, or a Scene "
                    "that takes every insert out when the plugin server dies. What was missing was something "
                    "that fires it faster than a person can. So I wrote that.",
                ],
            ),
            what=dict(
                kicker="In detail",
                items=[
                    ("Listens for a pilot tone.",
                     "A continuous tone on the path you can&rsquo;t afford to lose &mdash; from the app&rsquo;s own "
                     "generator or your own. Any input on any interface the Mac can see (Dante, SoundGrid, MADI, "
                     "Thunderbolt, USB, PCIe), on any channel."),
                    ("Fires your backup when it drops.",
                     "A Scene recall, a console Action, or both, sent to the dLive in milliseconds. You build the "
                     "backup once, on the console, the way you&rsquo;d build it anyway."),
                    ("Main and backup playback, no switching hardware.",
                     "Both playback machines feed the console directly &mdash; over Dante Virtual Soundcard, the "
                     "SoundGrid driver, or any interface. The Action switches each channel&rsquo;s input source "
                     "from Preamp A to B. Whatever the tracks run in &mdash; Ableton Live, Reaper, Logic, Cubase "
                     "&mdash; makes no difference."),
                    ("The &ldquo;inserts out&rdquo; scene, automated.",
                     "If you mix through SuperRack, SuperRack Performer, LiveProfessor, Gig Performer, MainStage "
                     "or another plugin host, you already have the Scene that bypasses every insert. Pilot Tone "
                     "Trigger pulls it the instant the server stops passing the tone."),
                    ("Checks the tone is clean, not just present.",
                     "Signal Integrity watches how much of the incoming audio actually sits at the tone&rsquo;s "
                     "frequency, so clicks, dropouts, noise, clipping and a garbled tone all show up &mdash; the "
                     "ways a digital path degrades before it fails outright. Warn only, or fail over. Off by "
                     "default; tune it to your own rig."),
                    ("Fail back your way.",
                     "Automatically when the tone returns, or hold on the backup until you press Reset &mdash; so "
                     "the desk never flips back onto a source that just failed. Reset won&rsquo;t fire while the "
                     "tone is still missing. Flip A/B switches by hand any time, whatever the detector thinks."),
                    ("Catches a feed that&rsquo;s already dead.",
                     "Press Start on a path that&rsquo;s already down and it fails over immediately."),
                    ("Fails safe.",
                     "Stopping the app, or the trial ending, sends nothing to the console. If the Mac running it "
                     "dies, nothing is sent either &mdash; the show stays exactly where it was."),
                    ("Know it works before doors.",
                     "Test Connection confirms the console is answering. The menu-bar icon shows tone present, "
                     "tone lost, degraded, and restored but still on the backup."),
                    ("Gentle on the show interface.",
                     "One input channel, a large buffer, and it never changes the sample rate."),
                    ("Stream Deck control &mdash; coming soon.",
                     "Run, failback mode, Reset and the tone generator as Bitfocus Companion buttons, with the "
                     "app&rsquo;s state shown back."),
                ],
            ),
            who=dict(
                kicker="Who uses it",
                paras=[
                    "Playback engineers and techs running tracks into a dLive; FOH and monitor engineers mixing "
                    "through Waves or a native plugin host; theatre and worship productions with a backup machine "
                    "and nobody spare to watch it. It needs a dLive, a Mac on the network, and the backup path "
                    "already patched to the console.",
                ],
            ),
            faq=dict(
                kicker="Questions",
                items=[
                    ("Does this replace a Radial SW8 or an iConnectivity PlayAUDIO?",
                     "For a dLive, yes &mdash; that&rsquo;s what it&rsquo;s for. Those boxes switch analog outputs "
                     "upstream of any console, and if that&rsquo;s what you need, they&rsquo;re the right tool. "
                     "Pilot Tone Trigger switches at the console instead, so it costs nothing in hardware, works "
                     "with digital sources, and needs the backup path patched to spare inputs."),
                    ("My playback comes in over Dante Virtual Soundcard. Can hardware switchers handle that?",
                     "Not the analog ones. This can: the tone is just another channel, and the switch happens on "
                     "the console."),
                    ("What happens when the Waves server crashes mid-show?",
                     "If it stops passing the tone, Pilot Tone Trigger fires the Scene you&rsquo;ve built with every "
                     "insert out. Audio carries on through the console; nobody has to find the panic button."),
                    ("Isn&rsquo;t another computer just another thing that can fail?",
                     "If Pilot Tone Trigger stops &mdash; or the Mac does &mdash; nothing is sent, and the console "
                     "stays on the main rig exactly as it was. It can only ever fire the backup you built."),
                    ("How fast is it?",
                     "The detector&rsquo;s defaults are a 50 ms dropout hold and a 30 ms envelope release, so the "
                     "switch is sent in milliseconds. A measured end-to-end figure on a console is coming."),
                    ("What does it need?",
                     "A dLive, a Mac on the console&rsquo;s network (Direct TCP, or through the free MIDI Bridge), a "
                     "pilot-tone feed into any audio input, and the backup &mdash; a Scene, an Action, or both "
                     "&mdash; built on the console."),
                    ("Does it work with other consoles?",
                     "It&rsquo;s built for the dLive. Users report it works on Allen &amp; Heath Avantis with "
                     "Scene recall &mdash; Actions are a dLive feature &mdash; though I haven&rsquo;t tested that "
                     "myself yet. Other consoles are being looked into &mdash; <a href=\"/#contact\">register "
                     "your interest</a> and say which desk. (Time Code Tool already works with anything.)"),
                    ("Windows? Intel Macs?",
                     "Built for Apple Silicon. From this version the app also installs and runs on Intel Macs &mdash; verified so far in a VM, with testing on Intel hardware in October &mdash; so if you&rsquo;re on Intel, try the free trial and tell me how it goes. Windows is being looked into &mdash; <a href=\"/#contact\">register your interest</a>."),
                    ("Does it phone home?",
                     "No analytics, no telemetry. Activating the licence is the only network call; Check for updates "
                     "runs only when you press it, and nothing goes online while a trigger is armed. A licence "
                     "covers two Macs &mdash; show machine and spare."),
                ],
            ),
        ),
    ),
    "time-code-tool": dict(
        name="Time Code Tool", abbr="TxT", tag="Universal", accent="blue",
        icon="time-code-tool.png", affiliated=False, status="buy", trial=True, price="$69",
        store=CHECKOUT["time-code-tool"], trial_store=CHECKOUT["time-code-tool-trial"], youtube="A6iKjxHxXA4",
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
              "any console or application that needs timecode."),
        features=[
            "Read + monitor LTC or MTC — lock, frame rate, freewheel, missed / misread / jumped frames",
            "Convert in any direction — LTC → MTC, MTC → LTC, LTC → LTC, MTC → MTC — or both outputs at once",
            "Frame-rate conversion on either output (23.976 / 24 / 25 / 29.97 DF / NDF / 30)",
            "Generate mode — LTC and MTC from one clock; render sample-accurate LTC to a WAV",
            "Virtual audio and MIDI ports, in and out — timecode between apps on one Mac",
            "Works with any console or application that needs timecode — audio, lighting, video, playback, pyro",
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
                    ("Stream Deck control &mdash; coming soon.",
                     "Transport, mode, inputs and outputs and the generator as Bitfocus Companion buttons, "
                     "with the live timecode, lock state and frame rate shown back on the deck."),
                ],
            ),
            who=dict(
                kicker="Who uses it",
                paras=[
                    "Anyone who sends or chases timecode from a Mac: playback engineers running Ableton Live "
                    "or Reaper; lighting programmers whose software wants MTC when the show sends LTC; video "
                    "and media-server operators; theatre sound with QLab; pyro and show control; FOH and "
                    "monitor engineers running timecode-driven console automation. It doesn&rsquo;t care what "
                    "console, desk or application is on the other end.",
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
                     "Built for Apple Silicon. From this version the app also installs and runs on Intel Macs &mdash; verified so far in a VM, with testing on Intel hardware in October &mdash; so if you&rsquo;re on Intel, try the free trial and tell me how it goes. Windows is being looked into &mdash; <a href=\"/#contact\">register your interest</a>."),
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
