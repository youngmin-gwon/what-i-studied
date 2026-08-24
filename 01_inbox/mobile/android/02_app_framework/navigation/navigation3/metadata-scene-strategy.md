---
title: metadata-scene-strategy
tags: [android, android/navigation, android/navigation3]
aliases: ["Metadata와 SceneStrategy는 표시 정책을 전달한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Metadata 와 SceneStrategy 는 표시 정책을 전달한다

상위 문서: [Navigation 3 계약](navigation3.md)

관련 계약: [SceneStrategy는 entry를 조합하고 decorator는 렌더링을 감싼다](scene-strategy-decorators.md)

---

### 개념과 필요성 (What & Why)

1. **개념 (What)**:
   - Navigation 3에서 **`NavEntry.metadata`**는 개별 목적지 키가 화면에 표시될 때 적용되어야 할 시각적 표시 정책(예: "이 엔트리는 Dialog로 띄울 것", "이 엔트리는 BottomSheet으로 띄울 것")을 담는 메타데이터 맵이다.
   - **`SceneStrategy`**는 현재 백스택 항목들과 각 엔트리의 `metadata`를 참조하여, 실제 화면에 렌더링될 visual state 인 `Scene` 목록을 최종 결정하는 엔진 규칙이다.
2. **필요성 (Why)**:
   - 목적지 라우트 키(`NavKey`) 자체에 "Dialog인가?", "Bottom Sheet인가?" 같은 시각적 UI 표현 상태를 직접 하드코딩하면, 동일한 라우트 키를 대화면에서는 일반 Pane으로 띄우고 스마트폰에서는 Dialog로 띄우는 반응형 분기가 불가능해진다. 라우트 키(Identity)와 표시 정책(Metadata/Strategy)을 분리해야 한다.

---

### 핵심 구현 예시

```kotlin
// 1. Dialog 메타데이터를 포함하는 NavEntry 정의
fun entryProvider() = entryProvider {
    entry<ProfileKey>(
        metadata = DialogSceneStrategy.dialog()
    ) { key ->
        ProfileDialogContent(id = key.id)
    }
}

// 2. SceneStrategy 적용
NavDisplay(
    backStack = backStack,
    entryProvider = entryProvider(),
    sceneStrategy = remember { DialogSceneStrategy() }
)
```

---

### 관련 상위 및 연관 노트

- 상위 계약: [Navigation 3 계약](navigation3.md)
- 연관 계약: [SceneStrategy는 entry를 조합하고 decorator는 렌더링을 감싼다](scene-strategy-decorators.md)
