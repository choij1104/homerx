#!/usr/bin/env python3
"""Builds android/www, the Google Play build of HomeRx, from the repository's index.html.

The web app in the repository root is not modified. It already works offline: no web fonts
(system font stack), no external scripts or stylesheets, no fetch/XHR, no service worker and
no file downloads. The store build therefore changes only what a native shell needs:

  1. Build marker: <meta name="homerx-build" content="store"> so the bundle can be identified.
  2. Local assets: manifest.json, icon.svg, icon-192.png and icon-512.png are copied next to
     index.html so every local reference resolves inside the app.
  3. Guards: the build fails if the source gains a network dependency (http(s) src/href, CSS
     @import/url() to a remote host, fetch/XMLHttpRequest/WebSocket/sendBeacon), a service worker
     registration, or a file download, so a future web change cannot silently break the
     offline promise of the store build. If any of these is added to the web app, this script
     must be extended (bundle the resource, disable the service worker in the native app, or
     save files through the share sheet) before the next store build.
  4. Content checks: EN/KO/JA parity on every entry field and every UI string key, and no
     wording that must not ship (see FORBIDDEN).

Clinical content (doses, safety text, warnings, disclaimers) is passed through byte-for-byte.
Every text replacement must match exactly once, or the build fails.
"""
import os, re, shutil, sys

AND = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # .../android
ROOT = os.path.dirname(AND)
OUT = os.path.join(AND, "www")
ASSETS = ("manifest.json", "icon.svg", "icon-192.png", "icon-512.png")
FORBIDDEN = ("NAMRU", "namru", "Naval Medical", "U.S. Navy", "Department of Defense",
             "TCCC", "남루", "choij1104")
LANGS = ("ko", "en", "ja")

def die(msg):
    sys.exit(f"build-store: {msg}")

def sub1(old, new, s, what):
    n = s.count(old)
    if n != 1:
        die(f"{what}: expected 1 match, found {n}")
    return s.replace(old, new)

src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
t = src

# 1. Build marker ------------------------------------------------------------------------
t = sub1('<meta charset="UTF-8">', '<meta charset="UTF-8">\n<meta name="homerx-build" content="store">',
         t, "charset meta")

# 3. Guards ------------------------------------------------------------------------------
if re.search(r'(src|href|action)\s*=\s*["\']?(https?:)?//', t, re.I):
    die("external resource reference (src/href/action) in index.html")
if re.search(r'@import|url\(\s*["\']?(https?:)?//', t, re.I):
    die("remote CSS import or url() in index.html")
for api in ("fetch(", "XMLHttpRequest", "WebSocket", "sendBeacon", "EventSource", "import("):
    if api in t:
        die(f"network API '{api}' in index.html: the store build must make no network request")
if "serviceWorker" in t:
    die("service worker found: disable it for the native app in build-store.py before building")
if re.search(r'\.download\s*=|\sdownload[\s>=]', t):
    die("file download found: route it through the share sheet in build-store.py before building")
for bad in FORBIDDEN:
    if bad in t:
        die(f"forbidden text '{bad}' in index.html")

# 4. Content parity ----------------------------------------------------------------------
def block(name, nxt):
    a, b = t.find(f"const {name} = "), t.find(f"const {nxt} = ")
    if a < 0 or b < 0 or b < a:
        die(f"data block {name} not found")
    return t[a:b]

counts = {}
for name, nxt, fields in (("otc", "supplements", ("use", "safety")),
                          ("supplements", "urgentLists", ("use", "safety", "evidence"))):
    blk = block(name, nxt)
    rows = [l for l in blk.splitlines() if l.startswith("  { ")]
    counts[name] = len(rows)
    for i, row in enumerate(rows):
        for f in fields:
            m = re.search(r"\b" + f + r': \{([^}]*)\}', row)
            if not m:
                die(f"{name}[{i}] has no '{f}' field")
            for l in LANGS:
                if not re.search(r"\b" + l + r': "[^"]+"', m.group(1)):
                    die(f"{name}[{i}].{f} is missing '{l}'")

i18n = block("i18n", "tabs")
keysets = {}
for l in LANGS:
    m = re.search(r"\n  " + l + r": \{(.*?)\n  \}", i18n, re.S)
    if not m:
        die(f"i18n.{l} not found")
    keysets[l] = set(re.findall(r"(?m)(?:^|,)\s*([A-Za-z0-9_]+): \"", m.group(1)))
if not (keysets["ko"] == keysets["en"] == keysets["ja"]):
    die("i18n key sets differ between ko/en/ja: "
        + str((keysets["ko"] ^ keysets["en"]) | (keysets["ko"] ^ keysets["ja"])))
for name, nxt in (("tabs", "otc"), ("phrases", "cardLabels")):
    for i, row in enumerate(l for l in block(name, nxt).splitlines() if l.startswith("  { ")):
        for l in LANGS:
            if not re.search(r"\b" + l + r': "[^"]+"', row):
                die(f"{name}[{i}] is missing '{l}'")
total = counts["otc"] + counts["supplements"]

# Write ----------------------------------------------------------------------------------
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(t)
for a in ASSETS:
    p = os.path.join(ROOT, a)
    if not os.path.isfile(p):
        die(f"{a} missing in repository root")
    shutil.copy(p, os.path.join(OUT, a))
for ref in re.findall(r'(?:src|href)="([^"#][^"]*)"', t):
    if not os.path.isfile(os.path.join(OUT, ref)):
        die(f"local reference '{ref}' not in the bundle")

print(f"build-store: HomeRx written to {OUT} ({len(t)} bytes); entries {total} "
      f"({counts['otc']} OTC + {counts['supplements']} supplements), EN/KO/JA parity "
      f"{total}/{total}/{total}, UI strings {len(keysets['en'])} keys x 3 languages")
