# watchOS Battery & Performance #apple #watchos #performance

애플워치에서 배터리를 아끼고 성능을 유지하는 방법을 쉽게 정리했다. 용어는 [[apple-glossary]].

## 제약 이해하기
- 작은 배터리/메모리, 강한 백그라운드 제한. [[apple-glossary#JetSam|Jetsam]]이 자주 발생할 수 있다.
- 화면이 꺼지면 앱이 정지되고, “손목 올림” 순간에 빠르게 다시 나타나야 한다.

## 코드/작업
- CPU/GPU 일을 짧게 나눈다. 긴 연산은 iPhone/서버에 맡기고 결과만 보여준다.
- 타이머/폴링 최소화. 필요한 경우 Background Refresh/Push/Workout 세션 등 허용된 모드만 사용.
- 애니메이션/이펙트는 단순/짧게.

## 네트워크
- 데이터 사용을 줄이고, 압축/짧은 요청/캐시 활용.
- 가능하면 iPhone 프록시 경로 사용, 직접 셀룰러는 최후 수단.
- 실패 시 재시도 횟수 제한, 오프라인 큐 사용.

## 화면/렌더링
- SwiftUI에서 복잡한 레이아웃/긴 리스트를 줄인다. 필요 시 `TimelineView`/`Canvas` 최적화.
- 이미지는 작은 해상도로, 캐시/프리로드.
- 햅틱/사운드는 짧게, 과다 사용 금지.

## 센서/헬스
- HealthKit/WorkoutKit 샘플 주기/정확도를 필요 최소로 설정.
- GPS/위치는 배터리를 크게 소모. 오프라인 지도/캐시, 샘플링 간격 조절.

## 메모리
- 큰 배열/이미지/모델을 보관하지 않는다. 사용 후 즉시 해제.
- Instruments(Memory/Time Profiler)로 피크 사용량 확인.

## 테스트
- 실제 운동/외부 환경/약한 네트워크에서 테스트.
- 배터리 소모/열/메모리 경고/종료 로그(JetsamEvent) 확인.
- 손목 올림/앱 전환/알림 간 전환 속도 측정.

## 사용자 경험
- 로딩/동기화 중에도 간단한 상태/진행 표시.
- 알림/컴플리케이션/Live Activity 업데이트 빈도를 제한.
- 배터리 부족 시 기능 축소/저품질 모드 안내.

## 링크
[[apple-watchos-wearables]], [[apple-watchos-fitness-guide]], [[apple-offline-and-resilience]], [[apple-performance-and-debug]].
