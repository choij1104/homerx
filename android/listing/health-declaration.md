# HomeRx — Health apps declaration (Play Console → App content → Health apps)

## Health features — tick only these

| Category | Feature | Tick |
|---|---|---|
| Medical | **Medical reference and education** (medicines, supplements, conditions) | **Yes** |
| Medical | Health information / health literacy (if listed separately) | Yes |
| Medical | Medication management (reminders, dosing trackers, refill) | No — "My cabinet" is an on-device list of products the user owns, with optional expiry dates and label-based overlap checks (same ingredient twice, same drug class twice). No reminders, schedules, dose logging or refills |
| Medical | Clinical decision support / diagnosis / disease management | No — it does not assess symptoms or tell a user what to take. Ticked conditions ("My health") only highlight the matching warnings already printed on the U.S. label |
| Medical | Medical device apps / apps that connect to medical devices | No |
| Medical | Electronic health records, telehealth, prescription services | No |
| Health & fitness | Activity, nutrition tracking, sleep tracking, mental health tools | No — the app has a Sleep category of OTC sleep aids, but no tracking |
| Other | Health research, period tracking, emergency response | No — the Help tab lists 911, Poison Control and 988; tapping one opens the phone's dialer. The app sends no alerts |

## Regulatory questions

| Question | Answer |
|---|---|
| Is your app a medical device, or does it require regulatory clearance/approval (e.g. FDA)? | **No.** It is a general educational reference; it does not diagnose, treat, mitigate or prevent disease and gives no patient-specific recommendations |
| Does the app have FDA (or other) clearance, approval or registration? | No — and the listing makes no such claim |
| Does the app collect health data or connect to Health Connect? | No. Cabinet items and ticked conditions stay on the device and are never transmitted (see data-safety.md); no Health Connect permissions |
| Privacy policy URL | https://choij1104.github.io/homerx/privacy.html |

## Disclaimer — where it appears (reviewers often check this)
- First launch: a disclaimer screen in English, Korean or Japanese: "Educational material · Not
  medical advice · Liability limitation", with four boxes the user must tick before continuing
  (educational only; no liability; read the label and ask a pharmacist or doctor; use 911 in an
  emergency).
- Help tab (bottom bar, every screen): 911, Poison Control 1-800-222-1222, 988.
- Footer: "Educational material only. Not medical diagnosis, prescribing, or treatment."
- Store listing: "educational reference only … not medical advice, diagnosis or treatment and is
  not a medical device."

## Content sources (as named in the app)
FDA OTC Drug Facts labels (DailyMed), 21 CFR 201.66, MedlinePlus, NIH Office of Dietary Supplements,
NCCIH, NIH LiverTox, CDC, Poison Control; for Korea/Japan items, the Korea Pharmaceutical Information Center
and the makers' product pages. Each entry lists its own sources and the date checked. Content is shipped exactly as in the web app; the store build does not edit any
dose or safety text.
