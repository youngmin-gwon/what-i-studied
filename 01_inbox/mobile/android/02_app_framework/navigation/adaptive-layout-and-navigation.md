# Adaptive Apps 공식 문서 총정리

> 대상 문서
> 사용자가 제공한 Android Developers adaptive apps 문서 전체를 주제별로 요약합니다. 이 문서는 프로젝트 적용 의견을 섞지 않고, 공식 문서들이 말하는 개념과 도구를 정리하는 용도입니다.

---

## 1. 큰 그림

Adaptive app은 phone, tablet, foldable, ChromeOS, desktop window, connected display, car, TV, XR 등 다양한 form factor에서 앱 window 상태에 맞게 UI 구조를 조정하는 앱입니다.

공식 문서의 핵심 관점은 다음입니다.

- 기기 종류보다 **앱 window 크기**를 기준으로 판단합니다.
- multi-window, split screen, freeform window, fold/unfold로 window 크기는 앱 실행 중에도 바뀔 수 있습니다.
- 좁은 화면에서는 한 번에 적은 콘텐츠를 보여주고, 넓은 화면에서는 navigation rail, drawer, list-detail, supporting pane 같은 구조로 더 많은 콘텐츠를 함께 보여줍니다.
- layout은 단순히 늘리거나 줄이는 것이 아니라, 필요한 경우 component 배치와 정보 밀도를 바꿉니다.

관련 문서:

- [Get started with adaptive apps](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps)
- [Support different display sizes](https://developer.android.com/develop/adaptive-apps/guides/support-different-display-sizes)
- [Adaptive do's and don'ts](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts)

---

## 2. Window와 Resizability

Adaptive layout의 기본 전제는 앱이 여러 window 크기에서 정상적으로 동작해야 한다는 것입니다.

공식 문서들이 반복해서 강조하는 내용:

- 특정 orientation에 고정하지 않습니다.
- 특정 aspect ratio에 강하게 의존하지 않습니다.
- resize 가능한 window를 정상 상태로 봅니다.
- multi-window mode에서 앱이 작아지거나 커지는 상황을 고려합니다.
- UI state는 configuration/window 변화에 견딜 수 있어야 합니다.

Android 16 / API 36 이상을 target하는 방향에서는 large screen에서 orientation, aspect ratio, resizability 제한에 기대는 설계가 점점 더 약해집니다. 따라서 처음부터 adaptive/resizable UI로 설계하는 편이 안전합니다.

관련 문서:

- [Support multi-window mode](https://developer.android.com/develop/adaptive-apps/guides/support-multi-window-mode)
- [App orientation, aspect ratio, and resizability](https://developer.android.com/develop/adaptive-apps/guides/app-orientation-aspect-ratio-resizability)

---

## 3. Sizing Strategy

### 3.1 Window Size Classes

`WindowSizeClass`는 window 크기를 몇 개의 breakpoint로 분류해 layout 결정을 단순화합니다.

공식 문서 기준 width class:

| Class | 기준 | 대표 상황 |
|:---|:---|:---|
| Compact | `< 600dp` | phone portrait |
| Medium | `600dp <= width < 840dp` | tablet portrait, unfolded foldable portrait |
| Expanded | `840dp <= width < 1200dp` | tablet landscape, unfolded foldable landscape |
| Large | `1200dp <= width < 1600dp` | large tablet |
| Extra large | `>= 1600dp` | desktop / large connected display |

height class도 별도로 존재합니다. 대부분의 일반 화면은 width가 더 중요하지만, landscape phone이나 tabletop posture처럼 height가 작아지는 상황에서는 height도 고려해야 합니다.

Compose에서는 `currentWindowAdaptiveInfo()`를 사용해 현재 adaptive 정보를 얻습니다.

```kotlin
val adaptiveInfo = currentWindowAdaptiveInfo(
    supportLargeAndXLargeWidth = true,
)
val windowSizeClass = adaptiveInfo.windowSizeClass
```

관련 문서:

- [Use window size classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes)

### 3.2 mediaQuery

`mediaQuery`는 Compose에서 현재 window 조건을 선언적으로 질의하는 sizing strategy입니다.

`WindowSizeClass`가 고수준 breakpoint 중심이라면, `mediaQuery`는 layout 내부에서 특정 조건에 맞춰 더 세밀한 분기를 만들 때 유용합니다.

관련 문서:

- [Query information for adaptive layouts with mediaQuery](https://developer.android.com/develop/adaptive-apps/guides/mediaquery)

---

## 4. Layout Containers

공식 adaptive guides는 layout container로 Flexbox와 Grid를 별도 주제로 다룹니다.

### 4.1 Flexbox

Flexbox는 남는 공간과 줄바꿈을 활용해 아이템을 유연하게 배치하는 container입니다.

주요 관심사:

- container 방향
- wrapping
- item grow/shrink
- alignment
- available space에 따른 item 재배치

관련 문서:

- [FlexBox](https://developer.android.com/develop/adaptive-apps/guides/flexbox)
- [FlexBox - Get started](https://developer.android.com/develop/adaptive-apps/guides/flexbox/get-started)
- [FlexBox - Container behavior](https://developer.android.com/develop/adaptive-apps/guides/flexbox/container-behavior)
- [FlexBox - Item behavior](https://developer.android.com/develop/adaptive-apps/guides/flexbox/item-behavior)

### 4.2 Grid

Grid는 화면을 열과 행으로 나누고, 아이템을 grid cell 단위로 배치하는 container입니다.

주요 관심사:

- column/row 구성
- item span
- spacing
- container size 변화에 따른 item 재배치
- 큰 화면에서 더 많은 콘텐츠를 구조적으로 보여주는 방식

관련 문서:

- [Grid](https://developer.android.com/develop/adaptive-apps/guides/grid)
- [Grid - Get started](https://developer.android.com/develop/adaptive-apps/guides/grid/get-started)
- [Grid - Container properties](https://developer.android.com/develop/adaptive-apps/guides/grid/container-properties)
- [Grid - Item properties](https://developer.android.com/develop/adaptive-apps/guides/grid/item-properties)

---

## 5. Canonical Layouts

Canonical layouts는 큰 화면과 다양한 form factor에서 자주 쓰이는 검증된 layout pattern입니다.

공식 문서가 다루는 주요 pattern:

- List-detail
- Supporting pane
- Feed

관련 문서:

- [Canonical layouts](https://developer.android.com/develop/adaptive-apps/guides/canonical-layouts)

### 5.1 List-detail

List-detail은 목록 pane과 상세 pane을 함께 다루는 pattern입니다.

공식 문서의 설명:

- 큰 화면에서는 list와 detail을 나란히 보여줄 수 있습니다.
- 작은 화면에서는 list 또는 detail 중 하나가 전체 화면을 차지합니다.
- Compose에서는 `NavigableListDetailPaneScaffold`를 사용해 list-detail pane navigation과 predictive back animation을 쉽게 구성할 수 있습니다.

관련 dependency 그룹:

```kotlin
implementation("androidx.compose.material3.adaptive:adaptive")
implementation("androidx.compose.material3.adaptive:adaptive-layout")
implementation("androidx.compose.material3.adaptive:adaptive-navigation")
```

관련 문서:

- [Build a list-detail layout](https://developer.android.com/develop/adaptive-apps/guides/list-detail)

### 5.2 Supporting pane

Supporting pane은 주 콘텐츠 옆에 보조 정보를 보여주는 pattern입니다.

공식 문서 기준:

- 주요 content pane과 supporting pane을 함께 배치합니다.
- 작은 화면에서는 pane 사이를 navigation합니다.
- Compose에서는 `NavigableSupportingPaneScaffold`를 사용할 수 있습니다.

관련 문서:

- [Build a supporting pane layout](https://developer.android.com/develop/adaptive-apps/guides/build-a-supporting-pane-layout)

---

## 6. Adaptive Navigation

Adaptive navigation은 window size와 posture에 따라 navigation UI를 바꾸는 것입니다.

공식 문서의 대표 API는 `NavigationSuiteScaffold`입니다.

기본 동작:

- compact width/height 또는 tabletop posture: navigation bar
- 그 외 큰 window: navigation rail
- 필요하면 expanded window에서 navigation drawer로 커스터마이즈 가능

사용 dependency:

```kotlin
implementation("androidx.compose.material3:material3-adaptive-navigation-suite")
```

공식 문서 예시는 enum 등으로 top-level destination을 정의하고, `NavigationSuiteScaffold`의 `navigationSuiteItems`에서 bar/rail/drawer item을 공통 선언하는 방식을 보여줍니다.

관련 문서:

- [Build adaptive navigation](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation)

---

## 7. Custom Layouts

공식 문서의 custom layout 영역은 특정 component나 canonical layout으로 충분하지 않을 때 Compose로 직접 adaptive layout을 만드는 방법을 다룹니다.

주요 내용:

- custom Compose layout 작성
- window information을 state처럼 하위 composable로 전달
- bubble support 같은 특수 UI 모드

관련 문서:

- [Support bubbles](https://developer.android.com/develop/adaptive-apps/guides/support-bubbles)
- [Custom layouts - Use Compose](https://developer.android.com/develop/adaptive-apps/guides/custom)

---

## 8. Foldables

Foldable 대응은 단순히 큰 화면 대응이 아니라 posture와 hinge/fold feature를 고려하는 것입니다.

공식 문서에서 다루는 주제:

- foldable device의 display mode 이해
- folding feature와 hinge를 고려한 layout
- tabletop mode, book mode 같은 posture
- tri-fold, landscape foldable 같은 새로운 form factor

관련 문서:

- [Learn about foldables](https://developer.android.com/develop/adaptive-apps/guides/foldables/learn-about-foldables)
- [Make your app fold aware](https://developer.android.com/develop/adaptive-apps/guides/foldables/make-your-app-fold-aware)
- [Support foldable display modes](https://developer.android.com/develop/adaptive-apps/guides/foldables/support-foldable-display-modes)
- [Support trifolds and landscape foldables](https://developer.android.com/develop/adaptive-apps/guides/foldables/trifolds-and-landscape-foldables)

---

## 9. Device-specific Guides

공식 문서는 Android adaptive apps를 여러 device category로 확장해서 설명합니다.

### 9.1 Desktop / Connected Displays

desktop windowing과 connected display에서는 window가 자유롭게 resize될 수 있고, 앱이 물리 display 하나에 고정되지 않습니다.

관련 문서:

- [Support connected displays](https://developer.android.com/develop/adaptive-apps/guides/support-connected-displays)
- [Support desktop windowing](https://developer.android.com/develop/adaptive-apps/guides/support-desktop-windowing)

### 9.2 ChromeOS

ChromeOS에서는 Android 앱이 desktop-like resizable window에서 실행될 수 있습니다.

관련 문서:

- [Build adaptive apps for ChromeOS](https://developer.android.com/develop/adaptive-apps/guides/chromeos/build-adaptive-apps-for-chromeos)

### 9.3 Camera

camera 앱은 foldable, tablet, desktop-like window에서 preview, control, capture UI 배치가 form factor에 따라 달라집니다.

관련 문서:

- [Camera form factors support](https://developer.android.com/develop/adaptive-apps/guides/camera-form-factors-support)

### 9.4 Cars, TV, XR

cars, TV, XR은 input 방식, viewing distance, safety, spatial layout 등 요구사항이 일반 phone/tablet과 다릅니다.

관련 문서:

- [Build adaptive apps for cars](https://developer.android.com/develop/adaptive-apps/guides/cars/build-adaptive-apps-for-cars)
- [Build adaptive apps for TV](https://developer.android.com/develop/adaptive-apps/guides/tv/build-adaptive-apps-for-tv)
- [Build adaptive apps for XR](https://developer.android.com/develop/adaptive-apps/guides/xr/build-adaptive-apps-for-xr)

---

## 10. Navigation 3 Scenes와 Adaptive Libraries

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

