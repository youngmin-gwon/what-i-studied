---
title: compose-layout-and-image-cost-must-be-budgeted
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Compose layout 과 image 비용은 프레임 예산 안에서 관리한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](../../../../06_testing_performance/performance/android-performance-quality-and-build-optimization.md)

관련 지도: [Compose 성능 계약](./compose-performance-contracts.md)

관련 노트: [렌더링 성능은 프레임 지연의 원인을 분리한다](../../../../06_testing_performance/performance/performance-contracts/rendering-jank-is-frame-deadline-failure.md)

Compose UI 도 layout, measure, draw, image loading 비용을 가진다.

`BoxWithConstraints` 처럼 유용한 layout 도구도 남용하면 하위 tree 의 재측정 비용을 키울 수 있다.

비동기 이미지는 표시 크기와 디코딩 크기를 맞추고, placeholder 와 error 상태를 안정적으로 제공해야 한다.

큰 이미지, 반복되는 clipping, shadow, alpha 합성은 GPU 비용을 늘릴 수 있다.

Lazy list 에서는 key 와 contentType 을 적절히 제공해 item 재사용과 상태 보존을 돕는다.

Developer Options 의 "Profile GPU Rendering"(On screen as bars)을 켜면 frame 별 measure/layout/draw 단계 시간이 16.67ms 기준선과 함께 막대 그래프로 표시된다. 특정 화면 진입이나 스크롤 중 막대가 기준선을 넘는지로 layout/image 비용 문제를 좁힐 수 있다.

layout 변경은 접근성과 화면 구조를 깨지 않는 범위에서 수행한다.

공식 참고: [Compose lazy layout 성능](https://developer.android.com/develop/ui/compose/lists#performance)
