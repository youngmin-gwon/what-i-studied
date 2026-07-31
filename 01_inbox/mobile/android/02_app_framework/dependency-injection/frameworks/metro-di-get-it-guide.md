# Metro DI 초보자 가이드 (`get_it` 경험자용)

이 문서는 Flutter에서 `get_it`을 써 본 개발자가 Android/Kotlin의 **Metro DI**를 처음 배울 때 필요한 개념과 사용 방법을 설명합니다.

Metro는 Kotlin Multiplatform을 지원하는 **컴파일 타임 의존성 주입(Dependency Injection) 프레임워크**입니다. Zac Sweers가 만든
오픈소스 라이브러리이며, Kotlin compiler plugin으로 동작합니다.

관련 공식 문서:

- [Metro GitHub README](https://github.com/ZacSweers/metro)
- [Metro Installation](https://zacsweers.github.io/metro/latest/installation/)
- [Metro Dependency Graphs](https://zacsweers.github.io/metro/latest/dependency-graphs/)
- [Metro Injection Types](https://zacsweers.github.io/metro/latest/injection-types/)
- [Metro Bindings](https://zacsweers.github.io/metro/latest/bindings/)
- [Metro Scopes](https://zacsweers.github.io/metro/latest/scopes/)

---

---

## 원자 노트

- [먼저 DI가 뭔가?](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide/01-%EB%A8%BC%EC%A0%80-di%EA%B0%80-%EB%AD%94%EA%B0%80.md)
- [get_it과 Metro의 가장 큰 차이](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide/02-get-it%EA%B3%BC-metro%EC%9D%98-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%B0%A8%EC%9D%B4.md)
- [Metro의 3대 기본 요소](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide/03-metro%EC%9D%98-3%EB%8C%80-%EA%B8%B0%EB%B3%B8-%EC%9A%94%EC%86%8C.md)
- [Gradle 설정](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide/04-gradle-%EC%84%A4%EC%A0%95.md)
- [`@Inject`: 생성자 주입](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide/05-inject-%EC%83%9D%EC%84%B1%EC%9E%90-%EC%A3%BC%EC%9E%85.md)
- [`@Provides`: 내가 직접 만드는 방법을 알려주는 함수](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide/06-provides-%EB%82%B4%EA%B0%80-%EC%A7%81%EC%A0%91-%EB%A7%8C%EB%93%9C%EB%8A%94-%EB%B0%A9%EB%B2%95%EC%9D%84-%EC%95%8C%EB%A0%A4%EC%A3%BC%EB%8A%94-%ED%95%A8%EC%88%98.md)
- [interface와 구현체 연결하기](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide/07-interface%EC%99%80-%EA%B5%AC%ED%98%84%EC%B2%B4-%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0.md)
- [런타임 값 넣기: Context, baseUrl, userId](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide/08-%EB%9F%B0%ED%83%80%EC%9E%84-%EA%B0%92-%EB%84%A3%EA%B8%B0-context-baseurl-userid.md)
- [Scope: singleton과 factory 감각](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide/09-scope-singleton%EA%B3%BC-factory-%EA%B0%90%EA%B0%81.md)
- [Android 앱에서 어디에 graph를 보관하나?](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide/10-android-%EC%95%B1%EC%97%90%EC%84%9C-%EC%96%B4%EB%94%94%EC%97%90-graph%EB%A5%BC-%EB%B3%B4%EA%B4%80%ED%95%98%EB%82%98.md)
- [Compose + ViewModel에서의 기본 흐름](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide/11-compose-viewmodel%EC%97%90%EC%84%9C%EC%9D%98-%EA%B8%B0%EB%B3%B8-%ED%9D%90%EB%A6%84.md)
- [멀티 모듈에서의 사고방식](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide/12-%EB%A9%80%ED%8B%B0-%EB%AA%A8%EB%93%88%EC%97%90%EC%84%9C%EC%9D%98-%EC%82%AC%EA%B3%A0%EB%B0%A9%EC%8B%9D.md)
- [get_it에서 Metro로 옮길 때의 매핑표](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide/13-get-it%EC%97%90%EC%84%9C-metro%EB%A1%9C-%EC%98%AE%EA%B8%B8-%EB%95%8C%EC%9D%98-%EB%A7%A4%ED%95%91%ED%91%9C.md)
- [자주 하는 실수](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide/14-%EC%9E%90%EC%A3%BC-%ED%95%98%EB%8A%94-%EC%8B%A4%EC%88%98.md)
- [최소 학습 순서](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide/15-%EC%B5%9C%EC%86%8C-%ED%95%99%EC%8A%B5-%EC%88%9C%EC%84%9C.md)
- [한 문장 요약](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide/16-%ED%95%9C-%EB%AC%B8%EC%9E%A5-%EC%9A%94%EC%95%BD.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
