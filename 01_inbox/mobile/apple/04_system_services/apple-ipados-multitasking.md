---
title: apple-ipados-multitasking
tags: [apple, drag-drop, ipados, multitasking, productivity, scene]
aliases: []
date modified: 2026-04-05 17:45:11 +09:00
date created: 2025-12-16 16:14:02 +09:00
---

## iPadOS Multitasking & Productivity

iPadOS 앱은 단순히 "큰 화면의 아이폰 앱"이 아닙니다.

키보드와 마우스, 그리고 여러 개의 창(Multi-window)을 동시에 다루는 **생산성 도구**여야 합니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **Pro User 경험**: 사용자가 iPad 에서 엑셀 옆에 내 앱을 띄워놓고 사진을 드래그해서 넣고 싶어 합니다. 이걸 지원하지 않는 앱은 "장난감" 취급을 받습니다.
- **State Restoration**: 멀티태스킹 환경에서는 앱이 언제든 메모리에서 내려갔다가(Background) 다시 올라올 수 있습니다. 사용자가 작성 중이던 글이 날아가면 최악의 경험이 됩니다.
- **Desktop Class**: 마우스 포인터(Trackpad) 지원과 키보드 단축키는 선택이 아니라 필수입니다.

---

### 🖥️ 멀티 윈도우와 Scene

#### 1. Scene Cycle

iPadOS 에서는 앱 아이콘을 누를 때마다 새로운 창(Scene)을 만들 수 있습니다.

- **문제**: 싱글톤(`SceneDelegate` 가 아닌 `AppDelegate` 에 UI 상태 저장)을 쓰면 모든 창이 똑같은 화면을 보여주는 버그가 생깁니다.
- **해결**: 모든 UI 상태는 `UIWindowSceneDelegate` 또는 SwiftUI 의 `WindowGroup` 단위로 관리해야 합니다.

#### 2. Stage Manager (스테이지 매니저)

사용자가 창 크기를 자유롭게 조절하고 겹칠 수 있습니다.

- **Responsive Layout**: 화면 크기가 실시간으로 변합니다. 고정 폭 레이아웃을 버리고 `Size Class` 와 `Auto Layout` (혹은 SwiftUI `GeometryReader`)으로 유연하게 대응해야 합니다.

---

### 🤏 Drag & Drop (드래그 앤 드롭)

앱 간 데이터 이동의 핵심입니다. 클립보드(Copy-Paste)의 시각적 버전이라고 보면 됩니다.

#### 1. Drag (주는 쪽)

`NSItemProvider` 에 데이터를 담아 보냅니다.

- 시간이 걸리는 데이터(대용량 파일)는 `FilePromise` 를 사용하여 드롭이 일어난 시점에 전송합니다.

```swift
func dragInteraction(_ interaction: UIDragInteraction, itemsForBeginning session: UIDragSession) -> [UIDragItem] {
    let provider = NSItemProvider(object: image)
    return [UIDragItem(itemProvider: provider)]
}
```

#### 2. Drop (받는 쪽)

받을 수 있는 데이터 타입(UTI)을 선언해야 합니다.

- **Uniform Type Identifier (UTI)**: `public.image`, `public.text`, `com.adobe.pdf` 등 표준 타입을 처리합니다.

```swift
// SwiftUI 예시
Text("Drop Here")
    .onDrop(of: [.image], isTargeted: nil) { providers in
        _ = providers.first?.loadObject(ofClass: UIImage.self) { image, _ in
            // 이미지 처리
        }
        return true
    }
```

---

### ⌨️ 입력 장치 (Input & Pointer)

#### 1. Pointer Interaction

iPad 의 트랙패드 커서는 둥근 원입니다. 버튼 위에 올라가면 자석처럼 붙는 효과(Magnetic effect)가 필요합니다.

- **UIPointerInteraction**: 버튼, 텍스트 등에 "Hover" 효과를 줍니다.

#### 2. Hardware Keyboard

`Command + S` (저장), `Command + F` (검색) 등 표준 단축키를 지원해야 합니다.

- **UIKeyCommand**: 뷰 컨트롤러나 `AppDelegate` 에서 단축키를 정의하면, 사용자가 Command 를 꾹 눌렀을 때 단축키 목록(HUD)에 자동으로 뜹니다.

### 더 보기
- [apple-app-lifecycle-and-ui](../02_ui_frameworks/apple-app-lifecycle-and-ui.md) - Scene 아키텍처 상세
- [apple-platform-differences](../00_foundations/apple-platform-differences.md) - iOS vs iPadOS 레이아웃 전략
