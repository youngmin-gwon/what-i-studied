---
title: android-architecture-stack
tags: [android, android/architecture, android/layers]
aliases: []
date modified: 2025-12-16 15:59:56 +09:00
date created: 2025-12-16 15:22:42 +09:00
---

## Android Architecture Stack android android/architecture android/layers

안드로이드는 층층이 쌓인 케이크처럼 만든다. 각 층이 하는 일을 간단히 적었다. 모르는 단어는 [[android-glossary]] 를 본다.

### 층 소개
1. [[android-glossary#리눅스 커널|커널]]: 프로세스·메모리·보안·전원 같은 기초.
2. [[android-glossary#hal|HAL]]: 기기별 하드웨어와 안드로이드를 잇는 통역.
3. 네이티브 서비스: SurfaceFlinger, Media, Audio 등 그림·소리·센서를 처리.
4. [[android-glossary#art|ART]]: 앱 코드를 실행하는 엔진.
5. [[android-glossary#system-server|system_server]] 의 서비스: Activity/Window/Package/Network 등 핵심 관리자.
6. SDK/Jetpack: 앱이 쓰는 공식 API 와 라이브러리.
7. 앱: 샌드박스 안에서 돌아가는 Activity/Service/Receiver/Provider.

### 커널이 하는 일
- 스케줄링, 메모리 관리 ([[android-glossary#lmkd|LMKD]] 포함), 전원 관리 ([[android-glossary#wakelock|Wakelock]] 처리).
- [[android-glossary#selinux|SELinux]] 와 seccomp 로 보안 규칙을 적용.
- 드라이버: [[android-glossary#binder|Binder]], 디스플레이, 오디오, 카메라, 센서.

### HAL
- 하드웨어를 표준 모양으로 보여주는 C/C++ 인터페이스.
- 예전엔 HIDL, 지금은 AIDL HAL 을 주로 쓴다. 둘 다 Binder 를 통해 격리된 프로세스로 동작한다.
- VINTF 계약으로 시스템/업체 파티션이 맞는지 확인한다.

### 네이티브 서비스·그래픽
- SurfaceFlinger 가 화면을 합친다. HWC 가 지원하면 더 적은 전력으로 그린다.
- RenderThread/Skia 가 UI 를 GPU 에 맞게 준비한다.
- AudioFlinger/Policy 가 소리를 섞고 길을 정한다. MediaServer 가 인코딩·디코딩을 맡는다.

### ART 층
- [[android-glossary#zygote#preload|Preload]] 한 클래스/리소스로 메모리를 아낀다.
- 프로필 기반 JIT/AOT 로 자주 쓰는 코드를 빠르게 만든다.
- GC 로 메모리를 돌려받는다. 멈춤 시간을 줄이는 것이 목표다.

### 시스템 서비스
- [[android-glossary#system-server|system_server]] 프로세스에서 돌며, [[android-glossary#binder|Binder]] 로 앱과 통신한다.
- ActivityManager/WindowManager/PackageManager/Connectivity/JobScheduler 등.
- 권한 검사는 여기서 대부분 이뤄진다.

### 프레임워크/라이브러리
- 공개 SDK 와 Jetpack 이 앱 개발자가 만나는 면이다.
- 숨겨진 API([[android-glossary#hidden-api|Hidden API]]) 는 호환성을 위해 막아 둔다.
- [[android-glossary#apex|Mainline/APEX]] 모듈은 ART/Media/PermissionController 같은 핵심을 따로 업데이트한다.

### 앱
- 각자 UID, [[android-glossary#selinux|SELinux]] 도메인, 스토리지 샌드박스를 가진다.
- 프로세스 생성은 [[android-glossary#zygote|Zygote]] 가 포크해서 빠르게 만든다.
- 시스템과의 대화는 [[android-glossary#binder|Binder]] 를 통해 이뤄진다.

### 예시 흐름: 화면 띄우기
1. 앱이 startActivity 를 부른다.
2. ActivityManager 가 필요하면 새 프로세스를 [[android-glossary#zygote#fork|fork]] 한다.
3. Activity 가 뜨고 WindowManager/SurfaceFlinger 가 화면을 만든다.
4. 입력과 렌더링이 이어져 사용자가 본다.

### 예시 흐름: 사진 찍기
1. Camera2/CameraX 가 카메라 서비스에 요청한다.
2. HAL 이 센서에서 버퍼를 받아 공유 메모리로 보낸다.
3. MediaCodec 이 인코딩하고, MediaStore 에 저장된다. 저장 권한/범위는 [[android-glossary#scoped-storage|Scoped Storage]] 규칙을 따른다.

### 기술이 바뀐 예
- Dalvik→ART, HIDL→AIDL HAL, ION/ashmem→DMABuf/memfd, 커널 모듈→GKI.

### 더 보기

[[android-boot-flow]], [[android-activity-manager-and-system-services]], [[android-security-and-sandboxing]], [[android-adb-and-images]], [[android-customization-and-oem]], [[android-evolution-history]].
