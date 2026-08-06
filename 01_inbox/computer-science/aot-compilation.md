---
title: aot-compilation
tags: [computer-science, compiler, aot, static-compilation, native-code]
aliases: [AOT, AOT Compilation, Ahead-Of-Time, 정적 컴파일]
date modified: 2026-08-06 17:58:00 +09:00
date created: 2026-08-06 17:58:00 +09:00
---

# AOT Compilation (Ahead-Of-Time 정적 사전 컴파일)

## 1. 개요 (Overview)

**AOT (Ahead-Of-Time / 사전) 컴파일**은 고수준 소스 코드나 중간 바이트코드(Bytecode)를 **프로그램이 실제로 실행되기 전(Before Execution Time)에 대상 타겟 CPU 아키텍처의 네이티브 기계어(Native Machine Code) 바이너리로 미리 번역하는 정적 컴파일 기법**이다.

컴파일 시점에 전체 코드베이스의 의존성과 데이터 타입을 완전히 분석하여 최적화된 기계어를 생성하므로, 런타임에 해석(Interpreting)이나 컴파일 단계 없이 CPU 가 즉시 명령어를 수행한다.

---

## 2. AOT 컴파일의 동작 원리 및 최적화 단계

```mermaid
graph LR
    Source["소스코드 / 바이트코드"] --> Frontend["Compiler Frontend (구문/타입 분석)"]
    Frontend --> Optimizer["Optimizer (LLVM/GCC 기계어 최적화)"]
    Optimizer --> Linker["Linker & Assembler"]
    Linker --> NativeBin["독립 네이티브 바이너리 (.so / .exe / .oat)"]
```

1. **사전 분석 (Static Analysis)**: 프로그램 빌드 타임이나 설치 타임에 전체 제어 흐름 그래프(CFG)와 데이터 타입을 정적으로 분석한다.
2. **공격적 최적화 (Aggressive Optimization)**:
   - **인라이닝 (Inlining)**: 메서드 호출 오버헤드를 줄이기 위해 코드 본문을 직접 삽입.
   - **데드 코드 제거 (Dead Code Elimination)**: 실제 실행될 리가 없는 불필요한 코드 분기 도려내기.
   - **Loop Unrolling / SIMD 벡터화**: CPU 병렬 명령어 집합 활용.
3. **독립 바이너리 패키징**: 타겟 CPU(ARM64, x86_64 등)에 최적화된 기계어 바이너리 파일로 저장한다.

---

## 3. AOT 컴파일의 주요 언어 및 런타임 사례

- **Flutter / Dart (Release Mode)**: 실제 마켓에 배포하는 릴리즈 빌드 시 Dart 코드를 타겟 기기 CPU(ARM64 등) 아키텍처의 네이티브 기계어로 AOT 완전 사전 번역하여 60fps/120fps 의 초고속 프레임을 보장한다.
- **C / C++ (GCC, Clang)**: 가장 대표적인 AOT 언어로 컴파일 타임에 ELF/PE 네이티브 기계어 바이너리를 생성한다.
- **Rust**: LLVM 기반 AOT 컴파일러로 고성능 및 메모리 안전 네이티브 바이너리를 만든다.
- **Go (Golang)**: 가상 머신 없이 전체 런타임을 포함한 단일 AOT 네이티브 바이너리를 출력한다.

---

## 4. AOT 컴파일의 장단점

### 장점
- **최고의 런타임 실행 속도**: 앱이 시작되자마자 100% 네이티브 기계어로 구동되어 초고속 반응성을 발휘한다.
- **런타임 CPU 및 배터리 효율 극대화**: 실행 중 컴파일러가 돌지 않으므로 CPU 전력 소비가 최소화된다.
- **예측 가능한 실시간 성능 (Predictable Latency)**: JIT 처럼 런타임 가열(Warm-up)이나 갑작스러운 컴파일 스파이크 현상이 없다.

### 단점
- **사전 컴파일 타임 및 파일 용량 증가**: 빌드/설치 시간이 오래 걸리고, 네이티브 기계어 보관으로 인해 저장공간(Disk/Flash Memory)을 더 차지한다.
- **타겟 시스템 아키텍처 종속성**: 컴파일된 바이너리가 특정 CPU 아키텍처(ARM64 등)에 고정되므로 크로스 컴파일 관리가 필요하다.

---

## 5. 연결 문서 (Related Links)

- [JIT Compilation](jit-compilation.md) - 런타임에 동적으로 기계어를 번역하는 JIT 방식
- [JIT vs AOT 비교](jit-vs-aot-compilation.md) - JIT 과 AOT 컴파일 이론 종합 비교
- [Android Compilation Pipeline](../mobile/android/01_system_internals/android-compilation-pipeline.md) - Android ART dex2oat 기반 AOT 활용 파이프라인
