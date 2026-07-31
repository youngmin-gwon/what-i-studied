# NavDisplay 기본형

상위 노트: [[jetpack-navigation-3-guide]]

앱에서 가장 흔한 `NavDisplay` 구성은 back stack, back 처리, entry decorators, entry provider를 함께 선언하는 형태입니다.

```kotlin
NavDisplay(
    backStack = backStack,
    onBack = { backStack.removeLastOrNull() },
    entryDecorators = listOf(
        rememberSaveableStateHolderNavEntryDecorator(),
        rememberViewModelStoreNavEntryDecorator(),
    ),
    entryProvider = appEntryProvider(backStack),
)
```

`entryDecorators` 기준:

- `rememberSaveableStateHolderNavEntryDecorator()`는 `rememberSaveable` 상태를 entry별로 보존합니다.
- `rememberViewModelStoreNavEntryDecorator()`는 entry별 `ViewModelStoreOwner`를 제공합니다.
- custom decorator는 logging, tracing, shared dependency scope처럼 모든 entry에 공통 적용할 일이 있을 때만 추가합니다.
- saveable state decorator는 특별한 이유가 없으면 첫 번째에 둡니다.

---
