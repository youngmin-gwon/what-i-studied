---
title: 19-serializable
tags: [android, ipc, java, serialization]
aliases: [Java Serializable, Serializable, 직렬화]
date modified: 2026-08-06 17:25:37 +09:00
date created: 2026-08-06 17:25:00 +09:00
---

## Serializable (Java 직렬화)

### 1. Serializable 이란 무엇인가

**`java.io.Serializable`** 은 Java 표준 라이브러리에서 제공하는 **마커 인터페이스(Marker Interface)** 로, 메모리 상에 존재하는 객체의 상태를 바이트 스트림(Byte Stream) 형태로 변환하여 파일에 저장하거나 네트워크/IPC 로 전송할 수 있게 해주는 직렬화 메커니즘이다.

인터페이스 내부에는 구현해야 할 메서드가 없으며, 단지 해당 클래스가 직렬화 가능하다는 라벨(Flag) 역할을 수행한다.

---

### 2. Serializable 의 동작 방식과 단점

#### 1) 리플렉션(Reflection) 기반 자동 처리

- 개발자가 직렬화 로직을 직접 코딩하지 않아도 자바 런타임이 **리플렉션(Reflection)** 기술을 사용하여 객체의 클래스 구조, 필드 타입, 내부 참조 객체들을 자동으로 탐색하고 바이트로 변환한다.

#### 2) Android 환경에서의 단점

- **극심한 런타임 성능 저하**: 리플렉션 탐색 특성상 많은 CPU 연산을 소모한다.
- **가비지 컬렉션(GC) 부담 증가**: 직렬화 과정에서 무수한 임시 객체가 생성되므로 GC 팝업과 프레임 드롭(Jank)의 주원인이 된다.

---

### 3. Parcelable 과의 비교 (Serializable vs Parcelable)

| 구분 | Serializable (Java 표준) | Parcelable (Android 전용) |
| :--- | :--- | :--- |
| **설계 목적** | 범용 Java 객체 저장 및 네트워크 전송 | Android Binder IPC 메모리 고속 전달 |
| **작동 메커니즘** | 런타임 리플렉션(Reflection) 자동 추출 | 개발자/컴파일러 지정 직접 마샬링(Explicit Marshalling) |
| **속도 및 성능** | 상대적으로 매우 둔람 (임시 객체 다수 생성) | **수 배 ~ 수십 배 이상 빠름 (메모리 최적화)** |
| **추천 사용처** | 디스크 파일 저장, 단순 자바 백엔드 통신 | **Android Intent, Bundle, Binder IPC 전송** |

---

### 4. 연결 문서 (Related Links)

- [Parcelable](18-parcelable.md) - Android 에 최적화된 고속 직렬화 레퍼런스
- [Binder IPC](../../../01_system_internals/binder-ipc.md) - Parcelable 객체를 전송하는 안드로이드 백본 IPC
