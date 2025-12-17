---
title: apple-macos-system
tags: [apple, macos, system, sandbox, hardened-runtime, window-server]
aliases: []
date modified: 2025-12-17 23:40:00 +09:00
date created: 2025-12-17 23:40:00 +09:00
---

## macOS System Internals

iOS가 "벽으로 둘러싸인 정원(Walled Garden)"이라면, macOS는 "울타리가 쳐진 광야"입니다.
사용자는 파일 시스템에 자유롭게 접근할 수 있지만, 앱은 **Sandbox**와 **Hardened Runtime**이라는 이중 잠금장치 속에서 동작해야 합니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **Distribution Hell**: "내 맥에서는 되는데 친구 맥에서는 안 켜져요." -> 99% 공증(Notarization)과 Hardened Runtime 문제입니다.
- **Automation**: macOS 앱의 꽃은 AppleScript나 XPC를 통한 "자동화"입니다. 하지만 샌드박스는 다른 앱 제어를 엄격히 막습니다. 이를 푸는 방법(`com.apple.security.scripting-targets`)을 알아야 합니다.
- **Multi-Window**: iOS처럼 Scene 하나만 신경 쓰는 게 아닙니다. 사용자가 창을 50개 띄울 수도 있습니다. `NSWindowController`와 `WindowServer`의 관계를 이해해야 합니다.

---

### 🛡️ Sandbox vs Hardened Runtime

macOS 앱 배포 방식에 따라 보안 모델이 다릅니다.

#### 1. App Sandbox (Mac App Store 필수)
iOS와 똑같습니다. 컨테이너 밖의 파일은 볼 수 없습니다.
- **Entitlements**: `com.apple.security.files.user-selected.read-write`가 있어야 `NSOpenPanel`로 파일을 열 수 있습니다.
- **Network**: `com.apple.security.network.client`가 없으면 소켓 연결 즉시 실패합니다.

#### 2. Hardened Runtime (Notarization 필수)
기본적으로 샌드박스보다 널널하지만, **코드 인젝션 방지**가 핵심입니다.
- **Runtime Integrity**: 디버거(Debugger)가 붙는 것을 막고, 변조된 dylib 로드를 차단합니다.
- **JIT**: 전자(Electron) 앱이나 Java처럼 런타임에 메모리를 실행 가능한 코드로 바꾸려면(`Allow Execution of JIT-compiled Code`) 예외를 신청해야 합니다.

---

### 🖥️ WindowServer (Quartz Compositor)

화면에 그려지는 모든 픽셀을 관리하는 시스템 프로세스입니다.

1. **Core Graphics**: 앱은 자기 윈도우 내용(Backing Store)을 그립니다.
2. **IPC**: 다 그린 버퍼를 WindowServer에게 넘깁니다.
3. **Compositing**: WindowServer는 여러 앱의 윈도우, 그림자, 투명도, 커서 위치를 계산해서 최종 화면을 합성합니다.
4. **Metal/OpenGL**: 합성된 결과는 GPU를 통해 모니터로 쏘아집니다.

**성능 팁**: `CGSGetWindowCount`가 너무 늘어나면 WindowServer CPU 점유율이 폭등합니다. 필요 없는 윈도우는 `orderOut:`으로 숨기세요.

---

### ⌨️ Menu Bar & Application Lifecycle

iOS와 가장 큰 차이점입니다. "창(Window)이 없어도 앱은 살아있을 수 있습니다."

- **NSApplication**: 앱 그 자체입니다.
- **NSWindow**: 화면에 떠 있는 창입니다.
- **Delegate Method**: `applicationShouldTerminateAfterLastWindowClosed`가 `false`(기본값)면, 빨간 버튼(X)을 눌러 창을 다 꺼도 앱은 Dock에 살아있습니다.
- **Menu Bar**: `Main.storyboard`나 코드에서 메뉴 아이템을 관리해야 합니다. Responder Chain을 통해 현재 포커스된 윈도우로 액션(`copy:`, `paste:`)이 전달됩니다.

### 더 보기
- [[apple-build-and-distribution]] - 공증(Notarization) 과정
- [[apple-sandbox-and-security]] - 샌드박스 파일 접근 (Security Scoped Bookmark)
