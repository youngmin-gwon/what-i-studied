---
title: 04-개발-프레임워크-compose-for-xr
tags: []
aliases: []
date modified: 2026-07-31 17:59:10 +09:00
date created: 2026-07-31 16:26:40 +09:00
---

## 개발 프레임워크: Compose for XR

공간상의 3D 컴포넌트와 2D 레이아웃을 선언형으로 작성할 수 있다.

```kotlin
// Compose for XR 예시
@Composable
fun SpatialCard() {
    SpatialPanel(
        modifier = Modifier.size(400.dp, 300.dp),
        zDistance = 1.5.m // 공간상의 거리 설정
    ) {
        Content()
    }
}
```
