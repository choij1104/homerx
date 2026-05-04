# HomeRx — OTC 의약품·보충제 참조 웹앱

**배포:** https://choij1104.github.io/homerx/
**저자:** Jae H. Choi, PhD, DVSc · HAKOYA LLC, San Antonio, Texas
**언어:** English / 한국어 / 日本語

---

## 현재 상태 (2026-04-28) — 3개 언어 완전 통합 완료 ✅

### Phase 1 — 콘텐츠 확장: ✅ 완료
- **114개 항목** (61개 → 114개)
- **14개 카테고리:** pain (6), allergy (9), cough (4), gi (15), skin (8), sleep (8), womens (7), pediatric (8), eye_ear (7), oral (7), first_aid (8), other (1), supplement (26)

### Phase 2 — 3개 언어 i18n 인프라: ✅ 완료
- 언어 토글: EN ↔ 한국어 ↔ 日本語 (3-way)
- 통합 라벨 시스템 (`L(key)` helper, ~16 라벨)
- 카드 렌더링: `[currentLang]` 자동 fallback (en)
- UI HTML 전체에 `data-ja` 속성 적용 (~21 elements)
- 14개 카테고리 모두 `ja` 필드 보유

### Phase 3 — 일본어 데이터 번역: ✅ 완료 (114/114)

**전체 카테고리 완료:**
- ✅ Pain (6/6)
- ✅ Allergy (9/9)
- ✅ Cough (4/4)
- ✅ GI (15/15)
- ✅ Skin (8/8)
- ✅ Sleep (8/8)
- ✅ Womens (7/7)
- ✅ Pediatric (8/8)
- ✅ Eye/Ear (7/7)
- ✅ Oral (7/7)
- ✅ First Aid (8/8)
- ✅ Other (1/1)
- ✅ Supplement (26/26)

### 검증 결과 (validate.js)
| 필드 | EN | JA | 일치 |
|------|-----|-----|------|
| generic.ja | 114 | 114 | ✅ |
| warn_ja | 114 | 114 | ✅ |
| danger_ja | 57 | 57 | ✅ |
| overuse_ja | 20 | 20 | ✅ |
| dose_ja | 114 | 114 | ✅ |
| uses titles ja | 216 | 216 | ✅ |
| interact ja | 333 | 333 | ✅ |

---

## 파일 구조

- `index.html` — 메인 PWA (단일 파일, 4,064 lines, ~589 KB)
- `README.md` — 본 문서
- `LICENSE` — 사용·재배포 조건

---

## 데이터 소스

- FDA OTC Monograph
- DailyMed (NIH)
- MedlinePlus (NIH)
- NIH Office of Dietary Supplements (ODS)
- NIH LiverTox Database (NIDDK)
- FDA Tainted Dietary Supplement Database (2007–2021)
- ADA, AAP, CDC, WHO Essential Medicines List
- Clean Label Project (independent third-party testing)

---

## 의학적 면책 (Medical Disclaimer)

이 애플리케이션은 **교육·참고 목적**으로만 제공됩니다.
의학적 진단, 치료, 처방을 대체하지 않으며,
약사·의사·기타 의료 전문가의 상담을 대신할 수 없습니다.

This application is an **EDUCATIONAL REFERENCE ONLY** and
does **NOT** constitute medical advice, diagnosis, or treatment.
Always read the product label and consult a licensed pharmacist
or physician before use.

---

## 저작권 및 라이선스 (Copyright & License)

**Copyright © 2026 Jae H. Choi, PhD, DVSc. All rights reserved.**
Developed and maintained by **HAKOYA LLC**, San Antonio, Texas, USA.

본 소프트웨어와 콘텐츠는 **개인·교육·비영리** 용도의 참조에 한해
사용이 허용됩니다. 코드 또는 콘텐츠의 일부 또는 전부에 대한
**재배포, 수정, 공개 호스팅, 상업적 사용**은 저작권자의
**서면 사전 허가** 없이는 금지됩니다.

This software and its content are provided for **personal,
educational, and non-commercial reference use only.**
Redistribution, modification, public hosting, or commercial use
of any part of this code or content is prohibited without prior
written permission from the copyright holder.

자세한 조건은 `LICENSE` 파일을 참조하십시오.
See `LICENSE` for full terms.

---

## 면책 사항 (Disclaimer)

본 자료에 포함된 견해는 저자 개인의 것이며,
미국 해군, 국방부, 또는 미국 정부의 공식 입장이나 정책을
반영하지 않습니다.

The views expressed are those of the author and do not reflect
the official policy or position of the U.S. Navy, Department of
Defense, or U.S. Government.

---

## 다음 작업 (선택)

1. ✅ ~~남은 항목 일본어 번역 완료~~ — 완료
2. Mother Program (`SOF_TCCC_MOTHER.html` 패턴) 통합 검토
3. PWA manifest 및 service worker 추가
4. 검색 인덱스에 일본어 키워드 포함
5. Beta 사용자 피드백 수집
