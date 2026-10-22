# HomeRx v2 data schema

One JSON file per batch: `v2/data/<batch>.json` containing `{"entries": [ ... ]}`.
Every field with `{en, ko, ja}` must have all three languages filled (parity is checked by the build).

## Entry

```json
{
  "id": "acetaminophen",                       // kebab-case, unique
  "kind": "otc",                               // "otc" | "supplement" | "guide" (guidance topic, no single product)
  "category": "pain",                          // see Categories
  "name":    {"en": "Acetaminophen", "ko": "아세트아미노펜", "ja": "アセトアミノフェン"},
  "aka":     ["paracetamol", "APAP"],          // other names people search for (any language)
  "brands":  ["Tylenol", "Mapap"],             // common US brand / store-brand names
  "active":  [{"ingredient": "acetaminophen", "strength": "325 mg, 500 mg (per tablet/caplet)", "purpose": "Pain reliever/fever reducer"}],
                                               // ingredient = lowercase key used for duplicate detection;
                                               // strength/purpose exactly as the Drug Facts label states
  "uses":    {"en": "...", "ko": "...", "ja": "..."},
  "directions_adult": {"en": "...", "ko": "...", "ja": "..."},   // adults and children 12+ as the label states; null for supplements without label directions
  "max_daily": {"en": "...", "ko": "...", "ja": "..."},          // label maximum; null if the label states none
  "children": {"en": "...", "ko": "...", "ja": "..."},           // ONLY what the label says (e.g. "under 12: ask a doctor" / "use a product made for children").
                                                                 // Never weight-based doses or numbers not printed on an adult label.
  "do_not_use": [{"en": "...", "ko": "...", "ja": "..."}],       // label "Do not use"
  "ask_doctor": [{"en": "...", "ko": "...", "ja": "..."}],       // label "Ask a doctor before use if you have"
  "ask_pharmacist": [{"en": "...", "ko": "...", "ja": "..."}],   // label "Ask a doctor or pharmacist before use if you are taking"
  "stop_use":  [{"en": "...", "ko": "...", "ja": "..."}],        // label "Stop use and ask a doctor if"
  "key_warning": {"en": "...", "ko": "...", "ja": "..."},        // the single most important safety point, plain words (label-based)
  "older_adults": {"en": "...", "ko": "...", "ja": "..."},       // 65+ note if a source supports it (e.g. AGS Beers Criteria 2023), else null
  "pregnancy": {"en": "...", "ko": "...", "ja": "..."},          // label wording (e.g. "ask a health professional before use"); add specific label text if present
  "flags": ["liver", "bleeding", "bp", "kidney", "sedation", "stomach", "heart", "diabetes", "glaucoma", "prostate", "seniors", "pregnancy", "children", "alcohol", "blood_thinner"],
                                               // conditions the label/source warns about (use only these keys)
  "classes": ["nsaid"],                        // optional class keys for stacking checks: nsaid, sedating_antihistamine, decongestant,
                                               // acetaminophen, ppi, h2_blocker, salicylate, stimulant_laxative, opioid_antagonist, sleep_aid
  "supplement_note": {"en": "...", "ko": "...", "ja": "..."},    // supplements only: evidence summary + safety, from NIH ODS / NCCIH / FDA
  "sources": [{"title": "DailyMed — Tylenol Extra Strength Drug Facts", "url": "https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=..."}],
  "verified": "2026-10-22"                     // date the source was read
}
```

Omit nothing: use `null` for an object field that does not apply and `[]` for an empty list.

## Categories
pain, allergy, cold_cough, nasal, eye_ear, stomach, laxative, motion, skin, first_aid, oral, sleep, womens, children, quit_smoking, supplement_vitamin, supplement_mineral, supplement_herbal, supplement_other

## Rules
- Read the primary source first (DailyMed Drug Facts label of a representative US OTC product; for supplements NIH Office of Dietary Supplements fact sheets, NCCIH, or FDA). Every fact must come from a source listed in `sources`.
- Doses: copy the label; do not compute, round, or add doses. Children: label text only, never weight-based numbers.
- Plain words for seniors. Korean and Japanese are natural translations, not literal; keep drug names recognizable (add the English in parentheses where helpful).
- No brand claims beyond names. No "FDA approved" for supplements. Never write NAMRU, TCCC-grade, Navy, Department of Defense.
