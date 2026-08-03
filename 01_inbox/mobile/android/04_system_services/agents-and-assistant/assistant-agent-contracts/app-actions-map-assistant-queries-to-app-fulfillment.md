---
title: app-actions-map-assistant-queries-to-app-fulfillment
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-03 18:13:11 +09:00
date created: 2026-07-31 17:42:24 +09:00
---

## App Actions 는 Assistant 질의를 앱 fulfillment 로 연결한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)

관련 지도: [Assistant와 에이전트 통합 계약](01_inbox/mobile/android/04_system_services/agents-and-assistant/assistant-agent-contracts/assistant-agent-contracts.md)

### 목적

App Actions 는 사용자가 Assistant 에 말하거나 입력한 작업을 앱의 기능으로 연결한다.

Built-in Intent(BII)는 운동 시작, 주차 찾기처럼 여러 앱에서 공통적인 사용자 작업을 의미 모델로 표현한다.

### 선언 흐름

1. 앱 기능과 가장 가까운 BII 를 찾는다.
2. `res/xml/shortcuts.xml` 에 `capability` 를 선언한다.
3. 하나 이상의 fulfillment `intent` 를 정의한다.
4. BII parameter 를 Android intent extra 또는 URL template parameter 에 매핑한다.
5. AndroidManifest 의 `android.app.shortcuts` metadata 로 파일을 등록한다.
6. App Actions test tool 과 실제 질의 변형으로 검증한다.

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

`capability` 의 BII 와 fulfillment 의 Android intent 는 역할이 다르다.

BII 는 질의를 분류하고, fulfillment intent 는 앱 안에서 어디로 이동할지 지정한다.

필요하면 여러 fulfillment 를 두어 parameter 가 풍부한 질의와 모호한 질의를 각각 처리한다.

모호한 값은 곧바로 실행하지 말고 앱의 검색·선택 화면에서 disambiguation 한다.

### BII 와 custom intent

- BII 는 Android 가 정의한 공통 의미와 parameter 를 사용한다.
- 대응하는 BII 가 없으면 custom intent 를 사용할 수 있다.
- custom intent 에는 `app:queryPatterns` 와 semantic MIME type 이 필요하다.
- custom intent 이름은 `custom.actions.intent` 접두사를 사용하고 BII 이름과 구분한다.

App Actions 의 노출 여부는 질의의 관련성, 품질, 지역·언어 지원 등의 요인에 따라 결정된다.

선언했다고 모든 질의에서 항상 노출된다고 가정하지 않는다.

공식 문서: [BII 구현](https://developer.android.com/develop/devices/assistant/intents), [shortcuts.xml 작성](https://developer.android.com/develop/devices/assistant/action-schema), [custom intents](https://developer.android.com/develop/devices/assistant/custom-intents)

검증일: 2026-08-03. BII 목록, locale 지원, App Actions test tool preview 조건은 배포 전에 다시 확인한다.
