---
title: android-binder-and-ipc
tags: [android, internals, binder, ipc, aidl]
aliases: [Binder IPC, 안드로이드 바인더]
date modified: 2025-12-18 05:40:00 +09:00
date created: 2025-12-16 15:22:42 +09:00
---

# Binder: The Nervous System of Android

안드로이드의 모든 시스템 서비스(ActivityManager, PackageManager 등)와 앱 간의 대화는 **Binder**를 통해 이루어집니다.
Binder가 없으면 안드로이드는 뇌(System Server)와 팔다리(App)가 끊어진 시체와 같습니다.

## 💡 Why it matters (Context)

-   **Performance**: 리눅스 전통적인 IPC(Pipe, Socket)는 데이터 복사가 2번(User -> Kernel -> User) 일어납니다. Binder는 **1번(User -> Kernel -> mmap된 User)**만 복사합니다. 이 차이가 60fps 터치 반응성을 결정합니다.
-   **Security**: Binder 커널 드라이버는 호출자의 `UID`와 `PID`를 수신자에게 강제로 주입합니다. 앱이 system_server를 속이는 것은 불가능합니다.
-   **TransactionTooLargeException**: Binder 버퍼는 프로세스당 **1MB**로 제한됩니다. 이 제한을 이해해야 "Intent에 큰 비트맵 넣었다가 크래시 나는" 초보 실수를 막을 수 있습니다.

---

## ⚙️ Binder Internals

### 1. The Architecture
Binder는 단순한 직렬화 라이브러리가 아닙니다. **커널 드라이버(`/dev/binder`)**입니다.

1.  **Client**: `transact()` 호출. 스레드는 블로킹(Blocking)됩니다.
2.  **Kernel Driver**:
    -   데이터를 **Sender**의 메모리에서 **Binder Buffer**로 딱 한 번 복사(Copy)합니다.
    -   이 버퍼는 **Receiver**의 주소 공간에 이미 매핑(`mmap`)되어 있습니다. 따라서 Receiver는 복사 없이 데이터를 읽을 수 있습니다.
3.  **Server (Receiver)**: `onTransact()` 호출. 미리 만들어둔 **Binder Thread Pool**의 스레드 하나가 깨어나서 일을 처리합니다.

### 2. Thread Pool Model
모든 앱 프로세스는 시작 시 Binder Thread Pool(기본 16개 스레드)을 만듭니다.
-   "앱이 멈췄어요 (ANR)"의 다른 원인: **Binder 스레드가 모두 바빠서** 시스템이 보낸 터치 이벤트를 처리 못한 경우일 수 있습니다.
-   `ps -T`로 보면 `Binder:1234_1`, `Binder:1234_2` 같은 스레드들이 보입니다.

---

## 🛠️ AIDL (Android Interface Definition Language)

복잡한 Binder 통신 코드를 자동으로 짜주는 도구입니다.

```java
// IRemoteService.aidl
interface IRemoteService {
    void doSomething(int aString);
    oneway void notificationOnly(); // 응답 안 기다림 (Non-blocking)
}
```

-   **Stub**: 서버 쪽 구현체. `onTransact()`를 처리합니다.
-   **Proxy**: 클라이언트 쪽 구현체. `transact()`를 호출합니다.
-   **oneway**: 매우 중요! 이 키워드를 붙이면 클라이언트는 서버의 처리를 기다리지 않고 즉시 리턴합니다. (비동기 호출)

---

## 🚨 Common Pitfalls

### 1. TransactionTooLargeException
-   **원인**: Binder 트랜잭션 버퍼(1MB) 초과. 이 1MB는 **현재 진행 중인 모든 트랜잭션**이 공유합니다.
-   **해결**: 이미지를 전달할 때는 `ContentProvider` URI를 넘기거나, 파일 디스크립터(`ParcelFileDescriptor`)를 쓰세요.

### 2. Deadlock (교착 상태)
-   Client(앱)가 Server(시스템)를 호출하면서 락(Lock)을 잡고 있습니다.
-   Server가 처리 중에 다시 Client를 호출(Callback)하려는데, Client가 락을 잡고 있어서 대기합니다.
-   Client는 Server 응답을 기다리고, Server는 Client 락 해제를 기다립니다. -> **Freeze**.
-   **해결**: Binder 호출은 락 구간 밖에서 하거나, `oneway`를 적절히 사용해야 합니다.

### 📚 연결 문서
- [[android-architecture-stack]] - Binder가 위치한 곳
- [[android-activity-manager-and-system-services]] - Binder의 최대 고객
- [[android-hal-and-kernel]] - 하드웨어 통신용 Binder (HIDL/AIDL)
