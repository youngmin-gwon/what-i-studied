---
title: adaptive-layout-structure
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-07-31 18:06:11 +09:00
---

## 적응형 레이아웃은 같은 화면을 늘리는 것이 아니라 구조를 바꾼다

상위 문서: [큰 화면 적응 계약](./large-screen.md)

Adaptive layout 은 compact 화면을 큰 화면에 단순 확대하는 방식이 아니다. 창이 넓어지면 navigation chrome, content pane, 보조 도구, density, modal 위치 같은 화면 구조를 바꿔야 한다.

### 왜 중요한가

큰 화면에서 한 열 UI 를 가운데 늘려 놓으면 정보량은 늘지 않고 이동 거리만 증가한다. 반대로 너무 이른 two-pane 전환은 작은 height, 분할 화면, 폴더블 posture 에서 조작성을 해칠 수 있다.

### 메커니즘 및 카노니컬 레이아웃 구현 (`ListDetailPaneScaffold`)

```kotlin
@OptIn(ExperimentalMaterial3AdaptiveApi::class)
@Composable
fun AdaptiveListDetailScreen(
    navigator: ThreePaneScaffoldNavigator<Long> = rememberListDetailPaneScaffoldNavigator()
) {
    ListDetailPaneScaffold(
        directive = navigator.scaffoldDirective,
        value = navigator.scaffoldValue,
        listPane = {
            AnimatedPane {
                MyListPane(onItemClick = { itemId ->
                    navigator.navigateTo(ListDetailPaneScaffoldRole.Detail, itemId)
                })
            }
        },
        detailPane = {
            AnimatedPane {
                val currentId = navigator.currentDestination?.content
                MyDetailPane(itemId = currentId)
            }
        }
    )
}
```

### 실무 규칙

- list-detail, supporting pane, feed 같은 canonical layout 을 먼저 검토한다.
- compact 에서는 한 번에 하나의 주요 작업에 집중시키고, expanded 이상에서는 관련 정보를 함께 보여준다.
- button, dialog, text field 는 전체 폭을 무조건 채우지 말고 기능적으로 적절한 최대 폭을 둔다.
- orientation lock 이나 aspect ratio 제한으로 레이아웃 문제를 숨기지 않는다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 적응형 레이아웃 구성 변환 시 창 계층 및 bounds 모니터링
adb shell dumpsys window windows | grep -E "Window #|mFrame|mRequestedWidth"

# 에뮬레이터에서 회전 및 크기 조절으로 스캐폴드 전환 검증
adb shell content insert --uri content://settings/system --bind name:s:user_rotation --bind value:i:1
```

### 관련 문서

- [창 크기 클래스는 기기 종류가 아니라 앱 창을 분류한다](window-size-class-classification.md)
- [큰 화면 내비게이션은 목적지 중요도와 창 폭에 따라 chrome을 바꾼다](large-screen-navigation-chrome.md)

공식 문서: [Get started with adaptive apps](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps), [Adaptive do's and don'ts](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts)

