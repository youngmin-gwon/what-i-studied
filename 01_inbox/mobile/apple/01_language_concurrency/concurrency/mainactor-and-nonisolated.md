---
title: mainactor-and-nonisolated
tags: [apple, apple/concurrency, apple/language, mainactor, swift, ui]
aliases: ["@MainActor 는 UI 상태를 메인 스레드에 묶고 nonisolated 가 그 탈출구다", "MainActor", "nonisolated", "메인 액터"]
date modified: 2026-09-03 00:00:00 +09:00
date created: 2026-09-03 00:00:00 +09:00
---

## @MainActor 는 UI 상태를 메인 스레드에 묶고 nonisolated 가 그 탈출구다

### 개념 (What)

`@MainActor` 는 **전역 actor** 다. 일반 actor 가 자기 인스턴스의 상태를 보호한다면, `@MainActor` 는 **프로세스 전체에서 하나뿐인 "메인 스레드"라는 실행 컨텍스트**를 보호한다.

`@MainActor` 가 붙은 타입·메서드·프로퍼티는 메인 스레드에서만 접근할 수 있고, 컴파일러가 이를 강제한다.

### 왜 필요한가 (Why)

기존에는 "이 코드가 메인 스레드에서 도는가"를 개발자가 추적해야 했다.

```swift
// 기존: 규율에 의존. 빠뜨려도 컴파일된다
api.fetch { data in
    DispatchQueue.main.async { self.label.text = data.title }
}

// 현재: 컴파일러가 강제. 빠뜨리면 컴파일 에러
@MainActor func update(_ data: Data) { label.text = data.title }
```

`UIView`, `UIViewController`, SwiftUI 의 `View` 는 이미 `@MainActor` 로 선언되어 있다. 그래서 백그라운드에서 UI 를 건드리는 코드가 **컴파일되지 않는다.**

### 격리 상속 규칙

이 규칙을 모르면 "왜 여기는 되고 저기는 안 되는가"가 혼란스럽다.

| 선언 | 격리 |
| :--- | :--- |
| 타입에 `@MainActor` | 모든 멤버가 상속 |
| 메서드에만 `@MainActor` | 그 메서드만 |
| `@MainActor` 타입 안의 `nonisolated` 멤버 | 격리 해제 (격리 상태 접근 불가) |
| `@MainActor` 함수가 호출하는 일반 async 함수 | **상속되지 않는다** |

마지막 줄이 함정이다.

```swift
@MainActor
final class ViewModel {
    var items: [Item] = []

    func load() async {
        // 여기는 MainActor
        let fetched = await repository.fetch()   // repository 는 MainActor 아님
        // await 에서 돌아오면 다시 MainActor 로 복귀한다
        items = fetched                          // 안전
    }

    // 무거운 계산은 메인 스레드에서 빼낸다
    nonisolated func checksum(of data: Data) -> String {
        // self.items 접근 불가 (격리 위반)
        SHA256.hash(data: data).description
    }
}
```

### `nonisolated` 를 쓰는 두 가지 이유

**1. 메인 스레드에서 빼내기**

`@MainActor` 타입의 무거운 순수 계산은 메인 스레드를 점유할 이유가 없다. `nonisolated` 로 빼면 협력적 풀에서 실행된다.

**2. 동기 접근을 허용하기**

`await` 없이 호출할 수 있게 만든다. 불변 프로퍼티나 순수 함수에 적합하다.

```swift
@MainActor
final class Store {
    nonisolated let id: UUID          // await 없이 어디서나 읽을 수 있다
    var items: [Item] = []            // 이건 MainActor
    init(id: UUID) { self.id = id }
}
```

### `MainActor.assumeIsolated` — 이미 메인인 것을 아는 경우

델리게이트 콜백처럼 **실제로는 메인 스레드에서 오지만 시그니처에 표시가 없는** 경우가 있다.

```swift
func someLegacyDelegateCallback() {
    // 메인 스레드에서 온다는 것을 알고 있을 때
    MainActor.assumeIsolated {
        self.items = []          // await 없이 접근
    }
}
```

> [!WARNING] assume 은 검증이 아니다
> 실제로 메인 스레드가 아니면 **런타임 크래시**다. 정말 확실할 때만 쓰고, 불확실하면 `Task { @MainActor in ... }` 를 쓴다.

### SwiftUI 와의 관계

SwiftUI 의 `View.body` 는 `@MainActor` 다. `@Observable` 이나 `@State` 로 관리하는 모델도 대개 `@MainActor` 로 두는 것이 자연스럽다. 반대로 **네트워크·파싱·이미지 디코딩은 `@MainActor` 밖으로 빼야** [커밋 구간이 늘어나지 않는다](../../01_system_internals/graphics-and-media/layer-tree-commit-to-render-server.md).

### 관찰 가능한 증거

```swift
// 현재 실행 컨텍스트가 메인인지 런타임 확인 (디버그 전용)
dispatchPrecondition(condition: .onQueue(.main))
assert(Thread.isMainThread)
```

- **Xcode Main Thread Checker**: 스킴 옵션에서 켜면 백그라운드에서의 UIKit 접근을 런타임에 잡는다. `@MainActor` 가 컴파일 타임에 못 잡는 레거시 경로를 보완한다.
- **Instruments의 Swift Concurrency**: 각 Task 가 어느 actor 에서 실행되는지 보여준다. `@MainActor` 작업이 과도하면 메인 스레드가 붐빈다.

### 연관 문서

- [actor 격리는 가변 상태 접근을 직렬화해 데이터 경합을 컴파일 타임에 차단한다](actor-isolation-serializes-state-access.md)
- [협력적 스레드 풀은 코어 수만큼만 스레드를 유지해 thread explosion 을 구조적으로 막는다](cooperative-thread-pool.md)
- [apple-observation-framework](../apple-observation-framework.md) - @Observable 과의 조합
- [07-swiftui-state-change-to-pixel](../../00_foundations/worked-examples/07-swiftui-state-change-to-pixel.md)

공식 문서: [SE-0316: Global actors](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0316-global-actors.md)
