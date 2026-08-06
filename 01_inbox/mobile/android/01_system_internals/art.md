---
title: art
tags: [android, art, runtime, system-internals, vm]
aliases: []
date modified: 2026-08-06 16:37:29 +09:00
date created: 2026-08-06 16:31:22 +09:00
---

## ART (Android Runtime)

### 1. 개요 (Overview)

**ART (Android Runtime)** 는 안드로이드 운영체제에서 애플리케이션과 시스템 서비스를 구동하는 관리형 런타임(Managed Runtime) 환경입니다.

기존의 **Dalvik 가상 머신(Dalvik VM)** 을 대체하기 위해 안드로이드 4.4(KitKat)에 실험적으로 도입되었고, **안드로이드 5.0(Lollipop)** 부터 안드로이드의 기본 런타임으로 전면 적용되었습니다. ART 는 바이트코드 해석 방식 및 컴파일 전략을 크게 개선하여 안드로이드 앱의 실행 속도와 전력 효율을 대폭 끌어올렸습니다.

---

### 2. 핵심 컴파일 전략 (Compilation Strategies)

#### ① Dalvik VM vs ART

- **Dalvik VM**: 앱 실행 중에 바이트코드를 실시간으로 기계어로 번역하는 **JIT (Just-In-Time)** 컴파일 위주로 동작하여 실행 시 CPU 부하가 높았습니다.
- **ART 초기 (Android 5.0~6.0)**: 앱 설치 시점에 DEX 바이트코드를 기계어 바이너리로 완전 컴파일하는 **AOT (Ahead-Of-Time)** 컴파일 방식을 채택했습니다. (설치 시간이 길고 용량을 많이 차지하는 단점 발생)

#### ② 현대 ART 의 혼합 컴파일 구조 (JIT + AOT + Profile-Guided Compilation)

안드로이드 7.0(Nougat) 이후의 ART 는 JIT 와 AOT 의 장점을 결합한 최적화 컴파일 모델을 도입했습니다.

1. **앱 설치 직후**: 빠르게 설치를 완료하기 위해 컴파일 없이 DEX 바이트코드 형태로 저장하고, 실행 시 **JIT 컴파일러**가 동작합니다.
2. **프로파일링 (Profiling)**: 앱을 사용하는 동안 자주 실행되는 핫코드(Hot Code) 영역을 감지하고 프로파일 파일(`.prof`)에 기록합니다.
3. **충전 및 대기 상태 (Background AOT 컴파일 - `dex2oat`)**: 기기가 충전 중이거나 유휴 상태일 때, 수집된 프로파일 데이터를 기반으로 핫코드 영역만 선별하여 **AOT 기계어**로 미리 컴파일합니다.
4. **결과**: 빠른 설치 속도, 적은 용량 차지, 잦은 사용 코드의 극대화된 실행 성능을 모두 달성했습니다.

---

### 3. DEX 바이트코드 실행 (DEX Bytecode Execution)

- 안드로이드 앱은 자바/코틀린 소스코드가 컴파일되어 일반 Java Class 파일(`.class`)이 아닌, 안드로이드 전용 압축 바이트코드 포맷인 **DEX (Dalvik Executable, `.dex`)** 파일로 변환됩니다.
- ART 는 이 DEX 바이트코드를 읽어 내장 해석기(Interpreter) 및 JIT/AOT 컴파일러(`dex2oat`)를 통해 디바이스 CPU 아키텍처(ARM, x86 등)에 최적화된 기계어로 실행합니다.

---

### 4. 가비지 컬렉션 최적화 (Garbage Collection, GC)

Dalvik VM 시절의 GC 는 앱 실행을 멈추게 하는 "Stop-The-World" 현상으로 인해 프레임 드랍(UI 끊김 현상)의 주원인이었습니다. ART 는 GC 구조를 혁신하여 이를 대폭 개선했습니다.

- **동시 가비지 컬렉션 (Concurrent GC)**: 메모리 해제 작업 대부분을 앱 스레드 정지 없이 백그라운드에서 동시 처리하여 GC 로 인한 일시정지 시간을 최소화합니다.
- **메모리 단편화 감소 (Compacting GC)**: 백그라운드 상태일 때 메모리 조각화(Fragmentation)를 정리하여 연속된 메모리 공간을 확보합니다.
- **메모리 할당 최적화**: 소형 객체 할당 속도를 크게 개선하여 GC 발생 빈도를 줄입니다.

---

### 5. 연관 개념 (Related Notes)

- [Linux Kernel](../../../operating-systems/linux-kernel.md) - ART 런타임 프로세스가 작동하는 하위 OS 커널 기반
- [HAL (Hardware Abstraction Layer)](hal.md) - ART 환경 위에서 동작하는 프레임워크가 하드웨어를 제어할 때 경유하는 추상화 계층
- [Zygote](zygote.md) - ART 가상 머신 인스턴스를 미리 메모리에 올려두고 앱 프로세스를 빠른 fork 로 띄워주는 마스터 프로세스
- [system_server](../04_system_services/system-server.md) - ART 런타임 위에서 동작하는 안드로이드 핵심 시스템 서비스 프로세스
