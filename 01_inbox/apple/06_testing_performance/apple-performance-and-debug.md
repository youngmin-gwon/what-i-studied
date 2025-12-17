---
title: apple-performance-and-debug
tags: [apple, debugging, performance, optimization, metrics, swiftui, uikit]
aliases: []
date modified: 2025-12-18 02:20:00 +09:00
date created: 2025-12-16 16:10:22 +09:00
---

## Performance & Debugging Deep Dive

"앱이 느리다"는 사용자의 불만은 대부분 **숫자(Number)**가 아니라 **느낌(Feeling)**에서 옵니다.
엔지니어는 0.1초를 줄이는 것보다, 0.1초 동안 "멈춘 느낌"을 주지 않는 것에 집중해야 합니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **Perceived Performance (인지된 성능)**: 앱 실행이 3초 걸려도 스플래시 화면 애니메이션이 부드럽다면 "빠르다"고 느낍니다. 반면 1초가 걸려도 버튼을 눌렀는데 UI가 0.2초간 먹통이 되면(Hitch) "버벅거린다"고 느낍니다.
- **Main Thread is Sacred**: 메인 스레드는 16ms(60Hz)마다 화면을 다시 그려야 합니다. 여기서 JSON 파싱하느라 50ms를 쓰면, 그동안 화면은 멈춥니다(Frame Drop).
- **Cold vs Warm Launch**: 사용자는 앱을 처음 켤 때(Cold)와 나갔다 들어올 때(Warm)의 속도 차이를 민감하게 느낍니다.

---

### 🚀 Optimization Targets

#### 1. App Launch (앱 실행 속도)
- **목표**: 400ms 이내에 첫 화면 렌더링.
- **범인**: `AppDelegate`의 `didFinishLaunching`에서 하는 무거운 초기화 작업. 서드파티 SDK 초기화는 비동기(`DispatchQueue.global`)로 미룰 수 있는지 확인하세요.
- **dyld**: 동적 라이브러리가 너무 많으면(50개 이상) 로딩이 느려집니다. 정적 라이브러리(Static Library)로 합치는 것을 고려하세요.

#### 2. Smooth Scrolling (Hitch Ratio)
- **목표**: 60fps (16.67ms) 또는 120fps (8.33ms) 유지.
- **범인**: 셀을 그릴 때(`cellForRow`) 일어나는 오토레이아웃 계산, 그림자 그리기(Offscreen Rendering), 이미지 리사이징.

---

### 🚅 UI Performance Best Practices

#### SwiftUI
SwiftUI는 선언형이기 때문에 "Diffing(비교)" 비용을 줄이는 것이 핵심입니다.
1. **State 줄이기**: `@State`나 `@EnvironmentObject`가 변경되면, 이를 의존하는 **모든** 뷰의 `body`가 다시 계산됩니다. 상태를 최하위 뷰로 내리세요(Push State Down).
2. **Stable ID**: `ForEach`에서 `id: \.self`를 피하세요. 데이터가 조금만 바뀌어도 전체를 다시 그릴 수 있습니다. 고유한 ID(`UUID`)를 사용하세요.
3. **Expensive Task**: `body` 프로퍼티 안에서는 절대 무거운 작업(초기화, 데이터 가공)을 하지 마세요. `body`는 초당 수십 번 호출될 수 있습니다.

#### UIKit
1. **Cell Reuse**: `dequeueReusableCell`은 필수입니다. 셀을 매번 `init`하면 스크롤은 멈춥니다.
2. **Auto Layout**: 제약 조건(Constraints)이 너무 많으면(뷰 하나에 50개 이상) 계산 비용이 기하급수적으로 늘어납니다. 복잡한 셀은 `layoutSubviews`에서 프레임을 직접 계산하는 것이 더 빠를 수 있습니다.
3. **ShadowPath**: 그림자는 가장 비싼 효과 중 하나입니다. `shadowPath`를 지정해 GPU가 픽셀 분석을 하지 않게 하세요.

---

### 🛠️ Debugging Tools (The Arsenal)

Xcode에는 강력한 무기들이 내장되어 있습니다. `print()`로 디버깅하는 습관을 버리세요.

#### 1. View Debugger
"이 뷰 왜 안 보이지?"
- 3D 뷰 계층 구조를 보여줍니다. 뷰가 가려졌는지, 크기가 0인지, `isHidden`인지 바로 알 수 있습니다.

#### 2. Memory Graph Debugger
"앱을 껐다 켜면 메모리가 계속 늘어나요."
- **Retain Cycle**을 시각적으로 보여줍니다. 보라색 느낌표(!)를 찾아보세요. 객체 간의 참조 관계 화살표를 따라가면 누가 안 놔주고 있는지 범인이 보입니다.

#### 3. Network Link Conditioner
"LTE 터질 때 테스트해보셨나요?"
- 개발자 설정에서 네트워크 환경을 `High Latency DNS`, `Edge`, `100% Loss` 등으로 시뮬레이션할 수 있습니다. 로딩 인디케이터나 에러 처리를 검증할 때 필수입니다.

### 더 보기
- [[apple-instruments-profiling]] - 범인을 잡는 정밀 분석 도구
- [[apple-rendering-and-media]] - 그래픽 파이프라인 심화
