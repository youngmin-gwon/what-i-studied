---
title: jit-vs-aot-compilation
tags: [aot, compiler, computer-science, execution-engine, jit]
aliases: [JIT vs AOT, JIT와 AOT 비교, 컴파일 방식 비교]
date modified: 2026-08-06 17:59:44 +09:00
date created: 2026-08-06 17:58:00 +09:00
---

## JIT vs AOT (컴파일 메커니즘 비교)

### 1. 개요 (Overview)

프로그래밍 언어 환경에서 **[JIT Compilation (동적 컴파일)](jit-compilation.md)** 과 **[AOT Compilation (정적 컴파일)](aot-compilation.md)** 은 바이트코드나 소스코드를 기계어로 번역하는 시점과 방식에서 근본적인 차이를 갖는다.

---

### 2. JIT vs AOT 비교표 (CS 종합 이론)

| 비교 항목 | [JIT (Just-In-Time)](jit-compilation.md) | [AOT (Ahead-Of-Time)](aot-compilation.md) |
| :--- | :--- | :--- |
| **번역 시점** | 프로그램 **실행 중 (Runtime)** | 프로그램 **실행 전 (Build / Install Time)** |
| **번역 대상** | 자주 실행되는 **핫스팟 (Hotspot Code)** | 프로그램 **전체 코드베이스** |
| **초기 응답성** | **빠름 (인터프리터로 즉시 실행 시작)** | 파일 읽기 즉시 가능하나 사전 준비 필요 |
| **피크 성능 (Peak Speed)**| Warm-up 가열 타임 필요 | **초기부터 100% 최고 네이티브 속도** |
| **CPU / 배터리 자원** | 런타임 컴파일러 동작으로 CPU/전력 소모 | 런타임 컴파일 CPU 소모 0 (전력 최적) |
| **저장공간 (Disk)** | 바이트코드 위주 (저장공간 절약) | 기계어 바이너리 저장 (공간 더 필요) |
| **대표적 언어/엔진** | V8 (JS), JVM HotSpot, PyPy | C, C++, Rust, Go, Flutter (Release) |

---

### 3. 대표적 하이브리드(Hybrid) 트렌드

현대 고성능 런타임 환경은 단일 방식만을 고집하지 않고 **JIT 과 AOT 를 결합한 하이브리드 파이프라인**을 채택한다.

- **[Android Compilation Pipeline](../mobile/android/01_system_internals/boot-and-runtime/zygote-runtime/android-compilation-pipeline.md)**: 설치 시 인터프리터 ➔ 사용 중 JIT 프로파일링 ➔ 유휴 상태 백그라운드 AOT 컴파일 3 단계 혼합 사용.
- **.NET Core**: AOT(Native AOT)와 JIT(RyuJIT)을 환경 설정에 따라 유연하게 선택 가능.

---

### 4. 연결 문서 (Related Links)

- [JIT Compilation](jit-compilation.md) - JIT 동적 컴파일의 CS 개념 및 원리
- [AOT Compilation](aot-compilation.md) - AOT 정적 컴파일의 CS 개념 및 원리
- [Android Compilation Pipeline](../mobile/android/01_system_internals/boot-and-runtime/zygote-runtime/android-compilation-pipeline.md) - Android 특화 JIT + AOT 3 단계 컴파일 파이프라인
