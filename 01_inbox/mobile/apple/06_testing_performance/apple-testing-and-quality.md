---
title: apple-testing-and-quality
tags: [apple, ci, quality, tdd, testing]
aliases: []
date modified: 2026-04-06 18:15:40 +09:00
date created: 2025-12-16 16:10:59 +09:00
---

## Testing & Quality Assurance Deep Dive

>[!WARNING] **Devil's Advocate : Swift Testing 프레임워크의 등장**
>WWDC 2024 에서 발표된 **Swift Testing** 프레임워크(`@Test` 매크로, `#expect` 어설션)는 XCTest 를 대체하는 차세대 테스트 프레임워크입니다.
> 1. `XCTAssertEqual` 대신 `#expect(a == b)` 로 더 자연스러운 표현식 사용.
> 2. `@Test("설명", .tags(.networking))` 매크로로 테스트 메타데이터를 선언적으로 관리.
> 3. 매개변수화된 테스트(`@Test(arguments: [1, 2, 3])`)를 기본 지원.
>신규 테스트 코드는 Swift Testing 을 우선 채택하되, UI Testing 은 아직 XCUITest 가 필수입니다.

"테스트 코드가 없는 코드는 레거시 코드다." — 마이클 페더스

앱이 1.0 에서 끝난다면 테스트는 필요 없습니다. 하지만 2.0 을 만들 생각이라면, 테스트는 선택이 아니라 **생명 보험**입니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **회귀(Regression) 방지**: A 기능을 고쳤는데 잘 되던 B 기능이 망가진 적 있으시죠? 테스트 커버리지가 높다면, 코드를 수정하고 Cmd+U 를 누르는 것만으로 "다른 기능은 안전하다"는 확신을 얻을 수 있습니다.
- **리팩토링의 용기**: 더러운 코드를 보고도 "건드리면 터질까 봐" 못 고치고 계신가요? 테스트가 있으면 과감하게 구조를 개선할 수 있습니다.
- **문서화**: 테스트 코드는 그 자체로 "이 함수는 이렇게 쓰는 거야"라고 말해주는, 거짓말하지 않는 문서입니다.

---

### 🧪 주요 테스트 전략 (Testing Pyramid)

#### 1. Unit Test (단위 테스트) - 70%

가장 빠르고 비용이 저렴합니다. 로직 하나하나를 검증합니다.

- **Mocking**: 네트워크나 DB 처럼 느린 의존성은 가짜(Mock)로 대체해야 합니다. "테스트가 1 초 이상 걸리면 안 한다"는 말을 명심하세요.

```swift
func testLoginSuccess() {
    let mockAPI = MockAPIService()
    mockAPI.shouldSucceed = true
    let viewModel = LoginViewModel(api: mockAPI)
    
    viewModel.login(id: "test", pw: "1234")
    
    XCTAssertTrue(viewModel.isLoggedIn)
}
```

#### 2. Integration Test (통합 테스트) - 20%

모듈 간의 연결을 테스트합니다.

- 예: Core Data 에 저장하고 읽어왔을 때 데이터가 깨지지 않는지 확인.

#### 3. UI Test (E2E 테스트) - 10%

실제 사용자가 버튼을 누르는 것처럼 시뮬레이터를 조작합니다.

- **Trade-off**: 매우 느리고 잘 깨집니다(Flaky). 중요한 사용자 흐름(로그인, 결제) 위주로 최소한만 작성하세요.

---

### 🧱 Testable Architecture (설계)

테스트를 짜기 어렵다면, 설계가 잘못된 것입니다.

#### 1. Dependency Injection (DI)

객체가 내부에서 의존성(`URLSession.shared`)을 직접 생성하면 테스트할 수 없습니다. 생성자로 주입받으세요.

#### 2. Protocol Oriented

구체 클래스(`MyDatabase`) 대신 프로토콜(`DatabaseProtocol`)에 의존해야 가짜 객체(Stub)를 끼워 넣을 수 있습니다.

---

### 💻 CI/CD & Automation

로컬에서 혼자 돌리는 테스트는 의미가 없습니다. 코드가 머지되기 전에 항상 검사해야 합니다.

- **Fastlane**: 빌드, 테스트, 배포를 스크립트 하나로 자동화합니다. (`fastlane test`)
- **Xcode Cloud**: Apple 이 제공하는 CI. TestFlight 와 연동이 매끄럽지만 비쌉니다.
- **GitHub Actions**: 가장 대중적입니다. PR 이 올라올 때마다 `xcodebuild test` 를 돌려서 빨간 줄(실패)이 뜨면 머지를 막으세요.

### 더 보기

- [apple-performance-monitoring](apple-performance-monitoring.md) - 성능 테스트(XCTMetric) 방법
- [apple-xctest-deep-dive](apple-xctest-deep-dive.md) - XCTest 프레임워크 상세 사용법
- [Swift Testing Documentation](https://developer.apple.com/documentation/testing) - 차세대 테스트 프레임워크 (WWDC 2024)
