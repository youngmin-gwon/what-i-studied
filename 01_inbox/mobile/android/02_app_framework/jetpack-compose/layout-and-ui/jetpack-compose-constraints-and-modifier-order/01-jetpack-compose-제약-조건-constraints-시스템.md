# Jetpack Compose 제약 조건 (Constraints) 시스템

Compose 레이아웃 모델의 가장 핵심은 **제약 조건(Constraints)** 입니다. 부모 노드는 자식 노드에게 Constraints를 전달하며, 이 제약 조건은 아래 4개의 값으로 구성됩니다.

* **Min Width (최소 너비)** / **Max Width (최대 너비)**
* **Min Height (최소 높이)** / **Max Height (최대 높이)**

자식 노드는 반드시 이 최소값과 최대값 사이의 범위에서 최종 크기를 스스로 결정해야 합니다.

### 1-1. Constraints의 유형
* **Bounded Constraints (제한적 제약 조건)**: 최대 너비와 높이가 특정한 값(예: `1080px`, `1920px`)으로 지정되어 있는 형태입니다.
* **Unbounded Constraints (무제한 제약 조건)**: 최대 너비나 높이가 `Infinite(무한)`로 설정된 경우입니다. 스크롤이 가능한 `LazyColumn` 내부의 높이 제약이나, `Scrollable` 수정자가 적용된 경우가 이에 해당하며, 이 경우 자식은 자신의 컨텐츠 크기만큼 무제한으로 확장될 수 있습니다.

---
