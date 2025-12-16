# App Lifecycle & UI #apple #uikit #swiftui #lifecycle

앱이 켜지고, 화면이 뜨고, 백그라운드로 가는 흐름을 쉽게 정리했다. 용어는 [[apple-glossary]].

## 시작
- 아이콘 탭 → SpringBoard가 프로세스 생성 → [[apple-glossary#dyld|dyld]] 로드 → @main에서 Run Loop 시작.
- SwiftUI: `App` 프로토콜의 `body`에서 Scene을 선언.
- UIKit: `UIApplicationDelegate`의 `application(_:didFinishLaunchingWithOptions:)` 호출 후 `UIWindow`/rootViewController 설정.

## Scene 기반(멀티 윈도우)
- iOS13+/iPadOS/visionOS: `UISceneDelegate`가 창 생명주기(`sceneWillEnterForeground` 등)를 관리.
- iPadOS/visionOS/Stage Manager는 여러 창을 동시에 띄울 수 있다. 각 Scene마다 별도 상태 저장 필요.

## 상태 전환
- Active ↔ Inactive ↔ Background ↔ Suspended.
- Background에서 짧은 시간만 코드 실행 가능. 허용된 [[apple-glossary#Background Modes|백그라운드 모드]]가 아니면 중지된다.
- 메모리 압박 시 `applicationDidReceiveMemoryWarning`/SwiftUI Task 취소 등을 받아 자원 해제.

## UI 프레임워크
- SwiftUI: 선언형, 상태 기반. `@State`, `@StateObject`, `@Environment`로 데이터 흐름을 표현.
- UIKit/AppKit: 명령형, 뷰 컨트롤러 패턴. Auto Layout/Storyboard/XIB 또는 코드로 작성.
- 공존: UIHostingController(UIKit 안에 SwiftUI), UIViewRepresentable(SwiftUI 안에 UIKit)로 섞을 수 있다.

## 입력·애니메이션
- 메인 Run Loop가 터치/제스처를 받아 뷰에 전달한다.
- Core Animation/SwiftUI Transaction이 애니메이션을 GPU 친화적으로 수행한다.
- watchOS/visionOS는 입력(디지털 크라운/제스처/시선) 특성이 다르다.

## 확장(Extension)
- WidgetKit(홈/잠금/스마트 스택/다이내믹 아일랜드), Live Activity, Share extension, Intents(Siri/Shortcuts), Safari Web Extension 등이 있다.
- 각 확장은 별도 .appex 프로세스이며, 메모리/시간 예산이 작다.

## 상태 보존/복원
- UIKit: `stateRestorationActivity`/`NSUserActivity`, Scene delegate의 `stateRestorationActivity(for:)`.
- SwiftUI: `@SceneStorage`, `@AppStorage`, App/Scene phase 감지.

## 접근성
- VoiceOver, Dynamic Type, 컬러 필터, Reduced Motion을 지원해야 심사에서 유리하다. [[apple-accessibility-and-internationalization]] 참고.

## 링크
[[apple-foundations]], [[apple-sandbox-and-security]], [[apple-rendering-and-media]], [[apple-performance-and-debug]], [[apple-platform-differences]].
