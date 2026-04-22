# HomeRx

Educational reference for common over-the-counter (OTC) medications and dietary supplements sold in U.S. pharmacies.

**Status:** Private prototype — not for public distribution.

## What it is

A single-file web app that provides FDA-approved uses, dosing, warnings, and drug interactions for 40 common items:

- **25 OTC medications** across 6 categories (pain/fever, allergy/cold, cough/throat, stomach/GI, skin/topical, other)
- **15 dietary supplements** with NIH ODS evidence tiers (Strong / Emerging / Limited)

All information sourced from:
- FDA OTC Monographs (public domain)
- DailyMed (NIH)
- MedlinePlus (NIH)
- NIH Office of Dietary Supplements

## Features

- Bilingual (English / Korean)
- Adjustable text size (Normal / Large / Extra Large)
- Offline — single HTML file, no network required after load
- Category filter + full-text search
- Strong disclaimer gate (must acknowledge 3 conditions before use)
- Emergency numbers always visible (911, Poison Control, 988)
- Editorial monochrome design optimized for readability

## Legal positioning

This app **does not recommend** any medication or supplement. It displays:

- For OTC drugs: only FDA-approved uses from public monographs
- For supplements: common uses with NIH ODS evidence levels and DSHEA 1994 regulatory context

All content requires user acknowledgment that the app is educational only, not medical advice, and does not replace a pharmacist or doctor.

## Access

This repo uses `noindex` meta tags and `robots.txt` to prevent search engine indexing. Access is by direct URL only.

## Files

- `index.html` — the complete app (HTML + CSS + JS + data)
- `manifest.json` — PWA manifest for home screen install
- `icon.svg`, `icon-192.png`, `icon-512.png` — app icons
- `robots.txt` — search engine exclusion
- `LICENSE` — copyright notice

## Deploying to GitHub Pages

1. Create a new public repository named `homerx` on GitHub (empty, no README)
2. Clone it locally, copy these files in, then push:
   ```bash
   git add .
   git commit -m "Initial HomeRx prototype"
   git push origin main
   ```
3. On GitHub, go to **Settings → Pages**
4. Under **Source**, select **Deploy from a branch** → **main** → **/ (root)** → **Save**
5. Wait 1–2 minutes, then access: `https://<your-username>.github.io/homerx/`

## Installing on iPhone / Android

1. Open the URL in Safari (iOS) or Chrome (Android)
2. Tap Share → **Add to Home Screen**
3. HomeRx icon appears on home screen and opens as a standalone app

## License

© 2026 Jae H. Choi, PhD, DVSc. All rights reserved.
HAKOYA LLC.

Content is for educational use only. Not for redistribution.
