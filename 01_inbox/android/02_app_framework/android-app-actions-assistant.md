---
title: android-app-actions-assistant
tags: [android, android/assistant, android/app-actions, android/app-functions]
aliases: [App Actions, Google Assistant, BII, shortcuts.xml, AppFunctions]
date modified: 2026-04-04 00:22:00 +09:00
date created: 2026-04-04 00:22:00 +09:00
---

## Assistant Integration: App Actions & AppFunctions

안드로이드 앱은 구글 어시스턴트(Google Assistant)와 긴밀하게 통합되어 음성 명령이나 자동화된 제안을 통해 사용자에게 다가갈 수 있다. **App Actions**는 기존의 `shortcuts.xml`을 활용한 표준 방식이며, **AppFunctions**는 AI 에이전트 시대를 겨냥한 차세대 기술이다.

> [!NOTE] **iOS 비교: App Intents vs App Actions**
> - **iOS**: `App Intents` 프레임워크를 통해 Siri, 단축어(Shortcuts), 위젯, Apple Intelligence와 통합한다. (iOS 16+)
> - **Android**: `App Actions`를 통해 구글 어시스턴트와 통합하며, `shortcuts.xml`에 정의된 BII(Built-in Intents)를 매핑한다. 두 플랫폼 모두 시스템이 앱의 기능을 이해하고 실행할 수 있도록 정형화된 인터페이스를 제공한다.
> 자세한 내용은 [apple-app-intents](../../apple/04_system_services/apple-app-intents.md)를 참고하세요.

### 1. App Actions (Built-in Intents, BII)

사용자가 "Hey Google, [App Name]에서 [Action]해줘"라고 말할 때 앱이 바로 반응하도록 설계되었다.

#### `shortcuts.xml` 정의

```xml
<shortcuts xmlns:android="http://schemas.android.com/apk/res/android">
    <capability android:name="actions.intent.START_EXERCISE">
        <intent
            android:action="android.intent.action.VIEW"
            android:targetPackage="com.example.app"
            android:targetClass="com.example.app.ExerciseActivity">
            <parameter
                android:name="exercise.name"
                android:key="exerciseType" />
        </intent>
    </capability>
</shortcuts>
```

#### AndroidManifest 등록

```xml
<meta-data
    android:name="android.app.shortcuts"
    android:resource="@xml/shortcuts" />
```

### 2. AppFunctions (차세대 AI 에이전트 통합)

Android 16+ 및 최신 Jetpack 라이브러리를 통해 도입된 **AppFunctions**는 AI 기반 어시스턴트가 앱 내부의 특정 로직을 마치 API처럼 호출할 수 있도록 해준다.

> [!CAUTION] **Devil's Advocate : AI 시대를 대비하라**
> 사용자가 앱을 직접 열고 버튼을 누르기를 기다리는 시대는 지나가고 있다. AI 에이전트가 내 앱의 핵심 기능을 "함수"로 호출할 수 있도록 개방하는 것이 미래의 핵심 경쟁력이다.

#### AppFunction 구현 예시 (개념적)

```kotlin
@AppFunction(name = "send_message")
suspend fun sendMessage(recipient: String, body: String): MessageResult {
    return chatRepository.send(recipient, body)
}
```

### 🏛️ 핵심 아키텍처 및 보안

어시스턴트 호출은 보안이 중요하다. 항상 호출의 출처를 검증하고, 민감한 작업(결제 등)은 추가 인증을 거쳐야 한다.

```kotlin
// 호출 데이터 검증 예시
val exerciseType = intent.getStringExtra("exerciseType")
if (exerciseType != null) {
    viewModel.startExercise(exerciseType)
}
```

### 더 보기
- [android-intent-and-ipc](android-intent-and-ipc.md)
- [android-deep-links](android-deep-links.md)
- [android-coroutines-flow](android-coroutines-flow.md)
- [android-jetpack-architecture](android-jetpack-architecture.md)
