---
title: android-knowledge-map-is-organized-by-runtime-app-framework-services-security-and-tooling
tags: ["android", "android/foundations"]
aliases: []
role: routing-shim
date modified: 2026-08-06 14:58:00 +09:00
date created: 2026-07-31 23:04:26 +09:00
---

## Android 지식 지도는 runtime, app framework, services, security, tooling 으로 나누어 읽는다

문서 역할: **routing shim**. 이 노트는 저장소의 전체 목차를 복제하지 않고, 질문의 소유 영역을 고르는 안정된 분류 기준만 제공한다. 실제 읽는 순서와 cluster 목록은 [Foundation contracts](foundation.md)와 각 영역의 상위 map이 소유한다.

### 질문을 소유 영역으로 보내는 기준

| 질문의 중심 | 먼저 갈 영역 | 이 영역이 소유하지 않는 것 |
| --- | --- | --- |
| boot, process, Binder, kernel, HAL, graphics runtime | `01_system_internals` | 앱 화면 상태·navigation 설계 |
| component, Context, UI state, Compose, data, navigation | `02_app_framework` | OS service 내부 정책 |
| build variant, APK/AAB, 서명, Play delivery | `03_packaging_deployment` | runtime permission 판단 |
| notification, scheduler, connectivity, sensor 같은 OS capability | `04_system_services` | feature별 앱 UI architecture |
| UID sandbox, permission, AppOps, SELinux, key와 data 보호 | `05_security_privacy` | 일반적인 lifecycle 설명 |
| 재현, test, benchmark, trace, 품질 지표 | `06_testing_performance` | subsystem 자체의 정본 설명 |
| Wear, TV, Auto, ChromeOS, large screen, XR의 환경 차이 | `07_platforms` | 공통 app framework의 반복 설명 |

관련 노트: [platform modularity](../../../01_system_internals/platform-modularity/android-platform-modularity.md), [packaging/deployment](../../../03_packaging_deployment/android-packaging-deployment.md), [platforms/form factors](../../../07_platforms/android-platforms-and-form-factors.md).

### 여러 영역을 지나는 문제

예를 들어 "백그라운드 알림이 보이지 않는다"는 app callback, FCM 전달, notification permission/channel, scheduler와 OEM 정책을 지난다. 증상 이름으로 한 영역을 고르지 말고 마지막 성공 신호와 최초 실패 신호를 찾는다. FCM 수신 callback까지 왔다면 표시 계약을, callback이 없다면 전달·background 실행 조건을 먼저 소유 영역으로 보낸다.

### 경계

한 문제가 여러 영역을 지나면 최초 실패를 소유한 영역을 중심으로 두고 나머지는 관련 노트로 연결한다. 새 cluster를 추가하거나 읽는 순서를 바꿀 때는 이 shim을 늘리지 않고 [Foundation contracts](foundation.md) 또는 해당 상위 map을 수정한다.
