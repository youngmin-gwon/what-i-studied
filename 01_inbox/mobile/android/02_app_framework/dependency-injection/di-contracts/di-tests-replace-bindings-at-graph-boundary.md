# DI 테스트는 내부 구현을 건드리지 않고 graph boundary에서 binding을 교체한다

DI가 테스트에 주는 이점은 production code 내부의 생성 코드를 바꾸지 않고 fake, test dispatcher, in-memory database, fake API를 graph boundary에서 바꿀 수 있다는 점이다.

테스트가 consumer 내부 필드를 직접 덮어쓰거나 singleton registry를 공유하면 순서 의존성과 누수가 생긴다. test graph, module replacement, factory injection처럼 명시적인 교체 지점을 둔다.
