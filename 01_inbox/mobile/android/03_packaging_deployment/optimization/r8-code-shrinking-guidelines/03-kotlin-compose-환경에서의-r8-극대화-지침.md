# Kotlin & Compose 환경에서의 R8 극대화 지침

R8은 Kotlin 언어 특성(람다, 인라인 함수, Data Class)과 결합될 때 최적화 시너지가 매우 큽니다.

### 3-1. Reflection 기반 라이브러리 배제
* Gson, Java Reflection API 등 런타임에 클래스 필드 이름을 탐색하는 라이브러리는 R8이 해당 클래스의 이름을 난독화하거나 필드를 깎아내지 못하게 막습니다.
* **대안**: 컴파일 타임에 Serializer 코드를 자동 생성하는 **`kotlinx.serialization`**이나 **Metro / Hilt** (Compile-time DI)를 사용하면 R8이 불필요한 클래스를 제약 없이 수축(Shrink)시킬 수 있습니다.

### 3-2. Compose UI와 R8
* `@Composable` 함수는 컴파일 타임에 Compose Compiler 플러그인에 의해 바이트코드가 변환되며, R8은 미사용 컴포저블 함수 및 파라미터 람다 객체를 효과적으로 인라이닝하여 DEX 바이너리 크기를 단축시킵니다.

---
