---
title: per-app-language-with-setapplicationlocales-overrides-system-locale
tags: ["android", "android/app-framework"]
aliases: ["Android 13+ 앱별 언어 설정으로 setApplicationLocales가 시스템 로케일과 별개로 앱 언어를 바꾼다"]
date modified: 2026-08-04 18:00:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## Android 13+ 앱별 언어 설정으로 setApplicationLocales가 시스템 로케일과 별개로 앱 언어를 바꾼다

[리소스 Qualifier는 런타임 로케일에 따라 문자열을 선택한다](./resource-qualifiers-select-strings-by-runtime-locale.md) 에서 설명한 선택 메커니즘은 "현재 `Configuration` 의 로케일이 무엇인가"를 전제로 동작한다. 전통적으로 이 로케일은 시스템 설정 하나였다 — 기기 전체가 한 언어로 통일된다. Android 13(API 33)부터는 앱마다 별도의 언어를 시스템 언어와 독립적으로 지정할 수 있는 앱별 언어(per-app language) 기능이 플랫폼에 들어왔다. 다국어 사용자가 번역 앱은 중국어로, 은행 앱은 힌디어로 쓰면서 시스템 언어는 영어로 유지하는 시나리오가 이 계약의 핵심이다.

### 메커니즘: LocaleManager와 AppCompatDelegate

Android 13+ 에서 프레임워크 API 는 `LocaleManager` 다.

```kotlin
val localeManager = context.getSystemService(LocaleManager::class.java)
localeManager.applicationLocales = LocaleList(Locale.forLanguageTag("ko-KR"))
```

Android 12 이하까지 호환하려면 AndroidX `AppCompatDelegate`(1.6.0+)를 쓴다. 이 API 는 Android 13+ 에서는 내부적으로 `LocaleManager` 를 호출하고, 그 이하 버전에서는 자체적으로 `Configuration` 을 재구성해 같은 효과를 낸다.

```kotlin
import androidx.appcompat.app.AppCompatDelegate
import androidx.core.os.LocaleListCompat

// 앱 언어를 프랑스어로 설정 — 시스템 언어는 그대로 둔다
val appLocale = LocaleListCompat.forLanguageTags("fr")
AppCompatDelegate.setApplicationLocales(appLocale)

// 현재 앱 언어 조회
val current = AppCompatDelegate.getApplicationLocales().get(0)?.toLanguageTag() ?: "en"
```

`setApplicationLocales()` 를 호출하면 시스템은 `Configuration` 변경으로 처리해 현재 `Activity` 를 재생성한다 — [리소스 Qualifier는 런타임 로케일에 따라 문자열을 선택한다](./resource-qualifiers-select-strings-by-runtime-locale.md) 의 선택 메커니즘이 이 새 로케일 값을 기준으로 다시 동작한다. 또한 이 설정은 시스템 설정(Settings > 앱 > 언어)과 양방향으로 동기화된다 — API 로 설정한 값이 시스템 설정 화면에 그대로 보이고, 사용자가 시스템 설정에서 바꾼 값도 `getApplicationLocales()` 로 읽힌다.

### 시스템 언어 설정 화면 노출

Android 13+ 에서 시스템의 앱별 언어 설정 화면(Settings > System > Languages & Input > App Languages)에 앱이 나타나게 하려면 매니페스트에 지원 언어 목록을 선언해야 한다.

```xml
<!-- AndroidManifest.xml -->
<application android:localeConfig="@xml/locale_config">
```

```xml
<!-- res/xml/locale_config.xml -->
<locale-config xmlns:android="http://schemas.android.com/apk/res/android">
    <locale android:name="en-US"/>
    <locale android:name="ko"/>
    <locale android:name="fr"/>
</locale-config>
```

Android 12 이하 기기에서 API 로 설정한 값을 앱 재시작 후에도 유지하려면(AndroidX 의 자동 저장), 다음 meta-data 를 매니페스트에 추가한다.

```xml
<service
    android:name="androidx.appcompat.app.AppLocalesMetadataHolderService"
    android:enabled="false"
    android:exported="false">
    <meta-data
        android:name="autoStoreLocales"
        android:value="true" />
</service>
```

### 경계

- 이 기능은 리소스 qualifier 폴백 체인 자체를 바꾸지 않는다 — "어떤 로케일 값을 기준으로 선택할지"만 시스템 전체 로케일에서 앱별 로케일로 바꾼다.
- `android:localeConfig` 매니페스트 선언은 시스템 설정 화면 노출 여부에 관한 것이지, `setApplicationLocales()` 자체의 동작 전제 조건은 아니다 — 선언 없이도 API 호출은 동작하지만 사용자가 시스템 설정에서 앱을 찾지 못한다.

### 관찰 가능한 신호

- `setApplicationLocales()` 호출 직후 현재 `Activity` 의 `onDestroy()`/`onCreate()` 가 다시 호출되는 것을 lifecycle 로그로 확인할 수 있다 — `Configuration` 변경으로 처리된다는 증거다.
- 시스템 설정의 App Languages 화면에서 앱을 선택해 언어를 바꾸면, 앱을 다시 열지 않고도 `getApplicationLocales()` 값이 갱신돼 있다.

관련 노트: [리소스 Qualifier는 런타임 로케일에 따라 문자열을 선택한다](./resource-qualifiers-select-strings-by-runtime-locale.md)

공식 문서: [앱 언어 지원](https://developer.android.com/guide/topics/resources/app-languages)

검증일: 2026-08-04. Android 13(API 33) 플랫폼 지원 시점, `LocaleManager`/`AppCompatDelegate.setApplicationLocales()` API, `android:localeConfig` 매니페스트 선언과 `AppLocalesMetadataHolderService` 자동 저장 패턴을 공식 문서에서 확인했다.
