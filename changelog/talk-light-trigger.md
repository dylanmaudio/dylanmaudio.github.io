# Changelog — Talk Light Trigger (dLive)

Customer-facing version history. Mirrors the Changelog section on the
Lemon Squeezy product page — keep the two in sync (entries below are
written to be copy/pasted there verbatim, minus this header).

One entry per PUBLIC release. The top entry is the release being
prepared: until it ships, keep adding to it and keep its version in step
with setup.py — the build prints it on the Quick Reference cover (first
six bullets, so the most important go first) and in every build's
changelog PDF. Notes on builds that never ship go in BUILD-HISTORY.md.

Note: the public launch was v1.0.7 (16 September 2026), updated to
v1.0.8 the same week. Everything from v1.0.0 to v1.0.6 was internal —
those entries are kept below as the history of what launched.

v1.2.0
- Now runs on macOS 11 Big Sur or later, as the store page has always
  said, and natively on Intel Macs as well as Apple Silicon. Earlier
  versions needed macOS 13.3 or later — on macOS 11 to 13.2 the app
  failed to open, with no message — and on an Intel Mac they installed
  but could not run.
- New: the lights now flash. While talkback is active the app alternates
  the Quiet and Talkback Scenes at a Flash Rate you set, instead of
  holding on the Talkback Scene. Flash Hold keeps them flashing for a
  set time after talkback stops (3 seconds by default; 0 is Off, to
  follow the microphone exactly), so a short pause doesn't cut them off,
  and talking again inside the hold just keeps the flash going.
- New: cancel the flash. The Cancel flash button under Start/Stop — or a
  console SoftKey assigned to Custom MIDI — turns the lights dark at
  once; flashing resumes on its own after a cooldown you set if talkback
  is still going. The Cancel SoftKey section shows the exact text to
  type into the console's Custom MIDI page, in large type, and updates
  it as you change the CC number or the base MIDI channel. The SoftKey
  needs Direct TCP or an Existing MIDI Port that can receive — it can't
  be received through a MIDI Bridge lane; the button works everywhere.
- Fixed: when sending through MIDI Bridge, the lights could stop
  responding after a couple of minutes without talkback, with "Send
  failed" in the status panel, until you pressed Stop and Start. MIDI
  Bridge closes a connection that has been quiet for two minutes, and
  Talk Light Trigger did not reconnect. It now reconnects by itself and
  the Scene goes out as normal.
- Fixed: when the Mac's audio system resets — installing an audio driver
  does this (Time Code Tool's installer is one), and so can waking from
  sleep — Start could fail every time with "Internal PortAudio error
  [PaErrorCode -9986]" until you quit and reopened the app, and an input
  that was already running could stop for good: the level froze where it
  was and, if talkback was on, the lights kept flashing until you
  pressed Stop. The app now refreshes its device list and opens your
  input as normal, and notices a stopped input within 3 seconds: it sets
  the lights to the Quiet Scene, reopens the input and carries on
  listening, and the status panel says what happened.
- Fixed: the Audio Input channel could not be set above 64, so channels
  on a larger interface (Dante, MADI) were out of reach. The Channel box
  now goes up to the last channel of the device you have selected — a
  channel you saved earlier for a bigger interface is left alone, not
  quietly reduced, so it is still there when you plug that interface
  back in — and if you pick one the device hasn't got, the message says
  so plainly.
- If Scenes stop reaching the console while the app is running, the
  status panel now turns red and says why, and stays that way until a
  Scene gets through — before, the message vanished almost at once and
  the panel carried on looking normal. Warnings and errors now stay
  until you press Start or Stop, and the green "Connected" from Test
  Connection is cleared when you press Start, so it can't be mistaken
  for a live status.
- New: Options — Start at login, Show in Dock and Check for updates live
  together behind one disclosure at the bottom of the panel. Show in
  Dock puts Talk Light Trigger in the Dock and in Cmd-Tab for easier
  switching; it is off by default. Check for updates tells you whether a
  newer version is on the store, with a link to get it. It only checks
  when you press it, never on its own and never while Talk Light Trigger
  is running, and it sends nothing about you or your Mac.
- The Quick Reference guide is now installed with the app, so the
  footer's Quick Reference link opens it even with no internet — and it
  always matches the version you are running. The app's title and
  version stay in view while you scroll, and the panel sizes itself to
  the screen it is on instead of clipping its footer on shorter
  displays.
- On macOS 11 and 12, the panel now shows all its colours — the red "Not
  reaching the console" status, the trial banner and the blue accents
  were missing there, because those Macs' web engine didn't understand
  how they were written — and the first click after opening the panel
  works: before, it only brought the app forward, and a right-click
  showed a bare "Reload" menu. Nothing changes on macOS 13 or later.
- Export log now saves a diagnostics zip to your Desktop and shows it in
  Finder — this session's log, the previous session's, and your settings
  (licence details removed) — so one attachment covers a bug report. The
  session log itself now records your settings and where the app is
  running from at launch (a copy still running from the DMG is called
  out, since settings don't stick there), the audio and MIDI devices
  present and any change to that list, each setting you change, every
  Start with the settings and connection in force and every Stop with
  why and how many Scenes were sent and failed, any Scene that fails to
  send and when sending recovers, each Cancel SoftKey press, a Start or
  console connection that fails and why, a MIDI port that has gone
  missing, your licence or trial state, and a final line when you quit.
- Fixed: a damaged settings file was silently replaced with the defaults
  on the next save. It is now set aside under a dated name, the log says
  so, and the app runs on defaults until you set things again.
- Smaller fixes: pressing Start while already running now restarts
  cleanly instead of leaving the first run's audio stream and console
  connection alive underneath the new one; a Start or Stop that fails
  outright no longer leaves the button stuck on "Starting…"; and if the
  device or MIDI port list can't be read, the dropdown says "Couldn't
  list devices — Rescan" and keeps your saved choice instead of going
  empty.

v1.0.8
- Fixed: on macOS 15 Sequoia, Talk Light Trigger could fail to reach the
  console over Direct TCP ("No route to host") without ever asking for
  Local Network permission, because macOS was mistaking it for another
  dylanmaudio app. Each app now has its own identity, so macOS asks once:
  click Allow (if the first Run gives up while the question is on screen,
  press Run again). If the connection is still blocked, the message now
  says where to switch it on: System Settings → Privacy & Security →
  Local Network.

v1.0.7
- Tidier popover: the Bitfocus Companion settings and the on-screen hints now
  sit behind disclosures, closed by default (a green dot on the Companion
  header shows when Companion is connected); the trademark notice at the
  bottom has gone — it's in the Quick Reference and the licence. Companion
  can now also bring the app's window forward.
- New: Talk Light Trigger can now be controlled from Bitfocus Companion —
  Run and Threshold, plus a status feed for buttons/variables. Off by
  default is "on": Companion control is allowed out of the box (this Mac
  only); a new "Lock show-critical controls" switch refuses Stop and
  other critical presses from Companion when you want it. Both switches
  live in the popover, next to Start at login.

v1.0.5
- Improved: the app now opens just the one input channel you chose, with
  a large audio buffer, and never changes the interface's sample rate —
  so it costs the show's audio interface as little as a second app can.
  The channel, rate and buffer are written to the session log when the
  input opens.
- Clearer message when the chosen channel doesn't exist on the device,
  instead of a cryptic driver error.
- Fixed: if the audio input fails to open, the console connection is
  closed again instead of being left open behind the error.
- New: every session now writes a log, and a new Export log button in
  the footer saves a copy to your Desktop — so if something goes wrong at a
  show, there is evidence to send, without instructions.
- Quick Reference and README now document an optional console-side
  setup — a SoftKey sending a positive talk-state message over the
  network — for reference. Talk Light Trigger still detects talk state
  from the audio input by default; nothing changes unless you wire this
  up yourself.

v1.0.4
- Talk Light Trigger now installs into a "dylanmaudio" folder inside Applications,
  alongside the other dylanmaudio apps, instead of sitting loose in
  Applications. Updating moves your existing copy for you.
- The download is now an installer you double-click, rather than a disk
  image you drag from.

v1.0.3
- New: a footer link to the app's Quick Reference guide, so the guide is
  always a click away instead of only being on the disk image.
- New: send feedback from inside the app — a short message straight to
  me, no email client or web form needed.
- New: a link to the other dLive utilities.
- Fixed: a stray highlight box that appeared around the first section
  heading when the window opened.

v1.0.2
- When used with MIDI Bridge, this app now identifies itself by name
  in the bridge's MIDI Monitor instead of appearing as a generic DAW
  connection.

v1.0.1 - First build (internal — the public launch was v1.0.7)
