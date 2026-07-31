# Metro 선언이 왜 `[libraries]`만으로는 부족했나?

Metro는 단순한 런타임 라이브러리가 아니라 **Kotlin compiler plugin 기반 DI 프레임워크**입니다.

즉 Metro가 하려는 일은 아래입니다.

```text
@DependencyGraph, @Inject, @Provides를 컴파일 중에 분석
-> 의존성 그래프가 맞는지 검증
-> 필요한 생성/연결 코드를 컴파일러 단계에서 생성
```

그래서 아래 선언만 있으면 부족합니다.

```toml
[versions]
metro = "1.3.0"

[libraries]
metro = { group = "dev.zacsweers", name = "metro", version.ref = "metro" }
```

```kotlin
dependencies {
    implementation(libs.metro)
}
```

이 선언은 Metro를 일반 라이브러리처럼 classpath에 추가하는 모양입니다. 하지만 Metro의 핵심인 **컴파일러 플러그인 연결**이 빠져 있습니다.

Metro를 일반적으로 쓰려면 plugin 선언이 필요합니다.

```toml
[versions]
metro = "1.3.0"

[plugins]
metro = { id = "dev.zacsweers.metro", version.ref = "metro" }
```

그리고 Metro 그래프를 작성하는 모듈에 적용합니다.

```kotlin
plugins {
    alias(libs.plugins.metro)
}
```

이렇게 하면 Gradle이 Metro plugin을 빌드 과정에 적용하고, Metro가 Kotlin 컴파일러에 연결되어 DI 그래프 코드를 만들 수 있습니다.

현재 프로젝트의 `app/build.gradle.kts`처럼:

```kotlin
plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.compose)
    alias(libs.plugins.jetbrains.kotlin.serialization)
    alias(libs.plugins.metro)
}
```

이 형태가 맞습니다.

Metro를 처음 잘못 선언하기 쉬운 이유는 `@Inject`, `@DependencyGraph` 같은 annotation이 코드에서 보이기 때문에 라이브러리만 추가하면 될 것처럼
보이기 때문입니다. 하지만 annotation은 표식일 뿐이고, 그 표식을 읽어서 그래프 구현체를 만들어 주는 쪽은 빌드 시점의 compiler plugin입니다.

비슷한 예시가 Kotlin Serialization입니다.

```toml
[plugins]
jetbrains-kotlin-serialization = { id = "org.jetbrains.kotlin.plugin.serialization", version.ref = "kotlinSerialization" }

[libraries]
kotlinx-serialization-core = { module = "org.jetbrains.kotlinx:kotlinx-serialization-core", version.ref = "kotlinSerializationCore" }
```

```kotlin
plugins {
    alias(libs.plugins.jetbrains.kotlin.serialization)
}

dependencies {
    implementation(libs.kotlinx.serialization.core)
}
```

Serialization은 plugin이 `@Serializable`을 보고 serializer 코드를 만들고, library가 런타임에서 필요한 타입과 API를 제공합니다.
Metro도 같은 방향으로 이해하면 됩니다.
