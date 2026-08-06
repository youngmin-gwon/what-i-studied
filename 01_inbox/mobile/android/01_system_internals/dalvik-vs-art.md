---
title: dalvik-vs-art
tags: [android, system-internals, dalvik, art, runtime, vm]
aliases: [Dalvik vs ART, Dalvik과 ART 비교]
date modified: 2026-08-06 17:56:00 +09:00
date created: 2026-08-06 17:56:00 +09:00
---

# Dalvik vs ART (안드로이드 런타임 진화 및 비교)

## 1. 개요 (Overview)

Android 런타임은 4.4(KitKat) 버전까지의 레거시 가상 머신인 **[Dalvik VM](dalvik-vm.md)** 에서 Android 5.0(Lollipop) 이후 현대의 **[ART (Android Runtime)](art.md)** 로 대전환을 이루었다.

이 문서에서는 두 런타임의 기술적 차이점, 컴파일 전략의 진화 및 가비지 컬렉션(GC) 메커니즘 차이를 모듈화하여 비교한다.

---

## 2. Dalvik vs ART 핵심 기술 비교표

| 비교 항목 | [Dalvik VM](dalvik-vm.md) (레거시) | [ART (Android Runtime)](art.md) (현대) |
| :--- | :--- | :--- |
| **적용 시기** | Android 1.0 ~ 4.4 | Android 5.0(Lollipop) ~ 현재 |
| **컴파일 방식** | [JIT (Just-In-Time)](../../../computer-science/jit-vs-aot-compilation.md) 위주 런타임 컴파일 | **Profile-Guided [JIT + AOT 컴파일](../../../computer-science/jit-vs-aot-compilation.md) 혼합** |
| **실행 속도** | 실행 시 마다 실시간 번역으로 느림 | **미리 번역된 네이티브 기계어 직접 실행으로 초고속** |
| **CPU / 배터리 효율** | 런타임 컴파일로 CPU 소모 및 전력 소모 큼 | 런타임 컴파일 부하 0 으로 **전력 효율 우수** |
| **가비지 컬렉션** | Stop-the-World (앱 정지 발생) | **Concurrent [Garbage Collection](../../../computer-science/garbage-collection.md) (정지 수ms 이하)** |
| **기본 바이트코드** | [DEX (Dalvik Executable)](android-compilation-pipeline.md) | [DEX (Dalvik Executable)](android-compilation-pipeline.md) |

---

## 3. 런타임 전환 배경과 효과

1. **JIT 런타임 컴파일 병목 해소**:
   - Dalvik 은 앱을 구동할 때마다 반복적으로 바이트코드를 번역하여 CPU 자원을 유연하게 쓰지 못했다. ART 는 유휴 시간에 프로파일링 기반 AOT 컴파일을 수행하여 네이티브 코드로 즉시 구동시킨다.
2. **UI 프레임 드롭(Jank) 예방**:
   - Dalvik 의 Stop-the-World GC 는 화면 렌더링 중 스레드를 멈춰 UI 끊김을 유발했다. ART 의 Concurrent GC 는 스레드 정지 없이 백그라운드 메모리 수거를 달성했다.

---

## 4. 연결 문서 (Related Links)

- [Dalvik VM](dalvik-vm.md) - Dalvik 가상 머신의 독립 정의 노드
- [ART (Android Runtime)](art.md) - 현대 ART 런타임의 독립 정의 노드
- [JIT & AOT 컴파일](../../../computer-science/jit-vs-aot-compilation.md) - JIT 와 AOT 컴파일 방식의 상세 비교
- [DEX (Dalvik Executable)](android-compilation-pipeline.md) - 런타임이 실행하는 압축 바이트코드 포맷
