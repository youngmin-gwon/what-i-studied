# DSL 문법은 ownership과 lifetime 계약을 바꾸지 않는다

Compose, Gradle Kotlin DSL, Koin DSL, Navigation DSL은 선언을 읽기 쉽게 만들지만 owner와 lifetime을 자동으로 올바르게 만들어 주지는 않는다. DSL 안에 쓰였다는 이유만으로 state, graph, route, build configuration의 책임이 사라지지 않는다.

DI/Navigation 관련 DSL을 볼 때는 문법보다 "무엇을 선언하는가", "누가 실행하는가", "언제 생성되고 언제 사라지는가", "어느 모듈이 이 이름을 알 수 있는가"를 먼저 본다.

관련 정본: [Navigation contracts](01_inbox/mobile/android/02_app_framework/navigation/navigation-contracts/navigation-contracts.md).
