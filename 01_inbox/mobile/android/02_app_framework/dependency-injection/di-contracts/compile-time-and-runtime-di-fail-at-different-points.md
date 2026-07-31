# Compile-time DI와 runtime DI는 실패 시점이 다르다

DI framework 비교의 핵심은 문법보다 graph 오류가 언제 드러나는가다. Hilt, Dagger, Metro 같은 compile-time DI는 누락 binding, cycle, 잘못된 graph wiring을 build 단계에서 더 많이 드러내려 한다.

Koin이나 `get_it`처럼 runtime resolution 성격이 강한 도구는 설정과 실험이 빠를 수 있지만, binding 오류가 실행 경로에서 드러날 수 있다. 작은 앱에서는 편의가 이길 수 있고, 큰 앱이나 multi-module graph에서는 검증 시점이 architecture 비용을 크게 바꾼다.

관련 노트: [Hilt](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/hilt-is-official-android-dagger-integration.md), [Metro](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/metro-is-compile-time-kotlin-di-not-get-it-style-global-locator.md), [Koin](01_inbox/mobile/android/02_app_framework/dependency-injection/di-contracts/koin-trades-compile-time-graph-generation-for-runtime-dsl-convenience.md).
