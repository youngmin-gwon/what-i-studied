# Constructor injection은 기본 binding 경로다

DI graph에 타입을 넣는 기본 방법은 constructor injection이다. 생성자에 필요한 dependency가 드러나면 graph는 타입 간 연결을 정적으로 추적할 수 있고, 테스트에서도 생성자가 요구하는 협력 객체가 명확해진다.

`@Provides`나 factory가 먼저 떠오른다면 그 타입을 직접 소유하지 않는지, 런타임 값이 필요한지, interface binding이 빠진 것은 아닌지 확인한다. 소유한 일반 클래스는 constructor injection으로 시작하는 편이 가장 단순하다.

공식 문서: [Dependency injection in Android](https://developer.android.com/training/dependency-injection)
