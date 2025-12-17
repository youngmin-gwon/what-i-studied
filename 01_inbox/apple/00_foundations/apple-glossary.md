---
title: apple-glossary
tags: [apple, glossary, reference, terms, dictionary]
aliases: []
date modified: 2025-12-18 03:00:00 +09:00
date created: 2025-12-16 16:06:41 +09:00
---

# Apple Developer Glossary

"애플 문서를 읽는데 외계어 같아요."
이 문서는 단순한 사전이 아닙니다. Apple 생태계에서 사용되는 **핵심 용어의 맥락(Context)**을 설명합니다.
이 용어들을 알면 문서가 보이고, 로그가 읽히고, 에러의 원인이 보입니다.

---

## 🏗️ Architecture & Kernel (기반)

이 시스템이 어떻게 돌아가는지 이해하기 위한 용어들입니다.

### **Darwin**
- **정의**: macOS, iOS, watchOS, visionOS의 뿌리가 되는 오픈소스 유닉스 운영체제입니다.
- **Context**: 터미널에서 `ls`, `cd`, `ps` 같은 명령어가 먹히는 이유입니다. iOS는 예쁜 껍데기를 쓴 유닉스입니다.
- **Deep Dive**: [[apple-architecture-stack#Core OS Layer]]

### **XNU (X is Not Unix)**
- **정의**: Darwin의 커널입니다. Mach 마이크로커널(메시지 전달)과 BSD(파일/네트워크)를 섞었습니다.
- **Context**: 앱이 느리거나 죽을 때 "Mach Message"나 "BSD System Call" 관련 로그가 보이면 커널 레벨의 문제입니다.

### **Sandbox**
- **정의**: 앱을 가두는 울타리입니다. 앱은 자신의 컨테이너(폴더) 밖으로 나갈 수 없습니다.
- **Context**: 파일을 저장했는데 파일 앱에서 안 보이나요? 샌드박스 규칙 때문입니다. 다른 앱과 대화하려면 XPC나 App Group 같은 공식 통로를 써야 합니다.
- **Deep Dive**: [[apple-sandbox-and-security]]

### **Daemon (데몬)**
- **정의**: 백그라운드에서 조용히 도는 시스템 서비스입니다. 이름 끝에 `d`가 붙습니다 (`locationd`, `bluetoothd`, `backboardd`).
- **Context**: 내 앱이 위치를 못 잡는다면 `locationd`가 죽었거나 권한 문제일 수 있습니다. 시스템 로그에서 이 데몬들의 이름을 찾아보세요.

---

## 📦 App Structure (앱 구조)

앱이 어떻게 포장되고 설치되는지 설명합니다.

### **Bundle (번들)**
- **정의**: 실행 파일, 이미지, 소리, 서명 등을 하나로 묶은 디렉터리입니다 (`.app`).
- **Context**: 파인더에서는 파일처럼 보이지만 우클릭 > "패키지 내용 보기"를 하면 폴더임이 드러납니다. 리소스 로딩(`Bundle.main.url`)은 이 폴더 안을 뒤지는 것입니다.

### **Info.plist**
- **정의**: 앱의 신분증이자 설정 파일입니다.
- **Context**: "카메라 권한 팝업이 안 떠요" -> 99% 확률로 `Info.plist`에 설명 문구(`Privacy - Camera Usage Description`)를 안 적어서 그렇습니다.

### **Entitlement (엔타이틀먼트)**
- **정의**: "이 앱은 iCloud를 쓸 수 있음", "Push 알림을 받을 수 있음" 같은 특수 권한 목록입니다. 코드 서명에 박제됩니다.
- **Context**: 코드는 완벽한데 기능이 안 된다면 `Signing & Capabilities` 탭을 확인하세요. 이 "딱지"가 없으면 OS가 API 호출을 거절합니다.
- **Deep Dive**: [[apple-sandbox-and-security#Entitlements]]

---

## 🎨 UI & Graphics (화면)

화면에 픽셀을 그리는 과정과 관련된 용어입니다.

### **WindowServer**
- **정의**: 여러 앱이 그린 화면을 모아서 최종적으로 디스플레이에 합성해 주는 시스템 프로세스입니다.
- **Context**: 맥이 버벅거릴 때 활성 상태 보기에서 `WindowServer` CPU가 높다면, 너무 많은 투명 효과나 그래픽 부하가 원인입니다.

### **Scene**
- **정의**: iOS 13부터 도입된 개념으로, 앱의 "UI 인스턴스" 하나를 의미합니다.
- **Context**: 아이패드에서는 한 앱이 두 개의 창(Scene)을 띄울 수 있습니다. `AppDelegate`가 아니라 `SceneDelegate`에서 UI 초기화를 해야 하는 이유입니다.
- **Deep Dive**: [[apple-app-lifecycle-and-ui]]

### **Main Run Loop**
- **정의**: 터치, 이벤트, 화면 갱신을 처리하는 무한 루프입니다. 메인 스레드에서 돌아갑니다.
- **Context**: "앱이 멈췄어요" -> 메인 런루프에서 무거운 작업(JSON 파싱, DB 읽기)을 했기 때문입니다. UI는 오직 메인 런루프에서만 고쳐야 합니다.

---

## ⚡️ Concurrency & Runtime (실행)

코드가 실제로 어떻게 실행되는지 설명합니다.

### **GCD (Grand Central Dispatch)**
- **정의**: 작업을 큐(Queue)에 넣으면 시스템이 알아서 스레드를 만들어 처리해 주는 기술입니다 (`DispatchQueue`).
- **Context**: 직접 스레드를 만들지 마세요. GCD가 CPU 코어 수에 맞춰 최적으로 조절해 줍니다. 이제는 Swift Concurrency (`Task`)로 넘어가는 추세입니다.
- **Deep Dive**: [[apple-gcd-deep-dive]]

### **dyld (Dynamic Link Editor)**
- **정의**: 앱이 켜질 때 필요한 라이브러리(UIKit, Foundation 등)를 연결해 주는 로더입니다.
- **Context**: 앱 실행 속도(Launch Time)를 줄이려면 dyld가 할 일을 줄여야 합니다 (사용하지 않는 프레임워크 링크 해제).

### **Retain Cycle (순환 참조)**
- **정의**: A가 B를 잡고, B가 A를 잡아서 메모리가 해제되지 않는 상황입니다 (메모리 누수).
- **Context**: `weak self`를 써야 하는 이유입니다. 메모리 누수가 쌓이면 앱이 결국 강제 종료(OOM)됩니다.
- **Deep Dive**: [[apple-memory-management]]

---

## 🔐 Security & Privacy (보안)

### **Keychain**
- **정의**: 암호화된 시스템 데이터베이스입니다. 앱을 지워도 남습니다.
- **Context**: `UserDefaults`에 비밀번호 저장하지 마세요. 탈옥된 폰에서는 다 보입니다. 중요 정보는 무조건 키체인입니다.
- **Deep Dive**: [[apple-keychain-biometrics]]

### **TCC (Transparency, Consent, and Control)**
- **정의**: "카메라에 접근하려고 합니다" 팝업을 띄우고 사용자의 허락을 관리하는 시스템입니다.
- **Context**: 사용자가 한 번 거절하면 앱 내에서 다시 팝업을 띄울 수 없습니다. 설정 앱으로 유도해야 합니다.
- **Deep Dive**: [[apple-privacy-and-tcc-details]]

---

## 🛠️ Tools (도구)

### **Instruments**
- **정의**: 성능 분석 도구 종합 선물 세트입니다. (Time Profiler, Leaks, Network...)
- **Context**: "앱이 느려요"라고 감으로 찍지 말고, Instruments를 돌려서 "이 함수가 300ms 걸립니다"라고 말해야 합니다.
- **Deep Dive**: [[apple-instruments-profiling]]

### **TestFlight**
- **정의**: 앱스토어 배포 전에 베타 테스터에게 앱을 뿌리는 공식 도구입니다.
- **Context**: 개발 빌드(Debug)와 배포 빌드(Release)는 다릅니다. 꼭 TestFlight(Release) 환경에서 테스트해야 실제 버그를 잡을 수 있습니다.
