# R8 keep 규칙은 최적화 경계다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [R8와 Gradle 빌드 최적화 계약](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/build-optimization-contracts.md)
관련 노트: [R8은 릴리즈 코드의 수축, 최적화, 난독화를 수행한다](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/r8-shrinks-optimizes-and-obfuscates-release-builds.md), [R8 Full Mode와 Configuration Analyzer는 막힌 최적화를 드러낸다](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/r8-full-mode-and-configuration-analyzer-expose-blocked-optimization.md)

## 핵심 주장

keep 규칙은 R8을 끄는 스위치가 아니라 정적 분석이 알 수 없는 계약을 설명하는 선언이다.

패키지 전체를 보존하면 안전해 보이지만 수축, 최적화, 난독화의 이점을 넓게 잃는다.

규칙은 동적 접근의 실제 단위에 맞춰 클래스, 생성자, 필드, 메서드로 좁혀야 한다.

## 먼저 찾아야 할 경계

- 클래스 이름을 문자열로 읽는 리플렉션
- JSON/XML 직렬화가 필드 또는 생성자 이름에 의존하는 코드
- `ServiceLoader`나 동적 클래스 로딩
- JNI에서 이름으로 Java/Kotlin 멤버를 찾는 호출
- 프레임워크가 애노테이션을 스캔하는 진입점
- `getIdentifier()`로 리소스 이름을 조합하는 코드

정적 호출 그래프에 나타나지 않는 경계만 keep의 후보로 삼는다.

## 규칙을 좁히는 순서

1. 문제가 발생하는 실제 클래스 또는 멤버를 재현한다.
2. `usage.txt`에서 제거되었는지 확인한다.
3. 클래스 전체가 필요한지 멤버만 필요한지 구분한다.
4. 이름 보존만 필요한지, 구현 보존까지 필요한지 구분한다.
5. 보정 후 릴리즈 테스트를 다시 실행한다.

예를 들어 직렬화 라이브러리가 생성자만 찾는다면 패키지 전체보다 생성자 규칙이 적합하다.

```proguard
-keepclassmembers,allowoptimization class com.example.api.User {
    <fields>;
}
```

난독화된 이름을 외부 계약이 직접 참조하면 이름 보존이 필요하다.

반대로 내부 구현까지 보존하면 최적화 기회를 불필요하게 막을 수 있다.

## 라이브러리 규칙의 위치

재사용 라이브러리는 소비 앱이 알아야 할 최소 계약을 `consumer-rules.pro`에 둔다.

앱 모듈의 규칙 파일에 모든 라이브러리 예외를 복사하면 소유권과 변경 이유가 흐려진다.

라이브러리 규칙은 공개 API가 아니라 런타임 검색 방식에 대한 계약이어야 한다.

## 금지할 패턴

```proguard
-keep class com.example.** { *; }
```

이 규칙은 오류를 숨기는 대신 미사용 코드와 최적화 대상까지 보존한다.

규칙을 추가할 때는 대상, 동적 접근 이유, 제거 시 실패 증상, 검증 테스트를 함께 기록한다.

참고: [Android 앱 최적화 활성화](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization)

참고: [Keep rules and why they matter](https://developer.android.com/topic/performance/app-optimization/keep-rules)
