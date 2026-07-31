# Scene 도입 기준

Navigation 3 `Scene`은 처음부터 모든 route에 넣을 필요는 없습니다.

도입하지 않는 경우:

- placeholder 화면
- 단순 single screen flow
- 아직 list/detail route가 없는 feature

도입 검토 대상:

- `TrainingRoute` + `TrainingDetailRoute`
- `MeasureRoute` + `MeasureResultRoute`
- `TrainingRecordRoute` + `TrainingRecordDetailRoute`

`NavigationSuiteScaffold`와 Navigation 3 `Scene`은 같이 사용할 수 있습니다.

```text
MainScaffold
 └─ NavigationSuiteScaffold
     └─ selected tab NavDisplay
         └─ sceneStrategies = listOf(...)
```

다만 feature 내부 list-detail 화면은 `NavigableListDetailPaneScaffold`와 custom `SceneStrategy` 중 하나를 선택하는 편이 좋습니다.

---
