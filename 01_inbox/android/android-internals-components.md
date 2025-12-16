---
title: android-internals-components
tags: [android, android/internals, android/system-server]
aliases: []
date modified: 2025-12-16 15:41:57 +09:00
date created: 2025-12-16 15:26:56 +09:00
---

## Android Internals Components android android/internals android/system-server

[[android-architecture-stack]] · [[android-binder-and-ipc]] · [[android-activity-manager-and-system-services]]

### system_server 구조
- init 가 zygote 를 통해 system_server 를 포크하며 다수의 Java 서비스가 등록. critical 서비스는 zygote native preload 후 Java 초기화 순서에 민감.
- service.startBootstrapServices → startCoreServices → startOtherServices 단계적 부팅. Watchdog 등록, dropbox/ANR trace path 설정.
- Thread priority: foreground/system/server priority 조정. mHandler thread, foreground service map 등 핵심 상태 보유.

### ActivityTask/Window/Display
- ATMS 는 task/window hierarchy 를 관리하며 multi-display, multi-window, freeform, picture-in-picture, bubbles 등을 조합한다.
- WMS 는 SurfaceControl 트리를 구성하고 Insets/IME/StatusBar/NavigationBar 레이어를 배치. Input Focus/Touchable region 계산.
- Shell/Transitions: shell transitions(controller) + BLASTBufferQueue 로 프레임 동기화. WM Shell 이 SystemUI 와 협력.

### PackageManager/Overlay
- PMS 는 package scanning(codePath, abi, nativeLibDir), permission grant, split install, shared libs. Settings data 는 packages.xml 로 저장.
- DexManager 가 `usage` 통계와 profile 적용을 담당. `BackgroundDexOptService` 가 idle 시 dexopt 실행.
- OverlayManagerService 가 RRO 적용 순서/priority 를 관리. Fabricated overlay 와 dynamic refresh 지원.

### Input/IME
- InputManagerService 가 event device 를 모니터, InputReader/Dispatcher 파이프라인을 제어. Gesture/Mouse/Keyboard 모드 차별.
- IME 는 InputMethodManagerService 가 연결, window insets 로 크기 조절. 새 IME API 는 private IME switching 제한, haptic/text classification 연계.
- PointerCapture, stylus/hover, accessibility services 와의 상호작용.

### Power/배터리 관리
- PowerManagerService: wakelock bookkeeping, idleness, brightness curve. Doze/standby 는 AlarmManager/JobScheduler 와 연결.
- BatteryStatsService: wakelock/alarms/jobs/network 데이터 수집, batterystats proto. Battery Historian 입력.
- DeviceIdleController: motion/light/doze constraints. thermal service 와 성능 스로틀.

### Storage/FS
- MountService/Vold: adoptable storage, FBE key mgmt, OBB, media mount. Checkpoints for F2FS/Ext4.
- StorageManagerService: quota, storage UUID, `StorageVolume` 제공. Scoped storage enforcer.
- IncrementalService: INCFS for streaming installs.

### Connectivity/Telephony
- ConnectivityService: network agent/transport(cell/wifi/ethernet), scoring, captive portal detection, VPN, netd policy.
- netd: firewall, per-UID routing, DNS resolver, tethering offload(eBPF), clat464(IPv6/IPv4). statsd inputs.
- Telephony: TelephonyRegistry, ServiceState/SignalStrength dispatch. CarrierConfigManager overlays, IMS service for VoLTE/VoWiFi.

### Location/Sensors
- LocationManagerService: fused provider, GNSS HAL, background throttling, mock location guard.
- SensorService: sensor events delivery rate, batching/flush, wake-up vs non-wake, FIFO sizing. Sensor privacy toggles.
- ActivityRecognition/HAL(AR), Context Hub Runtime Environment(CHRE) for low-power ML on sensor hub.

### Media/Audio
- MediaRouter/AudioPolicyService: routing decisions, audio focus, volume, ducking. Audio HAL interaction, mix effects.
- MediaSessionService/MediaBrowserServiceCompat: playback control, notification integration. MediaCodec/Extractor pipeline for playback/record.
- CameraService: open sessions, stream configuration, binder death, permissions. CameraX/Camera2 client mapping.

### Security/Keystore
- Keystore2 + KeyMint/StrongBox HAL: hardware-backed keys, auth-bound, rollback-resistant. Keystore daemon separate process.
- LockSettingsService: credential storage, Gatekeeper/Weaver. BiometricPrompt/Face/FP services with HAT tokens.
- PermissionController: runtime grant UI/logic mainline module. AppOps policies integrated with PermissionManager.

### Stats/Telemetry
- statsd: native daemon ingesting pulled/pushed atoms. Configs via protobuf. Subscription by UID, guardrails for privacy.
- DropBoxManagerService: system event logs/ANR/crash tombstones. Incidentd for redacted incident reports.
- Debug providers: dumpsys entry for most services; bugreport aggregator collects traces/logs.
- Stats pullers: battery, cpu time, memory, connectivity, binder latencies. Configs gated by whitelisted UIDs.
- Privacy mitigations: rate limits, anonymization, ephemeral ids; ATP (Android Test Platform) for server-side validation.

### Scheduler/Jobs/Alarms
- AlarmManagerService: app standby bucket-aware delivery, exact alarm permissions, alarm batching vs idle maintenance windows.
- JobSchedulerService: constraint tracking(network, idle, charging, storage, timing), quota controller for background tasks.
- WorkManager uses JobScheduler/gcmNetworkManager/backoff; expedited jobs vs foreground service interplay.
- Quota controller: standby bucket/fg/bg usage 기반 job budget 계산. thermal/power policies 와 연계.\n

### User/Profiles/Policy
- UserManagerService: multi-user/profile restrictions, device/profile owner policies. Work profile separation, cross-profile intents.
- DevicePolicyManagerService: enterprise controls, compliance checks, key provisioning. COSU/lock task mode.
- AppOps/UsageStats: app visibility, standby buckets, restricted apps, privacy sandbox interactions.
- Credential-encrypted vs device-encrypted storage 에 따라 direct boot 동작 구분. user switch/on-demand unlock sequence.
- Cross-profile apps/intent filters 로 업무/개인 데이터 흐름 제어. app linking restrictions.

### SystemUI & Render pipeline
- SystemUI hosts status bar/navigation/notifications/quick settings. Uses shells for transitions, Bubbles/Conversations/Media controls.
- Notification pipeline: ranking, channels, importance, smart actions/suggestions. Shade UI + lockscreen dependencies.
- Render thread & Composition: SystemUI heavy surfaces coordinate with WMS/SurfaceFlinger for smooth animations.
- Monet(dynamic color) pipeline: color extraction from wallpaper → material color seeds → palette applied via themes/overlays.
- LockScreen/Keyguard: trust agent, biometric unlock, bypass, dream service(always-on display), smart space/at-a-glance.

### Testing/Debug Hooks
- `cmd activity stack`/`cmd window tracing start` for WM/transition traces. `cmd stats print-logs`.
- service call binder debugging, `dumpsys` for each service. Perfetto configs focusing on WM/AM/Binder/SurfaceFlinger.
- `cmd uimode`, `cmd appops set`, `cmd overlay enable-disable` 등 런타임 스위치로 상태 재현.

### 설계 패턴
- 권한 검사: 시스템 서비스 경계에서 AppOps + permission + UID check. [[android-security-and-sandboxing]]
- non-blocking binder: binder thread pool 제한, long task offload. watchdog handler thread for ANR detection.
- feature flags/gatekeeper: DeviceConfig/Flags runtime toggles for experiments.
- crash isolation: critical 서비스 분리 (media/keystore/statsd), process health monitoring, tombstoned for native crash capture.
- Idle maintenance window: doze maintenance, jobs/alarms/network batching 으로 배터리 절약.\n
- stats/health indicator: Health HAL + Healthd, battery health estimation, charge cycles. thermal service policy for CPU/GPU.

### 역사적 맥락
- Monolithic system_server → 분리 (MM/media/statsd/keystore) 로 메모리/보안 개선.
- WMS re-architecture: SurfaceFlinger/HWC2/BLAST adoption. ATMS split from AMS.
- Permission controller mainline 화, Notification trampolines 금지, predictive back/gesture nav 진화.

### Graph Links
- [[android-foundations]], [[android-activity-manager-and-system-services]], [[android-performance-and-debug]], [[android-boot-flow]].
