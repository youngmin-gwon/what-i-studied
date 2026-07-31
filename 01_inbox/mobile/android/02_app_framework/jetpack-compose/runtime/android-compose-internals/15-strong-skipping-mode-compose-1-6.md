# Strong Skipping Mode (Compose 1.6+)

상위 노트: [[android-compose-internals]]

Compose 컴파일러가 더 공격적으로 재구성을 건너뛸 수 있도록 한다. **Kotlin 2.0+ 에서는 기본 활성화.**

**기존**: Unstable 파라미터를 가진 Composable 은 항상 재구성

**Strong Skipping**: Unstable 파라미터도 `equals()` 비교를 통해 **같으면 건너뜀**

```kotlin
// 기존: List<User> 는 Unstable → UserList 는 항상 재구성됨
// Strong Skipping: List<User> 도 equals() 비교 → 같은 리스트면 건너뜀
@Composable
fun UserList(users: List<User>) {
    LazyColumn {
        items(users) { user -> UserCard(user) }
    }
}
```

**실무 영향:**

- `@Stable`, `@Immutable` 어노테이션의 필요성이 줄어듦
- `kotlinx.collections.immutable` (`ImmutableList` 등) 없이도 성능 확보 가능
- 그래도 `data class` + `val` 조합은 여전히 권장 (의도 명확화)

>[!NOTE] **iOS 비교: SwiftUI 의 렌더링 최적화**
>SwiftUI 는 `@Observable` 매크로(iOS 17+)를 통해 **프로퍼티 수준 추적**을 자동화한다. Compose 의 Strong Skipping Mode 와 유사하게, 실제로 변경된 프로퍼티를 사용하는 뷰만 다시 그린다.
>차이점: SwiftUI 는 프레임워크가 자동으로 감지하는 반면, Compose 는 `equals()` 기반 비교에 의존한다.
>자세한 내용은 [[apple-observation-framework]] 참고.
