<!DOCTYPE html>

<!--
  HomeRx — Home OTC Reference (Civilian Edition)
  © 2026 Jae H. Choi, PhD, DVSc. All rights reserved.
  Educational reference only. Not medical advice.
  Information derived from FDA OTC Monographs, DailyMed (NIH), and MedlinePlus (NIH).
-->

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="theme-color" content="#fafaf7">
<meta name="robots" content="noindex, nofollow, noarchive">
<meta name="googlebot" content="noindex, nofollow, noarchive">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="HomeRx">
<meta name="mobile-web-app-capable" content="yes">
<meta name="description" content="HomeRx — Educational reference for common OTC medications and dietary supplements. FDA-approved uses only. Not medical advice.">
<link rel="manifest" href="manifest.json">
<link rel="apple-touch-icon" href="icon-192.png">
<link rel="icon" type="image/svg+xml" href="icon.svg">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="HomeRx">
<meta name="mobile-web-app-capable" content="yes">
<meta name="description" content="HomeRx — Educational reference for common OTC medications and dietary supplements. FDA-approved uses only. Not medical advice.">
<link rel="manifest" href="manifest.json">
<link rel="apple-touch-icon" href="icon-192.png">
<link rel="icon" type="image/svg+xml" href="icon.svg">
<title>HomeRx — OTC Reference</title>
<style>
  :root {
    /* MONOCHROME + DEEP NAVY — editorial, refined */
    --bg: #fafaf7;                /* warm off-white, paper-like */
    --bg-elev: #f3f2ec;            /* slightly deeper paper tone */
    --bg-card: #ffffff;             /* clean white cards pop against warm bg */
    --border: #d9d6cc;              /* warm beige border */
    --border-bright: #8a8578;       /* stronger divider */
    --text: #1a1a2e;                /* deep ink — not pure black */
    --text-body: #26263d;           /* body ink */
    --text-dim: #595878;            /* dimmed but readable (7:1) */
    --accent: #1e3a5f;              /* midnight navy */
    --accent-solid: #1e3a5f;
    --accent-bg: #e8ecf3;           /* pale navy tint */
    --accent-dark: #0f1e33;
    --warn: #8a5a00;                /* deep amber, almost brown */
    --warn-bg: #f7f0dc;             /* cream paper */
    --warn-border: #c89030;
    --danger: #8b1a1a;               /* deep wine-red */
    --danger-strong: #6b0f0f;
    --danger-bg: #f5e3e3;             /* dusty rose */
    --danger-border: #b52828;
    --safe: #1f5c2f;                 /* forest green, not bright */
    --safe-bg: #e8efe5;
    --info: #2d4a7c;                 /* slightly lighter navy for supplements */
    --info-bg: #eaeef5;
    --font-serif: 'Iowan Old Style', 'Palatino Linotype', 'Cambria', Georgia, serif;
    --font-base: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', 'Noto Sans KR', system-ui, sans-serif;

```
--fs-base: 17px;
--fs-sm: 15px;
--fs-lg: 19px;
--fs-xl: 22px;
--fs-xxl: 28px;
```

}
body.text-large {
–fs-base: 19px; –fs-sm: 17px; –fs-lg: 22px; –fs-xl: 26px; –fs-xxl: 32px;
}
body.text-xlarge {
–fs-base: 22px; –fs-sm: 19px; –fs-lg: 26px; –fs-xl: 30px; –fs-xxl: 38px;
}

- { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
  html, body {
  background: var(–bg); color: var(–text-body);
  font-family: var(–font-base);
  font-size: var(–fs-base); line-height: 1.65;
  min-height: 100vh; overscroll-behavior: none;
  -webkit-font-smoothing: antialiased;
  }

/* DISCLAIMER GATE */
.gate { position: fixed; inset: 0; background: var(–bg); z-index: 1000; overflow-y: auto; padding: 20px; display: flex; align-items: flex-start; justify-content: center; }
.gate.hidden { display: none; }
.gate-card { max-width: 620px; width: 100%; background: var(–bg-card); border: 1px solid var(–border); border-radius: 4px; padding: 40px 32px; margin: 20px 0; box-shadow: 0 2px 40px rgba(26,26,46,0.06); }
.gate-title { font-family: var(–font-serif); font-size: var(–fs-xxl); font-weight: 600; margin-bottom: 6px; color: var(–text); letter-spacing: -0.01em; line-height: 1.15; }
.gate-subtitle { font-size: 12px; color: var(–text-dim); margin-bottom: 28px; font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; padding-bottom: 20px; border-bottom: 1px solid var(–border); }
.gate-body { font-size: var(–fs-base); color: var(–text-body); margin-bottom: 28px; line-height: 1.7; }
.gate-body p { margin-bottom: 16px; }
.gate-body ul { margin: 14px 0 14px 20px; }
.gate-body li { margin-bottom: 8px; color: var(–text-body); }
.gate-body strong { color: var(–text); font-weight: 700; }
.gate-checks { background: var(–bg); border: 1px solid var(–border); border-radius: 2px; padding: 20px; margin-bottom: 24px; }
.check-row { display: flex; gap: 14px; padding: 12px 0; align-items: flex-start; cursor: pointer; min-height: 44px; }
.check-row input[type=“checkbox”] { width: 22px; height: 22px; margin-top: 2px; accent-color: var(–accent); cursor: pointer; flex-shrink: 0; }
.check-row label { font-size: var(–fs-base); color: var(–text-body); cursor: pointer; line-height: 1.5; font-weight: 400; }
.gate-btn { width: 100%; padding: 18px; background: var(–accent-solid); color: #fafaf7; border: none; border-radius: 2px; font-size: var(–fs-base); font-weight: 600; cursor: pointer; transition: background 0.15s; min-height: 56px; text-transform: uppercase; letter-spacing: 0.1em; }
.gate-btn:disabled { background: var(–border); color: var(–text-dim); cursor: not-allowed; }
.gate-btn:not(:disabled):hover { background: var(–accent-dark); }
.gate-emergency { margin-top: 24px; padding: 20px; background: var(–danger-bg); border: 1px solid var(–danger-border); border-radius: 2px; font-size: var(–fs-sm); color: var(–text); line-height: 1.55; }
.gate-emergency strong { color: var(–danger); display: block; margin-bottom: 8px; font-size: 13px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; }

/* HEADER */
.header { position: sticky; top: 0; background: rgba(250,250,247,0.97); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border-bottom: 1px solid var(–border); padding: 14px 16px; z-index: 100; display: flex; align-items: center; gap: 10px; }
.logo { font-family: var(–font-serif); font-size: var(–fs-xl); font-weight: 700; letter-spacing: -0.01em; color: var(–text); font-style: italic; }
.logo-dot { color: var(–accent); font-style: normal; }
.header-spacer { flex: 1; }
.header-controls { display: flex; gap: 8px; align-items: center; }
.text-size-toggle { display: flex; background: var(–bg-card); border: 1px solid var(–border-bright); border-radius: 2px; overflow: hidden; }
.ts-btn { padding: 8px 10px; background: transparent; color: var(–text-dim); border: none; cursor: pointer; font-size: var(–fs-sm); font-weight: 700; min-width: 36px; min-height: 36px; font-family: var(–font-serif); }
.ts-btn.active { background: var(–accent-solid); color: #fafaf7; }
.lang-toggle { display: flex; background: var(–bg-card); border: 1px solid var(–border-bright); border-radius: 2px; overflow: hidden; }
.lang-btn { padding: 8px 12px; background: transparent; color: var(–text-dim); border: none; cursor: pointer; font-size: 12px; font-weight: 700; min-height: 36px; letter-spacing: 0.1em; }
.lang-btn.active { background: var(–accent-solid); color: #fafaf7; }

/* EMERGENCY STRIP */
.emergency-strip { background: var(–bg-card); border-bottom: 1px solid var(–danger-border); border-top: 3px solid var(–danger-border); padding: 14px 16px; font-size: 13px; color: var(–text); display: flex; align-items: center; gap: 10px; font-weight: 500; line-height: 1.4; letter-spacing: 0.02em; }
.emergency-strip::before { content: ‘⚠’; color: var(–danger); font-size: 20px; }
.emergency-strip strong { color: var(–danger); font-weight: 700; }

/* SEARCH */
.search-bar { padding: 20px 16px 16px; background: var(–bg); border-bottom: 1px solid var(–border); max-width: 760px; margin: 0 auto; width: 100%; }
.search-input { width: 100%; padding: 16px 18px; background: var(–bg-card); border: 1px solid var(–border-bright); border-radius: 2px; color: var(–text); font-size: var(–fs-base); outline: none; transition: border-color 0.15s; font-family: var(–font-base); font-weight: 400; }
.search-input:focus { border-color: var(–accent); }
.search-input::placeholder { color: var(–text-dim); font-style: italic; }

/* CATEGORY FILTER */
.category-bar { display: flex; gap: 6px; padding: 12px 16px 16px; overflow-x: auto; scrollbar-width: none; background: var(–bg); border-bottom: 1px solid var(–border); max-width: 760px; margin: 0 auto; width: 100%; }
.category-bar::-webkit-scrollbar { display: none; }
.cat-btn { padding: 10px 18px; background: transparent; border: 1px solid var(–border-bright); border-radius: 2px; color: var(–text-body); font-size: 13px; font-weight: 600; white-space: nowrap; cursor: pointer; min-height: 44px; text-transform: uppercase; letter-spacing: 0.08em; transition: all 0.15s; }
.cat-btn:hover { border-color: var(–accent); color: var(–accent); }
.cat-btn.active { background: var(–accent-solid); color: #fafaf7; border-color: var(–accent-dark); }

/* DRUG LIST */
.container { padding: 20px 16px 80px; max-width: 760px; margin: 0 auto; }
.drug-count { font-size: 13px; color: var(–text-dim); font-weight: 600; margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.12em; }
.drug-card { background: var(–bg-card); border: 1px solid var(–border); border-radius: 4px; margin-bottom: 14px; overflow: hidden; transition: all 0.2s; }
.drug-card.open { border-color: var(–accent); box-shadow: 0 4px 20px rgba(30,58,95,0.10); }
.drug-card.supplement { border-left: 4px solid var(–info); }
.drug-header { padding: 22px 22px; cursor: pointer; display: flex; align-items: flex-start; gap: 14px; min-height: 56px; }
.drug-main { flex: 1; min-width: 0; }
.drug-generic { font-family: var(–font-serif); font-size: var(–fs-xl); font-weight: 600; color: var(–text); margin-bottom: 4px; letter-spacing: -0.01em; line-height: 1.2; }
.drug-alt-name { font-size: var(–fs-sm); color: var(–text-dim); margin-bottom: 8px; font-weight: 400; font-style: italic; }
.drug-brand { font-size: 13px; color: var(–text-dim); font-weight: 500; text-transform: uppercase; letter-spacing: 0.08em; }
.drug-use-count { font-size: 13px; color: var(–accent); margin-top: 10px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; }
.supplement-badge { display: inline-block; font-size: 11px; padding: 3px 10px; background: var(–info-bg); color: var(–info); border: 1px solid var(–info); border-radius: 2px; font-weight: 700; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.1em; }
.chevron { color: var(–text-dim); font-size: 26px; transition: transform 0.2s; flex-shrink: 0; font-weight: 400; margin-top: 2px; }
.drug-card.open .chevron { transform: rotate(90deg); color: var(–accent); }

.drug-body { display: none; padding: 0 22px 22px; border-top: 1px solid var(–border); }
.drug-card.open .drug-body { display: block; }
.section { margin-top: 22px; }
.section-label { font-size: 12px; color: var(–accent); font-weight: 700; margin-bottom: 12px; display: flex; align-items: center; gap: 10px; letter-spacing: 0.14em; text-transform: uppercase; }
.section-label::before { content: ‘’; display: block; width: 24px; height: 1px; background: var(–accent); }
.section-label.warn-label { color: var(–warn); } .section-label.warn-label::before { background: var(–warn-border); }
.section-label.danger-label { color: var(–danger); } .section-label.danger-label::before { background: var(–danger-border); }

.use-item { background: var(–bg); border: 1px solid var(–border); border-left: 3px solid var(–accent); padding: 16px 18px; border-radius: 2px; margin-bottom: 8px; font-size: var(–fs-base); }
.use-title { font-weight: 600; color: var(–text); margin-bottom: 6px; font-size: var(–fs-base); line-height: 1.35; }
.use-detail { color: var(–text-body); font-size: var(–fs-sm); line-height: 1.6; font-weight: 400; }

.dose-table { background: var(–bg-elev); border: 1px solid var(–border); border-radius: 2px; padding: 16px 18px; font-size: var(–fs-base); }
.dose-row { display: flex; justify-content: space-between; gap: 14px; padding: 10px 0; border-bottom: 1px solid var(–border); }
.dose-row:last-child { border-bottom: none; }
.dose-label { color: var(–text-dim); font-size: 13px; font-weight: 600; flex-shrink: 0; text-transform: uppercase; letter-spacing: 0.06em; }
.dose-value { color: var(–text); font-weight: 600; text-align: right; font-size: var(–fs-base); }

.warn-box { background: var(–warn-bg); border: 1px solid var(–warn-border); border-left: 3px solid var(–warn-border); padding: 16px 18px; border-radius: 2px; font-size: var(–fs-base); color: var(–text); line-height: 1.6; font-weight: 400; }
.danger-box { background: var(–danger-bg); border: 1px solid var(–danger-border); border-left: 3px solid var(–danger-border); padding: 16px 18px; border-radius: 2px; font-size: var(–fs-base); color: var(–text); line-height: 1.6; font-weight: 400; }

.interact-list { list-style: none; }
.interact-list li { font-size: var(–fs-sm); padding: 10px 0 10px 20px; color: var(–text-body); position: relative; line-height: 1.55; border-bottom: 1px solid var(–border); font-weight: 400; }
.interact-list li:last-child { border-bottom: none; }
.interact-list li::before { content: ‘’; position: absolute; left: 0; top: 18px; width: 12px; height: 1px; background: var(–accent); }

.evidence-tier { display: inline-block; padding: 2px 8px; border-radius: 2px; font-size: 11px; font-weight: 700; margin-left: 8px; text-transform: uppercase; letter-spacing: 0.08em; vertical-align: middle; }
.evidence-strong { background: var(–safe-bg); color: var(–safe); border: 1px solid var(–safe); }
.evidence-emerging { background: var(–warn-bg); color: var(–warn); border: 1px solid var(–warn-border); }
.evidence-limited { background: var(–bg-elev); color: var(–text-dim); border: 1px solid var(–border-bright); }

.source-note { margin-top: 16px; padding-top: 14px; border-top: 1px solid var(–border); font-size: 12px; color: var(–text-dim); font-weight: 400; font-style: italic; }

.footer { padding: 32px 16px 40px; text-align: center; border-top: 1px solid var(–border); background: var(–bg-elev); margin-top: 20px; }
.footer-text { font-size: 13px; color: var(–text-dim); line-height: 1.8; font-weight: 400; }
.footer-text strong { color: var(–warn); font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; }

.no-results { padding: 60px 20px; text-align: center; color: var(–text-dim); font-size: var(–fs-lg); font-weight: 400; font-style: italic; }
</style>

</head>
<body>

<!-- DISCLAIMER GATE -->

<div class="gate" id="gate">
  <div class="gate-card">
    <div class="gate-title" data-en="Before You Begin" data-ko="시작 전 필독" data-ja="ご利用前にお読みください">Before You Begin</div>
    <div class="gate-subtitle">EDUCATIONAL REFERENCE · NOT MEDICAL ADVICE</div>
    <div class="gate-body">
      <p data-en="This app is an educational reference for over-the-counter (OTC) medications and common dietary supplements sold in U.S. pharmacies. For medications, it shows only FDA-approved uses from public FDA OTC Monographs, DailyMed (NIH), and MedlinePlus (NIH). For supplements, it shows common uses and evidence levels from the NIH Office of Dietary Supplements."
         data-ko="이 앱은 미국 약국에서 판매되는 일반의약품(OTC) 및 주요 식이 보충제에 대한 교육용 참고 자료입니다. 의약품은 FDA OTC 모노그래프, DailyMed(NIH), MedlinePlus(NIH)의 FDA 승인 용도만 표시합니다. 보충제는 NIH 식이보충제 사무국(ODS)의 일반적 용도 및 증거 수준을 표시합니다."
         data-ja="本アプリは米国の薬局で販売されている一般用医薬品(OTC)および主要なサプリメントに関する教育目的の参考資料です。医薬品はFDA OTCモノグラフ、DailyMed(NIH)、MedlinePlus(NIH)に基づくFDA承認の用途のみを表示します。サプリメントはNIHサプリメント事務局(ODS)の一般的用途とエビデンスレベルを表示します。"></p>
      <p data-en="<strong>Important — Supplements are NOT drugs.</strong> Dietary supplements in the U.S. are regulated as food under DSHEA 1994, not as medicine. The FDA does NOT review supplements for safety or effectiveness before they are sold. Product quality varies by brand. Look for USP-verified or NSF-certified products."
         data-ko="<strong>중요 — 보충제는 의약품이 아닙니다.</strong> 미국의 식이 보충제는 DSHEA 1994에 의해 의약품이 아닌 식품으로 규제됩니다. FDA는 판매 전 보충제의 안전성이나 효능을 심사하지 않습니다. 제품 품질이 브랜드마다 다르니 USP 또는 NSF 인증 제품을 찾으세요."
         data-ja="<strong>重要 — サプリメントは医薬品ではありません。</strong>米国のサプリメントはDSHEA 1994により医薬品ではなく食品として規制されています。FDAは販売前にサプリメントの安全性や有効性を審査しません。製品の品質はブランドにより異なるため、USPまたはNSF認証製品をお選びください。"></p>
      <p data-en="This app does NOT:" data-ko="이 앱은 다음을 하지 않습니다:" data-ja="本アプリは以下を行いません:"></p>
      <ul>
        <li data-en="Diagnose any medical condition" data-ko="질병을 진단하지 않습니다" data-ja="病気の診断は行いません"></li>
        <li data-en="Replace a doctor, pharmacist, or nurse" data-ko="의사, 약사, 간호사를 대체하지 않습니다" data-ja="医師·薬剤師·看護師の代わりにはなりません"></li>
        <li data-en="Recommend which medication or supplement you should take" data-ko="어떤 약이나 보충제를 복용해야 할지 추천하지 않습니다" data-ja="どの薬·サプリメントを服用すべきかは推奨しません"></li>
        <li data-en="Cover off-label or emergency substitute uses" data-ko="허가 외 사용이나 응급 대체 용도를 다루지 않습니다" data-ja="適応外使用や緊急代替使用は扱いません"></li>
      </ul>
      <p data-en="Always talk to a pharmacist before using any medication or supplement — pharmacists at CVS, Walgreens, Walmart, and most drugstores consult for free."
         data-ko="약이나 보충제를 복용하기 전에 반드시 약사와 상담하세요 — CVS, Walgreens, Walmart 등 대부분의 약국에서 약사 상담은 무료입니다."
         data-ja="医薬品·サプリメントを使用する前に必ず薬剤師にご相談ください — CVS、Walgreens、Walmartなど大半のドラッグストアで薬剤師相談は無料です。"></p>
    </div>
    <div class="gate-checks">
      <div class="check-row">
        <input type="checkbox" id="c1">
        <label for="c1" data-en="I understand this app is for education only and is not medical advice."
                        data-ko="이 앱이 교육 목적이며 의학적 조언이 아님을 이해합니다."
                        data-ja="本アプリは教育目的であり、医学的助言ではないことを理解しました。"></label>
      </div>
      <div class="check-row">
        <input type="checkbox" id="c2">
        <label for="c2" data-en="I will consult a pharmacist or doctor before taking any medication, especially if I have medical conditions, take other medications, am pregnant, breastfeeding, or giving medication to a child."
                        data-ko="약을 복용하기 전에 약사나 의사와 상담하겠습니다. 특히 기존 질환이 있거나, 다른 약을 복용 중이거나, 임신·수유 중이거나, 어린이에게 투여할 경우."
                        data-ja="薬を服用する前に薬剤師または医師に相談します。特に既往症がある場合、他の薬を服用中の場合、妊娠·授乳中の場合、または小児に投与する場合は必ず相談します。"></label>
      </div>
      <div class="check-row">
        <input type="checkbox" id="c3">
        <label for="c3" data-en="I will call 911 for emergencies and not rely on this app."
                        data-ko="응급 상황에서는 이 앱에 의존하지 않고 911에 전화하겠습니다."
                        data-ja="緊急時は本アプリに頼らず911(米国)·119(日本)·119(韓国)に通報します。"></label>
      </div>
    </div>
    <button class="gate-btn" id="gate-btn" disabled data-en="Continue" data-ko="계속하기" data-ja="続ける">Continue</button>
    <div class="gate-emergency">
      <strong data-en="EMERGENCY" data-ko="응급 상황" data-ja="緊急時">EMERGENCY</strong>
      <span data-en="Chest pain · trouble breathing · severe allergic reaction · stroke signs · uncontrolled bleeding · suicidal thoughts → Call 911"
            data-ko="가슴 통증 · 호흡 곤란 · 심한 알레르기 반응 · 뇌졸중 의심 · 멈추지 않는 출혈 · 자살 충동 → 911 전화"
            data-ja="胸の痛み · 呼吸困難 · 重度のアレルギー反応 · 脳卒中の兆候 · 止まらない出血 · 自殺念慮 → 911に通報"></span>
      <br><br>
      <span data-en="Poison: 1-800-222-1222 · Mental health: 988"
            data-ko="독극물 센터: 1-800-222-1222 · 정신건강 위기: 988"
            data-ja="中毒情報: 1-800-222-1222 · メンタルヘルス危機: 988"></span>
    </div>
  </div>
</div>

<!-- HEADER -->

<div class="header">
  <div class="logo">Home<span class="logo-dot">·</span>Rx</div>
  <div class="header-spacer"></div>
  <div class="header-controls">
    <div class="text-size-toggle" title="Text size">
      <button class="ts-btn active" data-size="normal" aria-label="Normal text">A</button>
      <button class="ts-btn" data-size="large" aria-label="Large text" style="font-size:17px">A</button>
      <button class="ts-btn" data-size="xlarge" aria-label="Extra large text" style="font-size:20px">A</button>
    </div>
    <div class="lang-toggle">
      <button class="lang-btn active" data-lang="en">EN</button>
      <button class="lang-btn" data-lang="ko">한</button>
      <button class="lang-btn" data-lang="ja">日</button>
    </div>
  </div>
</div>

<div class="emergency-strip">
  <span data-en="EMERGENCY: CALL 911 · POISON: 1-800-222-1222 · MENTAL HEALTH: 988"
        data-ko="응급: 911 · 독극물: 1-800-222-1222 · 정신건강: 988"
        data-ja="緊急: 911 · 中毒: 1-800-222-1222 · メンタルヘルス: 988"></span>
</div>

<div class="search-bar">
  <input type="search" class="search-input" id="search"
         autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false"
         placeholder="Search by drug or brand (e.g., Tylenol, ibuprofen)…"
         data-ph-en="Search by drug or brand (e.g., Tylenol, ibuprofen)…"
         data-ph-ko="약 이름이나 브랜드로 검색 (예: 타이레놀, 이부프로펜)…"
         data-ph-ja="薬名·ブランド名で検索 (例: タイレノール、イブプロフェン)…">
</div>

<div class="category-bar" id="categories"></div>

<div class="container">
  <div class="drug-count" id="drug-count"></div>
  <div id="drug-list"></div>
  <div id="no-results" class="no-results" style="display:none;"
       data-en="No medications match your search." data-ko="검색 결과가 없습니다." data-ja="検索結果がありません。"></div>
</div>

<div class="footer">
  <div class="footer-text">
    <strong data-en="EDUCATIONAL REFERENCE ONLY · NOT MEDICAL ADVICE" data-ko="교육용 참고 자료일 뿐 · 의학적 조언 아님" data-ja="教育目的の参考資料のみ · 医学的助言ではありません"></strong><br>
    <span data-en="Sources: FDA OTC Monograph · DailyMed (NIH) · MedlinePlus (NIH)"
          data-ko="출처: FDA OTC 모노그래프 · DailyMed(NIH) · MedlinePlus(NIH)"
          data-ja="出典: FDA OTCモノグラフ · DailyMed(NIH) · MedlinePlus(NIH)"></span><br>
    <span>© 2026 Jae H. Choi, PhD, DVSc · HAKOYA LLC</span><br>
    <span data-en="Always consult a pharmacist before use." data-ko="복용 전 반드시 약사와 상담하세요." data-ja="使用前に必ず薬剤師にご相談ください。"></span>
  </div>
</div>

<script>
// ============================================================
//  HomeRx Drug Database — Data inserted in next step
//  Each entry: id, generic{en,ko}, brands[], category, uses[],
//  dose_en{}, dose_ko{}, danger_en, danger_ko, warn_en, warn_ko,
//  interact[{en,ko}], source
// ============================================================
const DRUGS = [
  // ============ PAIN & FEVER ============
  {
    id: 'acetaminophen',
    generic: { en: 'Acetaminophen', ko: '아세트아미노펜', ja: 'アセトアミノフェン' },
    brands: ['Tylenol', 'Panadol', 'Mapap'],
    category: 'pain',
    uses: [
      { title_en: 'Pain relief (mild to moderate)', title_ko: '경도~중등도 통증 완화', title_ja: '軽度~中等度の痛みの緩和',
        detail_en: 'Headache, muscle aches, backache, toothache, menstrual cramps, minor arthritis pain',
        detail_ko: '두통, 근육통, 허리 통증, 치통, 생리통, 경미한 관절염 통증',
        detail_ja: '頭痛、筋肉痛、腰痛、歯痛、生理痛、軽度の関節炎の痛み' },
      { title_en: 'Fever reduction', title_ko: '해열', title_ja: '解熱',
        detail_en: 'Reduces fever in adults and children',
        detail_ko: '성인 및 어린이의 발열을 낮춤',
        detail_ja: '成人および小児の発熱を下げる' }
    ],
    dose_en: { 'Adult': '325–1000 mg every 4–6 hours', 'Max per day': '3000 mg (4000 mg only under doctor supervision)', 'Child': 'Weight-based — ask pharmacist' },
    dose_ko: { '성인': '325~1000 mg, 4~6시간마다', '하루 최대': '3000 mg (4000 mg은 의사 감독 하에만)', '어린이': '체중 기반 — 약사에게 문의' },
    dose_ja: { '成人': '4~6時間ごとに325~1000 mg', '1日最大量': '3000 mg(4000 mgは医師の監督下のみ)', '小児': '体重ベース — 薬剤師に相談' },
    danger_en: 'LIVER DAMAGE RISK. Exceeding the maximum dose — or combining with alcohol — can cause fatal liver failure. Many cold and flu medicines already contain acetaminophen, so always read all labels before combining products.',
    danger_ko: '간 손상 위험. 최대 용량을 초과하거나 알코올과 병용하면 치명적인 간부전을 일으킬 수 있습니다. 감기·독감약에 이미 아세트아미노펜이 들어 있는 경우가 많으므로 여러 제품을 함께 복용하기 전에 모든 라벨을 확인하세요.',
    danger_ja: '肝障害のリスクがあります。最大用量を超えたり、アルコールと併用すると致命的な肝不全を起こすことがあります。多くの風邪薬·インフルエンザ薬にはすでにアセトアミノフェンが含まれているため、複数の製品を併用する前に必ずすべてのラベルを確認してください。',
    warn_en: 'Avoid if you drink 3 or more alcoholic drinks daily. Ask a doctor before use if you have liver disease.',
    warn_ko: '하루 3잔 이상 음주하는 경우 사용하지 마세요. 간 질환이 있으면 사용 전 의사와 상담하세요.',
    warn_ja: '1日に3杯以上飲酒する場合は使用しないでください。肝疾患がある場合は使用前に医師に相談してください。',
    interact: [
      { en: 'Alcohol — significantly increases liver damage risk', ko: '알코올 — 간 손상 위험 크게 증가', ja: 'アルコール — 肝障害リスクを大幅に増加' },
      { en: 'Warfarin — may increase bleeding risk with prolonged use', ko: '와파린 — 장기 사용 시 출혈 위험 증가', ja: 'ワーファリン — 長期使用で出血リスク増加' },
      { en: 'Other acetaminophen-containing products (cold/flu combinations)', ko: '아세트아미노펜을 함유한 다른 제품 (감기·독감 복합제)', ja: 'アセトアミノフェン含有の他の製品(風邪·インフルエンザ複合薬)' }
    ],
    source: 'FDA OTC Monograph 21 CFR 343 · DailyMed (NIH)'
  },
  {
    id: 'ibuprofen',
    generic: { en: 'Ibuprofen', ko: '이부프로펜', ja: 'イブプロフェン' },
    brands: ['Advil', 'Motrin'],
    category: 'pain',
    uses: [
      { title_en: 'Pain relief', title_ko: '통증 완화', title_ja: '痛みの緩和',
        detail_en: 'Headache, muscle aches, backache, toothache, menstrual cramps, minor arthritis pain',
        detail_ko: '두통, 근육통, 허리 통증, 치통, 생리통, 경미한 관절염 통증',
        detail_ja: '頭痛、筋肉痛、腰痛、歯痛、生理痛、軽度の関節炎の痛み' },
      { title_en: 'Fever reduction', title_ko: '해열', title_ja: '解熱',
        detail_en: 'Reduces fever in adults and children',
        detail_ko: '성인 및 어린이의 발열을 낮춤',
        detail_ja: '成人および小児の発熱を下げる' },
      { title_en: 'Anti-inflammatory', title_ko: '소염 작용', title_ja: '抗炎症作用',
        detail_en: 'Reduces inflammation and swelling from minor injuries or arthritis',
        detail_ko: '경미한 부상이나 관절염으로 인한 염증과 붓기 감소',
        detail_ja: '軽度の外傷や関節炎による炎症·腫れを軽減' }
    ],
    dose_en: { 'Adult': '200–400 mg every 4–6 hours', 'Max per day (OTC)': '1200 mg', 'Take with': 'Food or milk to reduce stomach upset' },
    dose_ko: { '성인': '200~400 mg, 4~6시간마다', '하루 최대 (OTC)': '1200 mg', '복용 방법': '위장 장애를 줄이려면 음식이나 우유와 함께' },
    dose_ja: { '成人': '4~6時間ごとに200~400 mg', '1日最大量(OTC)': '1200 mg', '服用方法': '胃腸障害を軽減するため食事または牛乳と一緒に' },
    danger_en: 'HEART ATTACK AND STROKE RISK increases with long-term use or in people with heart disease. Can cause serious stomach bleeding — risk is higher if you are age 60 or older, have a history of ulcers, take blood thinners or steroids, or drink 3 or more alcoholic drinks daily.',
    danger_ko: '심장마비 및 뇌졸중 위험이 장기 복용 또는 심장병 환자에서 증가합니다. 심각한 위장 출혈을 일으킬 수 있으며, 60세 이상, 궤양 병력, 혈액 희석제나 스테로이드 복용, 하루 3잔 이상 음주하는 경우 위험이 더 높습니다.',
    danger_ja: '心筋梗塞および脳卒中のリスクが長期使用または心疾患患者で増加します。重大な胃腸出血を起こすことがあり、60歳以上、潰瘍の既往歴、抗凝固薬·ステロイド使用中、または1日3杯以上飲酒する場合にリスクが高くなります。',
    warn_en: 'Do not use in the last 3 months of pregnancy. Avoid if you have kidney disease, heart failure, or a history of stomach ulcers.',
    warn_ko: '임신 마지막 3개월에는 사용하지 마세요. 신장 질환, 심부전, 위궤양 병력이 있으면 사용하지 마세요.',
    warn_ja: '妊娠後期(最後の3か月)には使用しないでください。腎疾患、心不全、胃潰瘍の既往歴がある場合は使用しないでください。',
    interact: [
      { en: 'Aspirin — reduces aspirin\'s heart-protective effect', ko: '아스피린 — 아스피린의 심장 보호 효과 감소', ja: 'アスピリン — アスピリンの心保護効果を減少' },
      { en: 'Blood thinners (warfarin, apixaban, rivaroxaban) — bleeding risk', ko: '혈액 희석제 (와파린, 엘리퀴스, 자렐토) — 출혈 위험', ja: '抗凝固薬(ワーファリン、エリキュース、イグザレルト) — 出血リスク' },
      { en: 'Blood pressure medications — may reduce effectiveness', ko: '혈압약 — 효과 감소 가능', ja: '降圧薬 — 効果減少の可能性' },
      { en: 'Lithium and methotrexate — increased toxicity', ko: '리튬, 메토트렉세이트 — 독성 증가', ja: 'リチウム、メトトレキサート — 毒性増加' }
    ],
    source: 'FDA OTC Monograph 21 CFR 343 · DailyMed (NIH)'
  },
  {
    id: 'naproxen',
    generic: { en: 'Naproxen sodium', ko: '나프록센 나트륨', ja: 'ナプロキセンナトリウム' },
    brands: ['Aleve'],
    category: 'pain',
    uses: [
      { title_en: 'Pain relief (longer-lasting)', title_ko: '통증 완화 (장시간 지속)', title_ja: '痛みの緩和(長時間持続)',
        detail_en: 'Headache, muscle aches, backache, toothache, menstrual cramps, minor arthritis pain; single dose lasts up to 12 hours',
        detail_ko: '두통, 근육통, 허리 통증, 치통, 생리통, 경미한 관절염 통증; 1회 복용으로 최대 12시간 지속',
        detail_ja: '頭痛、筋肉痛、腰痛、歯痛、生理痛、軽度の関節炎の痛み;1回の服用で最大12時間持続' },
      { title_en: 'Fever reduction', title_ko: '해열', title_ja: '解熱',
        detail_en: 'Reduces fever',
        detail_ko: '발열을 낮춤',
        detail_ja: '発熱を下げる' },
      { title_en: 'Anti-inflammatory', title_ko: '소염 작용', title_ja: '抗炎症作用',
        detail_en: 'Reduces inflammation and swelling',
        detail_ko: '염증과 붓기를 감소',
        detail_ja: '炎症と腫れを軽減' }
    ],
    dose_en: { 'Adult': '220 mg every 8–12 hours', 'First dose': 'May take 440 mg within first hour', 'Max per day (OTC)': '660 mg', 'Take with': 'Food or milk' },
    dose_ko: { '성인': '220 mg, 8~12시간마다', '첫 용량': '첫 1시간 내에 440 mg까지 복용 가능', '하루 최대 (OTC)': '660 mg', '복용 방법': '음식이나 우유와 함께' },
    dose_ja: { '成人': '8~12時間ごとに220 mg', '初回用量': '最初の1時間以内に440 mgまで服用可能', '1日最大量(OTC)': '660 mg', '服用方法': '食事または牛乳と一緒に' },
    danger_en: 'Same risks as ibuprofen — HEART ATTACK, STROKE, and SERIOUS STOMACH BLEEDING. Because naproxen lasts longer in the body, these risks may accumulate. Do not exceed the labeled dose.',
    danger_ko: '이부프로펜과 동일한 위험 — 심장마비, 뇌졸중, 심각한 위장 출혈. 나프록센은 체내에 더 오래 머무르므로 이 위험이 누적될 수 있습니다. 라벨에 표시된 용량을 초과하지 마세요.',
    danger_ja: 'イブプロフェンと同じリスク — 心筋梗塞、脳卒中、重大な胃腸出血。ナプロキセンは体内により長く留まるため、これらのリスクが蓄積する可能性があります。ラベル表示の用量を超えないでください。',
    warn_en: 'Do not use in the last 3 months of pregnancy. Avoid if you have kidney disease, heart failure, or ulcer history. Do not combine with ibuprofen or aspirin without doctor approval.',
    warn_ko: '임신 마지막 3개월에는 사용하지 마세요. 신장 질환, 심부전, 궤양 병력이 있으면 사용하지 마세요. 의사 승인 없이 이부프로펜이나 아스피린과 병용하지 마세요.',
    warn_ja: '妊娠後期(最後の3か月)には使用しないでください。腎疾患、心不全、潰瘍の既往歴がある場合は使用しないでください。医師の承認なしにイブプロフェンやアスピリンと併用しないでください。',
    interact: [
      { en: 'Aspirin — reduces aspirin\'s heart-protective effect', ko: '아스피린 — 아스피린의 심장 보호 효과 감소', ja: 'アスピリン — アスピリンの心保護効果を減少' },
      { en: 'Blood thinners — bleeding risk', ko: '혈액 희석제 — 출혈 위험', ja: '抗凝固薬 — 出血リスク' },
      { en: 'Blood pressure medications — reduced effectiveness', ko: '혈압약 — 효과 감소', ja: '降圧薬 — 効果減少' },
      { en: 'SSRI antidepressants — increased bleeding risk', ko: 'SSRI 항우울제 — 출혈 위험 증가', ja: 'SSRI抗うつ薬 — 出血リスク増加' }
    ],
    source: 'FDA OTC Monograph 21 CFR 343 · DailyMed (NIH)'
  },
  {
    id: 'aspirin',
    generic: { en: 'Aspirin (acetylsalicylic acid)', ko: '아스피린 (아세틸살리실산)', ja: 'アスピリン(アセチルサリチル酸)' },
    brands: ['Bayer', 'Bufferin', 'Ecotrin'],
    category: 'pain',
    uses: [
      { title_en: 'Pain relief', title_ko: '통증 완화', title_ja: '痛みの緩和',
        detail_en: 'Headache, muscle aches, toothache, menstrual cramps, minor arthritis pain',
        detail_ko: '두통, 근육통, 치통, 생리통, 경미한 관절염 통증',
        detail_ja: '頭痛、筋肉痛、歯痛、生理痛、軽度の関節炎の痛み' },
      { title_en: 'Fever reduction', title_ko: '해열', title_ja: '解熱',
        detail_en: 'Reduces fever in adults (NOT for children or teens with viral illness)',
        detail_ko: '성인의 발열을 낮춤 (바이러스성 질환이 있는 어린이·청소년에게는 사용 금지)',
        detail_ja: '成人の発熱を下げる(ウイルス性疾患のある小児·青少年には使用禁止)' },
      { title_en: 'Anti-inflammatory', title_ko: '소염 작용', title_ja: '抗炎症作用',
        detail_en: 'Reduces inflammation',
        detail_ko: '염증 감소',
        detail_ja: '炎症を軽減' },
      { title_en: 'Heart attack and stroke prevention (low-dose, 81 mg)', title_ko: '심장마비·뇌졸중 예방 (저용량, 81 mg)', title_ja: '心筋梗塞·脳卒中予防(低用量、81 mg)',
        detail_en: 'Only when specifically prescribed by your doctor — do not start on your own',
        detail_ko: '의사가 처방한 경우에만 — 스스로 시작하지 마세요',
        detail_ja: '医師の処方がある場合のみ — 自己判断で開始しないでください' }
    ],
    dose_en: { 'Adult (pain/fever)': '325–650 mg every 4 hours', 'Low-dose (preventive)': '81 mg daily — ONLY if doctor-directed', 'Max per day (OTC pain)': '4000 mg', 'Take with': 'Food or water' },
    dose_ko: { '성인 (통증·발열)': '325~650 mg, 4시간마다', '저용량 (예방)': '하루 81 mg — 의사 지시가 있을 때만', '하루 최대 (OTC 통증)': '4000 mg', '복용 방법': '음식이나 물과 함께' },
    dose_ja: { '成人(痛み·発熱)': '4時間ごとに325~650 mg', '低用量(予防)': '1日81 mg — 医師の指示がある場合のみ', '1日最大量(OTC 痛み)': '4000 mg', '服用方法': '食事または水と一緒に' },
    danger_en: 'REYE\'S SYNDROME — Do NOT give to children or teenagers with flu, chickenpox, or any viral illness. Can cause fatal brain and liver damage. Also causes stomach bleeding and increases bleeding from any source.',
    danger_ko: '라이 증후군 — 독감, 수두, 또는 바이러스성 질환이 있는 어린이·청소년에게 절대 투여하지 마세요. 치명적인 뇌·간 손상을 일으킬 수 있습니다. 또한 위장 출혈 및 모든 부위의 출혈을 증가시킵니다.',
    danger_ja: 'ライ症候群 — インフルエンザ、水痘、その他のウイルス性疾患のある小児·青少年には絶対に投与しないでください。致命的な脳·肝障害を起こすことがあります。また胃腸出血およびあらゆる部位の出血を増加させます。',
    warn_en: 'Stop 7–10 days before any surgery (talk to your surgeon first). Avoid if you have bleeding disorders, ulcers, or aspirin allergy. Do not use in last 3 months of pregnancy.',
    warn_ko: '수술 7~10일 전에 중단하세요 (먼저 외과의와 상담). 출혈 장애, 궤양, 아스피린 알레르기가 있으면 사용하지 마세요. 임신 마지막 3개월에는 사용하지 마세요.',
    warn_ja: '手術の7~10日前に中止してください(まず外科医に相談)。出血性疾患、潰瘍、アスピリンアレルギーがある場合は使用しないでください。妊娠後期(最後の3か月)には使用しないでください。',
    interact: [
      { en: 'Ibuprofen — reduces aspirin\'s heart-protective effect', ko: '이부프로펜 — 아스피린의 심장 보호 효과 감소', ja: 'イブプロフェン — アスピリンの心保護効果を減少' },
      { en: 'Blood thinners (warfarin, apixaban) — major bleeding risk', ko: '혈액 희석제 (와파린, 엘리퀴스) — 심각한 출혈 위험', ja: '抗凝固薬(ワーファリン、エリキュース) — 重大な出血リスク' },
      { en: 'Other NSAIDs — stomach bleeding risk', ko: '다른 NSAID — 위장 출혈 위험', ja: '他のNSAID — 胃腸出血リスク' },
      { en: 'Methotrexate — increased toxicity', ko: '메토트렉세이트 — 독성 증가', ja: 'メトトレキサート — 毒性増加' }
    ],
    source: 'FDA OTC Monograph 21 CFR 343 · DailyMed (NIH)'
  },

  // ============ ALLERGY & COLD ============
  {
    id: 'diphenhydramine',
    generic: { en: 'Diphenhydramine', ko: '디펜히드라민', ja: 'ジフェンヒドラミン' },
    brands: ['Benadryl', 'ZzzQuil', 'Unisom SleepGels'],
    category: 'allergy',
    uses: [
      { title_en: 'Allergy symptom relief', title_ko: '알레르기 증상 완화', title_ja: 'アレルギー症状の緩和',
        detail_en: 'Runny nose, sneezing, itchy/watery eyes, itchy throat, hives, itchy rash',
        detail_ko: '콧물, 재채기, 눈 가려움·눈물, 목 간지러움, 두드러기, 가려운 발진',
        detail_ja: '鼻水、くしゃみ、目のかゆみ·涙目、のどのかゆみ、じんま疹、かゆみのある発疹' },
      { title_en: 'Nighttime sleep aid', title_ko: '야간 수면 보조', title_ja: '夜間の睡眠補助',
        detail_en: 'For occasional sleeplessness — not for long-term use',
        detail_ko: '일시적 불면에 사용 — 장기 사용 금지',
        detail_ja: '一時的な不眠に使用 — 長期使用は禁止' },
      { title_en: 'Motion sickness prevention', title_ko: '멀미 예방', title_ja: '乗り物酔い予防',
        detail_en: 'Nausea, vomiting, and dizziness from motion',
        detail_ko: '움직임으로 인한 메스꺼움, 구토, 어지러움',
        detail_ja: '動きによる吐き気、嘔吐、めまい' },
      { title_en: 'Cold symptom relief', title_ko: '감기 증상 완화', title_ja: '風邪症状の緩和',
        detail_en: 'Runny nose and sneezing from the common cold',
        detail_ko: '감기로 인한 콧물과 재채기',
        detail_ja: '風邪による鼻水とくしゃみ' }
    ],
    dose_en: { 'Adult': '25–50 mg every 4–6 hours', 'Max per day': '300 mg', 'Sleep aid': '50 mg at bedtime', 'Child': 'Ask pharmacist — do not give under age 6 without doctor' },
    dose_ko: { '성인': '25~50 mg, 4~6시간마다', '하루 최대': '300 mg', '수면 보조': '취침 시 50 mg', '어린이': '약사에게 문의 — 6세 미만은 의사 지시 없이 투여 금지' },
    dose_ja: { '成人': '4~6時間ごとに25~50 mg', '1日最大量': '300 mg', '睡眠補助': '就寝時に50 mg', '小児': '薬剤師に相談 — 6歳未満は医師の指示なく投与禁止' },
    danger_en: 'CAUSES MARKED DROWSINESS — do not drive or operate machinery. In older adults, can cause confusion, falls, and urinary retention. Long-term use is linked to increased risk of dementia in the elderly.',
    danger_ko: '심한 졸음을 유발합니다 — 운전이나 기계 조작 금지. 고령자에서 혼돈, 낙상, 소변 저류를 일으킬 수 있습니다. 장기 사용은 고령자의 치매 위험 증가와 관련이 있습니다.',
    danger_ja: '強い眠気を引き起こします — 運転や機械操作を禁止。高齢者では混乱、転倒、尿閉を起こすことがあります。長期使用は高齢者の認知症リスク増加と関連しています。',
    warn_en: 'Avoid if you have glaucoma, enlarged prostate, or breathing problems like asthma or COPD. Alcohol intensifies drowsiness. Not recommended for children under 6 or during pregnancy without doctor approval.',
    warn_ko: '녹내장, 전립선 비대, 천식·COPD 같은 호흡 문제가 있으면 사용하지 마세요. 알코올은 졸음을 심화시킵니다. 6세 미만 어린이나 임신 중에는 의사 승인 없이 사용하지 마세요.',
    warn_ja: '緑内障、前立腺肥大、喘息·COPDなどの呼吸器疾患がある場合は使用しないでください。アルコールは眠気を強めます。6歳未満の小児や妊娠中は医師の承認なく使用しないでください。',
    interact: [
      { en: 'Alcohol — increased drowsiness and impaired coordination', ko: '알코올 — 졸음 및 운동 조절 장애 심화', ja: 'アルコール — 眠気増強と協調運動障害' },
      { en: 'Sleep medications, sedatives — dangerous additive sedation', ko: '수면제, 진정제 — 위험한 진정 효과 누적', ja: '睡眠薬、鎮静薬 — 危険な鎮静作用の累積' },
      { en: 'MAO inhibitors — serious interaction', ko: 'MAO 억제제 — 심각한 상호작용', ja: 'MAO阻害薬 — 重大な相互作用' },
      { en: 'Other products containing diphenhydramine (many cold/sleep combos)', ko: '디펜히드라민을 함유한 다른 제품 (감기·수면 복합제 다수)', ja: 'ジフェンヒドラミン含有の他製品(風邪·睡眠複合薬多数)' }
    ],
    source: 'FDA OTC Monograph 21 CFR 341 · DailyMed (NIH)'
  },
  {
    id: 'loratadine',
    generic: { en: 'Loratadine', ko: '로라타딘', ja: 'ロラタジン' },
    brands: ['Claritin', 'Alavert'],
    category: 'allergy',
    uses: [
      { title_en: 'Allergy symptom relief (non-drowsy)', title_ko: '알레르기 증상 완화 (졸음 없음)', title_ja: 'アレルギー症状の緩和(眠くなりにくい)',
        detail_en: 'Runny nose, sneezing, itchy/watery eyes, itchy throat or nose from hay fever and other upper respiratory allergies',
        detail_ko: '꽃가루 알레르기 및 기타 상기도 알레르기로 인한 콧물, 재채기, 눈 가려움·눈물, 목·코 가려움',
        detail_ja: '花粉症およびその他の上気道アレルギーによる鼻水、くしゃみ、目のかゆみ·涙目、のど·鼻のかゆみ' },
      { title_en: 'Hives (urticaria)', title_ko: '두드러기', title_ja: 'じんま疹',
        detail_en: 'Relief of itching from hives',
        detail_ko: '두드러기로 인한 가려움 완화',
        detail_ja: 'じんま疹によるかゆみの緩和' }
    ],
    dose_en: { 'Adult and child 6+': '10 mg once daily', 'Child 2–5': '5 mg once daily (syrup or chewable)', 'Duration': 'Safe for daily seasonal use' },
    dose_ko: { '성인 및 6세 이상': '하루 1회 10 mg', '2~5세 어린이': '하루 1회 5 mg (시럽 또는 츄어블)', '사용 기간': '계절성 알레르기에 매일 사용 안전' },
    dose_ja: { '成人および6歳以上': '1日1回10 mg', '2~5歳': '1日1回5 mg(シロップまたはチュアブル)', '使用期間': '季節性アレルギーに毎日使用可能' },
    warn_en: 'Ask a doctor before use if you have liver or kidney disease — you may need a lower dose. Generally well tolerated. Does not typically cause drowsiness, but a small percentage of people do feel drowsy.',
    warn_ko: '간·신장 질환이 있으면 사용 전 의사와 상담하세요 — 용량 감량이 필요할 수 있습니다. 일반적으로 내약성이 좋습니다. 보통 졸음을 일으키지 않지만 소수에서 졸음을 느낄 수 있습니다.',
    warn_ja: '肝·腎疾患がある場合は使用前に医師に相談してください — 減量が必要な場合があります。一般的に忍容性は良好です。通常は眠気を起こしませんが、少数で眠気を感じる人がいます。',
    interact: [
      { en: 'Generally few significant interactions — one of the safest antihistamines', ko: '유의미한 상호작용이 거의 없음 — 가장 안전한 항히스타민 중 하나', ja: '有意な相互作用はほとんどなし — 最も安全な抗ヒスタミン薬の一つ' },
      { en: 'Ketoconazole, erythromycin — may increase loratadine levels', ko: '케토코나졸, 에리트로마이신 — 로라타딘 농도 상승 가능', ja: 'ケトコナゾール、エリスロマイシン — ロラタジン濃度上昇の可能性' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'cetirizine',
    generic: { en: 'Cetirizine', ko: '세티리진', ja: 'セチリジン' },
    brands: ['Zyrtec'],
    category: 'allergy',
    uses: [
      { title_en: 'Allergy symptom relief', title_ko: '알레르기 증상 완화', title_ja: 'アレルギー症状の緩和',
        detail_en: 'Runny nose, sneezing, itchy/watery eyes, itchy throat or nose from hay fever and other upper respiratory allergies',
        detail_ko: '꽃가루 알레르기 및 기타 상기도 알레르기로 인한 콧물, 재채기, 눈 가려움·눈물, 목·코 가려움',
        detail_ja: '花粉症およびその他の上気道アレルギーによる鼻水、くしゃみ、目のかゆみ·涙目、のど·鼻のかゆみ' },
      { title_en: 'Hives (urticaria)', title_ko: '두드러기', title_ja: 'じんま疹',
        detail_en: 'Relief of itching from hives',
        detail_ko: '두드러기로 인한 가려움 완화',
        detail_ja: 'じんま疹によるかゆみの緩和' }
    ],
    dose_en: { 'Adult and child 6+': '5–10 mg once daily', 'Child 2–5': '2.5 mg once or twice daily (syrup)', 'Max per day (child 2–5)': '5 mg' },
    dose_ko: { '성인 및 6세 이상': '하루 1회 5~10 mg', '2~5세 어린이': '하루 1~2회 2.5 mg (시럽)', '하루 최대 (2~5세)': '5 mg' },
    dose_ja: { '成人および6歳以上': '1日1回5~10 mg', '2~5歳': '1日1~2回2.5 mg(シロップ)', '1日最大量(2~5歳)': '5 mg' },
    warn_en: 'May cause mild drowsiness in some people — use caution when driving until you know how it affects you. Reduce dose if you have kidney or liver disease. Stopping after long-term use can cause a rebound itch.',
    warn_ko: '일부에서 경미한 졸음을 유발할 수 있으므로 반응을 확인할 때까지 운전 시 주의하세요. 신장·간 질환이 있으면 용량을 감량하세요. 장기 사용 후 중단 시 반동 가려움이 나타날 수 있습니다.',
    warn_ja: '一部の人で軽度の眠気を起こすことがあるため、影響を確認するまで運転には注意してください。腎·肝疾患がある場合は減量してください。長期使用後の中止でリバウンドかゆみが現れることがあります。',
    interact: [
      { en: 'Alcohol and other sedating drugs — added drowsiness', ko: '알코올 및 기타 진정 약물 — 졸음 누적', ja: 'アルコールおよびその他の鎮静薬 — 眠気の累積' },
      { en: 'Theophylline — may increase cetirizine levels', ko: '테오필린 — 세티리진 농도 상승 가능', ja: 'テオフィリン — セチリジン濃度上昇の可能性' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'fexofenadine',
    generic: { en: 'Fexofenadine', ko: '펙소페나딘', ja: 'フェキソフェナジン' },
    brands: ['Allegra'],
    category: 'allergy',
    uses: [
      { title_en: 'Allergy symptom relief (non-drowsy)', title_ko: '알레르기 증상 완화 (졸음 없음)', title_ja: 'アレルギー症状の緩和(眠くなりにくい)',
        detail_en: 'Runny nose, sneezing, itchy/watery eyes, itchy throat or nose from seasonal allergies',
        detail_ko: '계절성 알레르기로 인한 콧물, 재채기, 눈 가려움·눈물, 목·코 가려움',
        detail_ja: '季節性アレルギーによる鼻水、くしゃみ、目のかゆみ·涙目、のど·鼻のかゆみ' },
      { title_en: 'Hives (urticaria)', title_ko: '두드러기', title_ja: 'じんま疹',
        detail_en: 'Relief of itching from chronic hives',
        detail_ko: '만성 두드러기로 인한 가려움 완화',
        detail_ja: '慢性じんま疹によるかゆみの緩和' }
    ],
    dose_en: { 'Adult and child 12+': '60 mg twice daily OR 180 mg once daily', 'Child 6–11': '30 mg twice daily', 'Child 2–5': '30 mg twice daily (suspension)', 'Take with': 'Water only — avoid fruit juice within 4 hours' },
    dose_ko: { '성인 및 12세 이상': '60 mg 하루 2회 또는 180 mg 하루 1회', '6~11세': '30 mg 하루 2회', '2~5세': '30 mg 하루 2회 (현탁액)', '복용 방법': '물로만 — 과일 주스는 4시간 이내 피하기' },
    dose_ja: { '成人および12歳以上': '60 mg 1日2回または180 mg 1日1回', '6~11歳': '30 mg 1日2回', '2~5歳': '30 mg 1日2回(懸濁液)', '服用方法': '水のみで服用 — 果汁は4時間以内回避' },
    warn_en: 'Fruit juices (orange, grapefruit, apple) can reduce absorption by up to 40% — take with water only and separate from juice by 4 hours. Reduce dose if you have kidney disease.',
    warn_ko: '과일 주스(오렌지, 자몽, 사과)는 흡수를 최대 40%까지 감소시킬 수 있습니다 — 반드시 물로만 복용하고 주스와 4시간 간격을 두세요. 신장 질환이 있으면 용량을 감량하세요.',
    warn_ja: '果汁(オレンジ、グレープフルーツ、リンゴ)は吸収を最大40%減少させる可能性があります — 必ず水のみで服用し、果汁とは4時間間隔を開けてください。腎疾患がある場合は減量してください。',
    interact: [
      { en: 'Fruit juices — reduce drug absorption', ko: '과일 주스 — 약물 흡수 감소', ja: '果汁 — 薬物吸収減少' },
      { en: 'Antacids containing aluminum or magnesium — reduce absorption (separate by 2 hours)', ko: '알루미늄·마그네슘 함유 제산제 — 흡수 감소 (2시간 간격 필요)', ja: 'アルミニウム·マグネシウム含有制酸薬 — 吸収減少(2時間間隔が必要)' },
      { en: 'Erythromycin, ketoconazole — may increase fexofenadine levels', ko: '에리트로마이신, 케토코나졸 — 펙소페나딘 농도 상승 가능', ja: 'エリスロマイシン、ケトコナゾール — フェキソフェナジン濃度上昇の可能性' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'pseudoephedrine',
    generic: { en: 'Pseudoephedrine', ko: '슈도에페드린', ja: 'プソイドエフェドリン' },
    brands: ['Sudafed (behind-the-counter)'],
    category: 'allergy',
    uses: [
      { title_en: 'Nasal congestion relief', title_ko: '코막힘 완화', title_ja: '鼻づまりの緩和',
        detail_en: 'Stuffy nose from colds, allergies, hay fever, or sinus problems',
        detail_ko: '감기, 알레르기, 꽃가루 알레르기, 부비동 문제로 인한 코막힘',
        detail_ja: '風邪、アレルギー、花粉症、副鼻腔の問題による鼻づまり' },
      { title_en: 'Sinus and ear pressure relief', title_ko: '부비동·귀 압력 완화', title_ja: '副鼻腔·耳の圧力緩和',
        detail_en: 'Reduces pressure associated with congestion',
        detail_ko: '코막힘과 관련된 압력 감소',
        detail_ja: '鼻づまりに関連する圧力を軽減' }
    ],
    dose_en: { 'Adult': '30–60 mg every 4–6 hours', 'Extended release': '120 mg every 12 hours', 'Max per day': '240 mg', 'Purchase': 'Behind the counter — ID required (US federal law)' },
    dose_ko: { '성인': '30~60 mg, 4~6시간마다', '서방형': '120 mg, 12시간마다', '하루 최대': '240 mg', '구매': '카운터 뒤 판매 — 신분증 필요 (미국 연방법)' },
    dose_ja: { '成人': '4~6時間ごとに30~60 mg', '徐放性': '12時間ごとに120 mg', '1日最大量': '240 mg', '購入': 'カウンター裏販売 — 身分証明書必要(米国連邦法)' },
    danger_en: 'RAISES BLOOD PRESSURE AND HEART RATE. Do NOT use if you have uncontrolled high blood pressure, heart disease, hyperthyroidism, glaucoma, or enlarged prostate. Can cause insomnia, anxiety, and heart palpitations.',
    danger_ko: '혈압과 심박수를 상승시킵니다. 조절되지 않는 고혈압, 심장병, 갑상선 기능 항진증, 녹내장, 전립선 비대가 있으면 사용하지 마세요. 불면, 불안, 심계항진을 유발할 수 있습니다.',
    danger_ja: '血圧と心拍数を上昇させます。コントロール不良の高血圧、心疾患、甲状腺機能亢進症、緑内障、前立腺肥大がある場合は使用しないでください。不眠、不安、動悸を起こすことがあります。',
    warn_en: 'Do not take within 2 hours of bedtime. Do not use for more than 7 days. In the US, purchase is federally restricted (Combat Methamphetamine Act) — you must show ID.',
    warn_ko: '취침 2시간 이내에는 복용하지 마세요. 7일 이상 사용하지 마세요. 미국에서는 연방법에 의해 구매가 제한되어 있으며(메스암페타민 규제법) 신분증 제시가 필요합니다.',
    warn_ja: '就寝2時間以内には服用しないでください。7日以上使用しないでください。米国では連邦法により購入が制限され(メタンフェタミン規制法)、身分証明書の提示が必要です。',
    interact: [
      { en: 'MAO inhibitors — dangerous blood pressure spike (do not combine)', ko: 'MAO 억제제 — 위험한 혈압 급상승 (병용 금지)', ja: 'MAO阻害薬 — 危険な血圧急上昇(併用禁止)' },
      { en: 'Blood pressure medications — reduced effectiveness', ko: '혈압약 — 효과 감소', ja: '降圧薬 — 効果減少' },
      { en: 'Stimulants, caffeine — added cardiovascular effects', ko: '각성제, 카페인 — 심혈관 효과 누적', ja: '覚醒剤、カフェイン — 心血管系作用の累積' },
      { en: 'Tricyclic antidepressants — increased blood pressure', ko: '삼환계 항우울제 — 혈압 상승', ja: '三環系抗うつ薬 — 血圧上昇' }
    ],
    source: 'FDA OTC Monograph 21 CFR 341 · DailyMed (NIH)'
  },
  {
    id: 'phenylephrine',
    generic: { en: 'Phenylephrine (oral)', ko: '페닐에프린 (경구)', ja: 'フェニレフリン(経口)' },
    brands: ['Sudafed PE', 'Neo-Synephrine (nasal spray)'],
    category: 'allergy',
    uses: [
      { title_en: 'Nasal congestion relief', title_ko: '코막힘 완화', title_ja: '鼻づまりの緩和',
        detail_en: 'Stuffy nose from colds, allergies, or sinus problems',
        detail_ko: '감기, 알레르기, 부비동 문제로 인한 코막힘',
        detail_ja: '風邪、アレルギー、副鼻腔の問題による鼻づまり' }
    ],
    dose_en: { 'Adult (oral)': '10 mg every 4 hours', 'Max per day': '60 mg', 'Nasal spray': '2–3 sprays each nostril every 4 hours (max 3 days)', 'Availability': 'Sold without ID restriction' },
    dose_ko: { '성인 (경구)': '10 mg, 4시간마다', '하루 최대': '60 mg', '비강 스프레이': '콧구멍당 2~3회 분무, 4시간마다 (최대 3일)', '구매': '신분증 제한 없이 판매' },
    dose_ja: { '成人(経口)': '4時間ごとに10 mg', '1日最大量': '60 mg', '鼻スプレー': '4時間ごとに各鼻孔に2~3回噴霧(最大3日)', '購入': '身分証明書制限なしで販売' },
    warn_en: 'In 2023, an FDA advisory panel concluded oral phenylephrine is NOT effective as a decongestant at approved doses — if oral phenylephrine is not working, ask your pharmacist about pseudoephedrine instead. Nasal sprays remain effective but must not be used longer than 3 days (causes rebound congestion). Avoid in high blood pressure, heart disease, or enlarged prostate.',
    warn_ko: '2023년 FDA 자문위원회는 경구 페닐에프린이 승인된 용량에서 코막힘 해소제로 효과가 없다고 결론지었습니다 — 경구 페닐에프린이 듣지 않으면 약사에게 슈도에페드린을 문의하세요. 비강 스프레이는 여전히 효과적이지만 3일 이상 사용하면 안 됩니다 (반동성 코막힘 유발). 고혈압, 심장병, 전립선 비대에서는 사용하지 마세요.',
    warn_ja: '2023年、FDA諮問委員会は経口フェニレフリンが承認用量では鼻づまり解消薬として有効でないと結論づけました — 経口フェニレフリンが効かない場合は薬剤師にプソイドエフェドリンについて相談してください。鼻スプレーは依然有効ですが、3日以上使用してはいけません(リバウンド鼻づまりを起こします)。高血圧、心疾患、前立腺肥大では使用を避けてください。',
    interact: [
      { en: 'MAO inhibitors — dangerous blood pressure interaction', ko: 'MAO 억제제 — 위험한 혈압 상호작용', ja: 'MAO阻害薬 — 危険な血圧相互作用' },
      { en: 'Blood pressure medications — reduced effectiveness', ko: '혈압약 — 효과 감소', ja: '降圧薬 — 効果減少' },
      { en: 'Other stimulants — additive effects', ko: '다른 각성제 — 효과 누적', ja: '他の覚醒剤 — 作用の累積' }
    ],
    source: 'FDA OTC Monograph 21 CFR 341 · DailyMed (NIH)'
  },

  // ============ COUGH & THROAT ============
  {
    id: 'dextromethorphan',
    generic: { en: 'Dextromethorphan (DM)', ko: '덱스트로메토르판 (DM)', ja: 'デキストロメトルファン(DM)' },
    brands: ['Robitussin DM', 'Delsym', 'Mucinex DM'],
    category: 'cough',
    uses: [
      { title_en: 'Cough suppressant', title_ko: '기침 억제', title_ja: '咳止め',
        detail_en: 'Temporarily relieves dry, non-productive cough from the common cold or minor throat/bronchial irritation',
        detail_ko: '감기 또는 경미한 인후·기관지 자극으로 인한 마른 기침(가래 없는 기침)을 일시적으로 완화',
        detail_ja: '風邪または軽度の咽頭·気管支刺激による乾性咳(痰の出ない咳)を一時的に緩和' }
    ],
    dose_en: { 'Adult and child 12+': '10–20 mg every 4 hours OR 30 mg every 6–8 hours', 'Extended release (Delsym)': '60 mg every 12 hours', 'Max per day': '120 mg', 'Child 6–11': 'Half adult dose — check label' },
    dose_ko: { '성인 및 12세 이상': '10~20 mg, 4시간마다 또는 30 mg, 6~8시간마다', '서방형 (Delsym)': '60 mg, 12시간마다', '하루 최대': '120 mg', '6~11세': '성인 용량의 절반 — 라벨 확인' },
    dose_ja: { '成人および12歳以上': '4時間ごとに10~20 mgまたは6~8時間ごとに30 mg', '徐放性(Delsym)': '12時間ごとに60 mg', '1日最大量': '120 mg', '6~11歳': '成人用量の半分 — ラベル確認' },
    danger_en: 'ABUSE POTENTIAL — at very high doses dextromethorphan causes hallucinations and can be fatal. Keep away from teenagers. Do NOT combine with MAO inhibitors or SSRI antidepressants (serotonin syndrome risk). Do not give to children under 4.',
    danger_ko: '남용 위험 — 고용량에서는 환각을 유발하며 치명적일 수 있습니다. 청소년의 손이 닿지 않는 곳에 보관하세요. MAO 억제제나 SSRI 항우울제와 절대 병용하지 마세요 (세로토닌 증후군 위험). 4세 미만에게 투여 금지.',
    danger_ja: '乱用リスク — 高用量では幻覚を引き起こし致命的になる可能性。青少年の手の届かない場所に保管。MAO阻害薬やSSRI抗うつ薬と絶対に併用しないでください(セロトニン症候群リスク)。4歳未満には投与禁止。',
    warn_en: 'Do not use for cough with excessive mucus or cough lasting more than 7 days. If cough is accompanied by fever, rash, or persistent headache, see a doctor.',
    warn_ko: '가래가 많은 기침이나 7일 이상 지속되는 기침에는 사용하지 마세요. 기침과 함께 발열, 발진, 지속적 두통이 있으면 의사를 만나세요.',
    warn_ja: '痰の多い咳や7日以上続く咳には使用しないでください。咳とともに発熱、発疹、持続性頭痛がある場合は医師を受診してください。',
    interact: [
      { en: 'MAO inhibitors — serotonin syndrome (potentially fatal)', ko: 'MAO 억제제 — 세로토닌 증후군 (치명적일 수 있음)', ja: 'MAO阻害薬 — セロトニン症候群(致命的な可能性)' },
      { en: 'SSRI/SNRI antidepressants — serotonin syndrome risk', ko: 'SSRI/SNRI 항우울제 — 세로토닌 증후군 위험', ja: 'SSRI/SNRI抗うつ薬 — セロトニン症候群リスク' },
      { en: 'Alcohol, sedatives — increased drowsiness', ko: '알코올, 진정제 — 졸음 증가', ja: 'アルコール、鎮静薬 — 眠気増加' }
    ],
    source: 'FDA OTC Monograph 21 CFR 341 · DailyMed (NIH)'
  },
  {
    id: 'guaifenesin',
    generic: { en: 'Guaifenesin', ko: '구아이페네신', ja: 'グアイフェネシン' },
    brands: ['Mucinex', 'Robitussin'],
    category: 'cough',
    uses: [
      { title_en: 'Expectorant — loosens mucus', title_ko: '거담제 — 가래 배출 촉진', title_ja: '去痰薬 — 痰の排出促進',
        detail_en: 'Helps loosen phlegm (mucus) and thin bronchial secretions so cough is more productive and airways clear',
        detail_ko: '가래(점액)를 묽게 하고 기관지 분비물을 묽게 하여 기침으로 가래가 잘 배출되고 기도가 맑아지도록 도움',
        detail_ja: '痰(粘液)を緩め気管支分泌物を薄くし、咳で痰が出やすくなり気道を清浄化' }
    ],
    dose_en: { 'Adult and child 12+': '200–400 mg every 4 hours', 'Extended release (Mucinex)': '600–1200 mg every 12 hours', 'Max per day': '2400 mg', 'Drink': 'Plenty of water to help mucus thin' },
    dose_ko: { '성인 및 12세 이상': '200~400 mg, 4시간마다', '서방형 (Mucinex)': '600~1200 mg, 12시간마다', '하루 최대': '2400 mg', '수분 섭취': '물을 충분히 마셔 가래가 묽어지도록 도움' },
    dose_ja: { '成人および12歳以上': '4時間ごとに200~400 mg', '徐放性(Mucinex)': '12時間ごとに600~1200 mg', '1日最大量': '2400 mg', '水分摂取': '痰を薄めるため十分な水を摂取' },
    warn_en: 'Very well tolerated. If cough lasts more than 7 days, comes back, or is accompanied by fever, rash, or persistent headache, see a doctor — these may be signs of a more serious condition.',
    warn_ko: '내약성이 매우 좋습니다. 기침이 7일 이상 지속되거나 재발하거나, 발열·발진·지속적 두통이 동반되면 의사를 만나세요 — 더 심각한 질환의 징후일 수 있습니다.',
    warn_ja: '忍容性は非常に良好です。咳が7日以上続く、再発する、または発熱·発疹·持続性頭痛を伴う場合は医師を受診 — より重篤な疾患の徴候の可能性があります。',
    interact: [
      { en: 'Very few significant drug interactions', ko: '유의미한 약물 상호작용이 거의 없음', ja: '有意な薬物相互作用はほとんどなし' }
    ],
    source: 'FDA OTC Monograph 21 CFR 341 · DailyMed (NIH)'
  },
  {
    id: 'benzocaine-lozenge',
    generic: { en: 'Benzocaine (throat lozenge/spray)', ko: '벤조카인 (인후 로젠지/스프레이)', ja: 'ベンゾカイン(のどトローチ/スプレー)' },
    brands: ['Cepacol', 'Chloraseptic'],
    category: 'cough',
    uses: [
      { title_en: 'Sore throat pain relief', title_ko: '인후통 완화', title_ja: 'のどの痛みの緩和',
        detail_en: 'Temporarily numbs mouth and throat to relieve pain from sore throat, minor mouth irritation, or canker sores',
        detail_ko: '인후통, 경미한 구강 자극, 구내염으로 인한 통증을 완화하기 위해 일시적으로 입과 목을 마취',
        detail_ja: 'のどの痛み、軽度の口腔刺激、口内炎による痛みを緩和するため一時的に口とのどを麻酔' },
      { title_en: 'Minor mouth/gum irritation', title_ko: '경미한 구강·잇몸 자극', title_ja: '軽度の口腔·歯茎の刺激',
        detail_en: 'Relieves pain from minor mouth or gum irritation',
        detail_ko: '경미한 구강 또는 잇몸 자극으로 인한 통증 완화',
        detail_ja: '軽度の口腔または歯茎の刺激による痛みを緩和' }
    ],
    dose_en: { 'Adult and child 5+': 'Dissolve 1 lozenge slowly in mouth; repeat every 2 hours as needed', 'Spray': '1–2 sprays, up to every 2 hours', 'Do not exceed': 'Product label maximum' },
    dose_ko: { '성인 및 5세 이상': '로젠지 1개를 입안에서 천천히 녹임; 필요 시 2시간마다 반복', '스프레이': '1~2회 분무, 최대 2시간 간격', '초과 금지': '제품 라벨의 최대 용량' },
    dose_ja: { '成人および5歳以上': 'トローチ1個を口内でゆっくり溶かす;必要に応じて2時間ごとに繰り返し', 'スプレー': '1~2回噴霧、最大2時間間隔', '超過禁止': '製品ラベルの最大用量' },
    danger_en: 'METHEMOGLOBINEMIA — a rare but serious (sometimes fatal) condition where blood cannot carry oxygen. Signs: pale, gray, or blue-colored skin or lips; shortness of breath; fatigue; headache; rapid heart rate. FDA warns against use in children under 2. Stop and seek care if these signs appear.',
    danger_ko: '메트헤모글로빈혈증 — 혈액이 산소를 운반할 수 없게 되는 드물지만 심각한(때로는 치명적인) 질환. 증상: 창백하거나 회색·청색을 띠는 피부나 입술, 호흡 곤란, 피로, 두통, 빠른 심박수. FDA는 2세 미만 어린이에게 사용하지 말 것을 경고합니다. 이러한 증상이 나타나면 즉시 중단하고 진료를 받으세요.',
    danger_ja: 'メトヘモグロビン血症 — 血液が酸素を運搬できなくなる稀ですが重篤(時に致命的)な疾患。症状:蒼白·灰色·青色の皮膚や唇、呼吸困難、疲労、頭痛、頻脈。FDAは2歳未満の小児への使用を警告。これらの症状が現れたら直ちに中止し受診してください。',
    warn_en: 'Do not use more than the label states. Not for use in children under 2. If sore throat is severe, lasts more than 2 days, or comes with high fever, rash, headache, nausea, or vomiting — see a doctor (could be strep throat).',
    warn_ko: '라벨에 표시된 것보다 많이 사용하지 마세요. 2세 미만 어린이에게는 사용 금지. 인후통이 심하거나 2일 이상 지속되거나, 고열·발진·두통·메스꺼움·구토와 함께 나타나면 의사를 만나세요 (연쇄상구균 인두염일 수 있음).',
    warn_ja: 'ラベル表示より多く使用しないでください。2歳未満の小児には使用禁止。のどの痛みが重度、2日以上続く、または高熱·発疹·頭痛·吐き気·嘔吐を伴う場合は医師を受診(溶連菌咽頭炎の可能性)。',
    interact: [
      { en: 'Local anesthetics — avoid using multiple benzocaine products at once', ko: '국소 마취제 — 여러 벤조카인 제품을 동시에 사용하지 말 것', ja: '局所麻酔薬 — 複数のベンゾカイン製品を同時使用しないこと' }
    ],
    source: 'FDA OTC Monograph 21 CFR 356 · DailyMed (NIH)'
  },

  // ============ STOMACH & GI ============
  {
    id: 'famotidine',
    generic: { en: 'Famotidine', ko: '파모티딘', ja: 'ファモチジン' },
    brands: ['Pepcid', 'Pepcid AC', 'Zantac 360'],
    category: 'gi',
    uses: [
      { title_en: 'Heartburn relief (H2 blocker)', title_ko: '속쓰림 완화 (H2 차단제)', title_ja: '胸焼けの緩和(H2ブロッカー)',
        detail_en: 'Relieves heartburn associated with acid indigestion and sour stomach',
        detail_ko: '위산 소화불량 및 신트림과 관련된 속쓰림 완화',
        detail_ja: '胃酸消化不良および胃酸逆流に伴う胸焼けを緩和' },
      { title_en: 'Heartburn prevention', title_ko: '속쓰림 예방', title_ja: '胸焼け予防',
        detail_en: 'Prevents heartburn brought on by certain foods and beverages when taken 15–60 minutes before eating',
        detail_ko: '특정 음식·음료로 인한 속쓰림을 예방하려면 식사 15~60분 전에 복용',
        detail_ja: '特定の食事·飲料による胸焼けを予防するため食事15~60分前に服用' }
    ],
    dose_en: { 'Adult treatment': '10–20 mg when symptoms occur', 'Prevention': '10–20 mg 15–60 minutes before eating', 'Max per day (OTC)': '40 mg', 'Max duration': 'Do not use for more than 14 days without doctor' },
    dose_ko: { '성인 치료': '증상이 있을 때 10~20 mg', '예방': '식사 15~60분 전 10~20 mg', '하루 최대 (OTC)': '40 mg', '최대 기간': '의사 지시 없이 14일 이상 사용 금지' },
    dose_ja: { '成人治療': '症状時に10~20 mg', '予防': '食事15~60分前に10~20 mg', '1日最大量(OTC)': '40 mg', '最大期間': '医師の指示なく14日以上使用禁止' },
    warn_en: 'Reduce dose if you have kidney disease. Heartburn that is severe, lasts more than 3 months, comes with chest pain or pain spreading to the arm/jaw, or comes with trouble swallowing or unexplained weight loss — see a doctor. These can be signs of a heart attack or serious illness.',
    warn_ko: '신장 질환이 있으면 용량을 감량하세요. 속쓰림이 심하거나 3개월 이상 지속되거나, 가슴 통증 또는 팔·턱으로 퍼지는 통증과 함께 나타나거나, 삼키기 어려움이나 설명되지 않는 체중 감소와 함께 나타나면 의사를 만나세요. 심장마비나 심각한 질환의 징후일 수 있습니다.',
    warn_ja: '腎疾患がある場合は減量してください。胸焼けが重度、3か月以上続く、胸痛や腕·顎に広がる痛みを伴う、または嚥下困難·原因不明の体重減少を伴う場合は医師を受診。心筋梗塞や重篤疾患の徴候の可能性があります。',
    interact: [
      { en: 'Drugs requiring stomach acid for absorption (ketoconazole, atazanavir) — reduced effect', ko: '흡수에 위산이 필요한 약물 (케토코나졸, 아타자나비르) — 효과 감소', ja: '吸収に胃酸が必要な薬(ケトコナゾール、アタザナビル) — 効果減少' },
      { en: 'Generally few significant interactions compared to older H2 blockers', ko: '구형 H2 차단제에 비해 유의미한 상호작용이 적음', ja: '旧型H2ブロッカーと比べて有意な相互作用は少ない' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'omeprazole',
    generic: { en: 'Omeprazole', ko: '오메프라졸', ja: 'オメプラゾール' },
    brands: ['Prilosec OTC', 'Zegerid OTC'],
    category: 'gi',
    uses: [
      { title_en: 'Frequent heartburn (2+ days per week)', title_ko: '잦은 속쓰림 (주 2회 이상)', title_ja: '頻繁な胸焼け(週2日以上)',
        detail_en: 'Treats frequent heartburn — 14-day course that starts working in 1–4 days',
        detail_ko: '잦은 속쓰림 치료 — 14일 요법으로 1~4일 내에 효과 시작',
        detail_ja: '頻繁な胸焼けの治療 — 14日間療法で1~4日以内に効果開始' }
    ],
    dose_en: { 'Adult': '20 mg once daily, 30–60 minutes before breakfast', 'Duration': '14 days straight, then stop', 'Repeat course': 'Wait 4 months before another 14-day course', 'Max': 'No more than 3 courses per year without doctor' },
    dose_ko: { '성인': '아침 식사 30~60분 전 하루 1회 20 mg', '사용 기간': '연속 14일간 복용 후 중단', '재시작': '다음 14일 요법까지 4개월 대기', '최대': '의사 지시 없이 연 3회 초과 금지' },
    dose_ja: { '成人': '朝食30~60分前に1日1回20 mg', '使用期間': '連続14日間服用後中止', '再開': '次の14日療法まで4か月待機', '最大': '医師の指示なく年3回超過禁止' },
    danger_en: 'LONG-TERM USE RISKS — Beyond the 14-day OTC course, long-term PPI use is associated with low magnesium, vitamin B12 deficiency, increased bone fracture risk, increased risk of C. difficile and pneumonia infections, and possible kidney issues. Do not extend on your own.',
    danger_ko: '장기 사용 위험 — 14일 OTC 요법을 초과한 장기 PPI 사용은 저마그네슘혈증, 비타민 B12 결핍, 골절 위험 증가, 클로스트리디움 디피실·폐렴 감염 위험 증가, 신장 문제와 관련이 있습니다. 스스로 연장 복용하지 마세요.',
    danger_ja: '長期使用リスク — 14日OTC療法を超える長期PPI使用は低マグネシウム血症、ビタミンB12欠乏、骨折リスク増加、C. difficile·肺炎感染リスク増加、腎臓問題と関連。自己判断で延長しないでください。',
    warn_en: 'Do not use for immediate relief — this drug takes 1–4 days to start working. If symptoms persist or return after 14 days, see a doctor. Chest pain, trouble swallowing, vomiting blood, or bloody/black stools — seek emergency care.',
    warn_ko: '즉각적인 증상 완화용이 아닙니다 — 효과가 나타나는 데 1~4일이 걸립니다. 증상이 14일 후에도 지속되거나 재발하면 의사를 만나세요. 가슴 통증, 삼키기 어려움, 혈토, 혈변·흑변 — 응급 진료를 받으세요.',
    warn_ja: '即時症状緩和用ではありません — 効果が現れるまで1~4日かかります。14日後も症状が続くか再発する場合は医師を受診。胸痛、嚥下困難、吐血、血便·黒色便 — 救急受診。',
    interact: [
      { en: 'Clopidogrel (Plavix) — reduces its heart-protective effect (major concern)', ko: '클로피도그렐 (플라빅스) — 심장 보호 효과 감소 (주요 우려)', ja: 'クロピドグレル(プラビックス) — 心保護効果を減少(主要な懸念)' },
      { en: 'Methotrexate — increased toxicity', ko: '메토트렉세이트 — 독성 증가', ja: 'メトトレキサート — 毒性増加' },
      { en: 'Warfarin — increased bleeding risk', ko: '와파린 — 출혈 위험 증가', ja: 'ワーファリン — 出血リスク増加' },
      { en: 'Drugs needing stomach acid (ketoconazole, iron, atazanavir) — reduced absorption', ko: '위산이 필요한 약물 (케토코나졸, 철분제, 아타자나비르) — 흡수 감소', ja: '胃酸が必要な薬(ケトコナゾール、鉄剤、アタザナビル) — 吸収減少' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'calcium-carbonate',
    generic: { en: 'Calcium carbonate (antacid)', ko: '탄산칼슘 (제산제)', ja: '炭酸カルシウム(制酸薬)' },
    brands: ['Tums', 'Rolaids'],
    category: 'gi',
    uses: [
      { title_en: 'Fast heartburn relief', title_ko: '빠른 속쓰림 완화', title_ja: '胸焼けの即効緩和',
        detail_en: 'Neutralizes stomach acid quickly — works in minutes but short-acting',
        detail_ko: '위산을 빠르게 중화 — 몇 분 내에 작용하지만 짧게 지속됨',
        detail_ja: '胃酸を素早く中和 — 数分以内に作用するが短時間' },
      { title_en: 'Acid indigestion and sour stomach', title_ko: '위산 소화불량 및 신트림', title_ja: '胃酸消化不良と胃もたれ',
        detail_en: 'Relieves symptoms of indigestion and upset stomach from acid',
        detail_ko: '위산으로 인한 소화불량 및 속 불편감 완화',
        detail_ja: '胃酸による消化不良および胃の不快感を緩和' },
      { title_en: 'Calcium supplement', title_ko: '칼슘 보충', title_ja: 'カルシウム補給',
        detail_en: 'Can be used as a dietary calcium source (check label for amount)',
        detail_ko: '식이 칼슘 공급원으로 사용 가능 (양은 라벨 확인)',
        detail_ja: '食事性カルシウム源として使用可能(量はラベル確認)' }
    ],
    dose_en: { 'Adult': 'Chew 2–4 tablets as symptoms occur', 'Max per day': 'Follow product label — typically do not exceed 15 Tums Regular Strength tablets', 'Timing': 'Works in 5–15 minutes, lasts 20–60 minutes' },
    dose_ko: { '성인': '증상이 있을 때 2~4정 씹어 복용', '하루 최대': '제품 라벨에 따름 — 일반적으로 Tums Regular Strength 15정 초과 금지', '작용 시간': '5~15분 내 효과, 20~60분 지속' },
    dose_ja: { '成人': '症状時に2~4錠を噛んで服用', '1日最大量': '製品ラベルに従う — 通常Tums Regular Strength 15錠を超えない', '作用時間': '5~15分以内に効果、20~60分持続' },
    warn_en: 'Do not take if you have kidney disease without doctor approval. Do not take more than the label states. Chronic high-dose use can cause kidney stones, constipation, and milk-alkali syndrome. If symptoms last more than 2 weeks, see a doctor.',
    warn_ko: '신장 질환이 있으면 의사 승인 없이 복용하지 마세요. 라벨에 표시된 것보다 많이 복용하지 마세요. 고용량 만성 사용은 신장 결석, 변비, 우유-알칼리 증후군을 유발할 수 있습니다. 증상이 2주 이상 지속되면 의사를 만나세요.',
    warn_ja: '腎疾患がある場合は医師の承認なく服用しないでください。ラベル表示より多く服用しないでください。高用量慢性使用は腎結石、便秘、ミルク·アルカリ症候群を引き起こす可能性があります。症状が2週間以上続く場合は医師を受診。',
    interact: [
      { en: 'Antibiotics (tetracyclines, quinolones) — reduced absorption (separate by 2 hours)', ko: '항생제 (테트라사이클린, 퀴놀론) — 흡수 감소 (2시간 간격 필요)', ja: '抗生物質(テトラサイクリン、キノロン) — 吸収減少(2時間間隔必要)' },
      { en: 'Iron supplements, thyroid medication — reduced absorption', ko: '철분제, 갑상선약 — 흡수 감소', ja: '鉄剤、甲状腺薬 — 吸収減少' },
      { en: 'Digoxin — altered effect', ko: '디곡신 — 효과 변화', ja: 'ジゴキシン — 効果変動' }
    ],
    source: 'FDA OTC Monograph 21 CFR 331 · DailyMed (NIH)'
  },
  {
    id: 'loperamide',
    generic: { en: 'Loperamide', ko: '로페라미드', ja: 'ロペラミド' },
    brands: ['Imodium A-D'],
    category: 'gi',
    uses: [
      { title_en: 'Diarrhea control', title_ko: '설사 조절', title_ja: '下痢のコントロール',
        detail_en: 'Controls symptoms of diarrhea, including travelers\' diarrhea',
        detail_ko: '여행자 설사를 포함한 설사 증상 조절',
        detail_ja: '旅行者下痢を含む下痢症状をコントロール' }
    ],
    dose_en: { 'Adult and child 12+': '4 mg after first loose stool, then 2 mg after each subsequent loose stool', 'Max per day (OTC)': '8 mg', 'Max duration': 'Do not use for more than 2 days without doctor', 'Child 6–11': 'See label — lower doses' },
    dose_ko: { '성인 및 12세 이상': '첫 무른 변 후 4 mg, 이후 무른 변마다 2 mg', '하루 최대 (OTC)': '8 mg', '최대 기간': '의사 지시 없이 2일 이상 사용 금지', '6~11세': '라벨 참조 — 저용량' },
    dose_ja: { '成人および12歳以上': '最初の軟便後に4 mg、以後軟便ごとに2 mg', '1日最大量(OTC)': '8 mg', '最大期間': '医師の指示なく2日以上使用禁止', '6~11歳': 'ラベル参照 — 低用量' },
    danger_en: 'SERIOUS HEART PROBLEMS AT HIGH DOSES — FDA warns that taking much more than the recommended dose (abuse) can cause fatal heart rhythm problems. Keep out of reach of teens. Do not use if you have bloody stools or black stools (may indicate serious illness). Do not use if you have a fever over 101°F — this could be an infection that diarrhea is clearing.',
    danger_ko: '고용량에서 심각한 심장 문제 — FDA는 권장 용량을 크게 초과한 복용(남용)이 치명적인 부정맥을 일으킬 수 있다고 경고합니다. 청소년의 손이 닿지 않는 곳에 보관하세요. 혈변이나 흑변이 있으면 사용하지 마세요 (심각한 질환의 징후일 수 있음). 101°F(38.3°C) 이상의 발열이 있으면 사용하지 마세요 — 설사가 제거하고 있는 감염일 수 있습니다.',
    danger_ja: '高用量で重篤な心臓問題 — FDAは推奨用量を大幅に超える服用(乱用)が致命的不整脈を起こす可能性があると警告。青少年の手の届かない場所に保管。血便·黒色便がある場合は使用禁止(重篤疾患の徴候の可能性)。38.3°C(101°F)以上の発熱がある場合は使用禁止 — 下痢が排除している感染の可能性。',
    warn_en: 'Stop use and see a doctor if diarrhea lasts more than 2 days, if you develop abdominal swelling or bulging, or if you have bloody/black stools. Drink plenty of fluids to prevent dehydration.',
    warn_ko: '설사가 2일 이상 지속되거나, 복부 팽만이나 돌출이 발생하거나, 혈변·흑변이 있으면 사용을 중단하고 의사를 만나세요. 탈수 예방을 위해 수분을 충분히 섭취하세요.',
    warn_ja: '下痢が2日以上続く、腹部膨満や膨隆が現れる、または血便·黒色便がある場合は使用を中止し医師を受診。脱水予防のため十分な水分を摂取してください。',
    interact: [
      { en: 'Quinidine, ritonavir — may increase loperamide levels (heart risk)', ko: '퀴니딘, 리토나비르 — 로페라미드 농도 상승 가능 (심장 위험)', ja: 'キニジン、リトナビル — ロペラミド濃度上昇の可能性(心臓リスク)' },
      { en: 'Other drugs that prolong QT interval — heart rhythm risk', ko: 'QT 간격을 연장하는 다른 약물 — 부정맥 위험', ja: 'QT間隔を延長する他の薬 — 不整脈リスク' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'bismuth-subsalicylate',
    generic: { en: 'Bismuth subsalicylate', ko: '비스무스 서브살리실레이트', ja: '次サリチル酸ビスマス' },
    brands: ['Pepto-Bismol', 'Kaopectate'],
    category: 'gi',
    uses: [
      { title_en: 'Upset stomach', title_ko: '속 불편감', title_ja: '胃の不快感',
        detail_en: 'Relieves upset stomach, indigestion, and heartburn',
        detail_ko: '속 불편감, 소화불량, 속쓰림 완화',
        detail_ja: '胃の不快感、消化不良、胸焼けを緩和' },
      { title_en: 'Nausea', title_ko: '메스꺼움', title_ja: '吐き気',
        detail_en: 'Relieves nausea',
        detail_ko: '메스꺼움 완화',
        detail_ja: '吐き気を緩和' },
      { title_en: 'Diarrhea', title_ko: '설사', title_ja: '下痢',
        detail_en: 'Controls diarrhea',
        detail_ko: '설사 조절',
        detail_ja: '下痢をコントロール' },
      { title_en: 'Gas and fullness', title_ko: '가스 및 포만감', title_ja: 'ガスと膨満感',
        detail_en: 'Relieves gas and feeling of fullness',
        detail_ko: '가스와 포만감 완화',
        detail_ja: 'ガスと膨満感を緩和' }
    ],
    dose_en: { 'Adult and child 12+': '30 mL or 2 tablets every 30–60 minutes as needed', 'Max per day': '8 doses (240 mL)', 'Max duration': '2 days', 'Child under 12': 'Do not use without doctor' },
    dose_ko: { '성인 및 12세 이상': '필요 시 30~60분마다 30 mL 또는 2정', '하루 최대': '8회 (240 mL)', '최대 기간': '2일', '12세 미만': '의사 지시 없이 사용 금지' },
    dose_ja: { '成人および12歳以上': '必要に応じて30~60分ごとに30 mLまたは2錠', '1日最大量': '8回(240 mL)', '最大期間': '2日', '12歳未満': '医師の指示なく使用禁止' },
    danger_en: 'REYE\'S SYNDROME — Do NOT give to children or teenagers recovering from chicken pox or flu. Contains salicylate (aspirin-like), so same Reye\'s syndrome risk applies. Can cause temporary harmless black darkening of tongue and stool.',
    danger_ko: '라이 증후군 — 수두나 독감에서 회복 중인 어린이·청소년에게 투여하지 마세요. 살리실산염(아스피린 유사 성분)을 함유하므로 동일한 라이 증후군 위험이 적용됩니다. 혀와 대변이 일시적으로 검게 변할 수 있으며, 이는 무해합니다.',
    danger_ja: 'ライ症候群 — 水痘やインフルエンザから回復中の小児·青少年には投与禁止。サリチル酸塩(アスピリン類似成分)を含有するため同じライ症候群リスクが適用。舌と便が一時的に黒くなることがありますが無害です。',
    warn_en: 'Avoid if you have bleeding disorders, stomach ulcers, gout, or aspirin allergy. Do not combine with other salicylates (aspirin) due to additive toxicity risk. Stop and see a doctor if symptoms worsen or you develop ringing in your ears.',
    warn_ko: '출혈 장애, 위궤양, 통풍, 아스피린 알레르기가 있으면 사용하지 마세요. 독성 누적 위험 때문에 다른 살리실산염(아스피린)과 병용하지 마세요. 증상이 악화되거나 이명이 발생하면 중단하고 의사를 만나세요.',
    warn_ja: '出血性疾患、胃潰瘍、痛風、アスピリンアレルギーがある場合は使用禁止。毒性累積リスクのため他のサリチル酸塩(アスピリン)と併用禁止。症状が悪化するか耳鳴りが現れたら中止し医師を受診。',
    interact: [
      { en: 'Aspirin and other salicylates — additive toxicity', ko: '아스피린 및 기타 살리실산염 — 독성 누적', ja: 'アスピリンおよび他のサリチル酸塩 — 毒性累積' },
      { en: 'Blood thinners — increased bleeding risk', ko: '혈액 희석제 — 출혈 위험 증가', ja: '抗凝固薬 — 出血リスク増加' },
      { en: 'Tetracycline antibiotics — reduced absorption', ko: '테트라사이클린 항생제 — 흡수 감소', ja: 'テトラサイクリン抗生物質 — 吸収減少' },
      { en: 'Diabetes medications — may increase effect', ko: '당뇨병약 — 효과 증가 가능', ja: '糖尿病薬 — 効果増強の可能性' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'simethicone',
    generic: { en: 'Simethicone', ko: '시메티콘', ja: 'ジメチコン' },
    brands: ['Gas-X', 'Mylicon', 'Phazyme'],
    category: 'gi',
    uses: [
      { title_en: 'Gas pain and bloating', title_ko: '가스 통증 및 복부 팽만', title_ja: 'ガスの痛みと腹部膨満',
        detail_en: 'Relieves pressure, bloating, and fullness caused by swallowed gas in the stomach and intestines',
        detail_ko: '위와 장 내 삼킨 가스로 인한 압박감, 복부 팽만, 포만감 완화',
        detail_ja: '胃·腸内に飲み込まれたガスによる圧迫感、膨満、満腹感を緩和' }
    ],
    dose_en: { 'Adult': '40–360 mg after meals and at bedtime as needed', 'Max per day': '500 mg', 'Infant drops': 'Available for babies with gas — ask pediatrician' },
    dose_ko: { '성인': '필요 시 식후 및 취침 시 40~360 mg', '하루 최대': '500 mg', '영유아 점적액': '가스가 있는 아기를 위해 사용 가능 — 소아과 의사에게 문의' },
    dose_ja: { '成人': '必要に応じて食後·就寝時に40~360 mg', '1日最大量': '500 mg', '乳児用ドロップ': 'ガスのある赤ちゃん用あり — 小児科医に相談' },
    warn_en: 'Very safe — not absorbed from the digestive tract. If symptoms are severe or persistent, see a doctor to rule out other causes.',
    warn_ko: '매우 안전합니다 — 소화관에서 흡수되지 않습니다. 증상이 심하거나 지속되면 다른 원인을 배제하기 위해 의사를 만나세요.',
    warn_ja: '非常に安全 — 消化管から吸収されません。症状が重度または持続する場合は他の原因を除外するため医師を受診。',
    interact: [
      { en: 'Essentially no drug interactions — considered one of the safest OTC medications', ko: '약물 상호작용이 거의 없음 — 가장 안전한 OTC 약 중 하나로 여겨짐', ja: '薬物相互作用はほとんどなし — 最も安全なOTC薬の一つとされる' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },

  // ============ SKIN & TOPICAL ============
  {
    id: 'hydrocortisone',
    generic: { en: 'Hydrocortisone 1% (topical)', ko: '히드로코르티손 1% (외용)', ja: 'ヒドロコルチゾン1%(外用)' },
    brands: ['Cortizone-10', 'Cortaid'],
    category: 'skin',
    uses: [
      { title_en: 'Itch relief', title_ko: '가려움 완화', title_ja: 'かゆみの緩和',
        detail_en: 'Temporarily relieves itching from eczema, insect bites, poison ivy/oak/sumac, soap, detergents, cosmetics, jewelry, and minor skin irritations',
        detail_ko: '습진, 벌레 물림, 옻나무, 비누, 세제, 화장품, 장신구, 경미한 피부 자극으로 인한 가려움을 일시적으로 완화',
        detail_ja: '湿疹、虫刺され、ウルシ、石鹸、洗剤、化粧品、装身具、軽度の皮膚刺激によるかゆみを一時的に緩和' },
      { title_en: 'Rash and inflammation', title_ko: '발진 및 염증', title_ja: '発疹·炎症',
        detail_en: 'Reduces redness and swelling from minor skin inflammation',
        detail_ko: '경미한 피부 염증으로 인한 발적과 붓기 감소',
        detail_ja: '軽度の皮膚炎症による発赤と腫れを軽減' },
      { title_en: 'Anal/genital itching (external only)', title_ko: '항문·외음부 가려움 (외부에만)', title_ja: '肛門·外陰部のかゆみ(外部のみ)',
        detail_en: 'Relieves external anal and genital itching (do not use internally)',
        detail_ko: '항문 및 외음부의 외부 가려움 완화 (내부 사용 금지)',
        detail_ja: '肛門·外陰部の外部のかゆみを緩和(内部使用禁止)' }
    ],
    dose_en: { 'Adult and child 2+': 'Apply thin layer to affected area 3–4 times daily', 'Max duration': '7 days — if no improvement, see a doctor', 'Do not use on': 'Face, groin, or underarms for more than a few days' },
    dose_ko: { '성인 및 2세 이상': '환부에 얇게 하루 3~4회 도포', '최대 기간': '7일 — 호전되지 않으면 의사를 만나세요', '사용 금지 부위': '얼굴, 사타구니, 겨드랑이에 며칠 이상 사용 금지' },
    dose_ja: { '成人および2歳以上': '患部に1日3~4回薄く塗布', '最大期間': '7日 — 改善しない場合は医師を受診', '使用禁止部位': '顔、鼠径部、脇の数日以上の使用禁止' },
    warn_en: 'Do not use on children under 2 without doctor. Do not use on infected skin, acne, or rosacea. Long-term use can thin the skin, especially on face or sensitive areas. Do not use on large areas of the body.',
    warn_ko: '2세 미만 어린이에게는 의사 지시 없이 사용하지 마세요. 감염된 피부, 여드름, 주사피부염에 사용하지 마세요. 장기 사용은 특히 얼굴이나 민감한 부위의 피부를 얇게 만들 수 있습니다. 신체의 넓은 부위에 사용하지 마세요.',
    warn_ja: '2歳未満の小児には医師の指示なく使用しないでください。感染した皮膚、ニキビ、酒さに使用禁止。長期使用は特に顔や敏感部位の皮膚を薄くする可能性。広範囲には使用しないでください。',
    interact: [
      { en: 'Generally no significant systemic interactions at OTC strength', ko: 'OTC 농도에서 유의미한 전신 상호작용은 일반적으로 없음', ja: 'OTC濃度では一般的に有意な全身相互作用なし' }
    ],
    source: 'FDA OTC Monograph 21 CFR 347 · DailyMed (NIH)'
  },
  {
    id: 'bacitracin-neosporin',
    generic: { en: 'Bacitracin / Triple antibiotic ointment', ko: '바시트라신 / 삼중 항생제 연고', ja: 'バシトラシン / 三種抗生物質軟膏' },
    brands: ['Neosporin', 'Polysporin'],
    category: 'skin',
    uses: [
      { title_en: 'Prevent infection in minor wounds', title_ko: '경미한 상처의 감염 예방', title_ja: '軽度の傷の感染予防',
        detail_en: 'First aid to help prevent infection in minor cuts, scrapes, and burns',
        detail_ko: '경미한 베임, 찰과상, 화상의 감염 예방을 돕는 응급 처치',
        detail_ja: '軽度の切り傷、すり傷、やけどの感染予防を助ける応急処置' }
    ],
    dose_en: { 'Adult and child': 'Clean area, apply thin layer 1–3 times daily, cover with sterile bandage if desired', 'Max duration': '7 days — if no healing, see a doctor' },
    dose_ko: { '성인 및 어린이': '부위를 깨끗이 하고 얇게 하루 1~3회 도포, 원하면 멸균 붕대로 덮음', '최대 기간': '7일 — 치유되지 않으면 의사를 만나세요' },
    dose_ja: { '成人および小児': '部位を清潔にし1日1~3回薄く塗布、必要なら滅菌包帯で覆う', '最大期間': '7日 — 治癒しない場合は医師を受診' },
    warn_en: 'Do not use for more than 7 days unless directed by a doctor. Do not use on deep puncture wounds, animal bites, or serious burns — these need medical care. Neomycin (in triple antibiotic) causes allergic skin reactions in some people — if rash develops, stop use.',
    warn_ko: '의사 지시가 없으면 7일 이상 사용하지 마세요. 깊은 자상, 동물 물림, 심한 화상에는 사용하지 마세요 — 의료 처치가 필요합니다. 네오마이신(삼중 항생제에 포함)은 일부에서 알레르기성 피부 반응을 일으킵니다 — 발진이 생기면 중단하세요.',
    warn_ja: '医師の指示なく7日以上使用しないでください。深い刺し傷、動物咬傷、重度のやけどには使用禁止 — 医療処置必要。ネオマイシン(三種抗生物質含有)は一部の人にアレルギー性皮膚反応を起こします — 発疹が出たら中止。',
    interact: [
      { en: 'Minimal systemic absorption when used as directed', ko: '지시대로 사용 시 전신 흡수는 최소', ja: '指示通り使用すれば全身吸収は最小' }
    ],
    source: 'FDA OTC Monograph 21 CFR 333 · DailyMed (NIH)'
  },
  {
    id: 'miconazole',
    generic: { en: 'Miconazole / Clotrimazole', ko: '미코나졸 / 클로트리마졸', ja: 'ミコナゾール / クロトリマゾール' },
    brands: ['Lotrimin AF', 'Monistat (vaginal)', 'Desenex'],
    category: 'skin',
    uses: [
      { title_en: 'Athlete\'s foot (tinea pedis)', title_ko: '무좀 (백선)', title_ja: '水虫(白癬)',
        detail_en: 'Treats and relieves itching, burning, and cracking from athlete\'s foot',
        detail_ko: '무좀으로 인한 가려움, 작열감, 갈라짐을 치료하고 완화',
        detail_ja: '水虫によるかゆみ、灼熱感、ひび割れを治療·緩和' },
      { title_en: 'Jock itch (tinea cruris)', title_ko: '완선', title_ja: 'いんきんたむし(完癬)',
        detail_en: 'Treats jock itch in the groin area',
        detail_ko: '사타구니 부위의 완선 치료',
        detail_ja: '鼠径部のいんきんたむしを治療' },
      { title_en: 'Ringworm (tinea corporis)', title_ko: '어루러기/백선', title_ja: 'たむし(体部白癬)',
        detail_en: 'Treats ringworm on the body',
        detail_ko: '몸에 생기는 어루러기 치료',
        detail_ja: '体に生じるたむしを治療' },
      { title_en: 'Vaginal yeast infection', title_ko: '질 칸디다증', title_ja: '腟カンジダ症',
        detail_en: 'Treats vaginal candidiasis (Monistat formulations only)',
        detail_ko: '질 칸디다증 치료 (Monistat 제형에 한함)',
        detail_ja: '腟カンジダ症の治療(Monistat製剤に限る)' }
    ],
    dose_en: { 'Skin (cream/spray/powder)': 'Apply to clean, dry skin twice daily', 'Athlete\'s foot duration': '4 weeks', 'Jock itch / ringworm duration': '2 weeks', 'Vaginal': '1-, 3-, or 7-day courses per product label' },
    dose_ko: { '피부 (크림/스프레이/분말)': '깨끗하고 건조한 피부에 하루 2회 도포', '무좀 기간': '4주', '완선/어루러기 기간': '2주', '질 제품': '제품 라벨에 따라 1일·3일·7일 요법' },
    dose_ja: { '皮膚(クリーム/スプレー/パウダー)': '清潔で乾燥した皮膚に1日2回塗布', '水虫期間': '4週間', 'いんきんたむし/たむし期間': '2週間', '腟製剤': '製品ラベルに従い1日·3日·7日療法' },
    warn_en: 'Do not use in or near the eyes. For vaginal products: if this is your first yeast infection, see a doctor to confirm diagnosis — many other conditions have similar symptoms. See a doctor if no improvement in 2 weeks for skin or 3 days for vaginal use.',
    warn_ko: '눈이나 눈 주변에 사용하지 마세요. 질 제품의 경우: 처음 칸디다증이라면 의사에게 진단 확인을 받으세요 — 다른 많은 질환이 비슷한 증상을 보입니다. 피부는 2주, 질은 3일 이내 호전되지 않으면 의사를 만나세요.',
    warn_ja: '目や目の近くには使用しないでください。腟製剤の場合:初めてのカンジダ症なら医師に診断確認を — 多くの他疾患も類似症状を呈します。皮膚は2週間、腟は3日以内に改善しない場合は医師を受診。',
    interact: [
      { en: 'Vaginal miconazole can weaken latex condoms and diaphragms — use alternate contraception during treatment', ko: '질용 미코나졸은 라텍스 콘돔과 다이어프램을 약화시킬 수 있음 — 치료 중 대체 피임법 사용', ja: '腟用ミコナゾールはラテックスコンドームとダイアフラムを弱める可能性 — 治療中は代替避妊法' },
      { en: 'Vaginal product may increase warfarin effect (rare but possible)', ko: '질 제품은 와파린 효과를 증가시킬 수 있음 (드물지만 가능)', ja: '腟製剤はワーファリン効果を増加させる可能性(稀だが起こり得る)' }
    ],
    source: 'FDA OTC Monograph 21 CFR 333 · DailyMed (NIH)'
  },
  {
    id: 'benzoyl-peroxide',
    generic: { en: 'Benzoyl peroxide', ko: '벤조일 퍼옥사이드', ja: '過酸化ベンゾイル' },
    brands: ['PanOxyl', 'Clean & Clear Persa-Gel'],
    category: 'skin',
    uses: [
      { title_en: 'Acne treatment', title_ko: '여드름 치료', title_ja: 'ニキビ治療',
        detail_en: 'Treats acne blemishes, including pimples and blackheads; also helps prevent new acne',
        detail_ko: '여드름(구진·면포) 치료; 새로운 여드름 예방에도 도움',
        detail_ja: 'ニキビ(丘疹·面皰)を治療;新しいニキビの予防にも役立つ' }
    ],
    dose_en: { 'Adult and child 12+': 'Apply 2.5%, 5%, or 10% to affected area once daily at first, then increase to 2–3 times daily if tolerated', 'Start low': 'Begin with 2.5% to reduce irritation — equally effective as higher strengths' },
    dose_ko: { '성인 및 12세 이상': '환부에 2.5%, 5% 또는 10%를 처음에는 하루 1회 도포, 내약성이 있으면 하루 2~3회로 증량', '저농도 시작': '자극을 줄이기 위해 2.5%로 시작 — 고농도와 효과는 동일' },
    dose_ja: { '成人および12歳以上': '患部に2.5%、5%または10%をまず1日1回塗布、忍容性があれば1日2~3回に増量', '低濃度開始': '刺激軽減のため2.5%から開始 — 高濃度と効果は同等' },
    warn_en: 'Apply only to acne areas. Avoid eyes, lips, and mouth. Bleaches fabric, hair, and towels permanently — use white towels. May cause redness, dryness, peeling, or increased sun sensitivity — use sunscreen. Rare but serious allergic reaction possible (throat tightness, face swelling, hives) — stop and seek emergency care.',
    warn_ko: '여드름 부위에만 도포하세요. 눈, 입술, 입을 피하세요. 천, 머리카락, 수건을 영구적으로 탈색시킵니다 — 흰 수건을 사용하세요. 발적, 건조, 각질, 햇빛 민감도 증가를 유발할 수 있으므로 자외선 차단제를 사용하세요. 드물지만 심각한 알레르기 반응 가능 (목 조임, 얼굴 부종, 두드러기) — 중단하고 응급 진료를 받으세요.',
    warn_ja: 'ニキビ部位のみに塗布。目、唇、口を避ける。布、髪、タオルを永久に脱色 — 白いタオルを使用。発赤、乾燥、皮むけ、日光過敏増加の可能性 — 日焼け止めを使用。稀だが重篤なアレルギー反応の可能性(のどの締め付け、顔面腫脹、じんま疹) — 中止し救急受診。',
    interact: [
      { en: 'Topical retinoids (tretinoin, adapalene) — may increase irritation if used together', ko: '국소 레티노이드 (트레티노인, 아다팔렌) — 함께 사용 시 자극 증가 가능', ja: '外用レチノイド(トレチノイン、アダパレン) — 併用で刺激増加の可能性' },
      { en: 'Other drying acne products — excessive skin irritation', ko: '건조를 유발하는 다른 여드름 제품 — 과도한 피부 자극', ja: '乾燥を起こす他のニキビ製品 — 過度の皮膚刺激' }
    ],
    source: 'FDA OTC Monograph 21 CFR 333D · DailyMed (NIH)'
  },

  // ============ OTHER ============
  {
    id: 'melatonin',
    generic: { en: 'Melatonin', ko: '멜라토닌', ja: 'メラトニン' },
    brands: ['Natrol', 'Nature Made', 'ZzzQuil Pure Zzzs'],
    category: 'supplement',
    uses: [
      { title_en: 'Short-term sleep onset', title_ko: '단기 수면 유도', title_ja: '短期間の入眠促進', evidence: 'emerging',
        detail_en: 'May help fall asleep faster, especially when sleep schedule is shifted (jet lag, shift work). Effect on total sleep time is small.',
        detail_ko: '특히 수면 일정이 바뀌었을 때(시차, 교대 근무) 더 빨리 잠드는 데 도움이 될 수 있습니다. 총 수면 시간에 대한 효과는 작습니다.',
        detail_ja: '特に睡眠スケジュールがずれた時(時差、交代勤務)に早く寝付くのに役立つ可能性。総睡眠時間への効果は小さい。' },
      { title_en: 'Jet lag', title_ko: '시차 적응', title_ja: '時差ぼけ', evidence: 'emerging',
        detail_en: 'Taken at destination bedtime for several nights after travel across 2+ time zones',
        detail_ko: '2개 이상 시간대를 가로지르는 여행 후 현지 취침 시간에 며칠간 복용',
        detail_ja: '2つ以上のタイムゾーンを越える旅行後、現地の就寝時間に数晩服用' }
    ],
    dose_en: { 'Adult': '0.5–5 mg taken 30–60 minutes before bedtime', 'Start low': 'Lower doses (0.5–1 mg) often work as well as higher doses', 'Regulatory note': 'Sold as a dietary supplement in the US — NOT FDA-approved as a drug; quality varies by brand' },
    dose_ko: { '일반 용량': '취침 30~60분 전 0.5~5 mg', '저용량 시작': '저용량(0.5~1 mg)도 고용량만큼 효과적일 때가 많음', '품질': 'USP 인증 제품을 선택 — 라벨 정확도가 브랜드마다 크게 다름' },
    dose_ja: { '一般用量': '就寝30~60分前に0.5~5 mg', '低用量から開始': '低用量(0.5~1 mg)も高用量と同等以上に有効なことが多い', '規制上の注意': '米国では栄養補助食品として販売 — FDAの医薬品承認なし;品質はブランドにより異なる' },
    overuse_en: '10 MG IS NOT "STRONGER" — Korean pharmacies and online sellers promote 10 mg melatonin as "extra strength." Studies show 0.3–1 mg works as well or better than 10 mg, and high doses often cause next-day grogginess, headaches, and nightmares. Children should only use melatonin with doctor guidance — 2022 AAP data shows emergency room visits for accidental pediatric melatonin overdose increased 530% from 2012–2021. Keep melatonin gummies out of children\'s reach. Also, many Korean supplements combine melatonin with magnesium, L-theanine, and valerian — this stacking has not been tested for safety. Use melatonin alone, at the lowest effective dose, and avoid nightly long-term use.',
    overuse_ko: '10 mg가 "더 강한" 것이 아닙니다 — 한인 약국과 온라인 판매자가 10 mg 멜라토닌을 "고용량"으로 홍보합니다. 연구에 따르면 0.3~1 mg이 10 mg만큼 또는 더 효과적이며, 고용량은 다음날 멍한 느낌, 두통, 악몽을 자주 일으킵니다. 어린이는 의사 지시 하에만 사용해야 합니다 — 2022년 미국소아과학회 데이터에서 2012~2021년 사이 어린이 우발적 멜라토닌 과다복용 응급실 방문이 530% 증가했습니다. 멜라토닌 구미를 어린이 손이 닿지 않는 곳에 보관하세요. 또한 많은 한인 보충제가 멜라토닌을 마그네슘, L-테아닌, 쥐오줌풀과 혼합하는데, 이런 조합은 안전성 검증이 되지 않았습니다. 멜라토닌 단독으로, 효과가 나타나는 최저 용량으로 복용하고 매일 밤 장기 사용은 피하세요.',
    overuse_ja: '10 mgが「より強力」ではない — 韓国の薬局やネット販売者が10 mgメラトニンを「高用量」として宣伝しています。研究では0.3~1 mgが10 mgと同等以上に有効であり、高用量は翌日のぼーっとした感じ、頭痛、悪夢をしばしば引き起こします。小児は医師の指導下でのみ使用 — 2022年AAPデータで2012~2021年の小児偶発的メラトニン過量服用の救急受診が530%増加。メラトニングミは小児の手の届かない場所に保管。多くの韓国系サプリがメラトニンをマグネシウム、L-テアニン、バレリアンと混合しますが、この組み合わせの安全性は検証されていません。メラトニン単独で、最低有効量で服用し、毎晩長期使用は避けてください。',
    warn_en: 'A 2017 study found many melatonin products contained 80–500% of the labeled amount. Look for USP-verified products. Not recommended for children or pregnant women without doctor approval. Can cause drowsiness, headache, vivid dreams, and next-day grogginess. Long-term safety (beyond 3 months) is not well-studied.',
    warn_ko: '2017년 연구에서 많은 멜라토닌 제품이 라벨 표기량의 80~500%를 함유한 것으로 밝혀졌습니다. USP 인증 제품을 찾으세요. 어린이나 임산부는 의사 승인 없이 권장되지 않습니다. 졸음, 두통, 생생한 꿈, 다음날 멍한 느낌을 유발할 수 있습니다. 3개월 이상의 장기 안전성은 충분히 연구되지 않았습니다.',
    warn_ja: '2017年の研究で多くのメラトニン製品が表示量の80~500%を含有していることが判明。USP認証製品を選んでください。小児·妊婦は医師の承認なく推奨されません。眠気、頭痛、鮮明な夢、翌日のぼーっとした感じを引き起こす可能性。3か月超の長期安全性は十分に研究されていません。',
    interact: [
      { en: 'Blood thinners (warfarin) — may increase bleeding risk', ko: '혈액 희석제 (와파린) — 출혈 위험 증가 가능', ja: '抗凝固薬(ワーファリン) — 出血リスク増加の可能性' },
      { en: 'Sedatives, alcohol — increased drowsiness', ko: '진정제, 알코올 — 졸음 증가', ja: '鎮静薬、アルコール — 眠気増加' },
      { en: 'Blood pressure medications — may alter effect', ko: '혈압약 — 효과 변화 가능', ja: '降圧薬 — 効果変動の可能性' },
      { en: 'Immunosuppressants — may counteract effect', ko: '면역 억제제 — 효과 상쇄 가능', ja: '免疫抑制薬 — 効果相殺の可能性' }
    ],
    source: 'NIH Office of Dietary Supplements · MedlinePlus (NIH)'
  },
  {
    id: 'vitamin-d',
    generic: { en: 'Vitamin D3 (cholecalciferol)', ko: '비타민 D3 (콜레칼시페롤)', ja: 'ビタミンD3(コレカルシフェロール)' },
    brands: ['Nature Made', 'Kirkland', 'NOW Foods'],
    category: 'supplement',
    uses: [
      { title_en: 'Bone health (with calcium)', title_ko: '뼈 건강 (칼슘과 함께)', title_ja: '骨の健康(カルシウムと共に)', evidence: 'strong',
        detail_en: 'Needed for calcium absorption and bone mineralization; helps prevent osteoporosis and falls in older adults',
        detail_ko: '칼슘 흡수와 뼈 미네랄화에 필요하며, 고령자의 골다공증과 낙상 예방에 도움',
        detail_ja: 'カルシウム吸収と骨石灰化に必要;高齢者の骨粗鬆症と転倒予防に役立つ' },
      { title_en: 'Correction of vitamin D deficiency', title_ko: '비타민 D 결핍 교정', title_ja: 'ビタミンD欠乏の是正', evidence: 'strong',
        detail_en: 'Treats low blood levels of 25-hydroxyvitamin D (<20 ng/mL), which is common in adults who get little sun',
        detail_ko: '혈중 25-수산화비타민 D 저하(<20 ng/mL) 치료 — 햇빛 노출이 적은 성인에서 흔함',
        detail_ja: '血中25-ヒドロキシビタミンD低値(<20 ng/mL)の治療 — 日光曝露の少ない成人に多い' },
      { title_en: 'Muscle function in older adults', title_ko: '고령자 근육 기능', title_ja: '高齢者の筋機能', evidence: 'emerging',
        detail_en: 'May reduce falls and improve muscle strength in older adults with low vitamin D',
        detail_ko: '비타민 D가 낮은 고령자에서 낙상 감소 및 근력 개선 가능',
        detail_ja: 'ビタミンDが低い高齢者で転倒減少と筋力改善の可能性' }
    ],
    dose_en: { 'Maintenance (adult)': '600–800 IU (15–20 mcg) daily', 'Adult over 70': '800 IU daily (higher need)', 'Deficiency treatment': 'Doctor may prescribe 1000–5000 IU daily short-term', 'Upper limit': '4000 IU/day without doctor supervision' },
    dose_ko: { '유지 (성인)': '하루 600~800 IU (15~20 mcg)', '70세 이상': '하루 800 IU (필요량 증가)', '결핍 치료': '의사가 단기간 하루 1000~5000 IU 처방 가능', '상한': '의사 감독 없이 하루 4000 IU 이하' },
    dose_ja: { '維持(成人)': '1日600~800 IU(15~20 mcg)', '70歳以上': '1日800 IU(必要量増加)', '欠乏治療': '医師が短期間1日1000~5000 IU処方可能', '上限': '医師の監督なく1日4000 IU以下' },
    overuse_en: 'KOREAN HOUSEHOLDS OFTEN TAKE 5000–10000 IU DAILY — believing "more = stronger bones" or following Korean media recommendations. This is dangerous. Vitamin D is FAT-SOLUBLE and accumulates. High-dose long-term use causes hypercalcemia: kidney stones, kidney damage, confusion, muscle weakness, heart rhythm problems. Elderly Korean women who take 5000 IU daily + calcium supplements are at high risk. Get blood 25-OH vitamin D tested (ask doctor for "비타민 D 검사") — most deficiencies resolve with 1000–2000 IU daily within 3 months. Do not self-dose above 4000 IU.',
    overuse_ko: '한인 가정에서 하루 5000~10000 IU 복용이 흔함 — "많을수록 뼈가 튼튼"하다는 믿음이나 한국 언론 권고를 따라서입니다. 이는 위험합니다. 비타민 D는 지용성이라 체내에 축적됩니다. 고용량 장기 복용은 고칼슘혈증을 유발합니다: 신장 결석, 신장 손상, 혼돈, 근육 약화, 부정맥. 하루 5000 IU + 칼슘 보충제를 함께 복용하는 고령 한인 여성들이 고위험군입니다. 혈중 25-OH 비타민 D 검사를 받으세요 ("비타민 D 검사"라고 의사에게 요청). 대부분의 결핍은 하루 1000~2000 IU로 3개월 내 회복됩니다. 하루 4000 IU 초과 자가 복용은 피하세요.',
    overuse_ja: '韓国系家庭で1日5000~10000 IUの服用が多い — 「多いほど骨が強くなる」という信念や韓国メディアの推奨に従って。これは危険です。ビタミンDは脂溶性で体内に蓄積します。高用量長期使用は高カルシウム血症を引き起こします:腎結石、腎障害、混乱、筋力低下、不整脈。1日5000 IU+カルシウムサプリを併用する高齢韓国系女性は高リスク群。血中25-OHビタミンD検査を受けてください(医師に「ビタミンD検査」と依頼)。ほとんどの欠乏は1日1000~2000 IUで3か月以内に回復します。1日4000 IU超の自己服用は避けてください。',
    warn_en: 'Doses above 4000 IU/day long-term can cause dangerously high calcium (hypercalcemia), leading to kidney stones, weakness, or confusion. Have your doctor check blood levels before taking high doses. Fat-soluble — takes weeks to see effect.',
    warn_ko: '하루 4000 IU 이상을 장기간 복용하면 위험한 고칼슘혈증을 유발하여 신장 결석, 무력감, 혼돈을 일으킬 수 있습니다. 고용량 복용 전 의사에게 혈중 농도를 확인받으세요. 지용성 — 효과가 나타나는 데 몇 주가 걸립니다.',
    warn_ja: '1日4000 IU超を長期服用すると危険な高カルシウム血症を引き起こし、腎結石、脱力感、混乱を起こす可能性があります。高用量服用前に医師に血中濃度を確認してもらってください。脂溶性 — 効果発現まで数週間かかります。',
    interact: [
      { en: 'Thiazide diuretics — increased risk of high calcium', ko: '티아지드 이뇨제 — 고칼슘혈증 위험 증가', ja: 'チアジド系利尿薬 — 高カルシウム血症リスク増加' },
      { en: 'Digoxin — hypercalcemia can trigger heart rhythm problems', ko: '디곡신 — 고칼슘혈증이 부정맥을 유발 가능', ja: 'ジゴキシン — 高カルシウム血症が不整脈を誘発の可能性' },
      { en: 'Steroids (prednisone) — reduce vitamin D activity', ko: '스테로이드 (프레드니손) — 비타민 D 활성 감소', ja: 'ステロイド(プレドニゾン) — ビタミンD活性低下' }
    ],
    source: 'NIH Office of Dietary Supplements — Vitamin D Fact Sheet'
  },
  {
    id: 'vitamin-b12',
    generic: { en: 'Vitamin B12 (cyanocobalamin / methylcobalamin)', ko: '비타민 B12 (시아노코발라민 / 메틸코발라민)', ja: 'ビタミンB12(シアノコバラミン / メチルコバラミン)' },
    brands: ['Nature Made', 'Jarrow Methyl B-12'],
    category: 'supplement',
    uses: [
      { title_en: 'Correction of B12 deficiency', title_ko: 'B12 결핍 교정', title_ja: 'B12欠乏の是正', evidence: 'strong',
        detail_en: 'Treats deficiency-related anemia (megaloblastic) and neurological symptoms like numbness, tingling, or memory problems',
        detail_ko: '결핍으로 인한 빈혈(거대적아구성) 및 저림, 따끔거림, 기억력 문제 같은 신경학적 증상 치료',
        detail_ja: '欠乏による貧血(巨赤芽球性)およびしびれ、ピリピリ、記憶障害などの神経症状の治療' },
      { title_en: 'Support for vegetarians and vegans', title_ko: '채식·비건 보충', title_ja: 'ベジタリアン·ヴィーガンの補給', evidence: 'strong',
        detail_en: 'Required because B12 is not reliably found in plant foods',
        detail_ko: 'B12는 식물성 식품에서 안정적으로 얻을 수 없으므로 필요',
        detail_ja: 'B12は植物性食品では安定して得られないため必要' },
      { title_en: 'Support for adults over 50', title_ko: '50세 이상 성인 보충', title_ja: '50歳以上成人の補給', evidence: 'strong',
        detail_en: 'NIH recommends B12 from supplements or fortified foods after age 50 due to reduced absorption from food',
        detail_ko: 'NIH는 50세 이후 음식 흡수 감소 때문에 보충제나 강화 식품으로 B12 섭취를 권장',
        detail_ja: 'NIHは50歳以降は食物吸収低下のためサプリや強化食品でのB12摂取を推奨' }
    ],
    dose_en: { 'Adult RDA': '2.4 mcg daily; supplements typically 500–1000 mcg daily', 'Over age 50': 'Supplement or fortified foods recommended', 'Deficiency': 'Doctor may prescribe injection or high-dose oral (1000–2000 mcg daily)' },
    dose_ko: { '성인 RDA': '하루 2.4 mcg; 보충제는 보통 하루 500~1000 mcg', '50세 이상': '보충제나 강화 식품 권장', '결핍': '의사가 주사 또는 고용량 경구(하루 1000~2000 mcg) 처방 가능' },
    dose_ja: { '成人RDA': '1日2.4 mcg;サプリは通常1日500~1000 mcg', '50歳以上': 'サプリまたは強化食品推奨', '欠乏': '医師が注射または高用量経口(1日1000~2000 mcg)処方可能' },
    warn_en: 'Very safe — water-soluble, excess is excreted in urine. If you have unexplained fatigue, numbness, or memory problems, see a doctor for a B12 blood test before guessing. Metformin (diabetes drug) and long-term PPIs (omeprazole) can lower B12 — check levels.',
    warn_ko: '매우 안전 — 수용성이라 과잉분은 소변으로 배출됩니다. 원인 불명의 피로, 저림, 기억력 문제가 있으면 추측하지 말고 의사에게 B12 혈액 검사를 받으세요. 메트포르민(당뇨약)과 장기 PPI(오메프라졸)는 B12를 낮출 수 있으니 수치 확인 필요.',
    warn_ja: '非常に安全 — 水溶性で過剰分は尿排泄。原因不明の疲労、しびれ、記憶障害があれば推測せず医師にB12血液検査を依頼。メトホルミン(糖尿病薬)と長期PPI(オメプラゾール)はB12を低下させる可能性 — 濃度確認必要。',
    interact: [
      { en: 'Metformin — reduces B12 absorption (check level yearly)', ko: '메트포르민 — B12 흡수 감소 (매년 수치 확인)', ja: 'メトホルミン — B12吸収減少(毎年濃度確認)' },
      { en: 'Proton pump inhibitors (omeprazole) — reduce absorption with long-term use', ko: '양성자 펌프 억제제 (오메프라졸) — 장기 사용 시 흡수 감소', ja: 'プロトンポンプ阻害薬(オメプラゾール) — 長期使用で吸収減少' },
      { en: 'H2 blockers (famotidine) — may reduce absorption', ko: 'H2 차단제 (파모티딘) — 흡수 감소 가능', ja: 'H2ブロッカー(ファモチジン) — 吸収減少の可能性' }
    ],
    source: 'NIH Office of Dietary Supplements — Vitamin B12 Fact Sheet'
  },
  {
    id: 'vitamin-c',
    generic: { en: 'Vitamin C (ascorbic acid)', ko: '비타민 C (아스코르브산)', ja: 'ビタミンC(アスコルビン酸)' },
    brands: ['Nature Made', 'Emergen-C', 'Airborne'],
    category: 'supplement',
    uses: [
      { title_en: 'Correction of vitamin C deficiency (scurvy)', title_ko: '비타민 C 결핍 (괴혈병) 교정', title_ja: 'ビタミンC欠乏(壊血病)の是正', evidence: 'strong',
        detail_en: 'Required to prevent and treat scurvy (bleeding gums, poor wound healing, weakness)',
        detail_ko: '괴혈병(잇몸 출혈, 상처 치유 불량, 무력감) 예방 및 치료에 필요',
        detail_ja: '壊血病(歯ぐき出血、創傷治癒不良、脱力)の予防·治療に必要' },
      { title_en: 'Antioxidant and general nutrition', title_ko: '항산화·일반 영양', title_ja: '抗酸化·一般栄養', evidence: 'strong',
        detail_en: 'Supports collagen production, iron absorption from plants, and immune cell function',
        detail_ko: '콜라겐 생성, 식물성 철분 흡수, 면역 세포 기능 지원',
        detail_ja: 'コラーゲン産生、植物性鉄の吸収、免疫細胞機能をサポート' },
      { title_en: 'Duration of common cold', title_ko: '감기 지속 기간', title_ja: '感冒の罹病期間', evidence: 'limited',
        detail_en: 'Taken regularly (not at cold onset), may shorten cold duration by about 8% in adults. Does not prevent colds in most people.',
        detail_ko: '감기 시작 시점이 아닌 평소 복용 시 성인에서 감기 기간을 약 8% 단축 가능. 대부분의 사람에서 감기를 예방하지는 못함.',
        detail_ja: '感冒発症時ではなく日常的に服用すれば成人で罹病期間を約8%短縮の可能性。ほとんどの人で予防はできない。' }
    ],
    dose_en: { 'Adult RDA': '75 mg (women) / 90 mg (men) daily', 'Typical supplement': '250–1000 mg daily', 'Upper limit': '2000 mg/day to avoid GI upset', 'Smokers': 'Need +35 mg/day' },
    dose_ko: { '성인 RDA': '하루 75 mg (여성) / 90 mg (남성)', '일반 보충': '하루 250~1000 mg', '상한': '하루 2000 mg 이하 (위장 장애 예방)', '흡연자': '하루 +35 mg 추가 필요' },
    dose_ja: { '成人RDA': '1日75 mg(女性)/90 mg(男性)', '一般的なサプリ': '1日250~1000 mg', '上限': '1日2000 mg以下(消化器障害予防)', '喫煙者': '1日+35 mg追加必要' },
    overuse_en: '"MEGA-DOSE PREVENTS COLDS" MYTH — Taking 3000–10000 mg daily is common in Korean households, often promoted by Korean "health influencers." NIH data is clear: doses above 2000 mg/day cause diarrhea, nausea, abdominal cramps, and increased kidney stone risk (especially in men). Vitamin C does NOT prevent colds in most people — only shortens duration by about 8% when taken daily before infection. Also, sudden high-dose stopping can cause "rebound scurvy." IV vitamin C drips at naturopathic clinics (정맥 비타민 C 주사) are not FDA-approved for general health and have caused kidney failure in people with G6PD deficiency.',
    overuse_ko: '"메가도즈가 감기를 예방한다"는 신화 — 한국 "건강 인플루언서"들이 권장하여 한인 가정에서 하루 3000~10000 mg 복용이 흔합니다. NIH 데이터는 명확합니다: 하루 2000 mg 초과 시 설사, 메스꺼움, 복통, 신장 결석 위험 증가 (특히 남성). 비타민 C는 대부분 사람의 감기를 예방하지 않으며, 감염 전 매일 복용 시 기간을 약 8% 단축시킬 뿐입니다. 또한 갑자기 고용량을 중단하면 "반동성 괴혈병"이 올 수 있습니다. 자연요법 클리닉의 정맥 비타민 C 주사는 일반 건강용으로 FDA 승인되지 않았으며, G6PD 결핍자에게서 신부전을 유발한 사례가 있습니다.',
    overuse_ja: '「メガドーズで風邪予防」という神話 — 韓国の「健康インフルエンサー」の推奨で韓国系家庭で1日3000~10000 mgの服用が多い。NIHデータは明確:1日2000 mg超は下痢、吐き気、腹痛、腎結石リスク増加(特に男性)。ビタミンCはほとんどの人で風邪を予防せず、感染前に毎日服用した場合に期間を約8%短縮するのみ。突然の高用量中止で「反動性壊血病」の可能性。自然療法クリニックの静注ビタミンCは一般健康目的でFDA承認されておらず、G6PD欠損者で腎不全を起こした事例あり。',
    warn_en: 'Doses above 2000 mg/day can cause diarrhea, nausea, and stomach cramps. High doses may increase kidney stone risk. People with hemochromatosis (iron overload) should avoid high doses.',
    warn_ko: '하루 2000 mg 이상은 설사, 메스꺼움, 복통을 유발할 수 있습니다. 고용량은 신장 결석 위험을 증가시킬 수 있습니다. 혈색소증(철분 과잉) 환자는 고용량을 피해야 합니다.',
    warn_ja: '1日2000 mg超は下痢、吐き気、腹痛を起こす可能性。高用量は腎結石リスク増加。ヘモクロマトーシス(鉄過剰)患者は高用量回避。',
    interact: [
      { en: 'Iron supplements — vitamin C increases iron absorption (usually desired, but problematic in hemochromatosis)', ko: '철분제 — 비타민 C가 철분 흡수를 증가시킴 (일반적으로 바람직하나 혈색소증에는 문제)', ja: '鉄剤 — ビタミンCが鉄吸収増加(通常は望ましいがヘモクロマトーシスでは問題)' },
      { en: 'Chemotherapy — may reduce effectiveness of some treatments (ask oncologist)', ko: '항암제 — 일부 치료 효과를 감소시킬 수 있음 (종양내과 상담)', ja: '化学療法 — 一部の治療効果を減少の可能性(腫瘍内科に相談)' },
      { en: 'Warfarin — high doses may reduce effect', ko: '와파린 — 고용량은 효과 감소 가능', ja: 'ワーファリン — 高用量で効果減少の可能性' }
    ],
    source: 'NIH Office of Dietary Supplements — Vitamin C Fact Sheet'
  },
  {
    id: 'magnesium',
    generic: { en: 'Magnesium', ko: '마그네슘', ja: 'マグネシウム' },
    brands: ['Nature Made', 'Natural Vitality Calm', 'Doctor\'s Best'],
    category: 'supplement',
    uses: [
      { title_en: 'Correction of magnesium deficiency', title_ko: '마그네슘 결핍 교정', title_ja: 'マグネシウム欠乏の是正', evidence: 'strong',
        detail_en: 'Treats low magnesium (common in people on diuretics, PPIs, or with diabetes, alcoholism, or chronic diarrhea)',
        detail_ko: '저마그네슘혈증 치료 (이뇨제, PPI 복용자, 당뇨·알코올중독·만성 설사 환자에서 흔함)',
        detail_ja: '低マグネシウム血症の治療(利尿薬、PPI使用者、糖尿病·アルコール依存·慢性下痢患者に多い)' },
      { title_en: 'Constipation (magnesium citrate/hydroxide)', title_ko: '변비 (구연산/수산화 마그네슘)', title_ja: '便秘(クエン酸/水酸化マグネシウム)', evidence: 'strong',
        detail_en: 'Works as an osmotic laxative; draws water into the bowel',
        detail_ko: '삼투성 하제로 작용; 장으로 수분을 끌어들임',
        detail_ja: '浸透圧性下剤として作用;腸に水分を引き込む' },
      { title_en: 'Muscle cramps and sleep quality', title_ko: '근육 경련·수면 질', title_ja: '筋けいれん·睡眠の質', evidence: 'limited',
        detail_en: 'Often used for leg cramps and mild sleep issues; evidence is mixed but side effects are minimal at normal doses',
        detail_ko: '다리 경련과 경미한 수면 문제에 흔히 사용; 근거는 혼재되어 있으나 일반 용량에서 부작용은 적음',
        detail_ja: '下肢のけいれんや軽度の睡眠問題によく使用;エビデンスは混在するが通常用量では副作用は最小' }
    ],
    dose_en: { 'Adult RDA': '310–420 mg daily (from food + supplement)', 'Supplement upper limit': '350 mg/day of supplemental magnesium (food does not count)', 'Forms': 'Citrate, glycinate — better absorbed; oxide — cheaper but more GI side effects' },
    dose_ko: { '성인 RDA': '하루 310~420 mg (음식 + 보충제)', '보충제 상한': '보충제로 하루 350 mg (음식은 해당 안 됨)', '형태': '구연산염, 글리신산염 — 흡수 양호; 산화물 — 저렴하나 위장 부작용 많음' },
    dose_ja: { '成人RDA': '1日310~420 mg(食事+サプリ)', 'サプリ上限': 'サプリで1日350 mg(食事は含まない)', '形態': 'クエン酸塩、グリシン酸塩 — 吸収良好;酸化物 — 安価だが消化器副作用多い' },
    overuse_en: 'KIDNEY PATIENTS AT SEVERE RISK — Many older Koreans with early kidney disease (common with diabetes, hypertension) take magnesium for "leg cramps" or "sleep" without knowing their kidney function. Magnesium is cleared by the kidneys; in CKD patients, even moderate doses cause toxic buildup: dangerously slow heartbeat, low blood pressure, muscle paralysis, cardiac arrest. Also, "magnesium for sleep" TikTok/Instagram trends have led people to take 1000–2000 mg nightly — this causes severe diarrhea and electrolyte imbalance. If you are over 60, diabetic, or on blood pressure medications, have your kidney function (eGFR) checked before supplementing.',
    overuse_ko: '신장 환자는 심각한 위험 — 초기 신장 질환(당뇨·고혈압에서 흔함)이 있는 많은 한인 고령자가 자신의 신장 기능을 모른 채 "다리 경련"이나 "수면용"으로 마그네슘을 복용합니다. 마그네슘은 신장으로 배출되며, 만성 신장질환 환자는 중등도 용량에서도 독성 축적이 일어나 위험한 서맥, 저혈압, 근육 마비, 심정지를 일으킵니다. 또한 "수면용 마그네슘" SNS 트렌드로 매일 밤 1000~2000 mg 복용하는 경우도 있는데, 이는 심한 설사와 전해질 불균형을 유발합니다. 60세 이상, 당뇨, 혈압약 복용 중이면 보충 전 신장 기능(eGFR) 확인을 받으세요.',
    overuse_ja: '腎臓病患者は深刻なリスク — 早期腎疾患(糖尿病·高血圧でよくある)を持つ多くの韓国系高齢者が自身の腎機能を知らないまま「下肢けいれん」や「睡眠用」にマグネシウムを服用。マグネシウムは腎排泄され、CKD患者では中等度用量でも毒性蓄積:危険な徐脈、低血圧、筋麻痺、心停止。また「睡眠用マグネシウム」SNSトレンドで毎晩1000~2000 mg服用する例もあり、これは重度の下痢と電解質不均衡を起こします。60歳以上、糖尿病、降圧薬服用中なら補給前に腎機能(eGFR)確認を。',
    danger_en: 'KIDNEY DISEASE RISK — if your kidneys do not work well, magnesium can build up to dangerous levels causing heart rhythm problems, low blood pressure, and weakness. Talk to your doctor before supplementing if you have kidney disease.',
    danger_ko: '신장 질환 위험 — 신장 기능이 저하된 경우 마그네슘이 위험한 수준으로 축적되어 부정맥, 저혈압, 무력감을 일으킬 수 있습니다. 신장 질환이 있으면 보충 전 의사와 상담하세요.',
    danger_ja: '腎疾患リスク — 腎機能低下時はマグネシウムが危険なレベルまで蓄積し、不整脈、低血圧、脱力を起こす可能性。腎疾患があれば補給前に医師に相談。',
    warn_en: 'Common side effects are diarrhea and stomach cramps, especially with magnesium oxide. If this happens, switch to glycinate or reduce dose.',
    warn_ko: '흔한 부작용은 설사와 복통이며, 특히 산화마그네슘에서 잘 나타납니다. 이 경우 글리신산염으로 바꾸거나 용량을 줄이세요.',
    warn_ja: '一般的な副作用は下痢と腹痛、特に酸化マグネシウムで顕著。その場合はグリシン酸塩に切り替えるか減量。',
    interact: [
      { en: 'Antibiotics (tetracyclines, quinolones) — reduces absorption of both (separate by 2 hours)', ko: '항생제 (테트라사이클린, 퀴놀론) — 둘 다 흡수 감소 (2시간 간격 필요)', ja: '抗生物質(テトラサイクリン、キノロン) — 両方の吸収減少(2時間間隔必要)' },
      { en: 'Bisphosphonates (osteoporosis drugs) — reduced absorption', ko: '비스포스포네이트 (골다공증약) — 흡수 감소', ja: 'ビスホスホネート(骨粗鬆症薬) — 吸収減少' },
      { en: 'Diuretics — may change magnesium levels', ko: '이뇨제 — 마그네슘 수치 변화 가능', ja: '利尿薬 — マグネシウム濃度変動の可能性' }
    ],
    source: 'NIH Office of Dietary Supplements — Magnesium Fact Sheet'
  },
  {
    id: 'calcium',
    generic: { en: 'Calcium (with vitamin D)', ko: '칼슘 (비타민 D 포함)', ja: 'カルシウム(ビタミンD配合)' },
    brands: ['Citracal', 'Caltrate', 'Os-Cal'],
    category: 'supplement',
    uses: [
      { title_en: 'Bone health and osteoporosis prevention', title_ko: '뼈 건강 및 골다공증 예방', title_ja: '骨の健康·骨粗鬆症予防', evidence: 'strong',
        detail_en: 'Helps maintain bone mineral density, especially in postmenopausal women and older adults',
        detail_ko: '골밀도 유지에 도움, 특히 폐경 후 여성 및 고령자',
        detail_ja: '骨密度維持を助ける、特に閉経後女性·高齢者' },
      { title_en: 'Correction of calcium deficiency', title_ko: '칼슘 결핍 교정', title_ja: 'カルシウム欠乏の是正', evidence: 'strong',
        detail_en: 'Treats low calcium in blood, often from inadequate intake or vitamin D deficiency',
        detail_ko: '부족한 섭취나 비타민 D 결핍으로 인한 저칼슘혈증 치료',
        detail_ja: '不十分な摂取やビタミンD欠乏による低カルシウム血症の治療' }
    ],
    dose_en: { 'Adult RDA': '1000–1200 mg daily (food + supplement combined)', 'Per dose': 'Absorption is best with 500 mg or less at a time — split doses', 'Forms': 'Citrate — absorbed well with or without food; Carbonate — take with food', 'Upper limit': '2500 mg/day total (2000 mg over age 50)' },
    dose_ko: { '성인 RDA': '하루 1000~1200 mg (음식 + 보충제 합산)', '1회 복용': '1회 500 mg 이하로 나누어 복용 시 흡수 최적', '형태': '구연산염 — 식사 유무 관계없이 흡수 양호; 탄산염 — 식사와 함께 복용', '상한': '하루 총 2500 mg (50세 이상은 2000 mg)' },
    dose_ja: { '成人RDA': '1日1000~1200 mg(食事+サプリ合計)', '1回服用': '1回500 mg以下に分割で吸収最適', '形態': 'クエン酸塩 — 食事と無関係に吸収良好;炭酸塩 — 食事と共に服用', '上限': '1日合計2500 mg(50歳以上は2000 mg)' },
    overuse_en: 'ADDING CALCIUM TO A CALCIUM-RICH DIET IS HARMFUL — Many Korean postmenopausal women take 1000+ mg calcium daily "for bones" while also eating dairy, anchovies (멸치), tofu (두부), and leafy greens. This pushes total intake over 2000 mg/day, which is linked to increased heart attack risk in multiple meta-analyses. Also, high-dose calcium blocks absorption of iron, zinc, magnesium, and thyroid medication. If you also take Tums (calcium carbonate) for heartburn and calcium supplements and calcium-fortified foods, you may be at risk for kidney stones and cardiac calcification. Calculate your total from all sources, not just the pill.',
    overuse_ko: '칼슘이 풍부한 식단에 칼슘을 추가하면 해롭습니다 — 많은 한인 폐경 후 여성들이 "뼈를 위해" 하루 1000 mg 이상 칼슘을 복용하면서 유제품, 멸치, 두부, 잎채소도 먹습니다. 이는 총 섭취량을 하루 2000 mg 이상으로 밀어올리며, 여러 메타분석에서 심장마비 위험 증가와 연관되었습니다. 또한 고용량 칼슘은 철분, 아연, 마그네슘, 갑상선약의 흡수를 차단합니다. 속쓰림용 Tums(탄산칼슘)와 칼슘 보충제, 칼슘 강화 식품을 모두 복용한다면 신장 결석과 심장 석회화 위험이 있습니다. 모든 공급원의 총량을 계산하세요, 알약만이 아니라.',
    overuse_ja: 'カルシウム豊富な食事にカルシウムを追加すると有害 — 多くの韓国系閉経後女性が「骨のため」に1日1000 mg超のカルシウムを服用しつつ、乳製品、煮干し(メルチ)、豆腐(トゥブ)、青菜も食べています。これは総摂取量を1日2000 mg超に押し上げ、複数のメタ解析で心筋梗塞リスク増加と関連。また高用量カルシウムは鉄、亜鉛、マグネシウム、甲状腺薬の吸収を阻害。胸焼け用Tums(炭酸カルシウム)とカルシウムサプリ、カルシウム強化食品をすべて摂取していると腎結石と心血管石灰化リスク。錠剤だけでなく全供給源の合計を計算してください。',
    danger_en: 'HEART DISEASE CONCERN — some studies suggest high-dose calcium supplements (but not calcium from food) may be associated with increased heart attack risk. Get calcium from food first (dairy, leafy greens, fortified foods) and supplement only to fill the gap.',
    danger_ko: '심장병 우려 — 일부 연구는 고용량 칼슘 보충제(음식 칼슘은 제외)가 심장마비 위험 증가와 관련이 있을 수 있다고 시사합니다. 먼저 음식(유제품, 잎채소, 강화 식품)에서 칼슘을 섭취하고 부족분만 보충하세요.',
    danger_ja: '心疾患の懸念 — 一部の研究で高用量カルシウムサプリ(食事カルシウムは除く)が心筋梗塞リスク増加と関連の可能性。まず食事(乳製品、青菜、強化食品)からカルシウム摂取し不足分のみ補給。',
    warn_en: 'Can cause constipation and kidney stones. Do not exceed the upper limit. Do not take on the same hour as iron, thyroid medication, or certain antibiotics.',
    warn_ko: '변비와 신장 결석을 유발할 수 있습니다. 상한을 초과하지 마세요. 철분, 갑상선약, 특정 항생제와 같은 시간에 복용하지 마세요.',
    warn_ja: '便秘と腎結石を起こす可能性。上限を超えないでください。鉄、甲状腺薬、特定の抗生物質と同じ時間に服用しないでください。',
    interact: [
      { en: 'Thyroid medication (levothyroxine) — separate by 4 hours', ko: '갑상선약 (레보티록신) — 4시간 간격 필요', ja: '甲状腺薬(レボチロキシン) — 4時間間隔必要' },
      { en: 'Iron supplements — reduced absorption', ko: '철분제 — 흡수 감소', ja: '鉄剤 — 吸収減少' },
      { en: 'Antibiotics (tetracyclines, quinolones) — reduced absorption (separate by 2+ hours)', ko: '항생제 (테트라사이클린, 퀴놀론) — 흡수 감소 (2시간 이상 간격)', ja: '抗生物質(テトラサイクリン、キノロン) — 吸収減少(2時間以上間隔)' },
      { en: 'Bisphosphonates — reduced absorption', ko: '비스포스포네이트 — 흡수 감소', ja: 'ビスホスホネート — 吸収減少' }
    ],
    source: 'NIH Office of Dietary Supplements — Calcium Fact Sheet'
  },
  {
    id: 'iron',
    generic: { en: 'Iron (ferrous sulfate/gluconate/bisglycinate)', ko: '철분 (황산철/글루콘산철/비스글리신산철)', ja: '鉄(硫酸鉄/グルコン酸鉄/ビスグリシン酸鉄)' },
    brands: ['Slow Fe', 'Feosol', 'Nature Made'],
    category: 'supplement',
    uses: [
      { title_en: 'Treatment of iron-deficiency anemia', title_ko: '철결핍성 빈혈 치료', title_ja: '鉄欠乏性貧血の治療', evidence: 'strong',
        detail_en: 'Restores iron stores in people with low hemoglobin from blood loss, heavy menstruation, pregnancy, or inadequate intake',
        detail_ko: '출혈, 과다 월경, 임신, 섭취 부족으로 헤모글로빈이 낮은 사람의 철분 저장량 회복',
        detail_ja: '出血、月経過多、妊娠、摂取不足でヘモグロビン低下した人の鉄貯蔵を回復' },
      { title_en: 'Prevention during pregnancy', title_ko: '임신 중 예방', title_ja: '妊娠中の予防', evidence: 'strong',
        detail_en: 'Recommended during pregnancy to meet increased demand (as part of prenatal vitamin)',
        detail_ko: '증가된 요구량을 충족하기 위해 임신 중 권장 (산전 비타민에 포함)',
        detail_ja: '増加した需要を満たすため妊娠中に推奨(妊婦用ビタミンに含まれる)' }
    ],
    dose_en: { 'Adult men / postmenopausal women': '8 mg daily', 'Premenopausal women': '18 mg daily', 'Pregnancy': '27 mg daily', 'Deficiency treatment': '65–200 mg elemental iron daily (doctor-guided)', 'Take with': 'Vitamin C boosts absorption; avoid with calcium, coffee, or tea' },
    dose_ko: { '성인 남성·폐경 후 여성': '하루 8 mg', '폐경 전 여성': '하루 18 mg', '임신 중': '하루 27 mg', '결핍 치료': '의사 지도 하에 하루 원소철 65~200 mg', '복용 방법': '비타민 C와 함께 흡수 증가; 칼슘·커피·차와 병용 피하기' },
    dose_ja: { '成人男性·閉経後女性': '1日8 mg', '閉経前女性': '1日18 mg', '妊娠中': '1日27 mg', '欠乏治療': '医師の指導下で1日元素鉄65~200 mg', '服用方法': 'ビタミンCで吸収増加;カルシウム·コーヒー·茶との併用を避ける' },
    overuse_en: '"I AM TIRED SO I NEED IRON" MYTH — Fatigue has many causes. Taking iron without a blood test (ferritin, CBC) is dangerous because iron accumulates and damages the liver, pancreas, and heart. About 1 in 200 Koreans has hereditary hemochromatosis — these people should NEVER take iron supplements and can be killed by them. Postmenopausal women and men rarely need iron supplements. Also, iron tablets are the #1 cause of accidental child poisoning deaths — as few as 5 adult tablets can kill a toddler. Keep in child-proof containers separate from other supplements. Get ferritin and hemoglobin checked before starting iron.',
    overuse_ko: '"피곤하니까 철분이 필요해" 오해 — 피로에는 많은 원인이 있습니다. 혈액 검사(페리틴, CBC) 없이 철분제를 복용하는 것은 위험한데, 철분이 축적되어 간, 췌장, 심장을 손상시킵니다. 한국인 약 200명 중 1명이 유전성 혈색소증이며, 이들은 철분 보충제를 절대 복용해서는 안 되고 복용 시 사망할 수 있습니다. 폐경 후 여성과 남성은 철분 보충제가 거의 필요하지 않습니다. 또한 철분 정제는 어린이 우발적 중독 사망 원인 1위 — 성인용 5정만으로도 유아가 사망할 수 있습니다. 다른 보충제와 분리된 어린이 보호 용기에 보관하세요. 철분제 시작 전 페리틴과 헤모글로빈 검사를 받으세요.',
    overuse_ja: '「疲れたから鉄が必要」という誤解 — 疲労には多くの原因があります。血液検査(フェリチン、CBC)なしで鉄剤を服用するのは危険で、鉄が蓄積し肝臓、膵臓、心臓を損傷します。韓国人約200人に1人が遺伝性ヘモクロマトーシスで、これらの人は鉄サプリを絶対に服用すべきでなく、服用で死亡する可能性があります。閉経後女性と男性はほとんど鉄サプリを必要としません。また鉄錠剤は小児偶発的中毒死亡原因の第1位 — 成人用5錠で幼児が死亡する可能性。他のサプリと分けてチャイルドプルーフ容器に保管。鉄サプリ開始前にフェリチンとヘモグロビン検査を。',
    danger_en: 'SERIOUS POISONING RISK IN CHILDREN — as little as one adult iron tablet can be fatal to a young child. Keep in child-proof containers. If a child swallows iron, call Poison Control (1-800-222-1222) immediately. Do not take iron unless a blood test shows you need it — too much iron damages the liver and heart.',
    danger_ko: '어린이 중독 위험 — 성인용 철분제 1정만으로도 어린 아이에게 치명적일 수 있습니다. 어린이 보호 용기에 보관하세요. 어린이가 철분제를 삼켰으면 즉시 독극물 센터(1-800-222-1222)에 전화하세요. 혈액 검사로 필요가 확인되지 않은 경우 철분제를 복용하지 마세요 — 과잉 철분은 간과 심장을 손상시킵니다.',
    danger_ja: '小児中毒リスク — 成人用鉄錠1錠で幼児に致死的になる可能性。チャイルドプルーフ容器に保管。子どもが飲み込んだら即時毒物管理センター(米国1-800-222-1222)に連絡。血液検査で必要が確認されない限り服用しないでください — 過剰な鉄は肝臓と心臓を損傷。',
    warn_en: 'Common side effects: constipation, dark stools (harmless), nausea, stomach pain. Take with food if stomach upset, but absorption is better on empty stomach. Bisglycinate form is often gentler on the stomach.',
    warn_ko: '흔한 부작용: 변비, 검은 변(무해), 메스꺼움, 복통. 위장 장애가 있으면 음식과 함께 복용, 단 공복 복용 시 흡수가 더 좋음. 비스글리신산염 형태가 위장에 더 부드러움.',
    warn_ja: '一般的副作用:便秘、黒色便(無害)、吐き気、腹痛。胃部不快時は食事と共に服用、ただし空腹時のほうが吸収良好。ビスグリシン酸塩は胃にやさしい。',
    interact: [
      { en: 'Calcium, antacids, coffee, tea, dairy — reduce absorption (separate by 2 hours)', ko: '칼슘, 제산제, 커피, 차, 유제품 — 흡수 감소 (2시간 간격)', ja: 'カルシウム、制酸薬、コーヒー、茶、乳製品 — 吸収減少(2時間間隔)' },
      { en: 'Thyroid medication (levothyroxine) — separate by 4 hours', ko: '갑상선약 (레보티록신) — 4시간 간격', ja: '甲状腺薬(レボチロキシン) — 4時間間隔' },
      { en: 'Antibiotics (tetracyclines, quinolones) — reduced absorption of both', ko: '항생제 (테트라사이클린, 퀴놀론) — 둘 다 흡수 감소', ja: '抗生物質(テトラサイクリン、キノロン) — 両方の吸収減少' },
      { en: 'Proton pump inhibitors (omeprazole) — reduce iron absorption', ko: '양성자 펌프 억제제 (오메프라졸) — 철분 흡수 감소', ja: 'プロトンポンプ阻害薬(オメプラゾール) — 鉄吸収減少' }
    ],
    source: 'NIH Office of Dietary Supplements — Iron Fact Sheet'
  },
  {
    id: 'zinc',
    generic: { en: 'Zinc', ko: '아연', ja: '亜鉛' },
    brands: ['Nature Made', 'Zicam (lozenge)', 'Cold-EEZE'],
    category: 'supplement',
    uses: [
      { title_en: 'Immune function', title_ko: '면역 기능', title_ja: '免疫機能', evidence: 'strong',
        detail_en: 'Required for normal immune cell development and function; deficiency impairs immunity',
        detail_ko: '정상 면역 세포 발달과 기능에 필요; 결핍 시 면역 저하',
        detail_ja: '正常な免疫細胞の発達と機能に必要;欠乏時に免疫低下' },
      { title_en: 'Duration of common cold (lozenges)', title_ko: '감기 기간 단축 (로젠지)', title_ja: '風邪の期間短縮(ロゼンジ)', evidence: 'emerging',
        detail_en: 'Zinc lozenges started within 24 hours of symptom onset may shorten cold duration by 1–2 days',
        detail_ko: '증상 시작 24시간 이내 시작한 아연 로젠지는 감기 기간을 1~2일 단축 가능',
        detail_ja: '症状開始24時間以内に開始した亜鉛ロゼンジは風邪の期間を1~2日短縮可能' },
      { title_en: 'Wound healing', title_ko: '상처 치유', title_ja: '創傷治癒', evidence: 'strong',
        detail_en: 'Zinc-deficient wounds heal poorly; supplementing corrects this',
        detail_ko: '아연 결핍 상태의 상처는 치유가 저조하며 보충으로 개선',
        detail_ja: '亜鉛欠乏状態の創傷は治癒が不良で,補充により改善' }
    ],
    dose_en: { 'Adult RDA': '8 mg (women) / 11 mg (men) daily', 'Cold lozenges': '75 mg elemental zinc daily, spread across lozenges every 2 hours, for no more than 7 days', 'Upper limit': '40 mg/day long-term' },
    dose_ko: { '성인 RDA': '하루 8 mg (여성) / 11 mg (남성)', '감기 로젠지': '원소 아연 기준 하루 75 mg을 2시간마다 나눠서, 최대 7일까지', '상한': '장기 복용 시 하루 40 mg' },
    dose_ja: { '成人RDA': '1日8 mg(女性)/ 11 mg(男性)', '風邪ロゼンジ': '元素亜鉛換算で1日75 mgを2時間ごとに分けて,最大7日間', '上限': '長期服用時1日40 mg' },
    danger_en: 'INTRANASAL ZINC (Zicam nasal gel/spray) — FDA warned in 2009 that intranasal zinc can cause PERMANENT LOSS OF SMELL. Use only lozenge or oral forms. Long-term high-dose zinc (>40 mg/day) can cause copper deficiency, leading to anemia and nerve problems.',
    danger_ko: '비강 아연 (Zicam 비강 젤·스프레이) — FDA는 2009년 비강 아연이 영구적 후각 상실을 일으킬 수 있다고 경고했습니다. 로젠지나 경구 형태만 사용하세요. 하루 40 mg 초과 장기 복용은 구리 결핍을 유발하여 빈혈과 신경 문제를 일으킬 수 있습니다.',
    danger_ja: '鼻腔内亜鉛(Zicam鼻腔ジェル·スプレー) — FDAは2009年に鼻腔内亜鉛が永久的嗅覚喪失を引き起こす可能性があると警告しました。ロゼンジまたは経口形態のみ使用してください。1日40 mg超の長期服用は銅欠乏を誘発し,貧血と神経障害を引き起こす可能性があります。',
    warn_en: 'Nausea and stomach upset are common — take with food. Zinc can have a metallic taste in lozenges.',
    warn_ko: '메스꺼움과 위장 장애가 흔함 — 음식과 함께 복용. 로젠지에서 금속성 맛이 날 수 있습니다.',
    warn_ja: '吐き気と胃腸障害が一般的 — 食事と一緒に服用。ロゼンジで金属味がする場合があります。',
    interact: [
      { en: 'Antibiotics (tetracyclines, quinolones) — reduced absorption (separate by 2 hours)', ko: '항생제 (테트라사이클린, 퀴놀론) — 흡수 감소 (2시간 간격)', ja: '抗生物質(テトラサイクリン,キノロン) — 吸収低下(2時間間隔)' },
      { en: 'Copper — long-term high-dose zinc causes copper deficiency', ko: '구리 — 고용량 장기 복용 시 구리 결핍 유발', ja: '銅 — 高用量長期服用時に銅欠乏を誘発' },
      { en: 'Penicillamine — reduced effectiveness', ko: '페니실라민 — 효과 감소', ja: 'ペニシラミン — 効果低下' }
    ],
    source: 'NIH Office of Dietary Supplements — Zinc Fact Sheet'
  },
  {
    id: 'omega3',
    generic: { en: 'Omega-3 (EPA/DHA — fish oil)', ko: '오메가-3 (EPA/DHA — 어유)', ja: 'オメガ-3(EPA/DHA — 魚油)' },
    brands: ['Nature Made', 'Nordic Naturals', 'Kirkland'],
    category: 'supplement',
    uses: [
      { title_en: 'Triglyceride lowering (high-dose, prescription)', title_ko: '중성지방 감소 (고용량·처방)', title_ja: '中性脂肪低下(高用量·処方)', evidence: 'strong',
        detail_en: 'Prescription-strength omega-3 (4 g/day EPA+DHA) lowers very high triglycerides. OTC doses are lower and effect is smaller.',
        detail_ko: '처방 강도 오메가-3(하루 EPA+DHA 4 g)는 매우 높은 중성지방을 낮춤. OTC 용량은 낮고 효과도 작음.',
        detail_ja: '処方強度のオメガ-3(1日EPA+DHA 4 g)は非常に高い中性脂肪を低下させる。OTC用量は低く効果も小さい。' },
      { title_en: 'General cardiovascular health', title_ko: '일반 심혈관 건강', title_ja: '一般心血管健康', evidence: 'emerging',
        detail_en: 'Eating oily fish 1–2 times weekly is supported by the American Heart Association. Supplement evidence is mixed.',
        detail_ko: '주 1~2회 기름진 생선 섭취는 미국심장협회가 권장. 보충제에 대한 근거는 혼재.',
        detail_ja: '週1~2回の脂の多い魚摂取は米国心臓協会が推奨。サプリのエビデンスは混在。' },
      { title_en: 'Rheumatoid arthritis symptom support', title_ko: '류마티스 관절염 증상 보조', title_ja: '関節リウマチ症状補助', evidence: 'emerging',
        detail_en: 'May reduce joint stiffness and tenderness as adjunct to standard therapy',
        detail_ko: '표준 치료의 보조요법으로 관절 강직과 압통을 감소시킬 수 있음',
        detail_ja: '標準治療の補助として関節のこわばりと圧痛を軽減する可能性' }
    ],
    dose_en: { 'General health': '1000 mg fish oil daily (contains ~300 mg combined EPA+DHA)', 'AHA recommendation': '1 g EPA+DHA daily for people with heart disease (food or supplement)', 'High triglycerides': '2–4 g daily — requires doctor supervision', 'Quality': 'Look for IFOS-certified products (tested for mercury, PCBs)' },
    dose_ko: { '일반 건강': '하루 어유 1000 mg (EPA+DHA 합산 약 300 mg 함유)', 'AHA 권장': '심장병 환자는 하루 EPA+DHA 1 g (음식 또는 보충제)', '고중성지방': '하루 2~4 g — 의사 감독 필요', '품질': 'IFOS 인증 제품(수은·PCB 검사 통과) 선택' },
    dose_ja: { '一般健康': '1日魚油1000 mg(EPA+DHA合計約300 mg含有)', 'AHA推奨': '心疾患患者は1日EPA+DHA 1 g(食品またはサプリ)', '高中性脂肪': '1日2~4 g — 医師の管理が必要', '品質': 'IFOS認証製品(水銀·PCB検査済)を選択' },
    overuse_en: 'MULTIPLE OMEGA-3 PRODUCTS AT ONCE — Korean households often take fish oil + krill oil + algae oil + "high-concentration" omega-3 simultaneously, totaling 5000+ mg daily. This causes: (1) increased bleeding risk — especially dangerous with aspirin, warfarin, or before surgery; (2) atrial fibrillation risk — large 2021 trials showed high-dose omega-3 increased AFib by 50% in older adults; (3) fish burps and GI upset; (4) potential mercury/PCB accumulation from non-tested products. Stick to one product, 1–2 g EPA+DHA daily unless a doctor prescribes more. Eating oily fish 2x/week provides similar benefit without these risks.',
    overuse_ko: '여러 오메가-3 제품 동시 복용 — 한인 가정에서 어유 + 크릴오일 + 알지 오일 + "고농축" 오메가-3를 동시에 복용하여 하루 총 5000 mg 이상 섭취하는 경우가 흔합니다. 이는 다음을 유발합니다: (1) 출혈 위험 증가 — 특히 아스피린, 와파린 복용자나 수술 전 위험; (2) 심방세동 위험 — 2021년 대규모 임상시험에서 고용량 오메가-3가 고령자의 심방세동을 50% 증가시킴; (3) 생선 트림과 위장 장애; (4) 검사되지 않은 제품의 수은·PCB 축적 가능성. 의사가 고용량을 처방하지 않는 한 제품 1개, 하루 EPA+DHA 1~2 g으로 제한하세요. 기름진 생선을 주 2회 먹으면 이런 위험 없이 비슷한 이득을 얻습니다.',
    overuse_ja: '複数のオメガ-3製品の同時服用 — 日本·韓国の家庭で魚油+クリルオイル+藻油+「高濃縮」オメガ-3を同時に服用し1日合計5000 mg以上摂取するケースがあります。これは以下を引き起こします:(1)出血リスク増加 — 特にアスピリン·ワルファリン服用者や手術前は危険;(2)心房細動リスク — 2021年の大規模臨床試験で高用量オメガ-3が高齢者の心房細動を50%増加させた;(3)魚臭いげっぷと胃腸障害;(4)検査されていない製品の水銀·PCB蓄積の可能性。医師が高用量を処方しない限り,製品1つ,1日EPA+DHA 1~2 gに制限してください。脂の多い魚を週2回食べればこれらのリスクなく同様の効果が得られます。',
    warn_en: 'Fish burps, fishy aftertaste, and mild GI upset are common. Freezing capsules can help. High doses can increase bleeding time — stop before surgery (ask surgeon). Avoid products without third-party testing (mercury, oxidation risk).',
    warn_ko: '생선 트림, 생선 맛, 경미한 위장 장애가 흔함. 캡슐을 얼리면 도움이 됨. 고용량은 출혈 시간을 연장할 수 있으므로 수술 전 중단(외과의 상담). 제3자 검사를 거치지 않은 제품(수은·산화 위험)은 피하세요.',
    warn_ja: '魚臭いげっぷ,魚の後味,軽度の胃腸障害が一般的。カプセルを冷凍すると軽減。高用量は出血時間を延長する可能性があるため手術前は中止(外科医に相談)。第三者検査を経ていない製品(水銀·酸化リスク)は避けてください。',
    interact: [
      { en: 'Blood thinners (warfarin, apixaban) — increased bleeding risk at high doses', ko: '혈액 희석제 (와파린, 엘리퀴스) — 고용량에서 출혈 위험 증가', ja: '抗凝固薬(ワルファリン,エリキュース) — 高用量で出血リスク増加' },
      { en: 'Aspirin, NSAIDs — additive bleeding risk', ko: '아스피린, NSAID — 출혈 위험 누적', ja: 'アスピリン,NSAID — 出血リスクの累積' },
      { en: 'Blood pressure medications — may enhance effect', ko: '혈압약 — 효과 증강 가능', ja: '降圧薬 — 効果増強の可能性' }
    ],
    source: 'NIH Office of Dietary Supplements — Omega-3 Fact Sheet'
  },
  {
    id: 'probiotics',
    generic: { en: 'Probiotics', ko: '프로바이오틱스 (유산균)', ja: 'プロバイオティクス(乳酸菌)' },
    brands: ['Culturelle', 'Florastor', 'Align'],
    category: 'supplement',
    uses: [
      { title_en: 'Antibiotic-associated diarrhea prevention', title_ko: '항생제 관련 설사 예방', title_ja: '抗生物質関連下痢の予防', evidence: 'strong',
        detail_en: 'Taking probiotics during and after a course of antibiotics reduces diarrhea risk (Saccharomyces boulardii, Lactobacillus)',
        detail_ko: '항생제 복용 중과 직후 프로바이오틱스(Saccharomyces boulardii, 락토바실러스) 섭취 시 설사 위험 감소',
        detail_ja: '抗生物質服用中および直後にプロバイオティクス(Saccharomyces boulardii,ラクトバチルス)を摂取すると下痢リスク低下' },
      { title_en: 'Acute infectious diarrhea (adults)', title_ko: '급성 감염성 설사 (성인)', title_ja: '急性感染性下痢(成人)', evidence: 'emerging',
        detail_en: 'Certain strains may shorten duration by about 1 day',
        detail_ko: '특정 균주가 기간을 약 1일 단축할 수 있음',
        detail_ja: '特定の菌株が期間を約1日短縮する可能性' },
      { title_en: 'IBS symptom relief', title_ko: '과민성 대장 증후군 증상 완화', title_ja: '過敏性腸症候群の症状緩和', evidence: 'emerging',
        detail_en: 'Some strains help with bloating and abdominal discomfort; results vary by strain',
        detail_ko: '일부 균주가 복부 팽만과 불편감에 도움; 균주에 따라 효과가 다름',
        detail_ja: '一部の菌株が腹部膨満と不快感に有効;菌株により効果が異なる' }
    ],
    dose_en: { 'Typical': '1–10 billion CFU daily (check label)', 'Strain matters': 'Different strains do different things — match the strain to the use', 'Timing with antibiotics': 'Take 2+ hours apart from the antibiotic', 'Refrigeration': 'Some products require it — check label' },
    dose_ko: { '일반': '하루 10억~100억 CFU (라벨 확인)', '균주 중요': '균주마다 효과가 다름 — 목적에 맞는 균주 선택', '항생제와 병용': '항생제와 2시간 이상 간격을 두고 복용', '냉장': '일부 제품은 냉장 보관 필요 — 라벨 확인' },
    dose_ja: { '一般': '1日10億~100億CFU(ラベル確認)', '菌株が重要': '菌株ごとに効果が異なる — 目的に合った菌株を選択', '抗生物質との併用': '抗生物質と2時間以上の間隔をあけて服用', '冷蔵': '一部製品は冷蔵保管が必要 — ラベル確認' },
    danger_en: 'AVOID IF IMMUNOCOMPROMISED — people with weakened immune systems (chemotherapy, transplant recipients, severe illness, catheters) have had rare but serious bloodstream infections from probiotics. Talk to your doctor first.',
    danger_ko: '면역 저하자는 피하세요 — 면역 기능이 약화된 사람(항암치료 중, 장기이식 환자, 중증 환자, 카테터 삽입 환자)에게 드물지만 심각한 프로바이오틱스 유래 혈류 감염이 보고되었습니다. 먼저 의사와 상담하세요.',
    danger_ja: '免疫低下者は避けてください — 免疫機能が低下した人(化学療法中,臓器移植患者,重症患者,カテーテル挿入患者)では稀だが重篤なプロバイオティクス由来の血流感染が報告されています。まず医師に相談してください。',
    warn_en: 'Mild gas and bloating in the first few days are common. Product quality varies widely — look for brands that list exact strain (not just species) and CFU guaranteed through expiration date.',
    warn_ko: '첫 며칠간 경미한 가스와 복부 팽만이 흔함. 제품 품질이 크게 다르므로 정확한 균주(종 이름만이 아닌)와 유효기간까지 보장되는 CFU가 표기된 브랜드를 선택하세요.',
    warn_ja: '最初の数日間は軽度のガスと腹部膨満が一般的。製品品質が大きく異なるため,正確な菌株(種名だけでなく)と有効期限まで保証されたCFUが表記されたブランドを選択してください。',
    interact: [
      { en: 'Antibiotics — take 2+ hours apart to avoid killing the probiotics', ko: '항생제 — 프로바이오틱스가 죽지 않도록 2시간 이상 간격', ja: '抗生物質 — プロバイオティクスが死滅しないよう2時間以上の間隔' },
      { en: 'Immunosuppressants — infection risk (avoid probiotics)', ko: '면역 억제제 — 감염 위험 (프로바이오틱스 피하기)', ja: '免疫抑制薬 — 感染リスク(プロバイオティクスは避ける)' }
    ],
    source: 'NIH Office of Dietary Supplements · MedlinePlus (NIH)'
  },
  {
    id: 'multivitamin',
    generic: { en: 'Multivitamin', ko: '종합 비타민', ja: '総合ビタミン剤' },
    brands: ['Centrum', 'One A Day', 'Nature Made'],
    category: 'supplement',
    uses: [
      { title_en: 'Fill nutrient gaps in diet', title_ko: '식단 영양소 부족 보충', title_ja: '食事の栄養素不足を補う', evidence: 'emerging',
        detail_en: 'Provides small amounts of many vitamins and minerals; useful when diet is limited, restricted, or inconsistent',
        detail_ko: '많은 비타민과 미네랄을 소량씩 제공; 식단이 제한적·비일관적일 때 유용',
        detail_ja: '多くのビタミンとミネラルを少量ずつ提供;食事が限定的·不安定な時に有用' },
      { title_en: 'Targeted support (age/gender specific)', title_ko: '연령·성별 맞춤 보충', title_ja: '年齢·性別に応じた補充', evidence: 'emerging',
        detail_en: 'Prenatal, over-50, men, women formulas adjust for life-stage needs (iron for premenopausal women, B12 for older adults)',
        detail_ko: '산전, 50세 이상, 남성·여성용 등은 생애 단계별 필요(폐경 전 여성의 철분, 고령자의 B12)에 맞게 조정',
        detail_ja: '妊娠用,50歳以上,男性·女性用などはライフステージ別ニーズ(閉経前女性の鉄,高齢者のB12)に合わせて調整' }
    ],
    dose_en: { 'Typical': 'One tablet daily with food', 'Choose by life stage': 'Prenatal, men, women, over 50, etc.', 'Quality': 'USP-verified or NSF-certified products', 'Not a replacement for diet': 'Whole foods provide fiber, phytochemicals, and protein that no pill can replace' },
    dose_ko: { '일반': '하루 1정 식사와 함께', '생애 단계 선택': '산전, 남성, 여성, 50세 이상 등', '품질': 'USP 또는 NSF 인증 제품', '식단 대체 불가': '통곡물·식품은 알약이 대체할 수 없는 식이섬유·피토케미컬·단백질을 제공' },
    dose_ja: { '一般': '1日1錠を食事と一緒に', 'ライフステージ別選択': '妊娠用,男性,女性,50歳以上など', '品質': 'USPまたはNSF認証製品', '食事の代替不可': '全粒食品は錠剤では代替できない食物繊維·ファイトケミカル·タンパク質を提供' },
    warn_en: 'Adults with no deficiency and a reasonable diet may get little benefit. Smokers should avoid high-dose beta-carotene (linked to lung cancer). People who take multiple supplements can accidentally exceed upper limits — check totals. Do not use as a substitute for prenatal vitamin if pregnant.',
    warn_ko: '결핍이 없고 합리적인 식단을 유지하는 성인에게는 이득이 적을 수 있습니다. 흡연자는 고용량 베타카로틴(폐암 관련)을 피해야 합니다. 여러 보충제를 복용하는 사람은 상한을 초과할 수 있으므로 합산량을 확인하세요. 임신 중에는 산전 비타민을 대체하지 마세요.',
    warn_ja: '欠乏がなく合理的な食事を維持する成人には利益が少ない場合があります。喫煙者は高用量ベータカロテン(肺がんと関連)を避けるべきです。複数のサプリを服用する人は上限を超える可能性があるため,合計量を確認してください。妊娠中は妊娠用ビタミンの代替として使用しないでください。',
    interact: [
      { en: 'Iron in multivitamin — separates from thyroid medication, some antibiotics', ko: '종합 비타민의 철분 — 갑상선약, 일부 항생제와 간격 필요', ja: '総合ビタミンの鉄 — 甲状腺薬·一部の抗生物質と間隔が必要' },
      { en: 'Vitamin K content — can reduce warfarin effect (keep intake consistent)', ko: '비타민 K 함량 — 와파린 효과 감소 가능 (섭취량을 일정하게 유지)', ja: 'ビタミンK含有量 — ワルファリンの効果を低下させる可能性(摂取量を一定に保つ)' },
      { en: 'Calcium content — see calcium entry', ko: '칼슘 함량 — 칼슘 항목 참조', ja: 'カルシウム含有量 — カルシウムの項目参照' }
    ],
    source: 'NIH Office of Dietary Supplements — Multivitamin/Mineral Supplements'
  },
  {
    id: 'folic-acid',
    generic: { en: 'Folic acid / Folate', ko: '엽산', ja: '葉酸' },
    brands: ['Nature Made', 'Solgar'],
    category: 'supplement',
    uses: [
      { title_en: 'Neural tube defect prevention (pregnancy)', title_ko: '신경관 결손 예방 (임신)', title_ja: '神経管閉鎖障害の予防(妊娠)', evidence: 'strong',
        detail_en: 'CDC recommends 400 mcg daily for all women who could become pregnant; reduces risk of spina bifida and anencephaly',
        detail_ko: 'CDC는 임신 가능성이 있는 모든 여성에게 하루 400 mcg 권장; 척추이분증 및 무뇌증 위험 감소',
        detail_ja: 'CDCは妊娠可能なすべての女性に1日400 mcgを推奨;二分脊椎症および無脳症のリスクを低下' },
      { title_en: 'Correction of folate deficiency', title_ko: '엽산 결핍 교정', title_ja: '葉酸欠乏の是正', evidence: 'strong',
        detail_en: 'Treats megaloblastic anemia caused by low folate',
        detail_ko: '엽산 저하로 인한 거대적아구성 빈혈 치료',
        detail_ja: '葉酸低下による巨赤芽球性貧血の治療' },
      { title_en: 'Support with methotrexate', title_ko: '메토트렉세이트 복용 시 보충', title_ja: 'メトトレキサート服用時の補充', evidence: 'strong',
        detail_en: 'Doctors prescribe folic acid alongside methotrexate to reduce side effects',
        detail_ko: '의사가 메토트렉세이트의 부작용을 줄이기 위해 엽산을 함께 처방',
        detail_ja: '医師がメトトレキサートの副作用を軽減するために葉酸を併用処方' }
    ],
    dose_en: { 'Women who could become pregnant': '400 mcg daily', 'Pregnancy': '600 mcg daily', 'Breastfeeding': '500 mcg daily', 'Upper limit': '1000 mcg/day from supplements and fortified foods' },
    dose_ko: { '임신 가능 여성': '하루 400 mcg', '임신 중': '하루 600 mcg', '수유 중': '하루 500 mcg', '상한': '보충제·강화 식품으로 하루 1000 mcg' },
    dose_ja: { '妊娠可能女性': '1日400 mcg', '妊娠中': '1日600 mcg', '授乳中': '1日500 mcg', '上限': 'サプリ·強化食品から1日1000 mcg' },
    warn_en: 'High-dose folic acid can mask vitamin B12 deficiency (which causes nerve damage if untreated). If you are over 50 or at risk for B12 deficiency, have B12 checked before taking high-dose folate. Certain epilepsy medications reduce folate — ask your doctor.',
    warn_ko: '고용량 엽산은 비타민 B12 결핍(치료하지 않으면 신경 손상 유발)을 가릴 수 있습니다. 50세 이상이거나 B12 결핍 위험이 있으면 고용량 엽산 복용 전 B12 수치를 확인하세요. 특정 뇌전증 약은 엽산을 감소시키니 의사와 상담하세요.',
    warn_ja: '高用量葉酸はビタミンB12欠乏(未治療で神経損傷を引き起こす)を隠す可能性があります。50歳以上またはB12欠乏のリスクがある場合,高用量葉酸服用前にB12値を確認してください。特定のてんかん薬は葉酸を低下させるため医師に相談してください。',
    interact: [
      { en: 'Methotrexate — folic acid reduces side effects (intended)', ko: '메토트렉세이트 — 엽산이 부작용을 감소 (의도된 효과)', ja: 'メトトレキサート — 葉酸が副作用を軽減(意図された効果)' },
      { en: 'Antiepileptic drugs (phenytoin, phenobarbital) — may lower folate', ko: '항뇌전증약 (페니토인, 페노바르비탈) — 엽산 저하 가능', ja: '抗てんかん薬(フェニトイン,フェノバルビタール) — 葉酸低下の可能性' },
      { en: 'Sulfasalazine — reduces folate absorption', ko: '설파살라진 — 엽산 흡수 감소', ja: 'スルファサラジン — 葉酸吸収低下' }
    ],
    source: 'NIH Office of Dietary Supplements — Folate Fact Sheet · CDC'
  },
  {
    id: 'coq10',
    generic: { en: 'Coenzyme Q10 (ubiquinol/ubiquinone)', ko: '코엔자임 Q10 (유비퀴놀/유비퀴논)', ja: 'コエンザイムQ10(ユビキノール/ユビキノン)' },
    brands: ['Qunol', 'Doctor\'s Best', 'Kirkland'],
    category: 'supplement',
    uses: [
      { title_en: 'Statin-associated muscle symptoms', title_ko: '스타틴 관련 근육 증상', title_ja: 'スタチン関連筋症状', evidence: 'limited',
        detail_en: 'Statins can lower CoQ10 levels; some patients report reduced muscle aches with supplementation, but clinical trial results are mixed',
        detail_ko: '스타틴은 CoQ10 수치를 낮출 수 있으며, 일부 환자는 보충 시 근육통 감소를 보고하지만 임상시험 결과는 혼재',
        detail_ja: 'スタチンはCoQ10値を低下させる可能性があり,一部患者は補充により筋肉痛の軽減を報告するが臨床試験結果は混在' },
      { title_en: 'Heart failure (adjunct therapy)', title_ko: '심부전 (보조 치료)', title_ja: '心不全(補助治療)', evidence: 'emerging',
        detail_en: 'Some studies show improved symptoms and reduced hospitalizations when added to standard heart failure therapy',
        detail_ko: '일부 연구에서 표준 심부전 치료에 추가 시 증상 개선 및 입원율 감소',
        detail_ja: '一部研究で標準心不全治療に追加した際に症状改善と入院率低下を示す' },
      { title_en: 'Migraine prevention', title_ko: '편두통 예방', title_ja: '片頭痛予防', evidence: 'emerging',
        detail_en: 'May reduce migraine frequency when taken daily for preventive purposes',
        detail_ko: '예방 목적으로 매일 복용 시 편두통 빈도 감소 가능',
        detail_ja: '予防目的で毎日服用すると片頭痛頻度が減少する可能性' }
    ],
    dose_en: { 'Typical': '100–200 mg daily with a meal containing fat (better absorption)', 'Ubiquinol form': 'Preferred in older adults (better absorbed)', 'Patience': 'May take 4–12 weeks to see effect' },
    dose_ko: { '일반': '지방 함유 식사와 함께 하루 100~200 mg (흡수 양호)', '유비퀴놀 형태': '고령자에게 권장 (흡수 양호)', '인내': '효과가 나타나는 데 4~12주 소요' },
    dose_ja: { '一般': '脂質を含む食事と一緒に1日100~200 mg(吸収良好)', 'ユビキノール形態': '高齢者に推奨(吸収良好)', '忍耐': '効果発現まで4~12週間' },
    overuse_en: '"TAKING COQ10 MEANS I CAN SKIP STATINS" MYTH — Some people stop their statin (Lipitor, Crestor, 리피토) thinking CoQ10 "protects the heart" equally. This is dangerous — statins prevent heart attacks and strokes by lowering cholesterol, which CoQ10 does NOT do. Stopping statins triples heart attack risk within the first year. CoQ10 may help muscle aches from statins, but is NOT a replacement. Also, Korean anti-aging clinics promote 400+ mg daily for "energy" — doses this high can lower blood pressure dangerously when combined with BP medications, and can reduce warfarin effect (causing clots). Stick to 100–200 mg unless a doctor prescribes more.',
    overuse_ko: '"CoQ10 먹으니까 스타틴은 안 먹어도 돼" 오해 — 일부 환자가 CoQ10이 "심장을 똑같이 보호한다"며 스타틴(리피토, 크레스토)을 중단합니다. 이는 위험한 행동입니다 — 스타틴은 콜레스테롤을 낮춰 심장마비와 뇌졸중을 예방하는데 CoQ10은 그렇지 않습니다. 스타틴 중단은 첫 1년간 심장마비 위험을 3배 증가시킵니다. CoQ10은 스타틴 근육통에 도움될 수 있으나 대체재가 아닙니다. 또한 한인 항노화 클리닉에서 "에너지용"으로 하루 400 mg 이상을 홍보하는데, 이 정도 고용량은 혈압약과 병용 시 혈압을 위험하게 낮추고 와파린 효과를 감소시켜 혈전을 일으킬 수 있습니다. 의사가 고용량을 처방하지 않는 한 100~200 mg을 유지하세요.',
    overuse_ja: '「CoQ10を飲んでいるからスタチンは要らない」という誤解 — 一部の患者がCoQ10が「心臓を同じように保護する」と考えてスタチン(リピトール,クレストール)を中止します。これは危険な行為です — スタチンはコレステロールを下げて心筋梗塞と脳卒中を予防しますが,CoQ10にはそのような効果はありません。スタチン中止は最初の1年間で心筋梗塞リスクを3倍に増加させます。CoQ10はスタチンによる筋肉痛に有効な場合がありますが,代替品ではありません。また,アンチエイジングクリニックで「エネルギー用」として1日400 mg以上が宣伝されていますが,この高用量は降圧薬との併用で血圧を危険なほど低下させ,ワルファリンの効果を減弱させて血栓を引き起こす可能性があります。医師が高用量を処方しない限り100~200 mgを維持してください。',
    warn_en: 'Generally well tolerated. Mild GI upset is the most common side effect. Can lower blood pressure modestly — monitor if you take blood pressure medication. Quality varies — look for USP-verified products.',
    warn_ko: '일반적으로 내약성이 좋음. 가장 흔한 부작용은 경미한 위장 장애. 혈압을 약간 낮출 수 있으므로 혈압약을 복용 중이면 모니터링. 품질이 다양하므로 USP 인증 제품을 찾으세요.',
    warn_ja: '一般に忍容性は良好。最も一般的な副作用は軽度の胃腸障害。血圧をやや低下させる可能性があるため,降圧薬服用中はモニタリング。品質が様々なためUSP認証製品を選択。',
    interact: [
      { en: 'Warfarin — may reduce warfarin effect (monitor INR)', ko: '와파린 — 와파린 효과 감소 가능 (INR 모니터링)', ja: 'ワルファリン — ワルファリン効果低下の可能性(INRモニタリング)' },
      { en: 'Blood pressure medications — additive blood pressure lowering', ko: '혈압약 — 혈압 저하 효과 누적', ja: '降圧薬 — 血圧低下効果の累積' },
      { en: 'Chemotherapy — possible interaction (ask oncologist)', ko: '항암제 — 상호작용 가능 (종양내과 상담)', ja: '抗がん剤 — 相互作用の可能性(腫瘍内科に相談)' }
    ],
    source: 'NIH Office of Dietary Supplements · MedlinePlus (NIH)'
  },
  {
    id: 'glucosamine-chondroitin',
    generic: { en: 'Glucosamine / Chondroitin', ko: '글루코사민 / 콘드로이틴', ja: 'グルコサミン/コンドロイチン' },
    brands: ['Osteo Bi-Flex', 'Schiff Move Free'],
    category: 'supplement',
    uses: [
      { title_en: 'Knee osteoarthritis pain', title_ko: '무릎 골관절염 통증', title_ja: '膝変形性関節症の痛み', evidence: 'limited',
        detail_en: 'Evidence is mixed — some studies show modest pain relief in moderate-to-severe knee osteoarthritis; large trials (GAIT) showed no clear benefit overall',
        detail_ko: '근거는 혼재 — 중등도~중증 무릎 골관절염에서 경미한 통증 완화를 보이는 연구가 있으나, 대규모 시험(GAIT)에서는 전반적으로 명확한 이득 없음',
        detail_ja: 'エビデンスは混在 — 中等度~重度の膝変形性関節症で軽度の鎮痛を示す研究があるが,大規模試験(GAIT)では全体として明確な利益なし' }
    ],
    dose_en: { 'Typical': 'Glucosamine sulfate 1500 mg + chondroitin 1200 mg daily', 'Duration': 'If no benefit after 3 months, it likely will not work for you', 'Form matters': 'Glucosamine sulfate may work better than glucosamine hydrochloride' },
    dose_ko: { '일반': '하루 글루코사민 설페이트 1500 mg + 콘드로이틴 1200 mg', '기간': '3개월 후 효과 없으면 본인에게 맞지 않을 가능성', '형태': '글루코사민 설페이트가 염산염보다 효과 좋을 수 있음' },
    dose_ja: { '一般': '1日グルコサミン硫酸塩1500 mg + コンドロイチン1200 mg', '期間': '3ヶ月後に効果がなければ自分には合わない可能性', '形態': 'グルコサミン硫酸塩が塩酸塩より効果的な場合あり' },
    overuse_en: 'WARFARIN USERS AT SERIOUS RISK — Multiple case reports show glucosamine + warfarin causing dangerous INR increases and major bleeding, including brain hemorrhages. If you take warfarin (쿠마딘, Coumadin), do NOT start glucosamine without consulting your doctor — and if you do, INR must be checked weekly at first. Elderly Korean patients with AFib or post-stroke are often on warfarin AND take glucosamine "for knees" — a dangerous combination. Also, "liquid glucosamine" imports often contain extra ingredients (MSM, herbs) that compound risks. Finally, diabetics should monitor blood sugar — glucosamine can raise A1C slightly.',
    overuse_ko: '와파린 복용자는 심각한 위험 — 여러 사례 보고에서 글루코사민 + 와파린 병용이 위험한 INR 증가와 뇌출혈을 포함한 대량 출혈을 일으켰습니다. 와파린(쿠마딘, Coumadin)을 복용 중이라면 의사 상담 없이 글루코사민을 시작하지 마세요. 시작한다면 초기에는 매주 INR을 확인해야 합니다. 심방세동이나 뇌졸중 후 와파린을 복용 중인 한인 고령 환자가 "무릎용"으로 글루코사민을 함께 복용하는 경우가 많은데, 이는 위험한 조합입니다. 또한 수입 "액상 글루코사민"은 MSM이나 허브 등 추가 성분을 함유하여 위험을 가중시킵니다. 마지막으로, 당뇨 환자는 혈당을 모니터링하세요 — 글루코사민이 A1C를 약간 상승시킬 수 있습니다.',
    overuse_ja: 'ワルファリン服用者に重大なリスク — 複数の症例報告でグルコサミン+ワルファリンの併用が危険なINR上昇と脳出血を含む大量出血を引き起こしました。ワルファリン(クマジン,Coumadin)服用中は医師に相談せずグルコサミンを開始しないでください。開始する場合,初期は毎週INRを確認する必要があります。心房細動や脳卒中後にワルファリンを服用中の高齢患者が「膝のため」にグルコサミンを併用するケースが多いですが,これは危険な組み合わせです。また,輸入「液状グルコサミン」はMSMやハーブなどの追加成分を含み,リスクを増大させます。最後に,糖尿病患者は血糖をモニタリングしてください — グルコサミンがA1Cを若干上昇させる可能性があります。',
    warn_en: 'Derived from shellfish — avoid if you have shellfish allergy (or choose plant-based glucosamine). May mildly raise blood sugar — check with doctor if diabetic. Can increase bleeding risk when combined with warfarin.',
    warn_ko: '조개류에서 추출 — 조개 알레르기가 있으면 피하거나 식물성 글루코사민 선택. 혈당을 약간 올릴 수 있으므로 당뇨가 있으면 의사와 상담. 와파린과 병용 시 출혈 위험 증가 가능.',
    warn_ja: '甲殻類から抽出 — 甲殻類アレルギーがある場合は避けるか植物性グルコサミンを選択。血糖を若干上昇させる可能性があるため,糖尿病がある場合は医師に相談。ワルファリンとの併用で出血リスク増加の可能性。',
    interact: [
      { en: 'Warfarin — increased INR and bleeding risk (important)', ko: '와파린 — INR 및 출혈 위험 증가 (중요)', ja: 'ワルファリン — INRおよび出血リスク増加(重要)' },
      { en: 'Diabetes medications — glucosamine may affect blood sugar', ko: '당뇨약 — 글루코사민이 혈당에 영향 가능', ja: '糖尿病薬 — グルコサミンが血糖に影響する可能性' }
    ],
    source: 'NIH NCCIH · NIH Office of Dietary Supplements'
  },
  {
    id: 'lutein',
    generic: { en: 'Lutein + Zeaxanthin (AREDS2)', ko: '루테인 + 지아잔틴 (AREDS2)', ja: 'ルテイン+ゼアキサンチン(AREDS2)' },
    brands: ['PreserVision AREDS2', 'Ocuvite'],
    category: 'supplement',
    uses: [
      { title_en: 'Age-related macular degeneration progression', title_ko: '노인성 황반변성 진행 억제', title_ja: '加齢黄斑変性の進行抑制', evidence: 'strong',
        detail_en: 'AREDS2 study showed the combination (lutein, zeaxanthin, vitamin C, E, zinc, copper) slows progression of intermediate or advanced AMD',
        detail_ko: 'AREDS2 연구에서 복합 보충제(루테인, 지아잔틴, 비타민 C·E, 아연, 구리)가 중등도~진행성 AMD의 진행을 지연시킴을 입증',
        detail_ja: 'AREDS2研究で複合サプリ(ルテイン,ゼアキサンチン,ビタミンC·E,亜鉛,銅)が中等度~進行性AMDの進行を遅らせることを実証' },
      { title_en: 'General eye health', title_ko: '일반 안구 건강', title_ja: '一般眼の健康', evidence: 'emerging',
        detail_en: 'May support macular pigment density and visual function; found naturally in leafy greens and egg yolks',
        detail_ko: '황반 색소 밀도와 시각 기능을 지원할 수 있음; 잎채소와 달걀노른자에 자연적으로 함유',
        detail_ja: '黄斑色素密度と視機能を支援する可能性;葉物野菜と卵黄に自然に含有' }
    ],
    dose_en: { 'AREDS2 formula': 'Lutein 10 mg + Zeaxanthin 2 mg daily (plus other AREDS2 ingredients)', 'General use': '6–20 mg lutein daily from supplement or food', 'Only for AMD risk': 'AREDS2 is specifically for intermediate/advanced AMD — not preventive in healthy eyes' },
    dose_ko: { 'AREDS2 제형': '하루 루테인 10 mg + 지아잔틴 2 mg (기타 AREDS2 성분 포함)', '일반': '보충제나 음식으로 하루 루테인 6~20 mg', 'AMD 위험자 전용': 'AREDS2는 중등도~진행성 AMD용이며 건강한 눈에 예방 효과는 없음' },
    dose_ja: { 'AREDS2製剤': '1日ルテイン10 mg + ゼアキサンチン2 mg(その他AREDS2成分含む)', '一般': 'サプリまたは食品から1日ルテイン6~20 mg', 'AMDリスク者専用': 'AREDS2は中等度~進行性AMD用で,健康な眼への予防効果はない' },
    warn_en: 'Very well tolerated. Smokers should NOT take beta-carotene-containing AREDS formulations (lung cancer risk) — AREDS2 replaced beta-carotene with lutein/zeaxanthin for this reason. High doses of zinc in AREDS2 can cause stomach upset.',
    warn_ko: '내약성이 매우 좋음. 흡연자는 베타카로틴 함유 AREDS 제형을 복용하지 마세요 (폐암 위험) — AREDS2는 이런 이유로 베타카로틴을 루테인·지아잔틴으로 교체. AREDS2의 고용량 아연이 위장 장애를 유발할 수 있음.',
    warn_ja: '忍容性は非常に良好。喫煙者はベータカロテン含有AREDS製剤を服用しないでください(肺がんリスク) — AREDS2はこの理由でベータカロテンをルテイン·ゼアキサンチンに置換。AREDS2の高用量亜鉛が胃腸障害を引き起こす可能性。',
    interact: [
      { en: 'Beta-carotene — competes for absorption with lutein (separate products)', ko: '베타카로틴 — 루테인과 흡수 경쟁 (별도 복용)', ja: 'ベータカロテン — ルテインと吸収を競合(別々に服用)' },
      { en: 'Statins — no significant interaction', ko: '스타틴 — 유의미한 상호작용 없음', ja: 'スタチン — 有意な相互作用なし' }
    ],
    source: 'NIH NEI — AREDS2 Study · NIH Office of Dietary Supplements'
  },
  {
    id: 'vitamin-e',
    generic: { en: 'Vitamin E (alpha-tocopherol)', ko: '비타민 E (알파토코페롤)', ja: 'ビタミンE(アルファトコフェロール)' },
    brands: ['Nature Made', 'Solgar', 'NOW Foods'],
    category: 'supplement',
    uses: [
      { title_en: 'Correction of vitamin E deficiency', title_ko: '비타민 E 결핍 교정', title_ja: 'ビタミンE欠乏の是正', evidence: 'strong',
        detail_en: 'Treats rare deficiency, usually from fat malabsorption disorders',
        detail_ko: '주로 지방 흡수 장애로 인한 드문 결핍을 치료',
        detail_ja: '主に脂肪吸収障害による稀な欠乏症を治療' },
      { title_en: 'Antioxidant support', title_ko: '항산화 지원', title_ja: '抗酸化サポート', evidence: 'emerging',
        detail_en: 'Fat-soluble antioxidant found in nuts, seeds, and leafy greens; best obtained from food',
        detail_ko: '견과류, 씨앗, 잎채소에 함유된 지용성 항산화제; 음식 섭취가 최선',
        detail_ja: 'ナッツ,種子,葉物野菜に含まれる脂溶性抗酸化物質;食事からの摂取が最良' },
      { title_en: 'AMD (as part of AREDS2)', title_ko: '황반변성 (AREDS2 일부)', title_ja: '黄斑変性(AREDS2の一部)', evidence: 'strong',
        detail_en: 'Component of AREDS2 formula for intermediate/advanced AMD',
        detail_ko: '중등도~진행성 AMD용 AREDS2 제형의 구성 성분',
        detail_ja: '中等度~進行性AMD用AREDS2製剤の構成成分' }
    ],
    dose_en: { 'Adult RDA': '15 mg (22.4 IU) daily', 'Typical supplement': '100–400 IU daily', 'Upper limit': '1000 mg/day (1500 IU)', 'Quality': 'Natural d-alpha-tocopherol is better absorbed than synthetic dl-alpha-tocopherol' },
    dose_ko: { '성인 RDA': '하루 15 mg (22.4 IU)', '일반 보충': '하루 100~400 IU', '상한': '하루 1000 mg (1500 IU)', '품질': '천연 d-알파토코페롤이 합성 dl-알파토코페롤보다 흡수 양호' },
    dose_ja: { '成人RDA': '1日15 mg(22.4 IU)', '一般補充': '1日100~400 IU', '上限': '1日1000 mg(1500 IU)', '品質': '天然d-アルファトコフェロールが合成dl-アルファトコフェロールより吸収良好' },
    overuse_en: 'HIGH-DOSE VITAMIN E INCREASES BLEEDING AND STROKE RISK — A major trial (SELECT) found 400 IU/day increased prostate cancer risk by 17% in men. Another meta-analysis showed doses over 400 IU/day increased overall mortality. Many Korean households take 1000 IU "for heart health" — this is dangerous. If you take blood thinners, even 100 IU daily can increase bleeding. Get vitamin E from almonds, sunflower seeds, and leafy greens instead.',
    overuse_ko: '고용량 비타민 E는 출혈과 뇌졸중 위험을 증가시킵니다 — 대규모 임상시험(SELECT)에서 하루 400 IU가 남성의 전립선암 위험을 17% 증가시켰습니다. 다른 메타분석에서는 하루 400 IU 이상이 전반적 사망률을 증가시켰습니다. 많은 한인 가정에서 "심장에 좋다"며 1000 IU를 복용하는데 이는 위험합니다. 혈액 희석제 복용자는 하루 100 IU도 출혈을 증가시킬 수 있습니다. 아몬드, 해바라기씨, 잎채소에서 섭취하는 것이 권장됩니다.',
    overuse_ja: '高用量ビタミンEは出血と脳卒中リスクを増加させます — 大規模臨床試験(SELECT)で1日400 IUが男性の前立腺がんリスクを17%増加させました。他のメタ解析では1日400 IU超が全体の死亡率を増加させました。多くの家庭で「心臓に良い」と1000 IUを服用していますが,これは危険です。抗凝固薬服用者は1日100 IUでも出血を増加させる可能性があります。アーモンド,ひまわりの種,葉物野菜から摂取することを推奨します。',
    warn_en: 'Stop 1 week before surgery (bleeding risk). Rare allergic reactions possible. People with history of stroke or bleeding disorders should avoid high doses.',
    warn_ko: '수술 1주 전 중단 (출혈 위험). 드문 알레르기 반응 가능. 뇌졸중 병력이나 출혈 장애가 있으면 고용량을 피하세요.',
    warn_ja: '手術1週間前に中止(出血リスク)。稀にアレルギー反応の可能性。脳卒中の既往や出血障害がある場合は高用量を避けてください。',
    interact: [
      { en: 'Warfarin, aspirin, other blood thinners — significantly increased bleeding risk', ko: '와파린, 아스피린, 기타 혈액 희석제 — 출혈 위험 크게 증가', ja: 'ワルファリン,アスピリン,その他抗凝固薬 — 出血リスク大幅増加' },
      { en: 'Chemotherapy and radiation — may reduce effectiveness (ask oncologist)', ko: '항암제·방사선 치료 — 효과 감소 가능 (종양내과 상담)', ja: '抗がん剤·放射線治療 — 効果低下の可能性(腫瘍内科に相談)' },
      { en: 'Cholesterol medications (statins, niacin) — may interfere with HDL benefit', ko: '콜레스테롤약 (스타틴, 나이아신) — HDL 이점 방해 가능', ja: 'コレステロール薬(スタチン,ナイアシン) — HDLの利益を妨げる可能性' }
    ],
    source: 'NIH Office of Dietary Supplements — Vitamin E Fact Sheet · SELECT Trial (JAMA 2011)'
  },
  {
    id: 'vitamin-k2',
    generic: { en: 'Vitamin K2 (menaquinone)', ko: '비타민 K2 (메나퀴논)', ja: 'ビタミンK2(メナキノン)' },
    brands: ['Life Extension', 'NOW Foods MK-7', 'Jarrow MK-7'],
    category: 'supplement',
    uses: [
      { title_en: 'Bone health (with vitamin D and calcium)', title_ko: '뼈 건강 (비타민 D·칼슘과 함께)', title_ja: '骨の健康(ビタミンD·カルシウムと併用)', evidence: 'emerging',
        detail_en: 'Helps direct calcium into bones rather than arteries; Japanese trials show benefit in postmenopausal osteoporosis',
        detail_ko: '칼슘을 동맥이 아닌 뼈로 향하게 도움; 일본 임상시험에서 폐경 후 골다공증에 이득 확인',
        detail_ja: 'カルシウムを動脈ではなく骨へ向ける助けとなる;日本の臨床試験で閉経後骨粗鬆症への利益を確認' },
      { title_en: 'Cardiovascular health', title_ko: '심혈관 건강', title_ja: '心血管健康', evidence: 'emerging',
        detail_en: 'May reduce arterial calcification; data mostly from Rotterdam Study observational research',
        detail_ko: '동맥 석회화를 감소시킬 수 있음; 근거는 주로 로테르담 연구의 관찰 데이터',
        detail_ja: '動脈石灰化を低下させる可能性;エビデンスは主にロッテルダム研究の観察データ' }
    ],
    dose_en: { 'Typical': '90–180 mcg MK-7 daily', 'Higher dose (MK-4)': '15 mg three times daily (used in Japanese osteoporosis trials)', 'With fat': 'Take with a meal containing fat for absorption' },
    dose_ko: { '일반': '하루 MK-7 90~180 mcg', '고용량 (MK-4)': '하루 3회 15 mg (일본 골다공증 임상시험 용량)', '복용법': '흡수 위해 지방 포함 식사와 함께' },
    dose_ja: { '一般': '1日MK-7 90~180 mcg', '高用量(MK-4)': '1日3回15 mg(日本の骨粗鬆症臨床試験用量)', '服用法': '吸収のため脂質を含む食事と一緒に' },
    overuse_en: 'DANGEROUS INTERACTION WITH WARFARIN — Vitamin K directly opposes warfarin. If you take warfarin (Coumadin, 와파린), adding K2 without doctor supervision can cause clots, strokes, or heart attacks. INR must be monitored closely. Many elderly Koreans take both "for circulation" without telling their doctor — this is a medical emergency waiting to happen. Tell your doctor before starting ANY supplement if you are on warfarin.',
    overuse_ko: '와파린과 위험한 상호작용 — 비타민 K는 와파린과 직접 반대로 작용합니다. 와파린(쿠마딘, Coumadin)을 복용 중이라면 의사 감독 없이 K2를 추가하면 혈전, 뇌졸중, 심장마비를 일으킬 수 있습니다. INR을 면밀히 모니터링해야 합니다. 많은 한인 고령자가 "혈액순환에 좋다"며 둘 다 복용하고 의사에게 알리지 않는데, 이는 응급 상황을 기다리는 것과 같습니다. 와파린 복용자는 어떤 보충제든 시작 전에 의사에게 알리세요.',
    overuse_ja: 'ワルファリンとの危険な相互作用 — ビタミンKはワルファリンと直接反対に作用します。ワルファリン(クマジン,Coumadin)服用中に医師の監督なしにK2を追加すると,血栓,脳卒中,心筋梗塞を引き起こす可能性があります。INRを綿密にモニタリングする必要があります。多くの高齢者が「血流に良い」と両方を服用し医師に伝えていませんが,これは救急事態を待つようなものです。ワルファリン服用者はどのサプリでも開始前に医師に伝えてください。',
    warn_en: 'Generally safe otherwise. If you have a clotting disorder or take blood thinners, consult doctor first. The RDA is easily met by leafy greens (K1) and fermented foods like natto (K2).',
    warn_ko: '그 외에는 일반적으로 안전. 응고 장애가 있거나 혈액 희석제 복용 시 먼저 의사와 상담. RDA는 잎채소(K1)와 낫토 같은 발효 식품(K2)으로 쉽게 충족됩니다.',
    warn_ja: 'それ以外は一般に安全。凝固障害がある場合や抗凝固薬服用中は先に医師に相談。RDAは葉物野菜(K1)と納豆などの発酵食品(K2)で容易に充足。',
    interact: [
      { en: 'Warfarin — DIRECTLY COUNTERACTS warfarin (do not start without doctor)', ko: '와파린 — 와파린을 직접 상쇄 (의사 상담 없이 시작 금지)', ja: 'ワルファリン — ワルファリンを直接相殺(医師の相談なしに開始禁止)' },
      { en: 'Antibiotics (long-term) — can lower vitamin K levels', ko: '항생제 (장기) — 비타민 K 수치 저하 가능', ja: '抗生物質(長期) — ビタミンK値低下の可能性' },
      { en: 'Bile acid sequestrants, orlistat — reduce absorption', ko: '담즙산 결합제, 오르리스타트 — 흡수 감소', ja: '胆汁酸吸着薬,オルリスタット — 吸収低下' }
    ],
    source: 'NIH Office of Dietary Supplements — Vitamin K Fact Sheet'
  },
  {
    id: 'nac',
    generic: { en: 'N-acetylcysteine (NAC)', ko: 'N-아세틸시스테인 (NAC)', ja: 'N-アセチルシステイン(NAC)' },
    brands: ['NOW Foods', 'Jarrow', 'Life Extension'],
    category: 'supplement',
    uses: [
      { title_en: 'Acetaminophen overdose antidote (hospital)', title_ko: '아세트아미노펜 과다복용 해독제 (병원)', title_ja: 'アセトアミノフェン過量服用解毒薬(病院)', evidence: 'strong',
        detail_en: 'FDA-approved prescription use — life-saving IV treatment in ER for Tylenol overdose. OTC oral NAC is NOT a substitute if overdose has occurred — go to ER immediately.',
        detail_ko: 'FDA 승인 처방 용도 — 타이레놀 과다복용 시 응급실 정맥주사 치료로 생명 구조. 과다복용 발생 시 OTC 경구 NAC는 대체 불가 — 즉시 응급실.',
        detail_ja: 'FDA承認処方用途 — タイレノール過量服用時の救急静脈内投与で救命。過量服用発生時にOTC経口NACは代替不可 — 直ちに救急受診。' },
      { title_en: 'Chronic bronchitis / COPD mucus thinning', title_ko: '만성 기관지염·COPD 가래 묽게 하기', title_ja: '慢性気管支炎·COPDの痰の希釈', evidence: 'emerging',
        detail_en: 'Some evidence for reducing COPD exacerbations',
        detail_ko: 'COPD 악화 감소에 대한 일부 근거',
        detail_ja: 'COPD増悪減少に対する一部のエビデンス' },
      { title_en: 'Liver support (anecdotal)', title_ko: '간 건강 (경험적)', title_ja: '肝臓の健康(経験的)', evidence: 'limited',
        detail_en: 'Popular supplement for liver health; glutathione precursor but clinical benefit for healthy livers is unclear',
        detail_ko: '간 건강용으로 인기있는 보충제; 글루타티온 전구체지만 건강한 간에 대한 임상적 이득은 불분명',
        detail_ja: '肝臓の健康用として人気のサプリ;グルタチオン前駆体だが健常肝臓への臨床的利益は不明' }
    ],
    dose_en: { 'Typical': '600–1800 mg daily in divided doses', 'COPD': '600 mg twice daily', 'Sulfur smell': 'NAC has strong sulfur odor — take with food/juice' },
    dose_ko: { '일반': '하루 600~1800 mg, 나누어 복용', 'COPD': '600 mg 하루 2회', '황 냄새': 'NAC는 강한 황 냄새 — 음식·주스와 함께 복용' },
    dose_ja: { '一般': '1日600~1800 mg,分割服用', 'COPD': '600 mgを1日2回', '硫黄臭': 'NACは強い硫黄臭 — 食品·ジュースと一緒に服用' },
    overuse_en: '"LIVER DETOX" MYTH — Many people take NAC while drinking heavily or using acetaminophen, believing it "protects the liver." This is a dangerous misconception. NAC does NOT make it safe to drink alcohol or exceed Tylenol doses. If you are overdrinking or overdosing acetaminophen, the liver is still being damaged. Excess NAC itself can cause nausea, vomiting, diarrhea, low blood pressure. Korean ginseng and liver supplements often marketed with NAC are not FDA-verified for any liver benefit.',
    overuse_ko: '"간 해독" 신화 — 많은 사람들이 과음하거나 아세트아미노펜을 복용하면서 NAC를 같이 먹으며 "간을 보호한다"고 믿습니다. 이는 위험한 오해입니다. NAC는 음주나 타이레놀 초과 복용을 안전하게 만들지 않습니다. 과음이나 아세트아미노펜 과다복용 시 간은 여전히 손상됩니다. NAC 자체의 과량 복용은 메스꺼움, 구토, 설사, 저혈압을 유발할 수 있습니다. NAC가 함유된 한국 인삼·간 보충제는 간 이점에 대한 FDA 검증이 없습니다.',
    overuse_ja: '「肝臓デトックス」の神話 — 多くの人が過度の飲酒中やアセトアミノフェン服用中にNACを併用して「肝臓を保護する」と信じています。これは危険な誤解です。NACは飲酒やタイレノール過量服用を安全にはしません。過度の飲酒やアセトアミノフェン過量服用時は肝臓は依然として損傷します。NAC自体の過量服用は吐き気,嘔吐,下痢,低血圧を引き起こす可能性があります。NAC含有の人参·肝臓サプリは肝臓への利益についてFDAの検証はありません。',
    warn_en: 'May cause asthma-like reactions in sensitive people. FDA has historically regulated NAC as a drug; current OTC status is in regulatory flux. If symptoms of liver disease (yellowing skin/eyes, dark urine, severe fatigue) — see doctor, do not self-treat with NAC.',
    warn_ko: '민감한 사람에게 천식 유사 반응을 일으킬 수 있음. FDA는 NAC를 의약품으로 규제해 왔으며 현재 OTC 지위는 규제 변동 중. 간 질환 증상(피부·눈 황변, 진한 소변, 심한 피로)이 있으면 의사를 만나고 NAC로 자가치료하지 마세요.',
    warn_ja: '敏感な人に喘息様反応を引き起こす可能性。FDAはNACを医薬品として規制してきており,現在のOTC地位は規制変動中。肝疾患症状(皮膚·眼の黄染,濃い尿,強い疲労)がある場合,医師の診察を受け,NACで自己治療しないでください。',
    interact: [
      { en: 'Nitroglycerin — may enhance effect, causing low blood pressure and headaches', ko: '니트로글리세린 — 효과 증강으로 저혈압·두통 유발 가능', ja: 'ニトログリセリン — 効果増強による低血圧·頭痛の可能性' },
      { en: 'Activated charcoal — reduces NAC absorption', ko: '활성탄 — NAC 흡수 감소', ja: '活性炭 — NAC吸収低下' },
      { en: 'Blood thinners — may increase bleeding risk at high doses', ko: '혈액 희석제 — 고용량에서 출혈 위험 증가', ja: '抗凝固薬 — 高用量で出血リスク増加' }
    ],
    source: 'NIH MedlinePlus · NIH National Center for Complementary and Integrative Health'
  },
  {
    id: 'turmeric',
    generic: { en: 'Turmeric / Curcumin', ko: '강황 / 커큐민', ja: 'ウコン/クルクミン' },
    brands: ['NOW Foods', 'Gaia Herbs', 'Qunol'],
    category: 'supplement',
    uses: [
      { title_en: 'Osteoarthritis pain (modest benefit)', title_ko: '골관절염 통증 (경미한 이득)', title_ja: '変形性関節症の痛み(軽度の利益)', evidence: 'emerging',
        detail_en: 'Some randomized trials show modest pain reduction comparable to NSAIDs for knee osteoarthritis',
        detail_ko: '일부 무작위 임상시험에서 무릎 골관절염에 대해 NSAID와 비슷한 경미한 통증 감소 확인',
        detail_ja: '一部のランダム化臨床試験で膝変形性関節症に対しNSAIDと同程度の軽度の鎮痛を確認' },
      { title_en: 'General anti-inflammatory', title_ko: '일반 항염증', title_ja: '一般抗炎症', evidence: 'limited',
        detail_en: 'Widely marketed as anti-inflammatory but clinical evidence for most conditions is limited',
        detail_ko: '항염증제로 널리 홍보되지만 대부분의 질환에 대한 임상 근거는 제한적',
        detail_ja: '抗炎症剤として広く宣伝されているが,ほとんどの疾患に対する臨床的エビデンスは限定的' }
    ],
    dose_en: { 'Typical': '500–1500 mg curcumin daily in divided doses', 'Absorption': 'Poor absorption alone — combined with piperine (black pepper) or liposomal/nano forms for better uptake', 'With food': 'Take with fatty meal' },
    dose_ko: { '일반': '하루 커큐민 500~1500 mg, 나누어 복용', '흡수': '단독 복용 시 흡수율이 낮음 — 피페린(후추) 병용 또는 리포솜/나노 제형이 흡수 양호', '복용법': '지방 포함 식사와 함께' },
    dose_ja: { '一般': '1日クルクミン500~1500 mg,分割服用', '吸収': '単独服用では吸収率が低い — ピペリン(黒胡椒)併用またはリポソーム/ナノ製剤で吸収良好', '服用法': '脂質を含む食事と一緒に' },
    overuse_en: 'LIVER DAMAGE — High-potency turmeric/curcumin products with piperine enhancement have caused dozens of acute liver injury cases since 2017 (documented in LiverTox database, NIH). The US NIH issued warnings in 2023. Symptoms: yellowing of skin/eyes, dark urine, fatigue, nausea. More common with high doses (>1000 mg/day) and products combining curcumin with absorption enhancers. Many Korean households take "high-absorption" turmeric believing more is better — it is NOT.',
    overuse_ko: '간 손상 — 피페린이 첨가된 고농도 강황·커큐민 제품이 2017년 이후 수십 건의 급성 간 손상을 일으켰습니다 (NIH LiverTox 데이터베이스 기록). 미국 NIH는 2023년 경고를 발표했습니다. 증상: 피부·눈 황변, 진한 소변, 피로, 메스꺼움. 고용량(하루 1000 mg 이상) 및 커큐민과 흡수 촉진제 복합 제품에서 더 흔합니다. 많은 한인 가정에서 "많을수록 좋다"며 "고흡수" 강황을 복용하는데 이는 잘못된 믿음입니다.',
    overuse_ja: '肝障害 — ピペリン添加の高濃度ウコン·クルクミン製品が2017年以降数十件の急性肝障害を引き起こしました(NIH LiverToxデータベース記録)。米国NIHは2023年に警告を発表しました。症状:皮膚·眼の黄染,濃い尿,疲労,吐き気。高用量(1日1000 mg超)およびクルクミンと吸収促進剤の複合製品でより一般的。多くの家庭で「多いほど良い」と「高吸収」ウコンを服用していますが,これは誤った信念です。',
    warn_en: 'Can increase bleeding — stop 2 weeks before surgery. May worsen gallbladder disease. Can reduce absorption of iron and some medications. Pregnancy: culinary amounts OK, supplement doses not recommended.',
    warn_ko: '출혈 증가 가능 — 수술 2주 전 중단. 담낭 질환 악화 가능. 철분 및 일부 약물 흡수 감소. 임신 중: 음식 양은 괜찮으나 보충제 용량은 권장되지 않음.',
    warn_ja: '出血増加の可能性 — 手術2週間前に中止。胆嚢疾患の悪化の可能性。鉄および一部の薬の吸収低下。妊娠中:食品量は問題ないがサプリ用量は推奨されない。',
    interact: [
      { en: 'Blood thinners (warfarin, aspirin) — increased bleeding risk', ko: '혈액 희석제 (와파린, 아스피린) — 출혈 위험 증가', ja: '抗凝固薬(ワルファリン,アスピリン) — 出血リスク増加' },
      { en: 'Diabetes medications — may enhance blood sugar lowering', ko: '당뇨병약 — 혈당 저하 효과 증강 가능', ja: '糖尿病薬 — 血糖低下効果増強の可能性' },
      { en: 'Iron supplements — curcumin reduces iron absorption', ko: '철분제 — 커큐민이 철분 흡수 감소', ja: '鉄剤 — クルクミンが鉄吸収を低下' },
      { en: 'Chemotherapy — possible interference (ask oncologist)', ko: '항암제 — 상호작용 가능 (종양내과 상담)', ja: '抗がん剤 — 相互作用の可能性(腫瘍内科に相談)' }
    ],
    source: 'NIH NCCIH · LiverTox Database (NIDDK/NIH) · NIH ODS'
  },
  {
    id: 'ginger',
    generic: { en: 'Ginger (Zingiber officinale)', ko: '생강', ja: 'ショウガ' },
    brands: ['Nature\'s Way', 'NOW Foods', 'Gaia Herbs'],
    category: 'supplement',
    uses: [
      { title_en: 'Nausea (pregnancy, motion, post-surgery, chemo)', title_ko: '메스꺼움 (임신, 멀미, 수술 후, 항암치료)', title_ja: '吐き気(妊娠,乗り物酔い,術後,化学療法)', evidence: 'strong',
        detail_en: 'One of the best-studied natural antiemetics; comparable to some prescription medications for pregnancy-related nausea',
        detail_ko: '가장 잘 연구된 천연 항구토제 중 하나; 임신성 메스꺼움에 대해 일부 처방약과 비슷한 효과',
        detail_ja: '最もよく研究された天然制吐剤の一つ;妊娠関連吐き気に対して一部の処方薬と同程度の効果' },
      { title_en: 'Menstrual cramps', title_ko: '생리통', title_ja: '生理痛', evidence: 'emerging',
        detail_en: 'Some trials suggest benefit comparable to NSAIDs',
        detail_ko: '일부 임상시험에서 NSAID와 비슷한 이득 확인',
        detail_ja: '一部の臨床試験でNSAIDと同程度の利益を確認' },
      { title_en: 'Digestion and bloating', title_ko: '소화·복부 팽만', title_ja: '消化·腹部膨満', evidence: 'emerging',
        detail_en: 'Traditional use supported by some modern evidence',
        detail_ko: '전통적 사용이 일부 현대 근거로 뒷받침',
        detail_ja: '伝統的使用が一部の現代的エビデンスで裏付け' }
    ],
    dose_en: { 'Nausea': '250 mg 4 times daily, or 1 gram total daily', 'Fresh ginger tea': 'Safe and effective — slice 1 inch, steep in hot water', 'Pregnancy': 'Up to 1 gram/day is considered safe; consult OB', 'Capsules': 'Typically 500–1000 mg daily' },
    dose_ko: { '메스꺼움': '250 mg 하루 4회, 또는 하루 총 1 g', '생강차': '안전하고 효과적 — 2.5 cm 두께로 썰어 뜨거운 물에 우림', '임신': '하루 1 g까지 안전으로 간주; 산부인과 상담', '캡슐': '보통 하루 500~1000 mg' },
    dose_ja: { '吐き気': '250 mgを1日4回,または1日合計1 g', '生姜茶': '安全で効果的 — 2.5 cmにスライスして熱湯に浸出', '妊娠': '1日1 gまで安全と見なされる;産婦人科に相談', 'カプセル': '通常1日500~1000 mg' },
    overuse_en: 'BLEEDING RISK — High-dose ginger supplements (>4 g/day) can increase bleeding, especially with warfarin or aspirin. A common Korean practice is drinking concentrated ginger tea (생강차) daily for "blood circulation" while taking aspirin — this is a bleeding risk. Food-level ginger in cooking is safe and healthy; concentrated supplements and extracts are different. If you bruise easily or take blood thinners, limit to culinary use.',
    overuse_ko: '출혈 위험 — 고용량 생강 보충제(하루 4 g 이상)는 특히 와파린이나 아스피린 병용 시 출혈을 증가시킬 수 있습니다. 한국인의 흔한 습관으로 아스피린을 복용하면서 매일 진한 생강차를 "혈액순환용으로" 마시는데, 이는 출혈 위험입니다. 요리에 사용하는 음식 수준의 생강은 안전하고 건강에 좋지만, 농축 보충제와 추출물은 다릅니다. 쉽게 멍들거나 혈액 희석제를 복용 중이면 요리용으로만 제한하세요.',
    overuse_ja: '出血リスク — 高用量ショウガサプリ(1日4 g超)は,特にワルファリンやアスピリン併用時に出血を増加させる可能性があります。一般的な習慣として,アスピリン服用中に毎日濃い生姜茶を「血流改善」のために飲むケースがありますが,これは出血リスクです。料理に使う食品レベルのショウガは安全で健康に良いですが,濃縮サプリと抽出物は異なります。あざができやすい場合や抗凝固薬服用中は料理用のみに制限してください。',
    warn_en: 'May lower blood sugar — monitor if diabetic. May lower blood pressure. Gallstone patients should avoid. Stop 2 weeks before surgery.',
    warn_ko: '혈당을 낮출 수 있음 — 당뇨 시 모니터링. 혈압을 낮출 수 있음. 담석 환자는 피하세요. 수술 2주 전 중단.',
    warn_ja: '血糖を低下させる可能性 — 糖尿病時はモニタリング。血圧を低下させる可能性。胆石患者は避けてください。手術2週間前に中止。',
    interact: [
      { en: 'Blood thinners — increased bleeding risk', ko: '혈액 희석제 — 출혈 위험 증가', ja: '抗凝固薬 — 出血リスク増加' },
      { en: 'Diabetes medications — may enhance blood sugar lowering', ko: '당뇨병약 — 혈당 저하 효과 증강 가능', ja: '糖尿病薬 — 血糖低下効果増強の可能性' },
      { en: 'Blood pressure medications — additive lowering', ko: '혈압약 — 저하 효과 누적', ja: '降圧薬 — 低下効果の累積' }
    ],
    source: 'NIH NCCIH · NIH ODS'
  },
  {
    id: 'elderberry',
    generic: { en: 'Elderberry (Sambucus nigra)', ko: '엘더베리 (딱총나무 열매)', ja: 'エルダーベリー(西洋ニワトコの実)' },
    brands: ['Sambucol', 'Nature\'s Way Sambucus', 'Gaia Herbs'],
    category: 'supplement',
    uses: [
      { title_en: 'Cold and flu duration reduction', title_ko: '감기·독감 기간 단축', title_ja: '風邪·インフルエンザの期間短縮', evidence: 'emerging',
        detail_en: 'Small trials suggest elderberry syrup/lozenges may shorten flu/cold duration by 2–4 days when started within 48 hours of symptoms',
        detail_ko: '소규모 임상시험에서 증상 48시간 이내 시작 시 독감·감기 기간을 2~4일 단축 가능성',
        detail_ja: '小規模臨床試験で症状48時間以内に開始した際にインフルエンザ·風邪の期間を2~4日短縮する可能性' }
    ],
    dose_en: { 'Syrup': '15 mL 4 times daily for up to 5 days at symptom onset', 'Lozenges': '175 mg 2–4 times daily', 'Form': 'Use only commercially prepared products — RAW elderberries, bark, and leaves contain CYANIDE and cause severe vomiting/diarrhea' },
    dose_ko: { '시럽': '증상 시작 시 하루 4회 15 mL, 최대 5일', '로젠지': '175 mg 하루 2~4회', '제형': '상용 제품만 사용 — 생 엘더베리, 나무껍질, 잎은 시안화물 함유로 심한 구토·설사 유발' },
    dose_ja: { 'シロップ': '症状開始時に1日4回15 mL,最大5日間', 'ロゼンジ': '175 mgを1日2~4回', '製剤': '市販製品のみ使用 — 生のエルダーベリー,樹皮,葉はシアン化物を含み激しい嘔吐·下痢を引き起こす' },
    overuse_en: 'RAW ELDERBERRY IS TOXIC — Every year, people get severely sick drinking "homemade" elderberry juice from uncooked berries, thinking natural = safe. Raw berries, leaves, and bark contain cyanogenic glycosides that release cyanide in the body. Only use commercially prepared, heat-treated products. Also, during COVID-19, many Korean media promoted elderberry as an immune booster — theoretical concern about over-stimulating immune system (cytokine storm) in severe viral illness was raised but not confirmed. Still, do not megadose in acute illness without medical advice.',
    overuse_ko: '생 엘더베리는 독성입니다 — 매년 생 열매로 "집에서 만든" 엘더베리 주스를 마시고 심하게 아픈 사람이 발생합니다. "천연=안전"이라는 착각 때문입니다. 생 열매, 잎, 나무껍질은 시안생성 배당체를 함유하여 체내에서 시안화물을 방출합니다. 상용 제품 중 가열 처리된 것만 사용하세요. 또한 COVID-19 기간 동안 한국 언론에서 엘더베리를 면역 증강제로 홍보했는데, 중증 바이러스 질환에서 면역계 과자극(사이토카인 폭풍) 우려가 제기되었으나 확인되지는 않았습니다. 그럼에도 급성 질환 시 의료 조언 없이 대용량 복용은 피하세요.',
    overuse_ja: '生のエルダーベリーは有毒です — 毎年,加熱されていない実から作った「自家製」エルダーベリージュースを飲んで重症化する人が発生します。「天然=安全」という誤認のためです。生の実,葉,樹皮はシアン生成配糖体を含み体内でシアン化物を放出します。市販製品のうち加熱処理されたもののみ使用してください。また,COVID-19期間中にエルダーベリーが免疫増強剤として宣伝されましたが,重症ウイルス疾患での免疫系過剰刺激(サイトカインストーム)の懸念が提起されたものの確認はされませんでした。それでも急性疾患時に医療助言なく大量服用は避けてください。',
    warn_en: 'Use only for 5 days at a time during illness, not as a daily supplement. Do not use in children under 1. Stop if nausea, vomiting, or severe diarrhea.',
    warn_ko: '질병 시 한 번에 5일만 사용하고, 상시 보충제로 사용하지 마세요. 1세 미만 어린이에게 사용 금지. 메스꺼움, 구토, 심한 설사 시 중단.',
    warn_ja: '疾患時に一度に5日間のみ使用し,日常サプリとして使用しないでください。1歳未満の小児に使用禁止。吐き気,嘔吐,激しい下痢があれば中止。',
    interact: [
      { en: 'Immunosuppressants — theoretical interference', ko: '면역 억제제 — 이론적 상호작용', ja: '免疫抑制薬 — 理論的相互作用' },
      { en: 'Diabetes medications — may lower blood sugar', ko: '당뇨병약 — 혈당 저하 가능', ja: '糖尿病薬 — 血糖低下の可能性' },
      { en: 'Diuretics — possible additive effect', ko: '이뇨제 — 효과 누적 가능', ja: '利尿薬 — 効果累積の可能性' }
    ],
    source: 'NIH NCCIH · NIH ODS'
  },
  {
    id: 'echinacea',
    generic: { en: 'Echinacea (E. purpurea, E. angustifolia)', ko: '에키네시아', ja: 'エキナセア' },
    brands: ['Nature\'s Way', 'Gaia Herbs', 'Airborne'],
    category: 'supplement',
    uses: [
      { title_en: 'Common cold (prevention and treatment)', title_ko: '감기 (예방·치료)', title_ja: '風邪(予防·治療)', evidence: 'limited',
        detail_en: 'Mixed evidence — some reviews find small benefit for cold duration, others find none. Effects may depend on species and preparation.',
        detail_ko: '근거 혼재 — 일부 리뷰는 감기 기간에 작은 이득, 다른 리뷰는 효과 없음. 종과 제형에 따라 효과가 달라질 수 있음.',
        detail_ja: 'エビデンス混在 — 一部のレビューは風邪の期間に小さな利益,他は効果なし。種と製剤により効果が異なる可能性。' }
    ],
    dose_en: { 'Typical for cold': '300–500 mg 3 times daily at symptom onset, up to 7 days', 'Do not use continuously': 'Best used short-term when symptoms appear', 'Species matters': 'E. purpurea aerial parts and E. angustifolia root are most studied' },
    dose_ko: { '감기용 일반': '증상 시작 시 300~500 mg 하루 3회, 최대 7일', '지속 사용 금지': '증상이 있을 때 단기 사용이 최선', '종 중요': 'E. purpurea 지상부와 E. angustifolia 뿌리가 가장 연구됨' },
    dose_ja: { '風邪用一般': '症状開始時に300~500 mgを1日3回,最大7日間', '継続使用禁止': '症状があるときの短期使用が最良', '種が重要': 'E. purpurea地上部とE. angustifolia根が最も研究されている' },
    overuse_en: 'DAILY LONG-TERM USE NOT RECOMMENDED — Many people take echinacea daily "to prevent colds" year-round. This is not supported by evidence and may paradoxically weaken immune response with prolonged use. If you have autoimmune disease (rheumatoid arthritis, lupus, MS, psoriasis), echinacea can trigger flares — do not use. Korean markets often sell echinacea combined with other "immune herbs" — these combinations have not been tested for safety.',
    overuse_ko: '매일 장기 복용은 권장되지 않음 — 많은 사람들이 "감기 예방"으로 에키네시아를 연중 매일 복용합니다. 이는 근거가 뒷받침하지 않으며, 장기 사용은 역설적으로 면역 반응을 약화시킬 수 있습니다. 자가면역질환(류마티스 관절염, 루푸스, 다발성경화증, 건선) 환자는 에키네시아가 재발을 유발할 수 있으니 사용하지 마세요. 한인 상점에서 에키네시아를 다른 "면역 허브"와 혼합한 제품을 판매하는데, 이런 복합제는 안전성 검증이 되지 않았습니다.',
    overuse_ja: '毎日の長期服用は推奨されません — 多くの人が「風邪予防」として年間を通じて毎日エキナセアを服用しています。これはエビデンスで裏付けられておらず,長期使用は逆説的に免疫応答を弱める可能性があります。自己免疫疾患(関節リウマチ,ループス,多発性硬化症,乾癬)患者にはエキナセアが再発を引き起こす可能性があるため使用しないでください。エキナセアを他の「免疫ハーブ」と混合した製品が販売されていますが,これらの複合剤は安全性が検証されていません。',
    warn_en: 'Do not use if you have autoimmune disease, HIV, tuberculosis, or are taking immunosuppressants. Allergic reactions possible, especially in people allergic to ragweed, chrysanthemums, marigolds, or daisies. Stop if rash appears.',
    warn_ko: '자가면역질환, HIV, 결핵이 있거나 면역 억제제 복용 시 사용하지 마세요. 돼지풀, 국화, 금잔화, 데이지에 알레르기가 있는 사람에게 알레르기 반응 가능. 발진 시 중단.',
    warn_ja: '自己免疫疾患,HIV,結核がある場合,または免疫抑制薬服用時は使用しないでください。ブタクサ,菊,マリーゴールド,デイジーにアレルギーがある人にアレルギー反応の可能性。発疹があれば中止。',
    interact: [
      { en: 'Immunosuppressants (tacrolimus, cyclosporine, methotrexate) — avoid combination', ko: '면역 억제제 (타크롤리무스, 사이클로스포린, 메토트렉세이트) — 병용 금지', ja: '免疫抑制薬(タクロリムス,シクロスポリン,メトトレキサート) — 併用禁止' },
      { en: 'CYP450-metabolized drugs — may alter levels', ko: 'CYP450 대사 약물 — 농도 변화 가능', ja: 'CYP450代謝薬 — 濃度変化の可能性' }
    ],
    source: 'NIH NCCIH · NIH ODS'
  },
  {
    id: 'ashwagandha',
    generic: { en: 'Ashwagandha (Withania somnifera)', ko: '아슈와간다', ja: 'アシュワガンダ (Withania somnifera)' },
    brands: ['KSM-66 (various)', 'Gaia Herbs', 'Nature\'s Way'],
    category: 'supplement',
    uses: [
      { title_en: 'Stress and anxiety', title_ko: '스트레스·불안', title_ja: 'ストレス·不安', evidence: 'emerging',
        detail_en: 'Several trials show modest reduction in perceived stress and cortisol over 6–12 weeks',
        detail_ko: '여러 임상시험에서 6~12주에 걸쳐 지각된 스트레스와 코르티솔의 경미한 감소 확인',
        detail_ja: '複数の臨床試験で6~12週にわたり知覚ストレスとコルチゾールの軽度の低下を確認' },
      { title_en: 'Sleep quality', title_ko: '수면 질', title_ja: '睡眠の質', evidence: 'emerging',
        detail_en: 'May improve sleep latency and quality, often studied as adjunct to stress reduction',
        detail_ko: '수면 잠복기와 질 개선 가능, 주로 스트레스 감소의 보조요법으로 연구됨',
        detail_ja: '入眠潜時と睡眠の質を改善する可能性。主にストレス軽減の補助療法として研究されている' },
      { title_en: 'Exercise performance', title_ko: '운동 수행 능력', title_ja: '運動パフォーマンス', evidence: 'limited',
        detail_en: 'Some evidence for strength and endurance gains, mostly in young men',
        detail_ko: '주로 젊은 남성에서 근력과 지구력 개선에 대한 일부 근거',
        detail_ja: '主に若年男性で筋力·持久力改善に関する一部のエビデンス' }
    ],
    dose_en: { 'Typical (KSM-66 extract)': '300–600 mg daily', 'Duration': 'Effects appear after 4–8 weeks; not for acute anxiety', 'Cycling': 'Many experts recommend 8-week use, 2-week break cycles' },
    dose_ko: { '일반 (KSM-66 추출물)': '하루 300~600 mg', '기간': '4~8주 후 효과 발현; 급성 불안에는 부적합', '주기': '많은 전문가들이 8주 사용 후 2주 휴식 주기 권장' },
    dose_ja: { '一般 (KSM-66エキス)': '1日300~600 mg', '期間': '4~8週後に効果発現;急性不安には不適合', 'サイクル': '多くの専門家が8週間使用後2週間休止のサイクルを推奨' },
    overuse_en: 'LIVER INJURY CASES — NIH LiverTox database has documented over 50 cases of acute liver injury linked to ashwagandha supplements since 2019, including cases requiring hospitalization. Symptoms: jaundice, dark urine, abdominal pain, severe fatigue. Risk is not dose-dependent — some cases occurred at standard doses. Also, ashwagandha can increase thyroid hormone — dangerous if you have hyperthyroidism or take levothyroxine. Korean online shopping has made ashwagandha extremely popular, but do not combine with other herbal supplements.',
    overuse_ko: '간 손상 사례 — NIH LiverTox 데이터베이스에 2019년 이후 아슈와간다 관련 급성 간 손상 50건 이상이 기록되었으며, 일부는 입원이 필요했습니다. 증상: 황달, 진한 소변, 복통, 심한 피로. 위험은 용량 의존적이지 않으며, 표준 용량에서도 발생했습니다. 또한 아슈와간다는 갑상선 호르몬을 증가시킬 수 있어 갑상선 기능 항진증이나 레보티록신 복용 시 위험합니다. 한국 온라인 쇼핑에서 아슈와간다가 매우 인기지만, 다른 허브 보충제와 병용하지 마세요.',
    overuse_ja: '肝障害症例 — NIH LiverToxデータベースに2019年以降アシュワガンダ関連の急性肝障害が50件以上記録されており、入院が必要な症例も含まれます。症状:黄疸、濃い尿、腹痛、重度の疲労。リスクは用量依存的でなく、標準用量でも発生しています。また、アシュワガンダは甲状腺ホルモンを増加させる可能性があり、甲状腺機能亢進症やレボチロキシン服用時に危険です。オンラインショッピングで非常に人気がありますが、他のハーブサプリと併用しないでください。',
    warn_en: 'Do not use in pregnancy (possible miscarriage risk). Avoid if you have thyroid disease, autoimmune disease, or take sedatives. Stop 2 weeks before surgery. Discontinue and see doctor if any sign of liver problem (yellowing, dark urine, right-side abdominal pain).',
    warn_ko: '임신 중 사용 금지 (유산 위험 가능). 갑상선 질환, 자가면역질환, 진정제 복용 시 피하세요. 수술 2주 전 중단. 간 문제 징후(황변, 진한 소변, 우측 복통) 시 중단하고 의사를 만나세요.',
    warn_ja: '妊娠中は使用禁止(流産リスクの可能性)。甲状腺疾患、自己免疫疾患、鎮静薬服用時は避けてください。手術2週間前に中止。肝障害の徴候(黄疸、濃い尿、右側腹痛)があれば中止し医師に相談してください。',
    interact: [
      { en: 'Thyroid medications (levothyroxine) — can enhance thyroid effect', ko: '갑상선약 (레보티록신) — 갑상선 효과 증강 가능', ja: '甲状腺薬(レボチロキシン) — 甲状腺効果増強の可能性' },
      { en: 'Immunosuppressants — may counteract', ko: '면역 억제제 — 상쇄 가능', ja: '免疫抑制薬 — 相殺の可能性' },
      { en: 'Sedatives, sleep aids — additive sedation', ko: '진정제, 수면제 — 진정 효과 누적', ja: '鎮静薬、睡眠薬 — 鎮静効果の相加' },
      { en: 'Diabetes and blood pressure medications — may enhance effect', ko: '당뇨·혈압약 — 효과 증강 가능', ja: '糖尿病·血圧薬 — 効果増強の可能性' }
    ],
    source: 'NIH NCCIH · LiverTox Database (NIDDK/NIH)'
  },
  {
    id: 'biotin',
    generic: { en: 'Biotin (vitamin B7)', ko: '비오틴 (비타민 B7)', ja: 'ビオチン (ビタミンB7)' },
    brands: ['Nature\'s Bounty Hair Skin Nails', 'Sports Research', 'NOW Foods'],
    category: 'supplement',
    uses: [
      { title_en: 'Correction of biotin deficiency (rare)', title_ko: '비오틴 결핍 교정 (드뭄)', title_ja: 'ビオチン欠乏の是正(まれ)', evidence: 'strong',
        detail_en: 'True deficiency is rare; causes hair loss, rash, neurological problems. Treated with supplementation.',
        detail_ko: '진짜 결핍은 드물며, 탈모, 발진, 신경학적 문제 유발. 보충제로 치료.',
        detail_ja: '真の欠乏はまれで、脱毛、発疹、神経学的問題を引き起こす。サプリメントで治療。' },
      { title_en: 'Hair, skin, nails support', title_ko: '모발, 피부, 손톱 지원', title_ja: '髪、肌、爪のサポート', evidence: 'limited',
        detail_en: 'Widely marketed for hair/nail growth but clinical evidence is weak except in biotin-deficient individuals',
        detail_ko: '모발·손톱 성장용으로 널리 홍보되지만, 비오틴 결핍자가 아닌 경우 임상 근거는 약함',
        detail_ja: '髪·爪の成長用途として広く宣伝されているが、ビオチン欠乏者以外では臨床的エビデンスは弱い' }
    ],
    dose_en: { 'Adult AI': '30 mcg daily (easily met by diet)', 'Typical supplement': '2500–10000 mcg (2.5–10 mg) daily — far above AI', 'In supplements': 'Some products contain 20000 mcg — no added benefit' },
    dose_ko: { '성인 AI': '하루 30 mcg (식단으로 쉽게 충족)', '일반 보충제': '하루 2500~10000 mcg (2.5~10 mg) — AI의 수백 배', '제품': '일부 제품은 20000 mcg 함유 — 추가 이득 없음' },
    dose_ja: { '成人AI': '1日30 mcg(食事で容易に充足)', '一般サプリ': '1日2500~10000 mcg(2.5~10 mg) — AIの数百倍', '製品': '一部製品は20000 mcg含有 — 追加の利益なし' },
    overuse_en: 'INTERFERES WITH BLOOD TESTS — FDA issued safety warning (2019) that high-dose biotin causes false results in many blood tests, including thyroid tests, cardiac enzymes (troponin — used to diagnose heart attacks), and hormone tests. At least one death occurred when biotin caused a missed heart attack diagnosis. Many Korean beauty supplements contain 5000–10000 mcg biotin — if you are having any blood test, tell the lab you take biotin and stop for at least 72 hours before testing. The "more is better for hair" belief is wrong — there is no evidence higher doses help normal people.',
    overuse_ko: '혈액 검사 결과 왜곡 — FDA는 2019년 안전 경고를 발표했는데, 고용량 비오틴이 갑상선 검사, 심장 효소(트로포닌 — 심장마비 진단용), 호르몬 검사 등 많은 혈액 검사에서 거짓 결과를 유발합니다. 비오틴으로 심장마비 진단을 놓쳐 사망한 사례가 최소 1건 있습니다. 많은 한국 미용 보충제가 비오틴 5000~10000 mcg을 함유하고 있으니, 혈액 검사를 받을 때는 검사실에 비오틴 복용을 알리고 검사 최소 72시간 전 중단하세요. "많을수록 모발에 좋다"는 믿음은 잘못된 것이며, 정상인에게 고용량이 도움이 된다는 근거는 없습니다.',
    overuse_ja: '血液検査結果の歪曲 — FDAは2019年に安全警告を発表し、高用量ビオチンが甲状腺検査、心筋酵素(トロポニン — 心筋梗塞診断用)、ホルモン検査など多くの血液検査で偽の結果を引き起こすと報告。ビオチンが原因で心筋梗塞の診断を見逃し死亡した症例が少なくとも1例あります。多くの美容サプリがビオチン5000~10000 mcgを含有しているため、血液検査を受ける際は検査室にビオチン服用を伝え、検査72時間前には中止してください。「多いほど髪に良い」という信念は誤りで、正常人に高用量が役立つというエビデンスはありません。',
    warn_en: 'Water-soluble, excess excreted in urine — direct toxicity is uncommon. Main risk is blood test interference. If you take biotin and have unexplained test results, ask your doctor to repeat after 72-hour washout.',
    warn_ko: '수용성이라 과잉분은 소변으로 배출 — 직접 독성은 드묾. 주요 위험은 혈액 검사 방해. 비오틴 복용 중 원인 불명의 검사 이상 결과가 나오면 72시간 휴약 후 재검사를 의사에게 요청하세요.',
    warn_ja: '水溶性のため過剰分は尿中に排泄 — 直接毒性はまれ。主なリスクは血液検査への干渉。ビオチン服用中に原因不明の検査異常が出た場合、72時間休薬後に再検査を医師に依頼してください。',
    interact: [
      { en: 'Blood tests (thyroid, troponin, hormones) — can cause false results — stop 72 hours before testing', ko: '혈액 검사 (갑상선, 트로포닌, 호르몬) — 거짓 결과 유발 — 검사 72시간 전 중단', ja: '血液検査(甲状腺、トロポニン、ホルモン) — 偽結果を引き起こす — 検査72時間前に中止' },
      { en: 'Anticonvulsants (phenytoin, carbamazepine) — may lower biotin levels', ko: '항경련제 (페니토인, 카바마제핀) — 비오틴 수치 저하 가능', ja: '抗てんかん薬(フェニトイン、カルバマゼピン) — ビオチン濃度低下の可能性' }
    ],
    source: 'FDA Safety Communication (2019) · NIH Office of Dietary Supplements'
  },
  {
    id: 'collagen',
    generic: { en: 'Collagen peptides (hydrolyzed collagen)', ko: '콜라겐 펩타이드 (가수분해 콜라겐)', ja: 'コラーゲンペプチド(加水分解コラーゲン)' },
    brands: ['Vital Proteins', 'Great Lakes', 'Ancient Nutrition'],
    category: 'supplement',
    uses: [
      { title_en: 'Skin elasticity and hydration', title_ko: '피부 탄력·수분', title_ja: '肌の弾力·保湿', evidence: 'emerging',
        detail_en: 'Several meta-analyses suggest modest improvements in skin hydration and elasticity over 8–12 weeks',
        detail_ko: '여러 메타분석에서 8~12주에 걸쳐 피부 수분과 탄력에 경미한 개선 시사',
        detail_ja: '複数のメタ解析で8~12週にわたり肌の保湿と弾力の軽度の改善が示唆されている' },
      { title_en: 'Joint pain and osteoarthritis', title_ko: '관절 통증·골관절염', title_ja: '関節痛·変形性関節症', evidence: 'limited',
        detail_en: 'Some trials suggest modest benefit, though evidence is mixed',
        detail_ko: '일부 임상시험에서 경미한 이득을 시사하나 근거는 혼재',
        detail_ja: '一部の臨床試験で軽度の利益が示唆されているが、エビデンスは一貫していない' }
    ],
    dose_en: { 'Typical': '2.5–10 grams daily in water, coffee, or smoothie', 'Hydrolyzed only': 'Non-hydrolyzed collagen is not absorbed; look for hydrolyzed or "peptides"', 'Duration': 'Minimum 8 weeks to assess effect', 'Source': 'Bovine, marine, or chicken — marine best absorbed but more expensive' },
    dose_ko: { '일반': '하루 2.5~10 g을 물, 커피, 스무디에 타서', '가수분해만': '비가수분해 콜라겐은 흡수 안 됨; "hydrolyzed" 또는 "peptides" 표기 확인', '기간': '효과 평가 최소 8주', '원료': '소, 해양, 닭 — 해양이 흡수 최고지만 가격 비쌈' },
    dose_ja: { '一般': '1日2.5~10 gを水、コーヒー、スムージーに混ぜて', '加水分解のみ': '非加水分解コラーゲンは吸収されない;「hydrolyzed」または「peptides」表記を確認', '期間': '効果評価には最低8週間', '原料': '牛、海洋、鶏 — 海洋が最も吸収良好だが高価' },
    overuse_en: 'NOT A PROTEIN SUBSTITUTE — Collagen is an INCOMPLETE protein (lacks tryptophan). Some people take 20–30 g daily as meal replacement, thinking "protein = protein." This can cause amino acid imbalances over time. Also, collagen products often contain heavy metals — a 2018 Clean Label Project test found cadmium, lead, mercury in many popular brands. Choose NSF or USP certified. Marine collagen can trigger fish/shellfish allergies. Korean beauty trend promotes multiple collagen products simultaneously (drink + pill + powder) — this does not multiply the benefit, just the cost and heavy metal exposure.',
    overuse_ko: '단백질 대체재가 아님 — 콜라겐은 불완전 단백질(트립토판 결여)입니다. 일부 사람들이 "단백질=단백질"이라며 하루 20~30 g을 식사 대체로 복용하는데, 이는 시간이 지나면서 아미노산 불균형을 유발할 수 있습니다. 또한 콜라겐 제품은 중금속을 흔히 함유합니다 — 2018년 Clean Label Project 검사에서 많은 유명 브랜드에 카드뮴, 납, 수은이 검출되었습니다. NSF 또는 USP 인증 제품을 선택하세요. 해양 콜라겐은 생선·조개 알레르기를 유발할 수 있습니다. 한국 뷰티 트렌드는 여러 콜라겐 제품(음료+알약+분말)을 동시에 홍보하는데, 이는 이득을 배가시키지 않고 비용과 중금속 노출만 증가시킵니다.',
    overuse_ja: 'タンパク質代替品ではない — コラーゲンは不完全タンパク質(トリプトファン欠如)です。一部の人々が「タンパク質=タンパク質」と考え、1日20~30 gを食事代替として摂取していますが、時間とともにアミノ酸不均衡を引き起こす可能性があります。また、コラーゲン製品は重金属を含むことが多く、2018年Clean Label Projectの検査で多くの有名ブランドからカドミウム、鉛、水銀が検出されました。NSFまたはUSP認証製品を選んでください。海洋コラーゲンは魚·貝アレルギーを誘発する可能性があります。美容トレンドが複数のコラーゲン製品(ドリンク+錠剤+粉末)を同時に宣伝していますが、これは利益を倍増させず、コストと重金属曝露を増やすだけです。',
    warn_en: 'Allergy risk if source is fish/shellfish (marine) or eggs (chicken). Some people report heartburn or feeling full. Not recommended during pregnancy (safety data insufficient). Kidney disease patients — excess protein can burden kidneys.',
    warn_ko: '알레르기 위험 — 원료가 생선·조개(해양)나 달걀(닭)인 경우. 속쓰림이나 포만감 보고됨. 임신 중 권장되지 않음 (안전성 데이터 부족). 신장 질환 환자 — 과도한 단백질은 신장에 부담.',
    warn_ja: 'アレルギーリスク — 原料が魚·貝(海洋)や卵(鶏)の場合。胸やけや満腹感が報告されている。妊娠中は推奨されない(安全性データ不足)。腎疾患患者 — 過剰なタンパク質は腎臓に負担をかける。',
    interact: [
      { en: 'Blood thinners — large doses may affect absorption of other supplements', ko: '혈액 희석제 — 대용량은 다른 보충제 흡수에 영향 가능', ja: '血液凝固阻止薬 — 大量では他のサプリの吸収に影響の可能性' },
      { en: 'Calcium-containing collagen (especially marine) — may interact with thyroid medication', ko: '칼슘 함유 콜라겐 (특히 해양) — 갑상선약과 상호작용 가능', ja: 'カルシウム含有コラーゲン(特に海洋) — 甲状腺薬と相互作用の可能性' }
    ],
    source: 'NIH ODS · Clean Label Project (independent testing)'
  },
  {
    id: 'beauty-combo-warning',
    generic: { en: 'Beauty / Weight-Loss / Energy Combination Supplements — Safety Warning', ko: '미용·다이어트·에너지 복합 보충제 — 안전 경고', ja: '美容·ダイエット·エナジー複合サプリ — 安全警告' },
    brands: ['"Hair, Skin, Nails" gummies', 'Slimming / Detox / Fat-burner capsules', 'Energy / Pre-workout blends'],
    category: 'supplement',
    uses: [
      { title_en: 'Marketed for hair growth, glowing skin, weight loss, energy', title_ko: '모발 성장, 피부 광채, 체중 감량, 에너지 증진 용도로 홍보', title_ja: '髪の成長、肌の輝き、体重減少、エナジー増進用途で宣伝', evidence: 'limited',
        detail_en: 'These combination products are popular but have been repeatedly found by the FDA to contain hidden, unapproved pharmaceutical ingredients. This card is a safety warning, not an endorsement.',
        detail_ko: '이 복합 제품들은 인기가 많지만, FDA가 반복적으로 비공개·미승인 의약품 성분을 검출했습니다. 이 카드는 효능 광고가 아니라 안전 경고입니다.',
        detail_ja: 'これらの複合製品は人気があるが、FDAが繰り返し非公開·未承認の医薬品成分を検出しています。このカードは効能広告ではなく安全警告です。' }
    ],
    dose_en: { 'Recommendation': 'Use only products with USP, NSF, or ConsumerLab third-party certification', 'Stop immediately if': 'headache, racing heart, chest tightness, dizziness, high blood pressure, anxiety, insomnia', 'Safer alternative': 'Get individual nutrients (biotin, collagen, vitamin D) as single-ingredient, USP-verified products instead of multi-ingredient blends' },
    dose_ko: { '권장': 'USP, NSF, 또는 ConsumerLab 제3자 인증 제품만 사용', '즉시 중단해야 할 증상': '두통, 심계항진, 가슴 답답함, 어지러움, 고혈압, 불안, 불면', '더 안전한 대안': '복합제 대신 단일 성분의 USP 인증 제품(비오틴, 콜라겐, 비타민 D 등)을 개별 복용' },
    dose_ja: { '推奨': 'USP、NSF、またはConsumerLab第三者認証製品のみ使用', '即座に中止すべき症状': '頭痛、動悸、胸の圧迫感、めまい、高血圧、不安、不眠', 'より安全な代替': '複合剤ではなく、単一成分のUSP認証製品(ビオチン、コラーゲン、ビタミンDなど)を個別に服用' },
    overuse_en: 'ACUTE HYPERTENSION AND CARDIOVASCULAR EVENTS REPORTED — The FDA Tainted Supplements Database documented 1,068 adulterated supplements between 2007 and 2021 containing undeclared pharmaceutical ingredients. The most common hidden drugs include:\n\n• SIBUTRAMINE — a weight-loss drug REMOVED from the US market in 2010 because it caused heart attacks, strokes, and acute blood pressure spikes. Still found in Chinese, Korean, and Southeast Asian "slimming beauty" imports.\n\n• SYNEPHRINE (bitter orange) — a legal but ephedrine-like stimulant that raises blood pressure and heart rate.\n\n• YOHIMBINE — causes hypertension, anxiety, palpitations.\n\n• HIGH-DOSE CAFFEINE ANHYDROUS — often undeclared, can acutely spike blood pressure.\n\n• EPHEDRINE — banned in supplements since 2004 but still appears in imported products.\n\nCLINICAL PATTERN commonly seen: A woman taking a multi-ingredient "hair/skin/nails" or "slimming beauty" product presents with new-onset headache, palpitations, and blood pressure 160-180/100+. On stopping the supplement, blood pressure normalizes within days. This pattern is almost never caused by vitamin E alone — it is caused by hidden or combined stimulants in the product. Ask your doctor to save the bottle and contact FDA MedWatch (1-800-FDA-1088).',
    overuse_ko: '급성 고혈압 및 심혈관 사건 보고 사례 — FDA 부정 보충제 데이터베이스에 2007~2021년 사이 1,068개의 불법 의약품 성분 함유 제품이 기록되었습니다. 가장 흔한 숨겨진 약물:\n\n• 시부트라민 (Sibutramine) — 2010년 심장마비·뇌졸중·급성 혈압 상승 때문에 미국 시장에서 퇴출된 체중감량약. 중국, 한국, 동남아시아의 "슬리밍 뷰티" 수입 제품에서 여전히 검출됨.\n\n• 시네프린 (Synephrine / 등자나무) — 합법이지만 에페드린 유사 자극제로 혈압과 심박수를 상승시킴.\n\n• 요힘빈 (Yohimbine) — 고혈압, 불안, 심계항진 유발.\n\n• 무수 카페인 고용량 — 라벨 미표기가 흔하며 급성 혈압 상승 유발.\n\n• 에페드린 — 2004년 보충제에서 금지되었으나 수입품에서 여전히 검출됨.\n\n흔히 관찰되는 임상 패턴: 여성이 복합 "헤어·스킨·네일" 또는 "슬리밍 뷰티" 제품을 복용하다가 새로 생긴 두통, 심계항진, 혈압 160~180/100 이상으로 내원. 보충제를 중단하면 며칠 내 혈압 정상화. 이 패턴은 비타민 E 단독으로는 거의 발생하지 않으며, 제품에 숨겨지거나 첨가된 자극제가 원인입니다. 의사에게 제품 병을 보관하도록 하고 FDA MedWatch (1-800-FDA-1088)에 신고하도록 하세요.',
    overuse_ja: '急性高血圧および心血管イベント報告症例 — FDA不正サプリデータベースに2007~2021年の間に1,068件の違法医薬品成分含有製品が記録されています。最も一般的な隠された薬物:\n\n• シブトラミン(Sibutramine) — 2010年に心筋梗塞·脳卒中·急性血圧上昇のため米国市場から撤退した体重減少薬。中国、韓国、東南アジアの「スリミングビューティ」輸入品で依然として検出されています。\n\n• シネフリン(Synephrine / ダイダイ) — 合法だがエフェドリン類似刺激薬で、血圧と心拍数を上昇させる。\n\n• ヨヒンビン(Yohimbine) — 高血圧、不安、動悸を誘発。\n\n• 無水カフェイン高用量 — 表示されないことが多く、急性血圧上昇を引き起こす。\n\n• エフェドリン — 2004年にサプリで禁止されたが、輸入品で依然として検出。\n\nよく観察される臨床パターン:女性が複合「ヘア·スキン·ネイル」または「スリミングビューティ」製品を服用中に、新規発症の頭痛、動悸、血圧160~180/100以上で来院。サプリ中止により数日以内に血圧正常化。このパターンはビタミンE単独ではほぼ発生せず、製品に隠された刺激薬が原因です。医師に製品ボトルを保管するよう依頼し、FDA MedWatch(1-800-FDA-1088)に報告してください。',
    danger_en: 'RED FLAGS indicating a likely adulterated or dangerous product:\n• "Rapid" results promised (weight loss, hair growth) in days/weeks\n• Sold primarily online, through MLM, or at community events\n• Labeled "100% herbal" or "all natural" but produces strong stimulant effects\n• Imported from countries with weak supplement regulation\n• No third-party testing certification (no USP/NSF/ConsumerLab mark)\n• Contains proprietary "blends" without disclosed ingredient amounts\n• Generic names like "Slimming Beauty", "Mega Energy", "Detox Complex"',
    danger_ko: '오염되거나 위험한 제품일 가능성을 나타내는 위험 신호:\n• 며칠·몇 주 안에 "빠른" 결과 약속 (체중 감량, 모발 성장)\n• 주로 온라인, 다단계 판매, 지역 행사에서 판매\n• "100% 허브" 또는 "천연"이라고 표시되었으나 강한 자극 효과 발생\n• 보충제 규제가 약한 국가에서 수입\n• 제3자 검사 인증 없음 (USP·NSF·ConsumerLab 마크 없음)\n• "독점 혼합(proprietary blend)"으로 성분 함량 비공개\n• "슬리밍 뷰티", "메가 에너지", "디톡스 복합" 같은 포괄적 이름',
    danger_ja: '汚染されたまたは危険な製品の可能性を示す危険信号:\n• 数日·数週間で「迅速な」結果を約束(体重減少、髪の成長)\n• 主にオンライン、ネットワークビジネス、地域イベントで販売\n•「100%ハーブ」または「天然」と表示されているが強い刺激作用が発生\n• サプリ規制が弱い国からの輸入\n• 第三者検査認証なし(USP·NSF·ConsumerLabマークなし)\n•「プロプライエタリブレンド」で成分含量非公開\n•「スリミングビューティ」「メガエナジー」「デトックスコンプレックス」のような包括的な名称',
    warn_en: 'Women aged 30–60 are the most common consumers of beauty supplements and therefore overrepresented in adverse event reports. If you are pregnant, nursing, have hypertension, heart disease, anxiety disorder, or take blood pressure medication, avoid all multi-ingredient "beauty" blends entirely. Individual nutrients (biotin alone, vitamin D alone, collagen alone) from reputable brands are far safer than combination products.',
    warn_ko: '30~60대 여성이 미용 보충제의 주 소비자이며, 따라서 부작용 보고에도 가장 많이 등장합니다. 임신, 수유, 고혈압, 심장병, 불안장애가 있거나 혈압약을 복용 중이면 모든 복합 "미용" 제품을 완전히 피하세요. 개별 성분(비오틴 단독, 비타민 D 단독, 콜라겐 단독)을 신뢰할 수 있는 브랜드에서 구입하는 것이 복합 제품보다 훨씬 안전합니다.',
    warn_ja: '30~60代女性が美容サプリの主な消費者であり、副作用報告にも最も多く登場します。妊娠、授乳、高血圧、心疾患、不安障害がある場合や血圧薬を服用中の場合は、すべての複合「美容」製品を完全に避けてください。個別成分(ビオチン単独、ビタミンD単独、コラーゲン単独)を信頼できるブランドから購入することが複合製品より遥かに安全です。',
    interact: [
      { en: 'Blood pressure medications — hidden stimulants can neutralize or dangerously oppose the medication', ko: '혈압약 — 숨겨진 자극제가 약효를 중화하거나 위험하게 상쇄', ja: '血圧薬 — 隠された刺激薬が薬効を中和または危険に拮抗' },
      { en: 'MAO inhibitors, SSRIs — dangerous interaction with hidden stimulants or SSRI adulterants', ko: 'MAO 억제제, SSRI — 숨겨진 자극제나 SSRI 첨가물과 위험한 상호작용', ja: 'MAO阻害薬、SSRI — 隠された刺激薬やSSRI混入物と危険な相互作用' },
      { en: 'Thyroid medication — biotin in these products interferes with thyroid blood tests', ko: '갑상선약 — 이 제품에 든 비오틴이 갑상선 혈액 검사 결과 왜곡', ja: '甲状腺薬 — これらの製品中のビオチンが甲状腺血液検査結果を歪曲' },
      { en: 'Other supplements — stacking multiple "beauty" or "energy" products multiplies the hidden-stimulant dose', ko: '다른 보충제 — 여러 "미용"·"에너지" 제품을 중첩하면 숨겨진 자극제 용량이 배가됨', ja: '他のサプリ — 複数の「美容」·「エナジー」製品を重ねると隠された刺激薬用量が倍増' }
    ],
    source: 'FDA Tainted Dietary Supplement Database (2007–2021) · Tucker et al. JAMA Netw Open 2018 · White et al. J Clin Pharmacol 2022 · FDA MedWatch'
  },
  {
    id: 'meclizine',
    generic: { en: 'Meclizine', ko: '메클리진', ja: 'メクリジン' },
    brands: ['Bonine', 'Dramamine Less Drowsy'],
    category: 'gi',
    uses: [
      { title_en: 'Motion sickness prevention and treatment', title_ko: '멀미 예방 및 치료', title_ja: '乗り物酔いの予防·治療',
        detail_en: 'Prevents and treats nausea, vomiting, and dizziness from motion (car, boat, plane)',
        detail_ko: '움직임으로 인한 메스꺼움, 구토, 어지러움을 예방하고 치료 (자동차, 배, 비행기)',
        detail_ja: '動きによる吐き気、嘔吐、めまいを予防·治療(車、船、飛行機)' }
    ],
    dose_en: { 'Adult and child 12+': '25–50 mg taken 1 hour before travel', 'Repeat': 'May repeat every 24 hours as needed', 'Duration of travel': 'One dose lasts up to 24 hours' },
    dose_ko: { '성인 및 12세 이상': '여행 1시간 전 25~50 mg', '반복': '필요 시 24시간마다 반복', '지속 시간': '1회 복용으로 최대 24시간 지속' },
    dose_ja: { '成人および12歳以上': '旅行1時間前に25~50 mg', '反復': '必要に応じて24時間ごとに反復', '持続時間': '1回服用で最大24時間持続' },
    warn_en: 'Causes drowsiness — do not drive or operate machinery until you know how it affects you. Avoid alcohol. Use caution if you have glaucoma, enlarged prostate, or breathing problems. Not for children under 12.',
    warn_ko: '졸음을 유발합니다 — 반응을 확인할 때까지 운전이나 기계 조작을 하지 마세요. 알코올을 피하세요. 녹내장, 전립선 비대, 호흡 문제가 있으면 주의해서 사용하세요. 12세 미만에게는 사용 금지.',
    warn_ja: '眠気を引き起こします — 影響を確認するまで運転·機械操作を避けてください。アルコールを避ける。緑内障、前立腺肥大、呼吸器疾患がある場合は注意。12歳未満には使用禁止。',
    interact: [
      { en: 'Alcohol — increased drowsiness', ko: '알코올 — 졸음 증가', ja: 'アルコール — 眠気増加' },
      { en: 'Sleep aids, sedatives — additive sedation', ko: '수면제, 진정제 — 진정 효과 누적', ja: '睡眠補助薬、鎮静薬 — 鎮静作用累積' },
      { en: 'Other anticholinergics — dry mouth, urinary retention', ko: '다른 항콜린제 — 구강 건조, 소변 저류', ja: '他の抗コリン薬 — 口渇、尿閉' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'polyethylene-glycol',
    generic: { en: 'Polyethylene glycol 3350 (PEG)', ko: '폴리에틸렌 글리콜 3350 (PEG)', ja: 'ポリエチレングリコール3350(PEG)' },
    brands: ['MiraLAX', 'GaviLAX'],
    category: 'gi',
    uses: [
      { title_en: 'Occasional constipation relief', title_ko: '일시적 변비 완화', title_ja: '一時的な便秘の緩和',
        detail_en: 'Relieves occasional constipation; works by drawing water into the stool to soften it',
        detail_ko: '일시적 변비 완화; 대변에 수분을 끌어들여 부드럽게 만드는 방식으로 작용',
        detail_ja: '一時的な便秘を緩和;便に水分を引き込み軟らかくする作用' }
    ],
    dose_en: { 'Adult and child 17+': '17 g (1 capful) dissolved in 4–8 oz of liquid, once daily', 'Onset': 'Usually produces a bowel movement within 1–3 days', 'Max duration (OTC)': '7 days without doctor approval' },
    dose_ko: { '성인 및 17세 이상': '17 g (뚜껑 1개) 분량을 120~240 mL 음료에 녹여 하루 1회', '작용 시간': '일반적으로 1~3일 내에 배변 유발', '최대 기간 (OTC)': '의사 승인 없이 7일' },
    dose_ja: { '成人および17歳以上': '17 g(キャップ1杯)を120~240 mLの飲料に溶かし1日1回', '作用時間': '通常1~3日以内に排便を促す', '最大期間(OTC)': '医師の承認なく7日' },
    warn_en: 'Do not use if you have a bowel obstruction. Stop use and see a doctor if you get rectal bleeding, have no bowel movement after use, or if symptoms last longer than 7 days. May cause bloating, cramping, or diarrhea — reduce dose if this happens.',
    warn_ko: '장폐색이 있으면 사용하지 마세요. 직장 출혈이 있거나, 사용 후 배변이 없거나, 증상이 7일 이상 지속되면 사용을 중단하고 의사를 만나세요. 복부 팽만, 경련, 설사를 유발할 수 있으며 — 이 경우 용량을 줄이세요.',
    warn_ja: '腸閉塞がある場合は使用禁止。直腸出血、使用後排便なし、または症状が7日以上続く場合は使用を中止し医師を受診。腹部膨満、けいれん、下痢を起こす可能性 — 該当時は減量。',
    interact: [
      { en: 'Generally few drug interactions — not absorbed systemically', ko: '약물 상호작용이 일반적으로 적음 — 전신 흡수되지 않음', ja: '薬物相互作用は一般的に少ない — 全身吸収されない' },
      { en: 'May affect absorption of other medications if taken at the same time — separate by 2 hours', ko: '동시 복용 시 다른 약물의 흡수에 영향 가능 — 2시간 간격을 두세요', ja: '同時服用で他の薬の吸収に影響の可能性 — 2時間間隔をあける' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'fluticasone',
    generic: { en: 'Fluticasone propionate (nasal spray)', ko: '플루티카손 프로피오네이트 (비강 스프레이)', ja: 'フルチカゾンプロピオン酸エステル(鼻スプレー)' },
    brands: ['Flonase', 'Flonase Sensimist'],
    category: 'allergy',
    uses: [
      { title_en: 'Nasal allergy symptom control', title_ko: '비강 알레르기 증상 조절', title_ja: '鼻アレルギー症状のコントロール',
        detail_en: 'Relieves nasal congestion, runny nose, sneezing, itchy nose from hay fever and other upper respiratory allergies',
        detail_ko: '꽃가루 알레르기 및 기타 상기도 알레르기로 인한 코막힘, 콧물, 재채기, 코 가려움 완화',
        detail_ja: '花粉症およびその他の上気道アレルギーによる鼻づまり、鼻水、くしゃみ、鼻のかゆみを緩和' },
      { title_en: 'Itchy, watery eyes from allergies', title_ko: '알레르기로 인한 눈 가려움·눈물', title_ja: 'アレルギーによる目のかゆみ·涙目',
        detail_en: 'Also reduces eye symptoms associated with allergies',
        detail_ko: '알레르기 관련 눈 증상도 감소',
        detail_ja: 'アレルギー関連の目の症状も軽減' }
    ],
    dose_en: { 'Adult and child 12+': '2 sprays in each nostril once daily; after a week, reduce to 1 spray each nostril if symptoms controlled', 'Child 4–11': '1 spray in each nostril once daily', 'Onset': 'Full effect takes several days — not for immediate relief', 'Technique': 'Aim spray away from the septum (toward outer wall of nostril) to prevent nosebleeds' },
    dose_ko: { '성인 및 12세 이상': '콧구멍당 하루 2회 분무, 1주 후 증상이 조절되면 콧구멍당 1회로 감량', '4~11세': '콧구멍당 하루 1회 분무', '작용 시간': '완전한 효과는 수일 소요 — 즉각 완화용 아님', '사용법': '코피 예방을 위해 비중격 반대쪽(콧구멍 바깥쪽 벽)을 향해 분무' },
    dose_ja: { '成人および12歳以上': '各鼻孔に1日2回噴霧、1週間後に症状がコントロールされたら各鼻孔に1回に減量', '4~11歳': '各鼻孔に1日1回噴霧', '作用時間': '完全な効果まで数日 — 即時緩和用ではない', '使用法': '鼻血予防のため鼻中隔の反対側(鼻孔の外側壁)に向けて噴霧' },
    warn_en: 'Can cause nosebleeds, nasal irritation, or burning sensation. Rare but serious — glaucoma, cataracts, or adrenal problems with long-term high-dose use. If no improvement after 1 week, see a doctor. Do not use if you have a nasal infection or recent nasal injury/surgery.',
    warn_ko: '코피, 비강 자극, 작열감을 유발할 수 있습니다. 드물지만 심각한 부작용 — 장기 고용량 사용 시 녹내장, 백내장, 부신 문제. 1주 후에도 호전이 없으면 의사를 만나세요. 비강 감염이나 최근 비강 부상·수술이 있으면 사용하지 마세요.',
    warn_ja: '鼻血、鼻の刺激、灼熱感を起こすことがあります。稀ですが重篤 — 長期高用量使用で緑内障、白内障、副腎の問題。1週間後に改善がない場合は医師を受診してください。鼻の感染や最近の鼻の外傷·手術がある場合は使用しないでください。',
    interact: [
      { en: 'Ritonavir, ketoconazole — can increase fluticasone levels significantly (adrenal suppression risk)', ko: '리토나비르, 케토코나졸 — 플루티카손 농도를 크게 증가시킬 수 있음 (부신 억제 위험)', ja: 'リトナビル、ケトコナゾール — フルチカゾン濃度を大幅に上昇させる可能性(副腎抑制リスク)' },
      { en: 'Other nasal steroids — do not combine', ko: '다른 비강 스테로이드 — 병용 금지', ja: '他の鼻ステロイド — 併用禁止' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'oxymetazoline',
    generic: { en: 'Oxymetazoline (nasal spray)', ko: '옥시메타졸린 (비강 스프레이)', ja: 'オキシメタゾリン(鼻スプレー)' },
    brands: ['Afrin', 'Vicks Sinex'],
    category: 'allergy',
    uses: [
      { title_en: 'Fast relief of nasal congestion', title_ko: '빠른 코막힘 완화', title_ja: '即効性の鼻づまり緩和',
        detail_en: 'Shrinks swollen nasal blood vessels within minutes; provides relief up to 12 hours per dose',
        detail_ko: '부은 비강 혈관을 몇 분 내에 수축시킴; 1회 분무로 최대 12시간 효과',
        detail_ja: '腫れた鼻血管を数分以内に収縮;1回の噴霧で最大12時間効果' }
    ],
    dose_en: { 'Adult and child 6+': '2–3 sprays in each nostril every 10–12 hours', 'Maximum duration': 'DO NOT USE MORE THAN 3 DAYS', 'Max per day': '2 doses in 24 hours' },
    dose_ko: { '성인 및 6세 이상': '콧구멍당 10~12시간마다 2~3회 분무', '최대 사용 기간': '3일 이상 절대 사용 금지', '하루 최대': '24시간 내 2회' },
    dose_ja: { '成人および6歳以上': '各鼻孔に10~12時間ごとに2~3回噴霧', '最大使用期間': '3日以上絶対に使用禁止', '1日最大量': '24時間以内に2回' },
    danger_en: 'REBOUND CONGESTION (rhinitis medicamentosa) — Using more than 3 days causes worsening congestion when the spray wears off, leading to dependence. Some people end up using it for months or years and cannot breathe through their nose without it. Stopping causes severe rebound. If this happens, see a doctor — a short course of nasal steroids can help break the cycle.',
    danger_ko: '반동성 코막힘 (약물성 비염) — 3일 이상 사용하면 약효가 사라질 때 코막힘이 더 심해져 의존성이 생깁니다. 일부 환자는 몇 달~몇 년씩 사용하며 스프레이 없이는 코로 숨을 못 쉬게 됩니다. 중단 시 심한 반동 증상이 나타납니다. 이런 경우 의사를 만나세요 — 단기 비강 스테로이드로 끊을 수 있습니다.',
    danger_ja: 'リバウンド鼻づまり(薬剤性鼻炎) — 3日以上使用すると薬効が切れる際に鼻づまりが悪化し依存が生じます。一部の患者は数か月~数年使用し続け、スプレーなしでは鼻で呼吸できなくなります。中止すると重度のリバウンドが現れます。このような場合は医師を受診してください — 短期の鼻ステロイドで悪循環を断ち切ることができます。',
    warn_en: 'Can raise blood pressure and heart rate if absorbed. Avoid if you have high blood pressure, heart disease, hyperthyroidism, glaucoma, or enlarged prostate. Not for children under 6.',
    warn_ko: '흡수되면 혈압과 심박수를 상승시킬 수 있습니다. 고혈압, 심장병, 갑상선 기능 항진증, 녹내장, 전립선 비대가 있으면 사용하지 마세요. 6세 미만에게는 사용 금지.',
    warn_ja: '吸収されると血圧と心拍数が上昇する可能性があります。高血圧、心疾患、甲状腺機能亢進症、緑内障、前立腺肥大がある場合は使用しないでください。6歳未満には使用禁止。',
    interact: [
      { en: 'MAO inhibitors — dangerous blood pressure spike', ko: 'MAO 억제제 — 위험한 혈압 급상승', ja: 'MAO阻害薬 — 危険な血圧急上昇' },
      { en: 'Blood pressure medications — reduced effectiveness', ko: '혈압약 — 효과 감소', ja: '降圧薬 — 効果減少' }
    ],
    source: 'FDA OTC Monograph 21 CFR 341 · DailyMed (NIH)'
  },
  {
    id: 'bisacodyl',
    generic: { en: 'Bisacodyl (stimulant laxative)', ko: '비사코딜 (자극성 하제)', ja: 'ビサコジル(刺激性下剤)' },
    brands: ['Dulcolax', 'Correctol'],
    category: 'gi',
    uses: [
      { title_en: 'Short-term constipation relief', title_ko: '단기 변비 완화', title_ja: '短期間の便秘緩和',
        detail_en: 'Stimulates intestinal contractions to produce a bowel movement — works in 6–12 hours (oral) or 15–60 minutes (suppository)',
        detail_ko: '장 수축을 자극하여 배변을 유발 — 경구 6~12시간, 좌약 15~60분 내 작용',
        detail_ja: '腸の収縮を刺激し排便を促す — 経口6~12時間、坐薬15~60分以内に作用' }
    ],
    dose_en: { 'Adult tablet': '5–15 mg once daily, usually at bedtime', 'Suppository': '10 mg once daily as needed', 'Take tablet with': 'Water only — swallow whole, do not crush or chew', 'Avoid with': 'Milk or antacids within 1 hour (can break enteric coating)' },
    dose_ko: { '성인 정제': '하루 1회 5~15 mg, 보통 취침 시', '좌약': '필요 시 하루 1회 10 mg', '정제 복용법': '물로만 — 통째로 삼키고 부수거나 씹지 말 것', '병용 주의': '우유·제산제와 1시간 이내 병용 금지 (장용성 코팅 손상)' },
    dose_ja: { '成人錠剤': '1日1回5~15 mg、通常就寝時', '坐薬': '必要に応じて1日1回10 mg', '錠剤の服用法': '水のみで — 丸ごと飲み込み、砕いたり噛んだりしない', '併用注意': '牛乳·制酸薬と1時間以内の併用禁止(腸溶コーティング損傷)' },
    danger_en: 'LAXATIVE DEPENDENCE — Long-term use (>1 week) can cause the colon to become dependent on stimulation, making natural bowel movements impossible without laxatives. This is a common trap for elderly users. Use for the shortest time possible. If constipation is chronic, start with fiber (psyllium), fluids, and exercise before stimulant laxatives.',
    danger_ko: '하제 의존성 — 1주 이상 장기 사용 시 대장이 자극에 의존하게 되어 하제 없이는 자연 배변이 어려워집니다. 이는 고령자에게 흔한 함정입니다. 가능한 짧게 사용하세요. 만성 변비라면 자극성 하제 전에 식이섬유(차전자피), 수분, 운동부터 시작하세요.',
    danger_ja: '下剤依存 — 1週間以上の長期使用で大腸が刺激に依存し、下剤なしでは自然排便が困難になります。高齢者によくある落とし穴です。可能な限り短期間で使用。慢性便秘では刺激性下剤の前に食物繊維(サイリウム)、水分、運動から始めてください。',
    warn_en: 'Can cause severe cramping, diarrhea, dehydration, and low potassium. Do not use if you have appendicitis symptoms, intestinal obstruction, or unexplained abdominal pain. Stop and see a doctor if you need laxatives longer than 1 week.',
    warn_ko: '심한 복통, 설사, 탈수, 저칼륨혈증을 유발할 수 있습니다. 충수염 의심 증상, 장폐색, 원인 불명 복통이 있으면 사용하지 마세요. 1주 이상 하제가 필요하면 중단하고 의사를 만나세요.',
    warn_ja: '激しい腹痛、下痢、脱水、低カリウム血症を起こす可能性。虫垂炎疑い、腸閉塞、原因不明の腹痛がある場合は使用禁止。1週間以上下剤が必要な場合は中止し医師を受診。',
    interact: [
      { en: 'Milk, antacids, PPIs — can break enteric coating (take 1 hour apart)', ko: '우유, 제산제, PPI — 장용성 코팅 손상 가능 (1시간 간격)', ja: '牛乳、制酸薬、PPI — 腸溶コーティング損傷の可能性(1時間間隔)' },
      { en: 'Diuretics — compounded risk of low potassium', ko: '이뇨제 — 저칼륨혈증 위험 누적', ja: '利尿薬 — 低カリウム血症リスクの累積' },
      { en: 'Digoxin — low potassium from laxative can cause toxicity', ko: '디곡신 — 하제로 인한 저칼륨혈증이 독성 유발 가능', ja: 'ジゴキシン — 下剤による低カリウムが毒性を引き起こす可能性' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'ors',
    generic: { en: 'Oral rehydration solution (ORS)', ko: '경구 수액 보충제', ja: '経口補水液(ORS)' },
    brands: ['Pedialyte', 'DripDrop', 'Liquid I.V.'],
    category: 'gi',
    uses: [
      { title_en: 'Dehydration from diarrhea or vomiting', title_ko: '설사·구토로 인한 탈수', title_ja: '下痢·嘔吐による脱水',
        detail_en: 'Replaces water, sodium, potassium, and glucose lost through diarrhea, vomiting, fever, or heavy sweating. Better than water alone for significant fluid loss.',
        detail_ko: '설사, 구토, 발열, 과다 발한으로 손실된 수분, 나트륨, 칼륨, 포도당을 보충. 유의미한 수분 손실에는 물만보다 효과적.',
        detail_ja: '下痢、嘔吐、発熱、大量発汗で失われた水分、ナトリウム、カリウム、グルコースを補給。重大な水分喪失には水単独より有効。' },
      { title_en: 'Illness and heat exhaustion recovery', title_ko: '질병 및 열탈진 회복', title_ja: '病気·熱中症からの回復',
        detail_en: 'Also helpful during flu, food poisoning, or after intense exercise in heat',
        detail_ko: '독감, 식중독, 더위 속 격한 운동 후에도 유용',
        detail_ja: 'インフルエンザ、食中毒、暑さの中での激しい運動後にも有用' }
    ],
    dose_en: { 'Adult': 'Sip slowly — 8 oz (240 mL) after each loose stool or episode of vomiting', 'Child': 'Follow product label — 1–2 tsp every 5 minutes if vomiting', 'Infant under 1 year': 'See doctor — do not use adult ORS without guidance', 'Better than': 'Sports drinks (too much sugar) or soda (can worsen diarrhea)' },
    dose_ko: { '성인': '천천히 마시기 — 무른 변이나 구토 후 매번 240 mL', '어린이': '제품 라벨에 따름 — 구토 시 5분마다 1~2 티스푼', '1세 미만 영아': '의사 진료 필요 — 지시 없이 성인용 ORS 사용 금지', '대체 주의': '스포츠 음료(당분 과다)나 탄산음료(설사 악화)보다 효과적' },
    dose_ja: { '成人': 'ゆっくり飲む — 軟便·嘔吐の後ごとに240 mL', '小児': '製品ラベルに従う — 嘔吐時は5分ごとに小さじ1~2杯', '1歳未満乳児': '医師の診察必要 — 指示なく成人用ORS使用禁止', '代替注意': 'スポーツ飲料(糖分過多)や炭酸飲料(下痢悪化)より有効' },
    warn_en: 'If dehydration is severe (very dry mouth, no urination for 8+ hours, dizziness, rapid heartbeat, confusion), go to ER — oral rehydration may not be enough. Do not use homemade salt/sugar mixtures unless you know exact ratios (wrong ratios are dangerous). Check expiration — opened bottles last 48 hours refrigerated.',
    warn_ko: '심한 탈수(심한 구강 건조, 8시간 이상 소변 없음, 어지러움, 빠른 심박, 혼돈) 시 응급실로 가세요 — 경구 수액으로는 부족할 수 있습니다. 정확한 비율을 모른다면 집에서 만든 소금/설탕 혼합물은 사용하지 마세요 (잘못된 비율은 위험). 유효기간 확인 — 개봉한 병은 냉장 보관 시 48시간 이내 사용.',
    warn_ja: '重度の脱水(強い口渇、8時間以上排尿なし、めまい、頻脈、混乱)時は救急受診 — 経口補水では不十分な可能性。正確な比率を知らない場合は自家製塩·砂糖混合物を使用しない(誤った比率は危険)。有効期限確認 — 開封後の瓶は冷蔵で48時間以内に使用。',
    interact: [
      { en: 'High-potassium forms — caution if taking potassium-sparing diuretics or ACE inhibitors', ko: '고칼륨 제형 — 칼륨 보존 이뇨제나 ACE 억제제 복용 시 주의', ja: '高カリウム製剤 — カリウム保持性利尿薬やACE阻害薬服用時は注意' },
      { en: 'Kidney disease — check sodium and potassium content with doctor', ko: '신장 질환 — 의사와 나트륨·칼륨 함량 확인', ja: '腎疾患 — 医師とナトリウム·カリウム含有量を確認' }
    ],
    source: 'CDC · WHO Oral Rehydration Guidelines · MedlinePlus (NIH)'
  },
  {
    id: 'aquaphor',
    generic: { en: 'Petrolatum-based ointment (Aquaphor/petroleum jelly)', ko: '바세린 계열 연고', ja: 'ワセリン系軟膏(Aquaphor/ワセリン)' },
    brands: ['Aquaphor', 'Vaseline', 'CeraVe Healing Ointment'],
    category: 'skin',
    uses: [
      { title_en: 'Skin protection and moisture barrier', title_ko: '피부 보호 및 수분 장벽', title_ja: '皮膚保護·水分バリア',
        detail_en: 'Creates a protective barrier that locks in moisture and protects chapped, dry, or cracked skin',
        detail_ko: '수분을 가두고 갈라지거나 건조하거나 금이 간 피부를 보호하는 장벽 형성',
        detail_ja: '水分を閉じ込めひび割れ·乾燥·亀裂のある皮膚を保護する保護バリアを形成' },
      { title_en: 'Minor wound and burn aftercare', title_ko: '경미한 상처·화상 후 관리', title_ja: '軽度の傷·やけどのアフターケア',
        detail_en: 'Helps prevent scarring and supports moist wound healing; preferred over antibiotic ointments for uninfected wounds',
        detail_ko: '흉터 예방 및 습윤 상처 치유 지원; 감염되지 않은 상처에는 항생제 연고보다 권장됨',
        detail_ja: '瘢痕予防と湿潤創傷治癒を支援;非感染創には抗生物質軟膏より推奨' },
      { title_en: 'Diaper rash prevention', title_ko: '기저귀 발진 예방', title_ja: 'おむつかぶれ予防',
        detail_en: 'Acts as a moisture barrier for infant skin',
        detail_ko: '영유아 피부에 수분 장벽 역할',
        detail_ja: '乳児の皮膚に水分バリアとして作用' },
      { title_en: 'Chapped lips, cracked hands, cracked heels', title_ko: '튼 입술, 갈라진 손, 갈라진 발뒤꿈치', title_ja: '荒れた唇、ひび割れた手·かかと',
        detail_en: 'Deep moisturization for severely dry areas',
        detail_ko: '심하게 건조한 부위에 깊은 보습',
        detail_ja: '極度に乾燥した部位への深い保湿' }
    ],
    dose_en: { 'Application': 'Apply thin layer to affected area as needed', 'Frequency': 'Multiple times daily — very safe', 'Best time': 'Apply to damp skin after washing to trap moisture' },
    dose_ko: { '도포법': '필요 시 환부에 얇게 도포', '빈도': '하루 여러 번 — 매우 안전', '최적 시간': '씻은 후 촉촉한 피부에 발라 수분 가두기' },
    dose_ja: { '塗布法': '必要に応じて患部に薄く塗布', '頻度': '1日複数回 — 非常に安全', '最適なタイミング': '洗浄後の湿った皮膚に塗布し水分を閉じ込める' },
    warn_en: 'Very well tolerated. Avoid on deep puncture wounds or heavily infected wounds (can trap bacteria). A few people are allergic to lanolin (in some Aquaphor products) — pure Vaseline is lanolin-free. Do not use on burns with broken skin without doctor advice.',
    warn_ko: '내약성이 매우 좋음. 깊은 자상이나 심하게 감염된 상처에는 사용하지 마세요 (세균을 가둘 수 있음). 일부는 라놀린(Aquaphor 일부 제품에 포함)에 알레르기 — 순수 바세린은 라놀린이 없습니다. 피부가 벗겨진 화상에는 의사 조언 없이 사용 금지.',
    warn_ja: '忍容性は非常に良好。深い刺し傷や重度感染創には使用禁止(細菌を閉じ込める可能性)。一部の人はラノリン(Aquaphorの一部製品に含有)にアレルギー — 純粋なワセリンはラノリン不含。皮膚が剥がれたやけどには医師の助言なく使用禁止。',
    interact: [
      { en: 'Latex condoms — petroleum products degrade latex; use with caution near intimate areas', ko: '라텍스 콘돔 — 석유 제품은 라텍스 손상; 친밀 부위 근처에서는 주의', ja: 'ラテックスコンドーム — 石油系製品はラテックスを劣化させる;陰部周辺での使用は注意' },
      { en: 'No significant systemic drug interactions', ko: '유의미한 전신 약물 상호작용 없음', ja: '有意な全身薬物相互作用なし' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH) · AAD Recommendations'
  },
  {
    id: 'artificial-tears',
    generic: { en: 'Artificial tears (lubricant eye drops)', ko: '인공눈물 (눈 윤활제)', ja: '人工涙液(目の潤滑剤)' },
    brands: ['Systane', 'Refresh Tears', 'Blink Tears'],
    category: 'eye_ear',
    uses: [
      { title_en: 'Dry eye symptom relief', title_ko: '안구건조증 완화', title_ja: 'ドライアイ症状緩和',
        detail_en: 'Lubricates eyes to relieve dryness, burning, irritation from screen use, contact lenses, wind, or dry air',
        detail_ko: '화면 사용, 콘택트렌즈, 바람, 건조한 공기로 인한 건조함, 작열감, 자극을 완화하기 위해 눈에 윤활',
        detail_ja: '画面使用、コンタクトレンズ、風、乾燥空気による乾燥、灼熱感、刺激を緩和するため目に潤滑' },
      { title_en: 'Eye strain from prolonged screen use', title_ko: '장시간 화면 사용으로 인한 눈 피로', title_ja: '長時間画面使用による眼精疲労',
        detail_en: 'Helps with computer vision syndrome symptoms',
        detail_ko: '컴퓨터 시증후군 증상 완화',
        detail_ja: 'コンピュータ視覚症候群の症状を緩和' }
    ],
    dose_en: { 'Adult': '1–2 drops in affected eye(s) as needed', 'Preservative-free vials': 'Preferred if using more than 4 times daily or if eyes are sensitive', 'Contact lenses': 'Use rewetting drops specifically labeled for contacts' },
    dose_ko: { '성인': '필요 시 해당 눈에 1~2방울', '무방부제 제형': '하루 4회 초과 사용 시 또는 눈이 민감한 경우 권장', '콘택트렌즈': '콘택트렌즈용으로 명시된 재습윤 점안액 사용' },
    dose_ja: { '成人': '必要時に該当する目に1~2滴', '防腐剤フリー製剤': '1日4回超使用または目が敏感な場合に推奨', 'コンタクトレンズ': 'コンタクトレンズ用と明記された再湿潤点眼液を使用' },
    warn_en: 'If preservative-containing drops are used too often, preservatives can actually worsen dry eye — switch to preservative-free. If burning or redness worsens, discontinue. Persistent dry eye over 2 weeks: see eye doctor (can be sign of autoimmune disease like Sjögren\'s). Do not share bottles — risk of eye infection.',
    warn_ko: '방부제 함유 점안액을 너무 자주 사용하면 방부제가 오히려 건조증을 악화시킬 수 있으니 무방부제로 교체하세요. 작열감이나 충혈이 악화되면 중단하세요. 안구건조가 2주 이상 지속되면 안과 의사를 만나세요 (쇼그렌 증후군 같은 자가면역질환 징후일 수 있음). 병을 공유하지 마세요 — 안구 감염 위험.',
    warn_ja: '防腐剤含有点眼液を頻用すると防腐剤がドライアイを悪化させる可能性 — 防腐剤フリーに切り替え。灼熱感や充血が悪化したら中止。2週間以上続くドライアイは眼科受診(シェーグレン症候群など自己免疫疾患の徴候の可能性)。ボトルを共有しない — 眼感染リスク。',
    interact: [
      { en: 'Prescription eye drops — space by 5+ minutes (apply prescription first, then lubricant)', ko: '처방 점안액 — 5분 이상 간격 (처방약 먼저, 윤활제 나중)', ja: '処方点眼液 — 5分以上間隔(処方薬を先に、潤滑剤を後)' },
      { en: 'Eye ointments — use drops first, ointments last (bedtime)', ko: '안연고 — 점안액 먼저, 연고는 마지막(취침 시)', ja: '眼軟膏 — 点眼液を先に、軟膏は最後(就寝時)' }
    ],
    source: 'FDA OTC Monograph · MedlinePlus (NIH)'
  },
  {
    id: 'carbamide-peroxide',
    generic: { en: 'Carbamide peroxide (ear wax removal)', ko: '카바마이드 퍼옥사이드 (귀지 제거)', ja: '過酸化尿素(耳垢除去)' },
    brands: ['Debrox', 'Murine Ear Drops'],
    category: 'eye_ear',
    uses: [
      { title_en: 'Ear wax softening and removal', title_ko: '귀지 연화 및 제거', title_ja: '耳垢の軟化·除去',
        detail_en: 'Softens and loosens excessive or hardened ear wax so it can flush out naturally',
        detail_ko: '과도하거나 굳은 귀지를 부드럽게 하여 자연스럽게 배출되도록 함',
        detail_ja: '過剰または硬化した耳垢を軟らかくし自然に排出されるようにする' }
    ],
    dose_en: { 'Adult and child 12+': '5–10 drops in affected ear twice daily for up to 4 days', 'After drops': 'Tilt head, keep drops in for several minutes, then flush with warm water using bulb syringe', 'Child under 12': 'Only with doctor supervision' },
    dose_ko: { '성인 및 12세 이상': '해당 귀에 하루 2회 5~10방울, 최대 4일', '점적 후': '머리를 기울여 몇 분간 유지 후 벌브 주사기로 따뜻한 물로 세척', '12세 미만': '의사 감독 하에만 사용' },
    dose_ja: { '成人および12歳以上': '該当する耳に1日2回5~10滴、最大4日', '点滴後': '頭を傾け数分保持後、球状注射器で温水で洗浄', '12歳未満': '医師監督下でのみ使用' },
    warn_en: 'DO NOT USE if you have ear pain, discharge, itching, ear drum perforation, or recent ear surgery. DO NOT USE cotton swabs (Q-tips) to remove wax — they push wax deeper and can perforate the ear drum. Ear candles are NOT effective and are dangerous (FDA warning). If wax does not clear after 4 days, see a doctor.',
    warn_ko: '귀 통증, 분비물, 가려움, 고막 천공, 최근 귀 수술이 있으면 사용하지 마세요. 귀지 제거에 면봉(Q-tip)을 사용하지 마세요 — 귀지를 더 깊이 밀어넣고 고막에 구멍을 낼 수 있습니다. 귀 캔들은 효과가 없고 위험합니다 (FDA 경고). 4일 후에도 귀지가 제거되지 않으면 의사를 만나세요.',
    warn_ja: '耳痛、分泌物、かゆみ、鼓膜穿孔、最近の耳の手術がある場合は使用禁止。耳垢除去に綿棒(Qチップ)使用禁止 — 耳垢をより深く押し込み鼓膜に穴を開ける可能性。耳キャンドルは無効で危険(FDA警告)。4日後も耳垢が除去されない場合は受診。',
    interact: [
      { en: 'Other ear drops — do not combine', ko: '다른 귀 점적액 — 병용 금지', ja: '他の耳点滴液 — 併用禁止' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'nicotine-replacement',
    generic: { en: 'Nicotine replacement therapy (NRT)', ko: '니코틴 대체 요법 (금연 보조)', ja: 'ニコチン代替療法(NRT、禁煙補助)' },
    brands: ['Nicorette (gum/lozenge)', 'NicoDerm CQ (patch)', 'Nicotrol'],
    category: 'other',
    uses: [
      { title_en: 'Smoking cessation aid', title_ko: '금연 보조', title_ja: '禁煙補助',
        detail_en: 'Reduces withdrawal symptoms and cravings by providing controlled nicotine doses without the harmful chemicals in cigarettes. Doubles quit success rates when combined with behavioral support.',
        detail_ko: '담배의 유해 화학물질 없이 조절된 니코틴 용량을 공급하여 금단 증상과 갈망을 감소. 행동 치료와 병행 시 금연 성공률이 2배.',
        detail_ja: 'タバコの有害化学物質なしに制御されたニコチン量を供給し離脱症状と渇望を軽減。行動療法と併用で禁煙成功率が2倍。' }
    ],
    dose_en: { 'Patch (heavy smoker >10/day)': '21 mg/day for 6 weeks → 14 mg for 2 weeks → 7 mg for 2 weeks', 'Gum/lozenge': '2 mg (<25 cig/day) or 4 mg (>25 cig/day), 1 piece every 1–2 hours', 'Gum technique': 'Chew, park between cheek and gum, chew again — do not chew like regular gum (causes hiccups, nausea)', 'Duration': '8–12 weeks typical; longer use is safer than continued smoking' },
    dose_ko: { '패치 (하루 >10개비)': '6주간 21 mg/일 → 2주간 14 mg → 2주간 7 mg', '껌·로젠지': '하루 25개비 미만이면 2 mg, 이상이면 4 mg, 1~2시간마다 1개', '껌 사용법': '씹다가 볼과 잇몸 사이에 보관했다가 다시 씹기 — 일반 껌처럼 씹으면 딸꾹질·메스꺼움', '기간': '일반적으로 8~12주; 장기 사용도 흡연 지속보다 안전' },
    dose_ja: { 'パッチ(1日10本超の重度喫煙者)': '6週間21 mg/日 → 2週間14 mg → 2週間7 mg', 'ガム·ロゼンジ': '1日25本未満で2 mg、超で4 mg、1~2時間ごとに1個', 'ガムの使用法': '噛んで、頬と歯茎の間に置き、再び噛む — 通常のガムのように噛むとしゃっくり·吐き気を起こす', '期間': '通常8~12週;長期使用も喫煙継続より安全' },
    warn_en: 'DO NOT smoke while using NRT — nicotine toxicity risk. Remove patch before MRI. Rotate patch site to prevent skin irritation. Vivid dreams common with patch — remove at bedtime if problematic. If you have heart disease, recent heart attack, or uncontrolled high blood pressure, talk to doctor first. Quit success depends on using for the full recommended duration — most people stop too early.',
    warn_ko: 'NRT 사용 중 흡연하지 마세요 — 니코틴 독성 위험. MRI 전 패치 제거. 패치 부위를 로테이션해야 피부 자극 예방. 패치 사용 시 생생한 꿈이 흔함 — 문제시 취침 시 제거. 심장병, 최근 심장마비, 조절되지 않는 고혈압이 있으면 먼저 의사와 상담. 금연 성공은 권장 기간을 모두 사용하는 데 달려있으며, 대부분 너무 빨리 중단합니다.',
    warn_ja: 'NRT使用中は喫煙禁止 — ニコチン中毒リスク。MRI前にパッチ除去。皮膚刺激予防のためパッチ部位をローテーション。パッチ使用時に鮮明な夢が多い — 問題なら就寝時に除去。心疾患、最近の心筋梗塞、コントロール不良の高血圧がある場合はまず医師に相談。禁煙成功は推奨期間を完遂することにかかっており、多くの人は早すぎて中止します。',
    interact: [
      { en: 'Caffeine, theophylline — nicotine withdrawal can raise their levels (cut caffeine in half during quitting)', ko: '카페인, 테오필린 — 니코틴 금단이 이들 농도를 상승시킴 (금연 중 카페인 절반으로 감소)', ja: 'カフェイン、テオフィリン — ニコチン離脱でこれらの濃度が上昇(禁煙中はカフェインを半量に減らす)' },
      { en: 'Insulin, blood pressure medications — may need dose adjustment after quitting', ko: '인슐린, 혈압약 — 금연 후 용량 조정이 필요할 수 있음', ja: 'インスリン、降圧薬 — 禁煙後に用量調整が必要な場合あり' },
      { en: 'Warfarin — levels may change after quitting', ko: '와파린 — 금연 후 농도 변화 가능', ja: 'ワーファリン — 禁煙後に濃度変動の可能性' }
    ],
    source: 'FDA OTC Monograph · CDC Smoking Cessation Guidelines · DailyMed (NIH)'
  },
  {
    id: 'lidocaine-patch',
    generic: { en: 'Lidocaine patch 4% (topical pain)', ko: '리도카인 패치 4% (국소 통증)', ja: 'リドカインパッチ4%(局所鎮痛)' },
    brands: ['Salonpas Lidocaine', 'Aspercreme with Lidocaine', 'IcyHot Lidocaine'],
    category: 'pain',
    uses: [
      { title_en: 'Minor muscle and joint pain', title_ko: '경미한 근육·관절 통증', title_ja: '軽度の筋肉·関節痛',
        detail_en: 'Temporarily numbs skin to relieve pain from muscle strains, sprains, backache, simple arthritis, and bruising',
        detail_ko: '근육 긴장, 염좌, 요통, 단순 관절염, 타박상으로 인한 통증을 일시적으로 마취하여 완화',
        detail_ja: '筋肉の緊張、捻挫、腰痛、単純な関節炎、打撲による痛みを一時的に麻酔して緩和' },
      { title_en: 'Localized nerve-type pain (adjunct)', title_ko: '국소 신경성 통증 (보조)', title_ja: '局所性神経痛(補助)',
        detail_en: 'Can help with postherpetic neuralgia or diabetic nerve pain — but prescription 5% patch is more effective for these',
        detail_ko: '대상포진 후 신경통이나 당뇨성 신경통에 도움이 될 수 있으나, 이런 경우 처방용 5% 패치가 더 효과적',
        detail_ja: '帯状疱疹後神経痛や糖尿病性神経痛に役立つ場合がありますが、これらには処方用5%パッチがより有効' }
    ],
    dose_en: { 'Application': 'Apply 1 patch to affected area, up to 3 patches at once', 'Duration': 'Wear up to 12 hours, then 12 hours off', 'Do not apply to': 'Broken skin, eyes, mouth, or with heating pads' },
    dose_ko: { '도포': '환부에 패치 1장, 최대 동시 3장', '지속 시간': '최대 12시간 착용 후 12시간 휴식', '도포 금지': '벗겨진 피부, 눈, 입, 또는 온찜질 패드와 함께 사용 금지' },
    dose_ja: { '貼付': '患部にパッチ1枚、同時に最大3枚まで', '持続時間': '最大12時間貼付後、12時間休止', '貼付禁止部位': '損傷した皮膚、目、口、または温熱パッドとの併用禁止' },
    danger_en: 'LIDOCAINE TOXICITY — Using more patches than recommended, leaving on longer, using on broken skin, or combining with heat can cause lidocaine to enter bloodstream and cause serious heart rhythm problems, seizures, or death. If you feel dizzy, numb beyond the patch, have ringing in ears, or irregular heartbeat — remove all patches and call a doctor.',
    danger_ko: '리도카인 독성 — 권장량 초과 패치 사용, 더 오래 부착, 벗겨진 피부 사용, 열과 병용 시 리도카인이 혈류로 흡수되어 심각한 부정맥, 경련, 사망을 일으킬 수 있습니다. 어지러움, 패치 범위 너머의 무감각, 이명, 불규칙한 심박을 느끼면 모든 패치를 제거하고 의사에게 연락하세요.',
    danger_ja: 'リドカイン中毒 — 推奨枚数を超えた使用、長時間貼付、損傷皮膚への使用、または熱との併用により、リドカインが血流に吸収され重篤な不整脈、けいれん、死亡を起こすことがあります。めまい、パッチ範囲を超えるしびれ、耳鳴り、不整脈を感じたら、すべてのパッチを除去し医師に連絡してください。',
    warn_en: 'Do not use on children under 12 without doctor. Do not cut patches. Wash hands after handling. If pain is not better after 7 days, see a doctor. Menthol/methyl salicylate versions (not lidocaine) are less risky for general use.',
    warn_ko: '의사 지시 없이 12세 미만 어린이에게 사용하지 마세요. 패치를 자르지 마세요. 취급 후 손을 씻으세요. 7일 후에도 통증이 호전되지 않으면 의사를 만나세요. 멘톨·메틸살리실레이트 제품(리도카인 아님)이 일반적 사용에 위험이 적습니다.',
    warn_ja: '医師の指示なく12歳未満の小児に使用しないでください。パッチを切らないでください。取り扱い後は手を洗ってください。7日後も痛みが改善しない場合は医師を受診してください。メントール·サリチル酸メチル製品(リドカインではない)の方が一般使用には低リスクです。',
    interact: [
      { en: 'Heart rhythm medications (Class I antiarrhythmics) — additive lidocaine effect', ko: '부정맥약 (Class I 항부정맥제) — 리도카인 효과 누적', ja: '不整脈薬(Class I抗不整脈薬) — リドカイン効果の累積' },
      { en: 'Heating pads or hot showers on patch site — dangerous absorption increase', ko: '패치 부위 온찜질 또는 뜨거운 샤워 — 위험한 흡수 증가', ja: 'パッチ部位への温熱パッドまたは熱いシャワー — 危険な吸収増加' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'mucinex-d',
    generic: { en: 'Guaifenesin + Pseudoephedrine (Mucinex D)', ko: '구아이페네신 + 슈도에페드린 (복합제)', ja: 'グアイフェネシン + プソイドエフェドリン(複合薬)' },
    brands: ['Mucinex D', 'Mucinex Sinus-Max'],
    category: 'cough',
    uses: [
      { title_en: 'Chest congestion + nasal congestion', title_ko: '가슴 답답함 + 코막힘', title_ja: '胸のつまり + 鼻づまり',
        detail_en: 'Combination product — guaifenesin thins mucus in the chest while pseudoephedrine shrinks swollen nasal passages',
        detail_ko: '복합제 — 구아이페네신은 가슴 가래를 묽게 하고, 슈도에페드린은 부은 비강을 축소',
        detail_ja: '複合薬 — グアイフェネシンが胸の痰を薄め、プソイドエフェドリンが腫れた鼻腔を収縮' },
      { title_en: 'Sinus pressure with productive cough', title_ko: '가래 동반 부비동 압박', title_ja: '痰を伴う副鼻腔圧迫',
        detail_en: 'Useful when cold or sinus infection involves both stuffy nose and chest mucus',
        detail_ko: '감기나 부비동 감염이 코막힘과 가슴 가래를 동시에 유발할 때 유용',
        detail_ja: '風邪や副鼻腔感染が鼻づまりと胸の痰を同時に起こす場合に有用' }
    ],
    dose_en: { 'Adult and child 12+': '1 tablet every 12 hours (extended release)', 'Max per day': '2 tablets', 'Purchase': 'Behind the counter — ID required (contains pseudoephedrine)', 'Alternative': 'If you don\'t have congestion, Mucinex (guaifenesin alone) is enough' },
    dose_ko: { '성인 및 12세 이상': '12시간마다 1정 (서방형)', '하루 최대': '2정', '구매': '카운터 뒤 판매 — 신분증 필요 (슈도에페드린 함유)', '대체': '코막힘이 없다면 Mucinex (구아이페네신 단독)로 충분' },
    dose_ja: { '成人および12歳以上': '12時間ごとに1錠(徐放性)', '1日最大量': '2錠', '購入': 'カウンター裏販売 — 身分証明書必要(プソイドエフェドリン含有)', '代替': '鼻づまりがなければMucinex(グアイフェネシン単独)で十分' },
    danger_en: 'SAME RISKS AS PSEUDOEPHEDRINE — Raises blood pressure and heart rate. Do NOT use with uncontrolled high blood pressure, heart disease, hyperthyroidism, glaucoma, or enlarged prostate. Can cause insomnia, anxiety, heart palpitations. Many people take this with other cold medicines — check for double-dosing (many combination products contain pseudoephedrine).',
    danger_ko: '슈도에페드린과 동일한 위험 — 혈압과 심박수 상승. 조절되지 않는 고혈압, 심장병, 갑상선 기능 항진증, 녹내장, 전립선 비대에서는 사용 금지. 불면, 불안, 심계항진 유발 가능. 많은 환자가 다른 감기약과 함께 복용하여 중복 복용 위험이 있으니 (복합 감기약에 슈도에페드린이 흔히 포함) 확인하세요.',
    danger_ja: 'プソイドエフェドリンと同じリスク — 血圧と心拍数を上昇。コントロール不良の高血圧、心疾患、甲状腺機能亢進症、緑内障、前立腺肥大では使用禁止。不眠、不安、動悸の可能性。多くの患者が他の風邪薬と併用し重複投与リスクがあるため(複合風邪薬にプソイドエフェドリンがよく含まれる)確認してください。',
    warn_en: 'Do not take within 2 hours of bedtime. Do not use for more than 7 days. In the US, purchase is federally restricted (Combat Methamphetamine Act) — must show ID.',
    warn_ko: '취침 2시간 이내 복용 금지. 7일 이상 사용 금지. 미국에서는 연방법(메스암페타민 규제법)에 의해 구매 제한되며 신분증 제시 필요.',
    warn_ja: '就寝2時間以内には服用禁止。7日以上使用禁止。米国では連邦法(メタンフェタミン規制法)により購入制限があり身分証明書提示必要。',
    interact: [
      { en: 'MAO inhibitors — dangerous blood pressure spike', ko: 'MAO 억제제 — 위험한 혈압 급상승', ja: 'MAO阻害薬 — 危険な血圧急上昇' },
      { en: 'Blood pressure medications — reduced effectiveness', ko: '혈압약 — 효과 감소', ja: '降圧薬 — 効果減少' },
      { en: 'Other decongestants — dangerous additive effect', ko: '다른 코막힘약 — 위험한 효과 누적', ja: '他の鼻づまり薬 — 危険な作用累積' },
      { en: 'Other cold/flu combos containing pseudoephedrine — double-dose risk', ko: '슈도에페드린 함유 다른 감기·독감 복합제 — 중복 복용 위험', ja: 'プソイドエフェドリン含有の他の風邪·インフルエンザ複合薬 — 重複投与リスク' }
    ],
    source: 'FDA OTC Monograph 21 CFR 341 · DailyMed (NIH)'
  },

  // ============ SLEEP & MENTAL ============
  {
    id: 'doxylamine',
    generic: { en: 'Doxylamine succinate', ko: '독실아민 숙신산염', ja: 'ドキシラミンコハク酸塩' },
    brands: ['Unisom SleepTabs', 'NyQuil (as ingredient)'],
    category: 'sleep',
    uses: [
      { title_en: 'Occasional sleeplessness', title_ko: '일시적 불면', title_ja: '一時的な不眠',
        detail_en: 'First-generation antihistamine used as a nighttime sleep aid for occasional difficulty falling asleep',
        detail_ko: '가끔씩 잠들기 어려울 때 야간 수면 보조제로 사용되는 1세대 항히스타민',
        detail_ja: '時々寝つきが悪い場合の夜間睡眠補助として使用される第一世代抗ヒスタミン薬' },
      { title_en: 'Nausea of pregnancy (with vitamin B6)', title_ko: '임신 오심 (비타민 B6 병용)', title_ja: '妊娠悪阻(ビタミンB6併用)',
        detail_en: 'Combined with pyridoxine (B6) for morning sickness — prescription product (Diclegis) but OTC doxylamine sometimes used under obstetric guidance',
        detail_ko: '피리독신(B6)과 함께 입덧에 사용 — 처방 복합제(Diclegis)가 있으며 산과 지침 하에 OTC 독실아민이 사용되기도 함',
        detail_ja: 'ピリドキシン(B6)と併用してつわりに使用 — 処方複合薬(Diclegis)あり、産科指導下でOTCドキシラミンが使用される場合あり' }
    ],
    dose_en: { 'Adult sleep-aid': '25 mg 30 minutes before bedtime', 'Max duration (self-treatment)': '2 weeks — see a doctor if insomnia persists', 'Child under 12': 'Do not use for sleep' },
    dose_ko: { '성인 수면 보조': '취침 30분 전 25 mg', '자가 치료 최대 기간': '2주 — 불면이 지속되면 의사 상담', '12세 미만 소아': '수면 목적으로 사용하지 마세요' },
    dose_ja: { '成人睡眠補助': '就寝30分前に25 mg', '自己治療最大期間': '2週間 — 不眠が続く場合は医師に相談', '12歳未満小児': '睡眠目的で使用しないでください' },
    danger_en: 'STRONG SEDATIVE AND ANTICHOLINERGIC EFFECTS. Do not drive or operate machinery after taking. Elderly patients (65+) are at high risk for falls, confusion, and worsened dementia — the American Geriatrics Society Beers Criteria recommends avoiding first-generation antihistamines in older adults.',
    danger_ko: '강한 진정·항콜린 작용이 있습니다. 복용 후 운전이나 기계 조작을 하지 마세요. 65세 이상 고령자에서는 낙상, 혼동, 치매 악화 위험이 높아 미국노인의학회 Beers Criteria는 노인에게 1세대 항히스타민 사용을 권장하지 않습니다.',
    danger_ja: '強い鎮静·抗コリン作用があります。服用後は運転や機械操作を避けてください。65歳以上の高齢者では転倒、混乱、認知症悪化のリスクが高く、米国老年医学会Beers基準は高齢者の第一世代抗ヒスタミン薬使用を推奨しません。',
    warn_en: 'Avoid alcohol and other sedating medications. Do not use with glaucoma, enlarged prostate, urinary retention, asthma, or chronic lung disease without a doctor\'s advice. Tolerance develops quickly — if needed more than occasionally, see a doctor.',
    warn_ko: '알코올 및 다른 진정제와 함께 복용하지 마세요. 녹내장, 전립선 비대, 요폐, 천식, 만성 폐질환이 있으면 의사 상담 없이 사용하지 마세요. 내성이 빨리 생기므로 가끔 이상 필요하면 의사와 상담하세요.',
    warn_ja: 'アルコールおよび他の鎮静薬と併用しないでください。緑内障、前立腺肥大、尿閉、喘息、慢性肺疾患がある場合は医師の助言なく使用しないでください。耐性が早く形成されるため、たまに以上必要なら医師に相談。',
    interact: [
      { en: 'Alcohol — additive sedation, impaired coordination', ko: '알코올 — 진정 작용 가중, 협응 장애', ja: 'アルコール — 鎮静作用累積、協調運動障害' },
      { en: 'Benzodiazepines, opioids, muscle relaxants — dangerous CNS depression', ko: '벤조디아제핀, 오피오이드, 근이완제 — 위험한 중추신경 억제', ja: 'ベンゾジアゼピン、オピオイド、筋弛緩薬 — 危険な中枢神経抑制' },
      { en: 'Other anticholinergics (oxybutynin, tricyclic antidepressants) — confusion, urinary retention', ko: '기타 항콜린제 (옥시부티닌, 삼환계 항우울제) — 혼동, 요폐', ja: '他の抗コリン薬(オキシブチニン、三環系抗うつ薬) — 混乱、尿閉' },
      { en: 'MAO inhibitors — avoid; hypertensive crisis risk', ko: 'MAO 억제제 — 사용 금지; 고혈압 위기 위험', ja: 'MAO阻害薬 — 使用禁止;高血圧危機リスク' }
    ],
    source: 'FDA OTC Monograph 21 CFR 338 · DailyMed (NIH) · AGS Beers Criteria 2023'
  },
  {
    id: 'valerian',
    generic: { en: 'Valerian root (Valeriana officinalis)', ko: '발레리안 뿌리', ja: 'バレリアン根(セイヨウカノコソウ)' },
    brands: ['Nature\'s Way', 'NOW Foods', 'Solaray'],
    category: 'sleep',
    uses: [
      { title_en: 'Mild sleep difficulty', title_ko: '경미한 수면 장애', title_ja: '軽度の睡眠障害',
        detail_en: 'Traditional herbal sedative; some studies suggest modest improvement in sleep latency and quality, but evidence is mixed and effect is smaller than prescription sleep medications',
        detail_ko: '전통적인 약용 진정제; 일부 연구에서 수면 잠복기와 수면 질이 약간 개선된다고 보고되나 근거는 일관되지 않으며 효과는 처방 수면제보다 작음',
        detail_ja: '伝統的な薬用鎮静剤;一部の研究で睡眠潜時と睡眠の質がわずかに改善されると報告されているがエビデンスは一貫せず、効果は処方睡眠薬より小さい' },
      { title_en: 'Mild anxiety symptoms', title_ko: '경미한 불안 증상', title_ja: '軽度の不安症状',
        detail_en: 'Sometimes used for daytime anxiety or nervousness; evidence is weaker than for sleep use',
        detail_ko: '낮 동안의 불안이나 긴장에 사용되기도 하나 수면 목적보다 근거가 약함',
        detail_ja: '日中の不安や緊張に使用されることもあるが睡眠目的よりエビデンスが弱い' }
    ],
    dose_en: { 'Typical (extract)': '300–600 mg standardized extract 30–60 minutes before bedtime', 'Tea': '2–3 g dried root steeped in hot water', 'Onset': 'May take 2–4 weeks of nightly use for full effect' },
    dose_ko: { '일반 용량 (추출물)': '취침 30~60분 전 표준화 추출물 300~600 mg', '차': '건조 뿌리 2~3 g을 뜨거운 물에 우림', '효과 발현': '매일 밤 복용 시 완전한 효과까지 2~4주 소요될 수 있음' },
    dose_ja: { '一般用量(抽出物)': '就寝30~60分前に標準化抽出物300~600 mg', '茶': '乾燥根2~3 gをお湯に浸す', '効果発現': '毎晩服用で完全な効果まで2~4週間かかる場合あり' },
    danger_en: 'Not well-studied for long-term safety. Reports of liver injury exist (rare, possibly from contaminated products). Do not combine with other sedatives, alcohol, or prescription sleep medications.',
    danger_ko: '장기 복용 안전성은 충분히 연구되지 않았습니다. 드물게 간 손상 보고가 있으며 오염된 제품 때문일 가능성이 있습니다. 다른 진정제, 알코올, 처방 수면제와 병용하지 마세요.',
    danger_ja: '長期使用の安全性は十分に研究されていません。稀に肝障害の報告があり、汚染製品が原因の可能性。他の鎮静薬、アルコール、処方睡眠薬と併用しないでください。',
    warn_en: 'Not recommended during pregnancy or breastfeeding (insufficient safety data). Stop 2 weeks before surgery — may increase effect of anesthesia. Supplement quality varies significantly between brands.',
    warn_ko: '임신·수유 중에는 권장되지 않습니다 (안전성 자료 부족). 수술 2주 전에는 중단하세요 — 마취제 효과를 증강시킬 수 있습니다. 제품 품질이 브랜드 간 크게 차이납니다.',
    warn_ja: '妊娠·授乳中は推奨されません(安全性データ不足)。手術2週間前に中止 — 麻酔効果を増強する可能性。製品品質はブランド間で大きく異なります。',
    interact: [
      { en: 'Alcohol, benzodiazepines, opioids — additive sedation', ko: '알코올, 벤조디아제핀, 오피오이드 — 진정 작용 가중', ja: 'アルコール、ベンゾジアゼピン、オピオイド — 鎮静作用累積' },
      { en: 'Anesthetics — may prolong effect; stop 2 weeks before surgery', ko: '마취제 — 효과 연장 가능; 수술 2주 전 중단', ja: '麻酔薬 — 効果延長の可能性;手術2週間前に中止' },
      { en: 'Other herbal sedatives (kava, chamomile, hops) — excess drowsiness', ko: '다른 약용 진정제 (카바, 카모마일, 홉) — 과도한 졸음', ja: '他の薬用鎮静剤(カバ、カモミール、ホップ) — 過度の眠気' }
    ],
    source: 'NIH Office of Dietary Supplements · MedlinePlus'
  },
  {
    id: 'l-theanine',
    generic: { en: 'L-theanine', ko: 'L-테아닌', ja: 'L-テアニン' },
    brands: ['NOW Foods', 'Jarrow Formulas', 'Suntheanine (ingredient)'],
    category: 'sleep',
    uses: [
      { title_en: 'Relaxation without drowsiness', title_ko: '졸음 없는 이완', title_ja: '眠気のないリラックス',
        detail_en: 'Amino acid found in tea leaves; may promote calm focus and reduce stress response without causing sedation — useful during the day',
        detail_ko: '찻잎에 함유된 아미노산; 진정을 유발하지 않고 차분한 집중과 스트레스 반응 감소를 돕는다고 보고됨 — 낮 동안 사용 가능',
        detail_ja: '茶葉に含まれるアミノ酸;鎮静を起こさず落ち着いた集中とストレス反応軽減を促進と報告 — 日中使用可能' },
      { title_en: 'Sleep quality support', title_ko: '수면 질 개선', title_ja: '睡眠の質改善',
        detail_en: 'Some evidence for improved subjective sleep quality, likely by reducing anticipatory anxiety rather than causing sleep',
        detail_ko: '주관적 수면 질 개선 근거가 일부 있으며, 수면을 직접 유도하기보다는 잠들기 전 불안 감소를 통한 간접 효과로 추정됨',
        detail_ja: '主観的睡眠の質改善のエビデンス一部あり、睡眠を直接誘導するより就寝前不安軽減による間接効果と推定' }
    ],
    dose_en: { 'Typical': '100–400 mg daily, can divide doses', 'For sleep': '200 mg taken 30–60 minutes before bedtime', 'Combined with caffeine': 'Often paired 1:1 or 2:1 with caffeine to reduce jitteriness' },
    dose_ko: { '일반 용량': '하루 100~400 mg, 분할 복용 가능', '수면 목적': '취침 30~60분 전 200 mg', '카페인 병용': '카페인과 1:1 또는 2:1로 병용하여 각성 불안감 감소' },
    dose_ja: { '一般用量': '1日100~400 mg、分割服用可能', '睡眠目的': '就寝30~60分前に200 mg', 'カフェイン併用': 'カフェインと1:1または2:1で併用しジリジリ感を軽減' },
    danger_en: 'Generally well-tolerated in studies up to 400 mg/day. No major safety concerns identified, but long-term data (beyond several months) are limited.',
    danger_ko: '하루 400 mg까지의 연구에서 일반적으로 잘 견디는 것으로 보고됩니다. 주요 안전성 문제는 확인되지 않았으나 수개월을 넘는 장기 복용 자료는 제한적입니다.',
    danger_ja: '1日400 mgまでの研究で一般的に忍容性良好と報告。主要な安全性問題は確認されていませんが数か月を超える長期使用データは限定的。',
    warn_en: 'Insufficient safety data during pregnancy and breastfeeding. May lower blood pressure slightly — use caution with antihypertensive medications. Not a replacement for evaluation of chronic insomnia or anxiety disorders.',
    warn_ko: '임신·수유 중 안전성 자료 부족. 혈압을 약간 낮출 수 있어 항고혈압제와 주의가 필요합니다. 만성 불면이나 불안장애 평가를 대체하지 않습니다.',
    warn_ja: '妊娠·授乳中の安全性データ不足。血圧をわずかに下げる可能性があり降圧薬との併用は注意。慢性不眠や不安障害の評価を代替しません。',
    interact: [
      { en: 'Antihypertensive medications — possible additive blood pressure lowering', ko: '항고혈압제 — 혈압 강하 작용 가중 가능', ja: '降圧薬 — 血圧降下作用累積の可能性' },
      { en: 'Stimulants (caffeine, ADHD medications) — L-theanine may blunt jitteriness; not necessarily a problem', ko: '자극제 (카페인, ADHD 약) — L-테아닌이 각성 불안감을 완화할 수 있으며 반드시 문제는 아님', ja: '覚醒剤(カフェイン、ADHD薬) — L-テアニンがジリジリ感を緩和する可能性、必ずしも問題ではない' },
      { en: 'Sedatives — minor additive calming effect', ko: '진정제 — 경미한 진정 작용 가중', ja: '鎮静薬 — 軽度の鎮静作用累積' }
    ],
    source: 'NIH Office of Dietary Supplements · MedlinePlus'
  },
  {
    id: '5-htp',
    generic: { en: '5-hydroxytryptophan (5-HTP)', ko: '5-하이드록시트립토판 (5-HTP)', ja: '5-ヒドロキシトリプトファン(5-HTP)' },
    brands: ['NOW Foods', 'Natrol', 'Doctor\'s Best'],
    category: 'sleep',
    uses: [
      { title_en: 'Mild mood support', title_ko: '경미한 기분 개선 보조', title_ja: '軽度の気分サポート',
        detail_en: 'Precursor to serotonin; limited evidence for mild depressive symptoms. Not a substitute for prescription antidepressants',
        detail_ko: '세로토닌 전구체; 경미한 우울 증상에 제한적인 근거. 처방 항우울제를 대체하지 않음',
        detail_ja: 'セロトニンの前駆体;軽度のうつ症状に限定的なエビデンス。処方抗うつ薬を代替しない' },
      { title_en: 'Sleep onset support', title_ko: '수면 유도 보조', title_ja: '睡眠導入サポート',
        detail_en: 'May improve sleep latency through serotonin conversion to melatonin; evidence is limited',
        detail_ko: '세로토닌을 거쳐 멜라토닌으로 전환되어 수면 잠복기를 단축할 수 있다고 보고되나 근거 제한적',
        detail_ja: 'セロトニンを経てメラトニンに変換され睡眠潜時を短縮する可能性があると報告されるがエビデンス限定的' }
    ],
    dose_en: { 'Typical': '50–100 mg 2–3 times daily', 'For sleep': '100–300 mg 30–45 minutes before bedtime', 'Start low': 'Begin with 50 mg to assess GI tolerance' },
    dose_ko: { '일반 용량': '하루 2~3회 50~100 mg', '수면 목적': '취침 30~45분 전 100~300 mg', '저용량 시작': '위장 내약성 평가를 위해 50 mg부터 시작' },
    dose_ja: { '一般用量': '1日2~3回50~100 mg', '睡眠目的': '就寝30~45分前に100~300 mg', '低用量開始': '消化器忍容性評価のため50 mgから開始' },
    danger_en: 'SEROTONIN SYNDROME RISK when combined with antidepressants (SSRIs, SNRIs, MAOIs, tricyclics), tramadol, triptans, or dextromethorphan. Symptoms include agitation, sweating, tremor, high heart rate, fever — potentially fatal. Do not combine with any serotonergic medication without medical supervision.',
    danger_ko: '세로토닌 증후군 위험 — 항우울제(SSRI, SNRI, MAOI, 삼환계), 트라마돌, 트립탄, 덱스트로메토르판과 병용 시. 증상으로 흥분, 발한, 떨림, 심박수 증가, 발열이 있으며 치명적일 수 있습니다. 의료 감독 없이 세로토닌 작용 약물과 병용하지 마세요.',
    danger_ja: 'セロトニン症候群リスク — 抗うつ薬(SSRI、SNRI、MAOI、三環系)、トラマドール、トリプタン、デキストロメトルファンとの併用時。症状に興奮、発汗、振戦、頻脈、発熱があり致命的になる可能性。医療監督なくセロトニン作動性薬剤と併用しないでください。',
    warn_en: 'Avoid in pregnancy and breastfeeding. Associated historically with eosinophilia-myalgia syndrome (contamination issue from impure tryptophan in 1989 — rare now but quality matters). GI side effects common: nausea, heartburn, diarrhea.',
    warn_ko: '임신·수유 중 피하세요. 과거 순도 문제로 호산구-근육통 증후군과 연관된 바 있습니다(1989년; 현재는 드물지만 제품 품질이 중요). 메스꺼움, 속쓰림, 설사 등 위장 부작용이 흔합니다.',
    warn_ja: '妊娠·授乳中は回避。過去に純度問題で好酸球増加筋痛症候群と関連(1989年;現在は稀だが製品品質が重要)。吐き気、胸焼け、下痢など消化器副作用が一般的。',
    interact: [
      { en: 'SSRIs, SNRIs, MAOIs, tricyclic antidepressants — serotonin syndrome risk', ko: 'SSRI, SNRI, MAOI, 삼환계 항우울제 — 세로토닌 증후군 위험', ja: 'SSRI、SNRI、MAOI、三環系抗うつ薬 — セロトニン症候群リスク' },
      { en: 'Tramadol, triptans (sumatriptan), dextromethorphan — serotonin syndrome risk', ko: '트라마돌, 트립탄 (수마트립탄), 덱스트로메토르판 — 세로토닌 증후군 위험', ja: 'トラマドール、トリプタン(スマトリプタン)、デキストロメトルファン — セロトニン症候群リスク' },
      { en: 'Carbidopa — may cause scleroderma-like skin changes', ko: '카르비도파 — 경피증 유사 피부 변화 가능', ja: 'カルビドパ — 強皮症様皮膚変化の可能性' },
      { en: 'St. John\'s wort, SAMe — additive serotonergic effect', ko: '세인트존스워트, SAMe — 세로토닌 작용 가중', ja: 'セントジョーンズワート、SAMe — セロトニン作動性作用の累積' }
    ],
    source: 'NIH Office of Dietary Supplements · MedlinePlus'
  },
  {
    id: 'gaba',
    generic: { en: 'Gamma-aminobutyric acid (GABA)', ko: '가바 (감마-아미노부티르산)', ja: 'γ-アミノ酪酸(GABA)' },
    brands: ['NOW Foods', 'Source Naturals', 'Thorne'],
    category: 'sleep',
    uses: [
      { title_en: 'Relaxation and stress support', title_ko: '이완 및 스트레스 보조', title_ja: 'リラックス·ストレスサポート',
        detail_en: 'Major inhibitory neurotransmitter in the brain; oral GABA supplements are marketed for calm and sleep, but whether oral GABA crosses the blood-brain barrier is debated',
        detail_ko: '뇌의 주요 억제성 신경전달물질; 경구 GABA 보충제는 진정·수면 용도로 판매되나 경구 섭취 시 혈액뇌관문 통과 여부에 대해서는 논란이 있음',
        detail_ja: '脳の主要な抑制性神経伝達物質;経口GABAサプリメントは鎮静·睡眠用途で販売されているが、経口摂取時の血液脳関門通過については議論あり' },
      { title_en: 'Sleep onset (limited evidence)', title_ko: '수면 유도 (제한적 근거)', title_ja: '睡眠導入(限定的エビデンス)',
        detail_en: 'Some small studies suggest modest improvement in sleep latency; larger studies are lacking',
        detail_ko: '일부 소규모 연구에서 수면 잠복기가 소폭 단축됨이 보고되었으나 대규모 연구는 부족',
        detail_ja: '一部の小規模研究で睡眠潜時のわずかな短縮が報告されているが大規模研究は不足' }
    ],
    dose_en: { 'Typical': '100–750 mg before bedtime', 'Max studied': 'Generally up to 3 g/day in research settings', 'Onset': 'Reported effects within 30–60 minutes if effective' },
    dose_ko: { '일반 용량': '취침 전 100~750 mg', '연구 최대 용량': '연구 환경에서 일반적으로 하루 최대 3 g', '효과 발현': '효과가 있다면 30~60분 이내로 보고됨' },
    dose_ja: { '一般用量': '就寝前100~750 mg', '研究最大用量': '研究環境で一般的に1日最大3 g', '効果発現': '効果がある場合30~60分以内と報告' },
    danger_en: 'Efficacy is uncertain due to blood-brain barrier permeability questions. Generally considered low-risk at typical doses, but mild side effects include drowsiness, tingling in extremities, throat tightness.',
    danger_ko: '혈액뇌관문 통과 문제로 효과가 불확실합니다. 일반 용량에서는 위험도가 낮은 편이나 졸음, 사지 저림, 인후 긴장감 등 경미한 부작용이 보고됩니다.',
    danger_ja: '血液脳関門通過の問題で有効性は不確実。一般用量ではリスクは低いとされるが、眠気、四肢のしびれ、のどの締め付け感など軽度の副作用が報告される。',
    warn_en: 'Not recommended in pregnancy, breastfeeding, or before surgery (stop 2 weeks prior). Do not combine with alcohol, sedatives, or prescription sleep medications.',
    warn_ko: '임신·수유 중이나 수술 전(2주 전 중단)에는 권장되지 않습니다. 알코올, 진정제, 처방 수면제와 병용하지 마세요.',
    warn_ja: '妊娠·授乳中や手術前(2週間前に中止)には推奨されません。アルコール、鎮静薬、処方睡眠薬と併用しないでください。',
    interact: [
      { en: 'Alcohol, benzodiazepines, opioids, other sedatives — additive CNS depression', ko: '알코올, 벤조디아제핀, 오피오이드, 기타 진정제 — 중추신경 억제 가중', ja: 'アルコール、ベンゾジアゼピン、オピオイド、他の鎮静薬 — 中枢神経抑制の累積' },
      { en: 'Antihypertensive medications — possible blood pressure lowering', ko: '항고혈압제 — 혈압 강하 가능', ja: '降圧薬 — 血圧降下の可能性' },
      { en: 'Other calming herbs (valerian, chamomile, kava) — additive sedation', ko: '다른 진정 허브 (발레리안, 카모마일, 카바) — 진정 작용 가중', ja: '他の鎮静ハーブ(バレリアン、カモミール、カバ) — 鎮静作用の累積' }
    ],
    source: 'NIH Office of Dietary Supplements · MedlinePlus'
  },
  {
    id: 'same',
    generic: { en: 'S-adenosylmethionine (SAMe)', ko: 'S-아데노실메티오닌 (SAMe)', ja: 'S-アデノシルメチオニン(SAMe)' },
    brands: ['Jarrow Formulas', 'Nature Made', 'Doctor\'s Best'],
    category: 'sleep',
    uses: [
      { title_en: 'Mild to moderate depression', title_ko: '경도~중등도 우울', title_ja: '軽度~中等度のうつ',
        detail_en: 'Some evidence of efficacy comparable to tricyclic antidepressants in mild-to-moderate depression; does not replace prescription treatment for major depressive disorder',
        detail_ko: '경도~중등도 우울에서 삼환계 항우울제와 유사한 효과를 보인다는 근거가 있으나 주요우울장애의 처방 치료를 대체하지 않음',
        detail_ja: '軽度~中等度のうつで三環系抗うつ薬と同等の有効性を示すエビデンスあり;大うつ病性障害の処方治療を代替しない' },
      { title_en: 'Osteoarthritis pain', title_ko: '골관절염 통증', title_ja: '変形性関節症の痛み',
        detail_en: 'Some studies suggest efficacy comparable to NSAIDs for osteoarthritis pain with fewer GI side effects',
        detail_ko: '골관절염 통증에 대해 NSAID와 유사한 효과를 보이면서 위장 부작용이 적다는 연구가 있음',
        detail_ja: '変形性関節症の痛みにNSAIDと同等の有効性を示し胃腸副作用が少ないとの研究あり' }
    ],
    dose_en: { 'Depression': '400–1600 mg/day in divided doses', 'Osteoarthritis': '600–1200 mg/day', 'Form': 'Enteric-coated tablets preferred for absorption' },
    dose_ko: { '우울': '하루 400~1600 mg 분할 복용', '골관절염': '하루 600~1200 mg', '제형': '흡수를 위해 장용정 권장' },
    dose_ja: { 'うつ': '1日400~1600 mg分割服用', '変形性関節症': '1日600~1200 mg', '剤形': '吸収のため腸溶錠を推奨' },
    danger_en: 'SERIOUS RISK IN BIPOLAR DISORDER — can trigger mania or hypomania. Do not use with history of bipolar disorder without psychiatric supervision. Serotonin syndrome risk when combined with antidepressants or other serotonergic drugs.',
    danger_ko: '양극성 장애에서 심각한 위험 — 조증·경조증 유발 가능. 양극성 장애 병력이 있으면 정신과 감독 없이 사용하지 마세요. 항우울제 및 기타 세로토닌 작용 약물과 병용 시 세로토닌 증후군 위험.',
    danger_ja: '双極性障害で重大なリスク — 躁·軽躁を誘発する可能性。双極性障害の既往がある場合は精神科の監督なく使用しないでください。抗うつ薬および他のセロトニン作動性薬剤との併用でセロトニン症候群リスク。',
    warn_en: 'Not recommended in pregnancy. May cause GI upset, insomnia, anxiety, or jitteriness (take earlier in day if this occurs). Quality varies significantly between brands — look for USP verification.',
    warn_ko: '임신 중 권장되지 않습니다. 위장 장애, 불면, 불안, 긴장감을 유발할 수 있습니다(이런 증상 시 아침에 복용). 브랜드 간 품질 차이가 커서 USP 인증 제품을 권장합니다.',
    warn_ja: '妊娠中は推奨されません。胃腸障害、不眠、不安、ジリジリ感を引き起こす可能性(これらの症状時は朝に服用)。ブランド間で品質差が大きくUSP認証製品を推奨。',
    interact: [
      { en: 'SSRIs, SNRIs, MAOIs, tricyclics — serotonin syndrome risk', ko: 'SSRI, SNRI, MAOI, 삼환계 — 세로토닌 증후군 위험', ja: 'SSRI、SNRI、MAOI、三環系 — セロトニン症候群リスク' },
      { en: 'Levodopa — may reduce effectiveness of levodopa', ko: '레보도파 — 레보도파 효과 감소 가능', ja: 'レボドパ — レボドパの効果減少の可能性' },
      { en: 'Dextromethorphan, tramadol, St. John\'s wort, 5-HTP — additive serotonergic effect', ko: '덱스트로메토르판, 트라마돌, 세인트존스워트, 5-HTP — 세로토닌 작용 가중', ja: 'デキストロメトルファン、トラマドール、セントジョーンズワート、5-HTP — セロトニン作動性作用の累積' }
    ],
    source: 'NIH Office of Dietary Supplements · MedlinePlus · AHRQ Evidence Report'
  },
  {
    id: 'phosphatidylserine',
    generic: { en: 'Phosphatidylserine (PS)', ko: '포스파티딜세린 (PS)', ja: 'ホスファチジルセリン(PS)' },
    brands: ['NOW Foods', 'Jarrow Formulas', 'Doctor\'s Best'],
    category: 'sleep',
    uses: [
      { title_en: 'Cognitive support in older adults', title_ko: '노년층 인지 보조', title_ja: '高齢者の認知サポート',
        detail_en: 'Phospholipid component of neuronal membranes; limited evidence for mild improvement in age-related memory complaints. FDA permits a qualified health claim with specific cautionary wording',
        detail_ko: '신경세포막의 인지질 성분; 노화 관련 경미한 기억력 저하에 제한적 개선 근거. FDA는 특정 주의 문구를 포함한 조건부 건강 강조 표시를 허용',
        detail_ja: '神経細胞膜のリン脂質成分;加齢関連の軽度記憶低下への改善エビデンスは限定的。FDAは特定の注意文言を伴う条件付き健康強調表示を許可' },
      { title_en: 'Stress and cortisol modulation', title_ko: '스트레스·코르티솔 조절', title_ja: 'ストレス·コルチゾール調節',
        detail_en: 'Some evidence for blunting cortisol response to acute stress (e.g., exercise); may help with overtraining-related fatigue',
        detail_ko: '급성 스트레스(예: 운동)에 대한 코르티솔 반응을 완화한다는 근거가 있으며 과훈련 관련 피로에 도움이 될 수 있음',
        detail_ja: '急性ストレス(運動など)へのコルチゾール反応を緩和するエビデンスあり;オーバートレーニング関連の疲労に役立つ可能性' }
    ],
    dose_en: { 'Typical': '100 mg 3 times daily (300 mg/day total)', 'Stress/sleep': '200–400 mg in evening', 'Source': 'Modern products are soy- or sunflower-derived (older products were bovine-derived and are no longer used due to BSE concerns)' },
    dose_ko: { '일반 용량': '하루 3회 100 mg (총 300 mg)', '스트레스·수면': '저녁 200~400 mg', '원료': '현재는 대두 또는 해바라기 유래 (과거 소 유래는 광우병 우려로 사용되지 않음)' },
    dose_ja: { '一般用量': '1日3回100 mg(計300 mg)', 'ストレス·睡眠': '夕方200~400 mg', '原料': '現在は大豆またはひまわり由来(過去の牛由来はBSE懸念で使用中止)' },
    danger_en: 'Generally well-tolerated. Main side effects are mild GI upset and insomnia at higher doses. Soy-derived products may be a concern in soy allergy.',
    danger_ko: '일반적으로 내약성 양호. 주요 부작용은 경미한 위장 장애이며 고용량에서 불면이 나타날 수 있습니다. 대두 유래 제품은 대두 알레르기에서 주의가 필요합니다.',
    danger_ja: '一般的に忍容性良好。主要な副作用は軽度の胃腸障害で高用量では不眠が現れる可能性。大豆由来製品は大豆アレルギーで注意が必要。',
    warn_en: 'Insufficient pregnancy/breastfeeding data. Theoretical bleeding risk — stop 2 weeks before surgery. FDA qualified health claim for cognitive decline states that "very limited and preliminary scientific research suggests" benefit.',
    warn_ko: '임신·수유 중 자료 부족. 이론적 출혈 위험 — 수술 2주 전 중단. FDA 조건부 건강 강조 표시는 "매우 제한적이고 예비적인 과학적 연구가 시사한다"는 문구를 포함합니다.',
    warn_ja: '妊娠·授乳中のデータ不足。理論的出血リスク — 手術2週間前に中止。FDA条件付き健康強調表示は「非常に限定的で予備的な科学研究が示唆」という文言を含む。',
    interact: [
      { en: 'Anticoagulants (warfarin, apixaban) — theoretical bleeding risk', ko: '항응고제 (와파린, 엘리퀴스) — 이론적 출혈 위험', ja: '抗凝固薬(ワーファリン、エリキュース) — 理論的出血リスク' },
      { en: 'Anticholinergic medications — theoretically opposing mechanism; clinical significance unclear', ko: '항콜린 약물 — 이론적으로 반대 기전; 임상적 중요성 불분명', ja: '抗コリン薬 — 理論的に反対の機序;臨床的重要性不明' },
      { en: 'Cholinesterase inhibitors (donepezil) — possibly additive effect on acetylcholine', ko: '콜린에스테라제 억제제 (도네페질) — 아세틸콜린에 대한 가중 작용 가능', ja: 'コリンエステラーゼ阻害薬(ドネペジル) — アセチルコリンへの作用累積の可能性' }
    ],
    source: 'NIH Office of Dietary Supplements · FDA qualified health claim'
  },
  {
    id: 'chamomile',
    generic: { en: 'Chamomile (Matricaria chamomilla / Roman chamomile)', ko: '카모마일', ja: 'カモミール' },
    brands: ['Traditional Medicinals (tea)', 'Nature\'s Way', 'Gaia Herbs'],
    category: 'sleep',
    uses: [
      { title_en: 'Mild sleep and relaxation support', title_ko: '경미한 수면·이완 보조', title_ja: '軽度の睡眠·リラックスサポート',
        detail_en: 'Traditional herbal tea used for relaxation before bed; modest evidence for sleep quality, particularly in older adults and postpartum women',
        detail_ko: '취침 전 이완을 위해 전통적으로 사용되는 약용차; 노년층 및 산후 여성에서 수면 질에 대한 경미한 근거가 있음',
        detail_ja: '就寝前のリラックスに伝統的に使用される薬用茶;高齢者と産後女性で睡眠の質に対する軽度のエビデンスあり' },
      { title_en: 'Mild anxiety symptoms', title_ko: '경미한 불안 증상', title_ja: '軽度の不安症状',
        detail_en: 'Some evidence for modest reduction in generalized anxiety symptoms with standardized extract',
        detail_ko: '표준화 추출물로 범불안 증상이 약간 감소한다는 근거가 있음',
        detail_ja: '標準化抽出物で全般性不安症状がわずかに軽減するエビデンスあり' }
    ],
    dose_en: { 'Tea': '1–4 cups daily (1 tsp dried flowers per cup, steeped 5–10 min)', 'Extract (standardized)': '220–1500 mg daily in divided doses', 'Topical (skin irritation)': 'Creams containing 3–10% chamomile' },
    dose_ko: { '차': '하루 1~4잔 (컵당 건조 꽃 1티스푼, 5~10분 우림)', '표준화 추출물': '하루 220~1500 mg 분할 복용', '외용 (피부 자극)': '3~10% 카모마일 함유 크림' },
    dose_ja: { '茶': '1日1~4杯(カップあたり乾燥花小さじ1、5~10分浸出)', '標準化抽出物': '1日220~1500 mg分割服用', '外用(皮膚刺激)': '3~10%カモミール含有クリーム' },
    danger_en: 'Allergic reactions possible in people allergic to ragweed, chrysanthemums, marigolds, or daisies (Asteraceae family) — ranging from mild skin reaction to anaphylaxis.',
    danger_ko: '돼지풀, 국화, 금잔화, 데이지(국화과) 알레르기가 있는 사람에서 알레르기 반응 가능 — 경미한 피부 반응부터 아나필락시스까지 나타날 수 있습니다.',
    danger_ja: 'ブタクサ、菊、マリーゴールド、デイジー(キク科)アレルギーの人にアレルギー反応の可能性 — 軽度の皮膚反応からアナフィラキシーまで起こり得る。',
    warn_en: 'Not recommended in pregnancy (theoretical uterine stimulation). May interact with anticoagulants. Stop 2 weeks before surgery. Concentrated extracts more likely to cause interactions than occasional tea use.',
    warn_ko: '임신 중 권장되지 않습니다 (이론적 자궁 수축 가능성). 항응고제와 상호작용 가능. 수술 2주 전 중단하세요. 농축 추출물은 가끔 마시는 차보다 상호작용 가능성이 높습니다.',
    warn_ja: '妊娠中は推奨されません(理論的な子宮刺激の可能性)。抗凝固薬と相互作用の可能性。手術2週間前に中止。濃縮抽出物は時折の茶飲用より相互作用の可能性が高い。',
    interact: [
      { en: 'Warfarin and other anticoagulants — possible increased bleeding risk (contains coumarins)', ko: '와파린 및 기타 항응고제 — 쿠마린 함유로 출혈 위험 증가 가능', ja: 'ワーファリンおよび他の抗凝固薬 — クマリン含有で出血リスク増加の可能性' },
      { en: 'Cyclosporine — reduced cyclosporine levels reported', ko: '사이클로스포린 — 혈중 농도 감소 보고', ja: 'シクロスポリン — 血中濃度低下の報告' },
      { en: 'Sedatives and alcohol — mild additive calming effect', ko: '진정제 및 알코올 — 경미한 진정 작용 가중', ja: '鎮静薬およびアルコール — 軽度の鎮静作用累積' },
      { en: 'Tamoxifen and other CYP substrates — possible CYP enzyme interaction', ko: '타목시펜 및 기타 CYP 기질 — CYP 효소 상호작용 가능', ja: 'タモキシフェンおよび他のCYP基質 — CYP酵素相互作用の可能性' }
    ],
    source: 'NIH Office of Dietary Supplements · MedlinePlus'
  },

  // ============ WOMEN'S HEALTH ============
  {
    id: 'levonorgestrel-ec',
    generic: { en: 'Levonorgestrel 1.5 mg (emergency contraception)', ko: '레보노르게스트렐 1.5 mg (응급 피임)', ja: 'レボノルゲストレル1.5 mg(緊急避妊)' },
    brands: ['Plan B One-Step', 'Take Action', 'Next Choice One Dose', 'AfterPill'],
    category: 'womens',
    uses: [
      { title_en: 'Emergency contraception after unprotected sex', title_ko: '피임하지 않은 성관계 후 응급 피임', title_ja: '避妊なし性交後の緊急避妊',
        detail_en: 'Reduces the chance of pregnancy when taken as soon as possible after unprotected intercourse or contraceptive failure. Most effective within 72 hours; some benefit up to 120 hours (5 days) but efficacy declines sharply with time',
        detail_ko: '피임 없는 성관계 또는 피임 실패 후 가능한 빨리 복용하면 임신 가능성을 낮춤. 72시간 이내가 가장 효과적이며 120시간(5일)까지도 일부 효과가 있으나 시간 경과에 따라 효과가 급격히 감소',
        detail_ja: '避妊なしの性交または避妊失敗後できるだけ早く服用すると妊娠の可能性を低下。72時間以内が最も有効、120時間(5日)まで一部有効だが時間経過で効果急減' }
    ],
    dose_en: { 'Adult and adolescent of childbearing potential': 'One 1.5 mg tablet by mouth as soon as possible after unprotected sex', 'Timing': 'Within 72 hours (3 days); best within 12 hours', 'If vomiting within 2 hours': 'Contact a pharmacist or doctor — a repeat dose may be needed' },
    dose_ko: { '가임기 성인·청소년': '피임하지 않은 성관계 후 가능한 빨리 1.5 mg 1정 경구 복용', '복용 시점': '72시간(3일) 이내; 12시간 이내가 최선', '복용 후 2시간 이내 구토 시': '약사 또는 의사에게 연락 — 재투여가 필요할 수 있음' },
    dose_ja: { '生殖年齢の成人·青少年': '避妊なし性交後できるだけ早く1.5 mg 1錠経口服用', '服用時期': '72時間(3日)以内;12時間以内が最良', '服用後2時間以内に嘔吐した場合': '薬剤師または医師に連絡 — 再投与が必要な場合あり' },
    danger_en: 'DOES NOT TERMINATE AN EXISTING PREGNANCY — it works by delaying ovulation and will not work if ovulation has already occurred. Not effective as routine contraception. Reduced efficacy in women weighing over 165 lb (75 kg); women over 176 lb (80 kg) should consider ulipristal (Ella, prescription) or a copper IUD instead. Does NOT protect against sexually transmitted infections.',
    danger_ko: '이미 진행 중인 임신을 중단시키지 않습니다 — 배란을 지연시키는 방식으로 작용하며 이미 배란이 일어났다면 효과가 없습니다. 일반적인 피임법으로 사용할 수 없습니다. 체중 75 kg(165 lb) 이상 여성에서 효과가 감소하며, 80 kg(176 lb) 이상이면 울리프리스탈(Ella, 처방) 또는 구리 IUD 고려. 성매개감염병(STI)은 예방하지 않습니다.',
    danger_ja: '既存の妊娠を中絶しません — 排卵を遅らせる作用で、すでに排卵が起こった場合は効果なし。日常的避妊法として使用不可。体重75 kg(165 lb)超の女性で効果減少、80 kg(176 lb)超ではウリプリスタル(Ella、処方)または銅IUDを検討。性感染症(STI)は予防しません。',
    warn_en: 'Available OTC without age restriction in the U.S. Side effects: nausea, abdominal pain, fatigue, headache, heavier or irregular menstrual bleeding in the following cycle. If your next period is more than 1 week late, take a pregnancy test. Seek medical care for severe abdominal pain 3–5 weeks after use (possible ectopic pregnancy).',
    warn_ko: '미국에서는 나이 제한 없이 OTC 구매 가능. 부작용: 메스꺼움, 복통, 피로, 두통, 다음 생리 주기의 출혈량 증가 또는 불규칙. 다음 생리가 1주일 이상 늦어지면 임신 테스트. 복용 후 3~5주 내 심한 복통이 있으면 진료(자궁외임신 가능성).',
    warn_ja: '米国では年齢制限なくOTCで購入可能。副作用:吐き気、腹痛、疲労、頭痛、次の月経周期の出血量増加または不規則。次の月経が1週間以上遅れたら妊娠検査。服用後3~5週間以内に激しい腹痛があれば受診(子宮外妊娠の可能性)。',
    interact: [
      { en: 'CYP3A4 inducers (rifampin, phenytoin, carbamazepine, St. John\'s wort, HIV drugs such as efavirenz) — may reduce effectiveness; consider copper IUD or ulipristal', ko: 'CYP3A4 유도제 (리팜핀, 페니토인, 카바마제핀, 세인트존스워트, 에파비렌츠 등 HIV 약물) — 효과 감소 가능; 구리 IUD 또는 울리프리스탈 고려', ja: 'CYP3A4誘導薬(リファンピン、フェニトイン、カルバマゼピン、セントジョーンズワート、エファビレンツなどのHIV薬) — 効果減少の可能性;銅IUDまたはウリプリスタルを検討' },
      { en: 'Ulipristal (Ella) taken in the same cycle — do not combine; they can reduce each other\'s effectiveness', ko: '같은 주기에 울리프리스탈 (Ella) 복용 — 병용 금지; 서로 효과 감소 가능', ja: '同じ周期にウリプリスタル(Ella)服用 — 併用禁止;互いの効果を減少させる可能性' },
      { en: 'Hormonal contraceptives — resume or start regular method after EC; no interaction but EC does not continue protection', ko: '호르몬 피임제 — 응급 피임 후 정규 피임법 재개/시작; 상호작용은 없으나 응급 피임은 지속 효과 없음', ja: 'ホルモン避妊薬 — 緊急避妊後に通常の避妊法を再開·開始;相互作用はないが緊急避妊は継続効果なし' }
    ],
    source: 'FDA-approved labeling · ACOG Practice Bulletin · DailyMed (NIH)'
  },
  {
    id: 'phenazopyridine',
    generic: { en: 'Phenazopyridine HCl (urinary analgesic)', ko: '페나조피리딘 (요로 진통제)', ja: 'フェナゾピリジン(尿路鎮痛薬)' },
    brands: ['Azo Urinary Pain Relief', 'Uristat', 'AZO Standard'],
    category: 'womens',
    uses: [
      { title_en: 'Urinary tract pain, burning, urgency', title_ko: '요로 통증·작열감·급박뇨', title_ja: '尿路の痛み·灼熱感·尿意切迫',
        detail_en: 'Local anesthetic effect on the lining of the urinary tract; provides symptomatic relief from the burning, pain, and urgency of urinary tract infection or urethral irritation. Does NOT treat the underlying infection',
        detail_ko: '요로 점막에 대한 국소 마취 작용; 요로감염이나 요도 자극으로 인한 작열감, 통증, 급박뇨를 일시적으로 완화. 감염 자체를 치료하지 않음',
        detail_ja: '尿路粘膜への局所麻酔作用;尿路感染や尿道刺激による灼熱感、痛み、尿意切迫を一時的に緩和。感染自体は治療しない' }
    ],
    dose_en: { 'Adult': '95 mg (OTC) or 190 mg three times daily after meals', 'Max duration (OTC)': '2 days — see a doctor if symptoms persist; a urine culture and antibiotics are usually needed', 'Take with': 'Food to reduce stomach upset' },
    dose_ko: { '성인': '식후 하루 3회 95 mg(OTC) 또는 190 mg', '자가 치료 최대 기간': '2일 — 증상 지속 시 진료; 소변 배양과 항생제가 보통 필요', '복용 방법': '위장 장애 완화를 위해 음식과 함께' },
    dose_ja: { '成人': '食後1日3回95 mg(OTC)または190 mg', '自己治療最大期間': '2日 — 症状が続く場合は受診;通常は尿培養と抗生物質が必要', '服用方法': '胃腸障害軽減のため食事と一緒に' },
    danger_en: 'DOES NOT CURE UTI — it only relieves symptoms. You still need a urine test and antibiotics from a doctor. Untreated UTI can spread to kidneys (pyelonephritis) and cause sepsis. Causes bright orange-red urine, tears, sweat — can permanently stain contact lenses and fabrics.',
    danger_ko: '요로감염을 치료하지 않습니다 — 증상만 완화합니다. 의사의 소변 검사와 항생제가 필요합니다. 치료하지 않은 요로감염은 신장으로 번져(신우신염) 패혈증을 유발할 수 있습니다. 소변·눈물·땀이 선명한 주황~빨간색으로 변하며 콘택트렌즈와 옷감에 영구적인 얼룩을 남길 수 있습니다.',
    danger_ja: '尿路感染を治療しません — 症状のみ緩和。医師の尿検査と抗生物質が必要です。未治療の尿路感染は腎臓に広がり(腎盂腎炎)敗血症を起こす可能性。尿·涙·汗が鮮やかなオレンジ~赤色になり、コンタクトレンズや衣類に永久的な染みを残す可能性。',
    warn_en: 'Do not use if you have G6PD deficiency (risk of hemolytic anemia), severe kidney or liver disease. Contraindicated in infants under 6 months. May interfere with urine glucose and ketone test strips. Stop 24 hours before any urine test.',
    warn_ko: 'G6PD 결핍(용혈성 빈혈 위험), 중증 신·간 질환이 있으면 사용하지 마세요. 6개월 미만 영아 금기. 소변 포도당·케톤 검사지에 영향을 줄 수 있습니다. 소변 검사 24시간 전에는 중단하세요.',
    warn_ja: 'G6PD欠損症(溶血性貧血リスク)、重度腎·肝疾患がある場合は使用禁止。6か月未満の乳児は禁忌。尿糖·ケトン試験紙に影響する可能性。尿検査の24時間前には中止。',
    interact: [
      { en: 'Other urinary analgesics or antispasmodics (methenamine, hyoscyamine) — additive anticholinergic effects', ko: '기타 요로 진통제·진경제 (메테나민, 하이오스시아민) — 항콜린 작용 가중', ja: '他の尿路鎮痛薬·鎮痙薬(メテナミン、ヒオスシアミン) — 抗コリン作用の累積' },
      { en: 'Urinalysis / urine dipstick tests — causes false results for protein, glucose, ketones, bilirubin', ko: '소변 검사 / 요시험지 — 단백, 포도당, 케톤, 빌리루빈 거짓 결과 유발', ja: '尿検査/尿試験紙 — タンパク、ブドウ糖、ケトン、ビリルビンの偽結果を引き起こす' },
      { en: 'Sulfonamide antibiotics — both can cause methemoglobinemia; caution', ko: '설폰아미드계 항생제 — 양쪽 모두 메트헤모글로빈혈증 유발 가능; 주의', ja: 'スルホンアミド系抗生物質 — 両方ともメトヘモグロビン血症を起こす可能性;注意' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'cranberry',
    generic: { en: 'Cranberry extract (Vaccinium macrocarpon)', ko: '크랜베리 추출물', ja: 'クランベリー抽出物' },
    brands: ['Azo Cranberry', 'Nature Made Cranberry', 'Ellura (high PAC)', 'TheraCran'],
    category: 'womens',
    uses: [
      { title_en: 'Recurrent UTI prevention (not treatment)', title_ko: '재발성 요로감염 예방 (치료 아님)', title_ja: '再発性尿路感染症予防(治療ではない)',
        detail_en: 'Proanthocyanidins (PACs) in cranberry may prevent E. coli from adhering to the bladder wall; 2023 Cochrane review found modest benefit for reducing UTI recurrence in women with repeated infections. Does NOT treat an active UTI',
        detail_ko: '크랜베리의 프로안토시아니딘(PAC)이 대장균의 방광벽 부착을 방해할 수 있음; 2023년 Cochrane 리뷰에서 재발성 요로감염 여성에서 재발 감소에 경미한 효과. 진행 중인 감염은 치료하지 않음',
        detail_ja: 'クランベリーのプロアントシアニジン(PAC)が大腸菌の膀胱壁付着を阻害する可能性;2023年Cochraneレビューで再発性尿路感染女性で再発減少に軽度の効果。進行中の感染は治療しない' }
    ],
    dose_en: { 'PAC-standardized extract': '36–72 mg of type-A PACs daily (most evidence-based)', 'Juice': '240–300 mL (8–10 oz) unsweetened cranberry juice daily', 'Capsules (typical)': '500–1500 mg cranberry extract twice daily', 'Duration': 'Continuous daily use for prevention; benefit seen over months' },
    dose_ko: { 'PAC 표준화 추출물': '하루 A형 PAC 36~72 mg (근거가 가장 확실)', '주스': '무가당 크랜베리 주스 하루 240~300 mL (8~10 oz)', '캡슐 (일반)': '하루 2회 500~1500 mg 크랜베리 추출물', '복용 기간': '예방 목적으로 매일 지속 복용; 수개월에 걸쳐 효과 확인' },
    dose_ja: { 'PAC標準化抽出物': '1日A型PAC 36~72 mg(最もエビデンス確実)', 'ジュース': '無糖クランベリージュース1日240~300 mL', 'カプセル(一般)': '1日2回500~1500 mgクランベリー抽出物', '服用期間': '予防目的で毎日継続服用;数か月かけて効果確認' },
    danger_en: 'NOT A TREATMENT for active UTI. If you have burning, fever, flank pain, or blood in urine, see a doctor for antibiotics. Cranberry products vary enormously in PAC content — sweetened juice cocktails often contain negligible amounts.',
    danger_ko: '진행 중인 요로감염의 치료제가 아닙니다. 작열감, 발열, 옆구리 통증, 혈뇨가 있으면 의사에게 항생제 처방을 받으세요. 제품별 PAC 함량 차이가 매우 크며, 가당 주스 칵테일에는 유효 성분이 거의 없는 경우가 많습니다.',
    danger_ja: '進行中の尿路感染の治療薬ではありません。灼熱感、発熱、側腹部痛、血尿がある場合は医師から抗生物質処方を受けてください。製品ごとのPAC含有量差が非常に大きく、加糖ジュースカクテルには有効成分がほとんど含まれない場合が多い。',
    warn_en: 'Can increase kidney stone risk in people prone to oxalate stones (cranberry is high in oxalate). Not a substitute for antibiotics during pregnancy UTI. Tablets can cause mild GI upset.',
    warn_ko: '옥살산 신장결석이 잘 생기는 사람에서 결석 위험 증가(크랜베리는 옥살산 함량 높음). 임신 중 요로감염에서 항생제를 대체할 수 없습니다. 정제는 경미한 위장 장애를 유발할 수 있습니다.',
    warn_ja: 'シュウ酸腎結石ができやすい人で結石リスク増加(クランベリーはシュウ酸高含有)。妊娠中の尿路感染で抗生物質を代替できません。錠剤は軽度の胃腸障害を起こす可能性。',
    interact: [
      { en: 'Warfarin — case reports of increased INR; monitor if combining regularly', ko: '와파린 — 정기 병용 시 INR 증가 사례 보고; 모니터링 필요', ja: 'ワーファリン — 定期併用でINR増加の症例報告;モニタリング必要' },
      { en: 'Aspirin allergy — cranberry contains salicylates; caution in severe sensitivity', ko: '아스피린 알레르기 — 크랜베리에 살리실산염 함유; 중증 과민성 환자는 주의', ja: 'アスピリンアレルギー — クランベリーにサリチル酸塩含有;重度過敏症の患者は注意' },
      { en: 'Proton pump inhibitors — theoretical reduction of B12 absorption worsened by cranberry; minor', ko: '양성자 펌프 억제제 — B12 흡수 감소가 이론적으로 악화될 수 있음; 경미', ja: 'プロトンポンプ阻害薬 — B12吸収減少が理論的に悪化する可能性;軽微' }
    ],
    source: 'NIH Office of Dietary Supplements · Cochrane Review 2023 · MedlinePlus'
  },
  {
    id: 'vaginal-moisturizer',
    generic: { en: 'Vaginal moisturizer / lubricant (non-hormonal)', ko: '질 보습제·윤활제 (비호르몬)', ja: '腟保湿剤·潤滑剤(非ホルモン)' },
    brands: ['Replens (long-acting moisturizer)', 'RepHresh (pH-balancing gel)', 'K-Y Liquibeads', 'Hyalofemme'],
    category: 'womens',
    uses: [
      { title_en: 'Vaginal dryness symptom relief', title_ko: '질 건조감 완화', title_ja: '腟乾燥症状の緩和',
        detail_en: 'Non-hormonal water-, silicone-, or hyaluronic-acid-based products that restore moisture to the vaginal tissue; useful for mild menopausal dryness, post-partum, or medication-induced dryness',
        detail_ko: '수성, 실리콘, 또는 히알루론산 기반 비호르몬 제품으로 질 조직에 수분을 공급; 경미한 폐경기 건조감, 산후, 약물 유발 건조감에 사용',
        detail_ja: '水性、シリコン、またはヒアルロン酸ベースの非ホルモン製品で腟組織に水分を補給;軽度の閉経期乾燥、産後、薬剤誘発性乾燥に使用' },
      { title_en: 'Painful intercourse (mild)', title_ko: '성교통 (경미)', title_ja: '性交痛(軽度)',
        detail_en: 'Water- or silicone-based lubricants reduce friction during intercourse when dryness is a factor',
        detail_ko: '수성 또는 실리콘 기반 윤활제로 건조감이 원인인 성교 시 마찰 감소',
        detail_ja: '水性またはシリコンベースの潤滑剤で乾燥が原因の性交時の摩擦を軽減' }
    ],
    dose_en: { 'Long-acting moisturizer (Replens)': '1 applicator inserted vaginally every 3 days', 'pH-balancing gel (RepHresh)': '1 applicator every 3 days to maintain acidic pH', 'Lubricant': 'Apply as needed before or during intercourse', 'Avoid with latex condoms': 'Do not use oil-based or petroleum products — degrade latex' },
    dose_ko: { '장시간 보습제 (Replens)': '질 내 어플리케이터 1개 3일마다 삽입', 'pH 조절 젤 (RepHresh)': '어플리케이터 1개 3일마다 삽입하여 산성 pH 유지', '윤활제': '성관계 전·중 필요시 사용', '라텍스 콘돔과 주의': '오일·바세린 제품 사용 금지 — 라텍스 손상' },
    dose_ja: { '長時間保湿剤(Replens)': '腟内アプリケーター1個を3日ごとに挿入', 'pH調節ゲル(RepHresh)': 'アプリケーター1個を3日ごとに挿入し酸性pHを維持', '潤滑剤': '性交前·中に必要に応じて使用', 'ラテックスコンドーム注意': 'オイル·ワセリン製品使用禁止 — ラテックス損傷' },
    warn_en: 'If dryness is severe, painful, or accompanied by bleeding, burning, or unusual discharge, see a doctor — may need prescription topical estrogen or evaluation for infection (yeast, bacterial vaginosis). Avoid products with parabens, glycerin (can worsen yeast infections in susceptible women), or warming/tingling additives.',
    warn_ko: '건조감이 심하거나 통증, 출혈, 작열감, 비정상 분비물을 동반하면 진료 — 처방 국소 에스트로겐이 필요하거나 감염(칸디다, 세균성 질증) 평가가 필요할 수 있습니다. 파라벤, 글리세린(일부 여성에서 칸디다 악화), 온열·자극 첨가제 함유 제품은 피하세요.',
    warn_ja: '乾燥が重度、痛みを伴う、または出血·灼熱感·異常分泌物を伴う場合は受診 — 処方外用エストロゲンが必要または感染(カンジダ、細菌性腟症)評価が必要な場合あり。パラベン、グリセリン(感受性女性でカンジダ悪化)、温感·刺激添加物含有製品は回避。',
    interact: [
      { en: 'Latex condoms — use only water- or silicone-based products; oil-based products destroy latex', ko: '라텍스 콘돔 — 수성 또는 실리콘 기반만 사용; 오일 기반은 라텍스 파괴', ja: 'ラテックスコンドーム — 水性またはシリコンベースのみ使用;オイルベースはラテックス破壊' },
      { en: 'Silicone sex toys — silicone lubricants can degrade silicone toys; use water-based with silicone toys', ko: '실리콘 성기구 — 실리콘 윤활제는 실리콘 제품 손상 가능; 수성 윤활제 사용', ja: 'シリコン製性具 — シリコン潤滑剤はシリコン製品を損傷の可能性;水性を使用' },
      { en: 'Spermicide — some moisturizers are not compatible; check labels if pregnancy prevention matters', ko: '살정제 — 일부 보습제와 비호환; 피임 고려 시 라벨 확인', ja: '殺精子剤 — 一部の保湿剤と非互換;避妊考慮時はラベル確認' }
    ],
    source: 'ACOG Committee Opinion · FDA device labeling · MedlinePlus'
  },
  {
    id: 'prenatal-multivitamin',
    generic: { en: 'Prenatal multivitamin (with folic acid, iron, DHA)', ko: '임산부 종합 비타민 (엽산·철분·DHA 포함)', ja: '妊婦用マルチビタミン(葉酸·鉄·DHA含有)' },
    brands: ['One A Day Prenatal', 'Nature Made Prenatal', 'Rainbow Light Prenatal One', 'Ritual Essential Prenatal'],
    category: 'womens',
    uses: [
      { title_en: 'Preconception and pregnancy nutritional support', title_ko: '임신 준비 및 임신 중 영양 보충', title_ja: '妊娠前·妊娠中の栄養補給',
        detail_en: 'Folic acid (400–800 mcg) reduces risk of neural tube defects by ~70% when started 1 month before conception and continued through the first trimester. Iron prevents iron-deficiency anemia. DHA supports fetal brain and eye development',
        detail_ko: '엽산(400~800 mcg)은 임신 1개월 전부터 복용 시 첫 3개월간 신경관 결손 위험을 약 70% 낮춤. 철분은 철결핍성 빈혈 예방. DHA는 태아 뇌·안구 발달 지원',
        detail_ja: '葉酸(400~800 mcg)は妊娠1か月前から服用すると最初の3か月間の神経管欠損リスクを約70%低減。鉄は鉄欠乏性貧血を予防。DHAは胎児の脳·眼の発達を支援' },
      { title_en: 'Breastfeeding nutritional support', title_ko: '수유 중 영양 보충', title_ja: '授乳中の栄養補給',
        detail_en: 'Continued use during lactation supports maternal nutrient stores and milk composition',
        detail_ko: '수유 중 지속 복용은 산모 영양 저장과 모유 성분을 지원',
        detail_ja: '授乳中の継続使用は母体の栄養貯蔵と母乳成分を支援' }
    ],
    dose_en: { 'Standard': '1 tablet or softgel daily with food', 'Folic acid (key ingredient)': '400–800 mcg daily; women with prior neural tube defect pregnancy need 4 mg (prescription)', 'Iron': 'Typically 27 mg — take with vitamin C to enhance absorption, avoid with calcium or coffee (reduced absorption)', 'DHA (if separate)': '200 mg daily recommended in pregnancy' },
    dose_ko: { '표준': '하루 1정 또는 1캡슐 식사와 함께', '엽산 (핵심 성분)': '하루 400~800 mcg; 이전 임신에서 신경관 결손이 있었던 여성은 4 mg(처방) 필요', '철분': '보통 27 mg — 비타민 C와 함께 흡수 촉진, 칼슘·커피와 병용 피함(흡수 감소)', 'DHA (별도 복용 시)': '임신 중 하루 200 mg 권장' },
    dose_ja: { '標準': '1日1錠またはソフトジェル、食事と一緒に', '葉酸(主要成分)': '1日400~800 mcg;前回妊娠で神経管欠損があった女性は4 mg(処方)必要', '鉄': '通常27 mg — ビタミンCと一緒に吸収促進、カルシウム·コーヒーとの併用回避(吸収減少)', 'DHA(別途服用時)': '妊娠中1日200 mg推奨' },
    danger_en: 'IRON OVERDOSE IS THE #1 CAUSE OF FATAL POISONING IN U.S. CHILDREN — keep tightly capped and out of reach; as few as 5 adult tablets can be fatal to a toddler. Do not take extra iron beyond prenatal content without a blood test (ferritin) — excess iron causes liver damage and in 1/200 Koreans with hemochromatosis is dangerous.',
    danger_ko: '철분 과량 복용은 미국 소아 치명적 중독의 1위 원인 — 밀봉하여 소아 손이 닿지 않게 보관; 성인용 5정만으로도 유아가 사망 가능. 혈액검사(페리틴) 없이 임산부 비타민 외 추가 철분 복용 금지 — 과잉 철분은 간 손상을 유발하며 한국인 200명 중 1명은 혈색소증으로 매우 위험.',
    danger_ja: '鉄過剰摂取は米国小児致命的中毒の第1位原因 — 密閉し小児の手の届かない場所に保管;成人用5錠で幼児が死亡する可能性。血液検査(フェリチン)なく妊婦用ビタミン以外の追加鉄剤服用禁止 — 過剰鉄は肝障害を起こし、ヘモクロマトーシス患者(東アジア人で稀)では非常に危険。',
    warn_en: 'Common side effects: nausea (take at night or with meals), constipation (increase fiber/water, or switch to slow-release iron form), dark/black stools (harmless from iron). If persistent vomiting, switch formulation. Women >35 or with prior gestational diabetes: discuss specific nutrient needs with obstetrician.',
    warn_ko: '흔한 부작용: 메스꺼움(취침 전 또는 식사와 함께 복용), 변비(섬유질·수분 증가, 또는 서방형 철분 제형으로 변경), 짙은·검은 변(철분에 의한 무해한 변화). 지속적인 구토 시 제형 변경. 35세 이상 또는 임신성 당뇨 병력 여성: 특정 영양소 요구량에 대해 산부인과 의사와 상담.',
    warn_ja: '一般的副作用:吐き気(就寝前または食事と一緒に服用)、便秘(食物繊維·水分増加、または徐放性鉄剤に変更)、濃い·黒い便(鉄による無害な変化)。持続性嘔吐時は剤形変更。35歳超または妊娠糖尿病既往の女性:特定の栄養素必要量について産科医に相談。',
    interact: [
      { en: 'Thyroid medications (levothyroxine) — iron and calcium reduce absorption; separate by 4 hours', ko: '갑상선 약 (레보티록신) — 철분·칼슘이 흡수 감소시킴; 4시간 간격', ja: '甲状腺薬(レボチロキシン) — 鉄·カルシウムが吸収減少;4時間間隔' },
      { en: 'Tetracycline and fluoroquinolone antibiotics — iron and calcium reduce absorption; separate by 2 hours', ko: '테트라사이클린·플루오로퀴놀론 항생제 — 철분·칼슘이 흡수 감소시킴; 2시간 간격', ja: 'テトラサイクリン·フルオロキノロン抗生物質 — 鉄·カルシウムが吸収減少;2時間間隔' },
      { en: 'Antacids, PPIs, H2 blockers — reduced iron absorption; take iron with vitamin C between doses', ko: '제산제, PPI, H2 차단제 — 철분 흡수 감소; 철분은 용량 사이 비타민 C와 함께 복용', ja: '制酸薬、PPI、H2ブロッカー — 鉄吸収減少;鉄は服用間にビタミンCと一緒に' },
      { en: 'Methotrexate — prenatals can contain folic acid that reduces drug effect; discuss with oncologist/rheumatologist if applicable', ko: '메토트렉세이트 — 임산부 비타민의 엽산이 약효 감소; 해당 시 종양내과·류마티스내과 상담', ja: 'メトトレキサート — 妊婦用ビタミンの葉酸が薬効を減少;該当時は腫瘍·リウマチ内科に相談' }
    ],
    source: 'ACOG · CDC Folic Acid Recommendations · NIH ODS'
  },
  {
    id: 'midol-complete',
    generic: { en: 'Acetaminophen + Caffeine + Pyrilamine (menstrual combination)', ko: '아세트아미노펜 + 카페인 + 피릴아민 (생리통 복합제)', ja: 'アセトアミノフェン + カフェイン + ピリラミン(月経痛複合薬)' },
    brands: ['Midol Complete', 'Pamprin Multi-Symptom', 'Premsyn PMS'],
    category: 'womens',
    uses: [
      { title_en: 'Menstrual cramps and body aches', title_ko: '생리통 및 근육통', title_ja: '月経痛と全身痛',
        detail_en: 'Acetaminophen 500 mg provides analgesia; caffeine 60 mg may enhance acetaminophen effect and reduce menstrual-related fatigue; pyrilamine 15 mg (antihistamine) reduces water retention and bloating',
        detail_ko: '아세트아미노펜 500 mg이 진통 작용; 카페인 60 mg이 아세트아미노펜 효과를 증강하고 생리 관련 피로를 감소; 피릴아민 15 mg (항히스타민)이 수분 정체와 부기를 감소',
        detail_ja: 'アセトアミノフェン500 mgが鎮痛作用;カフェイン60 mgがアセトアミノフェン効果を増強し月経関連疲労を軽減;ピリラミン15 mg(抗ヒスタミン薬)が水分貯留と腫れを軽減' },
      { title_en: 'Bloating and fluid retention', title_ko: '붓기 및 수분 정체', title_ja: '腫れと水分貯留',
        detail_en: 'Pyrilamine has mild diuretic effect; relief of breast tenderness and abdominal bloating',
        detail_ko: '피릴아민의 경미한 이뇨 작용; 유방 압통과 복부 부기 완화',
        detail_ja: 'ピリラミンの軽度利尿作用;乳房圧痛と腹部膨満を緩和' }
    ],
    dose_en: { 'Adult and child 12+': '2 caplets every 6 hours with water', 'Max per day': '6 caplets (contains 1500 mg acetaminophen)', 'Other acetaminophen products': 'Do not combine — total daily acetaminophen from all sources must stay under 3000 mg' },
    dose_ko: { '성인 및 12세 이상': '6시간마다 2정을 물과 함께', '하루 최대': '6정 (아세트아미노펜 1500 mg 함유)', '기타 아세트아미노펜 제품': '병용 금지 — 모든 제품의 하루 총 아세트아미노펜은 3000 mg 미만 유지' },
    dose_ja: { '成人および12歳以上': '6時間ごとに2錠を水と一緒に', '1日最大量': '6錠(アセトアミノフェン1500 mg含有)', '他のアセトアミノフェン製品': '併用禁止 — すべての製品の1日総アセトアミノフェンは3000 mg未満に維持' },
    danger_en: 'ACETAMINOPHEN LIVER INJURY RISK — many cold/flu/pain products also contain acetaminophen; check all labels. Pyrilamine is a first-generation antihistamine causing drowsiness — do not drive or operate machinery. Caffeine can worsen anxiety, insomnia, or palpitations.',
    danger_ko: '아세트아미노펜 간 손상 위험 — 많은 감기·독감·진통제에도 아세트아미노펜 함유; 모든 라벨 확인. 피릴아민은 1세대 항히스타민으로 졸음 유발 — 운전·기계 조작 금지. 카페인은 불안, 불면, 심계항진을 악화시킬 수 있습니다.',
    danger_ja: 'アセトアミノフェン肝障害リスク — 多くの風邪·インフルエンザ·鎮痛薬にもアセトアミノフェン含有;すべてのラベル確認。ピリラミンは第一世代抗ヒスタミン薬で眠気を起こす — 運転·機械操作禁止。カフェインは不安、不眠、動悸を悪化させる可能性。',
    warn_en: 'Avoid in liver disease, heavy alcohol use (≥3 drinks/day), glaucoma, enlarged prostate, asthma. May cause constipation or dry mouth from the antihistamine. Severe menstrual pain not relieved by OTC products warrants evaluation for endometriosis or fibroids.',
    warn_ko: '간 질환, 과음(하루 3잔 이상), 녹내장, 전립선 비대, 천식 시 사용 피하세요. 항히스타민으로 인한 변비·구갈 가능. OTC로 완화되지 않는 심한 생리통은 자궁내막증·자궁근종 평가 필요.',
    warn_ja: '肝疾患、過度の飲酒(1日3杯以上)、緑内障、前立腺肥大、喘息時は使用回避。抗ヒスタミン薬による便秘·口渇の可能性。OTCで緩和されない重度の月経痛は子宮内膜症·子宮筋腫の評価が必要。',
    interact: [
      { en: 'Alcohol — compounds liver risk from acetaminophen', ko: '알코올 — 아세트아미노펜의 간 위험 가중', ja: 'アルコール — アセトアミノフェンによる肝リスクの累積' },
      { en: 'Other sedating antihistamines, benzodiazepines, opioids — additive drowsiness', ko: '기타 진정성 항히스타민, 벤조디아제핀, 오피오이드 — 졸음 가중', ja: '他の鎮静性抗ヒスタミン薬、ベンゾジアゼピン、オピオイド — 眠気の累積' },
      { en: 'MAO inhibitors — avoid; pyrilamine interaction possible', ko: 'MAO 억제제 — 피하세요; 피릴아민 상호작용 가능', ja: 'MAO阻害薬 — 回避;ピリラミン相互作用の可能性' },
      { en: 'Warfarin — acetaminophen may increase INR with prolonged use', ko: '와파린 — 장기 복용 시 아세트아미노펜이 INR 증가 가능', ja: 'ワーファリン — 長期服用でアセトアミノフェンがINR増加の可能性' },
      { en: 'Stimulants, other caffeine sources — jitteriness, insomnia', ko: '자극제, 기타 카페인 공급원 — 각성 불안, 불면', ja: '覚醒剤、他のカフェイン源 — ジリジリ感、不眠' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'boric-acid-vaginal',
    generic: { en: 'Boric acid vaginal suppositories (600 mg)', ko: '붕산 질 좌제 (600 mg)', ja: 'ホウ酸腟坐薬(600 mg)' },
    brands: ['NutraBlast', 'The Honey Pot', 'pH-D', 'Love Wellness The Killer'],
    category: 'womens',
    uses: [
      { title_en: 'Recurrent or resistant yeast infections', title_ko: '재발성·내성 칸디다 질염', title_ja: '再発性·耐性カンジダ腟炎',
        detail_en: 'Second-line option recommended by CDC and ACOG for recurrent vulvovaginal candidiasis or infections caused by non-albicans Candida species (e.g., C. glabrata) that resist fluconazole and miconazole',
        detail_ko: 'CDC와 ACOG가 재발성 외음부질 칸디다증 또는 플루코나졸·미코나졸에 저항성인 비알비칸스 칸디다(예: C. glabrata)에 2차 선택으로 권장',
        detail_ja: 'CDCとACOGが再発性外陰腟カンジダ症またはフルコナゾール·ミコナゾール耐性の非アルビカンスカンジダ(例:C. glabrata)に第二選択として推奨' },
      { title_en: 'Recurrent bacterial vaginosis (adjunct)', title_ko: '재발성 세균성 질증 (보조)', title_ja: '再発性細菌性腟症(補助)',
        detail_en: 'Sometimes used after antibiotic treatment (metronidazole or clindamycin) to reduce recurrence by lowering vaginal pH',
        detail_ko: '항생제 치료(메트로니다졸·클린다마이신) 후 질 내 pH 감소를 통해 재발을 줄이는 보조 요법으로 사용되기도 함',
        detail_ja: '抗生物質治療(メトロニダゾール·クリンダマイシン)後に腟内pH低下による再発減少の補助療法として使用されることあり' }
    ],
    dose_en: { 'Yeast (non-albicans or resistant)': '600 mg intravaginally at bedtime for 14 days', 'Recurrent BV prevention': '600 mg intravaginally for 21 days after antibiotic, or 2x/week maintenance', 'Avoid during menses': 'Use during menstrual flow is not recommended' },
    dose_ko: { '칸디다 (비알비칸스 또는 내성)': '취침 시 600 mg 질 내 14일간', '재발성 세균성 질증 예방': '항생제 후 600 mg 질 내 21일, 또는 주 2회 유지', '월경 중 사용 금지': '월경 중에는 사용하지 마세요' },
    dose_ja: { 'カンジダ(非アルビカンスまたは耐性)': '就寝時に600 mg腟内、14日間', '再発性細菌性腟症予防': '抗生物質後600 mg腟内21日、または週2回維持', '月経中使用禁止': '月経中の使用は推奨されません' },
    danger_en: 'ORAL INGESTION IS TOXIC AND CAN BE FATAL — especially to children and pregnant women. Keep suppositories away from oral use and out of reach of children. FATAL IN PREGNANCY — boric acid is absorbed through vaginal mucosa and is teratogenic; CONTRAINDICATED in pregnancy. Not for use if you are pregnant or trying to conceive.',
    danger_ko: '경구 섭취 시 독성이 있으며 치명적일 수 있습니다 — 특히 소아·임산부. 좌제를 경구용으로 사용하지 말고 소아 손이 닿지 않게 보관하세요. 임신 중 치명적 — 붕산은 질 점막으로 흡수되며 기형 유발; 임신 중 금기. 임신했거나 임신 시도 중이면 사용 금지.',
    danger_ja: '経口摂取で毒性があり致命的になる可能性 — 特に小児·妊婦。坐薬を経口使用せず小児の手の届かない場所に保管。妊娠中致命的 — ホウ酸は腟粘膜から吸収され催奇形性;妊娠中禁忌。妊娠中または妊娠を試みている場合は使用禁止。',
    warn_en: 'Stop if burning, irritation, redness, or unusual discharge worsens. Not for use on broken or inflamed vaginal tissue. Not effective as primary treatment for first-episode yeast infection (use miconazole/clotrimazole). Do not use in children. See a doctor before first use to confirm diagnosis — symptoms of yeast infection, BV, trichomoniasis, and STIs overlap significantly.',
    warn_ko: '작열감, 자극, 발적, 이상 분비물이 악화되면 중단하세요. 손상되거나 염증이 있는 질 조직에 사용하지 마세요. 첫 칸디다 질염의 1차 치료로 효과 없음(미코나졸·클로트리마졸 사용). 소아에 사용 금지. 처음 사용 전 진단 확인을 위해 진료 — 칸디다, 세균성 질증, 트리코모나스, 성매개감염의 증상이 상당히 겹칩니다.',
    warn_ja: '灼熱感、刺激、発赤、異常分泌物が悪化したら中止。損傷または炎症のある腟組織には使用禁止。初回カンジダ腟炎の第一選択治療には無効(ミコナゾール·クロトリマゾールを使用)。小児に使用禁止。初回使用前に診断確認のため受診 — カンジダ、細菌性腟症、トリコモナス、性感染症の症状は大きく重複。',
    interact: [
      { en: 'Latex condoms and diaphragms — boric acid suppositories may weaken latex; use alternative contraception during treatment', ko: '라텍스 콘돔·다이어프램 — 붕산 좌제가 라텍스 약화 가능; 치료 기간 대체 피임', ja: 'ラテックスコンドーム·ダイアフラム — ホウ酸坐薬がラテックスを弱める可能性;治療期間中は代替避妊' },
      { en: 'Other vaginal medications (miconazole, metronidazole gel) — do not combine in the same day unless directed by a clinician', ko: '기타 질 내 약물 (미코나졸, 메트로니다졸 젤) — 임상의 지시가 없는 한 같은 날 병용 금지', ja: '他の腟内薬(ミコナゾール、メトロニダゾールゲル) — 臨床医の指示なく同日併用禁止' },
      { en: 'Anticoagulants — theoretical minor bleeding risk from mucosal irritation', ko: '항응고제 — 점막 자극으로 인한 이론적 경미한 출혈 위험', ja: '抗凝固薬 — 粘膜刺激による理論的軽度出血リスク' }
    ],
    source: 'CDC STI Treatment Guidelines · ACOG Practice Bulletin on Vaginitis · NIH MedlinePlus'
  },

  // ============ PEDIATRIC ============
  {
    id: 'acetaminophen-pediatric',
    generic: { en: "Acetaminophen (children's/infants')", ko: '아세트아미노펜 (소아·영아용)', ja: 'アセトアミノフェン(小児·乳児用)' },
    brands: ["Children's Tylenol", "Infants' Tylenol", "FeverAll suppositories"],
    category: 'pediatric',
    uses: [
      { title_en: 'Fever reduction in infants and children', title_ko: '영아·소아 해열', title_ja: '乳児·小児の解熱',
        detail_en: 'Reduces fever from viral illness, immunizations, or other causes; first-line antipyretic for children, including infants over 3 months with doctor guidance',
        detail_ko: '바이러스 질환, 예방접종 또는 기타 원인의 발열 감소; 소아 1차 해열제이며 3개월 이상 영아에게도 의사 지도 하에 사용 가능',
        detail_ja: 'ウイルス疾患、予防接種、その他の原因による発熱を低下;小児の第一選択解熱薬で3か月以上の乳児にも医師の指導下で使用可能' },
      { title_en: 'Mild to moderate pain in children', title_ko: '소아 경도~중등도 통증', title_ja: '小児の軽度~中等度の痛み',
        detail_en: 'Teething pain, ear pain, post-immunization soreness, minor injuries, headache',
        detail_ko: '이앓이, 귀 통증, 예방접종 후 통증, 경미한 부상, 두통',
        detail_ja: '歯ぐずり、耳の痛み、予防接種後の痛み、軽度の外傷、頭痛' }
    ],
    dose_en: { 'Dose by weight (preferred)': '10–15 mg/kg per dose every 4–6 hours', 'Max doses per day': '5 doses in 24 hours', 'Under 3 months': 'Consult a doctor before use', 'Use concentration on label': 'Infant drops and children\'s liquid have DIFFERENT concentrations — read label carefully and use included dosing device only' },
    dose_ko: { '체중 기반 용량 (권장)': '체중 kg당 10~15 mg, 4~6시간마다', '하루 최대 횟수': '24시간 내 5회', '3개월 미만': '사용 전 의사와 상담', '농도는 라벨 확인': '영아용 드롭과 소아용 시럽 농도가 다릅니다 — 라벨을 주의 깊게 읽고 동봉된 계량기만 사용' },
    dose_ja: { '体重ベース用量(推奨)': '体重1 kg当たり10~15 mg、4~6時間ごと', '1日最大回数': '24時間以内に5回', '3か月未満': '使用前に医師に相談', '濃度はラベル確認': '乳児用ドロップと小児用シロップは濃度が異なります — ラベルを注意深く読み付属の計量器のみ使用' },
    danger_en: 'DOSING ERRORS ARE COMMON AND DANGEROUS. Liquid concentrations have been standardized to 160 mg/5 mL since 2011, but old bottles and imports may have different strengths. Never use a kitchen teaspoon. Do not give with other products containing acetaminophen (many cold medicines). Liver damage can occur with overdose.',
    danger_ko: '용량 오류가 흔하며 위험합니다. 2011년 이후 액상 농도는 160 mg/5 mL로 표준화되었으나 구형·해외 제품은 농도가 다를 수 있습니다. 주방용 티스푼 사용 금지. 아세트아미노펜 함유 다른 제품(감기약 다수)과 병용 금지. 과량 복용 시 간 손상 발생 가능.',
    danger_ja: '用量エラーは頻繁で危険です。2011年以降液体濃度は160 mg/5 mLに標準化されましたが、旧型·輸入製品は濃度が異なる可能性。台所用スプーン使用禁止。アセトアミノフェン含有の他製品(風邪薬多数)と併用禁止。過剰摂取で肝障害が発生する可能性。',
    warn_en: 'Contact a doctor if fever in infant under 3 months (any fever ≥100.4°F/38°C), fever lasts more than 3 days in any child, or pain lasts more than 5 days. Suppository form useful when vomiting. Do not use alternating acetaminophen/ibuprofen schedules without pediatrician guidance — often causes dosing confusion.',
    warn_ko: '3개월 미만 영아가 열이 나면(38°C 이상 어떤 발열이든), 3일 이상 열이 지속되거나 5일 이상 통증이 지속되면 진료. 좌제는 구토 시 유용. 아세트아미노펜/이부프로펜 교대 투여는 소아과 지도 없이 하지 마세요 — 용량 혼동이 흔합니다.',
    warn_ja: '3か月未満の乳児に発熱があれば(38°C以上のいかなる発熱でも)、3日以上発熱が続く、または5日以上痛みが続く場合は受診。坐薬は嘔吐時に有用。アセトアミノフェン/イブプロフェンの交互投与は小児科指導なく行わない — 用量混乱が頻発。',
    interact: [
      { en: 'Other acetaminophen-containing cold/flu products — overdose risk', ko: '아세트아미노펜 함유 감기·독감 제품 — 과량 복용 위험', ja: 'アセトアミノフェン含有の風邪·インフルエンザ製品 — 過剰摂取リスク' },
      { en: 'Warfarin (rare in children) — may increase INR with prolonged use', ko: '와파린 (소아에서는 드물지만) — 장기 사용 시 INR 증가 가능', ja: 'ワーファリン(小児では稀) — 長期使用でINR増加の可能性' },
      { en: 'Isoniazid, phenytoin, carbamazepine — induce CYP2E1, potentially increasing liver toxicity risk', ko: '이소니아지드, 페니토인, 카바마제핀 — CYP2E1 유도로 간독성 위험 증가', ja: 'イソニアジド、フェニトイン、カルバマゼピン — CYP2E1誘導で肝毒性リスク増加' }
    ],
    source: 'FDA OTC Monograph 21 CFR 343 · AAP Clinical Report · DailyMed (NIH)'
  },
  {
    id: 'ibuprofen-pediatric',
    generic: { en: "Ibuprofen (children's/infants')", ko: '이부프로펜 (소아·영아용)', ja: 'イブプロフェン(小児·乳児用)' },
    brands: ["Children's Motrin", "Children's Advil", "Infants' Motrin"],
    category: 'pediatric',
    uses: [
      { title_en: 'Fever reduction in children 6 months and older', title_ko: '6개월 이상 소아 해열', title_ja: '6か月以上の小児の解熱',
        detail_en: 'Effective antipyretic with longer duration than acetaminophen (6–8 hours vs 4–6); often preferred for higher fevers',
        detail_ko: '아세트아미노펜보다 지속 시간이 긴 해열제(6~8시간 대 4~6시간); 고열에 선호되는 경우가 많음',
        detail_ja: 'アセトアミノフェンより持続時間が長い解熱薬(6~8時間 対 4~6時間);高熱で好まれることが多い' },
      { title_en: 'Pain and inflammation in children', title_ko: '소아 통증·염증', title_ja: '小児の痛みと炎症',
        detail_en: 'Ear pain (otitis media), teething, sore throat, musculoskeletal pain, post-injury, post-immunization — anti-inflammatory effect is advantage over acetaminophen',
        detail_ko: '귀 통증(중이염), 이앓이, 인후통, 근골격 통증, 부상 후, 예방접종 후 — 아세트아미노펜 대비 소염 작용이 장점',
        detail_ja: '耳痛(中耳炎)、歯ぐずり、咽頭痛、筋骨格痛、外傷後、予防接種後 — アセトアミノフェンに対して抗炎症作用が利点' }
    ],
    dose_en: { 'Dose by weight': '5–10 mg/kg per dose every 6–8 hours', 'Max doses per day': '4 doses in 24 hours', 'Under 6 months': 'Do NOT use without doctor approval — risk of kidney complications', 'Take with food or milk': 'Reduces stomach upset' },
    dose_ko: { '체중 기반 용량': '체중 kg당 5~10 mg, 6~8시간마다', '하루 최대 횟수': '24시간 내 4회', '6개월 미만': '의사 승인 없이 사용 금지 — 신장 합병증 위험', '음식 또는 우유와 함께': '위장 장애 감소' },
    dose_ja: { '体重ベース用量': '体重1 kg当たり5~10 mg、6~8時間ごと', '1日最大回数': '24時間以内に4回', '6か月未満': '医師の承認なく使用禁止 — 腎臓合併症リスク', '食事または牛乳と共に': '胃腸障害を軽減' },
    danger_en: 'DO NOT USE IN INFANTS UNDER 6 MONTHS without doctor approval. Do not give to dehydrated children (from vomiting, diarrhea, or poor fluid intake) — high risk of acute kidney injury. Avoid in children with chickenpox (theoretical link to severe skin infections). Not recommended for children with asthma who have had reactions to NSAIDs.',
    danger_ko: '6개월 미만 영아에게 의사 승인 없이 사용 금지. 탈수된 소아(구토, 설사, 수분 섭취 부족)에게 투여 금지 — 급성 신손상 위험 높음. 수두 소아에서 피하세요(중증 피부감염과의 이론적 연관). NSAID 반응 병력이 있는 천식 소아에게 비권장.',
    danger_ja: '6か月未満の乳児に医師の承認なく使用禁止。脱水の小児(嘔吐、下痢、水分摂取不足)に投与禁止 — 急性腎障害リスク高い。水痘の小児では回避(重度皮膚感染との理論的関連)。NSAID反応既往のある喘息小児には非推奨。',
    warn_en: 'Does not replace acetaminophen in children under 6 months. Check the label for concentration — infant drops and children\'s liquid differ. Prolonged use can cause GI bleeding (rare in children but possible). If vomiting, fever above 104°F (40°C), stiff neck, rash, or lethargy — see a doctor immediately.',
    warn_ko: '6개월 미만 소아에서 아세트아미노펜을 대체할 수 없습니다. 라벨의 농도 확인 — 영아용 드롭과 소아용 시럽 다름. 장기 사용 시 소화관 출혈 가능(소아에서 드물지만 발생 가능). 구토, 40°C 이상 발열, 목 경직, 발진, 기면이 있으면 즉시 진료.',
    warn_ja: '6か月未満の小児ではアセトアミノフェンを代替できません。ラベルの濃度を確認 — 乳児用ドロップと小児用シロップは異なる。長期使用で消化管出血の可能性(小児では稀だが起こり得る)。嘔吐、40°C以上の発熱、項部硬直、発疹、嗜眠があれば即時受診。',
    interact: [
      { en: 'Other NSAIDs or aspirin — avoid combining; additive bleeding/kidney risk', ko: '기타 NSAID 또는 아스피린 — 병용 금지; 출혈·신장 위험 가중', ja: '他のNSAIDまたはアスピリン — 併用回避;出血·腎臓リスクの累積' },
      { en: 'Dehydration, ACE inhibitors, diuretics — increased kidney injury risk', ko: '탈수, ACE 억제제, 이뇨제 — 신손상 위험 증가', ja: '脱水、ACE阻害薬、利尿薬 — 腎障害リスク増加' },
      { en: 'Methotrexate — increased toxicity; relevant in pediatric rheumatology patients', ko: '메토트렉세이트 — 독성 증가; 소아 류마티스 환자에서 관련', ja: 'メトトレキサート — 毒性増加;小児リウマチ患者で関連' }
    ],
    source: 'FDA OTC Monograph · AAP Clinical Report · DailyMed (NIH)'
  },
  {
    id: 'pedialyte',
    generic: { en: 'Pediatric oral rehydration solution (ORS)', ko: '소아용 경구 수액 보충제', ja: '小児用経口補水液(ORS)' },
    brands: ['Pedialyte (solution, freezer pops, powder packs)', 'Enfalyte', 'CeraLyte'],
    category: 'pediatric',
    uses: [
      { title_en: 'Mild to moderate dehydration in children', title_ko: '소아 경도~중등도 탈수', title_ja: '小児の軽度~中等度脱水',
        detail_en: 'Replaces water, sodium, potassium, and chloride lost to vomiting, diarrhea, fever, or heat — scientifically formulated to match WHO/UNICEF pediatric ORS composition with appropriate sodium (45 mEq/L) and glucose for absorption',
        detail_ko: '구토, 설사, 발열, 더위로 손실된 수분, 나트륨, 칼륨, 염소를 보충 — WHO/UNICEF 소아 ORS 조성에 맞춰 흡수에 적절한 나트륨(45 mEq/L)과 포도당으로 구성',
        detail_ja: '嘔吐、下痢、発熱、暑さで失われた水分、ナトリウム、カリウム、塩素を補給 — WHO/UNICEFの小児ORS組成に合わせ吸収に適切なナトリウム(45 mEq/L)とブドウ糖で構成' },
      { title_en: 'Dehydration prevention during acute illness', title_ko: '급성 질환 중 탈수 예방', title_ja: '急性疾患中の脱水予防',
        detail_en: 'Prophylactic use during stomach flu, norovirus, fever, or any illness causing poor oral intake — maintains hydration until illness resolves',
        detail_ko: '장염, 노로바이러스, 발열 또는 경구 섭취 부족을 유발하는 질환 중 예방적 사용 — 질병이 호전될 때까지 수분 유지',
        detail_ja: '胃腸炎、ノロウイルス、発熱、または経口摂取不足を起こす疾患中の予防的使用 — 病気が回復するまで水分維持' }
    ],
    dose_en: { 'Mild dehydration (infants and young children)': 'Offer small sips (1 teaspoon / 5 mL) every 1–5 minutes initially; increase as tolerated', 'Goal volume': 'Roughly 50 mL/kg over 4 hours for mild, 100 mL/kg for moderate dehydration', 'After each diarrhea episode': '10 mL/kg additional fluid', 'Do NOT dilute': 'Do not mix with water, juice, or formula — alters electrolyte balance' },
    dose_ko: { '경도 탈수 (영아·유아)': '처음에는 1~5분마다 소량(1티스푼/5 mL)씩 자주; 가능하면 점차 증량', '목표 용량': '경도 탈수는 4시간 동안 체중 kg당 약 50 mL, 중등도는 100 mL', '설사 에피소드마다': '체중 kg당 10 mL 추가', '희석 금지': '물, 주스, 분유와 섞지 마세요 — 전해질 균형 변경' },
    dose_ja: { '軽度脱水(乳児·幼児)': '最初は1~5分ごとに少量(小さじ1杯/5 mL)ずつ頻回に;可能なら徐々に増量', '目標量': '軽度脱水は4時間で体重1 kg当たり約50 mL、中等度は100 mL', '下痢エピソードごと': '体重1 kg当たり10 mL追加', '希釈禁止': '水、ジュース、ミルクと混ぜない — 電解質バランスを変える' },
    danger_en: 'DO NOT USE HOMEMADE SALT-SUGAR SOLUTIONS for children — incorrect proportions have caused fatal hypernatremia. Do NOT use sports drinks (Gatorade, Powerade) as a substitute — they contain too much sugar and too little sodium for pediatric use, worsening diarrhea. Signs of SEVERE dehydration (no tears, sunken fontanelle, no urine for 8+ hours, lethargy, rapid breathing) require emergency care — not just ORS.',
    danger_ko: '소아에게 가정에서 만든 소금-설탕 용액을 사용하지 마세요 — 비율 오류로 치명적인 고나트륨혈증 사례가 있습니다. 스포츠 음료(게토레이, 파워에이드)를 대체재로 사용하지 마세요 — 당분은 많고 나트륨은 부족하여 소아 설사를 악화시킵니다. 중증 탈수 징후(눈물 없음, 대천문 함몰, 8시간 이상 소변 없음, 기면, 빠른 호흡)는 ORS로 안 되고 응급 진료 필요.',
    danger_ja: '小児に自家製塩·砂糖溶液を使用しないでください — 比率エラーで致命的高ナトリウム血症の事例あり。スポーツ飲料(ゲータレード、パワーエイド)を代替として使用しない — 糖分が多く塩分が少なく小児の下痢を悪化。重度脱水徴候(涙なし、大泉門陥没、8時間以上排尿なし、嗜眠、頻呼吸)はORSでは不十分で救急受診必要。',
    warn_en: 'If vomiting persists despite small frequent sips, child refuses all fluids, has bloody diarrhea, high fever, or signs of severe dehydration — see a doctor. Continue normal diet as tolerated alongside ORS; do not withhold food more than 24 hours. Breastfeeding should continue.',
    warn_ko: '소량 자주 시도에도 구토가 지속되거나 모든 수분을 거부하거나 혈변, 고열, 중증 탈수 징후가 있으면 진료. ORS와 함께 가능한 범위에서 정상 식이 지속; 24시간 이상 음식 제한 금지. 모유 수유는 계속하세요.',
    warn_ja: '少量頻回の試みにも嘔吐が続く、すべての水分を拒否、血便、高熱、重度脱水徴候がある場合は受診。ORSと共に可能な範囲で通常食を継続;24時間以上食事制限禁止。母乳は継続。',
    interact: [
      { en: 'Kidney disease — consult doctor before use; may need modified electrolyte solution', ko: '신장 질환 — 사용 전 의사 상담; 전해질 조성 조정 필요 가능', ja: '腎疾患 — 使用前に医師相談;電解質組成調整必要の可能性' },
      { en: 'Diuretics — not a clinical interaction but check electrolyte status', ko: '이뇨제 — 임상 상호작용은 아니지만 전해질 상태 확인', ja: '利尿薬 — 臨床相互作用ではないが電解質状態を確認' },
      { en: 'Adrenal insufficiency — may need additional sodium; consult doctor', ko: '부신 부전 — 추가 나트륨 필요 가능; 의사 상담', ja: '副腎不全 — 追加ナトリウム必要の可能性;医師相談' }
    ],
    source: 'AAP Clinical Report on Pediatric Dehydration · WHO ORS Guidelines · DailyMed (NIH)'
  },
  {
    id: 'diphenhydramine-pediatric',
    generic: { en: "Diphenhydramine (children's)", ko: '디펜히드라민 (소아용)', ja: 'ジフェンヒドラミン(小児用)' },
    brands: ["Children's Benadryl Allergy", "PediaCare Allergy"],
    category: 'pediatric',
    uses: [
      { title_en: 'Allergic reactions in children 6 years and older', title_ko: '6세 이상 소아 알레르기 반응', title_ja: '6歳以上の小児のアレルギー反応',
        detail_en: 'Hives, insect stings, mild allergic rhinitis, reactions to food allergens (along with epinephrine if anaphylaxis), itching from eczema or poison ivy',
        detail_ko: '두드러기, 벌레 물림, 경미한 알레르기 비염, 음식 알레르기 반응(아나필락시스 시 에피네프린과 함께), 습진·옻 가려움',
        detail_ja: 'じんま疹、虫刺され、軽度のアレルギー性鼻炎、食物アレルギー反応(アナフィラキシー時はエピネフリンと併用)、湿疹·ウルシのかゆみ' }
    ],
    dose_en: { 'Age 6–11': '12.5–25 mg every 4–6 hours (max 6 doses in 24 hr)', 'Age 2–5': 'Only under doctor guidance; 6.25 mg every 4–6 hours if prescribed', 'Under 2 years': 'DO NOT USE — FDA warning against use in infants and toddlers for any purpose', 'Use measuring device provided': 'Never use a kitchen spoon' },
    dose_ko: { '6~11세': '4~6시간마다 12.5~25 mg (24시간 내 최대 6회)', '2~5세': '의사 지도 하에만; 처방 시 4~6시간마다 6.25 mg', '2세 미만': '사용 금지 — FDA는 영·유아 어떤 목적으로도 사용을 경고', '동봉된 계량기 사용': '주방용 스푼 사용 금지' },
    dose_ja: { '6~11歳': '4~6時間ごとに12.5~25 mg(24時間以内に最大6回)', '2~5歳': '医師指導下のみ;処方時は4~6時間ごとに6.25 mg', '2歳未満': '使用禁止 — FDAは乳幼児へのいかなる目的の使用にも警告', '付属の計量器使用': '台所用スプーン使用禁止' },
    danger_en: 'NEVER USE AS A SLEEP AID OR SEDATIVE IN CHILDREN — deaths have occurred from caregivers giving diphenhydramine to make children sleep or to sedate during travel. "Paradoxical agitation" is common in children: instead of drowsiness, children become hyperactive, agitated, or hallucinate. Overdose can cause seizures, coma, fatal heart rhythm disturbances.',
    danger_ko: '소아에게 수면 보조제·진정제로 절대 사용 금지 — 보호자가 수면 유도나 여행 중 진정을 위해 투여하여 사망한 사례가 있습니다. 소아에서 "역설적 흥분"이 흔함: 졸음 대신 과활동, 흥분, 환각 발생. 과량 복용 시 경련, 혼수, 치명적 부정맥 가능.',
    danger_ja: '小児に睡眠補助·鎮静目的で絶対使用禁止 — 保護者が睡眠導入や旅行中の鎮静のため投与し死亡した事例あり。小児では「逆説的興奮」が頻繁:眠気の代わりに多動、興奮、幻覚が発生。過剰摂取で発作、昏睡、致命的不整脈の可能性。',
    warn_en: 'Drowsiness, dry mouth, blurred vision, urinary retention common. Avoid in children with glaucoma (rare), asthma, or chronic lung conditions without doctor advice. Newer non-drowsy alternatives (children\'s cetirizine, children\'s loratadine) are preferred for daily allergy use.',
    warn_ko: '졸음, 구갈, 흐린 시야, 요폐가 흔함. 녹내장(드물지만), 천식, 만성 폐질환 소아는 의사 조언 없이 사용 피하세요. 일상 알레르기에는 졸음 없는 대체약(소아용 세티리진·로라타딘)을 권장합니다.',
    warn_ja: '眠気、口渇、霞み目、尿閉が一般的。緑内障(稀)、喘息、慢性肺疾患の小児は医師の助言なく使用回避。日常アレルギーには眠気のない代替薬(小児用セチリジン·ロラタジン)を推奨。',
    interact: [
      { en: 'Other sedating medications (cough/cold products, muscle relaxants) — dangerous additive sedation', ko: '기타 진정 작용 약물 (기침·감기약, 근이완제) — 위험한 진정 가중', ja: '他の鎮静作用薬(咳·風邪薬、筋弛緩薬) — 危険な鎮静の累積' },
      { en: 'MAO inhibitors — avoid', ko: 'MAO 억제제 — 피하세요', ja: 'MAO阻害薬 — 回避' },
      { en: 'Alcohol-containing medications (some cough syrups) — avoid', ko: '알코올 함유 약물 (일부 기침 시럽) — 피하세요', ja: 'アルコール含有薬(一部の咳止めシロップ) — 回避' },
      { en: 'Other anticholinergics — confusion, urinary retention', ko: '기타 항콜린제 — 혼동, 요폐', ja: '他の抗コリン薬 — 混乱、尿閉' }
    ],
    source: 'FDA Pediatric Cough/Cold Advisory · AAP · DailyMed (NIH)'
  },
  {
    id: 'pediatric-cold-caution',
    generic: { en: 'Children\'s cold and cough medicines — FDA age restrictions', ko: '소아 감기·기침약 — FDA 연령 제한', ja: '小児用風邪·咳止め薬 — FDA年齢制限' },
    brands: ['Dimetapp Children\'s', 'Robitussin Pediatric', 'Triaminic', 'Delsym Children\'s'],
    category: 'pediatric',
    uses: [
      { title_en: 'Limited role in cold/cough in children', title_ko: '소아 감기·기침에서의 제한된 역할', title_ja: '小児の風邪·咳での限定的役割',
        detail_en: 'FDA and American Academy of Pediatrics recommend against OTC cough and cold medicines in children under 4 years. Evidence of efficacy in children is weak and risk of dosing error, paradoxical reactions, and overdose is high. Use in ages 4–6 only with doctor guidance',
        detail_ko: 'FDA와 미국소아과학회는 4세 미만 소아에서 OTC 기침·감기약을 권장하지 않습니다. 소아에서 효과 근거는 약하며 용량 오류, 역설 반응, 과량 복용 위험이 높습니다. 4~6세에서는 의사 지도 하에만 사용',
        detail_ja: 'FDAと米国小児科学会は4歳未満の小児にOTC咳·風邪薬を推奨していません。小児での有効性エビデンスは弱く、用量エラー、逆説反応、過剰摂取リスクが高い。4~6歳では医師指導下でのみ使用' }
    ],
    dose_en: { 'Under 4 years': 'DO NOT USE any OTC cough/cold combination product', 'Age 4–6': 'Only if a doctor specifically recommends', 'Age 6 and older': 'Follow label; single-ingredient products preferred over combinations', 'Supportive care instead': 'Saline nasal drops + bulb syringe, humidifier, honey (age 1+) 2.5–5 mL for cough, extra fluids, rest' },
    dose_ko: { '4세 미만': 'OTC 기침·감기 복합제 사용 금지', '4~6세': '의사가 구체적으로 권장한 경우에만', '6세 이상': '라벨에 따름; 복합제보다 단일 성분 제품 권장', '대신 보조 요법': '식염수 비강 드롭 + 흡인기, 가습기, 꿀(1세 이상) 2.5~5 mL 기침에, 충분한 수분, 휴식' },
    dose_ja: { '4歳未満': 'OTC咳·風邪複合薬使用禁止', '4~6歳': '医師が具体的に推奨した場合のみ', '6歳以上': 'ラベルに従う;複合薬より単一成分製品を推奨', '代わりに支持療法': '生理食塩水点鼻 + 鼻吸引器、加湿器、ハチミツ(1歳以上)2.5~5 mLを咳に、追加の水分、休息' },
    danger_en: 'FATAL CASES HAVE OCCURRED from OTC cough/cold medicines in infants and toddlers (including pseudoephedrine, phenylephrine, diphenhydramine, chlorpheniramine combinations). In 2008, FDA and manufacturers voluntarily removed "under 2" dosing from labels. Honey should NOT be given to infants under 12 months (botulism risk).',
    danger_ko: '영·유아에서 OTC 기침·감기약(슈도에페드린, 페닐에프린, 디펜히드라민, 클로르페니라민 복합제 포함)으로 치명적인 사례가 발생했습니다. 2008년 FDA와 제조사는 "2세 미만" 용량 표기를 자율적으로 삭제했습니다. 12개월 미만 영아에게 꿀 금지(보툴리누스 위험).',
    danger_ja: '乳幼児でOTC咳·風邪薬(プソイドエフェドリン、フェニレフリン、ジフェンヒドラミン、クロルフェニラミン複合薬を含む)による致命的事例が発生。2008年FDAと製造業者は「2歳未満」の用量表示を自主的に削除。12か月未満の乳児にハチミツ禁止(ボツリヌス症リスク)。',
    warn_en: 'Do not combine multiple cold/cough products — many contain overlapping ingredients (acetaminophen, antihistamines, decongestants). Cough lasting more than 7 days, fever lasting more than 3 days, or worsening symptoms warrant evaluation — possible bacterial infection, asthma, pneumonia, or pertussis.',
    warn_ko: '여러 감기·기침약 병용 금지 — 많은 제품에 성분(아세트아미노펜, 항히스타민, 비충혈 완화제)이 중복됩니다. 7일 이상 기침, 3일 이상 발열, 증상 악화는 평가 필요 — 세균 감염, 천식, 폐렴, 백일해 가능성.',
    warn_ja: '複数の風邪·咳止め薬の併用禁止 — 多くの製品で成分(アセトアミノフェン、抗ヒスタミン薬、鬱血除去薬)が重複。7日以上続く咳、3日以上続く発熱、症状悪化は評価必要 — 細菌感染、喘息、肺炎、百日咳の可能性。',
    interact: [
      { en: 'Other acetaminophen-containing products — liver injury risk', ko: '기타 아세트아미노펜 함유 제품 — 간 손상 위험', ja: '他のアセトアミノフェン含有製品 — 肝障害リスク' },
      { en: 'MAO inhibitors (rare in pediatrics but possible) — dangerous interactions with decongestants', ko: 'MAO 억제제 (소아에서 드물지만 가능) — 비충혈 완화제와 위험한 상호작용', ja: 'MAO阻害薬(小児では稀だが起こり得る) — 鬱血除去薬と危険な相互作用' },
      { en: 'Other antihistamines or sedatives — additive CNS depression', ko: '기타 항히스타민 또는 진정제 — 중추신경 억제 가중', ja: '他の抗ヒスタミン薬または鎮静薬 — 中枢神経抑制の累積' }
    ],
    source: 'FDA Public Health Advisory 2008 · AAP Clinical Report on Pediatric Cough and Cold · DailyMed (NIH)'
  },
  {
    id: 'simethicone-infant',
    generic: { en: 'Simethicone drops (infant gas)', ko: '시메티콘 드롭 (영아 가스)', ja: 'ジメチコン点滴(乳児ガス)' },
    brands: ["Mylicon Infants' Gas Relief", 'Little Remedies Gas Relief', 'Gerber Soothe Colic Drops'],
    category: 'pediatric',
    uses: [
      { title_en: 'Infant gas and fussiness from swallowed air', title_ko: '공기 삼킴으로 인한 영아 가스·보챔', title_ja: '空気飲み込みによる乳児のガス·ぐずり',
        detail_en: 'Defoaming agent that reduces surface tension of gas bubbles in the gut; may relieve discomfort from trapped gas after feeding. Not absorbed systemically — considered very safe but evidence of efficacy in colic is weak',
        detail_ko: '장 내 가스 방울의 표면 장력을 낮추는 소포제; 수유 후 가스 축적으로 인한 불편을 완화할 수 있음. 전신 흡수되지 않아 매우 안전하나 영아 산통에서 효과 근거는 약함',
        detail_ja: '腸内ガス気泡の表面張力を低下させる消泡剤;授乳後のガス蓄積による不快感を緩和する可能性。全身吸収されず非常に安全だが、乳児疝痛での有効性エビデンスは弱い' }
    ],
    dose_en: { 'Under 2 years (< 11 kg / 24 lb)': '20 mg (0.3 mL) up to 4 times daily, after meals and bedtime', 'Age 2+ / over 11 kg': '40 mg (0.6 mL) up to 4 times daily', 'Max per day': '240 mg (12 doses)', 'How to give': 'Dropper can be placed in cheek; also mixed with 1 oz (30 mL) formula, breast milk, or water' },
    dose_ko: { '2세 미만 (11 kg / 24 lb 미만)': '식후와 취침 시 하루 최대 4회 20 mg (0.3 mL)', '2세 이상 / 11 kg 초과': '하루 최대 4회 40 mg (0.6 mL)', '하루 최대': '240 mg (12회)', '투여 방법': '드로퍼를 볼 안쪽에 투여; 분유, 모유 또는 물 30 mL와 섞어도 됨' },
    dose_ja: { '2歳未満(11 kg / 24 lb未満)': '食後·就寝時に1日最大4回20 mg(0.3 mL)', '2歳以上 / 11 kg超': '1日最大4回40 mg(0.6 mL)', '1日最大量': '240 mg(12回)', '投与方法': 'ドロッパーを頬の内側に投与;ミルク·母乳または水30 mLと混ぜてもよい' },
    warn_en: 'Colic and persistent fussiness have many causes — reflux (GERD), cow\'s milk protein allergy, lactose intolerance, maternal diet (if breastfed), or overfeeding. If crying lasts several hours daily or infant is poorly feeding, losing weight, vomiting forcefully, or has blood in stool — see a pediatrician. Simethicone is not a substitute for diagnosis.',
    warn_ko: '영아 산통과 지속적인 보챔의 원인은 다양합니다 — 역류(GERD), 우유 단백질 알레르기, 유당 불내증, 모유 수유 시 산모 식이, 과수유 등. 매일 수 시간 울음, 수유 부진, 체중 감소, 강한 구토, 혈변이 있으면 소아과 진료. 시메티콘은 진단을 대체하지 않습니다.',
    warn_ja: '乳児疝痛と持続的なぐずりの原因は様々 — 逆流(GERD)、牛乳タンパク質アレルギー、乳糖不耐症、母乳の場合の母親の食事、過剰授乳など。毎日数時間泣く、授乳不良、体重減少、強い嘔吐、血便がある場合は小児科受診。ジメチコンは診断を代替しません。',
    interact: [
      { en: 'Levothyroxine — theoretical absorption interference; separate by 2–4 hours if relevant (rare in infants)', ko: '레보티록신 — 이론적 흡수 방해; 해당 시 2~4시간 간격 (영아에서 드묾)', ja: 'レボチロキシン — 理論的吸収干渉;該当時は2~4時間間隔(乳児では稀)' },
      { en: 'Generally no clinically significant drug interactions (not absorbed)', ko: '일반적으로 임상적으로 유의한 약물 상호작용 없음 (흡수되지 않음)', ja: '一般的に臨床的に有意な薬物相互作用なし(吸収されない)' }
    ],
    source: 'FDA OTC Monograph · AAP · DailyMed (NIH)'
  },
  {
    id: 'saline-nasal-infant',
    generic: { en: 'Saline nasal drops / spray (infant and child)', ko: '식염수 비강 드롭·스프레이 (영아·소아용)', ja: '生理食塩水点鼻液·スプレー(乳児·小児用)' },
    brands: ['Little Remedies Saline Drops', 'Simply Saline Kids', 'Ayr Saline Mist', 'Boogie Mist'],
    category: 'pediatric',
    uses: [
      { title_en: 'Nasal congestion from cold, dry air, or allergies', title_ko: '감기·건조 공기·알레르기로 인한 코막힘', title_ja: '風邪·乾燥·アレルギーによる鼻づまり',
        detail_en: 'Isotonic 0.9% saline thins mucus and moisturizes nasal passages; safe first-line option for infants and young children who cannot take oral decongestants. Often paired with a bulb syringe or nasal aspirator (NoseFrida) for mucus removal',
        detail_ko: '등장성 0.9% 식염수가 점액을 묽게 하고 비강을 습윤; 경구 비충혈 완화제를 사용할 수 없는 영·유아의 안전한 1차 선택. 고무 흡인기 또는 비강 흡인기(NoseFrida)와 함께 점액 제거에 사용',
        detail_ja: '等張0.9%生理食塩水が粘液を薄め鼻腔を加湿;経口鬱血除去薬を使用できない乳幼児の安全な第一選択。ゴム吸引器または鼻吸引器(NoseFrida)と併用して粘液除去' },
      { title_en: 'Daily nasal hygiene', title_ko: '일상 비강 관리', title_ja: '日常の鼻ケア',
        detail_en: 'Useful in dry climates, after exposure to pollen or smoke, or to prevent mucus crusting during illness',
        detail_ko: '건조한 기후, 꽃가루·연기 노출 후, 질환 중 점액 굳음 예방에 유용',
        detail_ja: '乾燥気候、花粉·煙曝露後、疾患中の粘液固化予防に有用' }
    ],
    dose_en: { 'Infant drops': '2–6 drops in each nostril as needed; follow with bulb syringe suction if needed', 'Spray (ages 2+)': '1–3 sprays per nostril as needed', 'Frequency': 'Can be used multiple times daily — no rebound congestion (unlike oxymetazoline)', 'Technique for infants': 'Lay baby on back, instill drops, wait 30 seconds, suction gently with bulb or nasal aspirator' },
    dose_ko: { '영아용 드롭': '필요시 각 콧구멍에 2~6 방울; 필요하면 흡인기로 흡인', '스프레이 (2세 이상)': '필요시 각 콧구멍에 1~3회 분무', '사용 빈도': '하루 여러 번 사용 가능 — 옥시메타졸린과 달리 반동성 충혈 없음', '영아 사용법': '영아를 눕히고 드롭 투여 후 30초 대기, 흡인기로 부드럽게 흡인' },
    dose_ja: { '乳児用点滴': '必要に応じて各鼻孔に2~6滴;必要なら吸引器で吸引', 'スプレー(2歳以上)': '必要に応じて各鼻孔に1~3回噴霧', '使用頻度': '1日複数回使用可能 — オキシメタゾリンと異なり反跳性鬱血なし', '乳児への使い方': '乳児を仰向けにし点滴投与後30秒待機、吸引器で穏やかに吸引' },
    warn_en: 'Do not use homemade salt water — incorrect concentration can damage delicate nasal mucosa and introduce contamination. Bulb syringes should be cleaned and fully dried between uses to prevent mold. Excessive suctioning causes nasal irritation and nosebleeds. If infant has poor feeding from congestion, fever, difficulty breathing, or bluish lips — seek urgent care.',
    warn_ko: '집에서 만든 소금물 사용 금지 — 농도 오류로 비강 점막 손상 및 오염 가능. 흡인기는 사용 사이에 세척하고 완전히 건조하여 곰팡이 예방. 과도한 흡인은 비강 자극과 코피 유발. 영아가 코막힘으로 수유 부진, 발열, 호흡 곤란, 입술 청색증이 있으면 즉시 진료.',
    warn_ja: '自家製塩水使用禁止 — 濃度エラーで鼻腔粘膜損傷と汚染の可能性。吸引器は使用間に洗浄し完全に乾燥してカビ予防。過度の吸引は鼻腔刺激と鼻血を起こす。乳児が鼻づまりで授乳不良、発熱、呼吸困難、唇のチアノーゼがあれば即時受診。',
    interact: [
      { en: 'No systemic drug interactions', ko: '전신 약물 상호작용 없음', ja: '全身薬物相互作用なし' },
      { en: 'Can be used alongside other nasal medications with 5–10 minute separation', ko: '다른 비강 약물과 5~10분 간격으로 병용 가능', ja: '他の鼻用薬と5~10分の間隔で併用可能' }
    ],
    source: 'AAP Clinical Report on Infant Nasal Congestion · FDA · DailyMed (NIH)'
  },
  {
    id: 'gripe-water',
    generic: { en: 'Gripe water (herbal infant tonic)', ko: '그라이프 워터 (영아용 허브 토닉)', ja: 'グライプウォーター(乳児用ハーブトニック)' },
    brands: ['Mommy\'s Bliss Gripe Water', 'Little Remedies Gripe Water', 'Wellements Organic Gripe Water'],
    category: 'pediatric',
    uses: [
      { title_en: 'Folk remedy for infant fussiness, gas, hiccups', title_ko: '영아 보챔·가스·딸꾹질의 민간요법', title_ja: '乳児のぐずり·ガス·しゃっくりの民間療法',
        detail_en: 'Traditional herbal preparation, typically containing fennel, ginger, chamomile, and/or lemon balm. Marketed for gas and colic but NOT FDA-approved; no rigorous evidence of efficacy. Classified as a dietary supplement, so quality and composition vary by brand',
        detail_ko: '전통적인 허브 조제물로 보통 펜넬, 생강, 카모마일, 레몬밤 등을 함유. 가스와 산통 용도로 판매되나 FDA 승인되지 않았으며 엄격한 효과 근거 없음. 식이 보충제로 분류되어 브랜드별 품질·조성이 다름',
        detail_ja: '伝統的なハーブ調剤で通常フェンネル、生姜、カモミール、レモンバームなどを含有。ガスと疝痛用途で販売されているがFDA承認されておらず、厳密な有効性エビデンスなし。栄養補助食品に分類されブランドごとに品質·組成が異なる' }
    ],
    dose_en: { 'Typical label dose': '2.5 mL (½ tsp) for infants 2 weeks–1 month, up to 5 mL (1 tsp) for 1–6 months, up to 10 mL (2 tsp) for 6+ months, up to 6 times daily', 'Check label': 'Dosing varies significantly by brand', 'Choose alcohol-free and sugar-free formulations': 'Older formulations contained alcohol — no longer acceptable' },
    dose_ko: { '표준 용량 (라벨 기준)': '2주~1개월 영아 2.5 mL(½ 티스푼), 1~6개월 최대 5 mL(1 티스푼), 6개월 이상 최대 10 mL(2 티스푼), 하루 최대 6회', '라벨 확인': '브랜드별 용량 차이 큼', '무알코올·무가당 제형 선택': '구형 제품은 알코올 함유 — 현재는 허용되지 않음' },
    dose_ja: { '標準用量(ラベル基準)': '2週~1か月乳児2.5 mL(½小さじ)、1~6か月最大5 mL(1小さじ)、6か月以上最大10 mL(2小さじ)、1日最大6回', 'ラベル確認': 'ブランドごとに用量差大', 'アルコールフリー·砂糖フリー製剤を選択': '旧型製品はアルコール含有 — 現在は許容されない' },
    danger_en: 'NOT FDA-APPROVED AS A DRUG. Some products have been recalled for contamination (microbial, heavy metals). Avoid products containing alcohol, sucrose, or sodium bicarbonate (baking soda — can cause dangerous electrolyte imbalance in infants). Do NOT use in infants under 2 weeks or under 1 month per most labels. Does not treat the underlying cause of colic; evaluate for reflux, milk protein allergy, or overfeeding if fussiness is severe.',
    danger_ko: 'FDA 의약품으로 승인되지 않았습니다. 일부 제품은 오염(미생물·중금속)으로 리콜된 바 있습니다. 알코올, 수크로스, 탄산수소나트륨(베이킹소다 — 영아 전해질 불균형 위험) 함유 제품 피하세요. 대부분 라벨상 2주 미만 또는 1개월 미만 영아에게 사용 금지. 산통의 근본 원인을 치료하지 않으므로 심한 보챔은 역류, 우유 단백질 알레르기, 과수유 평가가 필요합니다.',
    danger_ja: 'FDA医薬品として承認されていません。一部の製品は汚染(微生物·重金属)でリコールされたことがあります。アルコール、ショ糖、炭酸水素ナトリウム(重曹 — 乳児電解質不均衡リスク)含有製品を回避。多くのラベルで2週間未満または1か月未満の乳児に使用禁止。疝痛の根本原因を治療しないため、強いぐずりは逆流、ミルクタンパク質アレルギー、過剰授乳の評価が必要。',
    warn_en: 'Herbal supplements during breastfeeding or in infants can interact with medications or cause allergic reactions (chamomile cross-reacts with ragweed allergy). Choose products that are USP-verified or from established brands with third-party testing. Evidence-based alternatives: bicycle-leg exercises, warm bath, white noise, pacifier, simethicone drops (if trapped gas suspected).',
    warn_ko: '수유 중이나 영아에서 허브 보충제는 약물과 상호작용하거나 알레르기 반응(카모마일은 돼지풀 알레르기와 교차 반응)을 일으킬 수 있습니다. USP 인증 또는 제3자 검사를 거친 믿을 만한 브랜드 선택. 근거 기반 대안: 자전거 다리 운동, 따뜻한 목욕, 백색 소음, 공갈젖꼭지, 시메티콘 드롭(가스 의심 시).',
    warn_ja: '授乳中や乳児でハーブサプリメントは薬と相互作用したりアレルギー反応(カモミールはブタクサアレルギーと交差反応)を起こす可能性。USP認証または第三者検査済みの信頼できるブランドを選択。エビデンスベースの代替案:自転車漕ぎ運動、温かい入浴、ホワイトノイズ、おしゃぶり、ジメチコン点滴(ガス疑い時)。',
    interact: [
      { en: 'Herbal constituents (fennel, chamomile) — theoretical interactions with anticoagulants (rare in infants)', ko: '허브 성분 (펜넬, 카모마일) — 항응고제와 이론적 상호작용 (영아에서 드묾)', ja: 'ハーブ成分(フェンネル、カモミール) — 抗凝固薬との理論的相互作用(乳児では稀)' },
      { en: 'Ragweed-family allergies — risk of allergic reaction to chamomile-containing products', ko: '돼지풀과 알레르기 — 카모마일 함유 제품에 알레르기 반응 위험', ja: 'ブタクサ科アレルギー — カモミール含有製品にアレルギー反応リスク' },
      { en: 'Other herbal products — cumulative herbal exposure in infants is not well-studied', ko: '기타 허브 제품 — 영아에서 허브 누적 노출은 연구 부족', ja: '他のハーブ製品 — 乳児でのハーブ累積曝露は研究不足' }
    ],
    source: 'FDA Dietary Supplement regulations (DSHEA) · AAP guidance · NIH Office of Dietary Supplements'
  },

  // ============ EYE & EAR (additional) ============
  {
    id: 'tetrahydrozoline',
    generic: { en: 'Tetrahydrozoline (redness-relief eye drops)', ko: '테트라히드로졸린 (충혈 완화 안약)', ja: 'テトラヒドロゾリン(充血緩和点眼液)' },
    brands: ['Visine Original', 'Murine Tears Plus', 'Altazine'],
    category: 'eye_ear',
    uses: [
      { title_en: 'Temporary relief of minor eye redness', title_ko: '경미한 눈 충혈의 일시적 완화', title_ja: '軽度の目の充血の一時的緩和',
        detail_en: 'Vasoconstrictor that narrows superficial conjunctival blood vessels; reduces appearance of redness from smoke, smog, swimming, contact lens wear, or minor irritation. Does NOT treat the underlying cause',
        detail_ko: '결막 표면 혈관을 수축시키는 혈관수축제; 연기, 스모그, 수영, 콘택트렌즈 착용 또는 경미한 자극으로 인한 충혈을 감소. 근본 원인을 치료하지 않음',
        detail_ja: '結膜表面の血管を収縮させる血管収縮薬;煙、スモッグ、水泳、コンタクトレンズ装用または軽度の刺激による充血を軽減。根本原因は治療しない' }
    ],
    dose_en: { 'Adult and child 6+': '1–2 drops in affected eye(s) up to 4 times daily', 'Max duration': '72 hours (3 days) — rebound redness develops with longer use', 'Remove contact lenses': 'Wait 15 minutes before reinserting contacts' },
    dose_ko: { '성인 및 6세 이상': '해당 눈에 하루 4회까지 1~2방울', '최대 사용 기간': '72시간(3일) — 장기 사용 시 반동성 충혈 발생', '콘택트렌즈': '렌즈 재착용 전 15분 대기' },
    dose_ja: { '成人および6歳以上': '該当する目に1日4回まで1~2滴', '最大使用期間': '72時間(3日) — 長期使用で反跳性充血が発生', 'コンタクトレンズ': 'レンズ再装着前に15分待機' },
    danger_en: 'ORAL INGESTION IS LIFE-THREATENING — accidental swallowing of a few drops by a small child can cause coma, slow heart rate, seizures, dangerously low blood pressure. Keep tightly capped and locked away from children. Eye-drop bottle looks similar to nasal and oral products — read label before each use. Rebound redness (worse redness when drug wears off) occurs with >3 days use.',
    danger_ko: '경구 섭취 시 생명을 위협 — 어린이가 몇 방울만 실수로 삼켜도 혼수, 서맥, 경련, 위험한 저혈압 발생 가능. 밀봉하여 소아 손이 닿지 않게 보관. 안약 병은 비강·경구 제품과 비슷하므로 매번 라벨 확인. 3일 초과 사용 시 반동성 충혈(약 효과가 사라질 때 더 심한 충혈) 발생.',
    danger_ja: '経口摂取で生命を脅かす — 小児が数滴を誤って飲み込むだけで昏睡、徐脈、けいれん、危険な低血圧を起こす可能性。密閉し小児の手の届かない場所に保管。点眼ボトルは鼻用·経口製品と似ているので毎回ラベル確認。3日超使用で反跳性充血(薬効が切れたときにより強い充血)が発生。',
    warn_en: 'Avoid if you have glaucoma or narrow anterior chamber angles — can trigger acute angle-closure glaucoma attack. Stop and see a doctor if redness persists beyond 72 hours, if pain, vision change, or discharge develops — these suggest infection, iritis, or other condition needing evaluation, not simple redness.',
    warn_ko: '녹내장 또는 좁은 전방각이 있으면 사용 피하세요 — 급성 폐쇄각 녹내장 발작 유발 가능. 72시간 후 충혈이 지속되거나 통증, 시력 변화, 분비물이 있으면 중단하고 진료 — 단순 충혈이 아니라 감염, 홍채염 등 평가가 필요한 상태 가능성.',
    warn_ja: '緑内障または狭隅角がある場合は回避 — 急性閉塞隅角緑内障発作を起こす可能性。72時間後も充血が続く、痛み·視力変化·分泌物が出る場合は中止し受診 — 単純充血ではなく感染、虹彩炎など評価が必要な状態の可能性。',
    interact: [
      { en: 'MAO inhibitors — risk of hypertensive crisis from systemic absorption', ko: 'MAO 억제제 — 전신 흡수로 인한 고혈압 위기 위험', ja: 'MAO阻害薬 — 全身吸収による高血圧危機リスク' },
      { en: 'Tricyclic antidepressants — potentiated vasoconstriction', ko: '삼환계 항우울제 — 혈관수축 작용 증강', ja: '三環系抗うつ薬 — 血管収縮作用の増強' },
      { en: 'Other vasoconstrictor eye drops (naphazoline, oxymetazoline ophthalmic) — do not combine', ko: '기타 혈관수축 안약 (나파졸린, 옥시메타졸린) — 병용 금지', ja: '他の血管収縮点眼液(ナファゾリン、オキシメタゾリン眼科用) — 併用禁止' },
      { en: 'Beta-blocker eye drops (for glaucoma) — discuss with ophthalmologist', ko: '베타차단제 안약 (녹내장 치료) — 안과 의사와 상담', ja: 'βブロッカー点眼液(緑内障治療) — 眼科医と相談' }
    ],
    source: 'FDA OTC Monograph 21 CFR 349 · DailyMed (NIH) · AAPCC poison exposure reports'
  },
  {
    id: 'ketotifen',
    generic: { en: 'Ketotifen fumarate 0.025% (antihistamine eye drops)', ko: '케토티펜 푸마르산염 0.025% (항히스타민 안약)', ja: 'ケトチフェンフマル酸塩0.025%(抗ヒスタミン点眼液)' },
    brands: ['Zaditor', 'Alaway', 'Claritin Eye', 'Refresh Eye Itch Relief'],
    category: 'eye_ear',
    uses: [
      { title_en: 'Allergic itching of the eyes', title_ko: '알레르기성 눈 가려움', title_ja: 'アレルギー性のかゆみ',
        detail_en: 'H1-antihistamine plus mast cell stabilizer; relieves itching from pollen, pet dander, dust mites, mold. Onset within minutes, lasts 8–12 hours',
        detail_ko: 'H1 항히스타민 및 비만세포 안정화제; 꽃가루, 반려동물 비듬, 집먼지진드기, 곰팡이로 인한 가려움 완화. 수분 이내 효과 시작, 8~12시간 지속',
        detail_ja: 'H1抗ヒスタミン薬およびマスト細胞安定化薬;花粉、ペットのフケ、ダニ、カビによるかゆみを緩和。数分以内に効果開始、8~12時間持続' }
    ],
    dose_en: { 'Adult and child 3+': '1 drop in each affected eye every 8–12 hours', 'Max': '2 doses per day (twice daily)', 'With contact lenses': 'Remove contacts before use; wait 10 minutes before reinserting (preservative-containing products)', 'Onset': 'Itching relief within minutes; full effect in 1 hour' },
    dose_ko: { '성인 및 3세 이상': '증상이 있는 각 눈에 8~12시간마다 1방울', '최대': '하루 2회 (12시간 간격)', '콘택트렌즈 사용자': '렌즈 제거 후 사용; 10분 후 재착용 (방부제 함유 제품)', '효과 발현': '수분 이내 가려움 완화; 완전 효과 1시간' },
    dose_ja: { '成人および3歳以上': '症状のある各目に8~12時間ごとに1滴', '最大': '1日2回(12時間間隔)', 'コンタクトレンズ使用者': 'レンズを外して使用;10分後に再装着(防腐剤含有製品)', '効果発現': '数分以内にかゆみ緩和;完全な効果は1時間' },
    warn_en: 'For itching only — does not relieve redness or swelling from infection. If eye pain, vision change, severe swelling, or purulent discharge occurs, see a doctor; these are not allergy symptoms. Can be used daily throughout allergy season. Mild transient burning or stinging is common.',
    warn_ko: '가려움 전용 — 감염으로 인한 충혈·부종은 완화하지 않습니다. 눈 통증, 시력 변화, 심한 부종, 화농성 분비물이 있으면 진료; 이는 알레르기 증상이 아닙니다. 알레르기 계절 동안 매일 사용 가능. 경미한 일시적 작열감·따가움은 흔함.',
    warn_ja: 'かゆみ専用 — 感染による充血·腫れは緩和しません。目の痛み、視力変化、強い腫れ、膿性分泌物がある場合は受診;これらはアレルギー症状ではありません。アレルギー季節中は毎日使用可能。軽度の一時的灼熱感·しみる感じは一般的。',
    interact: [
      { en: 'No major systemic drug interactions (minimal systemic absorption)', ko: '주요 전신 약물 상호작용 없음 (전신 흡수 최소)', ja: '主要な全身薬物相互作用なし(全身吸収最小)' },
      { en: 'Other eye drops — separate applications by 5–10 minutes', ko: '기타 안약 — 5~10분 간격으로 투여', ja: '他の点眼液 — 5~10分間隔で投与' },
      { en: 'Contact lens solutions — do not instill over lens in most formulations', ko: '콘택트렌즈 용액 — 대부분 제형에서 렌즈 위 투여 금지', ja: 'コンタクトレンズ溶液 — ほとんどの製剤でレンズ上に点眼禁止' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH) · American Academy of Ophthalmology'
  },
  {
    id: 'naphazoline-pheniramine',
    generic: { en: 'Naphazoline + Pheniramine (allergy + redness eye drops)', ko: '나파졸린 + 페니라민 (알레르기·충혈 복합 안약)', ja: 'ナファゾリン + フェニラミン(アレルギー·充血複合点眼液)' },
    brands: ['Visine-A', 'Naphcon-A', 'Opcon-A', 'Clear Eyes Allergy'],
    category: 'eye_ear',
    uses: [
      { title_en: 'Allergic itching plus redness', title_ko: '알레르기 가려움 및 충혈', title_ja: 'アレルギーかゆみと充血',
        detail_en: 'Combines antihistamine (pheniramine) with vasoconstrictor (naphazoline); dual relief when both itching and visible redness are present. Short-term use only',
        detail_ko: '항히스타민(페니라민)과 혈관수축제(나파졸린) 복합; 가려움과 충혈이 동시에 있을 때 이중 완화. 단기 사용만',
        detail_ja: '抗ヒスタミン薬(フェニラミン)と血管収縮薬(ナファゾリン)の複合;かゆみと充血が同時にあるときの二重緩和。短期使用のみ' }
    ],
    dose_en: { 'Adult and child 6+': '1–2 drops in each affected eye up to 4 times daily', 'Max duration': '72 hours for redness component (same rebound concern as Visine)', 'Prefer ketotifen for daily allergy use': 'Single-ingredient ketotifen or olopatadine has better long-term profile' },
    dose_ko: { '성인 및 6세 이상': '증상이 있는 각 눈에 하루 4회까지 1~2방울', '최대 사용 기간': '충혈 성분 기준 72시간 (Visine과 동일한 반동 우려)', '일상 알레르기에는 케토티펜 권장': '단일 성분 케토티펜 또는 올로파타딘이 장기 사용에 적합' },
    dose_ja: { '成人および6歳以上': '症状のある各目に1日4回まで1~2滴', '最大使用期間': '充血成分基準で72時間(Visineと同じ反跳の懸念)', '日常アレルギーにはケトチフェン推奨': '単一成分ケトチフェンまたはオロパタジンが長期使用に適合' },
    danger_en: 'Same oral-ingestion toxicity as Visine — pediatric exposure can cause coma, seizures, slow heart rate. Keep away from children. Contraindicated in narrow-angle glaucoma.',
    danger_ko: 'Visine과 동일한 경구 섭취 독성 — 소아가 삼키면 혼수, 경련, 서맥 발생 가능. 소아 손이 닿지 않게 보관. 폐쇄각 녹내장 금기.',
    danger_ja: 'Visineと同じ経口摂取毒性 — 小児が飲み込むと昏睡、けいれん、徐脈の可能性。小児の手の届かない場所に保管。閉塞隅角緑内障禁忌。',
    warn_en: 'Avoid with MAO inhibitors, severe cardiovascular disease, hyperthyroidism, or high blood pressure (vasoconstrictor can raise BP). Not for long-term allergy management — switch to single-agent antihistamine drop (ketotifen, olopatadine) or intranasal steroid.',
    warn_ko: 'MAO 억제제, 중증 심혈관 질환, 갑상선 기능 항진증, 고혈압 환자에서는 피하세요 (혈관수축제가 혈압 상승 가능). 장기 알레르기 관리용 아님 — 단일 성분 항히스타민 안약(케토티펜, 올로파타딘) 또는 비강 스테로이드로 전환.',
    warn_ja: 'MAO阻害薬、重度心血管疾患、甲状腺機能亢進症、高血圧患者では回避(血管収縮薬で血圧上昇の可能性)。長期アレルギー管理用ではない — 単一成分抗ヒスタミン点眼液(ケトチフェン、オロパタジン)または鼻ステロイドに切り替え。',
    interact: [
      { en: 'MAO inhibitors — hypertensive crisis risk', ko: 'MAO 억제제 — 고혈압 위기 위험', ja: 'MAO阻害薬 — 高血圧危機リスク' },
      { en: 'Tricyclic antidepressants — potentiated vasoconstriction', ko: '삼환계 항우울제 — 혈관수축 증강', ja: '三環系抗うつ薬 — 血管収縮の増強' },
      { en: 'Beta-blockers — blunted response; discuss with doctor', ko: '베타차단제 — 반응 둔화; 의사 상담', ja: 'βブロッカー — 反応鈍化;医師相談' },
      { en: 'Other vasoconstrictor drops — do not combine', ko: '기타 혈관수축 안약 — 병용 금지', ja: '他の血管収縮点眼液 — 併用禁止' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'swimmers-ear-drops',
    generic: { en: "Swimmer's ear drops (isopropyl alcohol + glycerin)", ko: '수영자 귀 드롭 (이소프로필 알코올 + 글리세린)', ja: 'スイマーズイヤー点耳薬(イソプロピルアルコール+グリセリン)' },
    brands: ['Swim-EAR', 'Auro-Dri', 'Ear Drops by Debrox (drying formula)'],
    category: 'eye_ear',
    uses: [
      { title_en: 'Prevention of swimmer\'s ear (otitis externa)', title_ko: '수영자 귀(외이도염) 예방', title_ja: 'スイマーズイヤー(外耳炎)の予防',
        detail_en: 'Isopropyl alcohol (95%) with anhydrous glycerin dries residual water in the ear canal and lowers pH, inhibiting bacterial and fungal growth. Preventive use after swimming, bathing, or sweating in humid climates',
        detail_ko: '이소프로필 알코올(95%)과 무수 글리세린이 외이도에 남은 물을 건조시키고 pH를 낮춰 세균·진균 성장 억제. 수영, 목욕 또는 습한 기후에서 땀을 흘린 후 예방 목적으로 사용',
        detail_ja: 'イソプロピルアルコール(95%)と無水グリセリンが外耳道に残った水を乾燥させpHを下げ、細菌·真菌の増殖を抑制。水泳、入浴、または湿潤環境での発汗後に予防目的で使用' }
    ],
    dose_en: { 'Prevention after water exposure': '4–5 drops in each ear after swimming/bathing, then tilt head to drain', 'Frequency': 'Each time water enters the ear', 'Age': 'Adults and children; for young children use under adult supervision' },
    dose_ko: { '물 노출 후 예방': '수영·목욕 후 각 귀에 4~5방울 투여, 고개를 기울여 배출', '빈도': '물이 귀에 들어갈 때마다', '연령': '성인 및 소아; 어린이는 보호자 감독 하에 사용' },
    dose_ja: { '水曝露後の予防': '水泳·入浴後、各耳に4~5滴点耳し、頭を傾けて排出', '頻度': '耳に水が入るたび', '年齢': '成人および小児;幼児は保護者監督下で使用' },
    danger_en: 'DO NOT USE if you have an active ear infection, pain, drainage, or a perforated eardrum — alcohol on a ruptured eardrum causes severe pain and can damage middle/inner ear structures. If in doubt whether the eardrum is intact (e.g., after recent ear infection or ear tube surgery), see a doctor first.',
    danger_ko: '현재 귀 감염, 통증, 분비물 또는 고막 천공이 있으면 사용하지 마세요 — 천공된 고막에 알코올이 닿으면 심한 통증과 중이·내이 구조 손상 가능. 고막이 온전한지 확실하지 않으면(예: 최근 귀 감염 또는 환기관 수술 후) 먼저 진료.',
    danger_ja: '現在の耳感染、痛み、分泌物、または鼓膜穿孔がある場合は使用禁止 — 穿孔した鼓膜にアルコールが触れると激しい痛みと中耳·内耳構造の損傷の可能性。鼓膜が無傷か不明な場合(例:最近の耳感染や換気チューブ手術後)はまず受診。',
    warn_en: 'Does not treat established otitis externa — that requires antibiotic ear drops (prescription). Pain, swelling, drainage, hearing loss, or fever means infection — see a doctor. Not for use with ear tubes in children without ENT advice.',
    warn_ko: '이미 발생한 외이도염은 치료하지 않습니다 — 항생제 귀 드롭(처방) 필요. 통증, 부종, 분비물, 청력 저하, 발열은 감염을 의미 — 진료. 소아 환기관 삽입 시 이비인후과 의사 조언 없이 사용 금지.',
    warn_ja: 'すでに発症した外耳炎は治療しません — 抗生物質点耳薬(処方)が必要。痛み、腫脹、分泌物、難聴、発熱は感染を意味 — 受診。小児の換気チューブ挿入時は耳鼻科医の助言なく使用禁止。',
    interact: [
      { en: 'Topical use only — no systemic drug interactions', ko: '외용 전용 — 전신 약물 상호작용 없음', ja: '外用のみ — 全身薬物相互作用なし' },
      { en: 'Prescription antibiotic ear drops — do not mix; separate by several hours if both needed', ko: '처방 항생제 귀 드롭 — 혼합 금지; 둘 다 필요하면 수시간 간격', ja: '処方抗生物質点耳薬 — 混合禁止;両方必要なら数時間間隔' }
    ],
    source: 'CDC · AAO-HNS Clinical Practice Guideline on Otitis Externa · DailyMed (NIH)'
  },
  {
    id: 'pink-eye-otc-caution',
    generic: { en: 'Pink eye (conjunctivitis) — OTC guidance and limits', ko: '결막염(핑크아이) — OTC 지침과 한계', ja: '結膜炎(ピンクアイ) — OTC指針と限界' },
    brands: ['(no OTC cure — symptomatic products: artificial tears, cool compresses)'],
    category: 'eye_ear',
    uses: [
      { title_en: 'Symptomatic relief for viral or allergic conjunctivitis', title_ko: '바이러스성·알레르기성 결막염의 대증 완화', title_ja: 'ウイルス性·アレルギー性結膜炎の対症緩和',
        detail_en: 'Most pink eye in adults is viral (self-limited, 7–14 days); in children bacterial is more common. OTC options provide symptom relief only: artificial tears for irritation, cold compresses for swelling, antihistamine drops (ketotifen) if allergic. Bacterial conjunctivitis requires prescription antibiotic drops',
        detail_ko: '성인 결막염은 대부분 바이러스성(자가 회복, 7~14일); 소아에서는 세균성이 더 흔함. OTC 옵션은 증상 완화만 제공: 자극에 인공눈물, 부종에 냉찜질, 알레르기성이면 항히스타민 안약(케토티펜). 세균성 결막염은 처방 항생제 안약 필요',
        detail_ja: '成人の結膜炎の多くはウイルス性(自然軽快、7~14日);小児では細菌性がより一般的。OTC選択肢は症状緩和のみ:刺激には人工涙液、腫脹には冷湿布、アレルギー性ならば抗ヒスタミン点眼薬(ケトチフェン)。細菌性結膜炎は処方抗生物質点眼薬が必要' }
    ],
    dose_en: { 'Artificial tears': 'As needed for irritation (preservative-free preferred)', 'Cold compress': '5–10 minutes several times daily', 'Ketotifen (if allergic)': '1 drop each eye twice daily', 'Hand hygiene': 'Wash hands frequently; do not share towels or pillows; stop contact lens use until resolved' },
    dose_ko: { '인공눈물': '자극에 따라 필요시 (방부제 무첨가 권장)', '냉찜질': '하루 수회 5~10분', '케토티펜 (알레르기성)': '각 눈에 하루 2회 1방울', '위생': '손을 자주 씻고 수건·베개 공유 금지; 호전까지 콘택트렌즈 중단' },
    dose_ja: { '人工涙液': '刺激に応じて必要時(無防腐剤推奨)', '冷湿布': '1日数回、5~10分', 'ケトチフェン(アレルギー性)': '各眼1日2回1滴', '衛生': '頻繁に手洗い;タオル·枕を共有しない;軽快までコンタクトレンズ中止' },
    danger_en: 'DO NOT USE VISINE OR OTHER REDNESS-RELIEF DROPS to "hide" pink eye — it does not treat the cause and worsens symptoms on withdrawal. Warning signs requiring urgent care: severe eye pain, vision change, light sensitivity, pupil size difference, contact lens wearer with pain — possible keratitis, iritis, or acanthamoeba infection (contact lens wearers are especially high risk). Newborns with pink eye need immediate evaluation.',
    danger_ko: '결막염을 "가리려고" Visine이나 기타 충혈 완화 안약 사용 금지 — 원인 치료가 안 되고 중단 시 증상 악화. 응급 진료가 필요한 경고 징후: 심한 눈 통증, 시력 변화, 빛 과민, 동공 크기 차이, 콘택트렌즈 착용자의 통증 — 각막염, 홍채염 또는 아칸트아메바 감염 가능성(콘택트렌즈 착용자 특히 고위험). 신생아 결막염은 즉시 평가 필요.',
    danger_ja: '結膜炎を「隠す」ためにVisineや他の充血除去点眼薬を使用しない — 原因治療にならず中止時に症状悪化。緊急受診が必要な警告徴候:激しい眼痛、視力変化、光過敏、瞳孔不同、コンタクトレンズ装用者の痛み — 角膜炎、虹彩炎、またはアカントアメーバ感染の可能性(コンタクトレンズ装用者は特に高リスク)。新生児の結膜炎は即時評価必要。',
    warn_en: 'Bacterial vs viral vs allergic pink eye can be hard to distinguish. Purulent (thick yellow/green) discharge favors bacterial; watery discharge with cold symptoms favors viral; itching with bilateral involvement favors allergic. Doctor evaluation recommended for: infants/newborns, severe symptoms, contact lens wearers, symptoms persisting >1 week, or anyone with eye pain or vision change.',
    warn_ko: '세균성·바이러스성·알레르기성 결막염 구별이 어려울 수 있음. 화농성(짙은 노랑·초록) 분비물은 세균성; 감기 증상과 함께 맑은 분비물은 바이러스성; 양측성 가려움은 알레르기성을 시사. 진료 권장: 영아·신생아, 중증 증상, 콘택트렌즈 착용자, 1주 이상 지속 증상, 또는 눈 통증·시력 변화가 있는 모든 경우.',
    warn_ja: '細菌性·ウイルス性·アレルギー性結膜炎の区別は困難な場合あり。膿性(濃い黄·緑)分泌物は細菌性を示唆;かぜ症状を伴う水様分泌物はウイルス性;両側性のかゆみはアレルギー性を示唆。受診推奨:乳児·新生児、重症、コンタクトレンズ装用者、1週間以上続く症状、または眼痛·視力変化のある全例。',
    interact: [
      { en: 'Corticosteroid eye drops — do not self-treat; can worsen herpes keratitis or fungal infection', ko: '스테로이드 안약 — 자가 치료 금지; 헤르페스 각막염 또는 진균 감염을 악화시킬 수 있음', ja: 'ステロイド点眼薬 — 自己治療禁止;ヘルペス角膜炎や真菌感染を悪化させる可能性' },
      { en: 'Old or shared eye drops — contamination risk; discard eye medications after eye infection resolves', ko: '오래된 또는 공유한 안약 — 오염 위험; 눈 감염 호전 후 안약 폐기', ja: '古い、または共有した点眼薬 — 汚染リスク;眼感染軽快後に点眼薬を廃棄' }
    ],
    source: 'American Academy of Ophthalmology Clinical Statement · CDC guidance on Conjunctivitis · AAP'
  },

  // ============ ORAL & DENTAL ============
  {
    id: 'benzocaine-oral',
    generic: { en: 'Benzocaine oral gel (toothache, teething)', ko: '벤조카인 구강 젤 (치통·이앓이)', ja: 'ベンゾカイン口腔ゲル(歯痛·歯ぐずり)' },
    brands: ['Orajel', 'Anbesol', 'Kank-A', 'HurriCaine'],
    category: 'oral',
    uses: [
      { title_en: 'Temporary relief of toothache, gum pain, canker sores', title_ko: '치통·잇몸 통증·구내염의 일시적 완화', title_ja: '歯痛·歯肉痛·口内炎の一時的緩和',
        detail_en: 'Topical local anesthetic; numbs oral mucosa within 30 seconds for 15–20 minutes. Used for dental pain while awaiting dental appointment, denture irritation, or mouth sores',
        detail_ko: '국소 마취제; 30초 이내 구강 점막을 마비시켜 15~20분간 효과. 치과 진료 대기 중 치통, 의치 자극, 구내염에 사용',
        detail_ja: '局所麻酔薬;30秒以内に口腔粘膜を麻痺させ15~20分間効果。歯科受診待ちの歯痛、義歯刺激、口内炎に使用' },
      { title_en: 'Sore throat (benzocaine lozenges)', title_ko: '인후통 (벤조카인 로젠지)', title_ja: '咽頭痛(ベンゾカイントローチ)',
        detail_en: 'Also available as lozenges and sprays for sore throat — see separate Benzocaine lozenge entry',
        detail_ko: '인후통용 로젠지·스프레이로도 판매 — 별도 벤조카인 로젠지 항목 참고',
        detail_ja: '咽頭痛用トローチ·スプレーも販売 — 別項のベンゾカイントローチを参照' }
    ],
    dose_en: { 'Adult and child 2+': 'Apply small amount to affected area up to 4 times daily', 'Duration': 'Not more than 7 days without dental evaluation', 'Under 2 years': 'DO NOT USE — FDA warning against benzocaine for teething in infants and toddlers', 'Denture wearers': 'Apply to sore spot; see dentist if irritation persists >3 days' },
    dose_ko: { '성인 및 2세 이상': '해당 부위에 하루 4회까지 소량 도포', '사용 기간': '치과 진료 없이 7일 초과 사용 금지', '2세 미만': '사용 금지 — FDA는 영·유아 이앓이에 벤조카인 사용을 경고', '의치 착용자': '통증 부위에 도포; 3일 이상 자극 지속 시 치과 진료' },
    dose_ja: { '成人および2歳以上': '患部に1日4回まで少量塗布', '使用期間': '歯科評価なく7日超使用禁止', '2歳未満': '使用禁止 — FDAは乳幼児の歯ぐずりへのベンゾカイン使用を警告', '義歯装着者': '痛い部位に塗布;3日以上刺激が続く場合は歯科受診' },
    danger_en: 'METHEMOGLOBINEMIA RISK — benzocaine can convert hemoglobin to methemoglobin, reducing oxygen delivery; deaths have occurred, especially in infants and small children. FDA has strong warning against use in children under 2 for teething. Symptoms of methemoglobinemia: pale/gray/blue skin or lips, headache, rapid heart rate, shortness of breath, fatigue — seek EMERGENCY care if these occur.',
    danger_ko: '메트헤모글로빈혈증 위험 — 벤조카인은 헤모글로빈을 메트헤모글로빈으로 전환시켜 산소 전달을 감소; 특히 영·유아에서 사망 사례 발생. FDA는 2세 미만 이앓이 사용에 강한 경고. 메트헤모글로빈혈증 증상: 창백·회색·청색 피부나 입술, 두통, 빠른 심박수, 호흡곤란, 피로 — 이런 증상 시 즉시 응급 진료.',
    danger_ja: 'メトヘモグロビン血症のリスク — ベンゾカインはヘモグロビンをメトヘモグロビンに変換し酸素運搬を低下;特に乳幼児·小児で死亡例。FDAは2歳未満の歯ぐずりへの使用に強い警告。メトヘモグロビン血症の症状:蒼白·灰色·青色の皮膚や唇、頭痛、頻脈、呼吸困難、疲労 — これらが現れたら即時救急受診。',
    warn_en: 'Do not use on extensive wounds or if allergic to ester-type local anesthetics (procaine, tetracaine). Persistent dental pain, swelling, fever, or foul taste means infection — see a dentist; benzocaine only masks symptoms. Avoid use with aspirin or ibuprofen directly on gum tissue (causes chemical burns — a common myth that should be avoided).',
    warn_ko: '광범위한 상처에 사용 금지; 에스테르형 국소 마취제(프로카인, 테트라카인) 알레르기 시 금기. 지속되는 치통, 부종, 발열, 악취는 감염 신호 — 치과 진료; 벤조카인은 증상만 가립니다. 아스피린·이부프로펜을 잇몸에 직접 대는 속설은 피하세요(화학 화상 유발).',
    warn_ja: '広範な創傷には使用禁止;エステル型局所麻酔薬(プロカイン、テトラカイン)アレルギー時は禁忌。持続する歯痛、腫脹、発熱、悪臭は感染の徴候 — 歯科受診;ベンゾカインは症状を覆い隠すだけ。アスピリン·イブプロフェンを歯肉に直接当てる俗説は避ける(化学熱傷を起こす)。',
    interact: [
      { en: 'Other local anesthetics — additive systemic toxicity if used excessively', ko: '기타 국소 마취제 — 과다 사용 시 전신 독성 누적', ja: '他の局所麻酔薬 — 過剰使用で全身毒性累積' },
      { en: 'Sulfonamide antibiotics — both can cause methemoglobinemia', ko: '설폰아미드계 항생제 — 양쪽 모두 메트헤모글로빈혈증 유발 가능', ja: 'スルホンアミド系抗生物質 — 双方ともメトヘモグロビン血症を起こす可能性' },
      { en: 'Dapsone, nitrates, phenazopyridine — increased methemoglobinemia risk', ko: '댑손, 질산염, 페나조피리딘 — 메트헤모글로빈혈증 위험 증가', ja: 'ダプソン、硝酸塩、フェナゾピリジン — メトヘモグロビン血症リスク増加' }
    ],
    source: 'FDA Drug Safety Communication 2018 · DailyMed (NIH)'
  },
  {
    id: 'fluoride-rinse',
    generic: { en: 'Fluoride mouth rinse (0.05% sodium fluoride)', ko: '불소 구강 린스 (0.05% 불화나트륨)', ja: 'フッ化物洗口液(0.05%フッ化ナトリウム)' },
    brands: ['ACT Anticavity Fluoride Rinse', 'Colgate Phos-Flur', 'Listerine Total Care Anticavity'],
    category: 'oral',
    uses: [
      { title_en: 'Cavity prevention', title_ko: '충치 예방', title_ja: 'むし歯予防',
        detail_en: 'Supplement to fluoride toothpaste for adults and children at higher risk of cavities: dry mouth, orthodontic appliances, frequent snacking, exposed root surfaces in older adults. Remineralizes early enamel decay',
        detail_ko: '불소 치약에 보조; 충치 위험이 높은 성인·소아에 사용: 구강건조, 교정장치, 잦은 간식, 노년층의 치근 노출. 초기 법랑질 탈회를 재광화',
        detail_ja: 'フッ化物配合歯磨剤の補助;むし歯リスクが高い成人·小児に使用:口腔乾燥、矯正装置、頻繁な間食、高齢者の歯根露出。初期エナメル質脱灰を再石灰化' }
    ],
    dose_en: { 'Age 6+': 'Rinse with 10 mL (2 teaspoons) for 1 minute, then spit out; once daily, typically at bedtime', 'Do not eat or drink': 'For 30 minutes after rinsing', 'Under 6 years': 'Do not use — children may swallow the rinse; use fluoride toothpaste under supervision instead', 'Swallowing warning': 'Not for swallowing; if more than 10 mL swallowed, seek emergency care (esp. children)' },
    dose_ko: { '6세 이상': '10 mL(2 티스푼)로 1분간 가글 후 뱉음; 하루 1회, 보통 취침 시', '먹거나 마시지 않기': '가글 후 30분간', '6세 미만': '사용 금지 — 어린이가 삼킬 수 있음; 대신 보호자 감독 하 불소 치약 사용', '삼킴 경고': '삼키지 않기; 10 mL 이상 삼킨 경우 응급 진료 (특히 소아)' },
    dose_ja: { '6歳以上': '10 mL(小さじ2杯)で1分間うがいし吐き出す;1日1回、通常就寝時', '飲食禁止': 'うがい後30分', '6歳未満': '使用禁止 — 小児が飲み込む可能性;代わりに保護者監督下でフッ化物配合歯磨剤を使用', '誤飲警告': '飲み込み禁止;10 mL以上飲み込んだ場合は救急受診(特に小児)' },
    danger_en: 'ACUTE FLUORIDE POISONING from swallowing large amounts (especially in children): nausea, vomiting, abdominal pain, muscle weakness, seizures. As little as 5–10 mg/kg can cause symptoms; 16 mg/kg can be fatal in children. Keep bottle out of reach of children under 6. Lifetime excessive fluoride can cause dental fluorosis (cosmetic white spots) — not from appropriate use but from ingesting toothpaste/rinse.',
    danger_ko: '어린이가 다량 삼킬 시 급성 불소 중독 — 메스꺼움, 구토, 복통, 근력 저하, 경련. 체중 kg당 5~10 mg만으로도 증상 발생; 16 mg/kg는 소아에서 치명적 가능. 6세 미만 손이 닿지 않게 보관. 평생 과잉 불소는 치아 불소증(미용적 흰 반점) 유발 — 적절한 사용이 아닌 치약·린스를 삼킬 때 발생.',
    danger_ja: '小児が大量誤飲した場合、急性フッ化物中毒 — 吐き気、嘔吐、腹痛、筋力低下、けいれん。体重kg当たり5~10 mgで症状;16 mg/kgは小児で致命的の可能性。6歳未満の手の届かない場所に保管。生涯にわたる過剰フッ化物は歯のフッ素症(美容的な白斑)を起こす — 適切な使用ではなく歯磨剤·洗口液の誤飲による。',
    warn_en: 'Not a substitute for brushing and flossing. Do not rinse with water after — water washes away the fluoride. Regular dental visits still needed for cleaning and cavity detection. Some rinses contain alcohol (can worsen dry mouth); alcohol-free versions available.',
    warn_ko: '양치질과 치실질을 대체하지 않습니다. 사용 후 물로 헹구지 마세요 — 물이 불소를 씻어냅니다. 스케일링과 충치 검사를 위해 정기 치과 방문 필요. 일부 린스에는 알코올 함유(구강건조 악화 가능); 무알코올 제품 선택 가능.',
    warn_ja: '歯磨きとデンタルフロスの代替ではない。使用後に水ですすがない — 水がフッ化物を洗い流す。クリーニングとむし歯検査のため定期歯科受診が必要。一部の洗口液はアルコール含有(口腔乾燥を悪化させる可能性);ノンアルコール製品選択可能。',
    interact: [
      { en: 'Calcium, magnesium, aluminum supplements — can reduce fluoride absorption; separate by 1–2 hours', ko: '칼슘, 마그네슘, 알루미늄 보충제 — 불소 흡수 감소 가능; 1~2시간 간격', ja: 'カルシウム、マグネシウム、アルミニウムサプリメント — フッ化物吸収を減少させる可能性;1~2時間間隔' },
      { en: 'Dairy products (rinsing after eating dairy may reduce fluoride deposition on teeth)', ko: '유제품 (유제품 섭취 후 바로 가글 시 치아 불소 침착 감소 가능)', ja: '乳製品(乳製品摂取直後のうがいで歯へのフッ化物沈着が減る可能性)' },
      { en: 'Other fluoride products (toothpaste is normal; avoid multiple rinses)', ko: '기타 불소 제품 (치약과 병용은 정상; 여러 린스 동시 사용 금지)', ja: '他のフッ化物製品(歯磨剤との併用は通常;複数の洗口液同時使用禁止)' }
    ],
    source: 'FDA OTC Monograph 21 CFR 355 · ADA · CDC Community Water Fluoridation'
  },
  {
    id: 'peroxyl-rinse',
    generic: { en: 'Hydrogen peroxide 1.5% oral rinse', ko: '과산화수소 1.5% 구강 린스', ja: '過酸化水素1.5%口腔洗口液' },
    brands: ['Colgate Peroxyl', 'Orajel Antiseptic Mouth Sore Rinse', 'generic hydrogen peroxide (diluted)'],
    category: 'oral',
    uses: [
      { title_en: 'Minor oral wounds, canker sores, post-dental surgery rinse', title_ko: '경미한 구강 상처·구내염·치과 수술 후 세정', title_ja: '軽度の口腔創傷·口内炎·歯科手術後の洗浄',
        detail_en: 'Releases oxygen on contact with tissue enzymes, providing mechanical debridement and mild antimicrobial action. Often recommended after tooth extraction, for canker sores, minor mouth irritation, or orthodontic appliance irritation',
        detail_ko: '조직 효소와 접촉 시 산소를 방출하여 기계적 세정 및 경미한 항균 작용. 발치 후, 구내염, 경미한 구강 자극, 교정장치 자극에 권장',
        detail_ja: '組織酵素との接触で酸素を放出し機械的洗浄および軽度の抗菌作用。抜歯後、口内炎、軽度の口腔刺激、矯正装置刺激に推奨' }
    ],
    dose_en: { 'Adult and child 6+': 'Dilute 1:1 with water, swish 10 mL for 1 minute, then spit', 'Frequency': 'Up to 4 times daily after meals and at bedtime', 'Duration': 'Not more than 7 days — prolonged use can disrupt oral microbiome and delay healing', 'For children 2–6': 'Only under adult supervision; use smaller volume' },
    dose_ko: { '성인 및 6세 이상': '물과 1:1 희석 후 10 mL를 1분간 가글 후 뱉음', '빈도': '식후와 취침 시 하루 최대 4회', '사용 기간': '7일 초과 금지 — 장기 사용은 구강 미생물 균형을 깨고 치유를 지연', '2~6세 소아': '보호자 감독 하에만; 소량 사용' },
    dose_ja: { '成人および6歳以上': '水で1:1に希釈し10 mLを1分間うがいして吐き出す', '頻度': '食後と就寝時、1日最大4回', '使用期間': '7日超禁止 — 長期使用は口腔細菌叢を乱し治癒を遅延', '2~6歳小児': '保護者監督下のみ;少量使用' },
    warn_en: 'DO NOT SWALLOW — concentrated hydrogen peroxide can cause chemical burns, air embolism, or severe GI injury. Foaming is normal and indicates reaction with tissue. Prolonged use can cause black hairy tongue (harmless but cosmetic). Persistent mouth pain, ulcers that don\'t heal in 2 weeks, or bleeding gums warrant dental evaluation — may be oral cancer, severe periodontitis, or other condition.',
    warn_ko: '삼키지 마세요 — 농축 과산화수소는 화학 화상, 공기 색전증 또는 중증 위장 손상 유발 가능. 거품은 정상이며 조직 반응을 의미. 장기 사용 시 흑모설(무해하나 미용적) 발생 가능. 2주 이상 낫지 않는 궤양, 지속적인 구강 통증, 잇몸 출혈은 치과 평가 필요 — 구강암, 중증 치주염 등 가능성.',
    warn_ja: '飲み込まない — 濃縮過酸化水素は化学熱傷、空気塞栓、重度消化管損傷を起こす可能性。発泡は正常で組織反応を示す。長期使用で黒毛舌(無害だが美容的)の可能性。2週間以上治らない潰瘍、持続する口腔痛、歯肉出血は歯科評価が必要 — 口腔がん、重度歯周炎などの可能性。',
    interact: [
      { en: 'Whitening toothpastes and products — additive bleaching effect; may cause sensitivity', ko: '미백 치약 및 제품 — 표백 작용 가중; 지각 과민 유발 가능', ja: 'ホワイトニング歯磨剤·製品 — 漂白作用累積;知覚過敏を起こす可能性' },
      { en: 'Chlorhexidine rinse — do not use simultaneously; separate by at least 30 minutes', ko: '클로르헥시딘 린스 — 동시 사용 금지; 최소 30분 간격', ja: 'クロルヘキシジン洗口液 — 同時使用禁止;最低30分間隔' }
    ],
    source: 'ADA · FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'antiseptic-mouthwash',
    generic: { en: 'Antiseptic mouthwash (essential oils + ethanol)', ko: '살균 구강청결제 (에센셜 오일 + 에탄올)', ja: '殺菌うがい薬(エッセンシャルオイル+エタノール)' },
    brands: ['Listerine Original', 'Listerine Cool Mint Antiseptic', 'Scope (cetylpyridinium chloride)', 'Crest Pro-Health'],
    category: 'oral',
    uses: [
      { title_en: 'Plaque and gingivitis reduction', title_ko: '치태·치은염 감소', title_ja: '歯垢·歯肉炎の減少',
        detail_en: 'Essential oils (thymol, eucalyptol, menthol, methyl salicylate) or cetylpyridinium chloride (CPC) reduce bacterial load; ADA Seal of Acceptance studies show ~25% reduction in plaque and gingivitis with twice-daily use adjunct to brushing/flossing',
        detail_ko: '에센셜 오일(티몰, 유칼립톨, 멘톨, 메틸살리실산) 또는 염화세틸피리디늄(CPC)이 세균량 감소; ADA 승인 마크 연구에서 양치·치실질 보조로 하루 2회 사용 시 치태·치은염 약 25% 감소',
        detail_ja: 'エッセンシャルオイル(チモール、ユーカリプトール、メントール、サリチル酸メチル)またはセチルピリジニウム塩化物(CPC)が細菌量を減少;ADA承認マーク研究で歯磨き·フロス補助として1日2回使用で歯垢·歯肉炎が約25%減少' },
      { title_en: 'Bad breath (halitosis) reduction', title_ko: '구취 감소', title_ja: '口臭の減少',
        detail_en: 'Temporarily reduces volatile sulfur compounds produced by oral bacteria; effect lasts 3–6 hours',
        detail_ko: '구강 세균이 생성하는 휘발성 황화합물을 일시적으로 감소; 효과는 3~6시간 지속',
        detail_ja: '口腔細菌が産生する揮発性硫黄化合物を一時的に減少;効果は3~6時間持続' }
    ],
    dose_en: { 'Adult and child 12+': 'Rinse with 20 mL (4 tsp) full-strength for 30 seconds, twice daily', 'Do not dilute': 'Full strength is needed for antimicrobial effect', 'Do not swallow': 'High alcohol content (21–27% in Listerine Original)', 'Wait after brushing': 'Sodium lauryl sulfate in toothpaste can inactivate CPC; rinse or wait 30 minutes' },
    dose_ko: { '성인 및 12세 이상': '원액 20 mL(4 티스푼)로 30초간 하루 2회 가글', '희석 금지': '항균 효과에 원액 필요', '삼킴 금지': '에탄올 함량 높음 (Listerine Original 21~27%)', '양치질 후 대기': '치약의 라우릴황산나트륨이 CPC를 비활성화; 헹구거나 30분 대기' },
    dose_ja: { '成人および12歳以上': '原液20 mL(小さじ4杯)で30秒間1日2回うがい', '希釈禁止': '抗菌効果には原液が必要', '飲み込み禁止': 'エタノール含量高い(Listerine Original 21~27%)', '歯磨き後の待機': '歯磨剤のラウリル硫酸ナトリウムがCPCを失活;すすぐか30分待つ' },
    warn_en: 'High ethanol content — children can develop acute alcohol intoxication from ingestion (seizures, hypoglycemia); keep out of reach. Not a substitute for brushing and flossing. Alcohol-based rinses dry out the mouth, which can increase cavity risk in dry-mouth patients — alcohol-free alternatives are available. Some rinses stain teeth with long-term use (especially chlorhexidine-based prescription rinses; less with OTC).',
    warn_ko: '에탄올 함량 높음 — 어린이가 섭취 시 급성 알코올 중독(경련, 저혈당) 가능; 손이 닿지 않게 보관. 양치·치실질을 대체하지 않음. 알코올 기반 린스는 입안을 건조시켜 구강건조 환자의 충치 위험 증가 — 무알코올 제품 선택 가능. 일부 린스는 장기 사용 시 치아 착색(특히 처방 클로르헥시딘 린스; OTC는 덜함).',
    warn_ja: 'エタノール含量高い — 小児が摂取すると急性アルコール中毒(けいれん、低血糖)の可能性;手の届かない場所に保管。歯磨き·フロスの代替ではない。アルコールベースの洗口液は口腔を乾燥させ、口腔乾燥患者のむし歯リスクを増加 — ノンアルコール選択肢あり。一部の洗口液は長期使用で歯を着色(特に処方クロルヘキシジン;OTCは少ない)。',
    interact: [
      { en: 'Toothpaste sodium lauryl sulfate — reduces cetylpyridinium chloride effectiveness', ko: '치약의 라우릴황산나트륨 — CPC 효과 감소', ja: '歯磨剤のラウリル硫酸ナトリウム — CPC効果を減少' },
      { en: 'Disulfiram (Antabuse) — alcohol-based mouthwash can trigger reaction; use alcohol-free', ko: '디설피람 (Antabuse) — 알코올 린스가 반응 유발 가능; 무알코올 사용', ja: 'ジスルフィラム(アンタビュース) — アルコールベース洗口液が反応を起こす可能性;ノンアルコールを使用' },
      { en: 'Methotrexate — limited data; some reports of oral mucositis worsening', ko: '메토트렉세이트 — 자료 제한적; 구강 점막염 악화 보고 있음', ja: 'メトトレキサート — データ限定的;口腔粘膜炎悪化の報告あり' }
    ],
    source: 'ADA Council on Scientific Affairs · FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'biotene',
    generic: { en: 'Dry mouth (xerostomia) products', ko: '구강건조증 (제로스토미아) 제품', ja: '口腔乾燥症(キセロストミア)製品' },
    brands: ['Biotene (rinse, spray, gel, toothpaste)', 'Oasis', 'ACT Dry Mouth', 'XyliMelts'],
    category: 'oral',
    uses: [
      { title_en: 'Dry mouth symptom relief', title_ko: '구강건조 증상 완화', title_ja: '口腔乾燥症状の緩和',
        detail_en: 'Moisturizing rinses, sprays, and gels for dry mouth caused by medications, Sjögren\'s syndrome, diabetes, radiation to head/neck, aging. Contain carboxymethylcellulose, glycerin, xylitol, or salivary enzymes (lactoperoxidase)',
        detail_ko: '약물, 쇼그렌 증후군, 당뇨, 두경부 방사선 치료, 노화로 인한 구강건조 대상; 카르복시메틸셀룰로스, 글리세린, 자일리톨, 타액 효소(락토퍼옥시다제) 함유 보습 린스·스프레이·젤',
        detail_ja: '薬物、シェーグレン症候群、糖尿病、頭頸部放射線、加齢による口腔乾燥対象;カルボキシメチルセルロース、グリセリン、キシリトール、唾液酵素(ラクトペルオキシダーゼ)を含む保湿洗口液·スプレー·ジェル' },
      { title_en: 'Cavity risk reduction in dry mouth', title_ko: '구강건조 환자의 충치 위험 감소', title_ja: '口腔乾燥患者のむし歯リスク減少',
        detail_en: 'Xylitol-containing products have antimicrobial effects against Streptococcus mutans; helpful when reduced saliva no longer buffers acids. Often used with high-fluoride toothpaste (prescription 5000 ppm)',
        detail_ko: '자일리톨 함유 제품은 뮤탄스 연쇄구균에 항균 작용; 타액 감소로 산 완충이 안 될 때 도움. 보통 고농도 불소 치약(처방 5000 ppm)과 병용',
        detail_ja: 'キシリトール含有製品はミュータンス菌に抗菌作用;唾液減少で酸の緩衝ができない場合に有用。通常高濃度フッ化物歯磨剤(処方5000 ppm)と併用' }
    ],
    dose_en: { 'Rinse': '10–15 mL swish for 30 seconds, up to 5 times daily; do not rinse with water after', 'Spray/gel': 'Apply to oral tissues as needed throughout the day and at bedtime', 'XyliMelts (adherent disc)': 'Place on upper molar gum; dissolves over 6–8 hours — useful for nighttime dryness', 'Sugar-free gum with xylitol': 'Stimulates residual saliva production; chew for 10–20 minutes after meals' },
    dose_ko: { '린스': '10~15 mL로 30초 가글, 하루 최대 5회; 사용 후 물로 헹구지 않음', '스프레이/젤': '하루 종일 그리고 취침 시 필요에 따라 구강 조직에 도포', 'XyliMelts (접착 디스크)': '위쪽 어금니 잇몸에 부착; 6~8시간에 걸쳐 용해 — 야간 건조에 유용', '자일리톨 함유 무설탕 껌': '잔여 타액 생성 촉진; 식후 10~20분 씹기' },
    dose_ja: { '洗口液': '10~15 mLで30秒うがい、1日最大5回;後で水ですすがない', 'スプレー/ジェル': '日中と就寝時、必要に応じて口腔組織に塗布', 'XyliMelts(接着ディスク)': '上の臼歯歯肉に貼付;6~8時間かけて溶解 — 夜間の乾燥に有用', 'キシリトール無糖ガム': '残存唾液分泌を刺激;食後10~20分噛む' },
    warn_en: 'Identify and address the cause — common culprits are anticholinergic medications (diphenhydramine, oxybutynin, tricyclic antidepressants), diuretics, radiation, uncontrolled diabetes, Sjögren\'s syndrome, dehydration. Dry mouth greatly increases cavity, gum disease, and oral infection risk — see dentist every 3–6 months. Avoid mouthwashes with alcohol and products with sugar (including many lozenges).',
    warn_ko: '원인을 찾아 해결 — 흔한 원인: 항콜린 약물(디펜히드라민, 옥시부티닌, 삼환계 항우울제), 이뇨제, 방사선, 조절되지 않은 당뇨, 쇼그렌 증후군, 탈수. 구강건조는 충치·치주질환·구강감염 위험을 크게 증가 — 3~6개월마다 치과 방문. 알코올 함유 구강청결제와 당분 함유 제품(많은 로젠지 포함) 피하세요.',
    warn_ja: '原因を特定し対処 — 一般的な原因:抗コリン薬(ジフェンヒドラミン、オキシブチニン、三環系抗うつ薬)、利尿薬、放射線、コントロール不良の糖尿病、シェーグレン症候群、脱水。口腔乾燥はむし歯·歯周病·口腔感染リスクを大きく増加 — 3~6か月ごとに歯科受診。アルコール含有うがい薬と糖分含有製品(多くのトローチ含む)は避ける。',
    interact: [
      { en: 'Anticholinergic medications — leading iatrogenic cause of dry mouth; discuss with prescriber about alternatives', ko: '항콜린 약물 — 의인성 구강건조의 주요 원인; 처방의와 대체약 상담', ja: '抗コリン薬 — 医原性口腔乾燥の主要原因;処方医と代替薬を相談' },
      { en: 'Diuretics, antihypertensives, antidepressants (many types) — can worsen dry mouth', ko: '이뇨제, 항고혈압제, 항우울제 (다양한 계열) — 구강건조 악화 가능', ja: '利尿薬、降圧薬、抗うつ薬(多種) — 口腔乾燥を悪化させる可能性' },
      { en: 'Pilocarpine or cevimeline (prescription sialagogues) — for severe xerostomia (Sjögren\'s, post-radiation); discuss with physician', ko: '필로카르핀 또는 세비멜린 (처방 타액 분비 촉진제) — 중증 구강건조(쇼그렌, 방사선 후)에 의사 상담', ja: 'ピロカルピンまたはセビメリン(処方唾液分泌促進薬) — 重度口腔乾燥(シェーグレン·放射線後)で医師に相談' }
    ],
    source: 'ADA Council on Scientific Affairs · NIDCR · FDA OTC regulations'
  },
  {
    id: 'temporary-filling',
    generic: { en: 'Temporary dental filling / cement (zinc oxide-eugenol)', ko: '임시 치과 충전제 (산화아연 유지놀)', ja: '応急歯科充填材/セメント(酸化亜鉛ユージノール)' },
    brands: ['Dentemp OS', 'Refilit', 'Dentek Temparin', 'Recapit (for crowns)'],
    category: 'oral',
    uses: [
      { title_en: 'Emergency temporary repair of lost filling or broken tooth', title_ko: '빠진 충전재·깨진 치아의 응급 임시 수복', title_ja: '欠落した詰め物·欠けた歯の応急修復',
        detail_en: 'Zinc oxide–eugenol material that hardens in the cavity to seal exposed dentin, reducing pain and preventing food/debris entry while awaiting dental care. Use while waiting for a dentist appointment — NOT a permanent solution',
        detail_ko: '산화아연-유지놀 재료가 충치 내에서 경화되어 노출된 상아질을 봉쇄; 치과 진료 대기 중 통증 감소와 음식물 유입 방지. 치과 약속까지만 사용 — 영구적 해결책 아님',
        detail_ja: '酸化亜鉛-ユージノール材が窩洞内で硬化し露出象牙質を封鎖;歯科受診待ちの間、痛みを軽減し食物·破片の侵入を防ぐ。歯科予約までの間のみ使用 — 永久的解決ではない' },
      { title_en: 'Temporary recementation of loose crown', title_ko: '흔들리는 크라운의 임시 재접착', title_ja: '緩んだクラウンの応急再装着',
        detail_en: 'Specific products (Recapit, Dentek Temparin Max) can re-secure a dislodged crown until a dentist can properly recement',
        detail_ko: '특정 제품(Recapit, Dentek Temparin Max)은 빠진 크라운을 치과 방문 전까지 임시 고정 가능',
        detail_ja: '特定製品(Recapit、Dentek Temparin Max)は外れたクラウンを歯科受診まで仮固定可能' }
    ],
    dose_en: { 'Application': 'Clean the tooth cavity thoroughly with water, dry with gauze, apply small amount of material, bite gently to shape, wait 30 min before eating', 'Duration': 'Maximum 2–4 weeks — see a dentist as soon as possible', 'Not for active pain with swelling/fever': 'Infection requires professional treatment', 'Do not use on a tooth with visible abscess': 'Trapping pus worsens infection' },
    dose_ko: { '사용법': '충치 부위를 물로 깨끗이 씻고 거즈로 건조, 소량 도포, 가볍게 물어 형태 형성, 30분 후 식사', '사용 기간': '최대 2~4주 — 가능한 빨리 치과 진료', '부종·발열을 동반한 통증에는 사용 금지': '감염은 전문 치료 필요', '농양이 보이는 치아에 사용 금지': '고름을 가두면 감염 악화' },
    dose_ja: { '使用法': '窩洞を水で十分洗浄、ガーゼで乾燥、少量塗布、軽く噛んで形を整え、30分後に食事', '使用期間': '最大2~4週間 — できるだけ早く歯科受診', '腫脹·発熱を伴う痛みには使用禁止': '感染は専門治療必要', '膿瘍が見える歯への使用禁止': '膿を閉じ込めると感染悪化' },
    danger_en: 'DOES NOT TREAT DENTAL INFECTION OR ABSCESS. Signs of dental emergency requiring immediate care (not temporary filling): facial swelling, fever, severe throbbing pain, bad taste/pus in mouth, difficulty swallowing or breathing, trismus (inability to open mouth). Dental infections can spread to the face, neck, or bloodstream (Ludwig\'s angina, mediastinitis) — rare but fatal.',
    danger_ko: '치과 감염·농양을 치료하지 않습니다. 즉시 진료가 필요한 치과 응급 징후(임시 충전제 아닌): 얼굴 부종, 발열, 심한 박동성 통증, 입에서 고름·악취, 삼킴·호흡 곤란, 개구 장애. 치과 감염은 얼굴, 목, 혈류로 번질 수 있음(루드비히 앙기나, 종격동염) — 드물지만 치명적.',
    danger_ja: '歯科感染·膿瘍を治療しません。即時受診が必要な歯科救急徴候(応急充填材ではなく):顔面腫脹、発熱、激しい拍動性痛、口腔内の膿·悪臭、嚥下·呼吸困難、開口障害。歯科感染は顔、頸、血流に拡大する可能性(ルードビッヒ·アンギナ、縦隔炎) — 稀だが致命的。',
    warn_en: 'Sensitivity to eugenol (oil of cloves) is rare but possible. Do not use on primary (baby) teeth without dentist approval. If the temporary filling falls out repeatedly, the cavity is too large for self-repair — urgent dental visit needed. Pain medicine (acetaminophen or ibuprofen) can bridge to dental care.',
    warn_ko: '유지놀(정향유) 과민 반응은 드물지만 가능. 치과의 승인 없이 유치에 사용 금지. 임시 충전재가 반복적으로 빠지면 충치가 너무 큼 — 긴급 치과 진료 필요. 진통제(아세트아미노펜·이부프로펜)로 진료까지 시간 벌기 가능.',
    warn_ja: 'ユージノール(クローブ油)過敏反応は稀だが可能。歯科医の承認なく乳歯に使用禁止。応急充填が繰り返し外れる場合は窩洞が大きすぎる — 緊急歯科受診必要。鎮痛薬(アセトアミノフェン·イブプロフェン)で受診までつなぐ。',
    interact: [
      { en: 'Eugenol contact allergy — rare but possible; stop if rash develops', ko: '유지놀 접촉 알레르기 — 드물지만 가능; 발진 시 중단', ja: 'ユージノール接触アレルギー — 稀だが可能;発疹時は中止' },
      { en: 'No systemic drug interactions (localized use)', ko: '전신 약물 상호작용 없음 (국소 사용)', ja: '全身薬物相互作用なし(局所使用)' }
    ],
    source: 'American Dental Association · FDA dental device regulations'
  },
  {
    id: 'canker-sore-patch',
    generic: { en: 'Canker sore treatments (oral protectants)', ko: '구내염 치료제 (구강 보호제)', ja: '口内炎治療薬(口腔保護剤)' },
    brands: ['Canker Cover (Quantum Health)', 'CankerMelts', 'Orabase with Benzocaine', 'Zilactin-B'],
    category: 'oral',
    uses: [
      { title_en: 'Canker sore (aphthous ulcer) pain relief and protection', title_ko: '구내염(아프타성 궤양) 통증 완화·보호', title_ja: '口内炎(アフタ性潰瘍)の鎮痛·保護',
        detail_en: 'Adherent patches or gels that cover the sore, forming a protective barrier against food, acid, and mechanical trauma; pain relief within minutes, and may shorten healing time. Some contain benzocaine for numbing; others are purely protective',
        detail_ko: '궤양을 덮는 접착성 패치 또는 젤이 음식, 산, 기계적 자극에 대한 보호막 형성; 수분 이내 통증 완화 및 치유 기간 단축 가능. 일부는 벤조카인 함유로 마비 작용; 일부는 순수 보호 목적',
        detail_ja: '潰瘍を覆う接着性パッチまたはジェルが食物、酸、機械的刺激に対する保護膜を形成;数分以内の鎮痛と治癒期間短縮の可能性。一部はベンゾカイン含有で麻痺作用;他は純粋に保護目的' },
      { title_en: 'Mild mouth wounds from orthodontic irritation', title_ko: '교정장치 자극에 의한 경미한 구강 상처', title_ja: '矯正装置刺激による軽度の口腔創傷',
        detail_en: 'Can protect ulcers caused by braces, dentures, or sharp tooth edges while healing occurs',
        detail_ko: '치아교정장치, 의치, 날카로운 치아 모서리로 인한 궤양을 보호하며 치유 도움',
        detail_ja: 'ブラケット、義歯、鋭い歯縁による潰瘍を治癒中保護' }
    ],
    dose_en: { 'Patches': 'Apply 1 patch directly to the dried sore; dissolves over 6–8 hours. 3–4 times daily until healed', 'Gels (Orabase, Zilactin)': 'Apply thin layer to dried sore up to 4 times daily', 'Duration': '7–10 days typical canker sore healing; see doctor if sores last >2 weeks or recur frequently', 'Dry the sore first': 'Use a cotton swab to dry area before applying — improves adhesion' },
    dose_ko: { '패치': '건조한 궤양 위에 패치 1개 직접 부착; 6~8시간에 걸쳐 용해. 치유까지 하루 3~4회', '젤 (Orabase, Zilactin)': '건조한 궤양에 하루 최대 4회 얇게 도포', '기간': '일반적 구내염 치유 7~10일; 2주 이상 지속되거나 자주 재발 시 진료', '궤양 건조 먼저': '도포 전 면봉으로 건조 — 접착력 향상' },
    dose_ja: { 'パッチ': '乾燥した潰瘍に直接1枚貼付;6~8時間かけて溶解。治癒まで1日3~4回', 'ジェル(Orabase、Zilactin)': '乾燥した潰瘍に1日最大4回薄く塗布', '期間': '一般的な口内炎の治癒7~10日;2週間以上続く、または頻繁に再発する場合は受診', 'まず潰瘍を乾燥': '塗布前に綿棒で乾燥 — 接着性向上' },
    warn_en: 'Canker sores (aphthous ulcers, inside cheek/lips/tongue) are not the same as cold sores (herpes simplex, usually on lip border) — cold sores need different treatment (docosanol/Abreva). Recurrent canker sores (>3 per year, large sores, or accompanied by other symptoms) may indicate iron/B12/folate deficiency, celiac disease, Behçet\'s disease, or Crohn\'s — evaluation recommended.',
    warn_ko: '구내염(뺨·입술 안쪽·혀의 아프타성 궤양)은 감기 물집(헤르페스 단순, 보통 입술 가장자리)과 다름 — 감기 물집은 다른 치료(도코사놀/Abreva) 필요. 재발성 구내염(연 3회 이상, 큰 궤양, 다른 증상 동반)은 철분/B12/엽산 결핍, 셀리악병, 베체트병, 크론병 시사 가능 — 평가 권장.',
    warn_ja: '口内炎(アフタ性潰瘍、頬·唇内側·舌)は口唇ヘルペス(ヘルペス単純、通常唇縁)とは異なる — 口唇ヘルペスは別治療(ドコサノール/Abreva)が必要。再発性口内炎(年3回超、大型潰瘍、他症状を伴う)は鉄/B12/葉酸欠乏、セリアック病、ベーチェット病、クローン病を示唆 — 評価推奨。',
    interact: [
      { en: 'Benzocaine-containing products — see benzocaine methemoglobinemia warnings', ko: '벤조카인 함유 제품 — 벤조카인 메트헤모글로빈혈증 경고 참조', ja: 'ベンゾカイン含有製品 — ベンゾカインメトヘモグロビン血症の警告参照' },
      { en: 'Acidic foods/drinks — worsen pain; avoid during healing', ko: '산성 음식·음료 — 통증 악화; 치유 중 피함', ja: '酸性食品·飲料 — 痛みを悪化させる;治癒中は回避' },
      { en: 'Sodium lauryl sulfate (in many toothpastes) — linked to canker sore triggering in susceptible people; try SLS-free toothpaste', ko: '라우릴황산나트륨 (많은 치약 함유) — 감수성 있는 사람에서 구내염 유발 가능; SLS 무첨가 치약 시도', ja: 'ラウリル硫酸ナトリウム(多くの歯磨剤に含有) — 感受性のある人で口内炎を誘発する可能性;SLSフリー歯磨剤を試す' }
    ],
    source: 'ADA · NIH MedlinePlus · FDA OTC guidance'
  },

  // ============ FIRST AID ============
  {
    id: 'hydrogen-peroxide-3pct',
    generic: { en: 'Hydrogen peroxide 3% (topical antiseptic)', ko: '과산화수소 3% (외용 소독제)', ja: '過酸化水素3%(外用消毒薬)' },
    brands: ['Generic (sold as "Hydrogen Peroxide USP 3%")', 'CVS Health', 'Walgreens'],
    category: 'first_aid',
    uses: [
      { title_en: 'Initial cleansing of minor cuts and scrapes (limited role)', title_ko: '경미한 절창·찰과상의 초기 세척 (제한적 역할)', title_ja: '軽度の切り傷·すり傷の初期洗浄(限定的役割)',
        detail_en: 'Historically used for wound cleaning, but current evidence and CDC/AAP guidance recommend plain water or saline as the preferred first-line wound rinse. Hydrogen peroxide kills some bacteria but also damages healthy cells (fibroblasts, keratinocytes) and may delay healing when used repeatedly',
        detail_ko: '과거 상처 세척에 사용되었으나 현재 근거와 CDC/AAP 지침은 물이나 식염수를 1차 상처 세척제로 권장. 과산화수소는 일부 세균을 죽이나 건강한 세포(섬유아세포, 각질세포)도 손상시켜 반복 사용 시 치유 지연 가능',
        detail_ja: '従来創傷洗浄に使用されてきたが、現在のエビデンスとCDC/AAPの指針は水または生理食塩水を第一選択の創傷洗浄剤として推奨。過酸化水素は一部の細菌を殺すが健康な細胞(線維芽細胞、ケラチノサイト)も損傷し、反復使用で治癒が遅れる可能性' },
      { title_en: 'Removing dried blood or debris', title_ko: '굳은 혈액·이물 제거', title_ja: '乾いた血液·異物の除去',
        detail_en: 'Effervescent action helps mechanically loosen debris from wounds; one-time cleaning use is acceptable',
        detail_ko: '거품 반응이 상처의 이물을 기계적으로 분리; 1회 세척 사용은 수용 가능',
        detail_ja: '発泡作用が創部の異物を機械的に剥離;1回の洗浄使用は許容可能' }
    ],
    dose_en: { 'Wound cleansing': 'Pour or apply with cotton/gauze once at initial cleaning; rinse with water or saline afterward', 'Do NOT use repeatedly': 'For ongoing wound care, use saline or plain water', 'Never use on deep or puncture wounds': 'Risk of tissue injury and (rare) gas embolism in deep tissue', 'Not for eyes, ears (intact drum only), or large burn areas': 'Can cause serious injury' },
    dose_ko: { '상처 세척': '초기 세척 시 부어 사용하거나 면·거즈로 도포 1회; 이후 물이나 식염수로 헹굼', '반복 사용 금지': '지속적 상처 관리는 식염수 또는 물 사용', '깊은 상처·관통상 금지': '조직 손상 및 (드물게) 심부 조직 가스 색전증 위험', '눈, 귀(고막 온전할 때만), 광범위 화상 부위 금지': '심각한 손상 유발 가능' },
    dose_ja: { '創傷洗浄': '初期洗浄時に注ぐか綿·ガーゼで1回塗布;その後水または生理食塩水ですすぐ', '反復使用禁止': '継続的な創傷管理には生理食塩水または水を使用', '深い創傷·穿通創禁止': '組織損傷と(稀な)深部組織のガス塞栓のリスク', '眼、耳(鼓膜が無傷の時のみ)、広範な熱傷部位禁止': '重篤な損傷の可能性' },
    danger_en: 'DO NOT INJECT, DRINK, OR USE INTRAVENOUSLY — fatal cases have occurred from internet "oxygen therapy" scams; concentrated or injected H2O2 causes fatal oxygen embolism. Do not use 35% "food grade" peroxide anywhere on or in the body — household 3% is the only appropriate concentration. Deep wound irrigation can cause subcutaneous emphysema or gas embolism. Not a substitute for medical care of infected wounds.',
    danger_ko: '주사, 음용, 정맥 투여 금지 — 인터넷 "산소 요법" 사기로 사망 사례 다수 발생; 농축 또는 주사된 H2O2는 치명적 산소 색전증 유발. 35% "식품급" 과산화수소는 몸 어디에도 사용 금지 — 가정용 3%만 적절. 깊은 상처 세척은 피하 기종 또는 가스 색전증 유발 가능. 감염된 상처의 의학적 치료를 대체하지 않습니다.',
    danger_ja: '注射、飲用、静脈内投与禁止 — インターネット「酸素療法」詐欺で死亡例多数;濃縮または注射されたH2O2は致命的酸素塞栓を起こす。35%「食品グレード」過酸化水素は体のどこにも使用禁止 — 家庭用3%のみ適切。深い創傷洗浄は皮下気腫やガス塞栓を起こす可能性。感染創の医療的治療の代替ではない。',
    warn_en: 'Wounds with these features need evaluation, not home care: bites (animal/human), deep puncture, inability to remove debris, signs of infection (redness spreading, pus, fever), last tetanus >5–10 years ago, or in diabetics/immunocompromised. Store tightly capped, away from light and heat — decomposes and loses potency. Expires ~6 months after opening.',
    warn_ko: '가정 관리가 아닌 진료가 필요한 상처: 물림(동물·사람), 깊은 관통상, 이물 제거 불가, 감염 징후(발적 확산, 고름, 발열), 마지막 파상풍 예방접종 5~10년 이상 경과, 당뇨·면역저하자. 빛과 열을 피해 밀봉 보관 — 분해되어 효능 상실. 개봉 후 약 6개월 유효.',
    warn_ja: '家庭ケアではなく受診が必要な創傷:咬傷(動物·ヒト)、深い穿通創、異物除去不能、感染徴候(広がる発赤、膿、発熱)、最後の破傷風予防接種から5~10年以上経過、糖尿病·免疫不全者。光と熱を避け密閉保管 — 分解し効力低下。開封後約6か月有効。',
    interact: [
      { en: 'Hydrogen peroxide is inactivated by organic matter and catalase — effect is limited in bloody wounds', ko: '과산화수소는 유기물과 카탈라제에 의해 비활성화 — 혈액이 있는 상처에서 효과 제한적', ja: '過酸化水素は有機物とカタラーゼで失活 — 血液のある創傷では効果限定的' },
      { en: 'Chlorhexidine, silver-containing products — do not mix; can reduce effectiveness of both', ko: '클로르헥시딘, 은 함유 제품 — 혼합 금지; 양쪽 효과 감소 가능', ja: 'クロルヘキシジン、銀含有製品 — 混合禁止;両方の効果が減少する可能性' }
    ],
    source: 'CDC Wound Care Guidelines · AAP · FDA OTC Monograph · FDA warning on high-strength H2O2'
  },
  {
    id: 'isopropyl-alcohol',
    generic: { en: 'Isopropyl alcohol 70% (rubbing alcohol)', ko: '이소프로필 알코올 70% (소독용 알코올)', ja: 'イソプロピルアルコール70%(消毒用アルコール)' },
    brands: ['Generic rubbing alcohol 70%', 'CVS, Walgreens, store brands'],
    category: 'first_aid',
    uses: [
      { title_en: 'Skin disinfection before injection or minor procedure', title_ko: '주사·경미한 시술 전 피부 소독', title_ja: '注射·軽度の処置前の皮膚消毒',
        detail_en: 'Rapid-acting skin antiseptic; standard for pre-injection skin prep, fingerstick blood glucose testing, thermometer cleaning, and surface disinfection',
        detail_ko: '빠른 작용의 피부 소독제; 주사 전 피부 소독, 손끝 혈당 측정, 체온계 세척, 표면 소독의 표준',
        detail_ja: '速効性皮膚消毒薬;注射前の皮膚消毒、指先血糖測定、体温計清拭、表面消毒の標準' },
      { title_en: 'Surface disinfection of medical devices and home surfaces', title_ko: '의료기기·가정 표면 소독', title_ja: '医療機器·家庭表面の消毒',
        detail_en: 'Effective against most bacteria, enveloped viruses (including coronaviruses, influenza); 70% concentration is more effective than 90%+ because water allows better penetration',
        detail_ko: '대부분 세균과 외피 보유 바이러스(코로나바이러스, 인플루엔자 포함)에 효과; 70% 농도가 90% 이상보다 효과적 — 물이 침투를 돕기 때문',
        detail_ja: '大部分の細菌とエンベロープウイルス(コロナウイルス、インフルエンザを含む)に有効;70%濃度が90%以上より有効 — 水が浸透を助けるため' }
    ],
    dose_en: { 'Injection site prep': 'Wipe area with alcohol pad or saturated cotton; allow to air-dry fully (30 seconds) before puncture', 'Surface cleaning': 'Apply and wipe; allow 30+ seconds contact time for disinfection', 'Do NOT use on': 'Open wounds, large abrasions, burns, mucous membranes, or face near eyes — severely painful and damages tissue', 'Flammable': 'Keep away from flames, cigarettes, cauterization' },
    dose_ko: { '주사 부위 소독': '알코올 패드 또는 포화된 면으로 닦음; 찌르기 전 완전히 건조(30초)', '표면 청소': '도포 후 닦음; 소독을 위해 30초 이상 접촉', '사용 금지 부위': '개방 상처, 큰 찰과상, 화상, 점막, 눈 주변 얼굴 — 심한 통증 및 조직 손상', '인화성': '불꽃, 담배, 소작 기구 멀리' },
    dose_ja: { '注射部位消毒': 'アルコールパッドまたは飽和綿で拭く;穿刺前に完全に風乾(30秒)', '表面清拭': '塗布後に拭く;消毒のため30秒以上の接触時間', '使用禁止部位': '開放創、大きなすり傷、熱傷、粘膜、眼周辺の顔面 — 強い痛みと組織損傷', '可燃性': '炎、タバコ、焼灼器具から離す' },
    danger_en: 'ORAL INGESTION IS TOXIC AND CAN BE FATAL — causes gastritis, CNS depression, coma, hypoglycemia. Ingestion by children of even small amounts (a few swallows) requires poison control call. Do not apply to infants for fever reduction ("alcohol sponging") — can be absorbed through thin skin causing toxicity. Inhaling concentrated fumes in poorly ventilated space causes headache, dizziness, nausea.',
    danger_ko: '경구 섭취 시 독성이 있으며 치명적일 수 있음 — 위염, 중추신경 억제, 혼수, 저혈당 유발. 어린이가 소량(몇 모금)만 삼켜도 중독관리센터 연락 필요. 영아 해열 목적으로 "알코올 찜질" 금지 — 얇은 피부로 흡수되어 독성 유발 가능. 환기 부족한 공간에서 농축 증기 흡입 시 두통, 어지러움, 메스꺼움.',
    danger_ja: '経口摂取は毒性で致命的の可能性 — 胃炎、中枢神経抑制、昏睡、低血糖を起こす。小児が少量(数口)でも飲み込んだ場合は中毒センターに連絡。乳児の解熱目的で「アルコール清拭」禁止 — 薄い皮膚から吸収され毒性を起こす可能性。換気不良空間での濃縮蒸気吸入は頭痛、めまい、吐き気を起こす。',
    warn_en: 'Not effective against spores (C. difficile) or non-enveloped viruses (norovirus, rotavirus) — for those, use soap and water or bleach. Dries out skin with repeated use — add hand moisturizer. Hand sanitizer (60%+ alcohol) is appropriate between handwashings, not as a replacement for washing visibly dirty hands. Store tightly capped away from children.',
    warn_ko: '포자(C. difficile)나 외피 없는 바이러스(노로바이러스, 로타바이러스)에는 효과 없음 — 비누·물 또는 표백제 사용. 반복 사용 시 피부 건조 — 보습제 병용. 손 소독제(60% 이상 알코올)는 손씻기 사이에 적절하며 눈에 보이게 더러운 손의 씻기 대체는 아님. 밀봉하여 소아 손이 닿지 않게 보관.',
    warn_ja: '芽胞(C. difficile)やエンベロープなしウイルス(ノロウイルス、ロタウイルス)には無効 — それらには石鹸·水または漂白剤を使用。反復使用で皮膚乾燥 — 保湿剤併用。手指消毒剤(60%以上アルコール)は手洗い間の使用に適切で、目に見えて汚れた手の洗浄の代替ではない。密閉し小児の手の届かない場所に保管。',
    interact: [
      { en: 'Disulfiram (Antabuse) — topical absorption generally insufficient to trigger reaction, but oral/concentrated exposure can', ko: '디설피람 (Antabuse) — 국소 흡수는 일반적으로 반응 유발 불충분; 경구·농축 노출은 가능', ja: 'ジスルフィラム(アンタビュース) — 局所吸収では一般的に反応誘発に不十分;経口·濃縮曝露は可能' },
      { en: 'Povidone-iodine, chlorhexidine — do not mix on wound (reduced effectiveness of each); use one or the other', ko: '포비돈 요오드, 클로르헥시딘 — 상처에서 혼합 금지 (각각의 효과 감소); 한 가지만 사용', ja: 'ポビドンヨード、クロルヘキシジン — 創傷で混合禁止(各々の効果減少);どちらか一方を使用' },
      { en: 'Open flame / electrocautery — fire risk; ensure full evaporation first', ko: '개방 화염 / 전기 소작 — 화재 위험; 완전 증발 후 시행', ja: '裸火/電気焼灼 — 火災リスク;完全蒸発後に実施' }
    ],
    source: 'CDC Guideline for Disinfection and Sterilization · FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'povidone-iodine',
    generic: { en: 'Povidone-iodine 10% (topical antiseptic)', ko: '포비돈 요오드 10% (외용 소독제)', ja: 'ポビドンヨード10%(外用消毒薬)' },
    brands: ['Betadine', 'Wound Wash', 'Generic povidone-iodine solution'],
    category: 'first_aid',
    uses: [
      { title_en: 'Skin and wound antisepsis', title_ko: '피부·상처 소독', title_ja: '皮膚·創傷消毒',
        detail_en: 'Broad-spectrum antiseptic effective against bacteria (including MRSA), viruses, fungi, protozoa, and spores. Used for minor wound cleansing, pre-surgical skin prep, and healthcare hand antisepsis. Effect starts within 30 seconds and lasts for hours (slow-release iodine)',
        detail_ko: '광범위 소독제로 세균(MRSA 포함), 바이러스, 진균, 원충, 포자에 효과. 경미한 상처 세척, 수술 전 피부 소독, 의료진 손 소독에 사용. 효과는 30초 이내 시작되어 수시간 지속(서방성 요오드)',
        detail_ja: '広域消毒薬で細菌(MRSA含む)、ウイルス、真菌、原虫、芽胞に有効。軽度の創傷洗浄、手術前皮膚消毒、医療従事者の手指消毒に使用。効果は30秒以内に開始し数時間持続(徐放性ヨウ素)' }
    ],
    dose_en: { 'Minor wounds': 'Apply to cleaned wound once daily until healed; rinse first with saline or water', 'Skin prep before minor procedures': 'Apply with swab in concentric circles outward; allow to dry fully for maximum effect', 'Duration on intact wounds': 'Short courses (up to a week); prolonged use may impair healing at high concentrations', 'Dilute forms': '5% and 7.5% scrubs also available for surgical hand washing' },
    dose_ko: { '경미한 상처': '세척한 상처에 하루 1회 치유까지 도포; 먼저 식염수·물로 세척', '경미한 시술 전 피부 소독': '면봉으로 바깥 방향 동심원으로 도포; 최대 효과를 위해 완전 건조', '온전한 상처에서 사용 기간': '단기 사용(최대 1주); 고농도 장기 사용 시 치유 지연 가능', '희석 제형': '5% 및 7.5% 스크럽은 수술용 손씻기로 제공' },
    dose_ja: { '軽度の創傷': '洗浄した創傷に1日1回治癒まで塗布;まず生理食塩水·水で洗浄', '軽度の処置前の皮膚消毒': '綿棒で外側に向かって同心円状に塗布;最大効果のため完全に乾燥', '無傷創傷での使用期間': '短期使用(最大1週);高濃度長期使用で治癒遅延の可能性', '希釈製剤': '5%·7.5%スクラブは手術用手洗いに提供' },
    danger_en: 'IODINE ALLERGY — avoid in people with known iodine allergy (different from shellfish allergy, which is NOT an iodine allergy contrary to common belief). Absorption of iodine through broken skin or mucous membranes can cause thyroid dysfunction, especially in: neonates, pregnant and breastfeeding women, infants, and people with known thyroid disease. Avoid in extensive wounds and burns. Stains skin, fabric, and surfaces brown (washes out with water plus soap or ammonia).',
    danger_ko: '요오드 알레르기 — 요오드 알레르기가 알려진 사람은 사용 금지(조개 알레르기는 요오드 알레르기가 아님 — 흔한 오해). 손상된 피부나 점막을 통한 요오드 흡수는 갑상선 기능 이상을 유발할 수 있음, 특히: 신생아, 임산부·수유부, 영아, 갑상선 질환자. 광범위 상처·화상 사용 피함. 피부, 천, 표면이 갈색으로 착색(물+비누 또는 암모니아로 제거).',
    danger_ja: 'ヨウ素アレルギー — 既知のヨウ素アレルギーがある人は使用禁止(貝アレルギーとは異なる、貝アレルギーはヨウ素アレルギーではない — 一般的な誤解)。損傷皮膚または粘膜からのヨウ素吸収で甲状腺機能異常の可能性、特に:新生児、妊婦·授乳婦、乳児、既知の甲状腺疾患患者。広範な創傷·熱傷では回避。皮膚、布、表面を茶色に着色(水+石鹸またはアンモニアで除去)。',
    warn_en: 'Not for use on deep or puncture wounds — same concerns as hydrogen peroxide plus iodine absorption. Do not use with mercury-containing antiseptics (merbromin). Multiple studies suggest saline is equivalent or superior for routine wound care; reserve povidone-iodine for heavily contaminated wounds, pre-procedural prep, or when MRSA/other resistant organisms are a concern.',
    warn_ko: '깊은 상처·관통상 사용 금지 — 과산화수소와 동일한 우려 및 요오드 흡수 문제. 수은 함유 소독제(머브로민)와 병용 금지. 여러 연구에서 일상 상처 관리에 식염수가 동등하거나 우수함이 시사됨; 포비돈 요오드는 심하게 오염된 상처, 시술 전 소독, MRSA 등 내성균 우려 시에 제한.',
    warn_ja: '深い創傷·穿通創には使用禁止 — 過酸化水素と同様の懸念に加えてヨウ素吸収の問題。水銀含有消毒薬(メルブロミン)との併用禁止。複数の研究で日常の創傷ケアでは生理食塩水が同等または優れていることが示唆;ポビドンヨードは重度汚染創傷、処置前消毒、MRSAなど耐性菌懸念時に限定。',
    interact: [
      { en: 'Thyroid function tests — can alter results; stop 1 month before thyroid scans if regular user', ko: '갑상선 기능 검사 — 결과 왜곡 가능; 정기 사용자는 갑상선 스캔 1개월 전 중단', ja: '甲状腺機能検査 — 結果に影響の可能性;常用者は甲状腺スキャン1か月前に中止' },
      { en: 'Lithium — both affect thyroid; avoid high-dose povidone exposure', ko: '리튬 — 양쪽 모두 갑상선에 영향; 고용량 포비돈 노출 피함', ja: 'リチウム — 双方とも甲状腺に影響;高用量ポビドン曝露を回避' },
      { en: 'Silver-containing products, chlorhexidine — do not combine on same wound; reduced efficacy', ko: '은 함유 제품, 클로르헥시딘 — 같은 상처에 병용 금지; 효과 감소', ja: '銀含有製品、クロルヘキシジン — 同じ創傷に併用禁止;効果減少' },
      { en: 'Mercury-containing antiseptics — caustic reaction; never combine', ko: '수은 함유 소독제 — 부식 반응; 절대 병용 금지', ja: '水銀含有消毒薬 — 腐食反応;絶対併用禁止' }
    ],
    source: 'WHO Model List of Essential Medicines · CDC Guideline · FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'calamine',
    generic: { en: 'Calamine lotion (zinc oxide + ferric oxide)', ko: '칼라민 로션 (산화아연 + 산화철)', ja: 'カラミンローション(酸化亜鉛+酸化鉄)' },
    brands: ['Caladryl', 'Generic Calamine Lotion USP', 'Aveeno Calamine'],
    category: 'first_aid',
    uses: [
      { title_en: 'Itching from poison ivy, poison oak, poison sumac', title_ko: '옻나무·덩굴옻나무에 의한 가려움', title_ja: 'ウルシ·ツタウルシ·ヌルデによるかゆみ',
        detail_en: 'Classic remedy for urushiol-induced contact dermatitis; zinc oxide provides mild astringent and cooling effect, reducing itch and providing a drying barrier',
        detail_ko: '우루시올 유발 접촉피부염의 고전적 치료제; 산화아연이 경미한 수렴·냉각 작용으로 가려움 감소 및 건조 차단막 형성',
        detail_ja: 'ウルシオール誘発接触皮膚炎の古典的治療薬;酸化亜鉛が軽度の収斂·冷却作用でかゆみを軽減し乾燥バリアを形成' },
      { title_en: 'Itching from insect bites, chickenpox, minor heat rash', title_ko: '벌레 물림·수두·경미한 땀띠로 인한 가려움', title_ja: '虫刺され·水痘·軽度のあせもによるかゆみ',
        detail_en: 'Symptomatic itch relief for various pruritic skin conditions; safe in children (traditional chickenpox home remedy)',
        detail_ko: '다양한 가려움 유발 피부 상태의 대증 완화; 소아에 안전(전통적 수두 가정 요법)',
        detail_ja: '様々なかゆみを伴う皮膚状態の対症緩和;小児に安全(伝統的水痘家庭療法)' }
    ],
    dose_en: { 'Application': 'Shake bottle, apply to affected area 3–4 times daily with cotton ball or pad', 'Do not rub in': 'Allow to dry on skin as a powder layer', 'Duration': 'Until itching resolves, typically 1–2 weeks for poison ivy', 'Washing off': 'Wash off and reapply as needed' },
    dose_ko: { '사용법': '병 흔들기, 해당 부위에 하루 3~4회 면 또는 패드로 도포', '문지르지 않기': '피부 위에서 가루 층으로 건조되도록 둠', '기간': '가려움 호전까지, 옻나무는 보통 1~2주', '씻어내기': '필요시 씻고 재도포' },
    dose_ja: { '使用法': 'ボトルを振り、患部に1日3~4回綿球またはパッドで塗布', 'こすらない': '皮膚上で粉末層として乾燥させる', '期間': 'かゆみが治まるまで、ウルシは通常1~2週', '洗い流す': '必要に応じて洗い流し再塗布' },
    warn_en: 'Does not treat the allergy itself — for severe reactions (swelling of face/eyes, extensive rash, blistering, or involvement of genitals) see a doctor; may need oral steroids. Do not use on broken skin, open blisters, or for prolonged periods on large areas. Some formulations contain diphenhydramine (Caladryl) — avoid in children under 2 and do not combine with oral diphenhydramine (risk of systemic toxicity from combined use).',
    warn_ko: '알레르기 자체를 치료하지 않음 — 중증 반응(얼굴·눈 부종, 광범위 발진, 수포, 생식기 침범)은 진료; 경구 스테로이드 필요 가능. 손상된 피부, 열린 수포, 넓은 부위 장기 사용 금지. 일부 제형(Caladryl)은 디펜히드라민 함유 — 2세 미만 금지 및 경구 디펜히드라민과 병용 금지(복합 사용 시 전신 독성 위험).',
    warn_ja: 'アレルギー自体は治療しない — 重症反応(顔·眼の腫脹、広範な発疹、水疱、外陰部の関与)は受診;経口ステロイドが必要な可能性。損傷皮膚、開いた水疱、広範囲への長期使用禁止。一部の製剤(Caladryl)はジフェンヒドラミン含有 — 2歳未満禁止、経口ジフェンヒドラミンとの併用禁止(複合使用で全身毒性リスク)。',
    interact: [
      { en: 'Diphenhydramine-containing calamine (Caladryl) — do not combine with oral diphenhydramine; skin absorption plus oral dose can cause toxicity', ko: '디펜히드라민 함유 칼라민 (Caladryl) — 경구 디펜히드라민과 병용 금지; 피부 흡수 + 경구 복용으로 독성 가능', ja: 'ジフェンヒドラミン含有カラミン(Caladryl) — 経口ジフェンヒドラミンとの併用禁止;皮膚吸収+経口投与で毒性の可能性' },
      { en: 'Topical steroids — can use in combination for poison ivy; apply steroid first, then calamine after it dries', ko: '국소 스테로이드 — 옻나무에 병용 가능; 스테로이드 먼저 도포 후 건조되면 칼라민', ja: '局所ステロイド — ウルシに併用可能;ステロイドを先に塗布、乾いてからカラミン' }
    ],
    source: 'FDA OTC Monograph 21 CFR 347 · DailyMed (NIH) · AAD'
  },
  {
    id: 'burn-aloe-gel',
    generic: { en: 'Aloe vera / burn gel (for minor burns)', ko: '알로에 베라·화상 젤 (경미한 화상)', ja: 'アロエベラ·やけどジェル(軽度のやけど)' },
    brands: ['Fruit of the Earth Aloe Vera Gel', 'Solarcaine Cool Aloe', 'Banana Boat Aloe After Sun'],
    category: 'first_aid',
    uses: [
      { title_en: 'Superficial sunburn and minor thermal burns (1st degree)', title_ko: '표재성 일광 화상·경미한 열화상 (1도)', title_ja: '表在性日焼けと軽度の熱傷(1度)',
        detail_en: 'Soothing, cooling effect for sunburn (red, painful, no blisters) and other minor superficial burns. Pure aloe vera gel (without added lidocaine or alcohol) is most broadly recommended — some evidence for shortening healing time of superficial partial-thickness burns',
        detail_ko: '일광 화상(붉고 아프나 수포 없음)과 기타 경미한 표재성 화상에 진정·냉각 작용. 리도카인이나 알코올 무첨가 순수 알로에 베라 젤이 가장 널리 권장됨 — 표재성 부분층 화상의 치유 단축 근거 일부',
        detail_ja: '日焼け(赤く痛みあり、水疱なし)とその他の軽度表在性熱傷に鎮静·冷却作用。リドカインやアルコール無添加の純粋なアロエベラジェルが最も広く推奨 — 表在性部分層熱傷の治癒短縮のエビデンスあり' },
      { title_en: 'Minor skin irritation, after-shave, dry skin', title_ko: '경미한 피부 자극·면도 후·건조한 피부', title_ja: '軽度の皮膚刺激·髭剃り後·乾燥肌',
        detail_en: 'Cool, non-comedogenic moisturizer; traditional uses include minor cuts and scrapes, skin irritation, and dry skin',
        detail_ko: '시원하고 비여드름 유발성 보습제; 전통적 용도로 경미한 절창·찰과상, 피부 자극, 건조한 피부',
        detail_ja: '冷感のあるノンコメドジェニック保湿剤;伝統的用途として軽度の切創·擦過傷、皮膚刺激、乾燥肌' }
    ],
    dose_en: { 'Application': 'Apply a thin layer to clean, cooled skin 3–4 times daily; store in refrigerator for enhanced cooling effect', 'For sunburn': 'First cool the area with cool (not icy) water 10–15 minutes, then apply aloe; drink extra water; acetaminophen or ibuprofen for pain', 'Do NOT use on': 'Deep burns, burns with blisters larger than fingertip, chemical burns, electrical burns, burns involving face/hands/feet/genitals', 'Avoid lidocaine-containing burn gels': 'On extensive surface area — systemic absorption risk' },
    dose_ko: { '사용법': '깨끗하고 식힌 피부에 하루 3~4회 얇게 도포; 냉각 효과를 위해 냉장 보관', '일광 화상': '먼저 시원한(얼음 아님) 물로 10~15분 식힌 후 알로에 도포; 수분 충분히 섭취; 통증에 아세트아미노펜·이부프로펜', '사용 금지': '깊은 화상, 손끝보다 큰 수포 동반 화상, 화학 화상, 전기 화상, 얼굴·손·발·생식기 화상', '리도카인 함유 화상 젤': '광범위 부위 사용 금지 — 전신 흡수 위험' },
    dose_ja: { '使用法': '清潔で冷やした皮膚に1日3~4回薄く塗布;冷却効果のため冷蔵保管', '日焼け': 'まず涼しい(氷ではない)水で10~15分冷却後アロエ塗布;水分十分摂取;痛みにはアセトアミノフェン·イブプロフェン', '使用禁止': '深い熱傷、指先より大きな水疱を伴う熱傷、化学熱傷、電気熱傷、顔·手·足·性器の熱傷', 'リドカイン含有やけどジェル': '広範囲使用禁止 — 全身吸収リスク' },
    danger_en: 'DO NOT USE ICE OR BUTTER OR TOOTHPASTE ON BURNS — these traditional remedies can worsen tissue damage. Burn emergencies requiring immediate care: burns larger than 3 inches (7 cm), burns of face/hands/feet/major joints/genitals, any blistering or charred skin (2nd and 3rd degree), electrical burns, chemical burns, burns in children or elderly, or any burn with inhalation injury (hoarse voice, soot around nose/mouth) — these need emergency evaluation regardless of size.',
    danger_ko: '화상에 얼음, 버터, 치약 사용 금지 — 이런 전통 요법은 조직 손상을 악화시킴. 즉시 진료가 필요한 화상 응급: 7 cm(3인치) 초과, 얼굴·손·발·주요 관절·생식기, 수포 또는 검게 탄 피부(2도·3도), 전기 화상, 화학 화상, 소아·고령자 화상, 또는 흡입 손상 동반(쉰 목소리, 코·입 주변 그을음) — 크기와 관계없이 응급 평가 필요.',
    danger_ja: 'やけどに氷·バター·歯磨き粉使用禁止 — これらの伝統療法は組織損傷を悪化させる。即時受診が必要なやけど緊急:7 cm(3インチ)超、顔·手·足·主要関節·性器、水疱または炭化した皮膚(2度·3度)、電気熱傷、化学熱傷、小児·高齢者のやけど、または吸入損傷を伴う(嗄声、鼻·口周囲の煤) — サイズに関わらず緊急評価必要。',
    warn_en: 'Some people are allergic to aloe — patch test on forearm before wide application. Oral aloe (juice, supplements) has different safety concerns and can cause severe diarrhea, electrolyte imbalance; do NOT drink wound-care gels. Aloe with lidocaine or benzocaine adds methemoglobinemia risk in children and on large areas. Preservatives in some products can cause contact dermatitis.',
    warn_ko: '알로에 알레르기가 있는 사람도 있음 — 광범위 도포 전 팔뚝 패치 테스트. 경구 알로에(주스, 보충제)는 안전성 문제가 다르며 심한 설사, 전해질 불균형 유발 가능; 상처용 젤을 마시지 마세요. 리도카인·벤조카인 함유 알로에는 소아 및 넓은 부위에서 메트헤모글로빈혈증 위험 추가. 일부 제품의 방부제가 접촉피부염 유발 가능.',
    warn_ja: 'アロエにアレルギーの人もいる — 広範囲塗布前に前腕でパッチテスト。経口アロエ(ジュース、サプリ)は安全性の問題が異なり重度の下痢、電解質不均衡を起こす可能性;傷ケアジェルを飲まないでください。リドカイン·ベンゾカイン含有アロエは小児·広範囲でメトヘモグロビン血症リスク追加。一部製品の防腐剤が接触皮膚炎を起こす可能性。',
    interact: [
      { en: 'Lidocaine- or benzocaine-containing burn products — methemoglobinemia risk in children and large areas', ko: '리도카인·벤조카인 함유 화상 제품 — 소아 및 넓은 부위에서 메트헤모글로빈혈증 위험', ja: 'リドカイン·ベンゾカイン含有やけど製品 — 小児·広範囲でメトヘモグロビン血症リスク' },
      { en: 'Topical corticosteroids — can use together for sunburn, but steroid first then aloe after it absorbs', ko: '국소 스테로이드 — 일광 화상에 병용 가능하나 스테로이드 먼저 흡수된 후 알로에', ja: '外用ステロイド — 日焼けに併用可能だがステロイド先に吸収後アロエ' },
      { en: 'Oral aloe supplements and laxatives — do not combine with diuretics (electrolyte loss) or digoxin', ko: '경구 알로에 보충제·하제 — 이뇨제(전해질 손실)·디곡신과 병용 금지', ja: '経口アロエサプリ·下剤 — 利尿薬(電解質喪失)·ジゴキシンと併用禁止' }
    ],
    source: 'American Burn Association · NIH Office of Dietary Supplements · DailyMed (NIH)'
  },
  {
    id: 'naloxone-narcan',
    generic: { en: 'Naloxone nasal spray 4 mg (opioid overdose reversal)', ko: '날록손 비강 스프레이 4 mg (오피오이드 과량 역전)', ja: 'ナロキソン点鼻スプレー4 mg(オピオイド過量反転)' },
    brands: ['Narcan Nasal Spray', 'RiVive (3 mg)', 'generic naloxone nasal spray'],
    category: 'first_aid',
    uses: [
      { title_en: 'Emergency reversal of opioid overdose', title_ko: '오피오이드 과량 복용 응급 역전', title_ja: 'オピオイド過量服用の緊急反転',
        detail_en: 'Opioid receptor antagonist that rapidly reverses life-threatening respiratory depression from opioid overdose (prescription opioids, heroin, fentanyl, illicitly manufactured opioids). FDA approved as OTC in March 2023 — no prescription needed. Every household with any opioid medication should have naloxone available, as should communities with opioid exposure risk',
        detail_ko: '오피오이드 수용체 길항제로 오피오이드 과량(처방 오피오이드, 헤로인, 펜타닐, 불법 제조 오피오이드)으로 인한 생명 위협 호흡 억제를 신속히 역전. 2023년 3월 FDA가 OTC로 승인 — 처방전 불필요. 오피오이드를 보유한 모든 가정과 오피오이드 노출 위험이 있는 지역사회는 날록손을 구비해야 함',
        detail_ja: 'オピオイド受容体拮抗薬でオピオイド過量(処方オピオイド、ヘロイン、フェンタニル、違法製造オピオイド)による生命に関わる呼吸抑制を迅速に反転。2023年3月FDAがOTC承認 — 処方箋不要。オピオイドを所有するすべての家庭およびオピオイド曝露リスクのある地域社会はナロキソンを常備すべき' }
    ],
    dose_en: { 'Administration': 'Call 911 first. Tilt head back, insert nozzle into ONE nostril, push plunger fully — delivers 4 mg dose. Lay person on side (recovery position). If no response in 2–3 minutes, give second dose in OTHER nostril', 'Additional doses': 'Can repeat every 2–3 minutes with alternating nostrils until emergency arrives — fentanyl overdose often requires multiple doses', 'Always call 911': 'Even after response — effects wear off in 30–90 minutes; opioid can re-sedate person', 'Rescue breathing': 'If trained, give rescue breaths while awaiting effect; CPR if no pulse' },
    dose_ko: { '투여법': '먼저 911 신고. 머리를 뒤로 젖히고 한쪽 콧구멍에 노즐 삽입, 플런저를 끝까지 누름 — 4 mg 투여. 대상자를 옆으로 눕힘(회복 자세). 2~3분 내 반응 없으면 다른 콧구멍에 2번째 투여', '추가 투여': '응급 대원 도착 전까지 2~3분마다 콧구멍을 번갈아 반복 가능 — 펜타닐 과량은 여러 번 필요한 경우가 많음', '반드시 911 신고': '반응 후에도 — 효과는 30~90분 후 소실되며 오피오이드가 다시 진정 유발 가능', '구조 호흡': '훈련된 경우 효과 대기 중 구조 호흡; 맥박 없으면 CPR' },
    dose_ja: { '投与法': 'まず911通報。頭を後ろに傾け片方の鼻孔にノズル挿入、プランジャーを最後まで押す — 4 mg投与。患者を横向きに寝かせる(回復体位)。2~3分以内に反応なければ反対側の鼻孔に2回目投与', '追加投与': '救急隊到着まで2~3分ごとに鼻孔を交互に反復可能 — フェンタニル過量はしばしば複数回必要', '必ず911通報': '反応後も — 効果は30~90分で消失しオピオイドが再鎮静を起こす可能性', '救命呼吸': '訓練されていれば効果待ちの間救命呼吸;脈拍なしならCPR' },
    danger_en: 'THIS IS A LIFE-SAVING EMERGENCY MEDICATION. Signs of opioid overdose: unresponsive to voice/touch, very slow or stopped breathing (less than 10 breaths per minute), pinpoint pupils, blue or gray lips/fingernails, gurgling/choking sounds. WHEN IN DOUBT, GIVE IT — naloxone does nothing harmful if the person is not overdosing on opioids. Do not delay 911 call waiting to see if naloxone works.',
    danger_ko: '이것은 생명을 구하는 응급 약물입니다. 오피오이드 과량 징후: 음성·촉각에 무반응, 매우 느리거나 정지된 호흡(분당 10회 미만), 바늘끝처럼 작은 동공, 청색·회색 입술·손톱, 가르랑·숨막힘 소리. 의심되면 투여 — 오피오이드 과량이 아니어도 날록손은 해롭지 않음. 날록손 효과를 기다리느라 911 신고를 지연하지 마세요.',
    danger_ja: 'これは命を救う緊急薬です。オピオイド過量の徴候:声·触覚に無反応、非常に遅いまたは停止した呼吸(毎分10回未満)、針先のように小さな瞳孔、青色·灰色の唇·爪、ゴロゴロ·窒息音。疑わしい場合は投与 — オピオイド過量でなくてもナロキソンは無害。ナロキソンの効果を待って911通報を遅らせないでください。',
    warn_en: 'After naloxone, person may experience acute opioid withdrawal: agitation, vomiting, sweating, rapid heart rate, tremor — uncomfortable but not dangerous. Keep them on their side to prevent aspiration if vomiting. Person may try to use more opioids when withdrawal hits — do not let them; stay until EMS arrives. Good Samaritan laws in every U.S. state protect both the administrator and the overdose victim from arrest for drug possession when calling 911. Store at room temperature; check expiration date periodically.',
    warn_ko: '날록손 투여 후 급성 오피오이드 금단 증상 가능: 흥분, 구토, 발한, 빠른 심박수, 떨림 — 불편하나 위험하지 않음. 구토 시 흡인 방지를 위해 옆으로 눕힘. 금단이 시작되면 대상자가 더 많은 오피오이드를 사용하려 할 수 있음 — 막고 응급 대원 도착까지 동행. 미국 모든 주의 선한 사마리아인법이 911 신고 시 투여자와 과량 복용자를 약물 소지로 인한 체포로부터 보호. 실온 보관; 유효기간 주기적 확인.',
    warn_ja: 'ナロキソン投与後、急性オピオイド離脱症状の可能性:興奮、嘔吐、発汗、頻脈、振戦 — 不快だが危険ではない。嘔吐時の誤嚥防止のため横向きに寝かせる。離脱が始まると患者が更にオピオイドを使おうとする可能性 — 阻止し救急隊到着まで付き添う。米国全州の善きサマリア人法が911通報時の投与者と過量服用者を薬物所持での逮捕から保護。室温保管;有効期限を定期確認。',
    interact: [
      { en: 'Opioids (morphine, oxycodone, hydrocodone, fentanyl, heroin, methadone, tramadol, codeine) — naloxone blocks and reverses', ko: '오피오이드 (모르핀, 옥시코돈, 하이드로코돈, 펜타닐, 헤로인, 메타돈, 트라마돌, 코데인) — 날록손이 차단·역전', ja: 'オピオイド(モルヒネ、オキシコドン、ヒドロコドン、フェンタニル、ヘロイン、メサドン、トラマドール、コデイン) — ナロキソンが遮断·反転' },
      { en: 'Buprenorphine — naloxone may have reduced effect; may need multiple doses', ko: '부프레노르핀 — 날록손 효과가 감소할 수 있으며 여러 번 투여 필요 가능', ja: 'ブプレノルフィン — ナロキソン効果が減少の可能性;複数回投与が必要な場合あり' },
      { en: 'Non-opioid overdoses (benzodiazepines, alcohol, stimulants) — naloxone will NOT help but is harmless; still call 911', ko: '비오피오이드 과량 (벤조디아제핀, 알코올, 자극제) — 날록손은 효과 없으나 해롭지 않음; 그래도 911 신고', ja: '非オピオイド過量(ベンゾジアゼピン、アルコール、刺激薬) — ナロキソンは無効だが無害;それでも911通報' },
      { en: 'Chronic opioid users — naloxone precipitates severe withdrawal; use minimum effective dose, expect severe reaction', ko: '만성 오피오이드 사용자 — 날록손이 중증 금단 촉발; 최소 유효 용량 사용, 중증 반응 예상', ja: '慢性オピオイド使用者 — ナロキソンが重度離脱を誘発;最小有効量を使用、重度反応を予期' }
    ],
    source: 'FDA OTC approval March 2023 · SAMHSA Naloxone Resource · CDC Overdose Prevention Guidelines'
  },
  {
    id: 'styptic-pencil',
    generic: { en: 'Styptic pencil / aluminum sulfate (minor bleeding)', ko: '지혈 연필·황산알루미늄 (경미한 출혈)', ja: '止血ペンシル·硫酸アルミニウム(軽度の出血)' },
    brands: ['Clubman Styptic Pencil', 'Pinaud Styptic Pencil', "Kelo-Cote (different product — scar gel)"],
    category: 'first_aid',
    uses: [
      { title_en: 'Stop minor shaving cuts and small nicks', title_ko: '면도 절창·작은 상처 지혈', title_ja: '髭剃り切創·小さな傷の止血',
        detail_en: 'Aluminum sulfate or potassium alum causes protein coagulation and mild vasoconstriction on contact, stopping bleeding from shallow cuts within seconds',
        detail_ko: '황산알루미늄 또는 칼륨백반이 접촉 시 단백질 응고와 경미한 혈관수축을 유발하여 얕은 절창의 출혈을 수초 내 중단',
        detail_ja: '硫酸アルミニウムまたはカリウムミョウバンが接触時に蛋白凝固と軽度血管収縮を起こし、浅い切創の出血を数秒以内に止める' }
    ],
    dose_en: { 'Application': 'Moisten pencil tip with water, press onto clean wound for 3–5 seconds; may sting briefly', 'Duration': 'Single application usually sufficient; can repeat if bleeding restarts', 'For larger cuts': 'Use direct pressure with clean cloth for 10+ minutes; if bleeding persists, seek care', 'Care of the pencil': 'Rinse with water and dry between uses; replace if contaminated' },
    dose_ko: { '사용법': '연필 끝을 물로 적신 후 깨끗한 상처에 3~5초 압박; 일시적 따가움 가능', '기간': '1회 도포로 충분한 경우가 많음; 재출혈 시 반복 가능', '큰 절창': '깨끗한 천으로 10분 이상 직접 압박; 출혈 지속 시 진료', '연필 관리': '사용 사이 물로 헹구고 건조; 오염 시 교체' },
    dose_ja: { '使用法': 'ペンシル先端を水で湿らせ清潔な傷に3~5秒押し当てる;一時的にしみる可能性', '期間': '1回塗布で通常十分;再出血時は反復可能', '大きな切創': '清潔な布で10分以上直接圧迫;出血が続く場合は受診', 'ペンシル管理': '使用間に水で洗い乾燥;汚染時は交換' },
    warn_en: 'Not for deep cuts, puncture wounds, or wounds with embedded debris — these need cleaning and sometimes sutures. Wounds that do not stop bleeding after 10–15 minutes of firm direct pressure, bleed through multiple bandages, or spurt (arterial) — apply pressure and go to emergency room. Do not use on eyes or mucous membranes. Single-use alternative: aluminum chloride liquid styptic applied with cotton swab.',
    warn_ko: '깊은 절창, 관통상, 이물이 박힌 상처에 사용 금지 — 세척 및 경우에 따라 봉합 필요. 10~15분 이상 단단히 직접 압박해도 출혈이 멈추지 않거나, 여러 붕대를 관통하거나, 뿜어 나오는(동맥성) 출혈 — 압박 유지하며 응급실 방문. 눈이나 점막에 사용 금지. 1회용 대안: 면봉으로 도포하는 염화알루미늄 지혈액.',
    warn_ja: '深い切創、刺し傷、異物が埋まった傷には使用禁止 — 洗浄および場合により縫合必要。10~15分以上しっかり直接圧迫しても出血が止まらない、複数の包帯を貫通する、または噴出する(動脈性)出血 — 圧迫を維持し救急受診。眼や粘膜には使用禁止。使い捨て代替:綿棒で塗布する塩化アルミニウム液状止血剤。',
    interact: [
      { en: 'Anticoagulant medications (warfarin, apixaban, dabigatran, rivaroxaban, aspirin, clopidogrel) — bleeding may be harder to control; consider medical care for any cut that persists more than a few minutes', ko: '항응고제 (와파린, 엘리퀴스, 프라닥사, 자렐토, 아스피린, 클로피도그렐) — 출혈 조절이 어려울 수 있음; 수분 이상 지속되는 절창은 진료 고려', ja: '抗凝固薬(ワーファリン、エリキュース、プラザキサ、イグザレルト、アスピリン、クロピドグレル) — 出血制御が困難になる可能性;数分以上続く切創は受診を検討' },
      { en: 'Local anesthetic creams — do not apply to fresh bleeding wound before attempting hemostasis', ko: '국소 마취 크림 — 지혈 시도 전 신선 출혈 상처에 도포 금지', ja: '局所麻酔クリーム — 止血試行前の新鮮出血創への塗布禁止' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH)'
  },
  {
    id: 'after-bite-stick',
    generic: { en: 'Insect bite / sting relief (ammonia, baking soda, topical products)', ko: '벌레 물림·쏘임 완화제 (암모니아, 베이킹소다, 국소 제품)', ja: '虫刺され·刺傷緩和剤(アンモニア、重曹、外用製品)' },
    brands: ['After Bite Original (ammonia pen)', 'StingEze', 'Sting-Kill (benzocaine/menthol)', 'generic hydrocortisone 1%'],
    category: 'first_aid',
    uses: [
      { title_en: 'Itching and mild pain from mosquito, gnat, flea, fly, or small bee/wasp sting', title_ko: '모기·진드기·벼룩·파리·작은 벌·말벌에 의한 가려움·경미한 통증', title_ja: '蚊·ブヨ·ノミ·ハエ·小さなハチ·スズメバチによるかゆみ·軽度の痛み',
        detail_en: 'Ammonia-based pens neutralize insect venom chemistry; topical hydrocortisone reduces inflammation; benzocaine-menthol products provide local anesthetic cooling. Pick one approach based on dominant symptom (itch vs pain)',
        detail_ko: '암모니아 기반 펜은 곤충 독의 화학 성질을 중화; 국소 하이드로코르티손은 염증 감소; 벤조카인-멘톨 제품은 국소 마취 냉각. 주 증상(가려움 vs 통증)에 따라 한 가지 선택',
        detail_ja: 'アンモニア系ペンは昆虫毒の化学性質を中和;外用ヒドロコルチゾンは炎症軽減;ベンゾカイン·メントール製品は局所麻酔と冷却作用。主症状(かゆみ vs 痛み)に応じて一つを選択' }
    ],
    dose_en: { 'Immediate steps for any bite/sting': 'Remove stinger if present (scrape with credit card, do not squeeze), wash with soap and water, apply cold compress 10 minutes', 'After-bite pen (ammonia)': 'Apply directly to site as soon as possible', 'Hydrocortisone 1% cream': 'Thin layer 2–4 times daily for itch and inflammation', 'Oral antihistamine': 'Cetirizine 10 mg or loratadine 10 mg once daily for widespread reactions' },
    dose_ko: { '모든 물림·쏘임 초기 조치': '독침이 있으면 제거(신용카드로 긁기, 짜지 않기), 비누와 물로 세척, 냉찜질 10분', '애프터바이트 펜 (암모니아)': '가능한 빨리 해당 부위에 직접 도포', '하이드로코르티손 1% 크림': '가려움·염증에 하루 2~4회 얇게', '경구 항히스타민': '광범위 반응에 세티리진 10 mg 또는 로라타딘 10 mg 하루 1회' },
    dose_ja: { 'すべての刺傷·咬傷の初期対応': '針があれば除去(クレジットカードで擦る、つまんで搾らない)、石鹸と水で洗浄、冷湿布10分', 'アフターバイトペン(アンモニア)': '可能な限り早く患部に直接塗布', 'ヒドロコルチゾン1%クリーム': 'かゆみ·炎症に1日2~4回薄く', '経口抗ヒスタミン薬': '広範囲反応にセチリジン10 mgまたはロラタジン10 mg 1日1回' },
    danger_en: 'ANAPHYLAXIS EMERGENCY — for bee/wasp/hornet sting with signs of severe allergic reaction: swelling beyond sting site (face/throat), difficulty breathing, wheeze, hives spreading, vomiting, dizziness/fainting, rapid heart rate → use epinephrine auto-injector (if available) and CALL 911 IMMEDIATELY. History of severe reaction = carry epinephrine and seek allergist. For multiple stings (>10 in adult or >5 in child) or stings inside mouth/throat — also emergency.',
    danger_ko: '아나필락시스 응급 — 벌·말벌·호넷에 쏘인 후 중증 알레르기 징후: 쏘인 부위 넘어선 부종(얼굴·목), 호흡 곤란, 쌕쌕거림, 두드러기 확산, 구토, 어지럼·실신, 빠른 심박수 → 에피네프린 자동주사기 사용(있으면) 및 즉시 911. 중증 반응 병력 = 에피네프린 소지 및 알레르기 전문의 상담. 다발성 쏘임(성인 10회 초과, 소아 5회 초과) 또는 입·목 안 쏘임 — 역시 응급.',
    danger_ja: 'アナフィラキシー緊急 — ハチ·スズメバチ·クマバチに刺された後の重度アレルギー徴候:刺された部位を超える腫れ(顔·喉)、呼吸困難、喘鳴、じんま疹拡大、嘔吐、めまい·失神、頻脈 → エピネフリン自己注射器使用(あれば)および即時911通報。重度反応既往 = エピネフリン携帯およびアレルギー専門医受診。多数刺傷(成人10回超、小児5回超)または口·喉内の刺傷 — 同様に緊急。',
    warn_en: 'Tick bites: remove tick with fine-tipped tweezers by grasping close to skin and pulling steadily upward — do NOT burn, twist, or apply petroleum jelly. Save tick for identification. Monitor bite site for expanding red ring (erythema migrans) = Lyme disease, or unexplained fever/rash/flu symptoms for 30 days — see doctor promptly. Spider bites: most "spider bites" diagnosed clinically are actually MRSA skin infections — if pain worsens, pus develops, or skin necroses, see doctor.',
    warn_ko: '진드기 물림: 미세 핀셋으로 피부 가까이 잡고 꾸준히 위로 당겨 제거 — 불로 태우거나 돌리거나 바세린 도포 금지. 진드기 보관하여 동정. 물린 자리의 확산성 붉은 고리(이동 홍반) = 라임병, 또는 30일간 설명 안 되는 발열·발진·독감 증상 — 즉시 진료. 거미 물림: 임상적으로 "거미 물림"으로 진단되는 대부분은 실제 MRSA 피부감염 — 통증 악화, 고름, 피부 괴사 시 진료.',
    warn_ja: 'ダニ咬傷:細先ピンセットで皮膚近くをつかみ着実に上に引いて除去 — 燃やしたり、ねじったり、ワセリンを塗布しない。ダニを同定のため保存。咬傷部位の拡大する赤いリング(遊走性紅斑) = ライム病、または30日間続く原因不明の発熱·発疹·インフルエンザ様症状 — 速やかに受診。クモ咬傷:臨床的に「クモ咬傷」と診断されるものの多くは実際にはMRSA皮膚感染 — 痛みが悪化、膿が出る、皮膚が壊死する場合は受診。',
    interact: [
      { en: 'Benzocaine-containing products — methemoglobinemia risk in children and large areas', ko: '벤조카인 함유 제품 — 소아 및 넓은 부위에서 메트헤모글로빈혈증 위험', ja: 'ベンゾカイン含有製品 — 小児·広範囲でメトヘモグロビン血症リスク' },
      { en: 'Topical antihistamines (diphenhydramine cream) — do not combine with oral diphenhydramine (additive absorption)', ko: '국소 항히스타민 (디펜히드라민 크림) — 경구 디펜히드라민과 병용 금지 (흡수 가중)', ja: '外用抗ヒスタミン薬(ジフェンヒドラミンクリーム) — 経口ジフェンヒドラミンと併用禁止(吸収累積)' },
      { en: 'Topical hydrocortisone + topical antibiotic — can be layered for contaminated bites', ko: '국소 하이드로코르티손 + 국소 항생제 — 오염된 물림에 함께 도포 가능', ja: '外用ヒドロコルチゾン+外用抗生物質 — 汚染された咬傷に重ね塗り可能' }
    ],
    source: 'CDC Insect Bite and Tick Removal · AAP · DailyMed (NIH)'
  },

  // ============ EXISTING CATEGORIES — REINFORCEMENT ============
  {
    id: 'lansoprazole',
    generic: { en: 'Lansoprazole 15 mg (proton pump inhibitor)', ko: '란소프라졸 15 mg (양성자 펌프 억제제)', ja: 'ランソプラゾール15 mg(プロトンポンプ阻害薬)' },
    brands: ['Prevacid 24HR'],
    category: 'gi',
    uses: [
      { title_en: 'Frequent heartburn (2+ days per week)', title_ko: '잦은 속쓰림 (주 2회 이상)', title_ja: '頻繁な胸焼け(週2日以上)',
        detail_en: 'Suppresses gastric acid production by blocking H+/K+-ATPase in parietal cells; reduces heartburn, regurgitation, and helps heal erosive esophagitis. Takes 1–4 days for full effect',
        detail_ko: '벽세포의 H+/K+-ATPase 차단으로 위산 생성 억제; 속쓰림, 역류를 감소시키고 미란성 식도염 치유에 도움. 완전 효과까지 1~4일 소요',
        detail_ja: '壁細胞のH+/K+-ATPaseを阻害して胃酸分泌を抑制;胸焼け、逆流を軽減し、びらん性食道炎の治癒を助ける。完全な効果まで1~4日要する' }
    ],
    dose_en: { 'Adult': '15 mg once daily in the morning before eating', 'Course length (OTC)': '14 days; may repeat every 4 months; do not take for more than 14 consecutive days without doctor approval', 'Timing': '30–60 minutes before first meal of the day', 'Not for immediate relief': 'Use antacid (calcium carbonate) for rapid-onset symptom relief while waiting for PPI effect' },
    dose_ko: { '성인': '아침 식전 15 mg 하루 1회', '복용 기간 (OTC)': '14일; 4개월마다 반복 가능; 의사 승인 없이 14일 연속 초과 복용 금지', '복용 시점': '하루 첫 식사 30~60분 전', '즉각 완화 목적 아님': 'PPI 효과 대기 중 신속 완화는 제산제(탄산칼슘) 사용' },
    dose_ja: { '成人': '朝食前に1日1回15 mg', '服用期間(OTC)': '14日;4か月ごとに反復可能;医師の承認なく14日連続を超えて服用禁止', '服用時間': '1日最初の食事の30~60分前', '即時緩和用ではない': 'PPI効果待ちの間の迅速緩和は制酸薬(炭酸カルシウム)を使用' },
    warn_en: 'Long-term use (>1 year) associated with: vitamin B12 deficiency, magnesium deficiency, increased risk of bone fractures, C. difficile infection, pneumonia, and kidney inflammation. Not for immediate relief of heartburn — use calcium carbonate or famotidine for rapid onset. See a doctor if symptoms include unintended weight loss, difficulty swallowing, vomiting blood, black stools, or chest pain — could be serious condition needing endoscopy.',
    warn_ko: '장기 사용(1년 초과) 시 연관된 위험: 비타민 B12 결핍, 마그네슘 결핍, 골절 위험 증가, C. difficile 감염, 폐렴, 신장 염증. 속쓰림 즉각 완화용 아님 — 신속 발현은 탄산칼슘 또는 파모티딘. 의도하지 않은 체중 감소, 삼킴 곤란, 토혈, 흑색변, 흉통이 있으면 진료 — 내시경이 필요한 중대 질환 가능성.',
    warn_ja: '長期使用(1年超)で関連するリスク:ビタミンB12欠乏、マグネシウム欠乏、骨折リスク増加、C. difficile感染、肺炎、腎臓の炎症。胸焼けの即時緩和用ではない — 迅速な発現は炭酸カルシウムまたはファモチジン。意図しない体重減少、嚥下困難、吐血、黒色便、胸痛がある場合は受診 — 内視鏡が必要な重篤疾患の可能性。',
    interact: [
      { en: 'Clopidogrel — lansoprazole has less interaction than omeprazole; still consider H2 blocker if needed', ko: '클로피도그렐 — 오메프라졸보다 상호작용 적으나 필요시 H2 차단제 고려', ja: 'クロピドグレル — オメプラゾールより相互作用は少ないが必要時はH2ブロッカーを検討' },
      { en: 'Methotrexate — increased methotrexate levels with PPI', ko: '메토트렉세이트 — PPI와 병용 시 혈중 농도 증가', ja: 'メトトレキサート — PPI併用で血中濃度上昇' },
      { en: 'Atazanavir, rilpivirine, itraconazole, ketoconazole — require acidic stomach for absorption; PPIs reduce effectiveness', ko: '아타자나비르, 릴피비린, 이트라코나졸, 케토코나졸 — 산성 위 환경에서 흡수; PPI가 효과 감소', ja: 'アタザナビル、リルピビリン、イトラコナゾール、ケトコナゾール — 酸性胃環境で吸収;PPIで効果減少' },
      { en: 'Warfarin, digoxin — monitor levels with concurrent use', ko: '와파린, 디곡신 — 병용 시 혈중 농도 모니터링', ja: 'ワーファリン、ジゴキシン — 併用時は血中濃度モニタリング' },
      { en: 'Iron supplements, calcium carbonate — reduced absorption; separate by hours', ko: '철분 보충제, 탄산칼슘 — 흡수 감소; 수시간 간격', ja: '鉄剤、炭酸カルシウム — 吸収減少;数時間間隔' }
    ],
    source: 'FDA OTC labeling · DailyMed (NIH)'
  },
  {
    id: 'esomeprazole',
    generic: { en: 'Esomeprazole 20 mg (proton pump inhibitor)', ko: '에소메프라졸 20 mg (양성자 펌프 억제제)', ja: 'エソメプラゾール20 mg(プロトンポンプ阻害薬)' },
    brands: ['Nexium 24HR'],
    category: 'gi',
    uses: [
      { title_en: 'Frequent heartburn (2+ days per week)', title_ko: '잦은 속쓰림 (주 2회 이상)', title_ja: '頻繁な胸焼け(週2日以上)',
        detail_en: 'S-isomer of omeprazole with similar mechanism and efficacy; suppresses gastric acid for up to 24 hours per dose',
        detail_ko: '오메프라졸의 S-이성체로 기전과 효과가 유사; 1회 복용으로 최대 24시간 위산 억제',
        detail_ja: 'オメプラゾールのS-異性体で機序と有効性が類似;1回服用で最大24時間胃酸抑制' }
    ],
    dose_en: { 'Adult': '20 mg once daily in the morning before eating', 'Course length (OTC)': '14 days; may repeat every 4 months', 'Timing': '30–60 minutes before first meal of the day', 'Capsule handling': 'Swallow whole; if unable, open capsule and mix granules with applesauce — do not crush or chew' },
    dose_ko: { '성인': '아침 식전 20 mg 하루 1회', '복용 기간 (OTC)': '14일; 4개월마다 반복 가능', '복용 시점': '하루 첫 식사 30~60분 전', '캡슐 취급': '통째로 삼킴; 어려우면 캡슐 열어 과립을 사과소스와 섞음 — 분쇄·씹기 금지' },
    dose_ja: { '成人': '朝食前に1日1回20 mg', '服用期間(OTC)': '14日;4か月ごとに反復可能', '服用時間': '1日最初の食事の30~60分前', 'カプセル取扱い': '丸ごと飲む;困難な場合はカプセルを開け顆粒をアップルソースと混ぜる — 砕いたり噛んだりしない' },
    warn_en: 'Same long-term concerns as other PPIs: B12/magnesium deficiency, fracture risk, C. difficile, pneumonia, kidney inflammation. Esomeprazole is one of the most-prescribed drugs globally — used for treating GERD, erosive esophagitis, and H. pylori (in combination with antibiotics). Red flags that need doctor workup before OTC PPI use: age over 55 with new heartburn, difficulty swallowing, weight loss, vomiting blood, black stool, chest pain with exertion.',
    warn_ko: '다른 PPI와 동일한 장기 우려: B12·마그네슘 결핍, 골절 위험, C. difficile, 폐렴, 신장 염증. 에소메프라졸은 전 세계에서 가장 많이 처방되는 약 중 하나 — 역류, 미란성 식도염, H. pylori 치료(항생제 병용)에 사용. OTC PPI 사용 전 의사 평가가 필요한 경고 징후: 55세 이상 새로 생긴 속쓰림, 삼킴 곤란, 체중 감소, 토혈, 흑색변, 운동 시 흉통.',
    warn_ja: '他のPPIと同じ長期懸念:B12·マグネシウム欠乏、骨折リスク、C. difficile、肺炎、腎臓の炎症。エソメプラゾールは世界で最も多く処方される薬の一つ — GERD、びらん性食道炎、H. pylori治療(抗生物質併用)に使用。OTC PPI使用前に医師評価が必要な警告徴候:55歳以上の新規胸焼け、嚥下困難、体重減少、吐血、黒色便、運動時胸痛。',
    interact: [
      { en: 'Clopidogrel — esomeprazole significantly reduces clopidogrel activation; avoid combination (use H2 blocker or pantoprazole instead)', ko: '클로피도그렐 — 에소메프라졸이 클로피도그렐 활성화를 유의하게 감소시킴; 병용 피함 (H2 차단제 또는 판토프라졸 대신)', ja: 'クロピドグレル — エソメプラゾールがクロピドグレルの活性化を有意に減少;併用回避(H2ブロッカーまたはパントプラゾール代替)' },
      { en: 'Methotrexate, warfarin, digoxin, tacrolimus — may affect levels; monitor', ko: '메토트렉세이트, 와파린, 디곡신, 타크로리무스 — 혈중 농도에 영향; 모니터링', ja: 'メトトレキサート、ワーファリン、ジゴキシン、タクロリムス — 血中濃度に影響;モニタリング' },
      { en: 'Antiretrovirals (atazanavir, nelfinavir, rilpivirine) — reduced absorption; avoid combination', ko: '항레트로바이러스제 (아타자나비르, 넬피나비르, 릴피비린) — 흡수 감소; 병용 피함', ja: '抗レトロウイルス薬(アタザナビル、ネルフィナビル、リルピビリン) — 吸収減少;併用回避' },
      { en: 'Iron, calcium carbonate, antifungals (itraconazole, ketoconazole) — separate by hours due to absorption interaction', ko: '철분, 탄산칼슘, 항진균제 (이트라코나졸, 케토코나졸) — 흡수 상호작용으로 수시간 간격', ja: '鉄剤、炭酸カルシウム、抗真菌薬(イトラコナゾール、ケトコナゾール) — 吸収相互作用のため数時間間隔' }
    ],
    source: 'FDA OTC labeling · DailyMed (NIH)'
  },
  {
    id: 'docusate',
    generic: { en: 'Docusate sodium (stool softener)', ko: '도큐세이트 나트륨 (대변 연화제)', ja: 'ドクサートナトリウム(便軟化剤)' },
    brands: ['Colace', 'DulcoEase', 'Surfak (docusate calcium)'],
    category: 'gi',
    uses: [
      { title_en: 'Prevention of constipation in situations with increased risk', title_ko: '변비 위험이 높은 상황에서의 변비 예방', title_ja: '便秘リスクが高い状況での便秘予防',
        detail_en: 'Surfactant laxative that allows water and fat to mix with stool, softening it. Used for prevention (post-surgery, opioid users, pregnancy/postpartum, elderly with straining concern); evidence of efficacy is actually limited but widely used and well-tolerated',
        detail_ko: '계면활성제 하제로 수분과 지방이 대변과 섞이도록 하여 부드럽게 함. 예방 목적으로 사용(수술 후, 오피오이드 사용자, 임신·산후, 힘주기가 우려되는 노년층); 실제 효과 근거는 제한적이나 널리 사용되고 내약성 양호',
        detail_ja: '界面活性剤下剤で水分と脂肪が便と混ざり軟らかくする。予防目的で使用(手術後、オピオイド使用者、妊娠·産後、いきみが懸念される高齢者);実際の有効性エビデンスは限定的だが広く使用され忍容性良好' }
    ],
    dose_en: { 'Adult': '50–300 mg daily in 1–4 divided doses', 'Onset': '12–72 hours — stool softener, not a rapid laxative', 'Duration': 'Can be used daily for short periods; for chronic constipation, PEG (MiraLAX) has better evidence', 'With plenty of water': 'Requires adequate fluid intake to work — dehydration negates effect' },
    dose_ko: { '성인': '하루 50~300 mg, 1~4회 분할 복용', '효과 발현': '12~72시간 — 연화제이며 빠른 하제가 아님', '기간': '단기간 매일 사용 가능; 만성 변비에는 PEG(MiraLAX)가 더 나은 근거', '충분한 수분과 함께': '작용에 적절한 수분 섭취 필요 — 탈수는 효과 상쇄' },
    dose_ja: { '成人': '1日50~300 mg、1~4回に分割服用', '作用発現': '12~72時間 — 軟化剤であり速効性下剤ではない', '期間': '短期間の毎日使用可能;慢性便秘にはPEG(MiraLAX)がより優れたエビデンス', '十分な水分': '作用に適切な水分摂取必要 — 脱水で効果消失' },
    warn_en: 'For prevention of straining, not for acute relief of impaction. If no bowel movement for several days, abdominal pain, or rectal bleeding — see doctor; could be impaction requiring manual disimpaction or obstruction. Do not combine with mineral oil — docusate enhances mineral oil absorption, which can cause lipid pneumonia. Some evidence suggests docusate is no more effective than placebo for constipation — consider alternatives (PEG, senna, psyllium).',
    warn_ko: '힘주기 예방용이며 분변 매복의 급성 완화가 아님. 수일간 배변 없음, 복통, 직장 출혈 시 진료 — 매복(수동 제거 필요) 또는 폐색 가능성. 광물유(미네랄 오일)와 병용 금지 — 도큐세이트가 광물유 흡수 증가시켜 지질성 폐렴 유발 가능. 일부 연구에서 도큐세이트가 변비에 위약 대비 효과 없다는 근거 — 대안 고려(PEG, 센나, 차전자피).',
    warn_ja: 'いきみ予防用であり糞便嵌入の急性緩和ではない。数日間排便なし、腹痛、直腸出血時は受診 — 嵌入(用手摘便必要)または閉塞の可能性。鉱油(ミネラルオイル)と併用禁止 — ドクサートが鉱油吸収を増加させ脂質性肺炎を起こす可能性。一部の研究でドクサートが便秘に対しプラセボと同等とのエビデンス — 代替を検討(PEG、センナ、サイリウム)。',
    interact: [
      { en: 'Mineral oil — enhanced absorption of mineral oil; lipid pneumonia risk', ko: '광물유 — 광물유 흡수 증가; 지질성 폐렴 위험', ja: '鉱油 — 鉱油吸収増加;脂質性肺炎リスク' },
      { en: 'Fat-soluble vitamins (A, D, E, K) — may reduce absorption with chronic use', ko: '지용성 비타민 (A, D, E, K) — 만성 사용 시 흡수 감소 가능', ja: '脂溶性ビタミン(A、D、E、K) — 慢性使用で吸収減少の可能性' },
      { en: 'Phenolphthalein, other stimulant laxatives — can be combined short term but avoid chronic combinations', ko: '페놀프탈레인, 기타 자극성 하제 — 단기 병용 가능하나 만성 병용 피함', ja: 'フェノールフタレイン、他の刺激性下剤 — 短期併用可能だが慢性併用は回避' }
    ],
    source: 'FDA OTC Monograph 21 CFR 334 · DailyMed (NIH) · AGA guidance'
  },
  {
    id: 'senna',
    generic: { en: 'Senna (stimulant laxative)', ko: '센나 (자극성 하제)', ja: 'センナ(刺激性下剤)' },
    brands: ['Senokot', 'Ex-Lax (sennosides)', 'Fletcher\'s Castoria (children\'s)'],
    category: 'gi',
    uses: [
      { title_en: 'Occasional constipation', title_ko: '일시적 변비', title_ja: '一時的な便秘',
        detail_en: 'Plant-derived anthraquinone glycosides converted by colonic bacteria to active compounds that stimulate colonic motility. Produces a bowel movement in 6–12 hours; useful for occasional constipation when bulk laxatives or osmotic agents are ineffective',
        detail_ko: '식물 유래 안트라퀴논 글리코시드가 대장 세균에 의해 활성 화합물로 전환되어 대장 운동성 자극. 6~12시간 내 배변 유발; 팽창성 하제나 삼투압 하제가 효과 없을 때 일시적 변비에 유용',
        detail_ja: '植物由来のアントラキノン配糖体が大腸細菌により活性化合物に変換され大腸運動性を刺激。6~12時間以内に排便を促す;膨張性下剤や浸透圧下剤が無効な一時的便秘に有用' }
    ],
    dose_en: { 'Adult': '17.2–34.4 mg sennosides orally at bedtime for morning bowel movement', 'Max per day': '68.8 mg', 'Child 6–11': '8.6–17.2 mg at bedtime (consult doctor)', 'Child 2–5': '3.75–8.6 mg (consult doctor)', 'Duration': 'Not more than 7 days without doctor approval' },
    dose_ko: { '성인': '취침 시 센노사이드 17.2~34.4 mg 경구 복용 → 아침 배변', '하루 최대': '68.8 mg', '소아 6~11세': '취침 시 8.6~17.2 mg (의사 상담)', '소아 2~5세': '3.75~8.6 mg (의사 상담)', '기간': '의사 승인 없이 7일 초과 사용 금지' },
    dose_ja: { '成人': '就寝時にセンノシド17.2~34.4 mg経口 → 朝の排便', '1日最大量': '68.8 mg', '小児6~11歳': '就寝時に8.6~17.2 mg(医師相談)', '小児2~5歳': '3.75~8.6 mg(医師相談)', '期間': '医師の承認なく7日超使用禁止' },
    danger_en: 'DO NOT USE FOR WEIGHT LOSS. Chronic use causes melanosis coli (pigmentation of the colon, reversible but concerning), electrolyte imbalance (hypokalemia), dehydration, and in extreme cases "cathartic colon" (loss of normal peristalsis). Eating disorders and excessive laxative use can cause cardiac arrhythmias and death. Signs of laxative abuse warrant immediate professional help.',
    danger_ko: '체중 감량 목적 사용 금지. 만성 사용 시 대장 흑색증(대장 색소 침착, 가역적이나 우려됨), 전해질 불균형(저칼륨혈증), 탈수, 극단적 경우 "완하제 대장"(정상 연동 상실) 유발. 섭식장애와 과도한 하제 사용은 부정맥과 사망 유발 가능. 하제 남용 징후는 즉시 전문가 도움 필요.',
    danger_ja: '体重減少目的での使用禁止。慢性使用で大腸メラノーシス(大腸色素沈着、可逆性だが懸念)、電解質不均衡(低カリウム血症)、脱水、極端な場合「瀉下大腸」(正常蠕動消失)を引き起こす。摂食障害と過度の下剤使用は不整脈と死亡を起こす可能性。下剤乱用の徴候は即時専門家の援助が必要。',
    warn_en: 'Do not use in intestinal obstruction, appendicitis, abdominal pain of unknown cause, rectal bleeding, or inflammatory bowel disease flare. Avoid in pregnancy unless approved by obstetrician (small amounts in breast milk are generally considered safe). Expect yellow-brown or pink-red urine (harmless). Abdominal cramping is common — if severe, reduce dose.',
    warn_ko: '장폐색, 충수염, 원인 불명 복통, 직장 출혈, 염증성 장질환 악화 시 사용 금지. 임신 중 산부인과 의사 승인 없이 피함(모유 내 소량은 일반적으로 안전). 황갈색·분홍빨강 소변 정상(무해). 복통 흔함 — 심하면 용량 감소.',
    warn_ja: '腸閉塞、虫垂炎、原因不明の腹痛、直腸出血、炎症性腸疾患増悪時は使用禁止。妊娠中は産科医の承認なく回避(母乳中の少量は一般的に安全)。黄褐色·ピンク赤色の尿は正常(無害)。腹部のけいれんは一般的 — 重度なら減量。',
    interact: [
      { en: 'Digoxin — hypokalemia from chronic senna use increases digoxin toxicity', ko: '디곡신 — 만성 센나 사용으로 인한 저칼륨혈증이 디곡신 독성 증가', ja: 'ジゴキシン — 慢性センナ使用による低カリウム血症がジゴキシン毒性を増加' },
      { en: 'Diuretics (furosemide, thiazides) — additive hypokalemia', ko: '이뇨제 (푸로세미드, 티아지드) — 저칼륨혈증 가중', ja: '利尿薬(フロセミド、チアジド) — 低カリウム血症の累積' },
      { en: 'Warfarin — possible reduced absorption if rapid transit; monitor INR', ko: '와파린 — 빠른 통과로 흡수 감소 가능; INR 모니터링', ja: 'ワーファリン — 速い通過で吸収減少の可能性;INRモニタリング' },
      { en: 'Oral contraceptives — theoretically reduced absorption with diarrhea', ko: '경구 피임제 — 설사 시 이론적 흡수 감소', ja: '経口避妊薬 — 下痢時に理論的に吸収減少' }
    ],
    source: 'FDA OTC Monograph 21 CFR 334 · DailyMed (NIH)'
  },
  {
    id: 'psyllium',
    generic: { en: 'Psyllium husk (bulk-forming fiber laxative)', ko: '차전자피 (팽창성 섬유 하제)', ja: 'サイリウム種皮(膨張性食物繊維下剤)' },
    brands: ['Metamucil', 'Konsyl', 'Fiberall', 'generic psyllium husk powder'],
    category: 'gi',
    uses: [
      { title_en: 'Chronic or occasional constipation', title_ko: '만성·일시적 변비', title_ja: '慢性·一時的便秘',
        detail_en: 'Soluble fiber absorbs water in the gut forming a gel that softens and bulks the stool; first-line non-pharmacological management of constipation. Effect develops over 12–72 hours; more effective with regular use',
        detail_ko: '가용성 섬유가 장내 수분을 흡수하여 대변을 부드럽고 부피 있게 만드는 젤 형성; 변비의 1차 비약물 관리. 12~72시간에 걸쳐 효과; 규칙적 사용 시 더 효과적',
        detail_ja: '水溶性食物繊維が腸内で水分を吸収し便を軟らかく嵩を増すゲルを形成;便秘の第一選択非薬物管理。12~72時間にわたり効果;規則的使用でより有効' },
      { title_en: 'Mild diarrhea (bulking effect)', title_ko: '경미한 설사 (부피 조절 작용)', title_ja: '軽度下痢(嵩調節作用)',
        detail_en: 'Paradoxically helpful for mild diarrhea by absorbing excess water and firming stool; useful in IBS-mixed type',
        detail_ko: '여분의 수분을 흡수하여 대변을 단단하게 하여 경미한 설사에 역설적으로 도움; IBS 혼합형에 유용',
        detail_ja: '余分な水分を吸収し便を硬くし軽度下痢に逆説的に有用;IBS混合型に有用' },
      { title_en: 'Cholesterol reduction', title_ko: '콜레스테롤 감소', title_ja: 'コレステロール低下',
        detail_en: 'FDA-authorized health claim: 7 g/day of soluble fiber from psyllium may reduce LDL cholesterol when combined with a low-fat diet',
        detail_ko: 'FDA 승인 건강 강조 표시: 저지방 식이와 함께 차전자피 가용성 섬유 하루 7 g이 LDL 콜레스테롤 감소 가능',
        detail_ja: 'FDA承認健康強調表示:低脂肪食と組み合わせたサイリウム水溶性食物繊維1日7 gがLDLコレステロールを低下させる可能性' }
    ],
    dose_en: { 'Starting dose': '3.4 g (1 teaspoon or rounded packet) mixed in 8 oz (240 mL) water, 1–3 times daily', 'Maintenance': 'Increase gradually to 10–15 g/day as tolerated', 'Take with plenty of water': '8+ oz per dose; follow with another glass', 'Timing': 'Separate from other medications by 2 hours', 'Cholesterol claim': '7 g of soluble fiber daily from psyllium' },
    dose_ko: { '시작 용량': '3.4 g(1 티스푼 또는 반올림 포장) 물 240 mL에 섞어 하루 1~3회', '유지 용량': '내약성에 따라 점차 하루 10~15 g까지 증량', '충분한 물과 함께': '용량당 240 mL 이상; 한 잔 더 추가 음용', '복용 시점': '다른 약과 2시간 간격', '콜레스테롤 강조 표시': '차전자피 가용성 섬유 하루 7 g' },
    dose_ja: { '開始用量': '3.4 g(小さじ1杯または袋)を水240 mLに混ぜ1日1~3回', '維持用量': '忍容性に応じて徐々に1日10~15 gまで増量', '十分な水と共に': '1回240 mL以上;追加でもう1杯飲む', '服用タイミング': '他の薬と2時間間隔', 'コレステロール強調表示': 'サイリウム水溶性食物繊維1日7 g' },
    danger_en: 'CHOKING AND ESOPHAGEAL OBSTRUCTION RISK — must be taken with adequate water. Swelling with insufficient liquid can cause esophageal or intestinal blockage. Do not take if you have difficulty swallowing. Contraindicated in intestinal obstruction or severe constipation with impaction. Rare but potentially fatal allergic reaction — stop immediately for breathing difficulty or hives.',
    danger_ko: '질식 및 식도 폐쇄 위험 — 반드시 충분한 물과 함께 복용. 수분 부족 시 팽창으로 식도·장 폐쇄 가능. 삼킴 곤란 시 사용 금지. 장폐색 또는 중증 매복 변비 금기. 드물지만 치명적 알레르기 반응 가능 — 호흡 곤란·두드러기 시 즉시 중단.',
    danger_ja: '窒息および食道閉塞リスク — 必ず十分な水と共に服用。水分不足で膨張による食道·腸閉塞の可能性。嚥下困難時は使用禁止。腸閉塞または重度嵌入便秘は禁忌。稀だが致命的アレルギー反応の可能性 — 呼吸困難·じんま疹時は即時中止。',
    warn_en: 'Start low and increase slowly to reduce gas and bloating (common in first week). Benefit requires consistent daily use. Not a quick fix — for acute constipation needing immediate relief, use PEG or senna instead. Chronic abdominal pain, rectal bleeding, unexplained weight loss, or change in bowel habits lasting over 2 weeks warrant evaluation before assuming benign constipation.',
    warn_ko: '가스·복부 팽만 감소를 위해 저용량으로 시작하여 서서히 증량(첫 주에 흔함). 효과는 꾸준한 매일 사용 필요. 즉효 치료 아님 — 즉각 완화가 필요한 급성 변비는 PEG 또는 센나 사용. 만성 복통, 직장 출혈, 설명 안 되는 체중 감소, 2주 이상 배변 습관 변화는 양성 변비로 가정하기 전 평가 필요.',
    warn_ja: 'ガス·腹部膨満軽減のため低用量で開始し徐々に増量(初週によくある)。効果には継続的な毎日使用が必要。即効治療ではない — 即時緩和が必要な急性便秘にはPEGまたはセンナを使用。慢性腹痛、直腸出血、原因不明の体重減少、2週間以上続く排便習慣変化は良性便秘と仮定する前に評価が必要。',
    interact: [
      { en: 'ALL oral medications — separate by at least 2 hours; fiber binds many drugs and reduces absorption', ko: '모든 경구 약물 — 최소 2시간 간격; 섬유가 많은 약물과 결합하여 흡수 감소', ja: 'すべての経口薬 — 最低2時間間隔;食物繊維が多くの薬と結合し吸収減少' },
      { en: 'Levothyroxine, lithium, digoxin, warfarin, carbamazepine — particularly vulnerable to reduced absorption', ko: '레보티록신, 리튬, 디곡신, 와파린, 카바마제핀 — 흡수 감소에 특히 취약', ja: 'レボチロキシン、リチウム、ジゴキシン、ワーファリン、カルバマゼピン — 吸収減少に特に脆弱' },
      { en: 'Diabetes medications — fiber slows glucose absorption; monitor blood sugar', ko: '당뇨 약 — 섬유가 포도당 흡수 감소; 혈당 모니터링', ja: '糖尿病薬 — 食物繊維がブドウ糖吸収を遅延;血糖モニタリング' },
      { en: 'Iron, calcium, zinc supplements — reduced absorption; separate doses', ko: '철분, 칼슘, 아연 보충제 — 흡수 감소; 복용 간격 두기', ja: '鉄、カルシウム、亜鉛サプリメント — 吸収減少;服用間隔をあける' }
    ],
    source: 'FDA Health Claim 21 CFR 101.81 · DailyMed (NIH) · AGA Clinical Practice Update'
  },
  {
    id: 'terbinafine',
    generic: { en: 'Terbinafine 1% cream (antifungal)', ko: '테르비나핀 1% 크림 (항진균제)', ja: 'テルビナフィン1%クリーム(抗真菌薬)' },
    brands: ['Lamisil AT', 'generic terbinafine HCl 1% cream'],
    category: 'skin',
    uses: [
      { title_en: 'Athlete\'s foot (tinea pedis)', title_ko: '무좀 (족부 백선)', title_ja: '水虫(足白癬)',
        detail_en: 'Allylamine antifungal — kills fungus rather than just inhibiting it; shorter treatment course (1 week) than azoles (miconazole/clotrimazole, 4 weeks). More effective for chronic moccasin-type athlete\'s foot',
        detail_ko: '알릴아민계 항진균제 — 억제가 아닌 살균 작용; 아졸계(미코나졸·클로트리마졸 4주)보다 짧은 치료 기간(1주). 만성 모카신형 무좀에 더 효과적',
        detail_ja: 'アリルアミン系抗真菌薬 — 抑制ではなく殺真菌作用;アゾール系(ミコナゾール·クロトリマゾール4週間)より短い治療期間(1週間)。慢性モカシン型水虫により有効' },
      { title_en: 'Jock itch (tinea cruris) and ringworm (tinea corporis)', title_ko: '완선·체부 백선', title_ja: 'いんきんたむし·体部白癬',
        detail_en: 'Effective for groin and body ringworm; typically 1–2 weeks of treatment',
        detail_ko: '사타구니와 몸의 백선에 효과; 보통 1~2주 치료',
        detail_ja: '鼠径部と体の白癬に有効;通常1~2週間の治療' }
    ],
    dose_en: { 'Athlete\'s foot between toes': 'Apply to clean, dry skin twice daily for 1 week', 'Athlete\'s foot on sole/sides (moccasin)': 'Apply twice daily for 2 weeks', 'Jock itch, ringworm': 'Apply once daily for 1 week', 'Continue after symptoms resolve': 'Complete full course even if symptoms improve; recurrence is common if stopped early' },
    dose_ko: { '발가락 사이 무좀': '깨끗하고 건조한 피부에 하루 2회 1주간', '발바닥·측면 무좀 (모카신형)': '하루 2회 2주간', '완선·백선': '하루 1회 1주간', '증상 호전 후에도 지속': '증상이 나아져도 전체 기간 완료; 조기 중단 시 재발 흔함' },
    dose_ja: { '足指間水虫': '清潔で乾燥した皮膚に1日2回1週間塗布', '足底·側面水虫(モカシン型)': '1日2回2週間', 'いんきんたむし·白癬': '1日1回1週間', '症状改善後も継続': '症状改善後も全期間完了;早期中止で再発が多い' },
    warn_en: 'For topical use only — oral terbinafine (prescription) has liver toxicity risk and requires monitoring. If no improvement in 2 weeks (tinea pedis) or 1 week (jock itch, ringworm), see a doctor — may not be fungal, or may need prescription oral antifungal. Does not treat nail fungus (onychomycosis) effectively — topical treatment of nail fungus has very low cure rate; see doctor for oral therapy if desired.',
    warn_ko: '외용 전용 — 경구 테르비나핀(처방)은 간 독성 위험이 있고 모니터링 필요. 2주(무좀) 또는 1주(완선·백선) 내 개선 없으면 진료 — 진균이 아닐 수 있고 경구 처방 항진균제가 필요할 수 있음. 조갑 백선(손발톱 진균)은 효과적으로 치료하지 못함 — 외용 치료는 완치율 매우 낮음; 원하면 경구 치료 위해 진료.',
    warn_ja: '外用専用 — 経口テルビナフィン(処方)は肝毒性リスクがありモニタリング必要。2週間(水虫)または1週間(いんきんたむし·白癬)で改善なければ受診 — 真菌でない可能性、または経口処方抗真菌薬が必要な可能性。爪白癬には効果的でない — 外用治療は治癒率が非常に低い;希望なら経口治療のため受診。',
    interact: [
      { en: 'Topical use has minimal systemic absorption — no significant systemic drug interactions', ko: '외용 시 전신 흡수 최소 — 유의한 전신 약물 상호작용 없음', ja: '外用使用では全身吸収最小 — 有意な全身薬物相互作用なし' },
      { en: 'Other topical products — apply terbinafine first, let absorb before other products', ko: '기타 외용 제품 — 테르비나핀 먼저 도포, 흡수된 후 다른 제품', ja: '他の外用製品 — テルビナフィンを先に塗布、吸収後に他の製品' },
      { en: 'Occlusive dressings — do not cover with airtight wrap (increases absorption and irritation)', ko: '밀폐 드레싱 — 공기가 차단되는 랩으로 덮지 않음 (흡수·자극 증가)', ja: '密封包帯 — 気密ラップで覆わない(吸収·刺激増加)' }
    ],
    source: 'FDA OTC Monograph 21 CFR 333 · DailyMed (NIH) · AAD'
  },
  {
    id: 'ketoconazole-shampoo',
    generic: { en: 'Ketoconazole 1% shampoo (antifungal)', ko: '케토코나졸 1% 샴푸 (항진균 샴푸)', ja: 'ケトコナゾール1%シャンプー(抗真菌シャンプー)' },
    brands: ['Nizoral A-D', 'generic ketoconazole 1% shampoo'],
    category: 'skin',
    uses: [
      { title_en: 'Dandruff and seborrheic dermatitis', title_ko: '비듬·지루성 피부염', title_ja: 'ふけ·脂漏性皮膚炎',
        detail_en: 'Antifungal shampoo that targets Malassezia furfur yeast, a primary contributor to dandruff and seborrheic dermatitis. Reduces flaking, itching, and oiliness of the scalp',
        detail_ko: '비듬과 지루성 피부염의 주요 원인균인 Malassezia furfur 효모에 작용하는 항진균 샴푸. 두피의 비듬, 가려움, 기름기 감소',
        detail_ja: 'ふけと脂漏性皮膚炎の主要原因菌であるマラセチア·ファーファー酵母に作用する抗真菌シャンプー。頭皮のふけ、かゆみ、油っぽさを軽減' },
      { title_en: 'Tinea versicolor (body)', title_ko: '어루러기 (몸)', title_ja: '癜風(でんぷう)',
        detail_en: 'Effective for tinea versicolor — discolored patches on chest, back, shoulders caused by Malassezia. Apply to affected skin, leave 5 minutes, rinse',
        detail_ko: 'Malassezia가 유발하는 가슴·등·어깨의 색조 변화 — 어루러기에 효과. 해당 피부에 도포 후 5분 방치, 헹굼',
        detail_ja: 'マラセチアが起こす胸·背中·肩の色調変化 — 癜風に有効。患部に塗布後5分放置、すすぐ' }
    ],
    dose_en: { 'Dandruff (scalp)': 'Wash hair with regular shampoo, then apply 1% ketoconazole shampoo, lather, leave 3–5 minutes, rinse; twice weekly for 2–4 weeks, then weekly for maintenance', 'Tinea versicolor': 'Apply to wet skin, lather, leave 5 minutes, rinse; daily for 5 days', 'Not for daily use': 'Over-drying and scalp irritation; follow label' },
    dose_ko: { '비듬 (두피)': '일반 샴푸로 먼저 감은 후 1% 케토코나졸 샴푸 도포, 거품 내고 3~5분 방치, 헹굼; 주 2회 2~4주간, 이후 유지 목적 주 1회', '어루러기': '젖은 피부에 도포, 거품 내고 5분 방치, 헹굼; 하루 1회 5일간', '매일 사용 금지': '과도한 건조·두피 자극; 라벨 준수' },
    dose_ja: { 'ふけ(頭皮)': '通常シャンプーで先に洗髪後1%ケトコナゾールシャンプーを塗布、泡立て3~5分放置、すすぐ;週2回2~4週間、その後は維持目的で週1回', '癜風': '濡れた皮膚に塗布、泡立て5分放置、すすぐ;1日1回5日間', '毎日使用禁止': '過度の乾燥·頭皮刺激;ラベル遵守' },
    warn_en: 'Does not treat tinea capitis (scalp ringworm, mostly in children) — this is a true dermatophyte infection needing oral antifungal (prescription). If scalp has patches of hair loss, scaly plaques, or swollen lymph nodes behind ears, see a dermatologist. Rare hair discoloration or texture change reported; discontinue if severe. Avoid eyes and mucous membranes.',
    warn_ko: '두부 백선(주로 소아의 두피 백선)은 치료하지 않음 — 이는 진정한 피부사상균 감염으로 경구 항진균제(처방) 필요. 두피에 탈모 반, 각질성 판, 귀 뒤 림프절 부종이 있으면 피부과 진료. 드물게 모발 탈색·질감 변화 보고; 심하면 중단. 눈·점막 회피.',
    warn_ja: '頭部白癬(主に小児の頭皮白癬)は治療しない — これは真の皮膚糸状菌感染で経口抗真菌薬(処方)が必要。頭皮に脱毛斑、鱗屑性局面、耳後リンパ節腫脹がある場合は皮膚科受診。稀に毛髪脱色·質感変化の報告;重度なら中止。目·粘膜を避ける。',
    interact: [
      { en: 'Other topical scalp products (tar shampoo, salicylic acid, selenium sulfide) — can rotate or combine, but watch for over-drying', ko: '기타 두피 외용 제품 (타르 샴푸, 살리실산, 이황화셀레늄) — 교대 또는 병용 가능하나 과건조 주의', ja: '他の頭皮外用製品(タールシャンプー、サリチル酸、二硫化セレン) — ローテーションまたは併用可能だが過乾燥に注意' },
      { en: 'Topical steroid (hydrocortisone) for scalp — can complement ketoconazole for seborrheic dermatitis; apply steroid to patches after shampoo', ko: '두피 외용 스테로이드 (하이드로코르티손) — 지루성 피부염에 케토코나졸 보완 가능; 샴푸 후 반에 스테로이드 도포', ja: '頭皮外用ステロイド(ヒドロコルチゾン) — 脂漏性皮膚炎にケトコナゾールを補完可能;シャンプー後に病変にステロイド塗布' },
      { en: 'Oral ketoconazole (prescription, now limited use) — carries liver toxicity, QT prolongation; topical ketoconazole has minimal absorption so no systemic interactions', ko: '경구 케토코나졸 (처방, 현재 사용 제한) — 간 독성, QT 연장; 외용 케토코나졸은 흡수 최소로 전신 상호작용 없음', ja: '経口ケトコナゾール(処方、現在は使用制限) — 肝毒性、QT延長を伴う;外用ケトコナゾールは吸収最小のため全身相互作用なし' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH) · AAD guidance on seborrheic dermatitis'
  },
  {
    id: 'salicylic-acid',
    generic: { en: 'Salicylic acid (acne, warts, psoriasis, calluses)', ko: '살리실산 (여드름·사마귀·건선·굳은살)', ja: 'サリチル酸(ニキビ·いぼ·乾癬·たこ)' },
    brands: ['Compound W (wart treatment)', 'Stridex (acne pads)', "Neutrogena Oil-Free Acne Wash", 'MG217 (psoriasis shampoo)', 'Dr. Scholl\'s Corn Removers'],
    category: 'skin',
    uses: [
      { title_en: 'Acne (mild comedonal and inflammatory)', title_ko: '여드름 (경미한 면포·염증성)', title_ja: 'ニキビ(軽度面皰·炎症性)',
        detail_en: 'Beta-hydroxy acid that penetrates oil-filled pores, breaks down keratin plugs, and has mild anti-inflammatory effect. 0.5–2% in face washes, toners, spot treatments; safer than benzoyl peroxide for darker skin (less pigmentation risk)',
        detail_ko: '유분으로 막힌 모공에 침투하여 각질 막음을 분해하며 경미한 항염 작용이 있는 베타하이드록시산. 세안제·토너·국소 제품에 0.5~2%; 벤조일 퍼옥사이드보다 짙은 피부에 안전(색소침착 위험 낮음)',
        detail_ja: '油で詰まった毛穴に浸透しケラチン栓を分解する軽度の抗炎症作用を持つベータヒドロキシ酸。洗顔料·化粧水·局所製品に0.5~2%;過酸化ベンゾイルより濃い肌に安全(色素沈着リスク低い)' },
      { title_en: 'Common warts and plantar warts', title_ko: '심상성 사마귀·족저 사마귀', title_ja: '尋常性いぼ·足底いぼ',
        detail_en: 'Keratolytic — removes layers of skin affected by HPV. 17% liquid or 40% patches; requires patience (weeks), cure rate higher than cryotherapy for some types',
        detail_ko: '각질용해제 — HPV에 감염된 피부층 제거. 17% 액체 또는 40% 패치; 인내 필요(수주), 일부 유형에서 냉동요법보다 완치율 높음',
        detail_ja: '角質溶解剤 — HPV感染皮膚層を除去。17%液体または40%パッチ;忍耐必要(数週間)、一部タイプで凍結療法より治癒率高い' },
      { title_en: 'Psoriasis scale reduction', title_ko: '건선 인설 감소', title_ja: '乾癬の鱗屑軽減',
        detail_en: 'Shampoos and creams with 2–6% salicylic acid soften psoriatic scales, allowing other treatments (steroids, vitamin D analogues) to penetrate',
        detail_ko: '2~6% 살리실산 샴푸·크림이 건선 인설을 연화시켜 다른 치료제(스테로이드, 비타민 D 유도체) 침투 가능',
        detail_ja: '2~6%サリチル酸シャンプー·クリームが乾癬鱗屑を軟化させ他の治療薬(ステロイド、ビタミンD誘導体)の浸透を可能にする' }
    ],
    dose_en: { 'Acne': '0.5–2% product applied 1–2 times daily after cleansing', 'Warts': '17% liquid applied to wart only (protect surrounding skin with petrolatum), once or twice daily for weeks; 40% patches changed every 48 hours', 'Psoriasis shampoo': '2x/week, leave 5–10 minutes, rinse', 'Corn/callus removers': '12.6–40% with pad; change daily, remove dead tissue with emery board after softening' },
    dose_ko: { '여드름': '세안 후 0.5~2% 제품 하루 1~2회', '사마귀': '17% 액체를 사마귀에만 도포(주변 피부는 바세린으로 보호), 하루 1~2회 수주간; 40% 패치는 48시간마다 교체', '건선 샴푸': '주 2회, 5~10분 방치 후 헹굼', '옥수수·굳은살 제거제': '12.6~40% 패드 부착; 매일 교체, 연화 후 줄로 죽은 조직 제거' },
    dose_ja: { 'ニキビ': '洗顔後0.5~2%製品を1日1~2回', 'いぼ': '17%液体をいぼのみに塗布(周囲の皮膚はワセリンで保護)、1日1~2回数週間;40%パッチは48時間ごとに交換', '乾癬シャンプー': '週2回、5~10分放置後すすぐ', 'たこ·胼胝除去剤': '12.6~40%パッド貼付;毎日交換、軟化後やすりで壊死組織を除去' },
    danger_en: 'DO NOT USE WART REMOVERS on face, moles, birthmarks, bleeding warts, or warts with hair — could cause severe damage. Do not use on diabetic feet, or in people with poor circulation — risk of ulceration, gangrene. Salicylate toxicity possible with extensive application on large body areas (>20% BSA) especially in children, causing nausea, tinnitus, hyperventilation.',
    danger_ko: '얼굴, 점, 모반, 출혈성 사마귀, 털이 있는 사마귀에 사마귀 제거제 사용 금지 — 심각한 손상 가능. 당뇨 환자의 발이나 혈액순환 불량자에게 사용 금지 — 궤양·괴저 위험. 광범위 부위(BSA 20% 초과) 도포 시, 특히 소아에서 살리실산 중독 가능 — 메스꺼움, 이명, 과호흡.',
    danger_ja: '顔、ほくろ、母斑、出血性いぼ、毛のあるいぼにいぼ除去剤を使用禁止 — 重篤な損傷の可能性。糖尿病足や血行不良の人に使用禁止 — 潰瘍·壊疽リスク。広範囲塗布(BSA 20%超)時、特に小児でサリチル酸中毒の可能性 — 吐き気、耳鳴り、過換気。',
    warn_en: 'May cause skin irritation, dryness, redness — start with lower concentration and less frequent use. Avoid combining with retinoids (tretinoin, adapalene) initially — excessive irritation. Pregnancy: topical low-concentration (e.g., face wash 2%) generally considered acceptable; higher concentrations (wart removers) and oral aspirin should be avoided. Allergic reaction to salicylates — if you cannot take aspirin, do not use large-area salicylic acid.',
    warn_ko: '피부 자극, 건조, 발적 가능 — 낮은 농도와 적은 빈도로 시작. 레티노이드(트레티노인, 아다팔렌)와 초기 병용 피함 — 과도한 자극. 임신: 저농도 외용(예: 2% 세안제)은 일반적으로 수용 가능; 고농도(사마귀 제거제)와 경구 아스피린은 피함. 살리실산염 알레르기 — 아스피린을 복용할 수 없으면 광범위 살리실산 사용 금지.',
    warn_ja: '皮膚刺激、乾燥、発赤の可能性 — 低濃度·低頻度から開始。レチノイド(トレチノイン、アダパレン)との初期併用回避 — 過度の刺激。妊娠:低濃度外用(例:2%洗顔料)は一般的に許容;高濃度(いぼ除去剤)と経口アスピリンは回避。サリチル酸塩アレルギー — アスピリンが服用できない場合は広範囲サリチル酸使用禁止。',
    interact: [
      { en: 'Other exfoliants (glycolic acid, retinoids, benzoyl peroxide) — stacking increases irritation; introduce one at a time', ko: '기타 각질 제거제 (글리콜산, 레티노이드, 벤조일 퍼옥사이드) — 중첩 시 자극 증가; 한 번에 하나씩 도입', ja: '他の角質除去剤(グリコール酸、レチノイド、過酸化ベンゾイル) — 重ね使用で刺激増加;一つずつ導入' },
      { en: 'Oral salicylates (aspirin) — systemic absorption from large-area topical use can add to oral dose; monitor', ko: '경구 살리실산염 (아스피린) — 광범위 외용의 전신 흡수가 경구 용량에 더해질 수 있음; 모니터링', ja: '経口サリチル酸塩(アスピリン) — 広範囲外用の全身吸収が経口用量に上乗せされる可能性;モニタリング' },
      { en: 'Topical steroids (for psoriasis) — apply salicylic acid first to soften scale, wait, then steroid', ko: '국소 스테로이드 (건선) — 살리실산 먼저 도포하여 인설 연화 후 대기, 이후 스테로이드', ja: '外用ステロイド(乾癬用) — サリチル酸を先に塗布して鱗屑を軟化、待ってからステロイド' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH) · AAD guidance'
  },
  {
    id: 'capsaicin-topical',
    generic: { en: 'Capsaicin topical cream 0.025–0.1%', ko: '캡사이신 외용 크림 0.025~0.1%', ja: 'カプサイシン外用クリーム 0.025~0.1%' },
    brands: ['Capzasin-HP', 'Zostrix', 'Salonpas Hot (as ingredient)'],
    category: 'pain',
    uses: [
      { title_en: 'Chronic musculoskeletal pain (arthritis, back, neuropathy)', title_ko: '만성 근골격계 통증 (관절염·허리·신경병증)', title_ja: '慢性筋骨格系の痛み(関節炎·腰·神経障害)',
        detail_en: 'Chili pepper extract that depletes substance P in sensory nerve endings, reducing pain signaling. Effective for osteoarthritis, low back pain, diabetic peripheral neuropathy. Requires 1–2 weeks of regular use for full effect — burning sensation lessens with continued use',
        detail_ko: '감각 신경 말단의 substance P를 고갈시켜 통증 신호를 줄이는 고추 추출물. 골관절염, 만성 요통, 당뇨병성 말초신경병증에 효과. 완전 효과까지 1~2주 규칙적 사용 필요 — 지속 사용 시 작열감 감소',
        detail_ja: '感覚神経末端のサブスタンスPを枯渇させ痛みのシグナルを減らす唐辛子抽出物。変形性関節症、慢性腰痛、糖尿病性末梢神経障害に有効。完全な効果まで1~2週間の規則的使用が必要 — 継続使用で灼熱感は軽減' },
      { title_en: 'Postherpetic neuralgia (shingles pain)', title_ko: '대상포진 후 신경통', title_ja: '帯状疱疹後神経痛',
        detail_en: 'Useful adjunct for chronic pain following shingles; lesions must be fully healed before starting',
        detail_ko: '대상포진 후 만성 통증의 유용한 보조제; 시작 전 병변이 완전히 치유되어야 함',
        detail_ja: '帯状疱疹後の慢性痛に有用な補助療法;開始前に病変が完全に治癒している必要あり' }
    ],
    dose_en: { 'Standard cream': 'Thin layer applied 3–4 times daily to affected area; wash hands thoroughly after', 'Duration for effect': '1–2 weeks of regular use; burning diminishes over time', 'Patch form': 'Lower concentration available as patch — apply to target area for up to 8 hours', 'Do not occlude': 'No airtight bandage; increases absorption and burning' },
    dose_ko: { '표준 크림': '해당 부위에 하루 3~4회 얇게 도포; 사용 후 손 철저히 씻음', '효과까지 기간': '규칙적 사용 1~2주; 시간 경과에 따라 작열감 감소', '패치형': '저농도 패치 제공 — 해당 부위에 최대 8시간 부착', '밀폐 금지': '공기 차단 붕대 사용 금지; 흡수·작열감 증가' },
    dose_ja: { '標準クリーム': '患部に1日3~4回薄く塗布;使用後は手を十分に洗う', '効果発現期間': '規則的使用1~2週間;時間の経過とともに灼熱感は減少', 'パッチ型': '低濃度パッチあり — 対象部位に最大8時間貼付', '密封禁止': '密閉包帯使用禁止;吸収·灼熱感が増加' },
    warn_en: 'INTENSE BURNING SENSATION is expected and is part of the mechanism — diminishes with continued use over 1–2 weeks. Wash hands immediately and thoroughly after application (contaminating eyes or genitals causes severe burning). Do not apply to broken skin, open wounds, or irritated skin. Do not apply heat (heating pad, hot shower) to treated area — can cause serious burn-like reaction. Keep away from eyes, nose, mouth, genitals.',
    warn_ko: '강한 작열감은 예상되며 작용 기전의 일부 — 1~2주 지속 사용 시 감소. 사용 직후 손을 즉시 철저히 씻음(눈·생식기 오염 시 심한 작열감). 손상된 피부, 열린 상처, 자극된 피부에 사용 금지. 치료 부위에 열(핫팩, 뜨거운 샤워) 적용 금지 — 심각한 화상 유사 반응 가능. 눈, 코, 입, 생식기 회피.',
    warn_ja: '強い灼熱感は予想され作用機序の一部 — 1~2週間の継続使用で減少。使用直後に手を即座に十分に洗う(目·性器汚染時に強い灼熱感)。損傷した皮膚、開放創、炎症部位には使用禁止。治療部位に熱(温熱パッド、熱いシャワー)を適用禁止 — 重篤な熱傷様反応の可能性。目、鼻、口、性器を避ける。',
    interact: [
      { en: 'Heat or heating pads on treated area — severe burn-like reaction; do not use', ko: '치료 부위에 열 또는 핫팩 — 심각한 화상 유사 반응; 사용 금지', ja: '治療部位への熱または温熱パッド — 重篤な熱傷様反応;使用禁止' },
      { en: 'ACE inhibitors — may intensify cough (systemic effect from substance P alteration)', ko: 'ACE 억제제 — 기침 심화 가능 (substance P 변화의 전신 영향)', ja: 'ACE阻害薬 — 咳の悪化の可能性(サブスタンスP変化の全身影響)' },
      { en: 'Other topical analgesics (menthol, methyl salicylate) — can layer but may cause excessive skin reaction', ko: '기타 외용 진통제 (멘톨, 메틸살리실산) — 중첩 가능하나 과도한 피부 반응 가능', ja: '他の外用鎮痛薬(メントール、サリチル酸メチル) — 重ね塗り可能だが過度の皮膚反応の可能性' }
    ],
    source: 'FDA OTC Monograph · DailyMed (NIH) · American Academy of Pain Medicine'
  },
  {
    id: 'chlorpheniramine',
    generic: { en: 'Chlorpheniramine maleate', ko: '클로르페니라민 말레산염', ja: 'クロルフェニラミンマレイン酸塩' },
    brands: ['Chlor-Trimeton', 'generic chlorpheniramine', 'ingredient in many combination products'],
    category: 'allergy',
    uses: [
      { title_en: 'Allergic rhinitis, hay fever, hives', title_ko: '알레르기 비염·고초열·두드러기', title_ja: 'アレルギー性鼻炎·花粉症·じんま疹',
        detail_en: 'First-generation H1 antihistamine; effective for sneezing, runny nose, itching, watery eyes, hives. Less sedating than diphenhydramine for many users but still causes drowsiness. Common ingredient in combination cold/flu products',
        detail_ko: '1세대 H1 항히스타민; 재채기, 콧물, 가려움, 눈물, 두드러기에 효과. 많은 사용자에서 디펜히드라민보다 덜 졸리나 여전히 졸음 유발. 복합 감기·독감 제품의 흔한 성분',
        detail_ja: '第一世代H1抗ヒスタミン薬;くしゃみ、鼻水、かゆみ、涙目、じんま疹に有効。多くの使用者でジフェンヒドラミンより眠気が少ないが依然眠気あり。複合風邪·インフルエンザ薬の一般的成分' }
    ],
    dose_en: { 'Adult': '4 mg every 4–6 hours; or 12 mg extended-release every 12 hours', 'Max per day': '24 mg (immediate-release); 24 mg (ER)', 'Age 6–11': '2 mg every 4–6 hours; max 12 mg per day', 'Age 2–5': '1 mg every 4–6 hours (only under doctor guidance)', 'Under 2 years': 'Do not use' },
    dose_ko: { '성인': '4~6시간마다 4 mg; 또는 12시간마다 서방형 12 mg', '하루 최대': '속효성 24 mg; 서방형 24 mg', '6~11세': '4~6시간마다 2 mg; 하루 최대 12 mg', '2~5세': '4~6시간마다 1 mg (의사 지도 하에만)', '2세 미만': '사용 금지' },
    dose_ja: { '成人': '4~6時間ごとに4 mg;または12時間ごとに徐放性12 mg', '1日最大量': '即効性24 mg;徐放性24 mg', '6~11歳': '4~6時間ごとに2 mg;1日最大12 mg', '2~5歳': '4~6時間ごとに1 mg(医師の指導下のみ)', '2歳未満': '使用禁止' },
    warn_en: 'Causes drowsiness — do not drive or operate machinery. Age 65+: high anticholinergic burden increases confusion, falls, urinary retention risk; AGS Beers Criteria recommends avoiding first-generation antihistamines in older adults. Second-generation alternatives (cetirizine, loratadine, fexofenadine) are preferred for daily allergy management. Check combination products to avoid duplicate doses.',
    warn_ko: '졸음 유발 — 운전·기계 조작 금지. 65세 이상: 항콜린 부담 증가로 혼동, 낙상, 요폐 위험; AGS Beers Criteria는 노년층에서 1세대 항히스타민 사용을 권장하지 않음. 일상 알레르기 관리에는 2세대 대체약(세티리진, 로라타딘, 펙소페나딘) 권장. 중복 복용 방지 위해 복합제 성분 확인.',
    warn_ja: '眠気を引き起こします — 運転·機械操作禁止。65歳以上:抗コリン負担増加で混乱、転倒、尿閉のリスク;AGS Beers基準は高齢者の第一世代抗ヒスタミン薬使用を推奨しません。日常アレルギー管理には第二世代代替薬(セチリジン、ロラタジン、フェキソフェナジン)を推奨。重複投与防止のため複合薬の成分を確認。',
    interact: [
      { en: 'Alcohol, benzodiazepines, opioids, sleep aids — additive sedation and respiratory depression', ko: '알코올, 벤조디아제핀, 오피오이드, 수면 보조제 — 진정 및 호흡 억제 가중', ja: 'アルコール、ベンゾジアゼピン、オピオイド、睡眠補助薬 — 鎮静および呼吸抑制の累積' },
      { en: 'MAO inhibitors — prolonged and intensified anticholinergic effects', ko: 'MAO 억제제 — 항콜린 작용 연장·증강', ja: 'MAO阻害薬 — 抗コリン作用の延長·増強' },
      { en: 'Other anticholinergics (tricyclic antidepressants, oxybutynin) — cumulative anticholinergic burden', ko: '기타 항콜린제 (삼환계 항우울제, 옥시부티닌) — 항콜린 부담 누적', ja: '他の抗コリン薬(三環系抗うつ薬、オキシブチニン) — 抗コリン負担の累積' },
      { en: 'Glaucoma medications, benign prostatic hyperplasia medications — may counteract or worsen conditions', ko: '녹내장 약, 전립선비대증 약 — 효과 상쇄 또는 상태 악화 가능', ja: '緑内障薬、前立腺肥大症薬 — 効果相殺または症状悪化の可能性' }
    ],
    source: 'FDA OTC Monograph 21 CFR 341 · DailyMed (NIH) · AGS Beers Criteria 2023'
  },
];

const CATEGORIES = [
  { id: 'all',        en: 'All',                ko: '전체',        ja: 'すべて' },
  { id: 'pain',       en: 'Pain & Fever',       ko: '진통·해열',   ja: '痛み·発熱' },
  { id: 'allergy',    en: 'Allergy & Cold',     ko: '알레르기·감기', ja: 'アレルギー·風邪' },
  { id: 'cough',      en: 'Cough & Throat',     ko: '기침·목',     ja: '咳·のど' },
  { id: 'gi',         en: 'Stomach & GI',       ko: '위장',        ja: '胃腸' },
  { id: 'skin',       en: 'Skin & Topical',     ko: '피부·외용',   ja: '皮膚·外用' },
  { id: 'sleep',      en: 'Sleep & Mental',     ko: '수면·정신',   ja: '睡眠·メンタル' },
  { id: 'womens',     en: "Women's Health",     ko: '여성 건강',   ja: '女性の健康' },
  { id: 'pediatric',  en: 'Pediatric',          ko: '소아',        ja: '小児' },
  { id: 'eye_ear',    en: 'Eye & Ear',          ko: '안·이',       ja: '目·耳' },
  { id: 'oral',       en: 'Oral & Dental',      ko: '구강·치과',   ja: '口腔·歯科' },
  { id: 'first_aid',  en: 'First Aid',          ko: '응급처치',    ja: '応急処置' },
  { id: 'other',      en: 'Other',              ko: '기타',        ja: 'その他' },
  { id: 'supplement', en: 'Supplements',        ko: '서플리먼트',  ja: 'サプリメント' }
];

let currentLang = 'en';
let currentCategory = 'all';
let currentSearch = '';

// ============ I18N LABELS ============
const I18N = {
  count_med: { en: n => n + ' medication' + (n === 1 ? '' : 's'), ko: n => '약 ' + n + '개', ja: n => '医薬品 ' + n + '件' },
  use_count_supp: { en: n => n + ' common use' + (n === 1 ? '' : 's'), ko: n => '일반적 용도 ' + n + '개', ja: n => '一般的用途 ' + n + '件' },
  use_count_drug: { en: n => n + ' FDA-approved use' + (n === 1 ? '' : 's'), ko: n => 'FDA 승인 용도 ' + n + '개', ja: n => 'FDA承認用途 ' + n + '件' },
  supplement_badge: { en: 'DIETARY SUPPLEMENT · NOT FDA-APPROVED DRUG', ko: '식이 보충제 · FDA 의약품 아님', ja: 'サプリメント · FDA承認医薬品ではない' },
  uses_label_supp: { en: 'Common Uses (Evidence Level)', ko: '일반적 용도 (증거 수준)', ja: '一般的用途 (エビデンスレベル)' },
  uses_label_drug: { en: 'FDA-Approved Uses', ko: 'FDA 승인 용도', ja: 'FDA承認用途' },
  evidence_strong: { en: 'Strong evidence', ko: '강한 근거', ja: '強いエビデンス' },
  evidence_emerging: { en: 'Emerging evidence', ko: '제한적 근거', ja: '新興エビデンス' },
  evidence_limited: { en: 'Limited evidence', ko: '근거 부족', ja: '限定的エビデンス' },
  dose_label_supp: { en: 'Typical Dose (check label)', ko: '일반적 복용량 (라벨 확인)', ja: '一般的用量 (ラベル確認)' },
  dose_label_drug: { en: 'Typical Adult Dosing (OTC Label)', ko: '성인 표준 복용량 (OTC 라벨)', ja: '成人標準用量 (OTCラベル)' },
  overuse_label: { en: 'Common Overuse & Misuse', ko: '흔한 과용·오용 주의', ja: '一般的な過剰使用·誤用の注意' },
  danger_label: { en: 'Serious Risks', ko: '심각한 위험', ja: '重大なリスク' },
  warn_label: { en: 'Cautions', ko: '주의사항', ja: '注意事項' },
  interact_label: { en: 'Interactions', ko: '상호작용', ja: '相互作用' },
  source_prefix: { en: 'Source: ', ko: '출처: ', ja: '出典: ' }
};
function L(key, ...args) {
  const v = I18N[key][currentLang];
  return typeof v === 'function' ? v(...args) : v;
}

// ============ TEXT SIZE ============
document.querySelectorAll('.ts-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.body.classList.remove('text-large', 'text-xlarge');
    const size = btn.dataset.size;
    if (size === 'large') document.body.classList.add('text-large');
    if (size === 'xlarge') document.body.classList.add('text-xlarge');
    document.querySelectorAll('.ts-btn').forEach(b => b.classList.toggle('active', b === btn));
  });
});

// ============ LANGUAGE ============
function applyLang(lang) {
  currentLang = lang;
  document.querySelectorAll('[data-en]').forEach(el => {
    const val = el.getAttribute('data-' + lang);
    if (val !== null) el.innerHTML = val;
  });
  document.querySelectorAll('[data-ph-en]').forEach(el => {
    el.placeholder = el.getAttribute('data-ph-' + lang);
  });
  document.documentElement.lang = lang;
  document.querySelectorAll('.lang-btn').forEach(b => {
    b.classList.toggle('active', b.dataset.lang === lang);
  });
  renderCategories();
  renderList();
}

document.querySelectorAll('.lang-btn').forEach(btn => {
  btn.addEventListener('click', () => applyLang(btn.dataset.lang));
});

// ============ DISCLAIMER GATE ============
const checks = ['c1','c2','c3'].map(id => document.getElementById(id));
const gateBtn = document.getElementById('gate-btn');
checks.forEach(c => c.addEventListener('change', () => {
  gateBtn.disabled = !checks.every(x => x.checked);
}));
gateBtn.addEventListener('click', () => {
  document.getElementById('gate').classList.add('hidden');
});

// ============ CATEGORIES ============
function renderCategories() {
  const bar = document.getElementById('categories');
  bar.innerHTML = '';
  CATEGORIES.forEach(cat => {
    const b = document.createElement('button');
    b.className = 'cat-btn' + (cat.id === currentCategory ? ' active' : '');
    b.textContent = cat[currentLang] || cat.en;
    b.addEventListener('click', () => {
      currentCategory = cat.id;
      renderCategories();
      renderList();
    });
    bar.appendChild(b);
  });
}

// ============ SEARCH ============
(function() {
  const searchInput = document.getElementById('search');
  const doSearch = () => {
    currentSearch = searchInput.value.toLowerCase().trim();
    renderList();
  };
  // Multiple events to ensure reliability across browsers and IME (Korean input)
  searchInput.addEventListener('input', doSearch);
  searchInput.addEventListener('keyup', doSearch);
  searchInput.addEventListener('change', doSearch);
  searchInput.addEventListener('compositionend', doSearch);  // Korean/Chinese/Japanese IME
  searchInput.addEventListener('search', doSearch);  // For type="search" clear button
})();

function matchesSearch(d, q) {
  if (!q) return true;
  const hay = [
    d.generic.en, d.generic.ko,
    ...(d.brands || []),
    ...d.uses.map(u => u.title_en + ' ' + u.title_ko + ' ' + u.detail_en + ' ' + u.detail_ko)
  ].join(' ').toLowerCase();
  return hay.includes(q);
}

// ============ RENDER LIST ============
function renderList() {
  const list = document.getElementById('drug-list');
  const noRes = document.getElementById('no-results');
  const count = document.getElementById('drug-count');
  list.innerHTML = '';

  const filtered = DRUGS.filter(d =>
    (currentCategory === 'all' || d.category === currentCategory) &&
    matchesSearch(d, currentSearch)
  );

  if (filtered.length === 0) {
    noRes.style.display = 'block';
    count.textContent = '';
    return;
  }
  noRes.style.display = 'none';

  count.textContent = L('count_med', filtered.length);

  filtered.forEach(d => list.appendChild(renderCard(d)));
}

function renderCard(d) {
  const card = document.createElement('div');
  card.className = 'drug-card' + (d.category === 'supplement' ? ' supplement' : '');

  // Build cross-language alt name (cycle through other languages)
  const langs = ['en', 'ko', 'ja'];
  const altLang = langs.find(l => l !== currentLang);
  const altName = d.generic[altLang] || d.generic.en;

  // Header
  const header = document.createElement('div');
  header.className = 'drug-header';
  const useCountLabel = d.category === 'supplement'
    ? L('use_count_supp', d.uses.length)
    : L('use_count_drug', d.uses.length);

  const supplementBadge = d.category === 'supplement'
    ? `<div class="supplement-badge">${L('supplement_badge')}</div>`
    : '';

  header.innerHTML = `
    <div class="drug-main">
      ${supplementBadge}
      <div class="drug-generic">${escapeHtml(d.generic[currentLang] || d.generic.en)}</div>
      <div class="drug-alt-name">${escapeHtml(altName)}</div>
      <div class="drug-brand">${(d.brands || []).join(' · ')}</div>
      <div class="drug-use-count">${useCountLabel}</div>
    </div>
    <div class="chevron">›</div>
  `;
  header.addEventListener('click', () => card.classList.toggle('open'));
  card.appendChild(header);

  // Body
  const body = document.createElement('div');
  body.className = 'drug-body';

  // Uses
  const usesSection = document.createElement('div');
  usesSection.className = 'section';
  const usesLabel = d.category === 'supplement' ? L('uses_label_supp') : L('uses_label_drug');
  usesSection.innerHTML = `<div class="section-label">${usesLabel}</div>`;
  d.uses.forEach(u => {
    const item = document.createElement('div');
    item.className = 'use-item';
    // Evidence tier badge (supplement only)
    let tierBadge = '';
    if (u.evidence) {
      const tierClass = u.evidence === 'strong' ? 'evidence-strong'
                      : u.evidence === 'emerging' ? 'evidence-emerging'
                      : 'evidence-limited';
      const tierKey = u.evidence === 'strong' ? 'evidence_strong'
                    : u.evidence === 'emerging' ? 'evidence_emerging'
                    : 'evidence_limited';
      tierBadge = `<span class="evidence-tier ${tierClass}">${L(tierKey)}</span>`;
    }
    item.innerHTML = `
      <div class="use-title">${escapeHtml(u['title_' + currentLang] || u.title_en)}${tierBadge}</div>
      <div class="use-detail">${escapeHtml(u['detail_' + currentLang] || u.detail_en)}</div>
    `;
    usesSection.appendChild(item);
  });
  body.appendChild(usesSection);

  // Dose (fallback to en if ja missing)
  const doseData = d['dose_' + currentLang] || d['dose_en'];
  if (doseData && Object.keys(doseData).length) {
    const doseSection = document.createElement('div');
    doseSection.className = 'section';
    const doseLabel = d.category === 'supplement' ? L('dose_label_supp') : L('dose_label_drug');
    doseSection.innerHTML = `<div class="section-label">${doseLabel}</div>`;
    const table = document.createElement('div');
    table.className = 'dose-table';
    Object.entries(doseData).forEach(([k, v]) => {
      const row = document.createElement('div');
      row.className = 'dose-row';
      row.innerHTML = `<span class="dose-label">${escapeHtml(k)}</span><span class="dose-value">${escapeHtml(v)}</span>`;
      table.appendChild(row);
    });
    doseSection.appendChild(table);
    body.appendChild(doseSection);
  }

  // Overuse warning (supplements only) — fallback to en
  const overuseText = d['overuse_' + currentLang] || d['overuse_en'];
  if (overuseText) {
    const os = document.createElement('div');
    os.className = 'section';
    os.innerHTML = `<div class="section-label danger-label">${L('overuse_label')}</div><div class="danger-box">${escapeHtml(overuseText)}</div>`;
    body.appendChild(os);
  }

  // Danger — fallback to en
  const dangerText = d['danger_' + currentLang] || d['danger_en'];
  if (dangerText) {
    const ds = document.createElement('div');
    ds.className = 'section';
    ds.innerHTML = `<div class="section-label danger-label">${L('danger_label')}</div><div class="danger-box">${escapeHtml(dangerText)}</div>`;
    body.appendChild(ds);
  }

  // Warn — fallback to en
  const warnText = d['warn_' + currentLang] || d['warn_en'];
  if (warnText) {
    const ws = document.createElement('div');
    ws.className = 'section';
    ws.innerHTML = `<div class="section-label warn-label">${L('warn_label')}</div><div class="warn-box">${escapeHtml(warnText)}</div>`;
    body.appendChild(ws);
  }

  // Interactions — fallback to en
  if (d.interact && d.interact.length) {
    const is = document.createElement('div');
    is.className = 'section';
    is.innerHTML = `<div class="section-label">${L('interact_label')}</div>`;
    const ul = document.createElement('ul');
    ul.className = 'interact-list';
    d.interact.forEach(i => {
      const li = document.createElement('li');
      li.textContent = i[currentLang] || i.en;
      ul.appendChild(li);
    });
    is.appendChild(ul);
    body.appendChild(is);
  }

  // Source
  if (d.source) {
    const src = document.createElement('div');
    src.className = 'source-note';
    src.textContent = L('source_prefix') + d.source;
    body.appendChild(src);
  }

  card.appendChild(body);
  return card;
}

function escapeHtml(s) {
  if (s == null) return '';
  return String(s).replace(/[&<>"']/g, c => ({
    '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'
  }[c]));
}

// Initial render
applyLang('en');
</script>

</body>
</html>