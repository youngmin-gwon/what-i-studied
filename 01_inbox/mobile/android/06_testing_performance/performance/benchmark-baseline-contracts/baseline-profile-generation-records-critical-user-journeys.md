---
title: "Baseline Profile 생성은 핵심 사용자 여정을 기록한다"
tags: ["android", "android/testing-performance"]
---

# Baseline Profile 생성은 핵심 사용자 여정을 기록한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [Benchmark와 Baseline Profile 계약](01_inbox/mobile/android/06_testing_performance/performance/benchmark-baseline-contracts/benchmark-baseline-contracts.md)
관련 노트: [Android 성능은 측정 후 최적화한다](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/measure-before-optimizing-android-performance.md)

## 목적

- Baseline Profile은 앱이 자주 실행하는 코드 경로를 배포 전에 알려주는 프로필이다.
- ART가 주요 경로를 더 이른 시점에 컴파일할 수 있도록 설치 패키지에 포함한다.
- 프로필 생성은 실제 사용 흐름을 실행해 핫 경로를 수집하는 작업이다.
- 따라서 임의의 메서드 목록을 작성하는 작업으로 이해하면 안 된다.

## 생성 흐름

1. 앱의 핵심 CUJ를 선정한다.
2. Baseline Profile 전용 테스트 모듈을 대상 앱에 연결한다.
3. `BaselineProfileRule`로 앱 실행과 사용자 행동을 캡처한다.
4. 실제 기기 또는 적절한 관리형 기기에서 생성 태스크를 실행한다.
5. 생성된 프로필을 앱 모듈의 baseline profile 위치에 반영한다.
6. 변경된 프로필을 소스 저장소에서 코드와 함께 관리한다.

## 캡처 시나리오

- 앱 시작 경로를 반드시 포함한다.
- 첫 화면에서 사용자가 곧바로 수행하는 핵심 액션을 포함한다.
- 로그인, 목록 로드, 스크롤처럼 반복 사용되는 흐름을 포함한다.
- 화면이 준비되기 전에 다음 액션을 실행하지 않도록 UI 조건을 기다린다.
- 프로필 생성 흐름은 짧더라도 대표성이 있어야 한다.

## 생성 품질

- 한 번의 성공보다 CUJ가 여러 번 안정적으로 실행되는지가 중요하다.
- 테스트 태그와 접근성 정보가 변경되면 생성 흐름도 함께 점검한다.
- 앱 코드나 주요 의존성의 큰 변경 뒤에는 프로필을 재생성한다.
- 모든 화면을 넣기보다 배포 초기에 가치가 큰 경로를 우선한다.
- 생성 결과가 실제 앱 빌드에 포함되는지 별도로 확인한다.

## 운영 원칙

- 생성은 릴리스 후보의 성능 검증 흐름과 연결한다.
- CI에서 실행한다면 에뮬레이터 가속과 리소스를 사전에 확인한다.
- 생성 비용이 크면 모든 커밋이 아니라 정해진 릴리스 단계에서 갱신한다.
- 프로필 파일의 변경 이유와 측정 결과를 릴리스 기록에 남긴다.
- 프로필은 최적화 힌트이지 앱 로직의 정합성을 보장하는 산출물이 아니다.

## 공식 참고

- [Baseline Profile 생성](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)
- [Baseline Profile 측정](https://developer.android.com/topic/performance/baselineprofiles/measure-baselineprofile)
