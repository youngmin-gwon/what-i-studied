---
title: apple-app-lifecycle-and-ui
tags: [apple, lifecycle, swiftui, uikit, appdelegate, scenedelegate]
aliases: []
date modified: 2025-12-17 19:40:00 +09:00
date created: 2025-12-16 16:08:54 +09:00
---

## App Lifecycle & UI Architecture

앱 아이콘을 누르면 무슨 일이 일어날까요? 단순히 "켜진다"고 생각하면 오산입니다.
OS는 앱을 죽일지 살릴지 끊임없이 고민하며, iOS 13부터는 "앱 하나에 창 여러 개(Multi-window)"라는 복잡한 개념이 도입되었습니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **앱이 자꾸 죽어요**: 백그라운드로 갔을 때 자원을 해제하지 않거나, 잘못된 타이밍에 네트워크 요청을 하면 OS가 앱을 강제 종료(Jetsam)합니다.
- **AppDelegate가 왜 텅 비었죠?**: 예전엔 `APP` = `UI`였지만, 지금은 `APP` = `n개의 Scene`입니다. 이 변화를 모르면 새 프로젝트의 `SceneDelegate`를 보고 당황하게 됩니다.
- **iPad 멀티태스킹**: 사용자가 앱을 두 개 띄워놓고 서로 데이터를 옮기는 경험을 제공하려면 `Scene` 개념이 필수입니다.

---

### 🏛️ 아키텍처 변화: From App to Scene

iOS 12까지는 `AppDelegate`가 앱의 시작과 UI(Window)를 모두 책임졌습니다.
iOS 13부터는 이 둘이 분리되었습니다.

| 역할 | AppDelegate | SceneDelegate (iOS 13+) |
|------|-------------|-------------------------|
| **Process Lifecycle** | 앱 시작/종료 (`launch`, `terminate`) | X |
| **System Event** | 푸시 알림, 메모리 경고 | X |
| **UI Lifecycle** | X (책임 박탈) | 화면 진입/이탈 (`foreground`, `background`) |
| **Connection** | X | 화면(Scene) 생성 및 설정 |

#### 1. 시작 (Launch)
- `@main` 어트리뷰트가 붙은 구조체(SwiftUI `App` 또는 `AppDelegate`)가 엔트리포인트입니다.
- **SwiftUI**: `App` 프로토콜의 `body`에서 최상위 `Scene`을 선언합니다.
- **UIKit**: `application(_:didFinishLaunching...)` 이후 `SceneDelegate`가 연결됩니다.

#### 2. Scene 기반 멀티태스킹
iPadOS와 visionOS에서는 하나의 앱이 여러 개의 창(Scene)을 가질 수 있습니다.
- 사용자가 "새 창 열기"를 하면 새로운 Scene Session이 생성되고, `SceneDelegate`가 하나 더 만들어집니다.
- **주의**: 전역 변수(Singleton)에 UI 상태를 저장하면 모든 창이 똑같은 화면을 보여주는 버그가 생깁니다. 상태는 Scene 단위로 관리해야 합니다.

---

### 🔄 상태 전환 (State Transitions)

앱은 살아있는 생물처럼 상태가 변합니다. 각 상태에 맞춰 자원을 관리해야 합니다.

1.  **Not Running**: 앱이 꺼져 있음.
2.  **Inactive**: 켜져 있지만 터치를 안 받음 (잠깐 전화가 왔거나, 알림 센터 내려옴).
3.  **Active**: 활성화됨. UI 업데이트 가능.
4.  **Background**: 화면에 없지만 코드는 돎. (음악 재생, 위치 추적 등 권한 필요).
5.  **Suspended**: 메모리에는 있지만 CPU는 멈춤. 언제든 삭제(Terminated)될 수 있음.

#### ⚠️ 백그라운드 작업의 골든 타임
앱이 백그라운드로 가면 약 5초~30초 정도의 유예 시간을 줍니다.
- 중요한 데이터 저장은 `sceneDidEnterBackground`에서 **동기(Synchronous)**로, 혹은 `beginBackgroundTask`를 요청해서 안전하게 끝마쳐야 합니다.

```swift
func sceneDidEnterBackground(_ scene: UIScene) {
    // 여기서 비동기(async)로 네트워크 요청하면 앱이 Suspended 되면서 요청이 끊길 수 있음!
    saveDataIdeallySynchronous()
}
```

---

### 📱 UI 프레임워크 생태계

#### SwiftUI (The Future)
- **특징**: 선언형(Declarative). 상태(State)가 바뀌면 뷰가 다시 만들어집니다.
- **장점**: 코드량이 적고, iPad/Mac/Watch 등 멀티플랫폼 대응이 쉽습니다.
- **단점**: OS 버전에 따라 동작이 다르고, 디테일한 제어가 어렵습니다.

#### UIKit / AppKit (The Legacy & Power)
- **특징**: 명령형(Imperative). 뷰 컨트롤러가 뷰를 소유하고 직접 고칩니다.
- **장점**: 15년간 쌓인 라이브러리, 완벽한 제어권.
- **공존**: `UIHostingController`(UIKit 안에 SwiftUI), `UIViewRepresentable`(SwiftUI 안에 UIKit) 통해 점진적 도입이 가능합니다.

### 📚 더 보기
- [[apple-uikit-lifecycle]] - UIViewController의 상세 생명주기
- [[apple-swiftui-deep-dive]] - SwiftUI 렌더링 원리
- [[apple-background-tasks]] - 백그라운드에서 오래 살아남는 법
