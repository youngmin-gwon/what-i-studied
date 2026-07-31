# Jetpack Compose Phases & Layout System (렌더링 파이프라인과 레이아웃) 개요

이 문서는 Jetpack Compose가 선언형 코드를 기반으로 화면에 픽셀을 그리기까지의 3단계 렌더링 파이프라인(Composition, Layout, Drawing), 이를
실질적으로 지원하는 3가지 트리 구조(Slot Table, LayoutNode, RenderNode), 그리고 상호작용하는 레이아웃 모델(Constraints & Size,
Modifier 순서)에 대해 상세히 다룹니다.

---
