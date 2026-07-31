---
title: 04-hal-hidl-aidl-2019
tags: []
aliases: []
date modified: 2026-07-31 15:40:54 +09:00
date created: 2026-07-31 15:38:23 +09:00
---

## HAL: HIDL → AIDL (2019+)

상위 노트: [02-주요-기술-전환](01_inbox/mobile/android/00_foundations/history/android-evolution-history/02-%EC%A3%BC%EC%9A%94-%EA%B8%B0%EC%88%A0-%EC%A0%84%ED%99%98.md)

**HIDL (Hardware Interface Definition Language, 2017)**:

```cpp
// HIDL (C++ 전용)
interface ICameraDevice {
    open(ICameraDeviceCallback callback) generates (Status status);
};
```

**문제**:

- C++ 만 지원
- 복잡한 문법
- 버전 관리 어려움

**AIDL HAL (2019+)**:

```java
// AIDL (다중 언어)
interface ICameraDevice {
    void open(in ICameraDeviceCallback callback);
}
```

**장점**:

- Java/Rust 도 지원
- 간단한 문법 (기존 AIDL 과 유사)
- 더 나은 버전 호환성
