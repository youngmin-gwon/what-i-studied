# DI(의존성 주입)와 Navigation의 관계

### 1-1. 왜 Navigation과 DI가 연결되는가?

Navigation 3의 철학은 **"화면 이동은 곧 상태(State)의 변화일 뿐"**입니다. 화면이 바뀔 때, 그 화면에 필요한 ViewModel이나 Repository 객체도
함께 **생성·주입**되어야 하고, 화면이 꺼지면 메모리에서 같이 **사라져야(Scope)** 합니다.

이 작업을 내비게이션과 연동해 자동으로 관리해 주는 도구가 **DI 라이브러리**입니다.

### 1-2. DI 라이브러리 비교표

| 라이브러리             | 정체 및 특징                                                    | Flutter 매핑              | 왜 Navigation 3 예시에?                 |
|:------------------|:-----------------------------------------------------------|:------------------------|:------------------------------------|
| **Dagger / Hilt** | 구글 공식 안드로이드 전용 DI. 컴파일 타임 그래프 검증. 안드로이드 OS 의존성 강함          | `get_it` + `injectable` | 전통적인 안드로이드 전용 아키텍처 예시               |
| **Koin**          | 코틀린 순수 코드 기반 가볍고 실용적 DI. 런타임 주입                            | `Provider` / `get_it`   | **KMP(멀티플랫폼)** 지원 → 크로스 플랫폼 예시      |
| **Metro** ★       | Zac Sweers가 만든 최신 컴파일 타임 코틀린 DI. Kotlin Compiler Plugin 기반 | `riverpod` (컴파일 타임 안전성) | Navigation 3의 멀티플랫폼 목표에 부합하는 최첨단 DI |

### 1-3. 왜 DI 라이브러리가 이렇게 많은가?

각 라이브러리가 **풀고자 하는 도메인(문제)**이 다릅니다:

#### 안드로이드 전용 vs. 멀티플랫폼(KMP)

* **Hilt**: Activity/Fragment에 종속되어 iOS/Web 코드에서 사용 불가
* **Koin, Metro**: Pure Kotlin 기반이라 Android, iOS, Web에서 동일 DI 코드 공유 가능

#### 런타임 에러 vs. 컴파일 에러

* **Koin**: 앱 실행 중(런타임)에 객체 주입 → 오타 시 앱 실행 중 크래시. 대신 빌드 속도 빠름
* **Metro, Hilt**: 빌드(컴파일) 시점에 의존성 그래프 전수 검증 → 에러를 사전에 완벽 통제

### 1-4. Metro 상세

* **제작자**: Zac Sweers (안드로이드 오픈소스 대부. Block/Square, Cash App, OpenAI 등에서 채택)
* **구글 공식이 아닌 오픈소스** 프로젝트
* **이름 유래**: DI는 여러 모듈의 의존성들을 촘촘하게 연결하여 목적지까지 수송하는 '교통망'과 같다 하여 🚇 **Metro(지하철)**

#### Metro의 킬러 피쳐: Dynamic Feature Module 자동 수집

```kotlin
@ContributesTo(AppGraph::class) // 메인 앱 그래프에 의존성을 바치겠다는 선언
@BindingContainer
interface PaymentModule {
    @Provides
    fun providePaymentApi(): PaymentApi = PaymentApiImpl()
}
```

컴파일러가 각 모듈의 `@ContributesTo` 장부를 자동 수집하여 최상위 `AppGraph`에 코드를 자동으로 연결합니다.

---
