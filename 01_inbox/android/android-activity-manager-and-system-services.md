# ActivityManager & System Services #android #android/system-services #android/ams

[[android-foundations]] · [[android-binder-and-ipc]] · [[android-zygote-and-runtime]]

## AMS/ATMS 역할
- ActivityTaskManagerService(ATMS)가 task/stack/transition을 관리, ActivityManagerService(AMS)가 프로세스 생애주기/메모리 정책을 담당.
- `ActivityRecord`/`Task`/`DisplayContent` 구조로 창/태스크 계층을 표현. WindowManagerService(WMS)와 협조.
- 프로세스 상태 계산: TOP/FOREGROUND_SERVICE/BOUND_TOP_APP/VISIBLE/SERVICE/CACHED 등. OOM adj 점수는 LMKD의 기준.

## 생명주기 관리
- startActivity → task 선택/재사용 → launch mode(singleTop/task/instance) → transition animation.
- process death 후 `onSaveInstanceState`/`ViewModel`/`SavedStateHandle` 조합으로 복원.
- 백그라운드 제한: API 26 이후 background execution limit, foreground service requirement, background start restrictions.

## 프로세스 관리
- `ProcessRecord`가 앱 프로세스 메타데이터 보유. AMS가 LRU list, cached/empty app trim 정책 적용.
- `trimApplications`/`collectProcesses`로 메모리 해제. `killProcessQuiet`/`forceStopPackage` 코드 경로.
- frozen processes: freezer cgroup로 프로세스 일시 정지. cached app compaction(zram)과 연계.
- cached/empty app eviction은 LMKD psi 신호와 연동되어 앱 경험에 직접 영향. 중요 앱은 setProcessImportant(visibility)로 보호.
- process state stats가 JobScheduler/AppStandby/Alarm throttle에 사용.

## 브로드캐스트/Job
- BroadcastQueue: foreground/ordered vs background/parallel 큐; ANR 타임아웃 상이.
- JobScheduler: network/battery/idle 조건. UID states와 연동해 throttling.
- AlarmManager: exact/RTC/ELAPSED_REALTIME; doze 앱 standby 고려.
- sticky broadcast는 제한적(배터리/보안 이유). manifest-registered vs context-registered 차이 주의.
- expedited jobs는 foreground service 비중을 낮추기 위한 최신 옵션.

## ContentProvider 관리
- App start 시 Provider 초기화 순서 관리(Dependency graph). `Authority` 충돌 처리.
- `ContentResolver` 호출은 Binder IPC; sync adapter, persistable URI permission.

## WindowManagerService 협업
- WMS는 SurfaceFlinger와 연결해 surface 할당, input focus, rotation, display cutout 관리.
- InputDispatcher는 포커스 윈도우로 이벤트 전달; ANR 시 input dispatching timeouts 기록.
- Transition/Animation: TransitionController(Shell), SurfaceControl transaction, BLASTBufferQueue.

## Notification/Foreground Service
- NotificationManagerService가 알림 채널/중요도/doze mode 제어. Foreground service는 ongoing notification 필요.
- AppOpsManager로 사용 권한 기록; [[android-security-and-sandboxing]] 참조.

## PackageManagerService
- install/update/remove, permission grant, split APK 관리. SettingsProvider에 패키지 스테이트 저장.
- Dexopt scheduler가 background에서 컴파일 작업 실행. Incremental FS로 스트리밍 설치.

## Connectivity/Location
- ConnectivityService는 network score, policy, VPN, Private DNS, tethering/eBPF offload 관리.
- Location: FusedLocationProvider, gnss HAL, background location 제한, NMEA/measurement API.
- Bluetooth/Wi-Fi: 각각 separate system service(bluetooth_manager/wifi). location permission과 연동된 스캔 정책.

## Watchdog과 안정성
- system_server watchdog이 binder thread/handler thread 응답 확인; 60s ANR 시 tombstone 작성.
- native 서비스 크래시 시 restarter가 재시작, critical service 반복 크래시 시 boot loop 보호.
- reboot escalation: persistent failure 시 Rescue Party가 설정/overlays 초기화 후 복구를 시도.

## Dumpsys/Debugging
- `adb shell dumpsys activity`로 task/process/oom adj 확인. `cmd activity`로 인텐트/force-stop 등 제어.
- `dumpsys package`, `dumpsys window`, `dumpsys meminfo`, `dumpsys batterystats` 등.
- `cmd` 하위 명령: `cmd stats print-logs`, `cmd jobscheduler monitor-battery`, `cmd power set-mode`. bugreport 시 snapshot.

## 정책 변천사
- Background execution limits(API 26), foreground service requirements(API 28), background activity start limits(API 29+), scoped storage(API 30), notification trampolines 금지(API 31).
- Task/Window model 변화: multi-window, freeform, bubbles, predictive back.
- Notification runtime permission(API 33), exact alarm permission(API 31+), foreground service types(API 34) 등으로 점진적 제한 강화.

## 연계 링크
- [[android-security-and-sandboxing]]: permission/AppOps/UID policies.
- [[android-performance-and-debug]]: ANR trace/Perfetto.
- [[android-evolution-history]]: 정책 변화 배경.
