# Qualifier는 같은 타입의 서로 다른 의미를 구분한다

DI graph는 타입만으로 binding을 찾는 경우가 많다. 같은 `String`, `CoroutineDispatcher`, `OkHttpClient`, `Context`가 여러 의미로 존재하면 타입만으로는 어떤 값을 넣어야 하는지 알 수 없다.

Qualifier는 같은 타입의 값을 의미별로 분리하는 이름표다. `@ApplicationContext`와 `@ActivityContext`, `@IoDispatcher`와 `@MainDispatcher`처럼 lifetime이나 역할이 다른 값을 구분할 때 사용한다.

관련 정본: [Context boundaries](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context-boundaries.md).
