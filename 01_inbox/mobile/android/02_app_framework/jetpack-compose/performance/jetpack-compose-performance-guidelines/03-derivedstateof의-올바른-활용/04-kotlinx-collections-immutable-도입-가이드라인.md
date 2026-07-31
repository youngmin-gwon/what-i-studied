# kotlinx-collections-immutable 도입 가이드라인
그럼에도 불고하고 `kotlinx-collections-immutable` (`PersistentList` 등)의 도입이 권장되는 상황은 다음과 같습니다:

1. **대용량 리스트의 `equals()` 비교 성능 최적화**
   * Strong Skipping이 동작할 때 리스트의 크기가 크면 `List.equals()` 비교 자체에 비용이 발생합니다.
   * `PersistentList`는 참조(Reference) 및 영구 구조(Persistent Data Structure) 기반 변경 추적이 가능하므로 `equals()` 비용을 최소화할 수 있습니다.
2. **도메인/State 모델의 엄격한 불변성 보장**
   * UI State(예: `UiState(items: PersistentList<Item>)`) 레벨에서 개발자의 실수로 인한 가변 객체 혼용을 언어/타입 차원에서 완전히 차단하고 싶을 때.
3. **컴파일러 수준 명시적 안정을 위한 어노테이션 활용**
   * 일반 Data Class의 경우 `@Immutable` 또는 `@Stable` 어노테이션을 사용하여 컴파일러에 불변 객체임을 명시할 수 있습니다.

```kotlin
// 🐳 컴파일러가 Stable로 판단하도록 보증
@Immutable
data class User(
    val id: String,
    val name: String
)
```
