---
title: "Foundation Contracts는 안드로이드 플랫폼을 관통하는 근본적인 원칙과 계약이다"
tags: ["android", "android/foundations"]
---

# Foundation Contracts는 안드로이드 플랫폼을 관통하는 근본적인 원칙과 계약이다

이 하위 지도는 system map을 구성하는 판단 단위를 관리한다. 처음 읽을 때는 플랫폼 모형 → 진단 기준 → 구체 경로 순서로 진행한다.

## 플랫폼 모형

- [Android는 앱 SDK만이 아니라 계층형 모바일 플랫폼이다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/android-is-layered-mobile-platform-not-just-an-app-sdk.md) - 전체 stack의 구성 요소를 잡는다.
- [Android 지식 지도는 runtime, app framework, services, security, tooling으로 나누어 읽는다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/android-knowledge-map-is-organized-by-runtime-app-framework-services-security-and-tooling.md) - 이 저장소의 canonical area를 책임별로 찾는다.

## 진단 기준

- [Android stack boundary는 문제가 어느 층에 속하는지 판단하게 해 준다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/android-stack-boundaries-explain-where-a-problem-belongs.md) - 증상과 실패 계층을 연결한다.
- [Android 보안은 UID sandbox, permission, SELinux, verified boot가 나뉜 계층이다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/android-security-is-layered-from-uid-sandbox-to-permissions-and-verified-boot.md) - 거절 원인을 서로 다른 보안 계층으로 분해한다.

## 구체 경로

- [앱 실행은 Launcher, system_server, Zygote, ActivityThread를 지나는 경로다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/app-launch-crosses-launcher-system-server-zygote-and-activitythread.md) - launch를 process와 component 책임으로 나눈다.
- [사진 찍기 예시는 permission, intent, UI, media, HAL, storage 경계를 함께 지난다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/camera-example-crosses-permission-intent-ui-media-hal-and-storage-boundaries.md) - 하나의 기능을 여러 canonical area로 routing한다.

## 판단 기준

새 노트가 여러 계층을 잇는 재사용 가능한 분류 기준이면 이 묶음에 둔다. 특정 subsystem만 설명하면 해당 canonical area에 둔다.

## 경계

상위 [Android System Map](01_inbox/mobile/android/00_foundations/overview/android-system-map.md)은 문제별 navigation을 소유하고, 이 지도는 원자 foundation contract의 역할과 생성 경계만 소유한다.
