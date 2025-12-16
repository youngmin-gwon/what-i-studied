# Performance & Debugging #android #android/performance #android/debugging

[[android-foundations]] · [[android-zygote-and-runtime]] · [[android-binder-and-ipc]]

## 성능 목표 설정
- 지연: cold start < 5s, hot start < 1s, frame time 16ms 이하(60fps).
- 메모리: heap leak 최소화, native/graphics/bitmap 별도 추적. LMKD 킬 회피 위해 RSS/Swap 모니터.
- 배터리: wakelock 시간, network/batch 작업, JobScheduler constraints 사용.

## 스타트업 최적화
- Baseline Profiles + cloud profile push. `Macrobenchmark`로 cold/hot start 측정.
- Lazy init/DI entry point 최소화. SplashScreen API 활용하되 작업은 비동기 전환.
- App Startup Library/Delayed initialization, ContentProvider auto-init 제거.
- Prewarmers: WebView/지도/미디어 SDK warmup, Trusted Web Activity 예열. Perfetto startup trace로 blocking call을 찾아 제거.
- cold/warm/hot start 정의와 cached process 유지 전략을 명확히 하고, start-up task 우선순위/병렬화 조정.

## 렌더링 최적화
- Compose: recomposition scope 최소화, remember/derivedStateOf, snapshot state ho이스팅.
- View: RecyclerView diffing, ConstraintLayout vs LinearLayout 깊이 최적화, overdraw 줄이기.
- RenderThread/Skia GPU: `adb shell dumpsys gfxinfo`, `FrameMetricsAggregator`. HWC composition fallback 체크.
- 카메라/지도처럼 무거운 surface는 SurfaceView/TextureView trade-off 고려. Jank 유형: input latency vs scheduling vs GPU stall을 구분.
- FrameTimeline API와 choreographer callback 순서를 이해해 input-to-render latency를 줄인다.

## 메모리 분석
- LeakCanary/Android Studio Profiler. `dumpsys meminfo <pkg>`로 java/native/graphics/stack/pixels/malloc breakdown.
- `heapprofd`/`meminfo --unreachable`/`simpleperf` for native. `perfetto --txt` heap tracks.
- Bitmap reuse/inBitmap, hardware bitmaps 제한, Glide/Picasso/Coil tuning.
- jemalloc/malloc debug options, `mallinfo`/`malloc_debug` system properties. Bitmap pool sizing vs memory class.
- native heap tagging(MTE/HWASAN)로 out-of-bounds 탐지; pointer tagging/Scudo adoption 흐름 주시.

## 쓰레드/동시성
- Main dispatcher 순수 유지, long work는 IO/Default dispatcher로. Structured concurrency + SupervisorJob.
- ANR: input dispatch timeout(5s), broadcast receiver timeout(10s), service timeout(20s). `data/anr/traces.txt` 분석.
- Binder: oneway flood 주의, binder thread pool saturation. `adb shell dumpsys binder --stacks`.
- StrictMode thread/VM policies: disk/network on main, leaked closable, file URI exposure. penaltyLog/dialog/dropbox.
- coroutine cancellation/timeout 사용으로 작업 중단. executor saturation 모니터링(queued tasks, thread pool size).

## 저장소/네트워크 효율
- Room 쿼리 index, WAL/foreign key. Paging3 for list streaming.
- DataStore/ProtoStore로 스레드 안전 설정 저장.
- HTTP: caching, gzip, HTTP/2/QUIC; WorkManager + backoff for retries. Metered network awareness.
- SQLite perf: PRAGMA synchronous/foreign_keys/wal_autocheckpoint, statement logging, I/O scheduler 영향.
- Network: DNS caching, okhttp connection pool, TLS session resumption. backpressure/Flow for streaming.\n

## 배터리/BG 정책 대응
- JobScheduler/WorkManager constraints로 doze/standby 대응. Foreground service는 실제 사용자 가시성 필요.
- Alarm exact 제한, setAlarmClock/use-case 명확화.
- Battery Historian/`dumpsys batterystats`/`bugreport`로 wakelock/alarms/Job stats 확인.
- Power KPI: doze maintenance budget, wakelock tag/uid attribution, network stats top offenders.

## 네이티브 프로파일링
- `simpleperf record` + `report_html`. `perfetto`로 CPU/GPU timeline, binder latency, frame slices.
- `atrace gfx view sched freq idle binder_driver` for quick trace. Systrace legacy.
- perf maps, `android-addr2line`, `ndk-stack`로 tombstone 심볼화.
- HW events via perf PMU; eBPF tracing for network/binder; kernel tracepoints for sched/wakeup.
- simpleperf unwinding, dwarf info in ndk builds, symbolization pipelines. jemalloc heap profiling hooks.

## Crash/ANR 대응
- Java crash: `Thread.setDefaultUncaughtExceptionHandler`로 로깅, but avoid swallowing.
- Native crash: tombstone in `/data/tombstones`. `debuggerd -b` attach.
- ANR: `traces.txt` + Perfetto slice. Input dispatch/executors blocked 원인 찾기.
- StrictMode death-on-file-uri, VMPolicy class instance limits. ANR repro 스크립트와 trace bookmark 유지.\n

## 릴리즈 안정성
- R8 shrinking/obfuscation; mapping file 관리. Play Console vitals(ANR/Crash), Pre-launch reports.
- Feature flags/remote config for safe rollout. Staged rollout/Canary channels.
- StrictMode/NetworkOnMainThread, `StrictMode.VmPolicy` for leaks/file/closers.
- metrics pipeline: logs → analytics → dashboards; alert on regressions. kill switches for experiments, remote config rollback.

## Graph Links
- [[android-activity-manager-and-system-services]], [[android-security-and-sandboxing]], [[android-adb-and-images]], [[android-evolution-history]].
