---
title: apple-macos-desktop
tags: [apple, macos]
aliases: []
date modified: 2025-12-16 16:15:41 +09:00
date created: 2025-12-16 16:14:17 +09:00
---

## macOS Desktop Notes apple macos

macOS 앱을 만들 때 알아두면 좋은 기초를 쉽게 정리했다. 용어는 [[apple-glossary]].

### UI 프레임워크
- AppKit 이 기본. 메뉴바, 윈도우, 도크, 드래그앤드롭, 키보드 포커스 등 데스크탑 패턴을 제공.
- Catalyst/SwiftUI 로 iPad/iOS 앱을 맥으로 가져올 수 있다. 입력/메뉴/파일 접근을 추가로 고려해야 한다.

### 윈도우/메뉴
- 다중 창/다중 모니터, 풀스크린, 스페이스, 미션 컨트롤.
- 메뉴바/단축키/터치바 (일부 기기) 지원. `NSMenu`, `NSStatusItem` 로 메뉴를 만든다.

### 파일/샌드박스
- 샌드박스 앱은 Security-scoped bookmark 로 사용자가 고른 파일에만 접근 가능.
- 비샌드박스 앱은 더 넓은 접근이 가능하지만, Gatekeeper/노타리제이션이 필요.
- SSV(서명된 시스템 볼륨) 로 시스템 파일은 보호된다.

### 배포
- Mac App Store: 샌드박스 의무. IAP/업데이트가 쉬움.
- 외부 배포: 서명 + 노타리제이션 필수, 첫 실행 시 Gatekeeper 확인. 자동 업데이트는 Sparkle 등 사용.

### 하드웨어
- Apple Silicon/Intel 겸용 Universal 앱 또는 한쪽만 지원. Rosetta2 로 x86 실행 가능.
- 외장 GPU 는 지원 종료, Metal 을 기본으로 사용.
- 다양한 입력 (마우스/트랙패드/키보드), 단축키가 중요.

### 특화 프레임워크
- AppKit 전용: NSDocument(문서 기반), NSWorkspace(파일/앱 관리), Quick Look, Spotlight 인덱싱.
- Menu Bar Extra, Finder Sync Extension, System Extensions(네트워크/엔드포인트/드라이버) 등.

### 테스트/디버깅
- 여러 모니터/해상도/다크모드/언어에서 확인.
- Instruments/Activity Monitor/Console 로 CPU/GPU/메모리/로그를 확인.

### 링크

[[apple-build-and-distribution]], [[apple-sandbox-and-security]], [[apple-accessibility-and-internationalization]], [[apple-history-and-evolution]].
