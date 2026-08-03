---
title: "Car App Library는 운전 중 배포 콘텐츠를 제한된 템플릿으로만 허용한다"
tags: ["android", "android/platforms"]
---

# Car App Library는 운전 중 배포 콘텐츠를 제한된 템플릿으로만 허용한다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](01_inbox/mobile/android/07_platforms/android-platforms-and-form-factors.md)
관련 지도: [Android Auto/Automotive 계약](01_inbox/mobile/android/07_platforms/auto/auto-contracts/auto-contracts.md)

## 핵심 정의

Jetpack의 Car App Library는 앱이 임의의 View/Compose 레이아웃을 차량 화면에 그리는 것을 허용하지 않는다. 대신 시스템이 미리 정의한 템플릿(목록, 지도, 내비게이션, 메시지 등)에 데이터를 채워 넣는 방식으로만 화면을 구성하게 강제한다. 실제 렌더링은 차량 헤드유닛(또는 Android Auto 호스트)이 수행한다.

## 메커니즘

앱은 `Screen` 클래스를 상속해 `ListTemplate`, `NavigationTemplate`, `MessageTemplate` 같은 템플릿 객체를 반환한다. 호스트(헤드유닛 또는 투영 클라이언트)는 이 템플릿을 자신의 렌더링 엔진으로 그리며, 이 과정에서 텍스트 길이 제한, 목록 항목 수 제한, 허용된 액션 개수 같은 규칙을 강제한다. 앱이 규칙을 어긴 데이터를 전달하면 호스트가 이를 자르거나 렌더링을 거부할 수 있다. 카테고리(내비게이션, 주차, 전기차 충전소 검색(POI) 등)에 따라 허용되는 템플릿 종류도 제한된다.

## 판단 기준

- 임의의 커스텀 UI가 필요한 기능은 Car App Library로 구현할 수 없다는 것을 전제로 제품 요구사항을 잡는다. 이는 버그가 아니라 운전 중 주의 분산을 막기 위한 의도된 제약이다.
- 앱이 지원하려는 카테고리(내비게이션, 파킹, 충전, 메시징 등)에 따라 Google의 앱 카테고리 검토를 통과해야 배포 및 화이트리스트 등록이 가능하다는 점을 출시 일정에 반영한다.
- 텍스트/목록 길이 제한을 미리 확인해 서버에서 넘어오는 데이터가 잘리지 않고 핵심 정보를 우선 배치하도록 설계한다.

## 경계

- 이 노트는 화면 구성 제약을 다룬다. 두 플랫폼(투영형/내장형)의 근본적 차이는 [Android Auto는 투영이고 Android Automotive OS는 차량에 내장된 독립 OS다](01_inbox/mobile/android/07_platforms/auto/auto-contracts/android-auto-is-projection-android-automotive-os-is-an-embedded-os.md)가 다룬다.
- 일반 Android 앱의 Play 배포/심사 절차 자체는 `03_packaging_deployment`가 다룬다.

## 관찰 가능한 신호

Android Auto 데스크톱 헤드유닛 에뮬레이터에서 앱을 실행하면 템플릿 규칙 위반(텍스트 초과, 허용되지 않은 액션 개수 등)이 런타임 경고나 콘텐츠 잘림으로 즉시 나타난다.

## 공식 문서

- https://developer.android.com/training/cars/apps
- https://developer.android.com/reference/androidx/car/app/model/package-summary
