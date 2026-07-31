# Koin은 런타임 DSL 편의와 정적 graph 검증의 트레이드오프를 가진다

Koin은 Kotlin DSL로 binding을 선언하고 런타임에 dependency를 resolve하는 방식에 가깝다. 설정이 가볍고 읽기 쉬운 장점이 있지만, Dagger/Hilt 같은 정적 graph generation과는 실패 시점과 검증 방식이 다르다.

따라서 Koin을 선택할 때는 간단한 setup만 보지 말고 startup cost, runtime resolution failure, module loading, test override, IDE/build integration까지 같이 판단한다.
