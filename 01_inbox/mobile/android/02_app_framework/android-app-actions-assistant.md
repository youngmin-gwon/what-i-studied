---
title: android-app-actions-assistant
tags: []
aliases: []
date modified: 2026-04-05 17:42:55 +09:00
date created: 2026-04-04 00:22:50 +09:00
---

## [[mobile-security]] > [[android-app-actions-assistant]]

### Assistant: Voice & Shortcut Actions

구글 어시스턴트(Google Assistant)를 통해 음성 명령과 지능형 제안을 처리하는 **App Actions**와 **BII(Built-in Intents)** 통합 기법을 분석합니다.

사용자가 앱을 직접 실행하지 않고도 원하는 기능을 수행할 수 있도록 `shortcuts.xml` 을 기반으로 시스템과 소통하고, 사용자 여정을 효율적으로 단축하는 인터페이스를 구축하는 것이 목표입니다.

---

#### 💡 Context: 보이스 퍼스트(Voice-First) 인터페이스

스마트폰 사용 경험은 터치를 넘어 음성과 자동화로 확장되고 있습니다. App Actions 는 앱의 기능을 시스템 수준의 역량(Capability)으로 노출하여 외부 진입점을 극대화합니다. [[android-deep-links]] 및 [[android-intent-and-ipc]] 아키텍처 위에서 동작하는 고급 통합 기술입니다.

>[!NOTE] **상호 참조**
>iOS 의 Siri 및 App Intents 통합 방식은 [[apple-app-intents]] 를 참고하세요.

---

#### 1. App Actions (Built-in Intents, BII)

사용자가 "Hey Google, [App Name]에서 [Action]해줘"라고 말할 때 앱이 바로 반응하도록 설계되었다.

##### `shortcuts.xml` 정의

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

##### AndroidManifest 등록

```xml
<meta-data
    android:name="android.app.shortcuts"
    android:resource="@xml/shortcuts" />
```

#### 2. AppFunctions (차세대 AI 에이전트 통합)

Android 16+ 및 최신 Jetpack 라이브러리를 통해 도입된 **AppFunctions**는 AI 기반 어시스턴트가 앱 내부의 특정 로직을 마치 API 처럼 호출할 수 있도록 해준다.

>[!CAUTION] **Devil's Advocate : AI 시대를 대비하라**
>사용자가 앱을 직접 열고 버튼을 누르기를 기다리는 시대는 지나가고 있다. AI 에이전트가 내 앱의 핵심 기능을 "함수"로 호출할 수 있도록 개방하는 것이 미래의 핵심 경쟁력이다.

##### AppFunction 구현 예시 (개념적)

```kotlin
@AppFunction(name = "send_message")
suspend fun sendMessage(recipient: String, body: String): MessageResult {
    return chatRepository.send(recipient, body)
}
```

#### 🏛️ 핵심 아키텍처 및 보안

어시스턴트 호출은 보안이 중요하다. 항상 호출의 출처를 검증하고, 민감한 작업(결제 등)은 추가 인증을 거쳐야 한다.

```kotlin
// 호출 데이터 검증 예시
val exerciseType = intent.getStringExtra("exerciseType")
if (exerciseType != null) {
    viewModel.startExercise(exerciseType)
}
```

#### See Also

- [[android-intent-and-ipc]]
- [[android-deep-links]]
- [[android-coroutines-flow]]
- [[android-jetpack-architecture]]
