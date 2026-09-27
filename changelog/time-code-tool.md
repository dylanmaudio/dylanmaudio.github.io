# Changelog — Time Code Tool

Customer-facing version history. Mirrors the Changelog section on the
Lemon Squeezy product page — keep the two in sync (entries below are
written to be copy/pasted there verbatim, minus this header).

One entry per PUBLIC release. The top entry is the release being
prepared: until it ships, keep adding to it and keep its version in step
with setup.py — the build prints it on the Quick Reference cover (first
six bullets, so the most important go first) and in every build's
changelog PDF. Notes on builds that never ship go in BUILD-HISTORY.md.

Note: the public launch was v1.1.5. Everything before it was internal —
those entries are kept below as the history of what launched.

v1.3.0
- Now runs on macOS 11 Big Sur or later, as the store page has always
  said. Earlier versions needed macOS 13.3 or later — on macOS 11 to
  13.2 the app failed to open, with no message.
- The app's two virtual MIDI ports are now named "Time Code Tool MTC
  Out" and "Time Code Tool MTC In", matching the "Time Code Tool LTC"
  audio device (they were "TCT MTC Out" and "TCT MTC In"). Nothing about
  how they work has changed. If your DAW or another app was set to the
  old name, select the new one once: apps that remember a MIDI port by
  name will show the old one as missing; apps that remember it by its ID
  carry on without you doing anything.
- Generate: a drop-frame start time that doesn't exist is now moved
  forward instead of refused. In 29.97 DF, frames 00 and 01 are skipped
  at the top of every minute not divisible by 10, so 00:17:00:00 was
  being rejected — the app now starts at 00:17:00;02 and says so. The
  same applies to the WAV generator's start and end times and to the
  Companion "Generate from" button. Truly impossible times (hour 24,
  frame 30) are still refused with the legal range shown.
- Generate: the start time and frame rate can no longer be changed while
  the generator is running — they only ever applied at the next Start,
  so the panel could show 30 fps while 25 fps was going out. Stop first,
  as for the mode and input source; Companion gets the same refusal.
- Fixed: in Generate mode, pressing Start with both outputs off seemed
  to do nothing. The app was refusing — "Nothing to generate — turn on
  LTC or MTC output" — but showed the message in the Input section,
  which Generate mode hides. Messages about Start now appear directly
  under the Start button in both modes, and clear when you switch mode
  or turn an output on.
- Fixed: the Audio Input channel could not be set above 64, so channels
  on a larger interface (Dante, MADI) were out of reach. The Channel box
  now goes up to the last channel of the device you have selected — a
  channel you saved earlier for a bigger interface is left alone, not
  quietly reduced, so it is still there when you plug that interface
  back in — and if you pick one the device hasn't got, the message says
  so plainly, without assuming you use Dante.
- Fixed: the MTC input list was not being re-read when the panel opened,
  so a MIDI port that appeared after launch could stay missing from it
  until the app was relaunched.
- New: Options — Start at login, Show in Dock and Check for updates live
  together behind one disclosure at the bottom of the panel. Show in
  Dock puts Time Code Tool in the Dock and in Cmd-Tab for easier
  switching; it is off by default. Check for updates tells you whether a
  newer version is on the store, with a link to get it. It only checks
  when you press it, never on its own and never while Time Code Tool is
  running, and it sends nothing about you or your Mac.
- The Quick Reference guide is now installed with the app, so the
  footer's Quick Reference link opens it even with no internet — and it
  always matches the version you are running. The app's title and
  version stay in view while you scroll, and the panel sizes itself to
  the screen it is on instead of clipping its footer on shorter
  displays.
- Error messages in the panel are now red, so a refused Start or a
  device that isn't available stands out from the notes; a stale error
  no longer survives a Rescan. The Licensed badge now matches the other
  dylanmaudio apps.
- On macOS 11 and 12, the panel now shows all its colours — the Start
  button showed as bare text there, and the trial banner and blue
  accents were gone, because those Macs' web engine didn't understand
  how they were written — and the first click after opening the panel
  works: before, it only brought the app forward, and a right-click
  showed a bare "Reload" menu. Nothing changes on macOS 13 or later.
- Fixed: macOS was mistaking the dylanmaudio apps for one another when
  deciding Local Network permission, which is why Time Code Tool could
  appear under System Settings → Privacy & Security → Local Network
  without using the network itself. Each app now has its own identity.
- Export log now saves a diagnostics zip to your Desktop and shows it in
  Finder — this session's log, the previous session's, and your settings
  (licence details removed) — so one attachment covers a bug report. The
  session log itself now records your settings and where the app is
  running from at launch (a copy still running from the DMG is called
  out, since settings don't stick there), the audio and MIDI devices
  present and any change to that list, each setting you change, every
  Start with the mode, source, devices and rates in force and every Stop
  with why, a Start that fails and why, your licence or trial state, and
  a final line when you quit.
- Fixed: a damaged settings file was silently replaced with the defaults
  on the next save. It is now set aside under a dated name, the log says
  so, and the app runs on defaults until you set things again.

v1.1.5
- Tidier popover: the Bitfocus Companion settings and the on-screen hints now
  sit behind disclosures, closed by default (a green dot on the Companion
  header shows when Companion is connected); the trademark notice at the
  bottom has gone — it's in the Quick Reference and the licence. Companion
  can now also bring the app's window forward.
- New: this app can now be controlled from Bitfocus Companion — Start/Stop,
  Read/Generate, the input source, MTC and LTC output, Reset counters and
  the generator's start time and rate all show up as Companion buttons,
  with the live timecode, lock state and frame rate reflected back on
  them (a multi-button timecode readout is one preset away). On by
  default; two new switches in the app let you turn Companion control
  off or lock the show-critical ones (Stop, and switching an output off).
  Mode and input source can't be changed from Companion while running —
  stop first, as in the app.
- The generator's start time (and the WAV generator's start and end) is
  now checked against the frame rate as you type it. A time that doesn't
  exist — 24:00:00:00, frame 25 at 25 fps, frame 00 at the top of a
  drop-frame minute — is refused with the legal range shown, instead of
  being stored and going wrong at Start.

v1.1.4
- An isolated bad frame in the incoming LTC no longer makes the app jump.
  LTC recordings and real signal paths carry the odd frame with a bit error
  that still decodes — to an impossible time — and the app used to relatch
  on every one, sending a full-frame MTC locate away and another back 33 ms
  later. Anything chasing the MTC (Reaper, Console Control) followed each
  one. A jump is now confirmed by the frame after it before the app acts on
  it: an isolated misread is dropped and counted, a real relocate goes
  through one frame (33 ms) later, and a frame the signal path merely
  missed no longer triggers a relatch at all.
- The Discontinuities counter now says which kind: Missed (the signal path
  dropped frames), Misread ignored (a bit error the app rode out), Jumps
  (a real relocate). Reset clears all of them.
- Every MTC full-frame locate the app sends is written to the session log,
  with why — so a show-day "the desk jumped" can be read back from the log
  rather than a screen recording.
- New: every session now writes a log, and a new Export log button in
  the footer saves a copy to your Desktop — so if something goes wrong at a
  show, there is evidence to send, without instructions.

v1.1.3
- Recovers from a macOS audio reset. After the Mac sleeps and wakes, or an
  audio driver is installed, the app used to show "Internal PortAudio error"
  or quietly stop receiving LTC until it was relaunched. It now refreshes its
  view of the audio devices whenever it starts, and if a running input stops
  delivering audio it restarts itself.
- The "TCT MTC Out" and "TCT MTC In" virtual ports keep the same identity
  every time the app runs, so Reaper, Console Control and other hosts that
  remembered them keep working after the app is restarted — no re-scan or
  reboot needed.
- MTC output is now paced evenly no matter which audio device the LTC comes
  in on. On some devices — the "Time Code Tool LTC" virtual device among
  them — quarter-frames were leaving in bursts every 57 ms instead of every
  8 ms, and apps chasing the MTC lost lock even though the LTC was solid.
- MTC freewheel is now measured in frames of missing timecode rather than
  audio blocks, so it behaves the same on every device and buffer size.
- Pressing Start while already running restarts cleanly instead of leaving
  the previous run going in the background.
- Regenerating LTC onto the same device it is being read from is refused,
  with a message saying why.

v1.1.2
- Time Code Tool now installs into a "dylanmaudio" folder inside Applications,
  alongside the other dylanmaudio apps, instead of sitting loose in
  Applications. Updating moves your existing copy for you.
- The download is now an installer you double-click, rather than a disk
  image you drag from.

v1.1.1
- New: a footer link to the app's Quick Reference guide, so the guide is
  always a click away instead of only being on the disk image.
- New: send feedback from inside the app — a short message straight to
  me, no email client or web form needed.
- New: a link to the other dLive utilities.
- Fixed: a stray highlight box that appeared around the first section
  heading when the window opened.

v1.1.0
- New: real-time LTC output — regenerate incoming timecode as clean,
  level-controlled LTC to any audio output device, riding through signal
  dropouts (freewheel) and optionally converting the frame rate on the way.
- New: Generate mode — the app free-runs as a timecode master. Choose a
  start time and frame rate and it sends LTC audio and MTC together from
  one clock, no input needed.
- New: MTC input — read MIDI Time Code from the new "TCT MTC In" virtual
  port (select it as an MTC output in your DAW) or from any MIDI
  interface, and convert it to LTC and/or re-send it as MTC.
- New: MTC output can now be sent to any MIDI interface, not only the
  "TCT MTC Out" virtual port.
- The "TCT MTC Out" virtual port now stays open the whole time the app is
  running, so your DAW's MIDI routing survives stopping and restarting.
- Now installed by a signed installer, which can also add the optional
  "Time Code Tool LTC" virtual audio device for you (a tick-box during
  installation, macOS 13+) so LTC can feed other apps with no cabling.
  Removal instructions are included on the disk image.
- Reorganised: one OUTPUT section holds both outputs, each with its own
  On/Off switch that reveals just its settings, and the transport switch at
  the top now reads Read Timecode / Generate Timecode.

v1.0.0 - Initial Release
