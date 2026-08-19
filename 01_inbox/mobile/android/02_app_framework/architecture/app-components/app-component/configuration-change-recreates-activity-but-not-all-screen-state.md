---
title: configuration-change-recreates-activity-but-not-all-screen-state
tags: [android, android/app-components, android/architecture]
aliases: ["Configuration change는 Activity를 재생성하지만 모든 화면 상태를 잃지 않는다"]
date modified: 2026-08-06 15:03:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Configuration change는 기본적으로 Activity instance를 바꾸되 process를 죽이지 않는다

회전, locale, font scale, window 크기, night mode 같은 configuration이 바뀌면 기본 처리에서는 현재 Activity를 destroy하고 새 resource configuration으로 다시 만든다. process와 task는 대개 유지된다. `android:configChanges`로 재생성을 막는 것은 앱이 resource·layout 갱신 책임을 직접 맡는 예외 선택이지 일반 상태 보존 해법이 아니다.

### 상태별 소유권

| 상태 위치 | configuration change | process death |
| --- | --- | --- |
| Activity field / Compose `remember` | 새 instance에서 소실 | 소실 |
| [viewmodel](../../../viewmodel.md) | 같은 `ViewModelStore` 경계를 통해 유지 | 소실 |
| `rememberSaveable` / `SavedStateHandle`의 저장 가능 값 | 복원 | saved snapshot에서 복원 가능 |
| Room/DataStore/file | 유지 | 유지 |

ViewModel이 configuration change 동안 유지된다는 것은 그 안의 모든 데이터가 영구 보존된다는 뜻이 아니다. 새 Activity가 같은 retained ViewModel을 다시 얻는 것이며, Activity/View reference를 ViewModel에 저장하면 이전 화면을 leak시킨다.

### 최소 구현과 재현

```kotlin
@Composable
fun SearchScreen(viewModel: SearchViewModel = viewModel()) {
    var expanded by rememberSaveable { mutableStateOf(false) }
    val results by viewModel.results.collectAsStateWithLifecycle()
    // expanded는 saved UI state, results는 screen state owner가 관리한다.
}
```

```kotlin
@Test
fun recreation_restores_screen_contract() {
    ActivityScenario.launch(MainActivity::class.java).use { scenario ->
        // 상태 입력
        scenario.recreate()
        // 새 Activity instance와 복원된 UI를 검증
    }
}
```

### 실패·관찰 신호

- `onCreate()`/`onDestroy()`에 Activity identity와 PID를 기록한다. identity만 바뀌고 PID가 같으면 configuration recreation 신호다.
- `ActivityScenario.recreate()`는 process death 테스트가 아니므로 SavedStateHandle 복구를 이것 하나로 증명하지 않는다.
- 회전 뒤 network 요청이 중복되면 Activity callback이 business 작업을 소유하는지, ViewModel init이 idempotent한지 확인한다.
- 이전 Activity가 LeakCanary에 남으면 retained ViewModel·singleton·callback이 View/Context를 잡는지 조사한다.

관련 노트: [ViewModel 수명과 프로세스 데스 계약](../../state-management/viewmodel/viewmodel-survives-configuration-change-not-process-death.md)

상위 문서: [App Component Contracts](./app-component.md)

공식 문서: [Handle configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes), [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states)
