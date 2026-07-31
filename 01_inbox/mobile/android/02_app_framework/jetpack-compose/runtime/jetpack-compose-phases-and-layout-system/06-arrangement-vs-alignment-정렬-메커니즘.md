# Arrangement vs Alignment (정렬 메커니즘)

`Row`나 `Column` 같은 표준 레이아웃에서는 자식들을 정렬하기 위해 주축(Main Axis)과 교차축(Cross Axis) 기준을 나누어 제어합니다.

```
[Row 레이아웃의 기준 축]
주축 (Main Axis - 가로): Arrangement로 제어 (SpaceBetween, Center 등)
┌──────────────────────────────────────────────┐
│  (자식 1)  ---- Arrangement ----  (자식 2)   │
└──────────────────────────────────────────────┘
교차축 (Cross Axis - 세로): Alignment로 제어 (CenterVertically, Top 등)
```

* **Arrangement (배치)**: **주축(Main Axis)** 기준 정렬로, 자식 노드들의 간격 분배와 고루 정렬하는 방식을 결정합니다. (`SpaceBetween`,
  `SpaceAround`, `Center`, `End` 등)
* **Alignment (정렬)**: **교차축(Cross Axis)** 기준 정렬로, 주축과 수직을 이루는 축 위에서 개별 자식들의 위치를 조율합니다. (
  `CenterVertically`, `Top`, `Bottom` / `CenterHorizontally`, `Start`, `End`)

---
