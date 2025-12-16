# Binder & IPC #android #android/binder #android/ipc #systems

[[android-zygote-and-runtime]] · [[android-architecture-stack]] · [[android-activity-manager-and-system-services]]

## 개요
- Binder는 커널 드라이버 기반 IPC 메커니즘. 전송 시 객체 평면화를 위한 Parcelable, IBinder 인터페이스, ServiceManager 등록을 사용.
- 특징: 참조 카운팅(Strong/Weak), Identity token, PID/UID 전파, fd/handle 전송 지원, async/sync 트랜잭션.

## Binder 동작 경로
1. 클라이언트가 proxy 객체(Stub.asInterface)로 트랜잭션 호출.
2. 프레임워크 BinderProxy가 binder ioctl을 통해 커널 드라이버에 트랜잭션 요청.
3. 커널이 대상 서비스의 looper thread(Binder thread pool) 큐에 work enqueuing.
4. 서버 측 Binder thread가 `onTransact`를 실행하고, 결과를 마샬링해 응답.
5. binder driver가 caller thread로 결과를 복귀.

## Binder driver와 binderfs
- binderfs는 binder device 노출을 /dev/binderfs 아래로 이동해 권한을 구분. /dev/binder,/dev/hwbinder,/dev/vndbinder 등 네임스페이스 가능.
- context manager(ServiceManager) binder context는 default(hwbinder/vndbinder)로 분리되어 framework/vintf layer 분리.
- ioctl: BC_TRANSACTION/BR_TRANSACTION 교환, flat_binder_object로 FD/Binder 참조 전달.

## 쓰레드 풀과 스케줄링
- 기본 Binder thread pool 크기는 `binder.threadpool.size` 프로퍼티와 `oneway` 메서드 부담에 따라 조정.
- `Looper.prepare()` + `Handler`와 별개로 `Binder`는 고유 looper를 사용. ANR는 binder 호출 타임아웃(예: 5s)과 연결.
- `oneway` 트랜잭션은 비동기, 큐 적체 시 흐름 제어 필요.

## 안정성 도구
- Stable AIDL: @StableParcelable, @FixedSize, @Nullable로 호환성 보장.
- HAL binderized 경우, `-nostatic_jni`로 symbol 충돌 방지, `libbinder_ndk`로 NDK 레벨 interface 제공.
- `libbinder` vs `libbinder_ndk` vs `libbinder_rs`(Rust) 비교: C++가 가장 기능 완전, NDK는 앱/NDK용, Rust는 safety 제공.

## 서비스 등록과 검색
- Java 프레임워크: ServiceManager.addService/getService. lazy 서비스는 `system_server` init 중 conditional 등록.
- native: `defaultServiceManager()` → `checkService`/`getService`. hwservicemanager는 HIDL 서비스 레지스트리.
- 앱 간 IPC: `bindService`로 바운드 서비스 연결, AIDL 인터페이스로 타입 안전 호출.
- `ContentProvider`도 내부적으로 binder binderized; content resolver 호출이 transaction stats에 잡힘.

## Parcelable과 데이터 전송
- Parcelable은 반드시 역직렬화 순서 유지, Nullable 필드는 presence flag 필요.
- 대용량 전송은 shared memory(ashmem→memfd), FileDescriptor 전달로 zero-copy 처리.
- transaction size는 1MB 제한. large payload는 chunking/streaming.
- Stability: @JavaDerive/FixedSize/StableParcelable로 forward/backward 호환성 유지, padding/field order 주의.

## Security
- Binder는 call sid(PID/UID) 전달로 권한 검증. 시스템 서비스는 호출자 UID 기준으로 AppOps/Permission 체크.
- SELinux binder 정책: binder_call, binder_transfer 규칙으로 도메인 간 IPC 제어.
- Identity: `Binder.clearCallingIdentity` 사용 시 주의(권한 상승 위험), finally 블록에서 restore 필요.
- shell UID는 별도 권한을 가지므로 shell commands vs app calls 차이를 이해해야 한다.\n

## Death Recipient & Lifecycle
- `linkToDeath`로 서버 프로세스 종료를 감지. strong vs weak binder handles.
- system_server 죽음 → zygote restart → boot loop 위험; watchdog/overload protection이 중요.
- binder refcount leak은 driver debugfs/binderfs stats로 확인. `binder_dump`로 참조 그래프 확인.

## Binder와 Job/Work
- 긴 작업은 binder oneway+JobScheduler/WorkManager로 오프로드, binder thread starvation 회피.
- `AsyncChannel`/`Messenger`는 binder 위 래퍼. 현대 코드는 AIDL coroutine/Flow bindings를 활용.

## Binder tracing & 디버깅
- `adb shell dumpsys binder`로 서비스/transaction 수 통계. `binder_calls_stats` 추적.
- systrace/Perfetto에서 binder categories(`binder_transaction`, `sched_wakeup`)로 경로 확인.
- heapprofd/atrace로 binder buffer/queue 상태 확인 가능.
- `service call <iface> <code>`로 raw binder 호출 테스트 가능(개발 빌드). binder_transaction_log enable로 상세 추적.
- stability/debug props: `persist.binder.debug`, `persist.sys.binder.full_stats` 등은 user 빌드에서는 제한됨.\n

## 시스템 서비스 사례
- ActivityManagerService, PackageManagerService, WindowManagerService, NotificationManagerService, ConnectivityService 모두 binder 인터페이스 노출.
- Keyguard/LockSettings(Keystore)도 binder로 credential 작업 처리.

## 진화
- HIDL binderized → AIDL hal, binderfs adoption, security hardening(binderfs, SELinux). io_uring 기반 전송 연구.
- RPC over binder for Rust(`binder_rpc_unstable`), binder lazy init for boot time 개선.
- stability 선언(@VintfStability, @RustDerive)으로 HAL/interface 호환성 강화.

## 연계 문서
- [[android-activity-manager-and-system-services]]: binder 서비스 설계 패턴.
- [[android-security-and-sandboxing]]: 권한/SELinux/binder 정책.
- [[android-adb-and-images]]: adb shell/service call/binder debugging.
