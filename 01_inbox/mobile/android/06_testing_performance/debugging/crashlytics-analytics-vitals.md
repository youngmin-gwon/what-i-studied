---
title: crashlytics-analytics-vitals
tags: ["android", "android/testing-performance"]
aliases: ["Crashlytics/Analytics SDK는 Android vitals에 없는 옵트인 컨텍스트를 더한다"]
date modified: 2026-08-04 20:20:00 +09:00
date created: 2026-08-04 20:20:00 +09:00
---

## Crashlytics/Analytics SDK 는 Android vitals 에 없는 옵트인 컨텍스트를 더한다

상위 문서: [디버깅 도구 계약](./debugging.md)

### 핵심 주장

Android vitals(Play Console)는 사용자 동의 시 기기가 자동으로 수집하는 안정성·성능·배터리 지표이며 앱 코드가 무엇을 로깅할지 개입할 수 없다. Firebase Crashlytics 같은 서드파티 SDK 는 그 반대다 — 앱이 명시적으로 호출해야만 데이터가 남는다: 어떤 non-fatal 예외를 기록할지, 크래시 직전에 어떤 커스텀 로그를 남길지, 어떤 사용자 식별자를 붙일지 전부 코드로 결정한다. 이 vault 의 [Learning Spine 11장](../../00_foundations/learning-spine/11-observation-testing-and-quality-feedback.md)이 다루는 Android vitals 피드백 루프와, 이 노트가 다루는 opt-in SDK 는 "자동 수집 vs 명시적 계측"이라는 서로 다른 축이며 대체 관계가 아니라 보완 관계다.

### 메커니즘

`FirebaseCrashlytics` SDK 는 세 가지를 앱 코드에서 명시적으로 남긴다.

```kotlin
// 1. 크래시로 이어지지 않은 예외도 기록(non-fatal event)
try {
    repository.syncNow()
} catch (e: SyncException) {
    FirebaseCrashlytics.getInstance().recordException(e)
    // 앱은 계속 실행되지만 이 예외는 대시보드에 별도로 집계된다
}

// 2. 크래시 직전 상황을 설명하는 커스텀 로그
FirebaseCrashlytics.getInstance().log("checkout: payment step started")

// 3. 어떤 사용자군에서 발생했는지(익명 식별자)
FirebaseCrashlytics.getInstance().setUserId(anonymizedUserId)
```

공식 문서에 따르면 non-fatal 이벤트와 커스텀 로그는 즉시 전송되지 않고 기기에 기록된 뒤 "다음 fatal crash 리포트와 함께, 또는 사용자가 앱을 다시 시작할 때" 함께 업로드된다. 즉 방금 발생한 non-fatal 예외를 실시간 대시보드에서 바로 보지 못하는 것이 정상 동작이다.

### 판단 기준

- 기기·OS·프로세서 종류에 따른 전반적 안정성 분포(예: "특정 기기에서만 크래시율이 높다")는 이미 Android vitals 가 코드 계측 없이 제공한다 — 이 목적만이면 서드파티 SDK 를 추가할 필요가 없다.
- "이 결제 흐름에서 어떤 단계까지 진행했는지", "이 예외가 어떤 사용자 세그먼트에서 반복되는지"처럼 앱 도메인 지식이 필요한 진단은 vitals 가 채울 수 없는 영역이라 opt-in 계측이 필요하다.
- non-fatal 예외를 남용해 실제로는 정상 흐름인 이벤트까지 기록하면 대시보드 신호 대 잡음비가 나빠진다. `recordException()`은 "코드가 계속 실행되지만 조사할 가치가 있는 이상 상태"에만 쓴다.

### 경계

- 이 노트는 Crashlytics 류 SDK 의 계측 모델까지만 다룬다. Play Console 이 기기 동의 기반으로 자동 수집하는 vitals 자체의 지표 종류는 [11장 관찰, 테스트와 품질 feedback](../../00_foundations/learning-spine/11-observation-testing-and-quality-feedback.md)이 다룬다.
- logcat/ANR trace 같은 로컬 진단 도구와의 역할 구분은 [Logcat, crash, ANR, debugger는 서로 다른 질문에 답한다](logcat-crash-anr-diagnosis.md)가 다룬다.
- 이벤트 분석(Firebase Analytics 의 funnel/retention 지표) 자체의 지표 설계는 이 노트의 범위 밖이다 — 여기서는 "옵트인 계측이 vitals 와 다른 축"이라는 계약만 다룬다.

### 관찰 가능한 신호

`recordException()` 으로 남긴 non-fatal 이벤트는 호출 즉시가 아니라 다음 fatal crash 또는 앱 재시작 시점에 함께 업로드된다 — 그래서 테스트 중 "방금 기록한 non-fatal 이 대시보드에 안 보인다"는 증상은 버그가 아니라 정상적인 배치 업로드 지연이다. 강제로 즉시 확인하려면 테스트 코드에서 앱을 의도적으로 재시작시키거나 디버그 빌드에서 `sendUnsentReports()` 류 API 로 강제 flush 해야 한다.

### 공식 문서

- [Get started with Firebase Crashlytics](https://firebase.google.com/docs/crashlytics/get-started?platform=android)
- [Customize crash reports](https://firebase.google.com/docs/crashlytics/customize-crash-reports?platform=android)

검증일: 2026-08-04. non-fatal 이벤트가 다음 crash/재시작 시점에 배치 업로드된다는 점, `log()`/`setUserId()` 동작을 공식 문서로 확인.
