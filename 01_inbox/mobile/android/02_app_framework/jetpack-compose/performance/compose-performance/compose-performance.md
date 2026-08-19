---
title: compose-performance
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-05 13:58:23 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Compose 성능 계약

이 지도는 Compose 성능을 API 팁 목록이 아니라 [recomposition](../../runtime/recomposition.md), stability, composition work, layout/image 비용의 판단 단위로 나눈다.

### 정본 노트
- [Compose 성능 최적화는 measure, debug, improve 순환으로 진행한다](./compose-performance-starts-with-measure-debug-improve-loop.md)
- [Compose 상태 읽기 위치는 recomposition 범위를 결정한다](./compose-state-read-location-controls-recomposition-scope.md)
- [**derivedStateOf**(고빈도 입력 상태 변경 중 최종 결과값이 뒤집힐 때만 Recomposition 스코프를 무효화하는 파생 상태 생성 API)는 고빈도 입력에서 저빈도 결과를 만들 때 쓴다](./derivedstateof-is-for-high-frequency-derived-values.md)
- [Compose 안정성과 strong skipping은 skippability에 영향을 준다](./compose-stability-and-strong-skipping-affect-skippability.md)
- [무거운 작업은 composition 안에 두지 않는다](./heavy-work-does-not-belong-in-composition.md)
- [Compose layout과 image 비용은 프레임 예산 안에서 관리한다](./compose-layout-and-image-cost-must-be-budgeted.md)
