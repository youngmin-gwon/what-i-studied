---
title: "Delivery mode는 기능 필수성, 조건, 런타임 요청으로 선택한다"
tags: ["android", "android/packaging-deployment"]
---

# Delivery mode는 기능 필수성, 조건, 런타임 요청으로 선택한다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [Play Delivery 계약](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/play-delivery-contracts.md)
관련 노트: [On-demand와 conditional delivery는 설치 상태와 실패 UX를 설계해야 한다](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/on-demand-and-conditional-delivery-require-install-state-and-failure-ux.md), [Play Delivery 운영은 UX, 테스트, Play 설치 경로를 함께 검증한다](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/play-delivery-operations-validate-ux-testing-and-play-install-path.md)

## 비교표

| 모드 | 다운로드 시점 | 런타임 API | 적합한 대상 |
| --- | --- | --- | --- |
| install-time | 앱 설치 중 | 불필요 | 첫 화면에 필수인 기능 |
| conditional | 조건을 만족한 기기의 설치 중 | 불필요 | 지역·기기별 기능 |
| on-demand | 앱의 요청 시점 | 필요 | 소수 사용자 또는 늦게 쓰는 기능 |
| fast-follow | 설치 직후 자동 시작 | asset API 필요 | 큰 게임 asset pack |

## 판단 순서

앱의 첫 실행이 기능 없이는 성립하지 않으면 install-time을 선택한다.
모든 사용자가 필요로 하지 않고 설치 전에 조건을 알 수 있으면 conditional을 검토한다.
사용자의 행동 뒤에만 필요하면 on-demand가 기본 선택이다.
실행 코드는 아니고 설치 직후 준비할 대형 리소스라면 asset pack의 fast-follow를 쓴다.

## install-time

기능 모듈에 별도 custom delivery를 쓰지 않으면 install-time이다.
앱 시작 전에 사용 가능하다는 장점이 있지만 초기 다운로드가 커진다.
설치 직후 제거할 수 있는 기능은 removable 여부를 별도로 설계한다.

## conditional

조건은 설치 시 자동 다운로드 여부를 결정한다.
조건을 만족하지 않아도 나중에 on-demand로 요청할 수 있다.
따라서 조건 불충족을 영구적인 기능 차단으로 해석하면 안 된다.

## on-demand

모듈 요청, 진행 상태, 실패, 사용자 확인, 재시도를 앱이 처리한다.
기능 화면을 열기 전에 설치 상태를 확인하고 미설치면 명확한 다운로드 흐름을 제공한다.
백그라운드 선행 설치는 best-effort이므로 사용 전 재확인이 필요하다.

## fast-follow의 경계

Play Feature Delivery의 feature module과 Play Asset Delivery의 asset pack은 다르다.
fast-follow asset pack은 코드 모듈이 아니며, 게임 리소스 전달에 사용한다.
asset pack은 Play Asset Delivery Library로 상태와 위치를 확인한다.

## 공식 문서

- [Overview of Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery)
- [UX best practices for on-demand delivery](https://developer.android.com/guide/playcore/feature-delivery/ux-guidelines)
- [Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery)
