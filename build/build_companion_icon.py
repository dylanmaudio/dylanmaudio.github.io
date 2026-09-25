#!/usr/bin/env python3
"""Render assets/companion.png — the icon for the Companion module page.

A dark rounded tile with a 3×2 grid of keys, some lit in the site's
signal colours: the shape of a Stream Deck page, no third-party logo.
Matches the 256 px app icons in /assets. Re-run after a colour change.
"""
from PIL import Image, ImageDraw, ImageFilter
import pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "companion.png"
S = 4 * 256                       # supersample, downscale at the end
BG_TOP, BG_BOT = (30, 36, 44), (14, 17, 22)
KEY_OFF = (38, 45, 55)
BLUE, GREEN, AMBER = (79, 163, 247), (98, 210, 122), (232, 158, 60)
LIT = {0: BLUE, 2: GREEN, 4: AMBER}   # key index → colour (row-major, 3 wide)


def rounded(draw, box, r, fill):
    draw.rounded_rectangle(box, radius=r, fill=fill)


def build():
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    # tile with a vertical gradient
    grad = Image.new("RGBA", (S, S))
    gd = ImageDraw.Draw(grad)
    for y in range(S):
        t = y / (S - 1)
        gd.line([(0, y), (S, y)], fill=tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3)) + (255,))
    mask = Image.new("L", (S, S), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, S - 1, S - 1), radius=int(S * 0.225), fill=255)
    img.paste(grad, (0, 0), mask)

    # key grid
    cols, rows = 3, 2
    pad, gap = int(S * 0.17), int(S * 0.055)
    kw = (S - 2 * pad - (cols - 1) * gap) / cols
    top = (S - (rows * kw + (rows - 1) * gap)) / 2
    glow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    d = ImageDraw.Draw(img)
    for i in range(cols * rows):
        c, r = i % cols, i // cols
        x0 = pad + c * (kw + gap); y0 = top + r * (kw + gap)
        box = (x0, y0, x0 + kw, y0 + kw)
        col = LIT.get(i)
        if col:
            rounded(gdraw, box, kw * 0.2, col + (150,))
            rounded(d, box, kw * 0.2, col + (255,))
            # inner highlight
            rounded(d, (x0 + kw * 0.12, y0 + kw * 0.12, x0 + kw * 0.88, y0 + kw * 0.30), kw * 0.08,
                    tuple(min(255, v + 45) for v in col) + (90,))
        else:
            rounded(d, box, kw * 0.2, KEY_OFF + (255,))
    glow = glow.filter(ImageFilter.GaussianBlur(S * 0.03))
    out = Image.alpha_composite(Image.new("RGBA", (S, S), (0, 0, 0, 0)), img)
    out = Image.alpha_composite(Image.composite(glow, Image.new("RGBA", (S, S), (0, 0, 0, 0)), mask), out)
    out.resize((256, 256), Image.LANCZOS).save(OUT)
    print("wrote", OUT.relative_to(OUT.parent.parent))


if __name__ == "__main__":
    build()
