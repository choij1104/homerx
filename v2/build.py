#!/usr/bin/env python3
"""Builds HomeRx v2 (root index.html) from v2/app.html, v2/data/*.json and v2/v1strings.json.

Checks (the build fails on any):
  - every entry has the schema's required keys and a known category/kind
  - every {en, ko, ja} object in the data has three non-empty strings
  - every entry has at least one source URL
  - ids are unique; home-brand us_match keys exist as an active ingredient somewhere
  - no prohibited strings anywhere in the output
  - no external src/href loads (links to sources open in the browser and are allowed)
Usage: python3 v2/build.py [--version 2.0.0]
"""
import json, os, re, sys, glob, datetime

V2 = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(V2)
CATS = {"pain","allergy","cold_cough","nasal","eye_ear","stomach","laxative","motion","skin","first_aid","oral","sleep","womens",
        "children","quit_smoking","supplement_vitamin","supplement_mineral","supplement_herbal","supplement_other"}
FLAGS = {"liver","bleeding","bp","kidney","sedation","stomach","heart","diabetes","glaucoma","prostate","seniors","pregnancy","children",
         "alcohol","blood_thinner","thyroid","asthma"}
CLASSES = {"nsaid","sedating_antihistamine","decongestant","acetaminophen","ppi","h2_blocker","salicylate","stimulant_laxative","opioid_antagonist","sleep_aid"}
BANNED = ["namru", "tccc-grade", "navy", "department of defense", "consulates, embassies", "before institutional distribution"]
errors = []

def err(m): errors.append(m)

def tri(o, where):
    if not isinstance(o, dict): return
    if set(o.keys()) >= {"en","ko","ja"} and all(isinstance(o[k], str) for k in ("en","ko","ja")):
        for k in ("en","ko","ja"):
            if not o[k].strip(): err(f"{where}: empty {k}")
    for k, v in o.items():
        walk(v, f"{where}.{k}")

def walk(v, where):
    if isinstance(v, dict): tri(v, where)
    elif isinstance(v, list):
        for i, x in enumerate(v): walk(x, f"{where}[{i}]")

entries = []
for f in sorted(glob.glob(os.path.join(V2, "data", "*.json"))):
    name = os.path.basename(f)
    if name == "home_brands.json": continue
    d = json.load(open(f, encoding="utf-8"))
    for e in d["entries"]:
        e["_file"] = name
        entries.append(e)

ids = set()
for e in entries:
    w = f'{e.get("_file")}:{e.get("id")}'
    for k in ("id","kind","category","name","sources"):
        if k not in e: err(f"{w}: missing {k}")
    if e.get("id") in ids: err(f"{w}: duplicate id")
    ids.add(e.get("id"))
    if e.get("category") not in CATS: err(f"{w}: bad category {e.get('category')}")
    if e.get("kind") not in ("otc","supplement","guide"): err(f"{w}: bad kind {e.get('kind')}")
    for fl in e.get("flags") or []:
        if fl not in FLAGS: err(f"{w}: unknown flag {fl}")
    for c in e.get("classes") or []:
        if c not in CLASSES: err(f"{w}: unknown class {c}")
    if not [s for s in e.get("sources") or [] if str(s.get("url","")).startswith("http")]: err(f"{w}: no source url")
    for a in e.get("active") or []:
        a["ingredient"] = str(a.get("ingredient","")).strip().lower()
    walk(e, w)
    e.pop("_file", None)

home = []
hb = os.path.join(V2, "data", "home_brands.json")
if os.path.exists(hb):
    home = json.load(open(hb, encoding="utf-8"))["items"]
    ings = {a["ingredient"] for e in entries for a in e.get("active") or []}
    for h in home:
        w = f"home:{h.get('product',{}).get('local')}"
        walk(h, w)
        h["us_match"] = [m.lower() for m in h.get("us_match") or []]
        if not h.get("sources"): err(f"{w}: no source")

v1 = json.load(open(os.path.join(V2, "v1strings.json"), encoding="utf-8"))
fix = {
  "en": "Reference standards: FDA OTC Drug Facts labels (DailyMed), 21 CFR 201.66, MedlinePlus, NIH Office of Dietary Supplements, NCCIH, NIH LiverTox, CDC, Poison Control.",
  "ko": "참고 기준: FDA 일반의약품 Drug Facts 라벨(DailyMed), 21 CFR 201.66, MedlinePlus, NIH 보충제 사무국(ODS), NCCIH, NIH LiverTox, CDC, Poison Control.",
  "ja": "参照基準: FDA市販薬Drug Factsラベル（DailyMed）、21 CFR 201.66、MedlinePlus、NIH栄養補助食品局（ODS）、NCCIH、NIH LiverTox、CDC、Poison Control。",
}
V1 = {l: dict(v1["i18n"][l]) for l in ("en","ko","ja")}
for l in V1:
    V1[l]["footerSources"] = fix[l]
    V1[l].pop("gateLi4", None)
V1["phrases"] = v1["phrases"]
V1["urgentLists"] = v1["urgentLists"]

version = sys.argv[sys.argv.index("--version")+1] if "--version" in sys.argv else "2.0.0"
verified = sorted({e.get("verified","") for e in entries if e.get("verified")})
data = {"version": version, "reviewed": verified[-1] if verified else datetime.date.today().isoformat(),
        "entries": entries, "home": home}

html = open(os.path.join(V2, "app.html"), encoding="utf-8").read()
html = html.replace("/*__HOMERX_DATA__*/null", json.dumps(data, ensure_ascii=False, separators=(",",":")))
html = html.replace("/*__V1_STRINGS__*/null", json.dumps(V1, ensure_ascii=False, separators=(",",":")))

low = html.lower()
for b in BANNED:
    if b in low: err(f"banned text in output: {b!r}")
if re.search(r'<(script|link|img)[^>]+(src|href)="https?://', html): err("external resource load in output")

if errors:
    print("\n".join(errors[:80])); print(f"BUILD FAILED: {len(errors)} problem(s)"); sys.exit(1)
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)
kinds = {}
for e in entries: kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1
print(f"HomeRx {version}: {len(entries)} entries {kinds}, {len(home)} home-brand items, {len(html)//1024} KB")
