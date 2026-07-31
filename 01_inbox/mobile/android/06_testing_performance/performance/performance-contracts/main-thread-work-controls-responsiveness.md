---
title: "메인 스레드 작업은 앱 응답성을 결정한다"
tags: ["android", "android/testing-performance"]
---

# 메인 스레드 작업은 앱 응답성을 결정한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [런타임 성능 계약](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/performance-contracts.md)

메인 스레드는 입력 이벤트를 받고 화면을 계산하고 그리기를 요청한다.

긴 작업이 이 스레드를 점유하면 입력 지연과 지연 프레임이 발생한다.

디스크, 네트워크, 큰 JSON 파싱, 데이터베이스 질의를 메인에서 실행하지 않는다.

계산 작업은 `Default`, 입출력 작업은 `IO` 실행 컨텍스트로 이동한다.

화면 갱신 결과만 메인 스레드로 되돌린다.

작업을 다른 스레드로 옮기는 것만으로 끝나지 않는다.

락 대기, 스레드 풀 고갈, 과도한 전환도 지연을 만든다.

Binder 호출은 짧게 유지하고 큰 결과를 동기적으로 기다리지 않는다.

동기 Binder 호출이 메인 스레드에 있으면 원격 서비스 지연이 UI를 멈출 수 있다.

반복 작업은 무제한 새 스레드보다 제한된 실행기를 사용한다.

사용자 시작이 아닌 지속 작업은 WorkManager 같은 예약 수단을 검토한다.

StrictMode는 개발 중 메인 스레드의 디스크와 네트워크 접근을 드러낸다.

`penaltyLog`로 먼저 위반을 수집하고, 팀 규칙이 정해지면 더 강한 정책을 적용한다.

ANR은 단순히 느린 메서드 하나가 아니라 응답하지 못한 상태의 결과다.

ANR trace와 Perfetto에서 메인 스레드가 무엇을 기다렸는지 확인한다.

메인 스레드가 CPU를 사용했는지 락이나 Binder를 기다렸는지 구분한다.

[앱 응답성](https://developer.android.com/topic/performance/vitals/render)은 입력 지연과 ANR을 사용자 영향으로 연결한다.

[ANR 진단](https://developer.android.com/topic/performance/vitals/anr)은 trace와 호출 경로를 해석하는 출발점이다.

작업을 백그라운드로 옮긴 뒤 취소와 수명도 설계한다.

화면이 사라진 뒤에도 결과를 적용하면 오래된 상태와 추가 작업이 생긴다.

코루틴은 화면 수명에 맞는 scope에서 시작한다.

메인 스레드의 짧은 구간이 반복되어도 전체 프레임 예산을 넘길 수 있다.

trace의 긴 구간과 호출 빈도를 함께 본다.

수정 후에는 입력, 스크롤, 화면 전환을 동일한 시나리오로 재측정한다.

성공 기준은 스레드 개수가 아니라 사용자 응답성이 회복되는 것이다.
