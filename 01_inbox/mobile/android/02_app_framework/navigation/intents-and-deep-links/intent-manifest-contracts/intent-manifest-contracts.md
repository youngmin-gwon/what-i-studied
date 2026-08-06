---
title: intent-manifest-contracts
tags: [android, android/navigation, android/intent]
aliases: ["Intent Manifest 계약", "Intent Manifest Contracts"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Intent & Manifest 계약 (Intent & Manifest Contracts)

안드로이드 OS 레벨에서 애플리케이션 컴포넌트(Activity, Service, BroadcastReceiver)의 진입점과 보안 경계를 정의하고 통제하는 계약 모음이다.

---

### 핵심 계약 가이드라인

1. **컴포넌트 선언 및 경계 통제 계약**:
   - OS에 노출되는 모든 컴포넌트는 `AndroidManifest.xml`에 선언되어야 하며, 외부 앱과의 수신 경계인 `android:exported` 속성을 명시적으로 설정해야 한다.
2. **Intent 통신 및 보안 위임 계약**:
   - 명시적(Explicit) Intent와 암시적(Implicit) Intent의 역할을 엄격히 구분한다.
   - 비동기 위임 토큰인 `PendingIntent` 생성 시 `FLAG_IMMUTABLE` 권한 제어를 강제한다.
3. **라이프사이클 인지 결과 수신 및 패키지 가시성 계약**:
   - 레거시 `onActivityResult()`를 대체하여 라이프사이클을 인지하는 **Activity Result API**를 사용한다.
   - Android 11+ 패키지 가시성 정책에 따라 Manifest `<queries>` 선언을 통해 타 앱 조회를 통제한다.

---

### 하위 세부 계약 목록

- [AndroidManifest는 OS에 노출되는 컴포넌트와 진입점을 선언한다](android-manifest-declares-os-visible-components-and-entry-points.md)
- [Intent는 컴포넌트 실행을 설명하는 메시지다](intent-describes-component-action-request.md)
- [Explicit intent는 알려진 컴포넌트를 지정하고 implicit intent는 요구 능력을 선언한다](explicit-intent-targets-known-component-implicit-intent-declares-capability.md)
- [Exported 속성은 외부 컴포넌트 경계를 정의한다](exported-attribute-defines-external-component-boundary.md)
- [Intent filter는 컴포넌트의 수신 계약이다](intent-filter-is-component-receiving-contract.md)
- [Intent filter는 action, category, data를 매칭한다](intent-filter-matches-action-category-data.md)
- [Intent 입력은 명시적 타입과 신뢰 경계가 필요하다](intent-inputs-need-explicit-type-and-trust-boundaries.md)
- [PendingIntent는 위임된 미래 intent 토큰이다](pendingintent-is-delegated-future-intent-token.md)
- [PendingIntent FLAG_IMMUTABLE vs FLAG_MUTABLE 보안 비교](../pendingintent-immutable-vs-mutable.md)
- [Activity Result API는 수명주기를 인식하는 결과 계약을 정의한다](activity-result-api-defines-lifecycle-aware-result-contract.md)
- [Package visibility는 조회 가능한 앱을 제한한다](package-visibility-limits-which-apps-can-be-queried.md)

---

### 상위 및 연관 지도

- 상위 가이드: [Android Intent 및 IPC 종합 가이드](../android-intent-and-ipc.md)
- 연관 가이드: [Android Deep Links 종합 가이드](../android-deep-links.md)
