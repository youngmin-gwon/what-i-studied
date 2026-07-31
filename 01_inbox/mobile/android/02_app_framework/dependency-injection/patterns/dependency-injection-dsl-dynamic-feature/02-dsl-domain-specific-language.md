# DSL (Domain-Specific Language)

### 2-1. DSL이란?

**"특정 영역(도메인)의 문제만 아주 쉽고 직관적으로 해결하기 위해 만든 미니 언어"**

* **External DSL**: HTML(웹 구조), SQL(데이터베이스 명령)
* **Internal DSL**: 코틀린 코드 안에서 마치 새로운 언어를 쓰는 것 같은 내장 DSL

### 2-2. DSL의 내부 동작 원리

코틀린 DSL이 작동하는 배후에는 **2가지 핵심 치트키**가 있습니다:

#### ① 수신 객체 지정 람다 (Lambda with Receiver)

```kotlin
// 일반적인 스타일 (지저분함)
fun buildUser(user: User) {
    user.name = "Youngmin"
    user.age = 31
}

// DSL 스타일 (수신 객체 지정 람다)
fun user(block: User.() -> Unit): User {
    val user = User()
    user.block()
    return user
}

// 사용하는 쪽: 마치 전용 미니 언어처럼 사용
val myUser = user {
    name = "Youngmin"  // this.name에서 this가 생략됨!
    age = 31
}
```

#### ② 스코프 제한자 (`@DslMarker`)

중첩 DSL에서 자식 블록이 부모의 엉뚱한 변수를 건드리지 못하도록 **컴파일러가 감시하는 제약 조건**.

### 2-3. DSL이 탄생한 언어적 근간

> 함수가 1급 객체(First-class citizen)이고, 마지막 인자인 람다를 소괄호 밖으로 꺼내서 중괄호 형태로 쓸 수 있는 **코틀린 언어의 특성**에서 나온 것.

여기에 **수신 객체 지정 람다**라는 치트키가 결합되어 중괄호 내부를 특정 클래스의 "안방"처럼 만들어 줍니다.

### 2-4. Swift와의 비교

| 기능         | Kotlin                       | Swift                                  |
|:-----------|:-----------------------------|:---------------------------------------|
| 함수의 지위     | 1급 객체                        | 1급 객체                                  |
| 소괄호 탈출 문법  | **Trailing Lambda**          | **Trailing Closure** (후행 클로저)          |
| DSL 치트키 엔진 | 수신 객체 지정 람다 (`T.() -> Unit`) | **Result Builders** (`@resultBuilder`) |

```kotlin
// Kotlin (Jetpack Compose DSL)
Row {
    Text("안녕 안드로이드")
}
```

```swift
// Swift (SwiftUI DSL)
HStack {
    Text("안녕 iOS")
}
```

> [!TIP]
> SwiftUI의 `VStack { }` 안에서 `return`도 없고 컴마도 없이 여러 `Text`를 나열할 수 있는 이유는, **`@ViewBuilder`라는 Result
Builder**가 컴파일 시 이를 자동으로 하나의 컴포넌트 묶음으로 변환해 주기 때문입니다.

### 2-5. 안드로이드/Jetpack Compose/KMP 진영의 대표 DSL들

#### Jetpack Compose UI DSL

```kotlin
LazyColumn {
    items(restaurantList) { restaurant ->
        RestaurantRow(restaurant)
    }
}
```

내부적으로 `LazyListScope.() -> Unit` 수신 객체 지정 사용.

#### Gradle KTS DSL

```kotlin
plugins {
    kotlin("android")
}
dependencies {
    implementation(libs.android.navigation.compose)
}
```

#### Ktor DSL (KMP 네트워크)

```kotlin
val client = HttpClient(CIO) {
    install(ContentNegotiation) {
        json(Json { prettyPrint = true })
    }
}
```

#### Koin DSL (의존성 주입)

```kotlin
val appModule = module {
    single { RestaurantRepository() }        // Singleton 등록
    factory { RestaurantViewModel(get()) }   // 매번 새로 생성
}
```

#### Navigation 3의 Entry Provider DSL

```kotlin
val entryProvider = { key ->
    when (key) {
        is HomeKey -> Entry(key) { HomeScreen() }
        is DetailKey -> Entry(key) { DetailScreen(id = key.id) }
        else -> null
    }
}
```

---
