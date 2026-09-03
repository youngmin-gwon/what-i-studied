---
title: apple-privacy-and-tcc-details
tags: [apple, apple/privacy, apple/security, compliance, privacy, tcc]
aliases: ["TCC 는 런타임 사용자 동의 게이트이고 Privacy Manifest 는 심사 시점 선언이다", "TCC", "Privacy Manifests", "프라이버시와 TCC"]
date modified: 2026-09-03 00:00:00 +09:00
date created: 2025-12-18 16:21:20 +09:00
---

## TCC 는 런타임 사용자 동의 게이트이고 Privacy Manifest 는 심사 시점 선언이다

민감 자원 접근은 서로 다른 시점의 두 관문을 모두 통과해야 한다. **TCC(Transparency, Consent, Control)** 는 런타임에 사용자에게 묻고, 사용자가 언제든 설정에서 회수할 수 있다. **Privacy Manifest(`PrivacyInfo.xcprivacy`)** 는 빌드/심사 시점에 "무엇을 왜 수집하는지"를 선언하는 정적 계약이며, 서드파티 SDK 까지 포함한다. 둘을 혼동하면 "권한은 받았는데 심사에서 반려"되는 상황을 이해할 수 없다. 용어는 [apple-glossary](../00_foundations/apple-glossary.md).

### TCC 가 하는 일

- 카메라/마이크/사진/연락처/캘린더/리마인더/블루투스/위치/알림 등 민감 자원에 접근할 때 사용자에게 묻는다.
- 사용자가 허락/거부/한 번만 허락을 선택하면, 그 설정을 저장하고 앱 호출 때마다 검사한다.
- **Transparency**: 앱이 데이터를 사용하려는 이유를 투명하게 공개해야 한다 (`Info.plist` 의 Purpose String — `NSCameraUsageDescription`, `NSLocationWhenInUseUsageDescription` 등).
- **Consent**: 명시적인 사용자 동의 없이는 접근할 수 없다.
- **Control**: 사용자는 언제든지 설정에서 특정 앱의 권한을 회수할 수 있다. 즉 **한 번 받은 권한은 영구적이지 않다.**

### Privacy Manifests (iOS 17+, 필수)

과거엔 `Info.plist` 에 사용 목적(Usage Description)만 적으면 되었으나, 현재는 SDK 를 포함한 전사적 차원에서 `PrivacyInfo.xcprivacy` 작성이 의무화되었다. 지문 수집(Fingerprinting) 방지가 목적이다.

- 앱 및 타사 SDK 의 개인정보 수집 이유를 선언한다.
- **Required Reason API**: 파일 타임스탬프, 시스템 부팅 시각, 디스크 여유 공간, `UserDefaults` 등 지문 수집에 악용될 수 있는 API 는 사용 사유를 명시해야 한다.

### 권한 종류별 요약

- 카메라/마이크: 실시간 영상/음성. 백그라운드 사용은 제한적.
- 사진: 전체 라이브러리 vs 선택한 항목만(Limited Photo Library, iOS 14+). Photos picker 로 최소 권한 권장.
- 위치: 항상/앱 사용 시/정확도 낮춤. 백그라운드 위치는 별도 플래그 필요.
- 블루투스: 주변 기기 검색/연결. 광고/스캔은 배터리/프라이버시 고려.
- 알림: 배너/사운드/배지. iOS 15+ 는 시간 민감/크리티컬 알림 옵션.
- 연락처/캘린더/리마인더: 개인 정보. 최소 권한/선택 UI 제공.
- 헬스/피트니스/모션: HealthKit/WorkoutKit/모션 센서. 데이터 종류별로 더 엄격.
- 추적(IDFA): TCC 가 아닌 **ATT** 별도 프롬프트. [apple-app-tracking-privacy](apple-app-tracking-privacy.md) 참조.

### 사용자 경험 가이드

- 권한을 "필요할 때" 요청. 앱 실행 직후 남용 금지.
- 왜 필요한지 짧고 친절하게 설명. 실제 사용 시점과 문구가 일치해야 한다.
- 거부 시 대체 흐름 제공(읽기 전용/기능 축소), 설정으로 이동 버튼 제공.

### 데이터 최소화

- 필요한 필드만 요청/저장. 예: 연락처 전체 대신 이메일만.
- 서버로 보내기 전에 익명화/집계/토큰화.
- 진단/로그에 개인 정보 넣지 않기.

### 지역/정책

- GDPR/CCPA 등 법에 따라 데이터 접근/삭제/이동 요청을 처리할 수 있어야 한다.
- 아동/학생 대상 앱은 부모 동의/추적 제한을 철저히.
- 중국 등 일부 지역은 인증서/네트워크/지도 데이터 정책이 다를 수 있다.

### 테스트/디버깅 (관찰 가능한 증거)

```bash
# 시뮬레이터에서 권한 허용/거부/초기화
xcrun simctl privacy booted grant  camera com.example.app
xcrun simctl privacy booted revoke camera com.example.app
xcrun simctl privacy booted reset  all    com.example.app

# TCC 데몬 로그 스트리밍 (실기기/시뮬레이터)
log stream --predicate 'subsystem == "com.apple.TCC"' --info
```

- 실제 기기에서 한 번만 허용/정확도 낮춤/백그라운드 조합 모두 확인한다.
- 권한이 있는데도 API 가 실패한다면 TCC 가 아니라 sandbox profile 또는 entitlement 게이트일 수 있다. [apple-sandbox-and-security](apple-sandbox-and-security.md) 의 게이트 구분을 먼저 적용한다.

### 심사 대비 체크리스트 (App Store Core Requirements)

- 권한 설명 문구가 명확한가? (무엇을, 왜 쓰는지)
- 실제 기능과 권한 사용 타이밍이 맞는가? (앱 진입 즉시 묻는 패턴 리젝 대상)
- 거부 시 앱이 멈추지 않는가?
- **[필수]** 서드파티 SDK 를 포함하여 앱 내 데이터 추적이 일어나는가? 일어난다면 ATT 프롬프트 조치를 취했는가?
- **[필수]** `PrivacyInfo.xcprivacy` 에 Required Reason API 사용 사유를 명시했는가?

### 링크

- [apple-sandbox-and-security](apple-sandbox-and-security.md) - 커널 게이트와 런타임 진단
- [apple-app-tracking-privacy](apple-app-tracking-privacy.md) - ATT 와 IDFA
- [apple-system-services](../04_system_services/apple-system-services.md) - TCC 를 집행하는 시스템 데몬
- [apple-distribution-and-policies](../08_packaging_deployment/apple-distribution-and-policies.md) - 심사 정책과 반려 사유
- [apple-accessibility](../02_ui_frameworks/apple-accessibility.md)
