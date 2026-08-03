---
title: chromeos-runs-android-apps-in-a-container-mapped-to-desktop-windows
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-03 18:15:26 +09:00
date created: 2026-08-03 17:29:56 +09:00
---

## ChromeOS 는 Android 앱을 컨테이너에서 실행하고 창을 데스크톱 윈도우로 매핑한다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](01_inbox/mobile/android/07_platforms/android-platforms-and-form-factors.md)

관련 지도: [ChromeOS 고유 계약](01_inbox/mobile/android/07_platforms/chromeos/chromeos-contracts/chromeos-contracts.md)

### 핵심 정의

ChromeOS 는 ARC(Android Runtime for Chrome) 컨테이너 안에서 Android 앱을 실행하고, 앱의 각 Activity/Task 창을 ChromeOS 데스크톱 환경의 일반 윈도우처럼 리사이즈·이동·최소화 가능한 창으로 매핑한다. 사용자 입장에서는 크롬 브라우저 창, 리눅스 앱 창과 함께 Android 앱 창이 동일한 데스크톱 윈도우 매니저 아래 공존한다.

### 메커니즘

앱 프로세스와 Android 프레임워크 자체는 컨테이너 안에서 평소와 동일하게 동작하지만, 창 크기와 위치는 ChromeOS 윈도우 매니저가 결정하고 이 정보가 Android 의 `Configuration`/윈도우 크기 변화로 앱에 전달된다. 즉 앱 입장에서 창 리사이즈는 여느 large-screen 멀티윈도우 환경과 마찬가지로 configuration change 또는 크기 변화 콜백으로 관찰된다. ChromeOS 자체의 파일 시스템, 클립보드 등 일부 리소스는 컨테이너 경계를 넘어 공유되도록 별도로 브리지된다.

### 판단 기준

- 창 크기 변화에 대한 대응은 ChromeOS 전용 코드를 새로 작성하지 않고 `07_platforms/large-screens/large-screen-contracts` 와 `windowing-multitasking-contracts` 가 다루는 일반적인 적응형 레이아웃/윈도잉 계약을 그대로 따른다.
- 파일 선택기, 클립보드 공유처럼 ChromeOS 네이티브 앱과 상호작용해야 하는 기능은 일반 Android Intent/Storage Access Framework 경로가 컨테이너 경계를 넘어 정상 동작하는지 실기기(Chromebook)에서 별도로 검증한다.
- 에뮬레이터로 이 컨테이너 매핑을 완벽히 재현하기 어려운 경우가 있으므로, ChromeOS 고유 동작은 가능하면 실제 Chromebook 에서 검증한다.

### 경계

- 이 노트는 실행 환경과 창 매핑 자체를 다룬다. Play 배포 심사 조건은 [ChromeOS 전용 배포는 Play 콘솔에서 Chromebook 지원 여부를 별도로 선언한다](01_inbox/mobile/android/07_platforms/chromeos/chromeos-contracts/chromeos-distribution-requires-a-separate-play-console-declaration.md) 가 다룬다.
- 창 크기별 레이아웃 구조 자체는 `07_platforms/large-screens/large-screen-contracts` 가 다루며 이 노트에서 반복하지 않는다.

### 관찰 가능한 신호

Chromebook 실기기 또는 ChromeOS 개발자 모드 환경에서 앱 창을 리사이즈하며 `onConfigurationChanged()` 또는 window size class 변화 콜백이 다른 large-screen 환경과 동일하게 호출되는지 확인한다.

### 공식 문서

- https://developer.android.com/topic/arc
- https://chromeos.dev/en/android
