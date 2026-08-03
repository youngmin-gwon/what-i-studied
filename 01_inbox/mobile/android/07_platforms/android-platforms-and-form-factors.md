---
title: "Android 폼 팩터와 플랫폼 확장 지도"
tags: ["android", "android/platforms"]
---

# Android 폼 팩터와 플랫폼 확장 지도

Android 앱은 더 이상 단일 휴대폰 화면만 대상으로 하지 않는다. 이 지도는 큰 화면, 폴더블, 데스크톱 윈도잉, XR처럼 앱 창과 입력 환경이 바뀌는 플랫폼 표면을 세 묶음으로 나눈다.

## 문제 분류

- 콘텐츠가 남거나 잘리는 문제는 먼저 기기명이 아니라 현재 창의 width/height class와 레이아웃 구조에서 찾는다.
- 접힘 영역에 UI가 걸리는 문제는 window size class가 아니라 `FoldingFeature`의 posture와 bounds 문제다.
- resize, focus, 여러 창, caption bar 문제는 적응형 레이아웃보다 windowing과 task/lifecycle 계약에서 찾는다.
- XR에서 패널은 보이지만 공간 기능이 실패하면 2D 레이아웃이 아니라 session, space mode, runtime capability를 확인한다.

## 정본 노트
- [큰 화면 적응 계약](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md)
- [데스크톱 윈도잉과 멀티태스킹 계약](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/windowing-multitasking-contracts.md)
- [Android XR 계약](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md)

## 판단 순서

1. 먼저 기기 이름이 아니라 현재 앱 창의 크기와 비율을 본다.
2. 폴더블에서는 hinge, posture, display feature가 레이아웃을 나누는지 확인한다.
3. 데스크톱 윈도잉에서는 창 크기 변경, caption bar, 여러 작업 인스턴스를 검증한다.
4. XR에서는 2D 앱을 띄우는 것과 공간 UI를 설계하는 것을 분리한다.
5. 모든 폼 팩터에서 터치 외 입력과 접근성 경로를 테스트한다.

## 읽는 순서

1. 큰 화면 계약에서 앱 창과 물리 기기를 분리하고 adaptive structure를 정한다.
2. 데스크톱 윈도잉 계약에서 resize, lifecycle, task, system UI를 검증한다.
3. XR 계약에서 2D 호환 실행과 공간화, runtime capability와 출시 조건을 분리한다.

검증일: 2026-08-03. 현재 공식 품질 기준은 큰 화면을 포함한 [Adaptive app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality)와 별도의 [Android XR app quality](https://developer.android.com/docs/quality-guidelines/android-xr)로 나뉜다.

## 목표 범위와 현재 공백 (2026-08-03 확정)

이 폴더 이름은 "폼 팩터 전체"를 가리키지만, 현재 실제로 작성된 것은 large-screen, desktop windowing, XR 뿐이다. 이름을 유지하기로 확정했으므로(`_meta/android-knowledge-base-quality-plan.md` Phase 1), 아래는 제목이 약속하는 범위 중 아직 없는 폼 팩터다. 각 폼팩터는 input, lifecycle, layout, system UI, capability, distribution, testing 관점을 모두 갖춰야 완료로 본다.

- TV (Android TV/Google TV): d-pad/리모컨 입력, 10-foot UI, leanback 계약
- Wear OS: 워치 입력, 짧은 상호작용 lifecycle, complication/tile 계약
- Auto/Automotive (Android Auto, Android Automotive OS): 운전 중 안전 제약, 차량 HAL 연동, distribution 정책
- ChromeOS 고유 계약: 이미 large-screen/windowing 이 일부 다루지만 ChromeOS 전용 정책(예: Play Store 배포 조건)은 별도 확인 필요
