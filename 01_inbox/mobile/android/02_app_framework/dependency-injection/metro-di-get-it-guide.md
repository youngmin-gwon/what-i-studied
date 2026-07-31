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

- [[01-먼저-di가-뭔가|먼저 DI가 뭔가?]]
- [[02-get-it과-metro의-가장-큰-차이|get_it과 Metro의 가장 큰 차이]]
- [[03-metro의-3대-기본-요소|Metro의 3대 기본 요소]]
- [[04-gradle-설정|Gradle 설정]]
- [[05-inject-생성자-주입|`@Inject`: 생성자 주입]]
- [[06-provides-내가-직접-만드는-방법을-알려주는-함수|`@Provides`: 내가 직접 만드는 방법을 알려주는 함수]]
- [[07-interface와-구현체-연결하기|interface와 구현체 연결하기]]
- [[08-런타임-값-넣기-context-baseurl-userid|런타임 값 넣기: Context, baseUrl, userId]]
- [[09-scope-singleton과-factory-감각|Scope: singleton과 factory 감각]]
- [[10-android-앱에서-어디에-graph를-보관하나|Android 앱에서 어디에 graph를 보관하나?]]
- [[11-compose-viewmodel에서의-기본-흐름|Compose + ViewModel에서의 기본 흐름]]
- [[12-멀티-모듈에서의-사고방식|멀티 모듈에서의 사고방식]]
- [[13-get-it에서-metro로-옮길-때의-매핑표|get_it에서 Metro로 옮길 때의 매핑표]]
- [[14-자주-하는-실수|자주 하는 실수]]
- [[15-최소-학습-순서|최소 학습 순서]]
- [[16-한-문장-요약|한 문장 요약]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
