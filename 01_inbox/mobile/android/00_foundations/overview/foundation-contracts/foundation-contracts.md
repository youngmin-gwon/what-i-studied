---
title: "Foundation Contracts"
tags: ["android", "android/foundations"]
---

# Foundation Contracts

- [Android는 앱 SDK만이 아니라 계층형 모바일 플랫폼이다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/android-is-layered-mobile-platform-not-just-an-app-sdk.md)
- [Android stack boundary는 문제가 어느 층에 속하는지 판단하게 해 준다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/android-stack-boundaries-explain-where-a-problem-belongs.md)
- [앱 실행은 Launcher, system_server, Zygote, ActivityThread를 지나는 경로다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/app-launch-crosses-launcher-system-server-zygote-and-activitythread.md)
- [Android 보안은 UID sandbox, permission, SELinux, verified boot가 나뉜 계층이다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/android-security-is-layered-from-uid-sandbox-to-permissions-and-verified-boot.md)
- [Android 지식 지도는 runtime, app framework, services, security, tooling으로 나누어 읽는다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/android-knowledge-map-is-organized-by-runtime-app-framework-services-security-and-tooling.md)
- [사진 찍기 예시는 permission, intent, UI, media, HAL, storage 경계를 함께 지난다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/camera-example-crosses-permission-intent-ui-media-hal-and-storage-boundaries.md)

## 판단 기준

Foundation 노트는 세부 구현을 반복하지 않고 Android 지식이 어느 계층의 문제인지 찾아가는 입구로 사용한다.

## 경계

학습 순서나 역사 설명은 API 목록을 외우는 방향이 아니라 runtime, framework, service, security, tooling boundary를 구분하는 방향으로 유지한다.
