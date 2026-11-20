#!/usr/bin/env python3
"""Generate the privacy page -> privacy/index.html (served at /privacy/).

Written 27 Sept 2026, when the store's Meta Pixel was agreed for the October
ads (dylanmaudio-marketing briefs/ad-campaign-october.md). Keep it true: if
the site gains a tag, a form service changes, or the apps start sending
anything new, change this page in the same commit.

The toolbar, footer and styles are the 404 page's (build_404.HTML), so the
two standalone pages can't drift apart.
"""
import common as C
import build_404 as NF

UPDATED = "3 December 2026"   # the day this version goes up, with Find my key; change it if that moves

# Revised 21 Nov 2026 to match the apps' PRIVACY.txt 1.2 (apps repo, #545,
# topic/eula-1.1 7a89dade), which names roles, not companies, and points here
# for the names. "Who else is involved" is STRATEGY: Downloads' wording (#545).
# Goes up with the Find my key page; keep the two, and PRIVACY.txt, saying the
# same thing.

BODY = r"""
<main>
  <article class="pv">
    <div class="kicker"><span class="tick">//</span>&nbsp; Privacy</div>
    <h1>Privacy</h1>
    <p class="lede">Short version: this website sets no cookies and runs no ad tags. When you buy, the store that sells it to you takes your details and payment. The apps go online only when you press a button, and send nothing about how you use them.</p>
    <p class="upd">Updated __UPDATED__</p>

    <h2>This website</h2>
    <ul>
      <li><strong>No cookies, no ad or tracking tags,</strong> and nothing stored in your browser to follow you around.</li>
      <li><strong>Visitor counts</strong> come from Cloudflare Web Analytics, which is cookieless and doesn&rsquo;t identify you.</li>
      <li><strong>Hosting:</strong> the site is served by GitHub Pages; GitHub keeps standard server logs, including IP addresses, for security (<a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener">GitHub&rsquo;s privacy statement</a>).</li>
      <li><strong>Where you came from:</strong> if you arrive from a post, an email or an ad whose link carries a campaign tag (<code>utm_source</code> and the like), the site passes that tag to the store link you click, so the order records which post or ad worked. Nothing is saved on your device.</li>
      <li><strong>Videos</strong> are embedded in YouTube&rsquo;s privacy-enhanced mode (youtube-nocookie.com), which doesn&rsquo;t set cookies until you press play.</li>
      <li><strong>The contact form</strong> sends your name, email and message to me through Web3Forms. I use them to reply, and for nothing else.</li>
      <li><strong>Find my key</strong> sends the email address you type to my licence service, which emails that address its keys. It keeps a one-way hash of the address and of your IP address for about a day, to limit abuse.</li>
    </ul>

    <h2>The store</h2>
    <ul>
      <li><strong>The store that sells you an app takes payment and handles tax.</strong> It&rsquo;s named on your receipt, as the merchant of record, and works under its own privacy policy. I never receive your card details.</li>
      <li><strong>Lemon Squeezy&rsquo;s store</strong> (store.dylanmaudio.com) also sends its own receipts and download emails, and handles free trials, free apps and Get notified, with your email address. I use that address to send the download, update news and launch news &mdash; never sold or shared &mdash; and you can unsubscribe from any email. What Lemon Squeezy collects is in <a href="https://www.lemonsqueezy.com/privacy" target="_blank" rel="noopener">its privacy policy</a>.</li>
      <li><strong>Meta Pixel:</strong> Lemon Squeezy&rsquo;s store uses Meta&rsquo;s Pixel to count what my ads lead to and to show ads to people who&rsquo;ve visited it. It runs on that store and its checkout only, not on this website. You can limit it in your <a href="https://www.facebook.com/adpreferences" target="_blank" rel="noopener">Meta ad preferences</a> or with your browser&rsquo;s tracking protection.</li>
    </ul>

    <h2>Your licence</h2>
    <ul>
      <li><strong>What I keep,</strong> once my own licence service holds your licence: for each order, your email, your name as given at checkout, the product, the payment reference and the date; your licence key; and for each computer you activate, its label (which includes the computer&rsquo;s name) and the date. No IP addresses, and no record of when you use the apps.</li>
      <li><strong>How long:</strong> as long as your licence can be used &mdash; for a licence with no end date, for good &mdash; so I can always send your key again and free its seats. It&rsquo;s used for nothing else.</li>
    </ul>

    <h2>The apps</h2>
    <ul>
      <li><strong>No analytics and no usage data.</strong> The apps don&rsquo;t report what you do with them, and nothing goes online by itself: not at launch, and not on a timer.</li>
      <li><strong>Licence:</strong> a paid app contacts the licence service only when you press Activate, Deactivate or (in Console Control) Check licence. Activate sends your key and a label for the computer: its name plus six characters of a one-way hash that can&rsquo;t be turned back into its hardware identifier. The free MIDI Bridge makes no licence calls.</li>
      <li><strong>Check for updates</strong> downloads a small file from dylanmaudio.com, only when you press the button. It carries the app&rsquo;s name, version and operating system, and nothing about you.</li>
      <li><strong>Send feedback</strong> sends the text you typed and the app&rsquo;s name, and nothing else, through Web3Forms. Put your email address in the message if you want a reply.</li>
      <li><strong>Logs stay on your computer.</strong> Export log saves a zip for you to send me if something goes wrong; nothing is sent on its own.</li>
      <li>Everything else the apps talk to is on your own network &mdash; the console, MIDI Bridge, Companion.</li>
    </ul>
    <p>The full statement that ships with the apps is in each download (PRIVACY.txt).</p>

    <h2>Who else is involved</h2>
    <ul>
      <li><strong>Store and payment:</strong> Lemon Squeezy is the merchant of record for purchases made in its store, which closes on 31 March 2027. Purchases in our new store are processed by Stripe; the merchant of record is the one named on your receipt.</li>
      <li><strong>Licence service:</strong> our own, run on Cloudflare (Workers and its D1 database). Keys bought from Lemon Squeezy are passed to Lemon Squeezy&rsquo;s licence service until we carry them over.</li>
      <li><strong>Key emails:</strong> Resend.</li>
      <li><strong>Send feedback:</strong> Web3Forms.</li>
      <li><strong>This website:</strong> hosted on GitHub Pages; its DNS is on Cloudflare.</li>
    </ul>

    <h2>Elsewhere</h2>
    <ul>
      <li>The Discord server, Instagram, Facebook and YouTube are run by those companies, under their own policies.</li>
    </ul>

    <h2>Questions, or deleting your details</h2>
    <p>Email <a href="mailto:dylan@dylanmaudio.com">dylan@dylanmaudio.com</a>. I&rsquo;ll tell you what I hold, correct it, or delete it, except records I must keep for tax and consumer law; once your order records are gone I can&rsquo;t send your key again or free its seats. For anything a store holds, I&rsquo;ll ask it to do the same.</p>
  </article>
</main>
"""

CSS = r"""
  /* Privacy */
  main { flex:1; display:block; }
  .pv { max-width:760px; margin:0 auto; padding:clamp(48px,8vw,88px) var(--pad); }
  .pv h1 { font-size:clamp(1.9rem,4.2vw,2.7rem); line-height:1.1; letter-spacing:-0.02em; font-weight:650; margin:16px 0 0; }
  .pv .lede { margin:16px 0 0; color:var(--muted); font-size:clamp(1.02rem,1.5vw,1.12rem); }
  .pv .upd { font-family:var(--mono); font-size:12px; color:var(--dim); margin:12px 0 0; }
  .pv h2 { font-size:1.15rem; font-weight:640; margin:40px 0 10px; }
  .pv ul { margin:0; padding-left:20px; color:var(--muted); }
  .pv li { margin:0 0 10px; }
  .pv li strong { color:var(--text); font-weight:600; }
  .pv p { color:var(--muted); }
  .pv a { color:var(--blue); }
  .pv a:hover { text-decoration:underline; }
  .pv code { font-family:var(--mono); font-size:0.9em; }
"""


def build():
    html = NF.HTML
    head, rest = html.split("<main>", 1)
    tail = rest.split("</main>", 1)[1]
    tail = tail[:tail.index("<script>")] + "</body>\n</html>"          # drop the 404's path script
    head = (head.replace('<meta name="robots" content="noindex, follow">\n', "")
                .replace("<title>Page not found — Dylan [M] Audio</title>",
                         '<title>Privacy — Dylan [M] Audio</title>\n'
                         '<meta name="description" content="What dylanmaudio.com, the store and the apps collect: '
                         'no cookies on the site, the apps send no usage data, and who handles your purchase and licence.">')
                .replace("</style>", CSS + "</style>"))
    assert "<title>Privacy" in head and "noindex" not in head
    out = (head + BODY.strip("\n").replace("__UPDATED__", UPDATED) + "\n" + tail)
    out = (out.replace("__DISCORD_URL__", C.DISCORD_URL)
              .replace("__DISCORD_SVG__", C.DISCORD_SVG)
              .replace("__STORE_URL__", C.STORE_URL)
              .replace("__NONAFFIL__", C.NONAFFIL))
    C.write("privacy/index.html", C.inject_analytics(out))


if __name__ == "__main__":
    build()
