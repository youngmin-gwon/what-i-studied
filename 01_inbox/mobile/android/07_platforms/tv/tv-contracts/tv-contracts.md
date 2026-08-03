---
title: "Android TV 계약"
tags: ["android", "android/platforms"]
---

# Android TV 계약

이 지도는 Android TV/Google TV를 d-pad 중심 입력, 10-foot UI 탐색, 배포 정책이라는 세 계약으로 분리한다.

## 읽는 순서

1. [Android TV는 d-pad/리모컨을 1차 입력으로 가정한다](01_inbox/mobile/android/07_platforms/tv/tv-contracts/android-tv-assumes-d-pad-remote-as-primary-input.md)에서 터치가 없는 입력 모델을 본다.
2. [10-foot UI는 포커스 기반 탐색을 요구한다](01_inbox/mobile/android/07_platforms/tv/tv-contracts/10-foot-ui-requires-focus-based-navigation.md)에서 레이아웃과 포커스 이동 설계를 본다.
3. [Android TV 배포는 터치스크린 미보유를 명시적으로 선언해야 한다](01_inbox/mobile/android/07_platforms/tv/tv-contracts/android-tv-distribution-requires-declaring-no-touchscreen.md)에서 Play 콘솔 배포 조건을 본다.

## 문제 분류

| 증상 | 먼저 확인할 경계 |
| --- | --- |
| 리모컨 방향키로 특정 UI 요소에 포커스가 안 감 | 포커스 순서(`nextFocusUp` 등)나 클릭 가능 영역이 d-pad 탐색 가능한지 |
| TV에서 앱이 Play 스토어에 안 보임 | 매니페스트의 leanback 기능 선언과 터치스크린 not-required 선언 |
| 화면 요소가 리모컨 시청 거리에서 너무 작음 | 10-foot UI 기준(큰 텍스트/여백)을 적용했는지 |

## 책임 경계

- Android TV는 휴대폰 UI를 그대로 축소 이식하는 플랫폼이 아니라 원격 입력과 시청 거리 전제가 다른 별도 디자인 표면이다.
- 이 지도는 TV 고유의 입력/UI/배포 계약만 다루며, 미디어 코덱이나 스트리밍 프로토콜 자체는 다루지 않는다.

## 노트 목록

- [Android TV는 d-pad/리모컨을 1차 입력으로 가정한다](01_inbox/mobile/android/07_platforms/tv/tv-contracts/android-tv-assumes-d-pad-remote-as-primary-input.md)
- [10-foot UI는 포커스 기반 탐색을 요구한다](01_inbox/mobile/android/07_platforms/tv/tv-contracts/10-foot-ui-requires-focus-based-navigation.md)
- [Android TV 배포는 터치스크린 미보유를 명시적으로 선언해야 한다](01_inbox/mobile/android/07_platforms/tv/tv-contracts/android-tv-distribution-requires-declaring-no-touchscreen.md)

검증일: 2026-08-03. [Android TV 앱 개발 가이드](https://developer.android.com/training/tv)를 기준으로 확인했다.
