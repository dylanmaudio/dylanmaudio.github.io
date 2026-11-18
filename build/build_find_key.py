#!/usr/bin/env python3
"""Generate the Find my key page -> find-my-key/index.html (served at /find-my-key/).

Written 18 Nov 2026 by STRATEGY: Console Control release, for the move to the
new store (D19 answered no, 18 Nov). The contract is the licence service's
(apps repo, topic/distribution-brief, docs/brief-store-and-licence-service.md
§7; the service is the new store thread's):

- The page POSTs {"email": ...} as JSON to ENDPOINT. CORS allows
  https://dylanmaudio.com.
- The service always answers 202, whether or not the address has an order
  and even over its rate limit (it then sends nothing), so the page always
  shows the same words. It trims and lower-cases the address itself. The email it sends lists every key,
  product and download page for that address. It's rate-limited per address
  and per IP.

Not merged until the service answers on licence.dylanmaudio.com. When it goes
live:
- set LISTED = True (drops noindex), and add the page to build_seo.PAGES;
- link it from the footer and the product pages' buy sections;
- put the privacy page's new wording into build_privacy.py in the same
  commit. STRATEGY: Downloads writes it under #545, with EULA 1.1: the email
  address typed here goes to our licence service, and the store is no longer
  Lemon Squeezy. Don't draft a second version; send any wording need there;
- set LS_NOTE = False once Lemon Squeezy's keys are imported (D14).

The toolbar, footer and styles are the 404 page's (build_404.HTML), as for
the privacy page.
"""
import common as C
import build_404 as NF

ENDPOINT = "https://licence.dylanmaudio.com/find"
LISTED = False      # noindex until the service is live
LS_NOTE = True      # until Lemon Squeezy's keys are imported into our service (D14)
LS_ORDERS = "https://app.lemonsqueezy.com/my-orders"
CONTACT = "dylan@dylanmaudio.com"

BODY = r"""
<main>
  <article class="fk">
    <div class="kicker"><span class="tick">//</span>&nbsp; Licence keys</div>
    <h1>Find my key</h1>
    <p class="lede">Type the email address you bought with. We&rsquo;ll email it every licence key and download link it owns. There&rsquo;s no account and no password.</p>

    <form id="fk-form" class="fk-form" novalidate>
      <label for="fk-email">Email address</label>
      <div class="fk-row">
        <input id="fk-email" name="email" type="email" autocomplete="email" inputmode="email"
               placeholder="you@example.com" required>
        <button id="fk-send" type="submit" class="btn btn-primary">Email my keys <span class="arw">&rarr;</span></button>
      </div>
      <p id="fk-status" class="fk-status" role="status" aria-live="polite"></p>
    </form>

    <h2>What happens next</h2>
    <ul>
      <li><strong>One email, within a minute or two,</strong> listing every key, app and download link bought with that address.</li>
      <li><strong>Nothing arrived?</strong> Check your spam or junk folder, and that you typed the address you paid with.</li>
      <li><strong>Lost access to that inbox, or bought with an address you can&rsquo;t remember?</strong> Email <a href="mailto:__CONTACT__">__CONTACT__</a> with your name and roughly when you bought, and I&rsquo;ll find it.</li>
__LS_NOTE__    </ul>
  </article>
</main>
"""

LS_NOTE_HTML = (
    '      <li><strong>Bought from the old store, run by Lemon Squeezy?</strong> Until those orders move across, '
    'your key is in Lemon Squeezy&rsquo;s receipt email, or at '
    '<a href="__LS_ORDERS__" target="_blank" rel="noopener">Lemon Squeezy&rsquo;s My Orders</a>.</li>\n'
)

CSS = r"""
  /* Find my key */
  main { flex:1; display:block; }
  .fk { max-width:680px; margin:0 auto; padding:clamp(48px,8vw,88px) var(--pad); }
  .fk h1 { font-size:clamp(1.9rem,4.2vw,2.7rem); line-height:1.1; letter-spacing:-0.02em; font-weight:650; margin:16px 0 0; }
  .fk .lede { margin:16px 0 0; color:var(--muted); font-size:clamp(1.02rem,1.5vw,1.12rem); }
  .fk h2 { font-size:1.15rem; font-weight:640; margin:44px 0 10px; }
  .fk ul { margin:0; padding-left:20px; color:var(--muted); }
  .fk li { margin:0 0 10px; }
  .fk li strong { color:var(--text); font-weight:600; }
  .fk a { color:var(--blue); }
  .fk a:hover { text-decoration:underline; }
  .fk-form { margin:32px 0 0; padding:22px; background:var(--surface); border:1px solid var(--border); border-radius:14px; }
  .fk-form label { display:block; font-family:var(--mono); font-size:12px; letter-spacing:0.08em; text-transform:uppercase; color:var(--dim); margin:0 0 10px; }
  .fk-row { display:flex; gap:10px; flex-wrap:wrap; }
  .fk-row input { flex:1 1 240px; min-width:0; font:inherit; color:var(--text); background:var(--bg);
    border:1px solid var(--border); border-radius:10px; padding:11px 14px; outline:none; transition:border-color .15s; }
  .fk-row input:focus { border-color:var(--blue); }
  .fk-row input::placeholder { color:var(--dim); }
  .fk-row .btn { flex:0 0 auto; border:1px solid transparent; border-radius:10px; cursor:pointer; font-family:inherit; }
  .fk-row .btn[disabled] { opacity:0.6; cursor:default; }
  .fk-status { margin:14px 0 0; min-height:1.6em; color:var(--muted); }
  .fk-status.ok { color:var(--green); }
  .fk-status.err { color:var(--amber); }
  @media (max-width:520px) { .fk-row .btn { flex:1 1 100%; justify-content:center; } }
"""

JS = r"""
<script>
(function () {
  var form = document.getElementById("fk-form");
  var input = document.getElementById("fk-email");
  var btn = document.getElementById("fk-send");
  var out = document.getElementById("fk-status");
  function say(text, cls) { out.textContent = text; out.className = "fk-status" + (cls ? " " + cls : ""); }
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var email = input.value.trim();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) { say("That doesn’t look like an email address.", "err"); input.focus(); return; }
    btn.disabled = true;
    say("Sending…");
    fetch("__ENDPOINT__", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: email })
    }).then(function (r) {
      if (r.ok) { say("If that address has an order, we’ve sent it.", "ok"); }
      else { say("Something went wrong at our end. Try again in a few minutes, or email __CONTACT__.", "err"); }
    }).catch(function () {
      say("Couldn’t reach the key service. Check your connection and try again, or email __CONTACT__.", "err");
    }).then(function () { btn.disabled = false; });
  });
})();
</script>
"""


def build():
    html = NF.HTML
    head, rest = html.split("<main>", 1)
    tail = rest.split("</main>", 1)[1]
    tail = tail[:tail.index("<script>")] + JS + "</body>\n</html>"      # the 404's path script out, ours in
    if LISTED:
        head = head.replace('<meta name="robots" content="noindex, follow">\n', "")
    head = (head.replace("<title>Page not found — Dylan [M] Audio</title>",
                         '<title>Find my key — Dylan [M] Audio</title>\n'
                         '<meta name="description" content="Type the email address you bought with, and get every '
                         'licence key and download link it owns by email. No account, no password.">')
                .replace("</style>", CSS + "</style>"))
    assert "<title>Find my key" in head and (("noindex" in head) != LISTED)
    body = BODY.strip("\n").replace("__LS_NOTE__", LS_NOTE_HTML if LS_NOTE else "")
    out = head + body + "\n" + tail
    out = (out.replace("__ENDPOINT__", ENDPOINT)
              .replace("__CONTACT__", CONTACT)
              .replace("__LS_ORDERS__", LS_ORDERS)
              .replace("__DISCORD_URL__", C.DISCORD_URL)
              .replace("__DISCORD_SVG__", C.DISCORD_SVG)
              .replace("__STORE_URL__", C.STORE_URL)
              .replace("__NONAFFIL__", C.NONAFFIL))
    assert "__" not in out.replace("__proto__", ""), "an unreplaced token"
    C.write("find-my-key/index.html", C.inject_analytics(out))


if __name__ == "__main__":
    build()
