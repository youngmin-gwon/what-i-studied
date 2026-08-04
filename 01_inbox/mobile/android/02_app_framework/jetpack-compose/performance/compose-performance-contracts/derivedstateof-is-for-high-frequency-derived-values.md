---
title: derivedstateof-is-for-high-frequency-derived-values
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## derivedStateOf 는 고빈도 입력에서 저빈도 결과를 만들 때 쓴다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](../../../../06_testing_performance/performance/android-performance-quality-and-build-optimization.md)

관련 지도: [Compose 성능 계약](./compose-performance-contracts.md)

관련 노트: [렌더링 성능은 프레임 지연의 원인을 분리한다](../../../../06_testing_performance/performance/performance-contracts/rendering-jank-is-frame-deadline-failure.md)

`derivedStateOf` 는 계산 결과를 캐시하는 일반 메모이제이션 도구가 아니다.

입력 상태는 자주 변하지만 UI 에 필요한 결과는 드물게 바뀔 때 효과가 있다.

예를 들어 스크롤 index 는 자주 변하지만 "맨 위로 이동 버튼을 보일지"는 특정 임계값을 넘을 때만 바뀐다.

이때 `derivedStateOf` 는 불필요한 recomposition 을 줄이는 경계가 될 수 있다. 예를 들어 `val showButton by remember { derivedStateOf { listState.firstVisibleItemIndex > 0 } }` 로 만들면 `firstVisibleItemIndex` 가 스크롤마다 바뀌어도 `showButton` 값이 실제로 true/false 로 뒤집힐 때만 그 값을 읽는 composable 이 recompose 된다.

반대로 단순 문자열 결합이나 값 복사는 `derivedStateOf` 자체의 비용만 추가한다.

결과가 거의 매번 바뀌는 계산에도 이점이 적다.

사용 전에는 입력 빈도, 결과 변경 빈도, downstream recomposition 비용을 함께 본다.

공식 참고: [derivedStateOf](https://developer.android.com/develop/ui/compose/side-effects#derivedstateof)
