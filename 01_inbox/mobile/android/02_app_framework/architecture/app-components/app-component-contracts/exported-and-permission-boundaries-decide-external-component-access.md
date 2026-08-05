---
title: exported-and-permission-boundaries-decide-external-component-access
tags: [android, android/app-components, android/architecture, android/security]
aliases: ["Exported와 permission 경계는 외부 접근을 결정한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Exported와 permission 경계는 외부 접근을 결정한다

안드로이드 애플리케이션 컴포넌트가 외부 타사 앱이나 OS 시스템으로부터 시작될 수 있는지 여부는 **`AndroidManifest.xml` 의 `android:exported` 속성값과 `android:permission` 보호 수준(Protection Level)**에 의해 통제된다.

---

### 1. 개념 및 핵심 명제 (What)

- **`android:exported` 명시적 선언 계약 (Android 12+)**:
  Android 12(API 31) 이상을 타깃으로 하는 모든 컴포넌트 중 Intent Filter 가 선언된 경우 `android:exported="true"` 또는 `"false"` 를 명시하지 않으면 패키지 설치 타임 컴파일 에러가 발생한다.
- **보안 격리 원칙**:
  내부 전용 Activity, Service, Receiver 는 반드시 `exported="false"` 로 설정하여 외부 악의적 인텐트 주입 공격(Intent Hijacking / Unauthorized Access)을 차단해야 한다.

---

### 2. 관련 문서 및 참조

- 상위 문서: [App Component Contracts](./app-component-contracts.md)
- 공식 문서: [Component Security](https://developer.android.com/privacy-and-security/risks/exported-components)

검증일: 2026-08-05. Exported 속성 필수화 규칙 대조 완료.
