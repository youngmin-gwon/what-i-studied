# kotlinx serialization은 컴파일러 플러그인과 런타임 포맷을 함께 요구한다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [의존성, 버전, CI 계약](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/dependency-ci-contracts.md)
관련 노트: [KSP는 Kotlin-first 코드 생성이고 kapt는 유지보수 모드다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/ksp-is-kotlin-first-code-generation-and-kapt-is-maintenance-mode.md), [Version Catalog는 의존성 좌표와 플러그인 좌표의 이름표다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/version-catalog-names-dependency-and-plugin-coordinates.md)

## 역할

Serialization은 메모리 객체를 JSON 같은 표현으로 바꾸고, 그 표현을 다시 객체로 복원하는 기술이다.
`kotlinx.serialization`은 Kotlin compiler plugin과 런타임 라이브러리를 함께 사용하는 Kotlin 생태계 도구다.
Java의 `java.io.Serializable`, Android의 `Parcelable`와는 별개의 선택지다.

## 구성

`@Serializable`이 붙은 타입을 처리하려면 serialization plugin을 적용하고 필요한 format 라이브러리를 추가한다.
Plugin은 컴파일 시 serializer 구현을 준비하고, 런타임 라이브러리는 JSON 인코더·디코더와 API를 제공한다.

```kotlin
plugins {
    alias(libs.plugins.kotlin.serialization)
}

dependencies {
    implementation(libs.kotlinx.serialization.json)
}
```

Plugin 버전은 Kotlin plugin과 호환되는 공식 구성을 따르고, serialization 라이브러리 버전은 별도 좌표로 관리한다.
두 버전을 무조건 같은 문자열로 맞춘다는 규칙을 만들지 말고 릴리스 호환성을 확인한다.

## 모델 예시

```kotlin
@Serializable
data class RestaurantRoute(
    val id: Long,
    val name: String
)
```

직렬화 경계에서는 필드 추가·삭제, 기본값, nullability, 이름 변경을 명시적으로 설계한다.
외부 API 모델과 화면 상태 모델을 같은 타입으로 재사용할 때는 스키마 변경과 보안 영향을 함께 검토한다.

## Navigation과의 관계

타입 안전 Navigation 구성에서 `@Serializable` 모델이 route 인자 표현에 사용될 수 있다.
그렇다고 모든 Navigation 사용에 serialization이 자동으로 필요한 것은 아니다.
선택한 Navigation API와 프로젝트 버전에 맞는 공식 안내를 확인하고, route에 큰 객체나 비밀값을 넣지 않는다.
보통 route에는 식별자만 전달하고 실제 데이터는 저장소나 ViewModel에서 조회한다.

## 운영 점검

- JSON format 설정과 unknown key 정책을 테스트한다.
- 역직렬화 실패를 사용자 화면까지 예외로 흘려보내지 않는다.
- 외부 입력은 스키마와 크기·값 검증을 거친다.
- plugin 적용 모듈과 런타임 dependency를 분리해 확인한다.

자세한 시작점은 [Kotlin serialization 공식 안내](https://kotlinlang.org/docs/serialization-get-started.html)와
[Kotlin compiler plugins 개요](https://kotlinlang.org/docs/compiler-plugins-overview.html)다.
