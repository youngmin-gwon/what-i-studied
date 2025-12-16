# Graphics & Media Pipeline #android #android/graphics #android/media

[[android-architecture-stack]] · [[android-performance-and-debug]] · [[android-hal-and-kernel]]

## 렌더링 스택
- UI Toolkit(View/Compose) → RenderThread/DisplayList → Skia → HWUI → SurfaceControl/BufferQueue → SurfaceFlinger → HWC.
- VSync/Choreographer가 프레임 스케줄 관리. `SurfaceControl.Transaction`으로 atomic 레이어 업데이트.
- BufferQueue: producer/consumer 모델; app produces buffers, SF/HWC consumes. BLASTBufferQueue로 latency 감소.
- Frame timeline API로 producers/consumers 간 타임스탬프 교환. choreographer callback order(input→animation→traversal→commit).
- HDR/wide color: color space metadata 전달, Display P3, BT2020; tone mapping at HWC/GPU.

## Compose vs View
- Compose: recomposition, snapshot system, `remember`/`derivedStateOf`, composition locals. Skia pipeline 동일하지만 레이아웃/측정 모델 간단.
- View: measure/layout/draw pass, ViewRootImpl, DisplayList caching. Invalidations propagate from view tree.
- Interop: ComposeView/AndroidView, performance trade-offs.

## SurfaceFlinger & HWC
- SurfaceFlinger 합성 단계에서 각 layer의 blend/transform/clip/z-order 결정. Color management/Render intent 지원.
- HWC2 HAL로 오프로드: client composition(GPU) vs device composition(HWC). Present fences, retire fences로 sync.
- Refresh rate switching/Frame rate API, touch latency alignment, async vsync.
- Layer stack/virtual display mirroring, screen recording path(media projection)에서 buffer duplication. frame rate overlay/debug.\n

## Graphics 메모리
- GraphicBuffer allocation via gralloc HAL; DMABuf handle. ION legacy. AHARDWAREBUFFER for NDK.
- Protected content/DRM surfaces require secure buffers + HWC path.
- GPU memory accounting, `dumpsys meminfo <pid> graphics`.
- Vulkan memory model vs OpenGL ES; descriptor sets/pipelines. ANGLE translating GL to Vulkan/D3D.
- GPU driver updates via Play System Update(GPU inspector). Adreno/Mali/PowerVR 차이.\n

## Input & Rendering 연계
- InputReader timestamps events, InputDispatcher delivers to focused window. `Choreographer` posts input vsync for latency smoothing.
- Touch resampling/prediction, display pipeline vs input sampling alignment.

## Camera/Media capture
- Camera HAL3 pipeline: request/result, stream config, sync fences, buffer formats(YUV/RAW), reprocessing.
- CameraX simplifies use cases; camera2 offers fine control. Permissions + concurrent camera limits.
- MediaRecorder/MediaCodec pipelines: hardware codecs via Codec2, buffer queue to encoder, muxer output.
- multi-camera, logical camera, depth/ultra-wide fusion. camera privacy switch/indicator wiring.
- image stabilization(EIS/OIS) metadata, rolling shutter correction, latency budgets for preview vs capture.\n

## Media Playback
- ExoPlayer: modular renderers/audio/video/text/drm. Adaptive streaming(DASH/HLS/SmoothStreaming), ABR algorithms, buffering/seek strategies.
- Audio: AudioTrack/AudioRecord, AAudio/Oboe for low latency. Audio focus/ducking, session IDs for effects.
- DRM: MediaDrm with Widevine, key status, offline keys, secure decoder surface.
- Subtitle pipelines(Cues), text rendering, font fallback. Live playback latency tuning(low-latency HLS/DASH).
- spatial audio/binaural rendering, head tracking, Bluetooth LE Audio/LC3.
- Mixer paths: AudioFlinger mixer vs direct output, offload playback for low power. Audio effects(EQ/BassBoost/Virtualizer) chains.
- Audio focus types(gain/transient/mayduck), audio attributes usage, volume shaping. record vs playback routing.

## Graphics Debugging
- GPU Inspector, Frame Profiler, `dumpsys SurfaceFlinger --latency`, `gfxinfo framestats`.
- Perfetto tracks: `gfx`, `view`, `sched`, `binder_driver`, `hwc`. GPU counters via AGI/Perfetto.
- Skia tracing, `adb shell setprop debug.hwui.profile visual_bars`.

## Media Debugging
- `dumpsys media.audio_flinger`, `media.audio_policy`, `media.metrics`, `media.player`, `mediadrm`, `cameraserver`.
- codec dumps: `dumpsys media.codec` to check component state, buffers. stagefright logging.
- Latency measurements: audio latency test loopback, camera capture latency traces.
- `atrace gfx view res` overlays, GPU counters via AGI, SurfaceFlinger latency histogram. media.metrics proto 분석.
- AudioThread timing logs, xruns detection, `audioserver` crash dumps, `ACDB`/audio calibration data issues.
- logcat tags: ExoPlayer event logs, `libc/avc/mediaserver` errors, `MediaCodec` state transitions. perfetto tracks for audio/codec.

## Evolution 포인트
- OpenGL ES → Vulkan adoption; ANGLE for compatibility. HDR/wide color gamut pipeline, tonemapping.
- MediaCodec2 replacing stagefright monolith; separated processes(media swcodec).
- AAudio for pro audio, Oboe wrapper. Spatial audio/ultra-low latency work.
- HEVC/AV1 hardware decode adoption, HDR10+/Dolby Vision metadata pass-through. Codec2 plugin model for vendor.

## Graph Links
- [[android-binder-and-ipc]] for buffer transactions, [[android-adb-and-images]] for trace collection, [[android-evolution-history]] for graphics/media 전환.
