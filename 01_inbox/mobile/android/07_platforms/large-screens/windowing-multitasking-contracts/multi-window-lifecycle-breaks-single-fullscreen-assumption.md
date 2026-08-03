---
title: "Multi-window 생명주기는 단일 전체 화면 가정을 깨뜨린다"
tags: ["android", "android/platforms"]
---

# Multi-window 생명주기는 단일 전체 화면 가정을 깨뜨린다

상위 문서: [데스크톱 윈도잉과 멀티태스킹 계약](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/windowing-multitasking-contracts.md)

Multi-window에서는 앱이 화면 전체를 독점한다는 가정이 깨진다. 사용자는 다른 앱과 동시에 상호작용하고, Android는 창 크기와 focus 상태를 바꾸며, 새 task가 새 window로 열릴 수 있다.

## 실무 규칙

- `onResume()`이 곧 전체 화면 독점 사용을 뜻한다고 가정하지 않는다.
- focus 상실, pause, stop, configuration change, resize를 각각 다른 사건으로 다룬다.
- media, sensor, camera, location 같은 자원은 실제 visible/interactive 상태와 정책을 기준으로 점유한다.
- deep link나 새 task launch가 어떤 window와 back stack에 붙는지 명시적으로 테스트한다.

## 경계

multi-window에서 여러 activity가 동시에 `RESUMED`일 수 있으므로 `onResume()`만으로 topmost나 독점 입력을 추론하지 않는다. 사용자 상호작용의 독점 여부가 필요하면 window focus를 별도로 관찰하고, resize에 따른 configuration change와 process death 후 복원을 같은 사건으로 취급하지 않는다.

## 관련 문서

- [Android Navigation 진입 계약](01_inbox/mobile/android/02_app_framework/navigation/navigation-contracts/navigation-contracts.md)
- [Android 상태 관리 정본 지도](01_inbox/mobile/android/02_app_framework/architecture/state-management/android-state-management.md)

공식 문서: [Support desktop windowing](https://developer.android.com/develop/adaptive-apps/guides/support-desktop-windowing)

검증일: 2026-08-03. lifecycle 콜백, window focus, task/window 배치는 서로 다른 상태 축으로 검증한다.
