# 불안정(Unstable) 타입과 기존 문제점
* **Collection 타입 사용**: `List`, `Map`, `Set` 등 Standard Collection 인터페이스는 내부 원소가 언제든지 변할 수 있는 가변 객체(예: `ArrayList`)일 가능성이 있어, 기존 Compose 컴파일러(Kotlin 1.x)는 이를 `Unstable`로 분류했습니다.
* 이로 인해 `List`를 받는 컴포저블은 매번 Skip되지 않고 불필요하게 리컴포지션이 발생하는 문제가 있었습니다.
