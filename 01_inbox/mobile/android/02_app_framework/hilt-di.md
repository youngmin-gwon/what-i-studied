---
title: hilt-di
tags: [android, architecture, hilt, dagger, di, dependency-injection]
---

# Hilt DI (안드로이드 표준 의존성 주입 프레임워크)

## 1. 개념 & 비유 (Concept & Real-World Analogy)

### 개념
**Hilt**는 Dagger를 기반으로 구축된 Android 전용 컴파일 타임(Compile-time) 표준 의존성 주입(Dependency Injection, DI) 라이브러리입니다. Android 앱 생명주기(Application, Activity, Fragment, ViewModel 등)에 직접 연동되는 사전 정의된 컴포넌트(Component)와 스코프(Scope)를 제공함으로써, 순수 Dagger의 복잡한 보일러플레이트 코드 작성 부담을 대폭 감소시켜 줍니다.

### 실생활 비유: 자동화 제품 조립 공장 (Automated Assembly Factory)
수동 의존성 주입이나 순수 Dagger 구현이 일일이 모든 부품의 수량과 규격을 측정하고 손으로 조립 레시피를 작성하는 과정이라면, Hilt는 **자동화 스마트 공장 라인**입니다.
공장 로봇(`@HiltAndroidApp`, `@AndroidEntryPoint`)에게 "이 부품이 필요해(`@Inject`)"라고 라벨을 붙여두면, 공장 제어 시스템(`Hilt Component Graph`)이 컴파일 시점에 최적의 부품 조립도를 생성하여 제품(Activity, ViewModel)이 필요한 순간에 자동으로 완제품 의존성을 전달합니다.

---

## 2. 핵심 구성 요소 & 동작 원리 (Core Components & How It Works)

### 핵심 구성 요소
1. **`@HiltAndroidApp`**: Application 클래스에 부착하며, Hilt 컴파일러에게 앱 레벨의 의존성 그래프 루트 생성(SingletonComponent)을 지시합니다.
2. **`@AndroidEntryPoint`**: Activity, Fragment, View, Service 등에 부착하여 해당 안드로이드 라이프사이클에 맞춘 Hilt 의존성 주입 컨테이너를 활성화합니다.
3. **`@HiltViewModel`**: Jetpack ViewModel 생명주기와 통합되어 ViewModelComponent에서 필요한 인스턴스를 자동으로 주입받도록 설정합니다.
4. **`@Module` & `@InstallIn`**: 인터페이스나 외부 라이브러리 객체처럼 생성자를 직접 수정할 수 없는 의존성의 바인딩 규칙(`@Provides`, `@Binds`)을 특정 계층 스코프에 등록합니다.
5. **Standard Scopes**: `@Singleton` (Application), `@ActivityRetainedScoped` (ViewModel), `@ActivityScoped` (Activity) 등 생명주기와 1:1 대응하는 메모리 보존 범위를 제공합니다.

### 동작 흐름도 (Mermaid Diagram)

```mermaid
flowchart TD
    subgraph Hilt Dependency Graph
        APP_COMP[SingletonComponent / @Singleton]
        VM_COMP[ViewModelComponent / @ActivityRetainedScoped]
        ACT_COMP[ActivityComponent / @ActivityScoped]
    end

    subgraph Dependency Modules
        MOD[NetworkModule / @Module @InstallIn]
        BIND[UserRepositoryImpl / @Binds]
    end

    subgraph Entry Points
        APP[@HiltAndroidApp Application]
        VM[@HiltViewModel UserViewModel]
        ACT[@AndroidEntryPoint MainActivity]
    end

    APP_COMP -->|"Parent of"| VM_COMP
    VM_COMP -->|"Parent of"| ACT_COMP

    MOD -->|"Provides OkHttpClient / Retrofit"| APP_COMP
    BIND -->|"Binds UserRepository Interface"| VM_COMP

    APP -->|"Initializes Graph Root"| APP_COMP
    VM -->|"Injects Repository"| VM_COMP
    ACT -->|"Injects ViewModel / Analytics"| ACT_COMP
```

---

## 3. 코드 예제 & 사용 방법 (Code Example & Implementation)

### Step 1: Application 클래스 선언
```kotlin
import android.app.Application
import dagger.hilt.android.HiltAndroidApp

@HiltAndroidApp
class MainApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        // 앱 수준의 초기화 로직
    }
}
```

### Step 2: Module 정의 (외부 라이브러리 및 인터페이스 바인딩)
```kotlin
import dagger.Binds
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import javax.inject.Singleton

interface ApiService {
    fun fetchData(): String
}

class ApiServiceImpl : ApiService {
    override fun fetchData(): String = "Data from Remote Server"
}

@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {

    @Provides
    @Singleton
    fun provideApiService(): ApiService {
        return ApiServiceImpl()
    }
}
```

### Step 3: ViewModel 및 Activity 주입
```kotlin
import androidx.lifecycle.ViewModel
import dagger.hilt.android.lifecycle.HiltViewModel
import javax.inject.Inject
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import dagger.hilt.android.AndroidEntryPoint

@HiltViewModel
class MainViewModel @Inject constructor(
    private val apiService: ApiService
) : ViewModel() {
    fun getData(): String = apiService.fetchData()
}

@AndroidEntryPoint
class MainActivity : AppCompatActivity() {

    // Activity 인젝션 예시 (필드 주입)
    @Inject lateinit var apiServiceDirect: ApiService

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate()
        setContentView(R.layout.activity_main)
        
        // hiltViewModel() 또는 ViewModelProvider를 통해 ViewModel 사용
    }
}
```

---

## 4. 주의사항 & 팁 (Key Considerations & Best Practices)

1. **컴파일 타임 검증**: Hilt는 주입 그래프의 누락이나 순환 참조(Circular Dependency)를 빌드 시점에 즉시 감지하여 앱 런타임 Crash를 방지합니다.
2. **생명주기 스코프 분리 주의**: `@ActivityScoped` 객체를 `@Singleton` 객체 생성자에 주입하려고 하면 컴파일 에러가 발생합니다. 하위 스코프 객체는 상위 스코프 객체보다 생명주기가 짧기 때문입니다.
3. **인터페이스 바인딩 시 `@Binds` 활용**: 추상 클래스 모듈과 `@Binds`를 활용하면 생성 코드가 절감되어 `@Provides` 대비 컴파일 속도가 향상됩니다.
4. **Jetpack Navigation 및 Compose 통합**: Compose 화면에서는 `hiltViewModel()`을 사용 시 Navigation BackStackEntry 스코프에 맞는 ViewModel을 자동으로 안전하게 바인딩합니다.

---

## 5. 연관 개념 & 참고 링크 (Related Concepts & Relative Markdown Links)

- [Dagger DI Architecture](dagger-di.md) - Hilt의 근간이 되는 컴파일 타임 DI 엔진
- [Paging 3 Architecture](paging-3.md) - Hilt를 통한 PagingSource & Repository 주입
- [Push Notification & FCM](push-notification-and-fcm.md) - FirebaseMessagingService 내부의 Hilt 주입 처리
