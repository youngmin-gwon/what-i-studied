# Navigation 3 Scenes와 Adaptive Libraries

상위 노트: [[adaptive-layout-and-navigation]]

사용자가 제공한 adaptive docs 목록에는 포함되지 않았지만, 함께 검토한 Navigation 3 Scenes 문서 기준으로 관계를 정리합니다.

Navigation 3의 `Scene`은 하나 이상의 `NavEntry`를 렌더링하는 단위입니다. `SceneStrategy`는 현재 back stack에서 만들어진 entries를 보고 어떤 `Scene`을 만들지 결정합니다. 아무 strategy도 scene을 만들지 않으면 기본 single-pane behavior로 마지막 entry 하나를 표시합니다.

관계:

| 항목 | 역할 |
|:---|:---|
| `NavigationSuiteScaffold` | top-level navigation UI를 bar/rail/drawer로 adaptive하게 표시 |
| `NavigableListDetailPaneScaffold` | Material adaptive pane scaffold로 list-detail pane navigation 제공 |
| Navigation 3 `Scene` | `NavDisplay` 내부에서 여러 `NavEntry`를 한 visual scene으로 렌더링 |

따라서 `NavigationSuiteScaffold`와 Navigation 3 `Scene`은 같이 사용할 수 있습니다. 전자는 app frame의 navigation chrome이고, 후자는 `NavDisplay` 내부의 content rendering 전략입니다.

반면 `NavigableListDetailPaneScaffold`와 custom Navigation 3 `Scene`은 같은 list-detail 문제를 서로 다른 방식으로 해결할 수 있으므로, 같은 화면에서 둘을 중복 적용하기보다 요구사항에 맞춰 하나를 선택하는 편이 자연스럽습니다.

관련 문서:

- [Navigation 3 Scenes](https://developer.android.com/guide/navigation/navigation-3/scenes)
