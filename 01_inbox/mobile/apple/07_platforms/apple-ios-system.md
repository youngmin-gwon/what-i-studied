---
title: apple-ios-system
tags: [apple, ios, jetsam, memory, springboard, system]
aliases: []
date modified: 2026-04-05 17:46:25 +09:00
date created: 2025-12-17 23:30:00 +09:00
---

## iOS System Internals

iOS 는 "제약의 예술"입니다.

사용자에게 최고의 반응성을 제공하기 위해, 시스템은 앱에게 가혹할 정도로 엄격한 메모리/CPU 제한을 둡니다.

이 규칙을 집행하는 **SpringBoard**와 **Jetsam**을 이해해야 앱이 죽지 않고 살아남을 수 있습니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **OOM (Out Of Memory)**: "메모리 경고도 안 받고 그냥 꺼졌어요." -> 100% Jetsam 이 죽인 겁니다. Jetsam 이 누구를 먼저 죽이는지(Priority) 알아야 방어할 수 있습니다.
- **Touch Responsiveness**: 사용자가 화면을 터치했을 때, 그 이벤트가 내 버튼에 도달하기까지의 여정(IOKit -> SpringBoard -> App)을 알면 "터치 씹힘" 현상을 분석할 수 있습니다.
- **Background Execution**: "유튜브는 백그라운드 재생 되는데 왜 내 앱은 안 돼요?" -> iOS 의 백그라운드 정책은 철저한 허가제입니다.

---

### 📱 SpringBoard (The Shell)

Mac 에 `Finder` 와 `WindowServer` 가 있다면, iOS 에는 **SpringBoard**가 있습니다.

홈 화면을 보여주는 앱처럼 보이지만, 실제로는 **iOS 의 Window Manager 이자 Process Manager**입니다.

#### 역할
1. **App Launch**: 앱 아이콘을 누르면 `runningboardd` 에 요청하여 앱 프로세스를 포크(fork)하고 실행합니다.
2. **Window Management**: 모든 앱의 UIWindow 는 사실 SpringBoard 가 관리하는 캔버스 위에 그려집니다. (Inter-process communication via Render Server)
3. **Event Routing**: 하드웨어 터치 이벤트를 받아서 현재 활성화된 앱으로 전달합니다.

---

### 🧹 Jetsam (The Reaper)

iOS 는 스왑(Disk Swap)이 없습니다. 메모리가 부족하면 누군가를 죽여야 합니다. 이 저승사자가 바로 **Jetsam**입니다.

#### Jetsam Priority Queue

레드 넷플릭스 게임(오징어 게임)과 비슷합니다. 우선순위가 낮은 순서대로 죽습니다.

1. **Background Suspended**: 백그라운드에 있는데 아무 일도 안 하는 앱. (가장 먼저 사망 💀)
2. **Background Running**: 음악 재생, 위치 추적 중인 앱.
3. **Foreground Inactive**: 전화가 와서 잠깐 멈춘 상태.
4. **Foreground Active**: 사용자가 지금 쓰고 있는 앱. (여기까지 죽으면 시스템 리부팅)
5. **System Services**: SpringBoard, telephony 등.

**방어 전략**:

- `applicationDidEnterBackground` 에서 5 초 안에 모든 작업을 끝내고 메모리를 최대한 비우세요. 그래야 Suspended 상태에서 오래 살아남습니다.

---

### 👆 Touch Event Loop

터치가 발생해서 `UIButton.action` 이 불리기까지의 과정:

1. **Hardware (Capacitive Sensor)**: 전압 변화 감지.
2. **IOKit (Kernel)**: 하드웨어 인터럽트를 `IOHIDEvent` 로 변환.
3. **SpringBoard (Backboardd)**: 이벤트를 받아서 "지금 켜져 있는 앱이 누구지?" 판단.
4. **IPC (Mach Message)**: 앱의 메인 런루프로 메시지 전달.
5. **UIKit (`UIApplication`)**: `UIEvent` 객체 생성.
6. **Hit Testing**: `window.hitTest()` -> `view.pointInside()` 재귀 호출로 터치된 뷰 찾기.
7. **Responder Chain**: 버튼이 처리 안 하면 상위 뷰로 전달.

### 더 보기
- [apple-app-lifecycle-and-ui](../02_ui_frameworks/apple-app-lifecycle-and-ui.md) - 앱 생명주기
- [apple-memory-management](../01_language_concurrency/apple-memory-management.md) - 메모리 관리 기법
