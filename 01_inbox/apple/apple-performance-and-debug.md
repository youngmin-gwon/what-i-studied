# Performance & Debugging #apple #performance #debugging

앱을 빠르고 안정적으로 만들기 위한 기본 체크리스트. 용어는 [[apple-glossary]].

## 속도 목표
- 앱 시작: 런치 화면에서 실제 UI까지 최대한 짧게(냉/온/재실행 구분).
- 프레임: 16ms(60fps) 또는 ProMotion 120Hz 타깃. dropped frame/jank 최소화.
- 메모리: [[apple-glossary#JetSam|Jetsam]] 종료를 피하고, 메모리 경고 시 자원 해제.
- 에너지: 불필요한 백그라운드/네트워크/로케이션 사용 줄이기.

## 도구
- Instruments: Time Profiler, Allocations, Leaks, Memory Graph, Energy Log, Network, Game/Metal.
- Xcode Organizer: 크래시/에너지 피드백, 성능 메트릭.
- sysdiagnose/metrics: 실제 기기 지표 수집.

## 스타트업 최적화
- @main 진입 전 실행되는 초기화 줄이기. SwiftUI `@main` body에서 무거운 일 피하기.
- dyld launch time을 줄이기 위해 프레임워크 수/의존성 최소화.
- Scene/윈도우 생성 후 비동기로 무거운 작업을 밀어낸다.

## 렌더링 성능
- SwiftUI: 상태 최소화, 뷰 ID 안정화, 과한 diff 방지.
- UIKit/AppKit: Auto Layout 제약 최소화, 레이아웃 패스 수 줄이기, 오버드로우 점검.
- Core Animation Profile, GPU Frame Capture로 병목 확인.

## 메모리
- 큰 이미지/데이터는 스트리밍/청크로 처리.
- 순환 참조(클로저 캡처) 점검, `weak self` 사용.
- Instruments Memory Graph로 누수/자원 누락 확인.

## 동시성
- [[apple-glossary#GCD|GCD]] QoS를 알맞게 설정, 메인 큐 차단 금지.
- Swift Concurrency(Task/Actor)로 데이터 경합을 줄이고, cancellation을 처리.

## 네트워크/저장소 효율
- 캐시/압축/백오프, HTTP/3 활용. Background URLSession로 업/다운로드.
- Core Data/SQLite는 페칭/프리페치, 배치 업데이트, 컨텍스트 병합 전략 주의.

## 에너지/배터리
- Background Modes 최소화, 타이머/폴링 줄이기.
- 위치/블루투스 스캔을 필요할 때만. Widgets/Live Activities는 업데이트 주기 관리.

## 크래시/안정성
- [[apple-glossary#Crash Report|크래시 리포트]] + [[apple-glossary#DSYM|dSYM]]로 심볼리케이션.
- 예외/에러 처리를 명확히. 보호되지 않은 옵셔널 언래핑 주의.

## 링크
[[apple-testing-and-quality]], [[apple-app-lifecycle-and-ui]], [[apple-rendering-and-media]], [[apple-networking-and-cloud]].
