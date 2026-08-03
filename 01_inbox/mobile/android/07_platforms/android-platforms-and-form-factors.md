---
title: "Android 폼 팩터와 플랫폼 확장 지도"
tags: ["android", "android/platforms"]
---

# Android 폼 팩터와 플랫폼 확장 지도

Android 앱은 더 이상 단일 휴대폰 화면만 대상으로 하지 않는다. 이 지도는 큰 화면, 폴더블, 데스크톱 윈도잉, XR, TV, Wear OS, Auto/Automotive, ChromeOS처럼 앱 창과 입력 환경이 바뀌는 플랫폼 표면을 나눈다.

## 문제 분류

- 콘텐츠가 남거나 잘리는 문제는 먼저 기기명이 아니라 현재 창의 width/height class와 레이아웃 구조에서 찾는다.
- 접힘 영역에 UI가 걸리는 문제는 window size class가 아니라 `FoldingFeature`의 posture와 bounds 문제다.
- resize, focus, 여러 창, caption bar 문제는 적응형 레이아웃보다 windowing과 task/lifecycle 계약에서 찾는다.
- XR에서 패널은 보이지만 공간 기능이 실패하면 2D 레이아웃이 아니라 session, space mode, runtime capability를 확인한다.
- TV에서 리모컨 방향키로 요소에 도달하지 못하면 포커스 순서와 d-pad 탐색 가능성을 확인한다.
- Wear OS에서 화면이 꺼진 듯 보이면 ambient mode 콜백 구현 여부를 확인한다.
- Auto/Automotive에서 앱이 안 보이거나 레이아웃이 깨지면 투영(Auto)과 내장(Automotive OS)을 혼동했는지, Car App Library 템플릿 제약을 지켰는지 확인한다.
- ChromeOS에서 마우스/키보드 조작이 안 되면 large-screen 레이아웃이 아니라 터치 전용으로 설계된 인터랙션이 있는지 확인한다.

## 정본 노트

- [큰 화면 적응 계약](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md)
- [데스크톱 윈도잉과 멀티태스킹 계약](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/windowing-multitasking-contracts.md)
- [Android XR 계약](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md)
- [Android TV 계약](01_inbox/mobile/android/07_platforms/tv/tv-contracts/tv-contracts.md)
- [Wear OS 계약](01_inbox/mobile/android/07_platforms/wear/wear-contracts/wear-contracts.md)
- [Android Auto/Automotive 계약](01_inbox/mobile/android/07_platforms/auto/auto-contracts/auto-contracts.md)
- [ChromeOS 고유 계약](01_inbox/mobile/android/07_platforms/chromeos/chromeos-contracts/chromeos-contracts.md)

## 판단 순서

1. 먼저 기기 이름이 아니라 현재 앱 창의 크기와 비율을 본다.
2. 폴더블에서는 hinge, posture, display feature가 레이아웃을 나누는지 확인한다.
3. 데스크톱 윈도잉에서는 창 크기 변경, caption bar, 여러 작업 인스턴스를 검증한다.
4. XR에서는 2D 앱을 띄우는 것과 공간 UI를 설계하는 것을 분리한다.
5. TV/Wear OS/Auto처럼 터치가 없거나 제한된 표면에서는 대체 입력 경로(d-pad, 리모컨, 음성, 마우스/키보드)로 모든 기능에 도달 가능한지 확인한다.
6. 모든 폼 팩터에서 터치 외 입력과 접근성 경로를 테스트한다.

## 읽는 순서

1. 큰 화면 계약에서 앱 창과 물리 기기를 분리하고 adaptive structure를 정한다.
2. 데스크톱 윈도잉 계약에서 resize, lifecycle, task, system UI를 검증한다.
3. XR 계약에서 2D 호환 실행과 공간화, runtime capability와 출시 조건을 분리한다.
4. TV 계약에서 d-pad 입력, 10-foot UI, 배포 조건을 확인한다.
5. Wear OS 계약에서 동반 앱과의 독립성, ambient mode, tile/complication을 확인한다.
6. Auto/Automotive 계약에서 투영과 내장 OS를 구분하고 Car App Library 템플릿, 차량 신호 접근을 확인한다.
7. ChromeOS 계약에서 large-screen/windowing 위에 얹히는 실행 환경, 배포, 입력 우선순위 차이를 확인한다.

검증일: 2026-08-03. 현재 공식 품질 기준은 큰 화면을 포함한 [Adaptive app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality)와 별도의 [Android XR app quality](https://developer.android.com/docs/quality-guidelines/android-xr)로 나뉜다. 이 지도는 `_meta/android-knowledge-base-quality-plan.md` Phase 1(2026-08-03)에서 확정한 "이름 유지 + 범위 확장" 결정에 따라 TV/Wear OS/Auto·Automotive/ChromeOS 클러스터를 모두 갖췄다.
