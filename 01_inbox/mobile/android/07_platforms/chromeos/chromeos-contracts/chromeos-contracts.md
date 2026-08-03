---
title: chromeos-contracts
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-03 18:15:25 +09:00
date created: 2026-08-03 17:29:41 +09:00
---

## ChromeOS 고유 계약

이 지도는 large-screen/windowing 지도가 다루지 않는 ChromeOS 만의 실행 환경, 배포 선언, 입력 우선순위 차이를 다룬다.

### 읽는 순서

1. [ChromeOS는 Android 앱을 컨테이너에서 실행하고 창을 데스크톱 윈도우로 매핑한다](01_inbox/mobile/android/07_platforms/chromeos/chromeos-contracts/chromeos-runs-android-apps-in-a-container-mapped-to-desktop-windows.md) 에서 실행 환경 자체의 차이를 본다.
2. [ChromeOS 전용 배포는 Play 콘솔에서 Chromebook 지원 여부를 별도로 선언한다](01_inbox/mobile/android/07_platforms/chromeos/chromeos-contracts/chromeos-distribution-requires-a-separate-play-console-declaration.md) 에서 배포 심사 조건을 본다.
3. [ChromeOS 입력은 마우스/트랙패드/키보드를 우선하고 터치는 보조 입력이다](01_inbox/mobile/android/07_platforms/chromeos/chromeos-contracts/chromeos-input-prioritizes-mouse-trackpad-and-keyboard-over-touch.md) 에서 입력 우선순위 가정을 본다.

### 문제 분류

| 증상 | 먼저 확인할 경계 |
| --- | --- |
| 앱이 Chromebook 에서 Play 스토어에 안 보임 | Play 콘솔의 Chromebook 지원 선언, 호환성 제외 사유 |
| 창 크기 조절 시 레이아웃이 깨짐 | large-screen 적응형 레이아웃을 갖췄는지(ChromeOS 고유 문제 아님) |
| 마우스 우클릭/키보드 단축키가 안 먹음 | 터치 전용으로 설계된 인터랙션에 데스크톱 입력 경로가 없는지 |

### 책임 경계

- 창 크기별 레이아웃 적응 자체는 이 지도가 아니라 `07_platforms/large-screens/large-screen-contracts` 와 `07_platforms/large-screens/windowing-multitasking-contracts` 가 담당한다. 이 지도는 그 위에 얹히는 ChromeOS 만의 실행 환경·배포·입력 차이만 다룬다.
- ChromeOS 는 Android 앱을 가상화가 아니라 컨테이너 방식으로 실행하지만, 이 격리 메커니즘의 세부 구현은 다루지 않는다.

### 노트 목록

- [ChromeOS는 Android 앱을 컨테이너에서 실행하고 창을 데스크톱 윈도우로 매핑한다](01_inbox/mobile/android/07_platforms/chromeos/chromeos-contracts/chromeos-runs-android-apps-in-a-container-mapped-to-desktop-windows.md)
- [ChromeOS 전용 배포는 Play 콘솔에서 Chromebook 지원 여부를 별도로 선언한다](01_inbox/mobile/android/07_platforms/chromeos/chromeos-contracts/chromeos-distribution-requires-a-separate-play-console-declaration.md)
- [ChromeOS 입력은 마우스/트랙패드/키보드를 우선하고 터치는 보조 입력이다](01_inbox/mobile/android/07_platforms/chromeos/chromeos-contracts/chromeos-input-prioritizes-mouse-trackpad-and-keyboard-over-touch.md)

검증일: 2026-08-03. [ChromeOS에서 Android 앱 최적화](https://developer.android.com/topic/arc) 를 기준으로 확인했다.
