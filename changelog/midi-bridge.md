# Changelog — MIDI Bridge (dLive)

Customer-facing version history. Mirrors the Changelog section on the
Lemon Squeezy product page — keep the two in sync (entries below are
written to be copy/pasted there verbatim, minus this header).

One entry per PUBLIC release. The top entry is the release being
prepared: until it ships, keep adding to it and keep its version in step
with setup.py — the build prints it on the Quick Reference cover (first
six bullets, so the most important go first) and in every build's
changelog PDF. Notes on builds that never ship go in BUILD-HISTORY.md.

v1.3.0
- Now runs natively on Intel Macs as well as Apple Silicon, on macOS 11
  Big Sur or later. Earlier builds installed on an Intel Mac but would
  not open there.
- Fixed: "Connected" now means the console is answering. Before, the
  bridge showed Connected as soon as anything accepted a network
  connection on the console's port, and could stay Connected, with
  "last activity" counting up, after the console had stopped responding.
  It now checks with the console straight away and every few seconds,
  shows "Waiting for a reply from …" until the console answers, and
  notices within about 20 seconds when it stops, then reconnects.
- Fixed on macOS 11 and 12: the first click after opening the panel did
  nothing — it only brought the app forward — and a right-click showed a
  bare "Reload" menu; the app now comes forward as the panel opens, so
  the first click works. The window also shows all its colours there: the
  blue accents were missing, because those Macs' web engine didn't
  understand how they were written. Nothing changes on macOS 13 or later.
- One log, one folder. The bridge's own lines — connecting, connected,
  reconnects, each app that joins and leaves, errors — now go into the
  session log alongside the panel's, so "Open Log" shows everything in
  one dated file and Export log includes it (before, the bridge wrote a
  separate file that the export left out). Everything lives in
  ~/Library/Logs/dylanmaudio/MIDI Bridge - dLive/, one right-click away
  as "Open Log Folder" on the menu bar icon. The MIDI monitor log stays
  its own file, saved from the Monitor page as before.
- Export log now saves a diagnostics zip to your Desktop and shows it in
  Finder — this session's log, the previous session's, and your settings
  — so one attachment covers a bug report. The session log itself now
  records your settings and where the app is running from at launch (a
  copy still running from the DMG is called out, since settings don't
  stick there), each setting you change, the bridge starting and
  stopping with its exit code, whether Start at login took, any error
  the panel shows, and a final line when you quit.
- Fixed: the MIDI Monitor no longer shows EQ, HPF and channel-assign
  changes as "fader moved". Parametric EQ, HPF, main, DCA and mute-group
  assignments, aux / FX / matrix sends, preamp gain, pad and 48V, and
  name and colour changes now each read as what they are — "Input 3 HPF
  → ~85 Hz", "Input 1 → Mono Aux 1 send → LV=107 (~0.0 dB)" — instead of
  appearing as a fader move or as an unlabelled SysEx line hidden under
  Advanced. They have a Params filter of their own.
- MIDI Monitor: you can now select and copy a message's raw MIDI without
  the row closing on you. Open a row and press Copy, or Cmd-click (or
  Ctrl-click) any row to copy its raw MIDI straight away; a fader, EQ or
  other NRPN change copies all three of its messages. The velocity-0
  "note-off terminator" that follows every mute is now shown only under
  Advanced, so each mute is one row.
- MIDI Monitor: the filter chips and Advanced are now remembered, so the
  window opens the way you left it. Pause, the search box and the lane
  filter still start fresh each time, so the Monitor never opens looking
  as though nothing is coming in.
- The session log now records each app that connects to the bridge by
  name, when it disconnects, when the bridge closes one that has been
  quiet for two minutes, and any message refused because its connection
  had already been closed — so an app that "stops working after a
  couple of minutes" shows up plainly in an exported log.
- Fixed: the bridge always connects to the console address shown in the
  panel. If the running bridge is using a different address from the
  one in the Connection fields, the panel now says so.
- Fixed: a damaged settings file was silently replaced with the defaults
  on the next launch, console address included. It is now set aside
  under a dated name, the log says so, and the app runs on defaults until
  you set things again.
- Fixed: the "Base channel mismatch" caption — the console is on one MIDI
  channel and the bridge is set to another — could never appear in the
  panel, although the bridge had detected it. It shows now.
- Fixed: if the bridge could not be started at all (the core missing, a
  launch error), the panel just said "Bridge process not running". It now
  says why, and clicking the tile opens the log.
- Fixed: if the app was force-quit or crashed, its bridge process kept
  running in the background — as a plain "python" in Activity Monitor —
  holding the monitor port and the console connection, so the next launch
  reported "Another copy of MIDI Bridge is already running". The bridge
  process now exits by itself within a second of the app going away.
- The "No peer" and "Bridge exited" captions now say what to do next:
  check the console's IP and that MIDI TCP/IP is on, or Start Bridge to
  relaunch after reading the log.
- Start at login: if macOS refuses the change, the Options row now says
  so instead of silently flipping the switch back. (All apps.)
- New: Options — Start at login, Show in Dock and Check for updates now
  live together behind one disclosure at the bottom of the panel. Show in
  Dock puts MIDI Bridge in the Dock and in Cmd-Tab for easier switching
  (the MIDI Monitor already did this while it was open; now the Dock icon
  can stay); it is off by default, so nothing changes unless you turn it
  on. Start at login has moved there from the Connection section, and
  the duplicate version line and Quit link at the bottom of the panel
  are gone — the version is in the header, and Quit is a right-click on
  the menu bar icon or Cmd-Q, as in the other dylanmaudio apps.
- New: Check for updates — press the button and MIDI Bridge tells you whether
  a newer version is on the store, with a link to get it. It only checks
  when you press it, never on its own and never while MIDI Bridge is running,
  and it sends nothing about you or your Mac.
- New: the Quick Reference guide is installed with the app, so the
  footer's Quick Reference link opens it even with no internet — and it
  always matches the version you are running.
- The app's title and version now stay in view while you scroll the
  panel.
- MIDI Bridge now carries its own identity for macOS's Local Network permission, instead of one shared with other apps built the same way. If macOS asks about MIDI Bridge once after updating, click Allow.

v1.1.9 - The bridge becomes a hub
- Tidier popover: the Bitfocus Companion settings and the on-screen hints now
  sit behind disclosures, closed by default (a green dot on the Companion
  header shows when Companion is connected); the trademark notice at the
  bottom has gone — it's in the Quick Reference and the licence. Companion
  can now also bring the app's window forward.

- New: other software can now share MIDI Bridge's connection to the console instead of opening its own — built for Bitfocus Companion and the other dylanmaudio apps. Connected software gets a live picture of the console, kept up to date from what the console itself broadcasts, and can recall scenes, fire Actions, and set faders, mutes, names, colours and aux, FX and matrix send levels, including timed fader moves. Companion can also start, stop and restart the bridge itself and show its status, and two new switches in the app turn that off or lock the show-critical controls.
- Fixed: fader moves made on the console now reach MIDI Bridge in full. The console sends most of each fader message in a compact form the bridge had been throwing away, so the MIDI Monitor, connected software and the "dLive Bridge Return" port could see that a fader had moved, but never where it moved to. Your DAW now receives the whole move through the Return port.
- New installer: MIDI Bridge now installs into a "dylanmaudio" folder inside Applications, alongside the other dylanmaudio apps. The download is an installer you double-click, and it moves your existing copy for you.
- The MIDI Monitor now shows which program each message came from, with a colour for each and a filter to show one at a time. It keeps its log when you reopen it, shows recent activity when you open it mid-show, follows you to the desktop Space you are on, and appears in the Dock and Cmd-Tab while it is open. You can also save or clear the MIDI log from inside it.
- New: every session writes a log, and an Export log button saves a copy to your Desktop — so if something goes wrong at a show, there is something to send. The footer also links to the Quick Reference guide and lets you send feedback from inside the app.
- Clearer when something is wrong: if another copy of MIDI Bridge is already running, the app says so, names the program holding the port and tells you how to fix it, instead of reporting only "Bridge exited with code 1". And if the bridge's base channel doesn't match the console's, it now says so shortly after the console sends anything, naming the channel to switch to — instead of looking exactly like a console that isn't there.
- The "dLive Bridge Return" port no longer passes the bridge's own background checks through to your DAW, while genuine console activity still reaches it. Configurable if you prefer the old behaviour or none at all.
- Clearer MIDI Monitor labels: console Actions are marked, with a filter of their own; queries from other software — Companion reading fader levels, for example — now show as queries rather than as unknown messages or garbled colour changes; a cue fired twice now shows twice instead of merging into one row; and a fader change another program sends without naming its channel — which the console applies to whatever is currently selected — is shown that way, rather than pinned on the wrong channel. If you use the console's MIDI Strips or SoftKeys, a setting in the config file shows their activity as strip activity.
- The control panel now uses the full height of your screen, so the version line and Quit are no longer cut off, and a stray highlight box that could appear around the first heading is gone.

v1.0.2 - MIDI Monitor fixes: correct fader dB values, correct mute on/off decoding, clearer channel labels when the base channel doesn't match

v1.0.1 - Fixed bug regarding the creation of virtual midi port (would report as a connection error)

v1.0.0 - Initial Release
