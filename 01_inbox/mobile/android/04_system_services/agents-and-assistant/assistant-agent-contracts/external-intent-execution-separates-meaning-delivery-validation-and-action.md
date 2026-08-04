---
title: external-intent-execution-separates-meaning-delivery-validation-and-action
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-04 15:00:00 +09:00
date created: 2026-07-31 17:42:24 +09:00
---

## 외부 의도 실행은 의미 해석, 전달, 검증, 실행을 분리한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)

관련 지도: [Assistant와 에이전트 통합 계약](01_inbox/mobile/android/04_system_services/agents-and-assistant/assistant-agent-contracts/assistant-agent-contracts.md)

### 단계별 모델

1. 사용자가 자연어로 목표를 말하거나 시스템 표면에서 작업을 선택한다.
2. Assistant 가 질의를 BII 또는 custom intent 의미에 매칭한다.
3. App Actions 가 추출한 parameter 를 fulfillment intent 또는 deep link 에 전달한다.
4. 앱은 전달값을 신뢰하지 않고 검증·정규화한다.
5. 앱 UI 가 선택·확인을 요구하거나, 허용된 경우 도메인 함수를 실행한다.
6. 결과를 사용자에게 보여주고 실패·모호성·추가 인증을 처리한다.

### 노출 가능한 기능의 조건

- 이름만으로 의도가 분명해야 한다.
- 입력값의 단위, 지역, 시간대, 식별자 규칙을 정의해야 한다.
- 읽기 작업과 상태 변경 작업을 구분해야 한다.
- 결제, 메시지 발송, 삭제, 공유처럼 되돌리기 어려운 작업은 확인 단계를 둔다.
- 동일 요청의 재실행이 중복 결과를 만들지 않도록 idempotency 를 고려한다.
- 함수나 Activity 가 실패해도 사용자가 다음 조치를 알 수 있어야 한다.

### App Actions fulfillment 선택

- **명시적 intent**: target package 와 class 를 지정한다. 특정 Activity 로 연결할 때 적합하다.
- **deep link**: 기존 내비게이션 계약을 재사용할 때 적합하다.
- **intent data**: fulfillment URI 를 직접 지정하는 방식이다.
- 이 세 방식은 한 fulfillment 에서 무분별하게 섞지 않는다.

명시적 intent 는 코드에서 이렇게 나타난다. `action`, `data`, `component` 를 한 fulfillment 에 섞지 않고 target 을 명시한다.

```kotlin
Intent(Intent.ACTION_VIEW).apply {
    setClassName("com.example.app", "com.example.app.ExerciseActivity")
    putExtra("exerciseType", "running")
}
```

App Actions 는 사용자의 의도를 앱의 화면 또는 위젯으로 연결하는 데 강하다.

AppFunctions 는 함수의 입력과 결과를 에이전트가 조합할 수 있게 하는 데 강하다.

예를 들어 "운동 시작 화면을 열어줘"는 App Actions 에 가깝고,

"이번 주 운동 기록을 찾아 요약해줘"는 검색·요약 함수 조합을 전제로 AppFunctions 를 검토할 수 있다.

### 설계 원칙

- 앱 UI 를 우회하는 모든 진입점은 공개 API 처럼 버전 관리한다.
- 질의 표현과 내부 도메인 모델을 직접 결합하지 않는다.
- 사용자의 의도보다 넓은 권한이나 동작을 자동으로 추론하지 않는다.

공식 문서: [App Actions fulfillment](https://developer.android.com/develop/devices/assistant/action-schema), [Intents와 intent filters](https://developer.android.com/guide/components/intents-filters)

### 실패와 모호성

질의에 parameter 가 빠졌거나 여러 항목이 같은 이름을 가지면 실행보다 명확화를 우선한다.

앱은 누락된 값을 추측해 민감한 대상을 선택하지 않는다.

네트워크나 저장소 오류가 발생하면 재시도 가능 여부와 사용자가 직접 이어갈 경로를 함께 제공한다.

사용자가 작업을 취소한 경우 에이전트의 이전 계획이 남아 있어도 후속 상태 변경을 실행하지 않는다.

이 경계는 음성 UI, launcher shortcut, deep link, AppFunctions 호출에 공통으로 적용된다.
