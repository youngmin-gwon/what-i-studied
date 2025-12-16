---
title: android-evolution-history
tags: [android, android/history, android/transitions]
aliases: []
date modified: 2025-12-16 16:03:01 +09:00
date created: 2025-12-16 15:25:47 +09:00
---

## Evolution & Technology Transitions android android/history android/transitions

안드로이드가 어떻게 변해왔는지 큰 흐름만 쉽게 짚었다. 용어는 [[android-glossary]].

### 런타임/언어
- Dalvik(옛 VM) → [[android-glossary#art|ART]]: 더 빠르고 배터리 친화적.
- 자바 6 → 8 → 11, Kotlin 우선. 람다/코루틴/Null- 안전 등이 기본이 되었다.
- APK → [[android-glossary#apk|App Bundle]](AAB) 로 전환해 기기별로 필요한 조각만 배포한다.

### IPC/HAL
- HIDL → AIDL HAL: 테스트와 호환성 개선, 언어 제약 완화.
- 공유 메모리/버퍼: ashmem/ION → memfd/DMABuf 로 더 안전하고 표준화됨.
- Binder 네임스페이스 (binderfs) 로 보안을 강화.

### 그래픽/미디어
- OpenGL ES 중심 → Vulkan/ANGLE 로 옮겨가며 성능·호환성을 높임.
- SurfaceFlinger/HWC2/BLAST 로 합성 경로를 단순화하고 지연을 줄임.
- MediaCodec2 로 모듈화, DRM/보안 강화.

### 보안/프라이버시
- 저장소: 무제한 외부 저장소 → [[android-glossary#scoped-storage|Scoped Storage]].
- 권한: 설치 시 묻기 → 실행 중/한 번만 허용/대략적 위치/알림 런타임 권한 등 점진적 강화.
- 부팅: Verified Boot → AVB2, Play Integrity.

### 업데이트/배포
- Non-A/B → A/B/Virtual A/B 로 중단 없는 OTA.
- [[android-glossary#apex|Mainline/APEX]] 로 ART/Media/NetworkStack 등 핵심 모듈을 따로 업데이트.
- Incremental 파일 시스템/Play Asset Delivery 로 설치를 스트리밍.

### UI
- View 시스템 → Jetpack Compose 병행.
- Material → Material 3/Monet(동적 색상), 제스처 내비게이션, 폴더블/대화면 대응.

### 버전별 한 줄 메모
- 5.0 Lollipop: ART 기본, Material 1, JobScheduler.
- 6.0 Marshmallow: 런타임 권한, Doze.
- 7.0 Nougat: 멀티 윈도우, Vulkan, FBE.
- 8.0 Oreo: Treble, 알림 채널, 백그라운드 제한.
- 9 Pie: 앱 대기 버킷, Digital Wellbeing.
- 10: 제스처 내비, Scoped Storage(도입), Dark Theme.
- 11: 한 번만 권한, Bubbles, Incremental FS.
- 12: Material You/Monet, Private Compute Core.
- 13/14: per-app 언어, Photo Picker, 예측적 뒤로가기, FGS 타입, Health Connect.

### 링크

[[android-customization-and-oem]], [[android-security-and-sandboxing]], [[android-performance-and-debug]].
