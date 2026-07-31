---
title: "Macrobenchmark는 실제 사용자 여정을 측정한다"
tags: ["android", "android/testing-performance"]
---

# Macrobenchmark는 실제 사용자 여정을 측정한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [Benchmark와 Baseline Profile 계약](01_inbox/mobile/android/06_testing_performance/performance/benchmark-baseline-contracts/benchmark-baseline-contracts.md)
관련 노트: [Android 성능은 측정 후 최적화한다](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/measure-before-optimizing-android-performance.md)

## 핵심 주장

- Macrobenchmark는 앱 프로세스 안의 작은 함수가 아니라 앱 전체의 큰 동작을 측정한다.
- 측정 단위는 시작, 화면 전환, 목록 스크롤처럼 사용자가 체감하는 여정이다.
- 테스트 코드는 별도 테스트 모듈에서 대상 앱을 외부에서 실행하고 조작한다.
- 따라서 단위 테스트보다 실제 배포 앱에 가까운 성능 신호를 얻을 수 있다.

## 측정 흐름

1. 테스트가 대상 패키지를 지정한다.
2. `setupBlock`에서 매 반복의 초기 상태를 준비한다.
3. 측정 블록 안에서 사용자 행동을 재현한다.
4. 지정한 metric이 시간, 프레임, 트레이스 등의 결과를 수집한다.
5. 여러 반복의 분포를 보고 최적화 전후를 비교한다.

## 여정 설계

- 앱 시작만 측정하면 시작 단계의 초기화 비용을 본다.
- 로그인 후 첫 화면 진입은 인증과 데이터 로딩 경로를 포함한다.
- 목록 스크롤은 프레임 렌더링과 UI 바인딩 경로를 포함한다.
- 검색, 상세 진입, 결제처럼 사업적으로 중요한 흐름도 후보가 된다.
- 각 여정은 시작 조건과 종료 조건을 문장으로 먼저 정의한다.

## 구현 시 주의점

- 앱 내부의 테스트 전용 우회 경로를 호출하면 실제 사용자 여정이 아니다.
- UI Automator가 찾을 수 있도록 안정적인 리소스 ID나 접근성 정보를 제공한다.
- 네트워크 응답이나 서버 상태가 매번 달라지면 결과 변동이 커진다.
- 필요한 경우 고정된 테스트 계정과 결정적인 테스트 데이터를 사용한다.
- 불필요한 대기 시간을 측정 블록에 넣지 않도록 준비와 측정을 분리한다.

## 결과 해석

- 한 번의 최솟값보다 반복 결과의 중앙값과 꼬리 분포를 함께 본다.
- 최적화 전후에는 같은 기기, 같은 빌드 변형, 같은 여정을 유지한다.
- 성능 회귀는 코드 변경과 측정 환경 변경을 구분해 확인한다.
- Macrobenchmark는 원인을 자동으로 고치는 도구가 아니라 재현 가능한 측정 경계다.

## 공식 참고

- [Macrobenchmark 개요](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
- [Baseline Profile 생성](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)
- [Baseline Profile 측정](https://developer.android.com/topic/performance/baselineprofiles/measure-baselineprofile)
