# Changelog — Pilot Tone Trigger (dLive)

Customer-facing version history. Mirrors the Changelog section on the
Lemon Squeezy product page — keep the two in sync (entries below are
written to be copy/pasted there verbatim, minus this header).

One entry per PUBLIC release. The top entry is the release being
prepared: until it ships, keep adding to it and keep its version in step
with setup.py — the build prints it on the Quick Reference cover (first
six bullets, so the most important go first) and in every build's
changelog PDF. Notes on builds that never ship go in BUILD-HISTORY.md.

Note: the public launch was v1.0.5. Everything before it was internal —
those entries are kept below as the history of what launched.

v1.2.0
- Now runs on macOS 11 Big Sur or later, as the store page has always
  said. Earlier versions needed macOS 13.3 or later — on macOS 11 to
  13.2 the app failed to open, with no message.
- Fixed: on macOS 15 Sequoia, Pilot Tone Trigger could fail to reach the
  console over Direct TCP ("No route to host") without ever asking for
  Local Network permission, because macOS was mistaking it for another
  dylanmaudio app. Each app now has its own identity, so macOS asks
  once: click Allow (if the first Run gives up while the question is on
  screen, press Run again). If the connection is still blocked, the
  message now says where to switch it on: System Settings → Privacy &
  Security → Local Network.
- Fixed: when sending through MIDI Bridge, a failover that came more
  than two minutes after pressing Start could fail to reach the console,
  with "Send failed" in the status panel. MIDI Bridge closes a
  connection that has been quiet for two minutes, and Pilot Tone Trigger
  did not reconnect. It now reconnects by itself and the failover goes
  out as normal. Direct TCP and plain MIDI ports were not affected.
- Fixed: when the Mac's audio system resets — installing an audio driver
  does this (Time Code Tool's installer is one), and so can waking from
  sleep — the input could stop for good, so a real dropout after that
  would have gone unseen; Start could fail every time with "Internal
  PortAudio error [PaErrorCode -9986]" until you quit and reopened the
  app; and a playing tone could stop, refuse to restart, or carry on
  from a different device. The app now notices a reset within about 2
  seconds and reopens the input and the tone on the devices you chose,
  keeping the Latch as it was and sending nothing to the console. A
  silent input right after a reset is retried every second, and a tone
  that stops for any other reason is reopened within 3 seconds. If
  macOS's own audio system stays stuck — seen only when forcing many
  resets in a row — the panel turns red with "macOS audio stuck — quit
  and reopen" instead of the app freezing on "Starting…".
- Failures now show. If an Action or Scene fails to send while running,
  the status panel turns red — "Not reaching the console", with the
  reason — and stays red until a send gets through; if the audio input
  stops and can't be reopened, it turns red with "Not monitoring the
  tone". Before, a "Send failed" message was overwritten by the next
  level update a fraction of a second later, so a failover that never
  reached the console could look fine. Errors that need you stay until
  you deal with them; messages about something the app has already
  handled show for a few seconds and clear. The green "Connected" from
  Test Connection is cleared when you press Start, and a status message
  too long for the panel shows in full when you hover over it.
- New: the panel shows which side the console is on — "On Primary (A)"
  in blue or "On Backup (B)" in red, in the bar under Start — going by
  the last Action or Scene that actually reached the console, so a
  manual Flip, a Signal Integrity failover or a failed send all show as
  they really are. Right after Start it reads "not switched since
  Start", since Start sends nothing. When the app is latched and the
  tone is back, the bar turns amber and becomes "Reset to Primary", and
  Reset works on the first click.
- New: Flip A/B — a button at the top of the panel that switches to the
  other side right now, whatever either check currently thinks, any time
  the app is running. It goes by the side the console was last switched
  to, and after a Flip to B the panel says "Held on Backup".
- New: Signal Integrity — beyond checking the tone is present at the
  right level, the app can now check it's actually clean (not corrupted
  by clicks, dropouts, noise or a garbled signal). Off by default; the
  Purity Threshold, Hold and Retrigger sliders start at conservative
  values meant to be tuned to your own signal chain, not treated as
  correct out of the box. Choose "Warn only" to just be told about it,
  or "Also fail over" to switch to backup the same as a real dropout.
  Signal Degraded has its own colour, purple, in the status panel and on
  the menu bar icon.
- New, off by default: "Don't fail over for a Mac audio reset", under
  Failback. A Mac audio reset — an audio driver install, or sleep/wake —
  silences the input for a moment, which reads as a dropout. With this
  on, a dropout is held only when macOS itself reports that its audio
  system has just restarted; any other dropout fails over exactly as
  before, with no delay. The hold ends the moment the tone returns
  (nothing is sent), fails over as soon as the audio is back without the
  tone, and never lasts more than 5 seconds. Every dropout near a reset
  is logged with the timing, whether or not the option is on.
- Tone generator: a new Output Channel field sends the tone to one
  channel of a multi-channel output device, instead of always the first.
  Start / Stop Tone also sits beside Flip A/B at the top of the panel,
  and both buttons always show what the tone is doing. Changing the
  tone's output device or channel while it plays moves it straight away,
  and a tone output device that isn't found gets the same "is it
  connected? Use Rescan" wording as the input.
- Fixed: the Audio Input and Tone Generator channels could not be set
  above 64, so channels on a larger interface (Dante, MADI) were out of
  reach. Both Channel boxes now go up to the last channel of the device
  each one is set to — a channel you saved earlier for a bigger
  interface is left alone, not quietly reduced, so it is still there
  when you plug that interface back in — and if you pick one the device
  hasn't got, the message says so plainly.
- New: Options — Start at login, Show in Dock and Check for updates live
  together behind one disclosure at the bottom of the panel. Show in
  Dock puts Pilot Tone Trigger in the Dock and in Cmd-Tab for easier
  switching; it is off by default. Check for updates tells you whether a
  newer version is on the store, with a link to get it. It only checks
  when you press it, never on its own and never while Pilot Tone Trigger
  is running, and it sends nothing about you or your Mac.
- The Quick Reference guide is now installed with the app, so the
  footer's Quick Reference link opens it even with no internet — and it
  always matches the version you are running. The app's title and
  version stay in view while you scroll, and the panel sizes itself to
  the screen it is on instead of clipping its footer on shorter
  displays.
- On macOS 11 and 12, the panel now shows all its colours — the Signal
  Lost, Latched and Degraded status colours, the trial banner and the
  blue accents were missing there, because those Macs' web engine didn't
  understand how they were written — and the first click after opening
  the panel works: before, it only brought the app forward, and a
  right-click showed a bare "Reload" menu. Nothing changes on macOS 13
  or later.
- Export log now saves a diagnostics zip to your Desktop and shows it in
  Finder — this session's log, the previous session's, and your settings
  (licence details removed) — so one attachment covers a bug report. The
  session log itself now records your settings and where the app is
  running from at launch (a copy still running from the DMG is called
  out, since settings don't stick there), the audio and MIDI devices
  present and any change to that list, each setting you change, every
  Start with the settings in force and every Stop with why and a tally
  of sends, every failover and signal-OK actually sent to the console
  (and any that failed), the latch engaging and each Reset and Flip, a
  Start or console connection that fails and why, your licence or trial
  state, and a final line when you quit.
- Fixed: a damaged settings file was silently replaced with the defaults
  on the next save. It is now set aside under a dated name, the log says
  so, and the app runs on defaults until you set things again.
- Smaller fixes: moving the Threshold slider no longer sends its value
  to the Failback control as well; pressing Start while already running
  restarts cleanly instead of leaving the first run's audio stream and
  console connection alive underneath the new one; if the device or MIDI
  port list can't be read, the dropdown says "Couldn't list devices —
  Rescan" and keeps your saved choice; and the Signal Lost caption says
  "console on backup" rather than "failover CC sent" — while latched, a
  further dropout sends nothing.

v1.0.5
- Tidier popover: the Bitfocus Companion settings and the on-screen hints now
  sit behind disclosures, closed by default (a green dot on the Companion
  header shows when Companion is connected); the trademark notice at the
  bottom has gone — it's in the Quick Reference and the licence. Companion
  can now also bring the app's window forward.
- New: this app can now be controlled from Bitfocus Companion — Run,
  Failback mode, Reset, and the tone generator all show up as Companion
  buttons, with the app's own state reflected back on them. On by
  default; two new switches in the app let you turn Companion control
  off or lock the show-critical ones.

v1.0.4
- Improved: the app now opens just the one input channel you chose, with
  a large audio buffer, and never changes the interface's sample rate —
  so it costs the show's audio interface as little as a second app can.
  The channel, rate and buffer are written to the session log when the
  input opens.
- Clearer message when the chosen channel doesn't exist on the device,
  instead of a cryptic driver error.
- New: every session now writes a log, and a new Export log button in
  the footer saves a copy to your Desktop — so if something goes wrong at a
  show, there is evidence to send, without instructions.
- New installs default to CC 85 for both messages — Pilot Tone Trigger's
  own number in the dylanmaudio suite, so it never shares a control
  number with show automation. Existing settings are not changed.
  Program the console's Actions for CC 85 value 127 (tone present) and
  value 0 (tone lost).

v1.0.3
- Pilot Tone Trigger now installs into a "dylanmaudio" folder inside Applications,
  alongside the other dylanmaudio apps, instead of sitting loose in
  Applications. Updating moves your existing copy for you.
- The download is now an installer you double-click, rather than a disk
  image you drag from.

v1.0.2
- New: a footer link to the app's Quick Reference guide, so the guide is
  always a click away instead of only being on the disk image.
- New: send feedback from inside the app — a short message straight to
  me, no email client or web form needed.
- New: a link to the other dLive utilities.
- Fixed: a stray highlight box that appeared around the first section
  heading when the window opened.

v1.0.1
- When used with MIDI Bridge, this app now identifies itself by name
  in the bridge's MIDI Monitor instead of appearing as a generic DAW
  connection.

v1.0.0 - Initial Release
