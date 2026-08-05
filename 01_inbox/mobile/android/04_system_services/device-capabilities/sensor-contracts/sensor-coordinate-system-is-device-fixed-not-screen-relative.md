---
title: sensor-coordinate-system-is-device-fixed-not-screen-relative
tags: ["android", "android/system-services"]
aliases: ["센서 좌표계는 화면 방향이 아니라 기기 고정 좌표계다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## 센서 좌표계는 화면 방향이 아니라 기기 고정 좌표계다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [센서 접근 계약](./sensor-contracts.md)

### 핵심 정의

가속도계, 자이로스코프 같은 motion 센서의 좌표축(X/Y/Z)은 기기가 `natural orientation`(기기 하드웨어가 디자인될 때 지정된 고정 물리 기본 방향)일 때를 기준으로 고정되어 있다. 사용자가 화면을 회전시켜 UI가 가로/세로로 바뀌어도 센서 좌표축 자체는 회전하지 않는다.

### 메커니즘

기본 방향은 기기 종류에 따라 다르다. 대부분의 휴대전화는 세로가 기본 방향이고, 일부 태블릿은 가로가 기본 방향이다. 센서 값은 항상 이 기본 방향 기준의 축으로 전달되므로, 화면이 회전된 상태에서 "화면 기준 위/아래"를 알고 싶은 앱은 센서 raw 값을 그대로 UI 좌표에 대응시키면 안 된다.

### 판단 기준

- 화면 방향에 따라 동작이 달라져야 하는 기능(예: 수평계, 게임 컨트롤)은 `SensorManager.remapCoordinateSystem()`(화면 회전 각도에 맞춰 센서의 물리 좌표축을 디스플레이 좌표축으로 변환하는 도우미 함수)으로 현재 디스플레이 회전에 맞춰 좌표축을 변환한 뒤 사용한다.
- 기기 기본 방향이 세로인지 가로인지 가정하지 않는다. `Display.getRotation()`과 함께 실제 기본 방향을 확인해야 정확히 리매핑할 수 있다.
- 좌표계 변환을 건너뛰고 raw 값을 그대로 UI에 매핑하면 태블릿과 휴대전화에서 같은 코드가 다르게 동작하는 버그가 생긴다.

### 경계

- 이 노트는 좌표계 정의와 리매핑 필요성까지 다룬다. 센서 자체의 배칭/전력 설정은 [센서 배칭은 수신 지연과 배터리 사이의 트레이드오프다](./sensor-batching-trades-latency-for-battery.md)가 다룬다.
- 화면 회전과 Activity/Window 레벨의 configuration change 처리는 `02_app_framework`의 lifecycle 관련 클러스터가 다룬다.

### 관찰 가능한 신호

기기를 물리적으로 회전시키지 않고 화면 회전만 발생시킨 뒤(예: 자동 회전 켠 상태에서 옆으로 눕히기) 가속도계 raw 값의 축이 그대로인지 로그로 확인하면 이 계약을 직접 검증할 수 있다.

### 공식 문서

- https://developer.android.com/develop/sensors-and-location/sensors/sensors_overview#sensors-coords
