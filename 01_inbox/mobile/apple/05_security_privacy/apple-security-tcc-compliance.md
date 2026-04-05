---
title: apple-security-tcc-compliance
tags: [apple, apple/security, compliance, privacy, tcc]
aliases: []
date modified: 2026-04-05 17:45:34 +09:00
date created: 2026-04-05 17:08:07 +09:00
---

## [[mobile-security]] > [[apple-security-tcc-compliance]]

### TCC & Privacy Compliance

프라이버시 중심의 사용자 동의 시스템인 **TCC (Transparency, Consent, and Control)**와 이를 준수하기 위한 법적 가이드라인입니다.

---

#### 🛡️ TCC (Transparency, Consent, and Control)

Apple 의 프라이버시 보호를 위한 핵심 프레임워크입니다.

- **Transparency**: 앱이 데이터를 사용하려는 이유를 투명하게 공개해야 합니다.
- **Consent**: 명시적인 사용자 동의 없이는 카메라, 마이크, 위치, 연락처에 접근할 수 없습니다.
- **Control**: 사용자는 언제든지 설정에서 특정 앱의 권한을 회수할 수 있습니다.

**Info.plist 의 Purpose String**

- 해당 속성을 구체적으로 작성해야 심사 거절을 피할 수 있습니다.
- `NSCameraUsageDescription`, `NSLocationWhenInUseUsageDescription` 등.

---

#### ⚖️ 개인정보 보호법 및 컴플라이언스

모바일 앱 배포 시 반드시 준수해야 할 법적 사항입니다.

1. **App Tracking Transparency (ATT)**: 광고 식별자(`IDFA`)를 수집하려면 반드시 사용자의 추적 동의를 얻어야 합니다.
2. **Limited Photo Library**: iOS 14+ 부터 사용자는 전체 사진첩 권한 대신 일부 사진만 선택하여 허용할 수 있습니다.
3. **App Privacy Manifesto**: 앱 및 타사 SDK 의 개인정보 수집 이유를 선언하는 파일이 필수적입니다. (2024+ 규정)

---

#### 🚨 보안 진단 기법 (Antis)

사용자 보안과 프라이버시를 지키는 기술적 대응입니다.

- **Anti-Jailbreak**: `stat` 호출을 통해 탈옥 여부를 확인하되, API 후킹을 방지하기 위해 `System Call`(`svc`)을 직접 사용하는 것이 권장됩니다.
- **Anti-Debugging**: `ptrace(PT_DENY_ATTACH)` 를 호출하여 상용 디버거(LLDB)의 부착을 차단합니다.

#### 연관 문서
- [[apple-security-sandbox]] - 샌드박싱 격리
- [[apple-security-app-attest]] - 무결성 검증
- [[mobile-advanced-security-tips]] - RASP 구현 팁
