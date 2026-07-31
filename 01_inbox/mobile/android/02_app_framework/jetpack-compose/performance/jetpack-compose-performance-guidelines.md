# Jetpack Compose 코드 수준 성능 최적화 가이드

이 문서는 Android Dev Summit ("More performance tips for Jetpack Compose") 세션 내용을 바탕으로, Jetpack Compose UI 작성 시 불필요한 리컴포지션(Recomposition)을 차단하고 렌더링 성능을 극대화하기 위한 **코드 수준의 최적화 규칙**을 정리합니다.

---

---

## 원자 노트

- [성능 최적화의 대전제: Loop Cycle (Measure -> Debug -> Improve)](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines/01-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94%EC%9D%98-%EB%8C%80%EC%A0%84%EC%A0%9C-loop-cycle-measure-debug-improve.md)
- [상태 읽기 지연 (Defer State Reads)](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines/02-%EC%83%81%ED%83%9C-%EC%9D%BD%EA%B8%B0-%EC%A7%80%EC%97%B0-defer-state-reads.md)
- [DerivedStateOf의 올바른 활용](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines/03-derivedstateof%EC%9D%98-%EC%98%AC%EB%B0%94%EB%A5%B8-%ED%99%9C%EC%9A%A9.md)
- [`reportFullyDrawn` API를 이용한 시작 성능 최적화](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines/04-reportfullydrawn-api%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%8B%9C%EC%9E%91-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94.md)
- [System Tracing & Perfetto 기반 원인 디버깅](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines/05-system-tracing-perfetto-%EA%B8%B0%EB%B0%98-%EC%9B%90%EC%9D%B8-%EB%94%94%EB%B2%84%EA%B9%85.md)
- [BoxWithConstraints 사용 시 주의사항 및 대체 방안](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines/06-boxwithconstraints-%EC%82%AC%EC%9A%A9-%EC%8B%9C-%EC%A3%BC%EC%9D%98%EC%82%AC%ED%95%AD-%EB%B0%8F-%EB%8C%80%EC%B2%B4-%EB%B0%A9%EC%95%88.md)
- [`remember` 내 무거운 연산(Heavy Computation) 격리](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines/07-remember-%EB%82%B4-%EB%AC%B4%EA%B1%B0%EC%9A%B4-%EC%97%B0%EC%82%B0-heavy-computation-%EA%B2%A9%EB%A6%AC.md)
- [비동기 이미지 로딩 (Asynchronous Image Loading)](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines/08-%EB%B9%84%EB%8F%99%EA%B8%B0-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%A1%9C%EB%94%A9-asynchronous-image-loading.md)
- [무거운 프레임 (Heavy Frames) 분해 및 스케줄링](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines/09-%EB%AC%B4%EA%B1%B0%EC%9A%B4-%ED%94%84%EB%A0%88%EC%9E%84-heavy-frames-%EB%B6%84%ED%95%B4-%EB%B0%8F-%EC%8A%A4%EC%BC%80%EC%A4%84%EB%A7%81.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
