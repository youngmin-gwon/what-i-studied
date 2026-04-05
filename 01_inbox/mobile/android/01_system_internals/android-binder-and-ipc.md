# [[mobile-security]] > [[android-binder-and-ipc]]

## Binder: The Nervous System of Android

안드로이드 시스템 서비스(ActivityManager, PackageManager 등)와 앱 간의 모든 대화는 **Binder**를 통해 이루어집니다. Binder가 없다면 안드로이드는 뇌(System Server)와 팔다리(App)가 연결되지 않은 것과 같습니다.

---

### 💡 Context: 왜 모바일 전용 IPC가 필요한가?

전통적인 리눅스 IPC(Pipe, Socket 등)는 모바일 환경에서 사용하기에 몇 가지 한계가 있습니다.

- **Performance**: 기존 IPC는 데이터를 커널과 유저 공간 사이에서 두 번 복사하지만, Binder는 매핑된 메모리 공간을 활용하여 **단 한 번의 복사(Zero-copy 지향)**만 수행합니다. 이는 60fps의 부드러운 화면 반응성을 유지하는 핵심 기술입니다.
- **Security**: Binder 커널 드라이버는 호출자의 **UID**와 **PID**를 수신 측에 강제로 전달합니다. 수신자는 이를 통해 발신자가 누구인지 확실히 식별할 수 있어, 앱이 시스템 서비스를 속이는 것을 방지합니다.
- **Resource Management**: 프로세스당 Binder 버퍼는 **1MB**로 제한됩니다. 이 제한은 시스템 전체의 메모리 고갈을 막는 안전장치 역할을 합니다.

---

### ⚙️ Binder Internals: 작동 원리

Binder는 단순한 직렬화 도구가 아닌, 핵심 **커널 드라이버(`/dev/binder`)**입니다.

1. **Client**: `transact()`를 호출하고 응답이 올 때까지 스레드가 블로킹(Blocking)됩니다.
2. **Kernel Driver**: 데이터를 발신자의 메모리에서 수신자의 주소 공간에 매핑된 **Binder Buffer**로 복사합니다.
3. **Server**: 미리 구성된 **Binder Thread Pool** 내의 스레드가 깨어나 `onTransact()`를 통해 요청을 처리하고 결과를 반환합니다.

---

### 🛠️ AIDL (Android Interface Definition Language)

복잡한 IPC 통신 코드를 자동으로 생성해주는 도구입니다.

- **Stub**: 서버(수신) 측 구현체로, 들어오는 트랜잭션을 처리합니다.
- **Proxy**: 클라이언트(발신) 측 대리인으로, 원격 프로세스의 메서드를 마치 로컬 메서드처럼 호출하게 해줍니다.
- **oneway**: 이 키워드를 사용하면 클라이언트가 서버의 처리를 기다리지 않는 비동기(Non-blocking) 호출이 가능해집니다.

---

### 🚨 주요 주의사항 (Pitfalls)

- **TransactionTooLargeException**: 1MB 제한을 초과하면 발생합니다. 비트맵과 같은 대용량 데이터는 Intent에 직접 담지 말고 `ContentProvider` URI나 `FileDescriptor`를 활용해야 합니다.
- **Binder Thread Pool Starvation**: 모든 Binder 스레드(기본 16개)가 작업 중이면 시스템의 호출에 응답하지 못해 **ANR**이 발생할 수 있습니다.
- **Deadlock**: 클라이언트와 서버가 서로의 응답이나 락(Lock) 해제를 기다리며 무한 대기에 빠지는 상황을 주의해야 합니다.

---

### 📚 연관 문서 및 심화 학습
- [[android-architecture-stack]] - 아키텍처 계층에서의 Binder 위치
- [[android-activity-manager-and-system-services]] - Binder를 가장 많이 사용하는 시스템 서비스
- [[android-hal-and-kernel]] - 하드웨어 통신용 Binder (HIDL/AIDL) 및 Treble
- [[mobile-android-foundation-security]] - Binder 기반의 권한 검사 매커니즘
- [[android-zygote-and-runtime]] - 프로세스 생성 시 Binder 스레드 초기화 과정
