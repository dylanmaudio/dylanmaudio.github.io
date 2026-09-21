#!/usr/bin/env python3
"""Regenerate the whole site. Run from anywhere:  python3 build/build_all.py"""
import runpy, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

for mod in ("build_site", "build_about", "build_products", "build_404", "build_redirects", "build_seo"):
    print(f"--- {mod} ---")
    runpy.run_path(str(HERE / f"{mod}.py"), run_name="__main__")
print("done.  (run build_og.py separately to regenerate the share image)")
