---
title: "Benchmark 결과는 물리 기기와 CI 조건을 통제해야 한다"
tags: ["android", "android/testing-performance"]
---

# Benchmark 결과는 물리 기기와 CI 조건을 통제해야 한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [Benchmark와 Baseline Profile 계약](01_inbox/mobile/android/06_testing_performance/performance/benchmark-baseline-contracts/benchmark-baseline-contracts.md)
관련 노트: [Android 성능은 측정 후 최적화한다](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/measure-before-optimizing-android-performance.md)

## 왜 환경이 중요한가

- Macrobenchmark는 CPU, 저장장치, 화면 주사율, 열 상태의 영향을 크게 받는다.
- 에뮬레이터와 물리 기기는 같은 앱이라도 다른 성능 분포를 만든다.
- CI의 가상화 성능과 백그라운드 부하는 반복 결과를 흔들 수 있다.
- 따라서 환경 정보 없는 숫자는 재현 가능한 성능 기준이 되기 어렵다.

## 물리 기기 권장 원칙

- 릴리스 사용자 경험을 대표하는 하나 이상의 물리 기기를 정한다.
- 기기 모델과 Android 버전을 고정해 전후 비교의 변수를 줄인다.
- 배터리, 열, 저장공간, 실행 중인 앱 상태를 관리한다.
- 측정 전 기기를 충분히 안정화하고 불필요한 작업을 중단한다.
- 같은 기기에서 기준군과 실험군을 번갈아 실행한다.

## 에뮬레이터와 관리형 기기

- 에뮬레이터는 자동화하기 쉽지만 가속 지원과 호스트 부하에 의존한다.
- Gradle Managed Device는 CI에서 일관된 단말 정의를 유지하는 데 도움이 된다.
- 헤드리스 실행은 디스플레이가 없는 서버의 제약을 줄일 수 있다.
- 관리형 기기의 API, 이미지, 가상화 설정을 결과와 함께 기록한다.
- 에뮬레이터 결과를 물리 기기의 사용자 체감과 동일하다고 표현하지 않는다.

## CI 운영

1. CI 머신의 하드웨어 가속 가능 여부를 확인한다.
2. SDK, 시스템 이미지, 빌드 도구 버전을 고정한다.
3. 테스트 앱 설치와 데이터 초기화 절차를 명시한다.
4. 생성 태스크와 검증 태스크를 별도의 파이프라인 단계로 둔다.
5. 성능 결과와 trace, 로그를 아티팩트로 보존한다.

## 실패와 변동 대응

- 기기 연결 실패와 성능 회귀를 같은 실패 유형으로 처리하지 않는다.
- timeout 증가는 무조건 해결책이 아니며 준비 조건의 불안정성을 먼저 찾는다.
- 실행 횟수를 늘리기 전에 열 상태와 백그라운드 부하를 점검한다.
- CI에서만 실패하면 테스트 동작과 환경 제약을 분리해 재현한다.
- 기준선은 단일 실행값보다 반복 분포와 허용 범위로 관리한다.

## 공식 참고

- [Macrobenchmark 개요](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
- [Baseline Profile 생성](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)
- [Baseline Profile 측정](https://developer.android.com/topic/performance/baselineprofiles/measure-baselineprofile)
