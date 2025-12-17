---
title: apple-xctest-deep-dive
tags: [apple, testing, xctest, ui-testing]
aliases: []
date modified: 2025-12-16 17:01:32 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## XCTest Deep Dive apple testing xctest ui-testing

XCTest 를 사용한 테스트. 기본은 [[apple-testing-and-quality]] 참고.

### 단위 테스트

```swift
import XCTest
@testable import MyApp

class CalculatorTests: XCTestCase {
    var calculator: Calculator!
    
    override func setUp() {
        super.setUp()
        calculator = Calculator()
    }
    
    override func tearDown() {
        calculator = nil
        super.tearDown()
    }
    
    func testAddition() {
        let result = calculator.add(2, 3)
        XCTAssertEqual(result, 5)
    }
    
    func testDivisionByZero() {
        XCTAssertThrowsError(try calculator.divide(10, by: 0))
    }
}
```

### 비동기 테스트

```swift
func testAsyncFetch() async throws {
    let data = try await fetchData()
    XCTAssertNotNil(data)
}

func testExpectation() {
    let expectation = XCTestExpectation(description: "Fetch data")
    
    fetchData { data in
        XCTAssertNotNil(data)
        expectation.fulfill()
    }
    
    wait(for: [expectation], timeout: 5.0)
}
```

### UI 테스트

```swift
import XCTest

class UITests: XCTestCase {
    var app: XCUIApplication!
    
    override func setUp() {
        super.setUp()
        continueAfterFailure = false
        app = XCUIApplication()
        app.launch()
    }
    
    func testLogin() {
        let usernameField = app.textFields["Username"]
        usernameField.tap()
        usernameField.typeText("john")
        
        let passwordField = app.secureTextFields["Password"]
        passwordField.tap()
        passwordField.typeText("password123")
        
        app.buttons["Login"].tap()
        
        XCTAssertTrue(app.staticTexts["Welcome"].exists)
    }
}
```

### 더 보기

[[apple-testing-and-quality]], [[apple-instruments-profiling]]
