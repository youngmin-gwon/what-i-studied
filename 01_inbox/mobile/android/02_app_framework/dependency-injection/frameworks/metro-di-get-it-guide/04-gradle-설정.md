# Gradle 설정

상위 노트: [metro-di-get-it-guide](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide.md)

공식 문서 기준으로 Metro는 Gradle plugin을 적용하는 방식이 기본입니다.

```kotlin
plugins {
    kotlin("android")
    id("dev.zacsweers.metro")
}
```

Version Catalog를 쓰면 보통 이런 형태가 됩니다.

```toml
[versions]
metro = "1.3.0"

[plugins]
metro = { id = "dev.zacsweers.metro", version.ref = "metro" }
```

```kotlin
plugins {
    alias(libs.plugins.metro)
}
```

> [!NOTE]
> 위 버전은 문서를 작성할 때 Metro GitHub README에서 확인한 최신 예시입니다. 실제 프로젝트에서는 Kotlin, AGP, Gradle 버전과 맞는 Metro 버전을 다시 확인하세요.

여기서 중요한 점은 `libs.versions.toml`의 `[libraries]`가 아니라 `[plugins]`에 Metro를 추가해야 한다는 것입니다.

```toml
[libraries]
metro = { group = "dev.zacsweers", name = "metro", version.ref = "metro" }
```

이 선언은 Metro runtime artifact를 라이브러리 의존성처럼 추가하는 선언입니다. 하지만 Metro는 Kotlin compiler plugin이 있어야 `@DependencyGraph`, `@Inject`, `@Provides`를 보고 코드를 생성할 수 있습니다. 공식 설치 방식은 Gradle plugin 적용이고, 이 plugin이 runtime dependency 추가와 compiler plugin wiring을 함께 처리합니다.

따라서 일반적인 Android Gradle 프로젝트에서는 아래처럼 plugin alias를 만들고:

```toml
[plugins]
metro = { id = "dev.zacsweers.metro", version.ref = "metro" }
```

모듈의 `build.gradle.kts`에 적용합니다.

```kotlin
plugins {
    alias(libs.plugins.metro)
}
```

`implementation(libs.metro)`만 추가한 상태라면 annotation type은 보일 수 있지만, Metro가 그래프 구현 코드를 생성하지 못합니다.

---
