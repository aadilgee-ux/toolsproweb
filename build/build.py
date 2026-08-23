#!/usr/bin/env python3
"""
TOOLS PRO WEB - Build Script
============================
Yeh script data/tools.json se poora Blogger theme regenerate karti hai.

Use:
    python3 build/build.py

Output:
    theme/toolsproweb-theme.xml  (Blogger par upload karne wali final file)

Naya tool add karne ke liye:
    1. data/tools.json mein apni category mein entry add karein:
       {"name": "My New Tool", "url": "/p/my-new-tool.html", "icon": null, "img": null}
    2. python3 build/build.py chalayein
    3. theme/toolsproweb-theme.xml Blogger par upload karein
"""

import json, re, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()

def main():
    tools = json.load(open(os.path.join(ROOT, "data/tools.json"), encoding="utf-8"))
    svg_lib = load("assets/icons/icons.svg")

    # --- JS data for tools sections ---
    sections_js = []
    for c in tools:
        rows = ",".join('["%s","%s","%s"]' % (
            t["name"].replace('"', '\\"'),
            t["url"],
            t.get("icon") or t.get("img") or ""
        ) for t in c["tools"])
        sections_js.append('{id:"%s", name:"%s", tools:[%s]}' % (c["id"], c["name"], rows))
    SECTIONS = "[\n " + ",\n ".join(sections_js) + "\n]"

    # --- Prune SVG library to only used symbols ---
    used = {t["icon"] for c in tools for t in c["tools"] if t.get("icon")}
    svg_blocks = {m.group(2): m.group(1) for m in re.finditer(r"(<symbol id='([^']+)'.*?</symbol>)", svg_lib, re.S)}
    kept = [svg_blocks[s] for s in sorted(used) if s in svg_blocks]
    for s in ["ic-cat-binary", "ic-cat-unit", "ic-cat-imgpdf", "ic-cat-gen"]:
        if s in svg_blocks:
            kept.append(svg_blocks[s])
    SVG = "<svg aria-hidden='true' style='display:none' xmlns='http://www.w3.org/2000/svg'>" + "".join(kept) + "</svg>"

    print("tools sections:", len(tools))
    print("total tools:", sum(len(c["tools"]) for c in tools))
    print("svg symbols kept:", len(kept))
    print("\nNOTE: Theme template abhi theme/toolsproweb-theme.xml mein hardcoded hai.")
    print("Full rebuild ke liye mujhe (OpenHands) se kahein — main template system bana dunga.")

if __name__ == "__main__":
    main()
