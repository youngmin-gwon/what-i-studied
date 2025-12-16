---
title: apple-watchos-wearables
tags: [apple, watchos, wearable]
aliases: []
date modified: 2025-12-16 16:15:51 +09:00
date created: 2025-12-16 16:13:50 +09:00
---

## watchOS & Wearables apple watchos wearable

애플워치용 앱/컴플리케이션을 만들 때 알아두면 좋은 점을 쉽게 정리했다. 용어는 [[apple-glossary]].

### 설계 철학
- 짧은 상호작용, 한눈에 정보. 배터리와 메모리 예산이 작다.
- iPhone 과 페어링되어 데이터를 주고받지만, 최신 워치는 독립 네트워크도 가능.

### 진입점
- 워치 앱 (전체 화면), 컴플리케이션 (시계 페이스 정보), 알림, Siri/단축어, 백그라운드 작업, 워크아웃 세션.
- SwiftUI 가 기본 UI 도구. Scene 기반이지만 화면 크기가 작으므로 단순 레이아웃 권장.

### 데이터 교환
- WCSession 으로 iPhone↔Watch 메시지/파일 전송. Reachability/활성 세션을 확인해야 한다.
- Background Refresh, Push, Complication push timeline 을 사용해 최신 상태 유지.

### 센서/헬스
- HealthKit/WorkoutKit 으로 심박/움직임/칼로리/산소포화도 등을 측정.
- CoreMotion 으로 걸음/낙상 감지, GPS/셀룰러로 위치 추적 (권한 필요).

### 배터리/제약
- 백그라운드 실행 시간 매우 짧음. 워크아웃/오디오/위치/VoIP 등 허용된 모드만 장시간 실행 가능.
- 메모리 부족 시 Jetsam 종료가 자주 발생할 수 있다. 큰 이미지/데이터를 피하고 즉시 해제.

### 네트워크
- 셀룰러/와이파이/블루투스. 가능하면 짧은 요청, 적은 데이터.
- iPhone 프록시를 통해 인터넷 접근할 때도 있다.

### 알림/컴플리케이션
- Rich Notification UI 가능. 미리보기가 간단해야 한다.
- Complication timeline 을 준비해 오프라인에서도 시간이 바뀌면 값이 변하도록 한다.

### 테스트
- 실제 기기에서 센서/배터리 동작을 확인. 시뮬레이터는 센서/배터리 차이를 반영하지 못한다.
- 여러 손목/피트니스 모드/네트워크 상태에서 동작을 점검.

### 링크

[[apple-networking-and-cloud]], [[apple-accessibility-and-internationalization]], [[apple-performance-and-debug]], [[apple-platform-differences]].
