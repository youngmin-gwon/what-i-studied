# Metro는 get_it식 전역 locator가 아니라 compile-time Kotlin DI로 이해한다

Flutter `get_it` 경험자는 DI를 전역 registry에서 객체를 꺼내는 방식으로 떠올리기 쉽다. Metro는 Kotlin compiler plugin 기반의 compile-time DI이므로, 핵심은 어디서든 꺼내 쓰는 것이 아니라 graph가 생성자를 호출하고 binding을 검증하게 두는 것이다.

`@DependencyGraph`, `@Inject`, `@Provides`, scope annotation은 "등록 목록"이라기보다 graph construction contract다. Android 앱에서는 이 graph를 Application 또는 feature entry 같은 명확한 owner에 보관해야 한다.

참고 문서: [Metro](https://zacsweers.github.io/metro/latest/)
