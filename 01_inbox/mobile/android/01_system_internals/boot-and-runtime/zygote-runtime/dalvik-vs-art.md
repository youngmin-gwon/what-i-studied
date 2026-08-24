---
title: dalvik-vs-art
tags: [android, system-internals, dalvik, art, runtime, vm]
aliases: [Dalvik vs ART, Dalvik과 ART 비교]
date modified: 2026-08-06 17:56:00 +09:00
date created: 2026-08-06 17:56:00 +09:00
---

## Dalvik vs ART (안드로이드 런타임 진화 및 비교)

### 1. 개요 (Overview)

Android 런타임은 4.4(KitKat) 버전까지의 레거시 가상 머신인 **[Dalvik VM](dalvik-vm.md)** 에서 Android 5.0(Lollipop) 이후 현대의 **[ART (Android Runtime)](art.md)** 로 대전환을 이루었다.

이 문서에서는 두 런타임의 기술적 차이점, 컴파일 전략의 진화 및 가비지 컬렉션(GC) 메커니즘 차이를 모듈화하여 비교한다.

---

### 2. Dalvik vs ART 핵심 기술 비교표

| 비교 항목 | [Dalvik VM](dalvik-vm.md) (레거시 가상 머신) | [ART (Android Runtime)](art.md) (현대 관리형 런타임) |
| :--- | :--- | :--- |
| **적용 시기** | Android 1.0 ~ 4.4 (KitKat) | Android 5.0 (Lollipop) ~ 현재 |
| **실행 주체 성격** | **인터프리터 중심 바이트코드 가상 머신(VM)** | **AOT/JIT 하이브리드 네이티브 실행 인프라(Runtime)** |
| **컴파일 방식** | [JIT (Just-In-Time)](../../../../../computer-science/jit-vs-aot-compilation.md) 위주 런타임 컴파일 | **Profile-Guided [JIT + dex2oat AOT 컴파일](../../../../../computer-science/jit-vs-aot-compilation.md) 혼합** |
| **실행 속도** | 실행 시마다 실시간 바이트코드 번역 (느림) | **사전 컴파일된 네이티브 ELF 기계어 직접 실행 (초고속)** |
| **CPU / 배터리 효율** | 기동 시마다 반복 컴파일로 전력 소모 큼 | 런타임 기계어 직접 실행으로 **배터리 소모 대폭 절감** |
| **가비지 컬렉션 (GC)** | Stop-the-World (모든 스레드 정지 10~50ms) | **Concurrent / Generational GC (정지 시간 1~2ms 이하)** |
| **바이너리 산출물** | `classes.dex` | `base.odex` / `base.vdex` / `base.art` (OAT 파일) |
| **기본 바이트코드** | [DEX (Dalvik Executable)](android-compilation-pipeline.md) | [DEX (Dalvik Executable)](android-compilation-pipeline.md) |

---

### 3. 런타임 전환 배경과 효과

1. **JIT 런타임 컴파일 병목 해소**:
   - Dalvik 은 앱을 구동할 때마다 반복적으로 바이트코드를 번역하여 CPU 자원을 유연하게 쓰지 못했다. ART 는 유휴 충전 시간에 프로파일링 기반 AOT 컴파일을 수행하여 네이티브 기계어로 즉시 구동시킨다.
2. **UI 프레임 드롭(Jank) 예방**:
   - Dalvik 의 Stop-the-World GC 는 화면 렌더링 중 스레드를 멈춰 UI 끊김을 유발했다. ART 의 Concurrent GC 는 스레드 정지 없이 백그라운드 메모리 수거를 달성했다.

---

### 4. 연결 문서 (Related Links)

- [Dalvik VM](dalvik-vm.md) - Dalvik 가상 머신의 독립 정의 노드
- [ART (Android Runtime)](art.md) - 현대 ART 런타임의 독립 정의 노드
- [Android Compilation Pipeline](android-compilation-pipeline.md) - 런타임이 구동하는 3단계 컴파일 파이프라인
- [JIT & AOT 컴파일](../../../../../computer-science/jit-vs-aot-compilation.md) - JIT 와 AOT 컴파일 방식의 상세 비교
- [Garbage Collection (GC)](../../../../../computer-science/garbage-collection.md) - ART Concurrent GC 가 수거하는 메모리 관리 메커니즘
- [JDK vs JRE vs JVM 의 차이와 런타임의 본질](../../../../../computer-science/jdk-vs-jre-vs-jvm.md)
