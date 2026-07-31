---
title: "Android Intent 는 컴포넌트 실행을 설명하는 메시지다"
tags: [android, android/navigation, android/intents]
aliases: ["Android Intent 는 컴포넌트 실행을 설명하는 메시지다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Android Intent 는 컴포넌트 실행을 설명하는 메시지다

상위 문서: [Intent와 Manifest 계약](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md)

### 핵심 주장

Intent 는 안드로이드 컴포넌트 사이에서 작업을 요청하는 메시지 객체다.

호출자는 실행할 작업과 입력을 표현하고, 시스템은 적절한 컴포넌트에 전달한다.

따라서 Intent 는 단순한 화면 이동 명령보다 넓은 IPC 계약으로 이해해야 한다.

### Intent 가 담는 정보

| 필드 | 의미 | 예시 |
| --- | --- | --- |
| `action` | 수행하려는 일반적인 작업 | `ACTION_VIEW`, `ACTION_SEND` |
| `data` | 작업 대상 URI | `https://example.com/item/3` |
| `type` | 데이터의 MIME 타입 | `text/plain`, `image/*` |
| `component` | 실행할 패키지와 클래스 | `ComponentName` |
| `category` | 실행 맥락이나 분류 | `CATEGORY_BROWSABLE` |
| `extras` | 추가 입력 데이터 | `userId=3` |
| `flags` | 실행 방식 제어 | task 와 back stack 제어 |

```kotlin
val intent = Intent(Intent.ACTION_VIEW).apply {
    data = Uri.parse("https://example.com/items/3")
    addCategory(Intent.CATEGORY_BROWSABLE)
    putExtra("referrer", "notification")
}
```

### 데이터와 라우팅의 분리

`action`, `data`, `category` 는 시스템이 대상을 찾는 데 사용된다.

`extras` 는 대상을 찾은 뒤 수신 컴포넌트가 읽는 애플리케이션 데이터다.

그러므로 `extras` 만 바꿔서는 다른 컴포넌트가 선택되지 않는다.

URI 는 위치나 식별자를 표현하고 MIME 타입은 데이터 형식을 표현한다.

둘을 함께 사용할 때는 수신 필터가 두 조건을 모두 처리할 수 있어야 한다.

`component` 를 지정하면 일반적인 암시적 해석보다 특정 컴포넌트 지정이 우선한다.

### Intent 를 사용할 때의 점검

1. 이 요청은 앱 내부 컴포넌트인가, 외부 앱인가?
2. 대상이 없을 때 사용자에게 보여줄 대체 흐름이 있는가?
3. `extras` 의 타입과 필수 여부를 수신 측에서 검증하는가?
4. 민감한 값을 암시적 Intent 로 노출하고 있지 않은가?
5. 링크나 URI 를 받은 뒤 허용된 scheme 과 host 를 확인하는가?

### 정리

Intent 는 실행 대상 자체가 아니라 실행 의도를 표현하는 데이터 구조다.

시스템 라우팅이 필요한 경우에는 필드와 Manifest 의 필터가 함께 계약을 이룬다.

명시적 호출은 대상 통제를 강화하고, 암시적 호출은 컴포넌트 교체 가능성을 높인다.

### 공식 문서

- [Intents and intent filters](https://developer.android.com/guide/components/intents-filters)
