---
title: accessibilityservice-observes-and-acts-on-other-apps-ui
tags: ["android", "android/system-services"]
aliases: ["AccessibilityService는 다른 앱의 UI 이벤트를 관찰하고 조작할 수 있는 특권 서비스다"]
date modified: 2026-08-04 15:30:00 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## AccessibilityService는 다른 앱의 UI 이벤트를 관찰하고 조작할 수 있는 특권 서비스다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [입력 장치와 접근성 서비스 계약](./input-accessibility-contracts.md)

### 핵심 정의

`AccessibilityService`는 시스템 전역에서 발생하는 UI 이벤트(다른 앱의 화면 전환, 뷰 포커스, 텍스트 변경 등)를 관찰하고, 필요하면 접근성 액션(클릭 수행, 스크롤, 텍스트 입력 등)으로 다른 앱의 UI를 조작할 수 있는 특권 서비스다. 원래 목적은 스크린 리더 같은 보조 기술이지만, 이 특권이 강력해 자동화 도구나 악성 앱의 남용 대상이 되기도 한다.

### 메커니즘

앱이 접근성 서비스를 선언해도 자동으로 동작하지 않는다. 사용자가 설정의 접근성 메뉴에서 해당 서비스를 명시적으로 찾아 켜야 하며, 이 과정에서 시스템은 이 서비스가 화면 내용을 읽고 조작할 수 있다는 강한 경고를 보여준다. 활성화되면 서비스는 `AccessibilityEvent`(창 전환, 콘텐츠 변경, 클릭 등)를 시스템으로부터 스트리밍받고, `AccessibilityNodeInfo` 트리를 통해 화면 요소 구조를 조회하거나 `performAction()`으로 조작할 수 있다.

### 판단 기준

- 이 특권을 실제 접근성 목적(스크린 리더, 스위치 접근 등) 외의 용도(자동화, 매크로)로 사용하려는 경우 Play 정책이 요구하는 접근성 서비스 선언 사유 소명을 통과해야 한다는 점을 먼저 확인한다.
- 앱이 다른 앱의 접근성 조작 대상이 되는 것(보안 관점)을 고려한다면, 민감한 화면에서 스크린샷/접근성 노출을 제한하는 `FLAG_SECURE` 같은 대응책을 검토한다.
- 자체 UI를 접근성 서비스가 잘 읽을 수 있게 하려면(스크린 리더 사용자 지원) contentDescription, 포커스 순서 같은 표준 접근성 속성을 갖추는 것이 먼저이며, 이는 접근성 서비스를 만드는 것과는 다른 작업이다.

### 경계

- 이 노트는 접근성 서비스가 다른 앱을 관찰/조작하는 특권 모델을 다룬다. 텍스트 입력을 담당하는 IME는 [InputMethodService는 AccessibilityService와 다른 별도의 입력 계약이다](./inputmethodservice-is-a-separate-contract-from-accessibilityservice.md)가 다룬다.
- 화면 내 UI 요소에 접근성 속성을 붙이는 앱 개발자 관점의 작업(Compose/View의 semantics)은 `02_app_framework` 관련 클러스터가 다룬다.

### 관찰 가능한 신호

`adb shell settings get secure enabled_accessibility_services`로 현재 활성화된 접근성 서비스 목록을 확인할 수 있다. `adb shell dumpsys accessibility`로 이벤트 스트림 상태와 등록된 서비스의 상세 설정(어떤 이벤트 타입을 구독하는지)을 볼 수 있다.

### 공식 문서

- https://developer.android.com/guide/topics/ui/accessibility/service
- https://developer.android.com/reference/android/accessibilityservice/AccessibilityService
