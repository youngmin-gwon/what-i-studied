---
title: apple-glossary
tags: [apple, glossary, ios, ipados, macos, visionos, watchos]
aliases: []
date modified: 2025-12-16 16:15:27 +09:00
date created: 2025-12-16 16:06:41 +09:00
---

## Apple OS Glossary (쉬운 설명) apple ios macos watchos ipados visionos glossary

기초 용어를 한 곳에 모았다. 다른 노트에서 모르는 말이 나오면 여기 링크 ([[apple-glossary#...]] ) 로 오면 된다.

- **Darwin**: macOS/iOS 의 땅바닥 (OS 커널 + 기초). XNU 커널과 BSD 유틸리티가 들어 있다.
- **XNU**: macOS/iOS 커널 이름. Mach 메시지와 BSD 를 섞었다.
- **Kext/DriverKit**: 하드웨어 드라이버. kext 는 커널 안에서, DriverKit 은 유저 공간에서 돈다.
- **Mach-O**: 실행 파일/라이브러리 포맷. 심볼/섹션/코드 서명이 담긴다.
- **dyld**: 런타임 로더. 앱이 켜질 때 라이브러리를 붙인다.
- **Code Signing**: 앱/라이브러리가 변조되지 않았는지 확인하는 서명.
- **Entitlement**: 앱이 쓸 수 있는 특별한 권한 목록. Info.plist 와 별도로 서명에 포함된다.
- **Sandbox**: 앱이 파일·네트워크·장치를 제한된 범위에서만 쓰게 하는 울타리.
- **TCC (Transparency, Consent, Control)**: 카메라/마이크/위치 같은 민감한 권한을 사용자에게 묻는 체계.
- **App Sandbox Container**: 앱 전용 폴더. Documents/Library/tmp 등으로 나뉜다.
- **Extension**: 앱 밖에서 작동하는 작은 모듈 (위젯, 공유 시트, Siri Intent 등).
- **XPC**: 프로세스 사이를 잇는 간단한 메시지 통로. 딕셔너리 형태로 주고받는다.
- **Grand Central Dispatch(GCD)**: 작업을 큐에 올려 스레드를 자동 관리하는 시스템.
- **Run Loop**: 이벤트를 받고 타이머를 돌리는 반복 루프. 메인 스레드는 UI 를 담당한다.
- **UIKit / AppKit / SwiftUI**: 화면을 만드는 도구. iOS/iPadOS 는 UIKit/SwiftUI, macOS 는 AppKit/SwiftUI.
- **Metal**: GPU 에 명령을 보내는 그래픽/컴퓨팅 API.
- **Scene**: iOS13+ 에서 하나의 창 (윈도우) 에 해당하는 단위. iPadOS/visionOS 멀티 윈도우에 중요.
- **Process / PID**: 실행 중인 프로그램 단위. 각자 PID 와 권한을 가진다.
- **Daemon**: 백그라운드에서 도는 시스템 서비스. launchd 가 관리한다.
- **launchd**: 서비스/에이전트를 시작·감시하는 관리자. plist 로 설정.
- **plist**: 설정/메타데이터를 담는 XML/바이너리 포맷.
- **ATS (App Transport Security)**: 기본 TLS 강제 규칙. 평문/낮은 TLS 를 막는다.
- **APNs**: 애플 Push 알림 서비스. 토큰으로 기기를 식별.
- **Keychain**: 비밀번호·토큰을 안전하게 보관하는 저장소.
- **Secure Enclave**: 별도 칩/프로세서. Touch ID/Face ID, 키 보호를 맡는다.
- **FileVault**: macOS 전 디스크 암호화. iOS 는 기본으로 데이터 보호가 켜져 있다.
- **Data Protection Class**: 파일이 언제 (잠금/해제) 접근 가능한지 정의하는 속성.
- **Power Assertions**: 기기가 잠들지 않게 잠시 잡아두는 요청. (iOS 의 [[android-glossary#wakelock|Wakelock]] 과 비슷)
- **Background Modes**: 백그라운드에서 허용되는 작업 종류 (오디오, 위치, VoIP, BLE 등).
- **Sideloading/TestFlight**: 앱을 스토어 밖 (개발/테스트) 에서 설치하는 방법.
- **App Store Review**: 앱이 스토어에 올라가기 전 검토 프로세스.
- **Provisioning Profile**: 어떤 기기/팀/권한으로 앱을 설치/디버그할 수 있는지 담은 문서.
- **Team ID / Bundle ID**: 개발자 팀 식별자 / 앱 고유 식별자.
- **Symbolication**: 크래시 보고서의 주소를 사람 읽을 수 있는 함수/파일로 바꾸는 과정.
- **Instruments**: 성능·메모리·에너지·네트워킹 등을 측정하는 도구 묶음.
- **Time Profiler / Allocations / Leaks**: Instruments 에서 자주 쓰는 프로파일러.
- **Crash Report**: 기기에서 나온 크래시 로그. UUID/DSYM 과 매칭해야 읽을 수 있다.
- **DSYM**: 디버그 심볼 파일. 비공개/릴리스 앱 분석에 필요.
- **Rosetta**: 다른 CPU 아키텍처용 바이너리를 번역 실행하는 계층 (Apple Silicon 에서 x86_64 앱 실행 시).
- **App Intent / SiriKit / Shortcuts**: 사용자가 음성·자동화로 앱 기능을 쓰게 하는 인터페이스.
- **WidgetKit / Live Activity**: 홈/잠금화면, 다이내믹 아일랜드 등에 정보를 보여주는 확장.
- **SceneKit / RealityKit / ARKit**: 3D/AR/VR/Spatial 앱을 만드는 도구.
- **Reality Composer Pro**: 비전 OS/AR 자산을 만드는 편집기.
- **Window Server**: macOS 의 창·레이어 관리 서비스.
- **Backboardd / SpringBoard**: iOS 에서 입력/애니메이션 (Backboardd) 과 홈 화면/런처 (SpringBoard) 를 맡는 데몬.
- **JetSam**: 메모리 부족 시 앱을 종료하는 정책 (안드로이드 LMKD 와 비슷한 역할).
- **JetsamEvent**: 메모리로 종료된 로그 기록.
- **Entrypoint**: 앱이 시작하는 함수. iOS 는 `@UIApplicationMain`/`@main` 에서 시작.
- **Bundle**: 리소스/바이너리가 들어 있는 디렉터리 구조 (.app/.framework/.appex 등).
- **Tweak/Hook (비공식)**: 탈옥 환경에서 함수를 갈아끼우는 것. 정식 앱은 사용할 수 없다.
