# HomeRx — OTC 의약품·보충제 참조 웹앱

**배포:** https://choij1104.github.io/homerx/
**저자:** Jae H. Choi, PhD, DVSc · HAKOYA LLC

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

## 파일 구조

- `index.html` — 메인 PWA (단일 파일, 4007 lines, ~586 KB)
- `README.md` — 본 문서

## 데이터 소스

- FDA OTC Monograph
- DailyMed (NIH)
- MedlinePlus (NIH)
- NIH Office of Dietary Supplements (ODS)
- ADA, AAP, CDC, WHO Essential Medicines List
- NIH LiverTox Database (NIDDK)
- FDA Tainted Dietary Supplement Database (2007–2021)
- Clean Label Project (independent testing)

## 다음 작업 (선택)

1. ✅ ~~남은 항목 일본어 번역 완료~~ — 완료
2. Mother Program (`SOF_TCCC_MOTHER.html` 패턴) 통합 검토
3. PWA manifest 및 service worker 추가
4. 검색 인덱스에 일본어 키워드 포함
5. Beta 사용자 피드백 수집

## 라이선스

© 2026 HAKOYA LLC. All rights reserved.
교육용·참고용. 의학적 조언을 대체하지 않음 (Disclaimer gate 강제).
