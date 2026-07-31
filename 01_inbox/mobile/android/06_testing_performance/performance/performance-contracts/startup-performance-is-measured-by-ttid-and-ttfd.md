---
title: "Android 시작 성능은 TTID와 TTFD로 나눈다"
tags: ["android", "android/testing-performance"]
---

# Android 시작 성능은 TTID와 TTFD로 나눈다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [런타임 성능 계약](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/performance-contracts.md)

앱 시작 시간은 첫 화면과 실제 사용 가능 상태를 구분해야 한다.

TTID는 첫 프레임이 표시되기까지의 시간이다.

TTFD는 사용자가 의미 있는 콘텐츠를 볼 수 있을 때까지의 시간이다.

첫 프레임만 빠르고 빈 화면이 오래 유지되면 TTFD는 나쁘다.

냉시작은 프로세스가 없는 상태에서 시작하는 경우다.

온시작은 프로세스가 살아 있는 상태에서 Activity를 다시 여는 경우다.

두 조건은 병목과 목표가 다르므로 별도로 측정한다.

시작 경로에는 `Application.onCreate`와 첫 Activity 초기화가 포함된다.

DI 그래프 생성, 로깅, 원격 설정, SDK 초기화가 이 구간을 늘릴 수 있다.

첫 화면에 필요하지 않은 초기화는 지연한다.

화면 뒤에서 가능한 작업은 비동기로 이동한다.

WebView와 지도 같은 무거운 SDK는 실제 사용 시점에 예열한다.

지연 초기화가 첫 사용 순간의 지연으로 이동하지 않는지도 측정한다.

Baseline Profile은 자주 실행되는 코드를 미리 컴파일하는 방법이다.

Cloud Profiles와 함께 사용하면 실제 사용 패턴에 맞는 최적화를 기대할 수 있다.

[앱 시작 시간 최적화](https://developer.android.com/topic/performance/vitals/launch-time)는 시작 구간을 측정하고 줄이는 기본 원칙을 설명한다.

[Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview)는 첫 실행과 주요 사용자 여정의 실행 비용을 낮추는 기준이다.

시작 측정은 화면이 실제로 준비된 시점까지 포함해야 한다.

테스트에서 `startActivityAndWait`만 호출하면 콘텐츠 준비가 끝났는지 확인한다.

Macrobenchmark의 `StartupTimingMetric`으로 냉시작과 온시작을 반복한다.

릴리스와 유사한 빌드 타입에서 측정한다.

디버그 빌드의 로그와 검증 코드는 시작 비용을 왜곡할 수 있다.

수정 전후에 중앙값과 상위 백분위 변화를 비교한다.

TTID가 줄었지만 TTFD가 늘었다면 초기화를 너무 늦춘 것이다.

TTFD가 줄었지만 냉시작만 악화되면 공통 초기화 비용을 다시 본다.

스플래시 화면은 측정값을 숨기는 장치가 아니다.

사용자가 첫 상호작용을 할 수 있는 시점과 스플래시 종료 시점을 구분한다.

프로파일링에서는 메인 스레드의 긴 구간을 먼저 찾는다.

그 다음 시작 중 생성된 객체와 디스크, 네트워크 접근을 확인한다.

시작 성능의 목표는 작은 숫자 하나보다 반복 가능한 사용자 경험이다.
