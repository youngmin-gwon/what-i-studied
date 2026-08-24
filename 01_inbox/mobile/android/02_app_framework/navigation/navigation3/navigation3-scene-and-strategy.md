---
title: navigation3-scene-and-strategy
tags: [android, compose, navigation3, scene, scene-strategy, multi-pane, list-detail, adaptive, metadata]
aliases: [Navigation 3 Scene, SceneStrategy, Navigation3 Scenes, Multi-Pane Layout]
date modified: 2026-08-18 10:13:00 +09:00
date created: 2026-08-10 17:28:00 +09:00
---

# Navigation 3 Scene & SceneStrategy (Navigation 3 Content Layout & Multi-Pane Adaptive)

## 1. 개요 (Overview)

**Navigation 3 Scene & SceneStrategy** 는 `androidx.compose.material3.adaptive:adaptive-navigation3` 및 `androidx.navigation3:navigation3-ui` 라이브러리가 제공하는 레벨 API 로, **동일한 Navigation Backstack 상태를 유지하면서 화면 크기(Window Size)에 따라 화면 콘텐츠(Content Layout)를 Single-Pane (1개) 또는 Multi-Pane (List-Detail / Supporting Pane 등 2~3개)으로 동시 배치 렌더링하는 Content Adaptive 엔진**이다.

스마트폰(Compact)에서는 Backstack 상단의 Detail 화면만 1-Pane 으로 보여주고, 태블릿(Expanded)에서는 동일한 Backstack `[ListNavKey, DetailNavKey]` 에 대해 `rememberListDetailSceneStrategy()` 가 List Pane 과 Detail Pane 을 한 화면에 2-Pane 으로 동시 분할 렌더링한다.

---

### 초보자를 위한 쉽게 이해하는 비유

* **Navigation 3 Scene (스마트 분할 렌더링 무대 감독)**:
  - 무대 대기실(Backstack)에 [목록, 상세] 2개의 대본이 있을 때, 무대가 좁으면 상세 대본만 무대에 올리고(1-Pane), 무대가 넓어지면 2개의 대본을 좌우 반씩 나눠 한 무대에 동시에 올려 연기시키는(2-Pane) 무대 디렉팅 감독.

```mermaid
graph TD
    Backstack["Backstack [InboxKey, DetailAliceKey]"] --> NavDisplay["NavDisplay (Navigation 3)"]
    NavDisplay --> Strategy["SceneStrategy (rememberListDetailSceneStrategy)"]
    Strategy --> EntryMeta{"NavEntry metadata 역할 지정 (listPane vs detailPane)"}
    
    EntryMeta -->|"Compact (폰)"| SinglePane["SinglePaneScene (detailPane 지정 화면만 1-Pane 렌더링)" ]
    EntryMeta -->|"Expanded (태블릿)"| MultiPane["ListDetailScene (listPane + detailPane 2-Pane 동시 렌더링)" ]
```

---

## 2. 핵심 역할 및 실전 코드 예시

### 1) 주요 관심사
- **해결 문제**: 이동 상태(Backstack) 내 여러 destination 들의 화면 동시 배치 ("현재 이동 상태의 콘텐츠를 어떻게 배치할 것인가?")
- **관심사**: Single-Pane vs List-Detail Pane vs Extra/Supporting Pane
- **Outer Navigation Chrome 조작 여부**: ❌ 조작하지 않음 (Bottom Bar / Rail 조작은 [navigation-suite-scaffold](../adaptive/navigation-suite-scaffold.md) 의 역할)
- **Metadata 역할 지정 필수**: 각 `NavEntry` 마다 `ListDetailSceneStrategy.listPane()`, `detailPane()`, `extraPane()` 메타데이터를 등록해야 전략이 각 화면의 렌더링 Pane 위치를 식별할 수 있다.

### 2) 실전 코드 예시 (Navigation 3 `NavDisplay` + `rememberListDetailSceneStrategy` + `metadata`)

```kotlin
@Composable
fun AppNavDisplay(
    backStack: SnapshotStateList<NavKey>,
    onItemClick: (String) -> Unit
) {
    // 1. Navigation 3 Material3 Adaptive 전용 List-Detail SceneStrategy 생성
    val listDetailStrategy = rememberListDetailSceneStrategy<NavKey>()

    // 2. NavDisplay 에 backStack 과 sceneStrategy 및 metadata 가 설정된 entryProvider 주입
    NavDisplay(
        backStack = backStack,
        sceneStrategy = listDetailStrategy,
        entryProvider = entryProvider {
            // 주 목록 Pane 메타데이터 지정 (listPane)
            entry<NavKey.InboxList>(metadata = ListDetailSceneStrategy.listPane()) {
                InboxListScreen(onItemClick = onItemClick)
            }
            // 상세 Pane 메타데이터 지정 (detailPane)
            entry<NavKey.EmailDetail>(metadata = ListDetailSceneStrategy.detailPane()) { entry ->
                EmailDetailScreen(emailId = entry.key.emailId)
            }
            // 3차 보조 Pane 메타데이터 지정 (extraPane)
            entry<NavKey.UserInfo>(metadata = ListDetailSceneStrategy.extraPane()) {
                UserInfoExtraScreen()
            }
        }
    )
}
```

---

## 3. 연결 문서 (Related Links)

- [navigation-suite-scaffold](../adaptive/navigation-suite-scaffold.md) - Material3 Top-Level Chrome Adaptive
- [navigation-suite-scaffold-vs-navigation3-scene](../adaptive/navigation-suite-scaffold-vs-navigation3-scene.md) - 둘의 비교 및 통합 사용 아키텍처
- [jetpack-navigation-3-guide](jetpack-navigation-3-guide.md) - Jetpack Navigation 3 가이드
