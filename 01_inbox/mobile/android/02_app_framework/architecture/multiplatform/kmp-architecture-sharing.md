---
title: kmp-architecture-sharing
tags: [android, android/architecture, android/multiplatform]
aliases: ["Kotlin Multiplatform은 비즈니스 로직과 데이터 레이어를 공유하고 UI는 기본적으로 플랫폼별로 유지한다"]
date modified: 2026-08-06 14:50:00 +09:00
date created: 2026-08-05 10:00:00 +09:00
---

## Kotlin Multiplatform은 비즈니스 로직과 데이터 레이어를 공유하고 UI는 기본적으로 플랫폼별로 유지한다

**Kotlin Multiplatform(KMP)**의 기본 원칙은 공통 비즈니스 로직(도메인, 데이터 계층)을 공유하고 UI는 각 플랫폼의 네이티브(Android Jetpack Compose, iOS SwiftUI)로 작성하는 것이다. 하지만 팀의 요구사항에 따라 **Compose Multiplatform**을 사용하여 UI까지 공유하는 선택을 할 수도 있다. 두 가지 접근 방식의 차이를 인지해야 한다.

---

### 1. 개념 및 핵심 명제 (What)

- **공유 로직 + 플랫폼 UI (Native by Default)**:
  공통 비즈니스 규칙과 데이터 접근을 재사용하면서 Android와 iOS의 UI 코드·탐색·플랫폼 관례를 독립적으로 설계한다. 플랫폼 특화 UX가 중요하거나 기존 UI를 점진적으로 유지해야 할 때 유용하지만, UI 구현과 테스트는 중복될 수 있다.
- **공유 로직 + 공유 UI (Compose Multiplatform)**:
  Compose Multiplatform을 사용해 화면이나 컴포넌트, 경우에 따라 앱 UI 대부분을 공유한다. 일관성과 개발 속도를 높일 수 있지만 플랫폼별 동작, 접근성, 입력, 성능과 native interop을 대상 플랫폼에서 실제로 검증해야 한다.
- **단계적 공유**:
  한 계산 모듈이나 데이터 계층부터 시작해 효과가 확인된 경계만 넓힐 수 있다. KMP 자체가 특정 공유 비율이나 UI 전략을 요구하지 않는다.

---

### 2. 왜 비즈니스 로직 중심 공유인가? (Why)

1. **플랫폼 간 규칙 불일치 감소**: 동일한 계산·검증 코드를 공유하면 플랫폼별 복제 구현에서 생기는 차이를 줄일 수 있다. 다만 플랫폼 adapter와 배포 설정까지 같아지는 것은 아니므로 타깃별 테스트는 여전히 필요하다.
2. **제품 요구에 맞춘 UI 경계 선택**: 플랫폼 UI는 플랫폼 고유 구성 요소와 팀의 기존 자산을 직접 활용하기 쉽고, 공유 UI는 화면 구현 중복을 줄이기 쉽다. 어느 쪽도 품질을 자동으로 보장하지 않는다.

---

### 3. 내부 메커니즘 (How)

```mermaid
graph TD
    subgraph Shared Core ["commonMain (Shared Kotlin Module)"]
        UseCase["Domain UseCases"]
        Repo["Data Repositories"]
        Ktor["Ktor HTTP Client"]
        SQL["SQLDelight / Room KMP DB"]
    end

    subgraph Android App ["Android App Target"]
        ComposeUI["Jetpack Compose UI"]
        AndroidVM"Android [viewmodel / stateflow"]
    end

    subgraph iOS App ["iOS App Target"]
        SwiftUI["SwiftUI Views"]
        iOSObservable["ObservableObject / SKIE StateFlow"]
    end

    ComposeUI --> AndroidVM
    AndroidVM --> UseCase
    SwiftUI --> iOSObservable
    iOSObservable --> UseCase
    UseCase --> Repo
    Repo --> Ktor
    Repo --> SQL
```

---

### 4. 현대 표준 코드 예시 (KMP Shared Repository & Coroutine Flow)

```kotlin
// commonMain/kotlin/com/example/data/UserRepository.kt
class UserRepository(
    private val api: KtorUserApi,
    private val database: UserDatabase
) {
    fun observeUser(id: String): Flow<UserDomainModel> {
        return database.userQueries.selectById(id)
            .asFlow()
            .mapToOne()
            .map { sqlEntity -> sqlEntity.toDomainModel() }
    }
}
```

---

### 5. 관측 가능 증거 및 진단 (Observability)

- **타깃별 빌드와 UI 검증**:
  프로젝트에 실제로 등록된 Gradle 태스크로 Android 라이브러리와 Apple framework를 각각 빌드하고, Android·iOS 앱에서 공통 상태와 플랫폼 adapter가 연결되는지 확인한다. Compose Multiplatform UI를 공유한다면 각 대상의 접근성, 텍스트 입력, 스크롤·gesture, native view interop을 별도로 테스트한다. 태스크 이름은 프로젝트의 framework/binary 설정에 따라 달라지므로 `./gradlew tasks`에서 확인한다.

---

### 6. 관련 문서 및 참조

- 상위 문서: [Multiplatform Contracts](multiplatform.md)
- 관련 계약 문서:
  - [Android 앱 아키텍처 정본](../android-app-architecture.md)
  - [expect/actual은 컴파일 타임 계약이다](expect-actual-implementations.md)
- 공식 문서: [Kotlin Multiplatform Overview](https://kotlinlang.org/docs/multiplatform.html)

검증일: 2026-08-06. Kotlin 공식 KMP 시작 문서의 "share logic but keep UI native"와 "share both logic and UI"를 동등한 선택지로 반영하고 품질 보장 표현을 제거했다.
