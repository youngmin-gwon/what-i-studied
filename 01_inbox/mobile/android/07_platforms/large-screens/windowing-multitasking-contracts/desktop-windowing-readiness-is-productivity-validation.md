---
title: desktop-windowing-readiness-is-productivity-validation
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-03 18:15:40 +09:00
date created: 2026-07-31 18:06:11 +09:00
---

## 데스크톱 윈도잉 준비도는 작은 화면 호환성이 아니라 생산성 검증이다

상위 문서: [데스크톱 윈도잉과 멀티태스킹 계약](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/windowing-multitasking-contracts.md)

데스크톱 윈도잉 대응은 phone UI 가 깨지지 않는 수준에서 끝나지 않는다. 사용자가 키보드, 포인터, 여러 창, 넓은 정보 공간을 사용해 더 빠르게 작업할 수 있는지 검증해야 한다.

### 체크 기준

- 창을 매우 좁게, 매우 넓게, 낮은 height 로 바꿔도 핵심 과업이 유지된다.
- list-detail, supporting pane, 도구 패널처럼 넓은 창에서 정보 구조가 좋아진다.
- keyboard shortcut, right click, hover, drag-drop 같은 생산성 입력이 중요한 명령에 연결된다.
- 여러 instance 에서 같은 데이터가 열릴 때 저장, 충돌, focus, notification routing 이 예측 가능하다.
- Adaptive app quality tier 와 Android resizable emulator, 실제 desktop/ChromeOS 환경 테스트를 release checklist 에 포함한다.
- caption bar 가 있는 창과 immersive 전환에서 상단 interactive UI 가 시스템 제어와 겹치지 않는다.

### 관련 문서

- [적응형 앱 준비도는 창, posture, 입력 테스트로 판단한다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/adaptive-app-readiness-requires-window-posture-input-testing.md)
- [테스트와 품질 계약](01_inbox/mobile/android/06_testing_performance/testing/testing-quality-contracts/testing-quality-contracts.md)

공식 문서: [Adaptive app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality), [Support desktop windowing](https://developer.android.com/develop/adaptive-apps/guides/support-desktop-windowing)

검증일: 2026-08-03. 호환성보다 생산성 높은 Tier 1/2 과업을 목표로 하되 앱 용도에 해당하는 요구사항만 적용한다.
