---
title: apple-system-services
tags: [apple, launchd, systemservices]
aliases: []
date modified: 2025-12-16 16:15:49 +09:00
date created: 2025-12-16 16:13:15 +09:00
---

## System Services & Daemons apple systemservices launchd

각 플랫폼에서 공통/중요한 데몬과 서비스 역할을 쉽게 모았다. 용어는 [[apple-glossary]].

### launchd
- 모든 데몬/에이전트의 부모. plist(Load/OnDemand/KeepAlive/RunAtLoad/EnvironmentVariables 등) 로 설정.
- 시스템 영역 (/System/Library/LaunchDaemons), 사용자 영역 (~/Library/LaunchAgents) 으로 나뉜다.
- 크래시 시 재시작 정책, 리소스 제한, Mach 서비스 이름을 정의한다.

### 입력/창
- iOS: Backboardd(입력/애니메이션), SpringBoard(홈/앱 전환/알림), mediaserverd(오디오/비디오), imagent(FaceTime/iMessage).
- macOS: WindowServer(창/레이어 합성), Dock(런처/엑스포제), SystemUIServer(메뉴바), coreaudiod(오디오), distnoted/notifyd(노티), syspolicyd(SIP/서명 정책).
- watchOS: Carousel/SpringBoard, heart/fitness 데몬, 나침반/센서 데몬.
- visionOS: 공간 창/패스스루/센서 처리 데몬, Reality compositor.

### 네트워크
- configd/networkd: 인터페이스 설정, DHCP, DNS, 라우팅.
- apsd: [[apple-glossary#APNs|푸시 알림]] 데몬.
- neagent/networkextensiond: VPN/프록시/필터링 플러그인 실행.
- mDNSResponder: Bonjour/mDNS.

### 전원/배터리
- powerd: 슬립/웨이크/배터리 상태 관리. Low Power Mode 조정.
- aggregated/thermalmonitord: 온도/성능 제한.
- locationd: 위치 서비스, 배터리 사용량을 고려해 정확도/주기를 조정.

### 저장소/파일
- fseventsd: 파일 시스템 이벤트 스트림 제공.
- cloudd/bird: iCloud 동기화.
- fileproviderd: File Provider 확장 관리, on-demand 다운로드/업로드.

### 보안/프라이버시
- tccd: [[apple-glossary#TCC|TCC]] 권한 관리 (카메라/마이크/사진/연락처/캘린더 등).
- securityd/keychaind: Keychain 요청 처리.
- trustd: 인증서/신뢰 결정.
- amfid: 코드 서명 검증.

### 멀티미디어
- mediaserverd: 오디오/비디오 캡처/재생 파이프라인.
- avbdeviced: AVB/프로 오디오.
- videogamed: ProMotion/AR/카메라 파이프라인 일부를 처리.

### 헬스/피트니스
- healthd: 건강 데이터 집계 (iOS/watchOS).
- workoutsd: 운동 세션/센서 수집.
- gait/wrist detection: 착용 감지, 워크아웃 자동 감지.

### 백업/동기화
- mobilebackupd: iTunes/Finder 백업.
- periodic tasks: 백그라운드 앱 리프레시/푸시, Spotlight 인덱싱.

### 진단/로그
- logd: 통합 로그 수집. Console/`log stream` 으로 확인.
- analyticsd/awd: 크래시/성능/배터리 진단.
- sysdiagnose: 여러 로그/프로파일을 한 번에 모음.

### 문제 해결 체크리스트
- 서비스가 안 뜬다: launchctl print, 코드 서명/Entitlement, plist 경로/소유자/퍼미션 확인.
- 권한 팝업이 안 나온다: Info.plist 설명, TCC 기록 리셋 시뮬레이터 `xcrun simctl privacy`.
- 배터리 급소모: logd, thermalmonitord, locationd, 네트워크 데몬 활동 검사.

### 링크

[[apple-architecture-stack]], [[apple-sandbox-and-security]], [[apple-performance-and-debug]], [[apple-history-and-evolution]].
