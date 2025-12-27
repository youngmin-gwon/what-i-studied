---
title: components-feedback
tags: [accessibility, design-system, expressive, loading, m3, material-design, progress, ux-design]
aliases: [Loading Indicators, Progress Indicators, Wavy Motion Feedback]
date modified: 2025-12-28 00:18:20 +09:00
date created: 2025-12-28 00:18:20 +09:00
---

## ⏳ Feedback (피드백): 기다림을 가치 있게 만들기

M3 Expressive 에서 피드백 컴포넌트는 사용자의 대기 시간을 지루하지 않게 하고, 시스템이 활발히 작동 중임을 감성적인 모션을 통해 소통합니다.

## 🌀 Loading Indicator (로딩 인디케이터) [Expressive 신규]

짧은 시간 동안의 불확정적인(Indeterminate) 프로세스를 표현하기 위해 새롭게 설계된 컴포넌트입니다.

### 1. 설계 이유 및 UX 가치

- **Shape Morphing**: 단순히 회전하는 원형에서 벗어나, 형태가 부드럽게 변하는(Morphing) 애니메이션을 사용합니다. 이는 사용자의 시선을 자연스럽게 붙잡아 **지각된 대기 시간(Perceived Latency)** 을 줄이는 효과가 있습니다.
- **감성적 연결**: 기계적인 회전보다 유기적인 움직임을 통해 사용자와의 정서적 교감을 강화합니다.

### 2. 사용 가이드라인

- **적정 시간**: 보통 **200ms 에서 5초 사이**의 짧은 대기 상황에 적합합니다.
- **교체 권고**: 기존의 불확정적 원형 프로그레스 인디케이터(Circular Progress) 를 대부분 이 로딩 인디케이터로 교체하는 것이 M3 Expressive 의 지향점입니다.

---

## 📈 Progress Indicator (프로그레스 인디케이터)

상대적으로 긴 시간이 소요되거나, 진행률이 명확한 작업(Determinate) 에 사용됩니다.

### 1. Wavy Motion: '살아있는' 대기

- **핵심 변화**: 선형(Linear) 및 원형(Circular) 인디케이터 모두에 **물결(Wavy)** 형태의 애니메이션이 도입되었습니다.
- **UX 적 이점**: 정적인 막대보다 파동이 있는 인터랙션은 작업이 원활하게 진행되고 있다는 확신을 주며, 사용자 연구 결과 동일한 시간이라도 물결 모션이 있을 때 더 빠르게 작업이 완료된 것으로 느끼는 경향이 확인되었습니다.

### 2. 구성 옵션

- **Thick Track (8dp)**: 더 눈에 띄어야 하는 맥락(예: 앱 업데이트, 대형 파일 업로드) 에서 활용하여 가시성을 확보할 수 있습니다.
- **Stop Indicator**: 선형 진행률 하단에 위치하는 4dp 크기의 점으로, 트랙의 끝점을 명확히 인지하게 돕습니다.

---

## ♿ Accessibility (A11y)

진행 상태 정보는 모든 사용자에게 동등하게 전달되어야 합니다.

### 1. 대비 및 가독성

- **3:1 대비 규정**: 진행 바(Active Indicator) 와 배경 간의 명도 대비는 최소 **3:1** 을 유지해야 합니다.
- **Stop Indicator 의 역할**: 배경과의 대비가 낮아 진행 바의 끝이 모호할 때, Stop Indicator 를 배치하여 전체 작업 범위를 시각적으로 격리합니다.

### 2. 스크린 리더 대응

- **Role**: 반드시 `progress bar` 역할을 부여하여 어시스티브 기술이 현재 진행률을 읽어줄 수 있도록 합니다.
- **Semantic Labels**: 단순히 "로딩 중"이 아닌, **"기사 불러오는 중"**, **"페이지 새로고침 중"** 과 같이 맥락이 포함된 레이블을 제공해야 합니다.

---

## 🔗 관련 문서

- [[../material3_walkthrough|Material Design 3 개요 (Expressive Deep Dive)]]
- [[components-actions|Actions: 버튼과 FAB]]
- [[components-selection-inputs|Selection & Inputs]]
- [[components-typography|Typography: 의미론적 가독성과 폰트 역할]]
- [[components-color-theme|Color & Theme: 지능적인 컬러 시스템과 HCT]]
