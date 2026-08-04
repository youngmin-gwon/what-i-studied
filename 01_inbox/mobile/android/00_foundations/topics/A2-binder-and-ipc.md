---
title: A2-binder-and-ipc
tags: [android, system-internals, binder, ipc, topic-synthesis]
aliases: [Binder IPC, Android IPC Topic]
date created: 2026-08-04 16:00:00 +09:00
date modified: 2026-08-04 16:00:00 +09:00
---

## A2 · Binder 와 IPC 완전 이해

> **이 문서의 목적**: Android 가 왜 Binder 를 IPC 메커니즘으로 선택했는지, Binder 트랜잭션이 어떻게 동작하는지, AIDL 이 그 위에서 무슨 역할을 하는지를 단일 흐름으로 이해한다. Android 의 모든 시스템 서비스 호출, 컴포넌트 통신, 권한 검사가 이 메커니즘 위에 서 있다.

---

### 이 주제를 읽기 전에

| 선행 개념 | 필요한 이유 |
|---|---|
| Linux 프로세스 모델 (PID, UID, 메모리 격리) | Binder 가 해결하는 문제의 배경 |
| Android 부팅 흐름 (SystemServer, ServiceManager) | Binder 위에 올라가는 시스템 서비스 구조 |
| SELinux 기초 | Binder 보안 정책 이해 |

관련 토픽: [A1 · 부팅과 프로세스 생성](./A1-boot-and-process.md) · [B1 · 컴포넌트 생명주기](./B1-component-lifecycle-and-task.md)

---

### 전체 조망도

```
[Client Process]
    │
    │  handle → IBinder proxy
    │
    ▼
[Binder Driver (/dev/binder)]  ← 커널 공간
    │  single-copy mmap
    │  caller UID/PID 주입
    │  object reference 중재
    ▼
[Server Process]
    │  Binder thread pool 에서 onTransact()
    │
    ▼
  reply → caller 로 반환

[ServiceManager] : "이름 → IBinder handle" 레지스트리
```

**핵심**: Binder 의 차별점은 byte stream 이 아니라 **커널이 중재하는 객체 참조(capability)** 다. 권한 검사, 신원 확인, 프로세스 간 메모리 전달이 모두 커널 드라이버 수준에서 이루어진다.

---

### 1. IPC 가 왜 필요한가

Android 의 모든 앱은 독립된 Linux 프로세스로 실행되고 서로의 메모리에 직접 접근할 수 없다. 그러나 앱은 카메라, 위치, 알림, 네트워크 같은 시스템 서비스를 사용해야 하고, 서비스들도 서로 협력해야 한다.

Binder 는 이 문제를 byte stream(소켓) 이 아닌 **원격 객체 참조** 로 해결한다. client 는 마치 로컬 객체처럼 메서드를 호출하고, 커널 드라이버가 실제 데이터 복사와 thread scheduling 을 처리한다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [Binder 는 객체 참조를 커널이 중재하는 capability IPC 다](../../01_system_internals/ipc-and-process/ipc-process-contracts/binder-is-kernel-mediated-object-capability-ipc.md) | byte stream 이 아닌 객체 capability 모델 |

---

### 2. Binder 트랜잭션 수명 (call → copy → dispatch → reply)

동기 Binder 호출의 4단계:

1. **Call**: client 가 `IBinder.transact()` 로 Parcel 데이터를 드라이버에 전달
2. **Copy (single-copy)**: 드라이버가 server 프로세스의 mmap 버퍼로 데이터를 1회 복사. 기본 수신 버퍼 크기는 약 1MB - 8KB (1016KB)
3. **Dispatch**: server 의 Binder thread pool 에서 `onTransact()` 실행
4. **Reply**: 결과가 역방향으로 caller 에게 반환되고, caller thread 가 차단 해제

이 구조 때문에 Binder 비용은 단순 함수 호출 비용이 아니다. thread scheduling, buffer copy, parcel marshaling, callee 작업 시간, reply 대기 시간이 모두 caller 지연으로 관찰된다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [Binder transaction lifetime 은 call, copy, dispatch, reply 로 나뉜다](../../01_system_internals/ipc-and-process/ipc-process-contracts/binder-transaction-lifetime-is-call-copy-dispatch-and-reply.md) | single-copy mmap 구조와 4단계 흐름 |

---

### 3. Binder 스레드 풀과 동시성 경계

각 프로세스는 들어오는 Binder 트랜잭션을 처리하는 **Binder thread pool** 을 가진다. 기본 최대 스레드 수는 15개다. 이 풀이 모두 차면 새 트랜잭션은 대기하고, caller 는 차단된다.

**교착(Deadlock) 주의**: service A 가 service B 를 동기 호출하고, B 가 다시 A 를 동기 호출하는 구조는 thread pool 과 lock 순서에 따라 멈출 수 있다. Binder API 설계 시 call graph 전체를 검토해야 한다.

**oneway 호출**: AIDL 메서드에 `oneway` 를 붙이면 caller 가 reply 를 기다리지 않는다. 그러나 server 의 thread pool 과 queue 는 그대로 존재한다. `oneway` 는 caller latency 를 줄이는 도구이지 무제한 이벤트 버스가 아니다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [Binder thread pool 은 service concurrency 와 deadlock 경계다](../../01_system_internals/ipc-and-process/ipc-process-contracts/binder-thread-pool-is-service-concurrency-and-deadlock-boundary.md) | pool 크기, 교착 조건, 설계 원칙 |
| [oneway Binder 는 caller 대기를 없애지만 server backpressure 를 없애지 않는다](../../01_system_internals/ipc-and-process/ipc-process-contracts/oneway-binder-removes-caller-waiting-not-server-backpressure.md) | FLAG_ONEWAY 의 의미와 한계 |

---

### 4. AIDL: 프로세스 경계 계약 정의

AIDL(Android Interface Definition Language) 은 client proxy 와 server stub 코드를 자동 생성해 Binder 트랜잭션의 형식을 맞춰주는 인터페이스 선언 언어다. `.aidl` 파일을 컴파일하면 Kotlin/Java 용 Proxy(client 쪽)와 Stub(server 쪽) 클래스가 생성된다.

AIDL 은 **프로세스 경계의 호출 모양을 고정**하지만, retry, idempotency, authorization, version 호환성은 별도로 설계해야 한다. 앱 내부 모듈 간 단순 추상화에 AIDL 을 도입하면 오히려 오버헤드와 실패 모드가 늘어난다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [AIDL 은 process boundary 계약이지 비즈니스 프로토콜이 아니다](../../01_system_internals/ipc-and-process/ipc-process-contracts/aidl-defines-process-boundary-contract-not-business-protocol.md) | AIDL 적합 범위와 설계 책임 범위 |

---

### 5. 관찰 가능한 신호와 IPC 디버깅

IPC 문제는 "호출이 실패했다"에서 시작해 원인을 단계적으로 좁혀야 한다:

1. **서비스가 등록됐는가?** → `adb shell service list`
2. **caller 가 handle 을 얻었는가?** → `adb shell service check <서비스명>`
3. **권한이 통과했는가?** → logcat 에서 `SecurityException`, SELinux denial(`avc: denied`)
4. **Binder thread 가 막혔는가?** → `/proc/binder/` 또는 `dumpsys activity --binder-ids`
5. **callee process 가 살아있는가?** → `adb shell ps -A | grep <프로세스명>`

```bash
# 등록된 서비스 목록
adb shell service list

# Binder 통계
adb shell cat /proc/binder/stats
adb shell cat /proc/binder/state

# ANR trace (Binder 교착 포함)
adb shell dumpsys activity processes

# SELinux denial 확인
adb shell logcat -b all | grep "avc: denied"
```

| 원자 노트 | 핵심 명제 |
|---|---|
| [IPC 디버깅은 service 등록, call path, thread state 에서 시작한다](../../01_system_internals/ipc-and-process/ipc-process-contracts/ipc-debugging-starts-from-service-registration-call-path-and-thread-state.md) | 4단계 triage 흐름과 진단 명령어 |

---

### 이 주제와 연결된 Worked Example

| Worked Example | 연결 포인트 |
|---|---|
| [WE 01 · App Icon Tap to First Frame](../worked-examples/01-app-icon-tap-to-first-frame.md) | AMS → Zygote Binder 통신, ActivityThread attach |

---

### 이 주제와 연결된 Diagnostic Runbook

| Runbook | 연결 포인트 |
|---|---|
| [RB 02 · ANR](../diagnostic-runbooks/02-anr.md) | Binder thread pool 고갈, 동기 Binder 블로킹 |
| [RB 01 · 앱 실행 느리거나 실패](../diagnostic-runbooks/01-app-launch-slow-or-fails.md) | AMS-Zygote Binder 호출 지연 |

---

### 더 깊이 들어갈 때 (Learning Spine)

- **Chapter 01 · Android Platform Overview** — SystemServer 와 ServiceManager 구조 서사
- **Chapter 08 · Security** — Binder 권한 검사, SELinux binder policy, caller UID 활용
