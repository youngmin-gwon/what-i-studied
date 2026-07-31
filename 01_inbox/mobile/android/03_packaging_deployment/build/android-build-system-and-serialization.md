# 안드로이드 빌드 시스템 & 직렬화(Serialization) 가이드

이 문서는 안드로이드 프로젝트의 의존성 관리 시스템인 **Version Catalog(`libs.versions.toml`)**, 타입 안전한 내비게이션을 가능하게 하는 *
*`kotlinx.serialization`**, 그리고 **KAPT → KSP → 컴파일러 플러그인**으로 이어지는 안드로이드 빌드 파이프라인의 진화사를 다룹니다.

---

## 1. Version Catalog (`libs.versions.toml`)

### 1-1. 왜 생겨났나? (역사적 배경)

과거 멀티 모듈 프로젝트에서는 각 모듈마다 **똑같은 라이브러리 버전을 수동으로 적어줘야** 했습니다.

* ❌ **과거의 문제**: `app`, `core-network`, `feature-restaurant` 모듈마다
  `implementation("androidx.navigation:navigation-compose:2.8.5")`를 각각 기재. 버전 업그레이드 시 모든 모듈 수정 필요 →
  누락 시 버전 충돌로 앱 크래시.
* ⭕ **해결책 (Version Catalog)**: Gradle 7.0+ 공식 기능으로, **앱의 모든 라이브러리와 버전을 `libs.versions.toml` 한 곳에서만
  관리**하도록 표준화.

### 1-2. 파일 구조와 4대 섹션

```toml
[versions]
# 1. 버전을 상수로 정의하는 곳
androidxNavigation = "2.8.5"
kotlin = "2.0.20"

[libraries]
# 2. 실제 라이브러리 '그룹:이름:버전'을 매핑하는 곳
android-navigation-compose = { group = "androidx.navigation", name = "navigation-compose", version.ref = "androidxNavigation" }

[plugins]
# 3. 그레이들 플러그인을 정의하는 곳
kotlin-serialization = { id = "org.jetbrains.kotlin.plugin.serialization", version.ref = "kotlin" }

[bundles]
# 4. 자주 함께 쓰는 라이브러리들을 세트로 묶는 곳
navigation-set = ["android-navigation-compose", "다른-내비-라이브러리"]
```

| 섹션            | 역할                                         |
|:--------------|:-------------------------------------------|
| `[versions]`  | 버전 숫자만 상수로 관리                              |
| `[libraries]` | 의존성 주소 정보. `version.ref`로 `[versions]`를 참조 |
| `[plugins]`   | 그레이들 플러그인 정의                               |
| `[bundles]`   | 자주 함께 쓰는 라이브러리 묶음                          |

### 1-3. `[libraries]`와 `[plugins]`는 무엇이 다른가?

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

### 1-4. Metro 선언이 왜 `[libraries]`만으로는 부족했나?

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

### 1-5. `build.gradle.kts`에서 `libs.~`로 바뀌는 이유

TOML 파일에는 `android-navigation-compose`라고 적지만, `build.gradle.kts`에서는
`libs.android.navigation.compose`로 씁니다.

#### 변환 규칙: 하이픈(`-`)이나 언더바(`_`)는 마침표(`.`)로 바뀐다

```
[TOML 파일]  android - navigation - compose
                ⬇          ⬇          ⬇
[KTS 파일]   libs . android . navigation . compose
```

**이유**: `build.gradle.kts`는 **코틀린 코드**입니다. 코틀린 변수명에 하이픈(`-`)을 쓰면 뺄셈 연산자로 인식하므로, 마침표(`.`)로 변환하여 코틀린
객체 계층 구조로 만들어 줍니다.

### 1-6. 내부 동작 원리 (타입 안정성과 코드 생성)

> `libs`라는 객체는 어디서 튀어나온 건가?

1. **TOML 파일 파싱**: Gradle이 빌드 사전 단계에서 `libs.versions.toml` 파일을 읽음
2. **클래스 자동 생성**: 빌드 캐시 디렉토리에 `LibrariesForLibs`라는 코틀린 클래스를 자동 빌드(Code Generation)
3. **타입 안정성 제공**: IDE에서 `libs.`을 치면 자동 완성이 뜨는 이유. 오타가 나면 컴파일 에러로 즉시 감지

> [!TIP]
> **Flutter 개발자 시점**: `pubspec.yaml`에 버전을 적을 때 오타가 나도 빌드 전까지 모르지만, 안드로이드의 이 방식은 **오타가 나면 실시간으로 IDE가
에러를 잡아주는 구조**입니다.
>
> **iOS 개발자 시점**: SPM이나 CocoaPods의 버전 선언을 `enum`/`struct` 상수 구조체로 정의해 타겟들이 안전하게 꺼내 쓰는 아키텍처와 동일합니다.

---

## 2. Serialization (`kotlinx.serialization`)

### 2-1. 두 가지 Serializable의 정체

| 구분        | Java 표준 `Serializable`            | Kotlin `kotlinx.serialization` ★     |
|:----------|:----------------------------------|:-------------------------------------|
| **패키지**   | `java.io.Serializable`            | `kotlinx.serialization.Serializable` |
| **태생/소속** | Java 표준 (Android 아님)              | Kotlin 전용 확장 (Android 아님)            |
| **형태**    | 인터페이스 (`implements Serializable`) | 어노테이션 (`@Serializable`)              |
| **특징**    | 옛날 자바 시절부터 쓰던 방식 (느림)             | 코틀린 컴파일러가 직접 직렬화 코드를 생성 (매우 빠름)      |

> [!IMPORTANT]
> 둘 다 안드로이드 OS 자체 패키지가 아닙니다. 안드로이드 자체 직렬화 기술로는 `android.os.Parcelable`이 별도로 존재합니다.

### 2-2. 직렬화(Serialization)의 역할

* **직렬화**: 메모리에 살아있는 코틀린 객체를 **바이트 배열이나 JSON 문자열** 형태로 포장하는 행위
* **역직렬화**: 전달받은 텍스트/바이트를 다시 코틀린 객체로 조립해 내는 행위

### 2-3. 왜 Navigation에서 핵심으로 쓰이나?

최신 Navigation(2.8+/3)은 문자열 주소 대신 **코틀린 객체 자체를 라우트 주소로 사용(Type-Safe Navigation)**합니다.

```kotlin
// 라우트 주소를 담을 데이터 규격 정의
@Serializable
data class RestaurantDetail(val id: Int, val name: String)

// 화면 이동 (오타가 나면 컴파일 에러)
navController.navigate(RestaurantDetail(id = 3, name = "pawtato"))
```

Navigation 내부 시스템이 이 객체를 다른 화면으로 **안전하게 포장·전달(직렬화)**하기 위해, `@Serializable` 표식이 필수가 된 것입니다.

---

## 3. 빌드 파이프라인의 진화: KAPT → KSP → 컴파일러 플러그인

### 3-1. 1세대: KAPT (Java의 유산과 억지 합체)

* **정체**: Kotlin Annotation Processing Tool
* **배경**: 옛날 핵심 라이브러리들(Dagger2, Room 등)이 Java 어노테이션 프로세서 기반이었는데, 코틀린 코드를 읽을 수 없어서 만들어진 가교
* **작동 원리**: 코틀린 코드를 **가짜 자바 코드(Java Stubs)**로 먼저 변환한 뒤 라이브러리 실행
* **문제점**: Stub 생성 과정이 극도로 느림. KMP 미지원.

### 3-2. 2세대: KSP (Kotlin-First 소스 생성)

* **정체**: Kotlin Symbol Processing (구글 주도 개발)
* **개선점**: 가짜 자바 코드를 만들지 않고, 코틀린 소스코드를 직접 분석하여 새로운 `.kt` 파일을 생성
* **속도**: KAPT 대비 약 **2배** 빌드 속도 향상
* **한계점**: 여전히 "새 파일 만들기"만 가능. 기존 코드 수정이나 바이트코드 조작 불가.

### 3-3. 3세대: 컴파일러 플러그인 (FIR/IR의 시대) ★

대표: Jetpack Compose 컴파일러, Kotlin Serialization, **Metro DI**

* **정체**: 코틀린 컴파일러(`Kotlinc`) 내부에 직접 기생하는 확장 프로그램
* **작동 원리**: 텍스트 파일을 새로 쓰지 않음. 컴파일러 중간 단계인 FIR(구조 분석)과 IR(바이트코드 생성 직전)에 직접 주입되어 코드를 실시간으로 변조

#### 왜 업계가 컴파일러 플러그인으로 이동하는가?

| 이점                   | 설명                                                                                         |
|:---------------------|:-------------------------------------------------------------------------------------------|
| **비교 불가능한 빌드 속도**    | 파일 I/O가 없이 컴파일러 내부 메모리에서 처리. Dagger/KAPT → Metro 교체로 빌드 시간 50~80% 단축 (Cash App: 29초 → 12초) |
| **기존 코드 강제 개조**      | 기존 클래스에 새 생성자 주입, 일반 함수를 Compose 함수로 변형 등 가능                                               |
| **완벽한 타입 안정성 + KMP** | 컴파일 시점에 의존성 그래프 검증. Android, iOS Native, Web 가리지 않고 동작                                     |

### 3-4. 비유 총정리

| 세대            | 비유                                                                         |
|:--------------|:---------------------------------------------------------------------------|
| **KAPT**      | 미국인(Java 프로세서)에게 일 시키려고 한국어 서류(Kotlin)를 번역기 돌려 가짜 영어 서류(Stubs)로 만드느라 시간 소모 |
| **KSP**       | 한국어 할 줄 아는 비서(KSP)를 고용해서 새 서류를 빠르게 타이핑                                     |
| **컴파일러 플러그인** | 공장 컨베이어 벨트(Compiler Pipeline)에 흘러가는 제품 내부 부품을 실시간으로 튜닝                     |

> [!NOTE]
> 컴파일러 플러그인을 활용하는 대표적인 DI 라이브러리 **Metro**에 대한 상세
>
내용은 [[dependency-injection-dsl-dynamic-feature]]
> 를 참조하세요.
