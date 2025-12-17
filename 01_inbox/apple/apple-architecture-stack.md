---
title: apple-architecture-stack
tags: [apple, architecture, darwin, kernel, xnu, internals]
aliases: []
date modified: 2025-12-17 14:15:00 +09:00
date created: 2025-12-16 16:07:53 +09:00
---

## Apple System Architecture & Kernel Internals

Apple 운영체제의 기반인 Darwin과 XNU 커널의 아키텍처 심층 분석. 용어 정의는 [[apple-glossary]] 참고.

### 📚 외부 리소스 및 참고 자료

#### 커널 소스 및 공식 문서
- **XNU Kernel Source**: [apple-oss-distributions/xnu](https://github.com/apple-oss-distributions/xnu) - 메인 커널 소스 (GitHub)
- **Darwin Open Source**: [Apple Open Source](https://opensource.apple.com/)
- **Kernel Programming Guide**: [Apple Developer Archive](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/)
- **Mach Microkernel**: [CMU Mach Project](https://www.cs.cmu.edu/afs/cs/project/mach/public/www/mach.html) - XNU의 기반이 된 마이크로커널

#### 📖 기술 서적 및 심화 학습
- **Mac OS X Internals**: [System Approach](https://www.amazon.com/Mac-OS-Internals-Systems-Approach/dp/0321278542) - 클래식하지만 여전히 유효한 바이블
- **OS X & iOS Kernel Programming**: [Book Link](https://www.amazon.com/OS-iOS-Kernel-Programming-Ole/dp/1430235973)
- [NewOSXBook](http://newosxbook.com/index.php) - Jonathan Levin의 현대적인 iOS 내부 구조 분석

---

### 🏛️ XNU 커널 아키텍처 (Hybrid Kernel)

XNU("X is Not Unix")는 **Mach 마이크로커널**의 유연성과 **BSD**의 실용성을 결합한 하이브리드 커널입니다.

#### 1. Mach (Microkernel Layer)
커널의 가장 안쪽 심장부입니다. 추상화와 리소스 관리를 담당합니다.
- **Tasks & Threads**: 프로세스(Task)와 실행 단위(Thread) 관리. BSD의 프로세스 모델은 Mach Task 위에서 구현됩니다.
- **IPC (Inter-Process Communication)**: **Mach Message**는 시스템 전체의 통신 동맥입니다. 매우 빠르고 안전하게 커널-유저, 유저-유저 간 데이터를 전달합니다.
- **Virtual Memory**: 가상 메모리 객체(Memory Object) 관리, 페이지 폴트 처리.

#### 2. BSD (Berkley Software Distribution Layer)
Mach 위에서 POSIX 호환성과 고수준 시스템 기능을 제공합니다.
- **File Systems (VFS)**: APFS, HFS+ 등 파일 시스템 추상화.
- **Networking**: TCP/IP 스택, 소켓 계층.
- **Security**: User ID (uid), Group ID (gid), 권한 관리.
- **System Calls**: `open()`, `read()`, `write()`, `fork()` 등 표준 유닉스 API 제공.

#### 3. I/O Kit
객체 지향(C++ 부분집합) 디바이스 드라이버 프레임워크입니다.
- 하드웨어(USB, Bluetooth, GPU 등)와 동적으로 연결되며, 전원 관리(Power Management) 기능을 내장하고 있습니다.

---

### 🚀 시스템 부팅과 앱 실행 과정 (Process Launch)

#### 1. Boot Chain (Secure Boot)
1. **Boot ROM**: 칩에 구워진 불변의 코드. Apple Root CA 공개키가 들어있음.
2. **iBoot (LLB)**: Low Level Bootloader. 서명을 검증하고 커널을 로드합니다.
3. **Kernel Boot**: XNU 커널 초기화. 드라이버 로드.

#### 2. User Space 시작 (Launchd)
- **launchd (PID 1)**: 커널이 띄우는 첫 번째 유저 프로세스. 모든 프로세스의 조상입니다.
- `/System/Library/LaunchDaemons` 등의 설정을 읽어 시스템 데몬(syslogd, backboardd 등)을 실행합니다.

#### 3. 앱 실행 시퀀스 (App Launch Detail)
사용자가 아이콘을 탭하면 어떤 일이 일어날까요?

1. **Request**: SpringBoard(홈 화면)가 `launchd`에게 앱 실행 요청 (XPC/Mach IPC).
2. **Fork/Exec**: `launchd`가 `posix_spawn()` 시스템 콜 호출.
3. **Dyld**: 동적 링커(`dyld`)가 프로세스 메모리에 로드됨.
   - **Shared Cache Map**: `/System/Library/Caches/com.apple.dyld/`에 있는 거대한 시스템 프레임워크 뭉치(Shared Cache)를 공유 메모리에 매핑. (앱 실행 속도 핵심)
   - **Load Dylibs**: 앱이 사용하는 dylib들을 로드하고 심볼 바인딩(Rebase/Bind).
4. **Runtime Init**: Objective-C `+load` 메서드, Swift 런타임 초기화.
5. **Main**: `main()` 함수 호출 -> `UIApplicationMain` -> Run Loop 시작.

---

### 🛡️ 보안 모델 (Security Model)

#### 1. Code Signing & Entitlements
단순히 "누가 만들었나" 서명뿐만 아니라, **"무엇을 할 수 있는가"** 권한(Entitlements)을 바이너리에 박아넣습니다.
- 커널의 **AMFI (Apple Mobile File Integrity)** 데몬이 실행 시 강제 검사합니다.
- 예: `com.apple.developer.nfc.readersession.formats` 엔타이틀먼트가 없으면 NFC 하드웨어 접근 불가.

#### 2. Sandbox (Seatbelt)
앱이 파일 시스템의 어디를 읽고 쓸 수 있는지 커널 레벨에서 차단합니다.
- `Container` 디렉토리 내부에 `Documents/`, `Library/`, `tmp/` 등을 격리.
- 외부 접근 시 커널 패닉이나 'Operation not permitted' 에러 발생.

#### 3. TCC (Transparency, Consent, and Control)
사용자 프라이버시 데이터 접근 제어.
- 카메라, 마이크, 사진첩 접근 시 뜨는 팝업.
- `tccd` 데몬이 관리하며 데이터베이스로 권한 상태 저장.

---

### 🧱 플랫폼 아키텍처 차이

| Feature | macOS | iOS/iPadOS/visionOS |
|---------|-------|-------------------|
| **파일 시스템** | 사용자 접근 비교적 자유로움 (Finder) | 철저한 샌드박스 격리 |
| **메모리(Swap)** | 디스크 스왑 사용 (Compressor + Swap) | **Swap 없음** (Compressor + Jetsam) |
| **앱 생명주기** | 사용자가 종료할 때까지 유지 | 백그라운드 시 적극적으로 Suspend/Terminate |
| **권한 관리** | Gatekeeper, SIP, TCC | Code Signing, Provisioning Profile, TCC |

---

### 더 보기
- [[apple-foundations]] - 시스템 기초
- [[apple-uikit-lifecycle]] - 앱 수준의 생명주기
- [[apple-memory-management]] - 메모리 관리 상세: Jetsam과 Swap
