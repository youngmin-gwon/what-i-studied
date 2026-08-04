---
title: foreground-service-is-for-visible-continuous-work
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-03 17:35:51 +09:00
date created: 2026-07-31 17:42:24 +09:00
---

## Foreground service 는 사용자에게 보이는 지속 작업에 쓴다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)

관련 지도: [백그라운드 작업 계약](./background-work-contracts.md)

### 핵심 주장

- foreground service 는 사용자가 작업 진행을 인지해야 하는 지속 작업에 사용한다.
- 음악 재생, 내비게이션, 운동 추적처럼 실행 중 상태가 사용자 경험의 일부인 경우가 대표적이다.
- 서비스가 포그라운드라는 말은 앱 화면이 보인다는 뜻이 아니라 지속 알림으로 실행 상태를 드러낸다는 뜻이다.
- 서비스는 시작 직후 적절한 알림과 foreground 상태를 설정해야 한다.
- Android 14 이상에서는 작업 성격에 맞는 foreground service type 과 관련 권한을 선언해야 한다.
- 타입 선언은 형식 요건이 아니라 서비스가 실제로 수행하는 작업을 설명하는 계약이다.
- 서비스 타입을 실제 작업과 다르게 선택해 제한을 피하려 해서는 안 된다.
- Android 와 Google Play 는 foreground service 사용 목적과 권한을 별도로 검토한다.

### 운영 원칙

- 사용자가 시작과 중지를 이해할 수 있는 UI 와 알림 액션을 제공한다.
- 작업이 끝나면 서비스를 즉시 중지하고 지속 알림도 제거한다.
- 프로세스가 회수될 수 있으므로 진행 상태와 재개 정책을 저장한다.
- 서비스 안에서 무제한 재시도나 불필요한 폴링을 수행하지 않는다.
- 단순한 업로드나 주기 동기화를 foreground service 로 포장하지 않는다.
- 서비스 시작 제한에 걸릴 수 있으므로 사용자 동작과 허용된 시작 시점을 설계에 반영한다.
- 알림 권한이 거부된 경우에도 기능의 허용 범위와 실패 상태를 명확히 처리한다.

### 버전 경계

- target 31+ 는 일부 예외를 제외하고 앱이 백그라운드인 동안 FGS 를 시작할 수 없으며, 위반하면 `ForegroundServiceStartNotAllowedException` 이 발생한다.
- target 34+ 는 FGS 생성 시 선언 type 과 type 별 권한을 검사한다. camera, microphone, location 처럼 while-in-use 권한이 필요한 type 은 보이는 Activity 에서 시작하는 흐름이 원칙이다.
- Android 15 이상에서 target 35+ 인 앱의 `dataSync` 와 `mediaProcessing` 은 앱이 백그라운드인 동안 type 별로 24 시간 중 총 6 시간 제한을 받는다. `Service.onTimeout()` 에서 즉시 상태를 저장하고 중지해야 한다.
- `shortService` 등 type 별 제한은 서로 다르므로 "FGS 는 계속 실행된다"는 공통 가정을 두지 않는다.

### WorkManager 와의 경계

- 작업이 사용자에게 계속 보여야 하는지는 실행 시간이 아니라 사용자 가치로 판단한다.
- 사용자에게 보일 필요가 없고 지연 가능한 작업이면 WorkManager 가 더 적절하다.
- WorkManager 가 실행 중 알림을 요구하는 장시간 작업은 foreground worker 형태를 검토할 수 있다.

### 사용자와 시스템의 계약

- 알림에는 현재 작업, 진행 정도, 예상 상태를 짧고 명확하게 표시한다.
- 알림을 숨기는 것보다 작업의 사용자 가치를 설명하고 중지 경로를 제공한다.
- 서비스가 재시작될 때 이전 작업을 복구할지 새 작업으로 시작할지 명시한다.
- 위치나 마이크처럼 민감한 자원을 사용하는 동안에는 관련 표시와 권한 상태를 일관되게 유지한다.
- 서비스 타입에 필요한 런타임 권한과 선언 권한을 각각 확인한다.
- 서비스가 실패하면 알림을 갱신하고 사용자에게 재시작 또는 종료 선택지를 제공한다.
- 화면이 사라졌다는 이유만으로 foreground service 를 계속 유지하지 않는다.
- 서비스가 필요 없어진 순간을 도메인 상태로 판단할 수 있어야 한다.

### 공식 문서

- [foreground service 개요](https://developer.android.com/develop/background-work/services/fgs)
- [foreground service 타입](https://developer.android.com/develop/background-work/services/fgs/service-types)
- [백그라운드 시작 제한](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start)
- [foreground service timeout](https://developer.android.com/develop/background-work/services/fgs/timeout)
- [Android 14 동작 변경](https://developer.android.com/about/versions/14/behavior-changes-14)

검증일: 2026-08-03. 실행 제한은 OS 버전, target SDK, service type, 현재 권한 상태를 각각 분리해 확인했다.
