# Kotlin 2.x (Strong Skipping Mode) 도입 이후 변화
* **Kotlin 2.0+ & Compose Compiler 2.0+**: **Strong Skipping Mode**가 기본 활성화되었습니다.
* 파라미터가 Unstable 타입(일반 `List` 포함)이라도, 전달된 인스턴스의 **동등성(`equals()`) 비교**를 거쳐 이전과 값이 같다고 판단되면 컴포저블 실행을 안전하게 생략(Skip)합니다.
* 따라서 단순한 Recomposition Skip만을 목적으로 모든 `List`를 `ImmutableList`로 교체할 필요는 없습니다.
