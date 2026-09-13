#!/usr/bin/env python3
"""Render the badge master + favicons from build/assets-src/logo.svg.

logo.svg is the crisp white-M/bars mark (recolored from the original in
logo-original-black.svg: black strokes -> white, their halos -> disc grey, both
rings kept). Renders the 1024 master with headless Chrome, then downsamples the
favicons with Pillow LANCZOS for crisp small sizes. Run when the mark changes:

    python3 build/build_icons.py && python3 build/build_og.py
"""
import subprocess
from PIL import Image
import common as C

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SRC = C.ROOT / "build/assets-src/logo.svg"
ASSETS = C.ROOT / "assets"

def render(px, out):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=1", "--default-background-color=00000000",
                    f"--window-size={px},{px}", f"--screenshot={out}", f"file://{SRC}"],
                   check=True, capture_output=True)

def build():
    master = ASSETS / "logo.png"
    render(1024, master)
    print("wrote", master.relative_to(C.ROOT))
    big = Image.open(master).convert("RGBA")
    for name, size in (("favicon-180.png", 180), ("favicon-32.png", 32), ("favicon-16.png", 16)):
        big.resize((size, size), Image.LANCZOS).save(ASSETS / name)
        print("wrote", (ASSETS / name).relative_to(C.ROOT))


if __name__ == "__main__":
    build()
