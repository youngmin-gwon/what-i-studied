---
title: apple-xctest-deep-dive
tags: [apple, async, testing, ui-testing, xctest]
aliases: []
date modified: 2026-04-06 18:15:16 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## XCTest & UI Testing Cookbook

>[!TIP] **Devil's Advocate : Swift Testing 으로의 전환**
>Xcode 16+/Swift 6 부터 **Swift Testing** 프레임워크가 XCTest 의 현대적 대안으로 부상했습니다. 단위 테스트에서는 `@Test` 매크로와 `#expect` 어설션이 `XCTAssert*` 계열을 대체합니다. 다만 **UI Testing (XCUITest)은 아직 Swift Testing 으로 대체 불가**하므로, XCTest 지식은 여전히 필수입니다.

테스트 코드는 작성하기 귀찮지만, 나중에 "이거 왜 안 되지?"라며 3 시간 동안 디버깅하는 시간을 3 초로 줄여줍니다.

특히 Swift Concurrency 가 도입되면서 비동기 테스트가 훨씬 쉬워졌습니다.

### 💡 왜 이것을 알아야 하나요? (Context)

- **Async Testing**: 예전에는 `Expectation` 만들고 `wait` 하고 코드가 너저분했습니다. 이제는 테스트 함수에 `async throws` 만 붙이면 됩니다.
- **UI Testing 의 함정**: UI 테스트는 강력하지만 "깨지기 쉽습니다(Flaky)". 네트워크가 조금만 느려도 실패합니다. UI 테스트를 100% 신뢰하지 말고, 중요한 흐름(Happy Path) 검증용으로만 쓰세요.
- **Teardown**: 테스트가 끝나면 데이터를 꼭 지워야 합니다. 안 그러면 다음 테스트가 "이미 존재하는 아이디입니다" 에러로 실패합니다. `addTeardownBlock` 을 쓰세요.

---

### 🧪 Unit Testing Recipes

#### 1. Setup & Teardown

`setUp()` 은 매 테스트마다 실행됩니다. 하지만 클래스 전체에서 한 번만 실행하고 싶다면 `setUpWithError()` (class func)를 쓰세요.

```swift
class CalculatorTests: XCTestCase {
    var sot: Calculator! // System Under Test
    
    override func setUp() {
        super.setUp()
        sot = Calculator()
    }
    
    override func tearDown() {
        sot = nil // 메모리 해제 확인
        super.tearDown()
    }
}
```

#### 2. Async Testing (Modern Way)

`Wait` 없이 `await` 로 깔끔하게 짭니다.

```swift
func testAsyncFetch() async throws {
    // Given
    let service = APIService()
    
    // When
    let data = try await service.fetchUser(id: "123")
    
    // Then
    XCTAssertEqual(data.name, "Jobs")
}
```

---

### 📱 UI Testing (XCUITest)

사용자 입력을 흉내 냅니다. 내부 코드(`sot.property`)에는 접근할 수 없고, 오직 화면에 보이는 요소(`app.buttons["Login"]`)만 만질 수 있습니다.

#### 1. Accessibility Identifier (필수)

버튼 타이틀("로그인")로 찾으면, 언어가 바뀌면(영어일 땐 "Login") 테스트가 실패합니다.

**식별자(Identifier)**를 코드에 심어두세요. 사용자 눈에는 안 보이고 테스트 봇만 봅니다.

```swift
// 앱 코드
loginButton.accessibilityIdentifier = "login_btn"

// 테스트 코드
app.buttons["login_btn"].tap()
```

#### 2. Waiting for Existence

UI 는 바로 뜨지 않습니다. 애니메이션 시간을 기다려줘야 합니다.

```swift
let welcomeLabel = app.staticTexts["welcome_msg"]
// 바로 접근하면 실패함 (아직 안 떴을 수 있음)
// XCTAssertTrue(welcomeLabel.exists) 

// ✅ Good: 5초까지 기다림
XCTAssertTrue(welcomeLabel.waitForExistence(timeout: 5.0))
```

### 더 보기

- [apple-testing-and-quality](apple-testing-and-quality.md) - 테스트 전략 (Pyramid)
- [apple-instruments-profiling](apple-instruments-profiling.md) - 테스트 통과 후 성능 최적화
