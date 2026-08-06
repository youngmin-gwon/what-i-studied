---
title: android-task-and-app-back-stack-are-different-stacks
tags: [android, android/navigation, android/navigation3]
aliases: ["Android task와 app back stack은 서로 다른 스택이다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android task 와 app back stack 은 서로 다른 스택이다

상위 문서: [Navigation 3 계약](navigation3-contracts.md)

---

### 개념과 두 스택의 계층 분리 (What & Why)

안드로이드 애플리케이션 아키텍처에는 OS 레벨의 **Task Stack**과 앱 레벨의 **App Back Stack (`NavBackStack`)**이라는 두 개의 완전히 다른 스택이 존재한다.

```mermaid
graph TD
    subgraph OS Level Task Stack (ActivityManagerService)
        A["Android Activity Task (PID 1024)"]
        A --> B["Activity A (Single Top)"]
    end
    
    subgraph App Level Navigation 3 Stack (In-Memory Compose State)
        C["NavBackStack<NavKey>"]
        C --> D["[HomeKey, ProductListKey, ProductDetailKey(id=42)]"]
    end

    A -->|"Hosts Single Activity"| C
```

1. **OS Task Stack (Activity Task Stack)**:
   - **소유 주체**: Android OS `ActivityManagerService(AMS)`.
   - **구성 단위**: `Activity` 인스턴스들의 스택.
   - **조작 방식**: `Intent` 플래그(`FLAG_ACTIVITY_NEW_TASK`, `FLAG_ACTIVITY_CLEAR_TOP`) 및 Manifest `launchMode`.
2. **App Back Stack (`NavBackStack`)**:
   - **소유 주체**: 애플리케이션 런타임 (Single Activity 내부 Compose 상태).
   - **구성 단위**: `NavKey` 캡슐화 개체들의 스택.
   - **조작 방식**: Kotlin 컬렉션 함수(`backStack.add()`, `backStack.removeLast()`).

---

### 차이점 및 구시대 레거시 비교

| 구분 | OS Task Stack (Activity 스택) | App Back Stack (`NavBackStack`) |
| :--- | :--- | :--- |
| **관리 단위** | OS 레벨 Heavyweight `Activity` | 앱 레벨 Lightweight Compose `NavKey` |
| **프로세스 메모리** | 각 Activity마다 윈도우/캔버스/뷰 트리 메모리 소모 | 단일 Activity 내 메모리 최소화 뷰포트 상태 |
| **전환 속도** | OS IPC 및 Activity Window Transition 비용 발생 | Compose 컴포지션 차원의 고속 인메모리 트랜지션 |
| **모던 표준 사양** | 1 앱 1 Activity (Single Activity Architecture) 지향 | Activity 내 내부 목적지는 `NavBackStack`으로 전담 처리 |

---

### 관련 상위 및 연관 노트

- 상위 계약: [Navigation 3 계약](navigation3-contracts.md)
- 연관 가이드: [Android Intent 및 IPC 종합 가이드](../../intents-and-deep-links/android-intent-and-ipc.md)
