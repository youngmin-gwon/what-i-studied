---
title: explicit-intent-targets-known-component-implicit-intent-declares-capability
tags: [android, android/intents, android/navigation]
aliases: ["명시적 Intent와 암시적 Intent를 선택하는 기준"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 명시적 Intent 와 암시적 Intent 를 선택하는 기준

상위 문서: [Intent와 Manifest 계약](intent-manifest-contracts.md)

### 명시적 Intent

명시적 Intent 는 패키지와 컴포넌트 클래스를 직접 지정한다.

시스템은 일반적인 후보 검색 없이 지정된 대상을 실행하려고 한다.

같은 앱의 내부 서비스나 특정 액티비티를 호출할 때 적합하다.

```kotlin
val intent = Intent(this, DetailActivity::class.java).apply {
    putExtra("itemId", itemId)
}
startActivity(intent)
```

명시성은 의도하지 않은 앱이 요청을 가로채는 가능성을 줄인다.

다만 대상 클래스가 바뀌거나 앱이 분리되면 호출 코드도 함께 수정해야 한다.

현대의 Single Activity 구조에서는 화면 이동을 Navigation 으로 처리하는 경우가 많다.

그래도 외부 카메라, 설정 화면, 서비스, 다른 앱의 특정 컴포넌트에는 여전히 유용하다.

### 암시적 Intent

암시적 Intent 는 대상 컴포넌트를 지정하지 않고 작업을 시스템에 위임한다.

시스템은 설치된 앱의 `intent-filter` 와 요청의 필드를 비교한다.

```kotlin
val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
if (intent.resolveActivity(packageManager) != null) {
    startActivity(intent)
}
```

웹 열기, 전화 걸기, 공유, 문서 선택처럼 여러 앱이 처리할 수 있는 작업에 적합하다.

처리 앱이 없거나 여러 개면 실패 또는 선택 UI 가 발생할 수 있다.

공유처럼 사용자가 대상을 고르는 작업은 `Intent.createChooser()` 가 명확한 UX 를 만든다.

### 선택 규칙

| 상황 | 권장 방식 |
| --- | --- |
| 앱 내부의 알려진 서비스 호출 | 명시적 Intent |
| 특정 외부 앱의 알려진 컴포넌트 호출 | 명시적 Intent 와 설치 여부 확인 |
| 웹, 지도, 전화, 공유 | 암시적 Intent |
| 민감한 데이터 전달 | 명시적 Intent 또는 권한으로 제한 |
| 처리 앱이 여러 개일 수 있음 | 암시적 Intent 와 chooser |

### 안전한 호출

`startActivity()` 전에 `resolveActivity()` 로 처리 가능 여부를 확인한다.

URI 를 외부에서 받았다면 허용된 scheme, host, path 만 통과시킨다.

암시적 브로드캐스트에는 민감한 데이터를 넣지 않고 필요하면 명시적 대상으로 좁힌다.

수신 컴포넌트는 호출자가 보낸 `extras` 를 신뢰하지 말고 타입과 범위를 검증한다.

### 정리

명시성은 대상 통제와 보안에 유리하고 암시성은 확장성과 앱 간 연동에 유리하다.

두 방식은 우열이 아니라 호출 계약의 공개 범위가 다르다는 차이다.
