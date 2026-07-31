---
title: 05-canonical-layouts
tags: []
aliases: []
date modified: 2026-07-31 18:22:43 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## Canonical Layouts

상위 노트: [adaptive-layout-and-navigation](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-layout-and-navigation.md)

Canonical layouts 는 큰 화면과 다양한 form factor 에서 자주 쓰이는 검증된 layout pattern 입니다.

공식 문서가 다루는 주요 pattern:

- List-detail
- Supporting pane
- Feed

관련 문서:

- [Canonical layouts](https://developer.android.com/develop/adaptive-apps/guides/canonical-layouts)

### 5.1 List-detail

List-detail 은 목록 pane 과 상세 pane 을 함께 다루는 pattern 입니다.

공식 문서의 설명:

- 큰 화면에서는 list 와 detail 을 나란히 보여줄 수 있습니다.
- 작은 화면에서는 list 또는 detail 중 하나가 전체 화면을 차지합니다.
- Compose 에서는 `NavigableListDetailPaneScaffold` 를 사용해 list-detail pane navigation 과 predictive back animation 을 쉽게 구성할 수 있습니다.

관련 dependency 그룹:

```kotlin
implementation("androidx.compose.material3.adaptive:adaptive")
implementation("androidx.compose.material3.adaptive:adaptive-layout")
implementation("androidx.compose.material3.adaptive:adaptive-navigation")
```

관련 문서:

- [Build a list-detail layout](https://developer.android.com/develop/adaptive-apps/guides/list-detail)

### 5.2 Supporting pane

Supporting pane 은 주 콘텐츠 옆에 보조 정보를 보여주는 pattern 입니다.

공식 문서 기준:

- 주요 content pane 과 supporting pane 을 함께 배치합니다.
- 작은 화면에서는 pane 사이를 navigation 합니다.
- Compose 에서는 `NavigableSupportingPaneScaffold` 를 사용할 수 있습니다.

관련 문서:

- [Build a supporting pane layout](https://developer.android.com/develop/adaptive-apps/guides/build-a-supporting-pane-layout)

---
