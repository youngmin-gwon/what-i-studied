---
title: resource-qualifiers-select-strings-by-runtime-locale
tags: ["android", "android/app-framework"]
aliases: ["리소스 Qualifier는 런타임 로케일에 따라 문자열을 선택한다"]
date modified: 2026-08-04 18:00:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## 리소스 Qualifier는 런타임 로케일에 따라 문자열을 선택한다

Android 는 같은 리소스 ID(`R.string.greeting`)에 여러 값을 준비해 두고, 앱 실행 시점의 `Configuration`(로케일, 화면 크기, 방향 등)에 맞는 값을 골라 쓴다. 문자열 지역화는 이 리소스 선택 메커니즘의 한 적용 사례다. 코드는 "지금 로케일이 무엇인가"를 직접 분기하지 않고 `getString()` 을 호출할 뿐이며, 어떤 값이 반환될지는 리소스 프레임워크가 언어 qualifier 를 기준으로 결정한다.

### 폴더 구조

```
res/
    values/            (기본값, qualifier 없음 — 폴백)
        strings.xml
    values-ko/         (한국어)
        strings.xml
    values-fr/         (프랑스어)
        strings.xml
    values-es-rES/     (스페인어, 스페인 지역 — 언어+지역)
        strings.xml
    values-zh-rTW/     (중국어, 대만 지역)
        strings.xml
```

```xml
<!-- res/values/strings.xml (기본값, 폴백) -->
<resources>
    <string name="greeting">Hello, %1$s!</string>
</resources>

<!-- res/values-ko/strings.xml -->
<resources>
    <string name="greeting">%1$s님, 안녕하세요!</string>
</resources>
```

```kotlin
// 코드는 로케일을 분기하지 않는다 — 리소스 시스템이 이미 고른 값을 받는다
val message = getString(R.string.greeting, userName)
```

### 메커니즘: 선택과 폴백 순서

시스템(또는 [Android 13+ 앱별 언어 설정으로 setApplicationLocales가 시스템 로케일과 별개로 앱 언어를 바꾼다](./per-app-language-with-setapplicationlocales-overrides-system-locale.md) 로 지정된) 로케일을 기준으로, 리소스 프레임워크는 가장 구체적으로 일치하는 qualifier 디렉터리를 찾는다. 정확히 일치하는 언어+지역 조합이 없으면 언어만 일치하는 디렉터리로, 그마저 없으면 qualifier 없는 기본 `values/` 로 폴백한다.

```
사용자 로케일: es-MX (스페인어, 멕시코)

1순위: values-es-rMX  (정확히 일치) — 없음
2순위: values-es       (언어만 일치) — 있으면 선택
3순위: values          (qualifier 없는 기본값) — 최종 폴백
```

이 폴백 체인 때문에 모든 언어에 모든 문자열을 번역할 필요는 없다 — 번역이 없는 문자열은 자동으로 기본 `values/` 값을 쓴다. 반대로 이 사실을 모르면 "번역이 반영이 안 된다"는 문제를 문자열 키 누락이 아니라 다른 원인으로 잘못 조사하기 쉽다.

### 판단 기준

- 언어 코드만으로 부족하고 지역별 표기가 갈리는 경우(예: 스페인어의 스페인/멕시코, 중국어의 간체/번체)에는 지역 qualifier(`-rXX`, 또는 BCP-47 형식 `-b+es+MX`)를 추가한다.
- 복수형, 통화, 날짜 형식처럼 언어만으로 결정되지 않는 값은 `plurals` 리소스나 `ICU` 형식을 함께 사용한다(이 노트에서는 문자열 선택 메커니즘만 다룬다).

### 관찰 가능한 신호

- 기기 언어를 한국어로 바꾸고 앱을 재실행하면(`Configuration` 변경으로 `Activity` 재생성) `values-ko/strings.xml` 값이 반영되는지 확인할 수 있다.
- `adb shell am start -n <package>/<activity> --es "locale" "ko-KR"` 같은 직접 전달보다는, 실제로는 시스템 설정 또는 앱별 언어 설정을 통해 `Configuration.getLocales()` 가 바뀌는지 `Log.d` 로 확인하는 방식이 신뢰도가 높다.
- Android Studio 의 Layout Validation/Locale 미리보기 드롭다운으로 `values-*` 폴더별 렌더링을 빌드 없이 확인할 수 있다.

관련 노트: [Android 13+ 앱별 언어 설정으로 setApplicationLocales가 시스템 로케일과 별개로 앱 언어를 바꾼다](./per-app-language-with-setapplicationlocales-overrides-system-locale.md)

공식 문서: [앱 언어 지원](https://developer.android.com/guide/topics/resources/app-languages), [리소스 제공](https://developer.android.com/guide/topics/resources/providing-resources)

검증일: 2026-08-04. 언어/지역 qualifier 명명 규칙과 BCP-47 형식(`values-b+es+MX` 등)을 공식 문서에서 확인했다.
