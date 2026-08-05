---
title: android-intent-and-ipc
tags: [android, android/navigation, android/intent, android/ipc]
aliases: ["Android Intent and IPC Guide", "안드로이드 인텐트 및 IPC 종합 가이드"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android Intent & IPC 종합 가이드: 컴포넌트 통신과 메시징 아키텍처

안드로이드 OS 환경에서 컴포넌트(Activity, Service, BroadcastReceiver) 간 요청을 매개하고 외부 프로세스 간 통신을 통제하는 **Intent**(안드로이드 컴포넌트 실행 요청 메시지 객체)와 **IPC**(프로세스 간 통신) 아키텍처 가이드다.

---

### 개념과 필요성 (What & Why)

1. **개념 (What)**:
   - **Intent**: 앱 내부 또는 앱 간 컴포넌트(Activity, Service, BroadcastReceiver)를 호출하기 위한 메시징 토큰 개체이다. 명시적(Explicit) Intent와 암시적(Implicit) Intent로 구분된다.
   - **IPC (Inter-Process Communication)**: 안드로이드 OS의 샌드박스 정책을 넘어 다른 앱 프로세스나 시스템 서비스에 작업을 요청하는 메시지 전달 메커니즘으로, 하부 구현은 Linux Kernel의 `Binder` 드라이버에 기반한다.
2. **필요성 (Why)**:
   - **프로세스 샌드박싱 격리**: 각 안드로이드 앱은 고유한 Linux UID와 샌드박스 프로세스를 할당받는다. 따라서 타 프로세스와 메모리를 직접 공유할 수 없으며, 안전하게 검증된 Intent 및 Binder IPC를 통해 메시지를 주고받아야 한다.
   - **보안 경계 통제**: 외부 앱에 노출되는 컴포넌트 경계(`android:exported`)와 패키지 조회 권한(`<queries>`), 위임 실행 토큰(`PendingIntent`)을 엄격히 통제하여 권한 승격 및 권한 남용 공격을 방지한다.

---

### 내부 동작 메커니즘 (How)

```mermaid
graph TD
    A["Intent 발신자 (App Process A)"] -->|startActivity(intent)| B["Android OS ActivityManagerService (AMS)"]
    B --> C{"Intent Filter Resolution"}
    C -->|Explicit Intent| D["Target Component Direct Launch"]
    C -->|Implicit Intent| E["PackageManager (PM) matching action/category/data"]
    E --> F["Security Check: android:exported & Package Visibility"]
    F -->|Allowed| G["Target Component (App Process B via Binder IPC)"]
    F -->|Denied| H["SecurityException / ActivityNotFoundException"]
```

1. **Intent Resolution (해상도 매칭)**:
   - **Explicit Intent**: `SetClass()` 또는 `SetComponent()`를 지정하여 대상 패키지와 컴포넌트 클래스를 직접 지칭한다.
   - **Implicit Intent**: Action(`ACTION_VIEW`), Category(`CATEGORY_DEFAULT`), Data Scheme/Type(`https`) 정보만 제공하면 OS `PackageManagerService`가 Manifest에 선언된 `<intent-filter>` 매칭 규칙을 수행한다.
2. **Security & Package Visibility (<queries>)**:
   - Android 11(API 30)+ 부터 적용된 패키지 가시성(Package Visibility) 정책에 따라, Manifest의 `<queries>` 태그에 선언된 앱 패키지만 조회가 가능하다.
   - 외부 수신 컴포넌트는 `android:exported="true"`로 명시적 선언되어야 하며, 불필요한 노출 시 외부 악성 앱의 엑세스 대상이 된다.

---

### 구시대 레거시 vs 현대 표준 비교 (Legacy vs Modern)

| 구분 | 구시대 레거시 (Legacy) | 현대 안드로이드 표준 (Modern Standard) |
| :--- | :--- | :--- |
| **Activity 결과 수신** | `startActivityForResult()` 및 `onActivityResult()` 재정의 | **Activity Result API** (`registerForActivityResult`, `ActivityResultContract`) |
| **패키지 조회** | `queryIntentActivities()`로 설치된 모든 앱 무조건 조회 | `<queries>` 태그 기반 Package Visibility 제한 및 명시적 거버넌스 |
| **컴포넌트 노출** | `android:exported` 생략 가능 (Intent Filter 존재 시 기본 true 위험) | Android 12+ `android:exported` 명시 필수 작성 강제 |
| **비동기 토큰 실행** | 일반 Intent 전달 및 수동 검증 부족 | `PendingIntent` 래핑 시 `FLAG_IMMUTABLE` / `FLAG_MUTABLE` 명시적 권한 제어 |

---

### 핵심 정본 지도 (Contract Index)

- [Intent & Manifest 계약](intent-manifest-contracts/intent-manifest-contracts.md)
- [Intent는 컴포넌트 실행을 설명하는 메시지다](intent-manifest-contracts/intent-describes-component-action-request.md)
- [Explicit intent는 알려진 컴포넌트를 지정하고 implicit intent는 요구 능력을 선언한다](intent-manifest-contracts/explicit-intent-targets-known-component-implicit-intent-declares-capability.md)
- [Exported 속성은 외부 컴포넌트 경계를 정의한다](intent-manifest-contracts/exported-attribute-defines-external-component-boundary.md)
- [Intent filter는 컴포넌트의 수신 계약이다](intent-manifest-contracts/intent-filter-is-component-receiving-contract.md)
- [PendingIntent는 위임된 미래 intent 토큰이다](intent-manifest-contracts/pendingintent-is-delegated-future-intent-token.md)
- [Activity Result API는 수명주기를 인식하는 결과 계약을 정의한다](intent-manifest-contracts/activity-result-api-defines-lifecycle-aware-result-contract.md)
- [Package visibility는 조회 가능한 앱을 제한한다](intent-manifest-contracts/package-visibility-limits-which-apps-can-be-queried.md)

---

### 연관 상위 및 관련 가이드

- [Android Deep Links 종합 가이드](android-deep-links.md)
- [Android Navigation 진입 계약](../navigation-contracts/navigation-contracts.md)
