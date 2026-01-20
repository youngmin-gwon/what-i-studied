---
title: android-zygote-and-runtime
tags: [android, art, dalvik, initialization, internals, zygote]
aliases: [ART, Dalvik, Zygote]
date modified: 2026-01-20 15:55:31 +09:00
date created: 2025-12-16 15:22:42 +09:00
---

## Zygote & Runtime: The Birth of an App

앱 아이콘을 터치하는 순간, 0.1 초 만에 앱이 뜹니다.

리눅스에서 Java 가상머신(JVM) 하나 띄우는 데 1 초가 넘게 걸리는 걸 생각하면 마법 같은 속도입니다.

그 비밀은 **Zygote ("수정란")**에 있습니다.

### 💡 Why it matters (Context)

- **Launch Speed**: 앱을 켤 때마다 JVM 을 새로 부팅한다면 스마트폰을 쓸 수 없을 것입니다. Zygote 덕분에 우리는 "즉시 실행"을 경험합니다.
- **Memory Sharing**: 수천 개의 앱이 똑같은 `String`, `TextView` 클래스를 씁니다. Zygote 가 없으면 메모리는 순식간에 동납니다.
- **Static Initialization Issues**: `static` 블록에 무거운 코드를 넣으면, 앱 시작 속도뿐만 아니라 **시스템 전체 부팅 속도**를 느리게 할 수 있습니다 (Preload 클래스의 경우).

---

### 🦠 Zygote Internals

Zygote 는 **"모든 앱의 부모 프로세스"**입니다.

#### 1. Boot Logic (The Warm-up)
1. 안드로이드가 부팅될 때 가장 먼저 (`init` 다음으로) Zygote 프로세스가 뜹니다.
2. **Preloading**: `framework.jar`, `androidx`, `drawable` 등 모든 앱이 공통으로 쓰는 4,000 여 개의 클래스와 리소스를 메모리에 미리 로드합니다.
3. **Socket Listen**: 로딩을 다 마치면 `/dev/socket/zygote` 를 열고 "새끼 칠 준비"를 마친 채 잠듭니다.

#### 2. Fork & Copy-on-Write (COW)

앱 실행 요청이 오면, Zygote 는 자기 자신을 **복제(`fork()`)**합니다.

- **Magic**: `fork()` 는 자식 프로세스에게 부모의 메모리를 그대로 물려줍니다.
- **COW**: 처음에는 메모리를 실제로 복사하지 않고 **공유(Share)**만 합니다. 앱이 데이터를 **쓰는(Write)** 순간에만 그 페이지만 뚝 떼어서 복사합니다.
- **Result**: 앱 100 개를 띄워도 `Framework` 클래스 메모리는 딱 1 개 분량만 듭니다.

---

### ☕️ ART vs Dalvik: Evolution of Runtime

안드로이드 런타임은 "배터리와 속도" 사이의 끝없는 줄타기 역사입니다.

#### 1. Dalvik (Android 4.4 이전)
- **JIT (Just-In-Time)**: 앱을 실행할 때마다 매번 기계어로 번역했습니다.
- **단점**: 실행할 때마다 배터리를 쓰고, 초기 구동이 느립니다.

#### 2. ART 1.0 (Android 5.0 ~ 6.0)
- **AOT (Ahead-Of-Time)**: 앱 설치할 때 **몽땅 다 기계어로 번역**(`dex2oat`)해버립니다.
- **장점**: 실행 빠름, 배터리 절약.
- **단점**: 설치 시간이 엄청 오래 걸림 ("앱 최적화 중입니다…" 화면 기억나시나요?), 용량이 커짐.

#### 3. Modern ART (Android 7.0+)
- **Hybrid (JIT + AOT + Profile)**:
    1. 처음 설치하면 **JIT** 모드로 동작 (설치 즉시 완료).
    2. 사용자가 자주 쓰는 기능을 **프로파일링(Profile)** 기록.
    3. 충전 중일 때(Idle), 프로파일을 바탕으로 **자주 쓰는 부분만 AOT 컴파일**.
    - **결론**: 설치도 빠르고, 쓸수록 앱이 빨라집니다.

---

### 🛠️ App Process Initialization

앱 프로세스가 fork 된 직후 실행되는 순서입니다:

1. **Zygote Init**: `fork()` 후 쓰레드 풀 초기화.
2. **Runtime Init**: C++ 네이티브 브릿지 설정.
3. **Application bind**: `ActivityThread.main()` 실행.
4. **Attach**: `AMS` 에게 "나 살았어요"라고 신고.
5. **Instrumentation**: `Application.onCreate()` 실행. (여기서부터 개발자 영역)

#### 📚 연결 문서
- [android-boot-flow](android-boot-flow.md) - Zygote 가 시작되는 시점
- [android-binder-and-ipc](android-binder-and-ipc.md) - AMS 가 Zygote 에게 fork 요청을 보내는 통로
- [android-process-and-memory](android-process-and-memory.md) - 프로세스별 메모리 구조
