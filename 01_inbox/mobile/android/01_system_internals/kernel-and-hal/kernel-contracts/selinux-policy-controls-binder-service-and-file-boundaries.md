---
title: selinux-policy-controls-binder-service-and-file-boundaries
tags: [android, android/ipc, android/kernel, android/security]
aliases: [SELinux Binder Policy, avc denied, binder call]
date modified: 2026-08-05 16:00:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

## SELinux policy는 Binder service와 file boundary를 함께 제어한다

상위 문서: [Kernel contracts](kernel-contracts.md)
배경 지식: [SELinux](01_inbox/linux/security/selinux.md), [IPC](01_inbox/operating-systems/ipc-mechanisms.md)

Android SELinux(Security-Enhanced Linux) 정책은 파일 디렉터리 및 문자/블록 디바이스 액세스뿐만 아니라, **binderfs**(전통적인 `/dev/binder` 캐릭터 디바이스 대신, 마운트 가능한 pseudo-filesystem 형태로 Binder 디바이스 노드를 동적으로 관리하는 커널 드라이버)를 통한 Binder IPC 통신(Binder 자체의 동작 방식은 아래 관련 문서 참고), **ServiceManager**(시스템 서비스들이 자신을 등록하고 client 가 서비스 이름으로 handle 을 찾을 수 있게 해주는 Android 의 Binder 서비스 registry) 서비스 등록/조회(`add`/`find`), 그리고 **System Property**(기기 전역에서 공유되는 key-value 설정값. `getprop`/`setprop` 으로 조회·설정한다) 읽기/쓰기에 이르는 Android 전용 경계를 통합 강제한다.

단순히 Linux DAC(UID/GID) 권한이 수락되거나 Android App Permission이 부여되었다고 해서 IPC 통신이 성립하는 것이 아니며, SELinux 커널 서브시스템이 Client Domain과 Server Domain(호출하는 프로세스와 호출받는 프로세스 각각에 매겨진 SELinux domain — domain/type 개념 자체는 [SELinux는 domain/type 정책으로 mandatory access control을 강제한다](selinux-enforces-mac-with-domain-type-policy.md) 참고) 간의 `binder { call transfer }` 클래스 규칙 및 ServiceManager `service_manager { find }` 규칙을 별도로 승인해야 한다.

---

### 메커니즘: Binder 호출 및 ServiceManager Lookup 시 SELinux 검증 단계

```mermaid
graph TD
    subgraph Client App Domain (untrusted_app)
        A["1. ServiceManager.getService('media.camera')"]
    end
    subgraph ServiceManager (servicemanager domain)
        B["2. Check service_manager find Permission\n(scontext=untrusted_app, tcontext=cameraserver_service, tclass=service_manager)"]
    end
    subgraph Kernel Binder Driver & SELinux LSM
        C["3. ioctl BINDER_WRITE_READ (binder call)"]
        D["4. Check binder call / transfer Permission\n(scontext=untrusted_app, tcontext=cameraserver, tclass=binder)"]
    end
    subgraph Target Service (cameraserver domain)
        E["5. Execute Service RPC Method"]
    end

    A --> B
    B -->|Passed Handle| C
    C --> D
    D -->|Passed AVC Check| E
```

1. **Service Lookup Stage (`service_manager`)**: Client가 ServiceManager에 정수 Handle을 요청할 때 `service_manager` 객체 클래스의 `find` 권한 검증.
2. **IPC Transaction Stage (`binder`)**: 커널 Binder 드라이버 트랜잭션 전송 시 `binder` 객체 클래스의 `call` 및 `transfer` (Binder handle/fd 전달 권한) 검증.
3. **FD Sharing Stage (`fd`)**: Binder를 통해 File Descriptor를 타 프로세스로 넘어줄 때 `fd { use }` 검증.

위 다이어그램의 "Passed AVC Check" 는 **AVC**(Access Vector Cache — SELinux 커널이 domain-type-class 조합마다 allow/deny 결정을 검사하고 캐싱하는 컴포넌트)를 통과했다는 뜻이며, 거부되면 앞서 본 `avc: denied` 로그가 남는다.

---

### SELinux Policy (`.te`) 선언 및 AVC Denial 예시

```text
# system/sepolicy/public/cameraserver.te 예시

# 1. untrusted_app domain이 cameraserver domain으로 binder call을 할 수 있도록 허용
allow untrusted_app cameraserver:binder { call transfer };

# 2. untrusted_app이 ServiceManager에서 cameraserver_service를 검색(find)할 수 있도록 허용
allow untrusted_app cameraserver_service:service_manager find;

# 3. cameraserver가 untrusted_app이 공유한 File Descriptor(fd)를 참조할 수 있도록 허용
allow cameraserver untrusted_app:fd use;
```

```text
# dmesg에서 관측되는 Binder AVC Denial 에러 로그 예시:
type=1400 audit(1620000000.123:45): avc: denied { call } for pid=1234 comm="app_process" scontext=u:r:untrusted_app:s0 tcontext=u:r:custom_service:s0 tclass=binder permissive=0
```

---

### 실무 규칙

- 신규 Native/HAL Binder 서비스를 추가할 때는 service_contexts 파일에 서비스 이름과 Type을 매핑하고, 해당 서비스의 Binder IPC 호출 도메인(`binder { call }`)과 ServiceManager find/add 권한을 `.te` 파일에 명시적으로 최소 권한 원칙(Principle of Least Privilege)으로 작성해야 한다.
- AVC Denial 해결 시 전체 접근을 열어주는 `allow domain self:binder *;` 와 같은 매크로를 작성해서는 안 되며, 좁혀진 Domain과 Specific Class 수준에서 정의해야 AOSP Treble/VTS 검증을 통과할 수 있다.

---

### 관측 가능한 증거 (Observable Evidence)

1. **SELinux Audit 로그 수집 및 AVC Denial 분석**:
   ```bash
   adb shell dmesg | grep "avc: denied"
   adb shell logcat | grep "avc:"
   ```
2. **`audit2allow` 툴을 이용한 디버깅 분석**:
   ```bash
   adb shell dmesg | audit2allow -p out/target/product/generic/root/sepolicy
   # 출력: allow untrusted_app custom_service:binder call;
   ```
3. **`servicemanager` 서비스 보안 컨텍스트 목록 확인**:
   ```bash
   adb shell service list
   ```

---

### 관련 문서

- [SELinux는 domain/type 정책으로 mandatory access control을 강제한다](selinux-enforces-mac-with-domain-type-policy.md)
- [Binder는 객체 참조를 커널이 중재하는 capability IPC다](../../ipc-and-process/ipc-process-contracts/binder-is-kernel-mediated-object-capability-ipc.md)
- [IPC and process contracts](../../ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)

공식 문서: [AOSP SELinux for Android](https://source.android.com/docs/security/features/selinux)

