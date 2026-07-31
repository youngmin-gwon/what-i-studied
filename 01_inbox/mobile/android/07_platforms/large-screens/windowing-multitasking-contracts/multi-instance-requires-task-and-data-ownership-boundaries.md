---
title: "데스크톱 멀티 인스턴스는 작업 단위와 데이터 소유권을 먼저 정해야 한다"
tags: ["android", "android/platforms"]
---

# 데스크톱 멀티 인스턴스는 작업 단위와 데이터 소유권을 먼저 정해야 한다

상위 문서: [데스크톱 윈도잉과 멀티태스킹 계약](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/windowing-multitasking-contracts.md)

Multi-instance 지원은 같은 앱 창을 여러 개 띄우는 스위치를 켜는 문제가 아니다. 문서, 대화, 탭, 계정, 편집 세션 같은 작업 단위가 무엇인지와 동시에 열린 인스턴스들이 어떤 데이터를 공유하거나 격리하는지 먼저 정해야 한다.

## 실무 규칙

- 새 window로 열 수 있는 사용자 과업을 명확히 정한다.
- 같은 항목을 두 인스턴스에서 편집할 때 충돌, 저장 순서, stale state 처리를 정의한다.
- singleton ViewModel, 전역 selection, shared mutable cache가 여러 window에서 섞이지 않는지 확인한다.
- drag-out으로 새 인스턴스를 만드는 UX는 원본 창과 새 창의 소유권 이전 규칙을 함께 설계한다.
- Android 15 이상의 system UI multi-instance affordance를 쓰려면 manifest property와 task launch 동작을 함께 검증한다.

## 관련 문서

- [드래그 앤 드롭은 창 사이 데이터 이동 계약이다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/drag-and-drop-is-cross-window-data-contract.md)
- [Android 상태 관리 정본 지도](01_inbox/mobile/android/02_app_framework/architecture/state-management/android-state-management.md)

공식 문서: [Support desktop windowing](https://developer.android.com/develop/adaptive-apps/guides/support-desktop-windowing)
