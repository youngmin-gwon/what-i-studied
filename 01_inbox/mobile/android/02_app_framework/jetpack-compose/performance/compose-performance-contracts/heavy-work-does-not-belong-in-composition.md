---
title: heavy-work-does-not-belong-in-composition
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 18:10:46 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## 무거운 작업은 composition 안에 두지 않는다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)

관련 지도: [Compose 성능 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/compose-performance-contracts.md)

관련 노트: [렌더링 성능은 프레임 지연의 원인을 분리한다](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/rendering-jank-is-frame-deadline-failure.md)

Composable 은 자주 다시 실행될 수 있는 함수다.

따라서 파일 읽기, 네트워크 요청, 큰 정렬, 이미지 디코딩, 복잡한 파싱을 composition 중에 수행하면 프레임 지연이 생긴다.

`remember` 는 값 보존 도구이지 무거운 일을 UI 스레드에서 실행해도 된다는 허가가 아니다.

입력이 바뀔 때만 필요한 계산은 ViewModel, repository, background dispatcher, 또는 명확한 캐시 경계로 옮긴다.

UI 가 필요한 것은 계산 과정이 아니라 현재 표시할 상태다.

무거운 초기화는 시작 성능과 첫 상호작용 지연으로 이어질 수 있으므로 TTID 와 TTFD 를 함께 본다.

공식 참고: [Compose 성능 모범 사례](https://developer.android.com/develop/ui/compose/performance/bestpractices)
