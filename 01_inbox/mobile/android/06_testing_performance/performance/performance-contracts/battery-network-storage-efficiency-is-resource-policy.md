---
title: "배터리, 네트워크, 저장소 성능은 자원 정책이다"
tags: ["android", "android/testing-performance"]
---

# 배터리, 네트워크, 저장소 성능은 자원 정책이다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [런타임 성능 계약](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/performance-contracts.md)

배터리 비용은 CPU 시간만으로 설명되지 않는다.

네트워크 라디오 깨움, 위치 센서, 알람, wakelock이 함께 영향을 준다.

작은 작업을 자주 실행하면 개별 작업보다 깨움 비용이 커질 수 있다.

즉시 필요하지 않은 동기화는 작업을 묶고 조건이 맞을 때 실행한다.

Doze와 App Standby를 우회하려는 설계는 장기적으로 사용자 비용을 높인다.

정확한 알람은 실제 시간 정확성이 필요한 경우에만 사용한다.

Foreground Service는 사용자에게 진행 중인 작업을 보여 줘야 할 때만 선택한다.

네트워크 요청은 캐시, 압축, 페이지 단위 응답으로 전송량을 줄인다.

실패 재시도에는 지수 백오프와 상한을 둔다.

연결이 불안정할 때 무한 재시도는 배터리와 데이터 비용을 함께 키운다.

네트워크 상태와 비용을 보고 예약 작업의 조건을 정한다.

저장소 접근은 작은 동기식 호출을 반복하지 않도록 묶는다.

Room 질의에는 실제 필터와 정렬에 맞는 인덱스를 둔다.

큰 결과는 Paging으로 읽어 메모리와 디스크 작업을 제한한다.

WAL은 읽기와 쓰기 동시성에 도움을 줄 수 있지만 저장소 비용을 측정해야 한다.

파일 캐시는 만료와 용량 상한을 가져야 한다.

`dumpsys batterystats`는 앱이 CPU, 네트워크, wakelock을 얼마나 사용했는지 확인하는 출발점이다.

Battery Historian은 bugreport를 시간축으로 비교할 때 유용하다.

[전원 관리 리소스 제한](https://developer.android.com/topic/performance/power/power-details)은 백그라운드 작업과 시스템 제약을 설계할 때 기준이 된다.

[Android 연결성](https://developer.android.com/develop/connectivity)은 네트워크 상태와 연결 비용을 고려할 때 참고할 공식 문서 묶음이다.

배터리 테스트는 동일한 밝기, 네트워크, 사용 시나리오에서 반복한다.

짧은 실험에서 배터리 잔량만 비교하면 오차가 크다.

시간축에서 깨움과 작업이 어떤 이벤트에 대응하는지 본다.

성공 기준은 기능을 유지하면서 작업 횟수와 전송량을 줄이는 것이다.
