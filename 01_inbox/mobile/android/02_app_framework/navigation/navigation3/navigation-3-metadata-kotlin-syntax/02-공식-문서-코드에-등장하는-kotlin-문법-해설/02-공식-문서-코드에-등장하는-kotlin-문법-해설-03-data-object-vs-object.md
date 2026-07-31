# `data object` vs `object`
```kotlin
// Navigation3 Route 정의 시
@Serializable
data object Home : NavKey     // data object

// Metadata Key 정의 시
object TransitionKey : NavMetadataKey<...>  // 일반 object
```
| 구분 | `object` | `data object` |
| :--- | :--- | :--- |
| 인스턴스 개수 | 단 1개 (싱글톤) | 단 1개 (싱글톤) |
| `toString()` | `패키지명@해시코드` (기본값) | `"Home"` (클래스 이름을 자동 반환) |
| `equals` / `hashCode` | 참조 비교 (기본값) | 자동 생성됨 |
| 용도 | 내부 키, 전략 객체 등 | 직렬화가 필요하거나 로그에 이름이 찍혀야 할 때 |
