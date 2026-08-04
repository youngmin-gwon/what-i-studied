---
title: android-external-execution-surfaces-split-app-actions-and-appfunctions
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-04 15:00:00 +09:00
date created: 2026-07-31 17:42:24 +09:00
---

## Android 외부 실행 표면은 App Actions 와 AppFunctions 로 나뉜다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)

관련 지도: [Assistant와 에이전트 통합 계약](01_inbox/mobile/android/04_system_services/agents-and-assistant/assistant-agent-contracts/assistant-agent-contracts.md)

### 한 문장 요약

Android 앱은 사용자의 의도를 앱 화면으로 연결하는 App Actions 와, 앱 기능을 시스템 에이전트의 도구로 등록하는 AppFunctions 를 서로 다른 계층에서 사용할 수 있다.

### 핵심 구성요소

1. **사용자 의도**: 자연어, 음성, 제안, 시스템 표면에서 사용자가 원하는 작업을 표현한다.
2. **Assistant**: App Actions 의 BII 를 해석하고 fulfillment 를 선택하는 호출 표면이다.
3. **App Actions**: `shortcuts.xml` 의 `capability` 로 일반적인 작업을 선언한다.
4. **Android intent**: 선택된 Activity, deep link 또는 다른 fulfillment 대상에 입력을 전달한다.
5. **AppFunctions**: 앱의 기능과 데이터를 에이전트가 발견하고 실행할 수 있는 함수형 도구로 노출한다.
6. **앱 도메인 로직**: 입력을 검증하고 권한·인증·상태를 확인한 뒤 실제 작업을 수행한다.

### 관계를 구분하는 기준

| 질문 | App Actions | AppFunctions |
| --- | --- | --- |
| 무엇을 모델링하는가 | 사용자가 하려는 일반적 작업 | 앱이 제공하는 실행 가능한 함수 |
| 주된 선언 | `shortcuts.xml` 의 BII 또는 custom intent | Jetpack AppFunctions API 와 KSP compiler |
| 대표 호출자 | Google Assistant | 권한을 가진 시스템 앱·에이전트·assistant |
| 결과 연결 | Activity, deep link, 위젯 등 fulfillment | 함수 실행 결과와 상태 |
| 현재 상태 | 지원되는 App Actions 기능 | Android 16+ 실험적 preview |

App Actions 의 BII 는 Android intent 와 같은 개념이 아니다.

Google 은 BII 를 사용자의 질의 의미로 해석하고, 앱은 이를 Android intent fulfillment 로 매핑한다.

반대로 AppFunctions 는 앱 기능 자체를 시스템 registry 에 등록하는 플랫폼 API 다.

### 선택 규칙

- Assistant 가 특정 화면을 열어 사용자가 이어서 작업하면 App Actions 를 검토한다.
- 에이전트가 앱의 함수들을 조합하거나 결과를 받아 다음 작업을 결정해야 하면 AppFunctions 를 검토한다.
- 두 방식을 함께 쓸 때도 각각의 입력 계약과 보안 경계를 별도로 유지한다.
- UI 진입이 필요한 작업과 백그라운드 함수 실행을 같은 계약으로 가정하지 않는다.

### 선언 형태로 구분하는 신호

두 표면은 코드 레벨에서 이렇게 구분된다.

```xml
<!-- App Actions: shortcuts.xml 의 capability -->
<capability android:name="actions.intent.START_EXERCISE">
  <intent android:action="android.intent.action.VIEW" ... />
</capability>
```

```kotlin
// AppFunctions: 함수에 붙는 어노테이션
@AppFunction
suspend fun createNote(title: String, content: String): CreateNoteResult
```

`shortcuts.xml` 에 `capability` 가 있으면 App Actions, 코드에 `@AppFunction` 이 있으면 AppFunctions 다. 한 저장소에 두 선언이 같은 기능을 가리켜도 서로 다른 registry 와 호출 경로로 등록된다.

공식 문서: [App Actions 개요](https://developer.android.com/develop/devices/assistant/get-started), [AppFunctions 개요](https://developer.android.com/ai/appfunctions)

### 오해하기 쉬운 지점

- App Actions 를 등록했다고 앱의 모든 내부 API 가 외부에 공개되는 것은 아니다.
- AppFunctions 를 선언했다고 임의의 제 3 자 앱이 함수를 실행할 수 있는 것도 아니다.
- Android intent 는 전달 메커니즘이고, 사용자 의도나 권한 승인 자체가 아니다.
- 에이전트의 계획 수립과 앱의 최종 실행 허가는 서로 다른 책임이다.

따라서 문서와 코드에서 `의미 해석`, `호출 전달`, `권한 확인`, `도메인 실행` 을 분리해 설명한다.

검증일: 2026-08-03. App Actions 의 BII/fulfillment 모델과 AppFunctions 의 Android 16+ preview 상태를 위 공식 문서에서 확인했다.
