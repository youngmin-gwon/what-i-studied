---
title: dalvik-vm
tags: [android, dalvik, runtime, system-internals, vm]
aliases: [Dalvik VM, Dalvik 가상 머신, 달빅]
date modified: 2026-08-06 18:00:24 +09:00
date created: 2026-08-06 17:55:00 +09:00
---

## Dalvik VM (Dalvik 가상 머신)

### 1. 개요 (Overview)

**Dalvik VM (Dalvik 가상 머신)** 은 Android 4.4(KitKat) 이하 버전까지 안드로이드 플랫폼의 기본 애플리케이션 실행 런타임으로 사용되었던 모바일 전용 가상 머신이다.

초기 모바일 기기의 제한된 RAM 과 CPU 성능 환경에 최적화하여 개발되었으며, 표준 Java 가상 머신(JVM)의 스택 기반(Stack-based) 구조와 달리 **레지스터 기반(Register-based) 구조**로 설계되었다.

Android 5.0(Lollipop)부터는 성능과 전력 효율성이 월등한 [ART (Android Runtime)](art.md) 로 완전히 대체되었다.

---

### 2. Dalvik VM 의 핵심 특성과 동작 원리

1. **레지스터 기반 구조 (Register-based Architecture)**:
   - 일반 JVM 이 스택 피셔(Stack Pushing/Popping) 방식으로 작동하는 반면, Dalvik 은 레지스터에 직접 명령을 전달한다.
   - 명령어 수가 줄어들어 실행 바이트코드 파일([DEX](android-compilation-pipeline.md)) 크기가 줄어들고 메모리 효율성이 뛰어났다.
2. **JIT (Just-In-Time) 컴파일 위주 동작**:
   - 앱이 실행되는 동안 [DEX 바이트코드](android-compilation-pipeline.md)를 실시간 인터프리팅(Interpreting)하다가, 자주 실행되는 핫코드(Hot Code)만 [JIT 컴파일](../../../computer-science/jit-compilation.md) 로 기계어로 바꿔 실행했다.
3. **Stop-the-world GC**:
   - 가비지 컬렉션이 구동되는 동안 앱 실행 스레드가 전면 정지되어 화면이 버벅이는 프레임 드롭(Jank)이 빈번했다.

---

### 3. Dalvik 과 ART 의 비교

Dalvik VM 과 현대 ART 런타임의 기술적 차이점 및 전환 배경은 독립된 [Dalvik vs ART 비교 문서](dalvik-vs-art.md) 를 참고한다.

---

### 4. 연결 문서 (Related Links)

- [Dalvik vs ART 비교](dalvik-vs-art.md) - Dalvik 과 ART 의 런타임 기술 세부 비교
- [ART (Android Runtime)](art.md) - Dalvik VM 을 대체한 차세대 안드로이드 런타임
- [DEX (Dalvik Executable)](android-compilation-pipeline.md) - Dalvik 이 실행하는 압축 바이트코드 포맷
- [JIT & AOT 컴파일](../../../computer-science/jit-vs-aot-compilation.md) - JIT 와 AOT 컴파일 방식 비교
- [Garbage Collection](../../../computer-science/garbage-collection.md) - 메모리를 수거하는 런타임 가비지 컬렉터
