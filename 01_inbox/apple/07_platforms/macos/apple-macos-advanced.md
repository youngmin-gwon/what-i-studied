# macOS Advanced Notes #apple #macos #desktop

macOS 데스크탑 앱을 더 깊게 만들 때 필요한 내용을 쉽게 정리했다. 용어는 [apple-glossary](../../00_foundations/apple-glossary.md).

## 샌드박스 vs 비샌드박스
- Mac App Store 앱은 샌드박스 필수. 파일은 Security-scoped bookmark/파일 선택기로 접근.
- 비샌드박스 배포는 더 많은 권한이 있지만, [[apple-glossary#Code Signing|서명]]과 노타리제이션이 필요하고 Gatekeeper가 검사한다.
- 시스템 확장/드라이버/네트워크 확장은 별도 Entitlement/승인 절차가 필요.

## 파일/권한
- NSOpenPanel/NSSavePanel로 사용자가 선택한 경로만 접근. 재접근은 보안 북마크 필요.
- Full Disk Access/TCC 권한(예: 캘린더/연락처/스크린 녹화)은 사용자 설정에서 허용해야 한다.
- 스크린 녹화/입력 모니터링/오디오 캡처 권한이 필요한 앱은 명확한 안내가 중요.

## UI/UX
- 메뉴바/단축키/드래그앤드롭/컨텍스트 메뉴는 데스크탑 필수 요소.
- NSDocument/NSWorkspace로 문서 기반/파일 통합.
- Menubar Extra(상단 아이콘), Dock tile badge, Touch Bar(일부 기기) 지원 검토.
- 윈도우 관리: 탭, 풀스크린, 스페이스, 다중 모니터, Stage Manager(macOS 14+).

## 성능/전원
- 데스크탑은 전력 제약이 덜하지만, 발열/팬/배터리(노트북) 고려.
- Grand Central Dispatch QoS로 백그라운드 작업을 분리, 메인 스레드 UI 유지.
- Metal/Accelerate로 CPU 부하를 줄이고, App Nap/에너지 임팩트도 점검.

## 디버깅/배포
- Console/Unified Logging, Instruments, Activity Monitor, spindump/hang report.
- dSYM/Crash report 심볼리케이션, `lldb`/`sample`로 성능 진단.
- 노타리제이션: `notarytool`로 업로드 후 스테이플, Gatekeeper 우회 시도 금지.

## 자동화/스크립트
- AppleScript/Shortcuts/Automator, LaunchAgent/Daemon으로 작업 자동화.
- 샌드박스 앱은 Apple Event Entitlement가 필요.

## 가상화/컨테이너
- Virtualization.framework로 VM 생성. 하드웨어 가속/네트워크/디스크 공유 설정.
- Docker/컨테이너 사용 시 파일/네트워크 권한, 퍼포먼스 영향 고려.

## 개발/테스트
- 다양한 해상도/스케일/모니터 배치에서 UI 확인.
- SIP 켜짐/꺼짐, 샌드박스/비샌드박스, 인텔/Apple Silicon, Rosetta 실행 모두 테스트.
- 입력 장치(마우스/트랙패드/키보드/펜/게임패드) 다양성 체크.

## 링크
[apple-macos-desktop](../../../../../../../apple-macos-desktop.md), [apple-build-and-distribution](../../05_security_privacy/apple-build-and-distribution.md), [apple-sandbox-and-security](../../05_security_privacy/apple-sandbox-and-security.md), [apple-performance-and-debug](../../06_testing_performance/apple-performance-and-debug.md).
