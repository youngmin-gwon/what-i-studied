---
title: navigation3-scenes-and-adaptive-scaffolds-solve-different-layout-problems
tags: []
aliases: []
date modified: 2026-07-31 18:22:34 +09:00
date created: 2026-07-31 17:13:53 +09:00
---

## Scenes 와 adaptive scaffolds 는 같은 문제를 푸는가

상위 문서: [Adaptive Navigation 계약](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/adaptive-navigation-contracts.md)

관련 정본: [Metadata와 SceneStrategy는 표시 정책을 전달한다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/metadata-and-scene-strategy-carry-display-policy.md)

### 서로 다른 계층

Navigation 3 `Scene` 은 `NavEntry` 하나 이상을 하나의 visual state 로 배치하는 navigation layer 의 개념이다.

`SceneStrategy` 는 현재 back stack 과 entry metadata 를 보고 single-pane, dialog, list-detail 같은 scene 을 만든다.

반면 adaptive scaffold 는 Material Compose 가 제공하는 pane 배치와 navigation interaction 의 UI 구성 요소다.

`NavigationSuiteScaffold` 는 앱 frame 의 bar, rail, drawer 를 다룬다.

`NavigableListDetailPaneScaffold` 는 list 와 detail pane 의 배치, 전환, predictive back 을 다룬다.

따라서 전자는 top-level chrome 이고, 후자는 feature content layout 이다.

```text
MainScaffold
  NavigationSuiteScaffold
    selected feature
      NavDisplay
        SceneStrategy 또는 adaptive pane scaffold
```

### 선택 기준

단순한 push/pop 화면이면 기본 single-pane `NavDisplay` 로 시작한다.

dialog 나 overlay destination 이 필요하면 `DialogSceneStrategy` 를 검토한다.

back stack 의 여러 entry 를 하나의 list-detail scene 으로 조합하려면 Navigation 3 scene strategy 를 검토한다.

feature 가 Material adaptive scaffold 의 표준 list-detail 동작과 잘 맞으면 `NavigableListDetailPaneScaffold` 를 사용한다.

이 경우 scaffold 가 pane navigation 과 back animation 을 소유하므로 같은 feature 에 custom scene strategy 를 중복 적용하지 않는다.

어떤 방식을 선택하든 window 폭이 바뀌어도 의미 있는 route stack 은 유지되어야 한다.

좁은 window 에서는 list 와 detail 이 순차적으로 보이고, 넓은 window 에서는 동시에 보일 수 있지만 목적지 key 의 의미는 바뀌지 않는다.

검증할 때는 같은 stack 을 compact, medium, expanded window 에서 각각 렌더링한다.

compact 에서는 detail 진입 뒤 back 이 list 로 돌아오는지 확인한다.

expanded 에서는 list 와 detail 을 함께 보여준 뒤 선택된 detail 이 바뀌는지 확인한다.

resize 중에도 selected destination 과 entry 별 saveable state 가 유지되는지 확인한다.

Scene strategy 를 먼저 선택할 기준은 여러 entry 가 같은 화면에 함께 보여야 하는가다.

Adaptive scaffold 를 먼저 선택할 기준은 표준 pane layout 과 Material navigation interaction 을 그대로 활용할 수 있는가다.

둘 다 필요하다고 느껴지면 어느 계층이 back 과 pane 상태를 소유하는지부터 정한다.

장치 종류보다 실제 window 크기와 posture 를 기준으로 판단해야 한다.

resize 와 multi-window 는 정상 상태이므로 특정 phone/tablet 모델에 맞춘 고정 분기보다 adaptive 정보에 반응한다.

관련 기준은 [Navigation 3 Scenes](https://developer.android.com/guide/navigation/navigation-3/scenes) 와 [Canonical layouts](https://developer.android.com/develop/adaptive-apps/guides/canonical-layouts) 에서 확인할 수 있다.
