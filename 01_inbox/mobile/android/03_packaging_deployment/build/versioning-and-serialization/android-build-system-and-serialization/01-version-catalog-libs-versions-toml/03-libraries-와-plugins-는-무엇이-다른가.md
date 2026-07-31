# `[libraries]`와 `[plugins]`는 무엇이 다른가?

`libs.versions.toml`에서 가장 헷갈리는 부분은 `[libraries]`와 `[plugins]`입니다.

둘 다 "외부에서 받아오는 것"처럼 보이지만, 역할이 다릅니다.

```toml
[libraries]
androidx-core-ktx = { group = "androidx.core", name = "core-ktx", version.ref = "coreKtx" }

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
```

핵심 차이:

| 구분          | `[libraries]`                                    | `[plugins]`                          |
|:------------|:-------------------------------------------------|:-------------------------------------|
| 무엇을 가리키나    | 앱/모듈 코드가 의존하는 Maven artifact                     | Gradle 빌드에 적용할 plugin                |
| 주소 형식       | `group + name + version` 또는 `module`             | `id + version`                       |
| 쓰는 위치       | `dependencies { implementation(...) }`           | `plugins { alias(...) }`             |
| 주된 역할       | 코드에서 import하거나 실행 시 필요한 라이브러리 제공                 | 빌드 과정 변경, task 추가, 컴파일러 설정, 코드 생성 연결 |
| 앱에 포함될 수 있나 | `implementation`이면 보통 APK/AAB 런타임 의존성으로 포함될 수 있음 | plugin 자체는 앱 런타임 코드가 아님              |

`[plugins]`에 `group`과 `name`을 쓰지 않고 `id`를 쓰는 이유는, Gradle plugin은 일반 라이브러리처럼 "이 Maven 좌표의 jar를 내 코드에서
쓰겠다"가 아니라 **"이 빌드 기능을 이 모듈에 적용하겠다"**는 선언이기 때문입니다.

예를 들어:

```toml
[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
kotlin-compose = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }
jetbrains-kotlin-serialization = { id = "org.jetbrains.kotlin.plugin.serialization", version.ref = "kotlinSerialization" }
metro = { id = "dev.zacsweers.metro", version.ref = "metro" }
```

이것들은 앱 코드에서 `import com.android.application...`처럼 쓰는 라이브러리가 아닙니다. Gradle이 빌드할 때 읽고, Android 빌드 기능을
켜거나, Compose/Serialization/Metro 같은 Kotlin compiler plugin을 컴파일 과정에 연결합니다.

반면 `[libraries]`는 이런 식으로 모듈 코드의 classpath에 들어갑니다.

```toml
[libraries]
kotlinx-serialization-core = { module = "org.jetbrains.kotlinx:kotlinx-serialization-core", version.ref = "kotlinSerializationCore" }
androidx-core-ktx = { group = "androidx.core", name = "core-ktx", version.ref = "coreKtx" }
```

```kotlin
dependencies {
    implementation(libs.kotlinx.serialization.core)
    implementation(libs.androidx.core.ktx)
}
```

여기서 `implementation`은 앱 코드가 컴파일될 때도 보고, 실행할 때도 필요할 수 있는 일반 의존성입니다.

> [!IMPORTANT]
> `[libraries]`가 항상 "runtime 전용"이라는 뜻은 아닙니다. `implementation`, `api`, `compileOnly`,
`testImplementation`, `ksp`, `kapt`처럼 어떤 Gradle configuration에 넣느냐에 따라 역할이 달라집니다.
>
> 다만 `[plugins]`는 앱 런타임 의존성이 아니라 **빌드 시스템을 바꾸는 도구**입니다.
