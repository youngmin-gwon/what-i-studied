---
title: "Android 성능은 측정 후 최적화한다"
tags: ["android", "android/testing-performance"]
---

# Android 성능은 측정 후 최적화한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [런타임 성능 계약](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/performance-contracts.md)

성능 문제는 먼저 관찰하고 나중에 수정한다.

사용자 체감은 느리다는 한 문장보다 구체적인 구간으로 쪼개야 한다.

- 시작: 앱을 누른 시점부터 첫 화면이 보이는 시점
- 입력: 입력 이벤트부터 화면에 반영되는 시점
- 스크롤: 프레임 예산을 넘긴 프레임의 비율
- 메모리: 화면 이동 뒤 회수되지 않는 메모리
- 에너지: CPU, 네트워크, 위치, 알람으로 깨어난 시간

최적화 전에 재현 조건을 고정한다.

- 동일한 빌드 타입과 앱 버전을 사용한다.
- 같은 기기 모델과 운영체제 버전을 기록한다.
- 배터리 잔량, 열 상태, 네트워크 종류를 기록한다.
- 데이터 크기와 로그인 상태를 고정한다.
- 냉시작, 온시작, 재시작 조건을 구분한다.

단일 실행 결과만으로 결론을 내리지 않는다.

여러 반복의 중앙값과 분산을 함께 본다.

이상치가 많으면 백그라운드 작업과 기기 열 상태를 의심한다.

사용자 영향이 큰 경로부터 측정한다.

예를 들어 앱 시작과 첫 목록 스크롤을 별도 시나리오로 만든다.

측정값에는 목표와 실패 기준을 붙인다.

목표가 없으면 작은 개선과 큰 회귀를 구별하기 어렵다.

프로덕션 문제는 개발자 기기에서 재현되지 않을 수 있다.

Play Console의 Android vitals와 함께 현장 분포를 확인한다.

[Android vitals 개요](https://developer.android.com/topic/performance/vitals)는 사용자 기기에서 관찰되는 시작, 렌더링, 배터리 문제를 분류할 때 기준이 된다.

측정 도구는 질문에 맞춰 고른다.

- 반복 가능한 사용자 여정은 Macrobenchmark
- 앱과 시스템의 시간 관계는 Perfetto
- 객체와 할당은 Android Studio Memory Profiler
- 서비스 상태의 순간값은 `dumpsys`

프로파일러를 켠 상태의 수치는 오버헤드가 있을 수 있다.

따라서 프로파일링 결과는 방향을 찾는 증거로 사용한다.

최종 회귀 기준은 동일한 릴리스 조건에서 다시 측정한다.

수정 전과 수정 후의 trace, 측정 조건, 수치를 함께 남긴다.

성능 개선은 코드 변경 자체가 아니라 사용자 지표의 변화로 판정한다.

측정할 수 없는 최적화 주장은 우선순위에서 제외한다.
