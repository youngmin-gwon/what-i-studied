---
title: apple-testing-and-quality
tags: [apple, quality, testing]
aliases: []
date modified: 2025-12-16 16:15:49 +09:00
date created: 2025-12-16 16:10:59 +09:00
---

## Testing & Quality apple testing quality

앱 품질을 지키는 테스트 흐름을 쉽게 정리했다. 용어는 [[apple-glossary]].

### 테스트 종류
- 단위 테스트: Swift/ObjC 로직을 빠르게 검증.
- UI 테스트: XCTest UI, XCUITest 로 실제 화면 동작 확인.
- 성능 테스트: XCTMetric, Instruments(Time Profiler, Energy, Memory).
- 스냅샷 테스트: 화면이 깨지지 않았는지 비교.
- 베타 배포: [[apple-glossary#Sideloading/TestFlight|TestFlight]] 로 실제 기기에서 사용자 피드백 수집.

### 설계와 테스트 용이성
- View-Model/UseCase/Repository 같은 계층 분리로 의존성을 주입하고 목/페이크로 교체.
- Swift Concurrency: async 함수는 TestActor/@MainActor 와 `XCTExpectations` 로 대기.

### 데이터/네트워크
- Mock URLProtocol/Network.framework NWProtocol for stubs.
- Core Data/In-Memory 스토어로 테스트 데이터 격리.

### CI 파이프라인
- xcodebuild test, Fastlane scan, GitHub Actions/Bitrise/CircleCI 등으로 자동화.
- 코드 스타일 (SwiftFormat/SwiftLint), 정적 분석 (Clang-Tidy, Swift Diagnostics) 적용.

### 크래시/로그
- Xcode Organizer/Crashes, MetricsKit, 외부 SDK(Firebase Crashlytics 등) 로 모니터링.
- DSYM 관리: 심볼 업로드 자동화, UUID 매칭.

### 접근성/현지화 테스트
- VoiceOver, Dynamic Type, RTL 레이아웃, 색상 대비 검사.
- 다국어 문자열 길이/줄바꿈/날짜/숫자 포맷 확인.

### 성능·배터리 검증
- XCTest 성능 메트릭, Instruments Energy/Network.
- 실제 저사양/배터리 세이브 모드/네트워크 제한 환경에서 재현.

### 리뷰 준비
- 개인정보/권한 문구 점검, ATT/프라이버시 라벨, 스크린샷/설명서 최신화.

### 링크

[[apple-performance-and-debug]], [[apple-build-and-distribution]], [[apple-accessibility-and-internationalization]], [[apple-platform-differences]].
