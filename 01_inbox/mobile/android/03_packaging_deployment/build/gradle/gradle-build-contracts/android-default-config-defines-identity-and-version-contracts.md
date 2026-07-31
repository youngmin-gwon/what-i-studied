# Android 기본 설정은 식별자와 버전 계약을 만든다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [Gradle 빌드 계약](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/gradle-build-contracts.md)
관련 정본: [R8와 Gradle 빌드 최적화 계약](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/build-optimization-contracts.md)

## `defaultConfig`의 역할

`defaultConfig`는 모든 변형이 상속하는 앱 기본값이다.
제품 flavor가 값을 재정의하면 해당 flavor 값이 기본값보다 우선한다.
빌드 type은 주로 패키징과 개발 단계 설정을 담당하므로 식별자 값과 섞어 설계하지 않는다.

## 핵심 속성

| 속성 | 의미 |
| --- | --- |
| `namespace` | 생성 코드와 소스에서 사용하는 Android 네임스페이스 |
| `applicationId` | 설치와 배포에서 앱을 식별하는 고유 ID |
| `minSdk` | 앱이 지원하는 최소 API 수준 |
| `targetSdk` | 앱이 대상으로 선언하고 호환성 동작을 받는 API 수준 |
| `compileSdk` | 컴파일 시 사용할 Android API 수준 |
| `versionCode` | 업그레이드 순서를 비교하는 정수 버전 |
| `versionName` | 사용자에게 표시하는 버전 문자열 |

## 네임스페이스와 applicationId

`namespace`를 바꾸는 것은 생성 코드의 패키지 경계를 바꾸는 일이다.
`applicationId`를 바꾸는 것은 설치 대상과 Play 앱 식별자를 바꾸는 일이다.
따라서 개발용 앱을 별도 설치하려면 flavor 또는 build type의 `applicationIdSuffix`를 검토한다.
소스 코드의 패키지와 manifest의 `package` 사용 방식은 applicationId와 동일하지 않을 수 있다.

```kotlin
android {
    namespace = "com.example.app"
    defaultConfig {
        applicationId = "com.example.app"
        versionCode = 42
        versionName = "2.3.0"
    }
    buildTypes {
        debug {
            applicationIdSuffix = ".debug"
            versionNameSuffix = "-debug"
        }
    }
}
```

## 버전 규칙

`versionCode`는 증가하는 정수여야 하며 배포 채널이 요구하는 범위도 확인해야 한다.
`versionName`은 표시 문자열이므로 의미 버전, 빌드 번호 등 팀의 릴리스 규칙을 반영한다.
flavor별 버전 차이가 필요하면 `versionNameSuffix`나 flavor의 버전 속성을 사용한다.

## 환경 분리 점검

- debug ID가 release ID와 충돌하지 않는가?
- 모든 배포 변형의 `applicationId`와 서명 키 조합이 의도한가?
- `minSdk`, `targetSdk`, `compileSdk`를 각각의 의미대로 선택했는가?
- 버전 코드는 이전 Play 업로드보다 큰가?

## 참고

앱 ID 설정: https://developer.android.com/build/configure-app-module
빌드 변형: https://developer.android.com/build/build-variants
