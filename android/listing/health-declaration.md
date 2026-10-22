# HomeRx — Health apps declaration (Play Console → App content → Health apps)

## Health features — tick only these

| Category | Feature | Tick |
|---|---|---|
| Medical | **Medical reference and education** (medicines, supplements, conditions) | **Yes** |
| Medical | Health information / health literacy (if listed separately) | Yes |
| Medical | Medication management (reminders, dosing trackers, refill) | No — the app has no reminders, schedules or dose logging |
| Medical | Clinical decision support / diagnosis / disease management | No — it does not assess symptoms or tell a user what to take |
| Medical | Medical device apps / apps that connect to medical devices | No |
| Medical | Electronic health records, telehealth, prescription services | No |
| Health & fitness | Activity, nutrition tracking, sleep tracking, mental health tools | No — the app has a Sleep category of OTC sleep aids, but no tracking |
| Other | Health research, period tracking, emergency response | No — emergency numbers (911, Poison Control, 988) are shown as text only; the app places no calls and sends no alerts |

## Regulatory questions

| Question | Answer |
|---|---|
| Is your app a medical device, or does it require regulatory clearance/approval (e.g. FDA)? | **No.** It is a general educational reference; it does not diagnose, treat, mitigate or prevent disease and gives no patient-specific recommendations |
| Does the app have FDA (or other) clearance, approval or registration? | No — and the listing makes no such claim |
| Does the app collect health data or connect to Health Connect? | No. No data collected (see data-safety.md); no Health Connect permissions |
| Privacy policy URL | Required — see listing.md, "Privacy policy" |

## Disclaimer — where it appears (reviewers often check this)
- First launch: a disclaimer screen in English, Korean or Japanese: "Educational material · Not
  medical advice · Liability limitation", with four boxes the user must tick before continuing
  (educational only; no liability; read the label and ask a pharmacist or doctor; use 911 in an
  emergency).
- Every screen: emergency line at the top (911, Poison Control 1-800-222-1222, 988).
- Footer: "Educational material only. Not medical diagnosis, prescribing, or treatment."
- Store listing: "educational reference only … not medical advice, diagnosis or treatment and is
  not a medical device."

## Content sources (as named in the app)
FDA OTC Monographs, DailyMed, MedlinePlus, NIH Office of Dietary Supplements, NIH LiverTox, CDC,
Poison Control. Content is shipped exactly as in the web app; the store build does not edit any
dose or safety text.
