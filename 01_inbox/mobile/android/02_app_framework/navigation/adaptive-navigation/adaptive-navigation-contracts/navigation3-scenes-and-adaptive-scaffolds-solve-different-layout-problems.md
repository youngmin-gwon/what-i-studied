# Scenes와 adaptive scaffolds는 같은 문제를 푸는가

상위 문서: [Adaptive Navigation 계약](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/adaptive-navigation-contracts.md)
관련 정본: [Metadata와 SceneStrategy는 표시 정책을 전달한다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/metadata-and-scene-strategy-carry-display-policy.md)


## 서로 다른 계층

Navigation 3 `Scene`은 `NavEntry` 하나 이상을 하나의 visual state로 배치하는 navigation layer의 개념이다.
`SceneStrategy`는 현재 back stack과 entry metadata를 보고 single-pane, dialog, list-detail 같은 scene을 만든다.
반면 adaptive scaffold는 Material Compose가 제공하는 pane 배치와 navigation interaction의 UI 구성 요소다.

`NavigationSuiteScaffold`는 앱 frame의 bar, rail, drawer를 다룬다.
`NavigableListDetailPaneScaffold`는 list와 detail pane의 배치, 전환, predictive back을 다룬다.
따라서 전자는 top-level chrome이고, 후자는 feature content layout이다.

```text
MainScaffold
  NavigationSuiteScaffold
    selected feature
      NavDisplay
        SceneStrategy 또는 adaptive pane scaffold
```

## 선택 기준

단순한 push/pop 화면이면 기본 single-pane `NavDisplay`로 시작한다.
dialog나 overlay destination이 필요하면 `DialogSceneStrategy`를 검토한다.
back stack의 여러 entry를 하나의 list-detail scene으로 조합하려면 Navigation 3 scene strategy를 검토한다.

feature가 Material adaptive scaffold의 표준 list-detail 동작과 잘 맞으면 `NavigableListDetailPaneScaffold`를 사용한다.
이 경우 scaffold가 pane navigation과 back animation을 소유하므로 같은 feature에 custom scene strategy를 중복 적용하지 않는다.

어떤 방식을 선택하든 window 폭이 바뀌어도 의미 있는 route stack은 유지되어야 한다.
좁은 window에서는 list와 detail이 순차적으로 보이고, 넓은 window에서는 동시에 보일 수 있지만 목적지 key의 의미는 바뀌지 않는다.

검증할 때는 같은 stack을 compact, medium, expanded window에서 각각 렌더링한다.
compact에서는 detail 진입 뒤 back이 list로 돌아오는지 확인한다.
expanded에서는 list와 detail을 함께 보여준 뒤 선택된 detail이 바뀌는지 확인한다.
resize 중에도 selected destination과 entry별 saveable state가 유지되는지 확인한다.

Scene strategy를 먼저 선택할 기준은 여러 entry가 같은 화면에 함께 보여야 하는가다.
Adaptive scaffold를 먼저 선택할 기준은 표준 pane layout과 Material navigation interaction을 그대로 활용할 수 있는가다.
둘 다 필요하다고 느껴지면 어느 계층이 back과 pane 상태를 소유하는지부터 정한다.

장치 종류보다 실제 window 크기와 posture를 기준으로 판단해야 한다.
resize와 multi-window는 정상 상태이므로 특정 phone/tablet 모델에 맞춘 고정 분기보다 adaptive 정보에 반응한다.

관련 기준은 [Navigation 3 Scenes](https://developer.android.com/guide/navigation/navigation-3/scenes)와 [Canonical layouts](https://developer.android.com/develop/adaptive-apps/guides/canonical-layouts)에서 확인할 수 있다.
