---
title: "적응형 앱 준비도는 창, posture, 입력 테스트로 판단한다"
tags: ["android", "android/platforms"]
---

# 적응형 앱 준비도는 창, posture, 입력 테스트로 판단한다

상위 문서: [큰 화면 적응 계약](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md)

큰 화면 대응 완료 여부는 특정 태블릿에서 화면이 넓게 보이는지로 판단하지 않는다. compact, medium, expanded, large, extra-large 창 크기와 폴더블 posture, multi-window, 입력 장치 조합에서 핵심 과업이 유지되는지로 판단한다.

## 체크 기준

- portrait, landscape, split screen, freeform resize에서 정보 손실과 overlap이 없어야 한다.
- activity recreation 또는 window size 변화 후에도 화면 상태가 복원되어야 한다.
- fold/unfold, tabletop, book posture에서 주요 콘텐츠와 조작부가 hinge 또는 접힘 영역을 피해야 한다.
- keyboard navigation, pointer hover/right-click/scroll, stylus 입력을 실제 기기 또는 emulator로 검증한다.
- 현재 Adaptive app quality의 Tier 3 ready, Tier 2 optimized, Tier 1 differentiated 체크리스트를 출시 전 기준으로 사용한다.
- breakpoint 바로 전후와 compact height를 포함해 레이아웃 전환 경계를 테스트한다.

## 관련 문서

- [Android 상태 관리 정본 지도](01_inbox/mobile/android/02_app_framework/architecture/state-management/android-state-management.md)
- [테스트와 품질 계약](01_inbox/mobile/android/06_testing_performance/testing/testing-quality-contracts/testing-quality-contracts.md)
- [데스크톱 윈도잉 준비도는 작은 화면 호환성이 아니라 생산성 검증이다](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/desktop-windowing-readiness-is-productivity-validation.md)

공식 문서: [Adaptive app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality), [Get started with large screens](https://developer.android.com/guide/topics/large-screens)

검증일: 2026-08-03. 기존 large screen quality 지침은 Adaptive app quality로 대체되었으므로 archive가 아니라 현재 tier와 compatibility tests를 기준으로 한다.
