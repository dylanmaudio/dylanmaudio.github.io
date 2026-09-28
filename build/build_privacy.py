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

UPDATED = "27 September 2026"

BODY = r"""
<main>
  <article class="pv">
    <div class="kicker"><span class="tick">//</span>&nbsp; Privacy</div>
    <h1>Privacy</h1>
    <p class="lede">Short version: this website sets no cookies and runs no ad tags. The store, run by Lemon Squeezy, is where your details go when you buy or download, and it uses Meta&rsquo;s Pixel so I can measure and target my ads. The apps send nothing about how you use them.</p>
    <p class="upd">Updated __UPDATED__</p>

    <h2>This website</h2>
    <ul>
      <li><strong>No cookies, no ad or tracking tags,</strong> and nothing stored in your browser to follow you around.</li>
      <li><strong>Visitor counts</strong> come from Cloudflare Web Analytics, which is cookieless and doesn&rsquo;t identify you.</li>
      <li><strong>Hosting:</strong> the site is served by GitHub Pages; GitHub keeps standard server logs, including IP addresses, for security (<a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener">GitHub&rsquo;s privacy statement</a>).</li>
      <li><strong>Where you came from:</strong> if you arrive from a post, an email or an ad whose link carries a campaign tag (<code>utm_source</code> and the like), the site passes that tag to the store link you click, so the order records which post or ad worked. Nothing is saved on your device.</li>
      <li><strong>Videos</strong> are embedded in YouTube&rsquo;s privacy-enhanced mode (youtube-nocookie.com), which doesn&rsquo;t set cookies until you press play.</li>
      <li><strong>The contact form</strong> sends your name, email and message to me through Web3Forms. I use them to reply, and for nothing else.</li>
    </ul>

    <h2>The store</h2>
    <ul>
      <li><strong>store.dylanmaudio.com is run by Lemon Squeezy</strong>, the merchant of record: it takes payment, handles tax, issues licence keys and sends receipts and download emails. What it collects is set out in <a href="https://www.lemonsqueezy.com/privacy" target="_blank" rel="noopener">Lemon Squeezy&rsquo;s privacy policy</a>.</li>
      <li><strong>Free trials, free apps and Get notified</strong> go through the store too, with your email address. I use it to send the download, update news and launch news &mdash; never sold or shared &mdash; and you can unsubscribe from any email.</li>
      <li><strong>Meta Pixel:</strong> the store uses Meta&rsquo;s Pixel to count what my ads lead to and to show ads to people who&rsquo;ve visited it. It runs on the store and checkout only, not on this website. You can limit it in your <a href="https://www.facebook.com/adpreferences" target="_blank" rel="noopener">Meta ad preferences</a> or with your browser&rsquo;s tracking protection.</li>
    </ul>

    <h2>The apps</h2>
    <ul>
      <li><strong>No analytics and no usage data.</strong> The apps don&rsquo;t report what you do with them.</li>
      <li><strong>Licence:</strong> a paid app contacts Lemon Squeezy&rsquo;s licence service when you activate your key, and re-checks it at most every 14 days, at launch. That sends the key and a name for this Mac &mdash; nothing else.</li>
      <li><strong>Check for updates</strong> downloads a small file from dylanmaudio.com, only when you press the button.</li>
      <li><strong>Logs stay on your Mac.</strong> Export log saves a zip for you to send me if something goes wrong; nothing is sent on its own.</li>
      <li>Everything else the apps talk to is on your own network &mdash; the console, MIDI Bridge, Companion.</li>
    </ul>

    <h2>Elsewhere</h2>
    <ul>
      <li>The Discord server, Instagram, Facebook and YouTube are run by those companies, under their own policies.</li>
    </ul>

    <h2>Questions, or deleting your details</h2>
    <p>Email <a href="mailto:dylan@dylanmaudio.com">dylan@dylanmaudio.com</a>. I&rsquo;ll tell you what I hold and remove it; for anything the store holds, I&rsquo;ll ask Lemon Squeezy to do the same.</p>
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
                         'no cookies on the site, Lemon Squeezy runs the store, the apps send no usage data.">')
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
