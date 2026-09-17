#!/usr/bin/env python3
"""Generate sitemap.xml and robots.txt.

Only LIVE, linked pages go in the sitemap. Parked product pages are excluded
(they also carry <meta name="robots" content="noindex">) until their product
ships — add their URL here and drop the noindex in common/build_products then.
"""
import datetime
import common as C

# Site-relative paths of the pages we want indexed. Add products at launch.
PAGES = [
    ("/", "1.0"),
    ("about.html", "0.8"),
    ("products/talk-light-trigger/", "0.7"),
    ("products/midi-bridge/", "0.7"),
    ("products/pilot-tone-trigger/", "0.7"),
]

def build():
    today = datetime.date.today().isoformat()
    urls = "\n".join(
        f"  <url><loc>{C.abs_url(p)}</loc><lastmod>{today}</lastmod>"
        f"<changefreq>monthly</changefreq><priority>{pr}</priority></url>"
        for p, pr in PAGES
    )
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               f"{urls}\n</urlset>\n")
    C.write("sitemap.xml", sitemap)

    robots = ("User-agent: *\n"
              "Allow: /\n\n"
              f"Sitemap: {C.abs_url('sitemap.xml')}\n")
    C.write("robots.txt", robots)


if __name__ == "__main__":
    build()
