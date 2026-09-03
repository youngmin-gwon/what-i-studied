---
title: apple-sandbox-and-security
tags: [apple, apple/security, apple/security/sandbox, mac, mobile-security, sandbox]
aliases: ["App Sandbox 는 커널 MAC 으로 기본 거부를 강제하고 런타임 진단이 그 위를 덮는다", "App Sandbox Model", "Apple 샌드박스와 보안 진단"]
date modified: 2026-09-03 00:00:00 +09:00
date created: 2026-04-06 17:50:00 +09:00
---

## App Sandbox 는 커널 MAC 으로 기본 거부를 강제하고 런타임 진단이 그 위를 덮는다

Apple 플랫폼의 보안은 두 개의 다른 층으로 이루어진다. 아래층은 **커널이 강제하는 App Sandbox**로, 앱이 무엇을 할 수 있는지를 프로세스 시작 시점에 확정한다. 위층은 **앱이 스스로 수행하는 런타임 진단(Security Diagnosis)** 으로, 샌드박스가 이미 깨진 환경(탈옥, 디버거 부착, 코드 패치)을 탐지한다. 두 층은 신뢰 주체가 다르므로 따로 다뤄야 한다 — 아래층은 커널을 믿고, 위층은 커널을 믿을 수 없을 때를 대비한다.

---

### 🛡️ 기본 철학: Deny by Default

Apple 플랫폼의 모든 앱은 명시적으로 허용되지 않은 상호작용이 불가능하다.

- 사용자가 직접 파일을 선택(Powerbox)하거나, 권한 매니페스트(Entitlements)에 명시되어야만 리소스 접근이 가능하다.
- `EPERM` (Operation not permitted) 에러가 발생한다면 코드 논리 오류가 아닌 샌드박스 정책 위반일 확률이 높다.

> [!TIP] 진단 구분
> 같은 "접근 실패"라도 게이트가 3 개다. **Sandbox profile 위반**(`EPERM`, 커널이 거부) / **Entitlement 누락**(서명 시점에 확정, 실행조차 안 되거나 API 가 `nil` 반환) / **TCC 미동의**(사용자 프롬프트, 런타임에 회수 가능). 어느 게이트인지 먼저 나눈 뒤 조사한다.

---

### ⚙️ 동작 메커니즘

1. **Sandbox Profile**: 앱 실행 시 커널은 해당 앱이 수행 가능한 동작(네트워크, 파일 읽기/쓰기 등)이 정의된 프로필을 로드한다.
2. **TrustedBSD MAC Framework**: 프로세스가 시스템 콜(`open`, `connect` 등)을 호출하면 커널 프레임워크가 이를 가로채 프로필과 대조한다. 이것이 **강제적 접근 제어(Mandatory Access Control, MAC)** 이며, 앱이 스스로 우회할 수 없는 이유다.
3. **Hardened Runtime (macOS)**:
   - 프로세스 인젝션 및 서명되지 않은 코드 로드를 차단한다.
   - `Library Validation`: Apple 이나 개발자 본인이 서명한 라이브러리만 로드하도록 강제한다.

---

### 📂 파일 접근 및 북마크 (Security-Scoped Bookmarks)

샌드박스 환경에서는 사용자가 `NSOpenPanel` 등으로 선택한 파일이라도, 앱을 재시작하면 접근 권한이 소실된다.

**해결책: Security-Scoped Bookmarks**

- 파일 URL 을 `BookmarkData` 로 변환하여 영구 보존한다.
- 다시 사용할 때는 `URL.startAccessingSecurityScopedResource()` 를 호출하여 일시적으로 권한을 획득해야 한다.

```swift
if url.startAccessingSecurityScopedResource() {
    defer { url.stopAccessingSecurityScopedResource() }
    // 파일 작업 수행
}
```

---

### 🚨 보안 진단 기법 (Security Diagnosis)

앱의 런타임 무결성을 보장하기 위해 개발자가 직접 구현하거나 시스템이 제공하는 공격 탐지 기술이다.

**1. 탈옥 탐지 (Anti-Jailbreak)**

- **파일 시스템 검사**: `Cydia`, `Sileo`, `/bin/bash` 등 특정 경로의 존재 여부 확인.
- **API 후킹 탐지**: `stat` 함수를 직접 호출(SVC Instruction)하여 표준 라이브러리가 오염되었는지 확인.
- **샌드박스 상태 확인**: 샌드박스 외부의 파일(예: `/private/jailbreak.txt`)을 생성할 수 있는지 테스트.

**2. 디버깅 및 분석 방지 (Anti-Debugging)**

- **ptrace(PT_DENY_ATTACH)**: LLDB 와 같은 디버거가 프로세스에 붙는 것을 거부한다.
- **sysctl 검사**: `P_TRACED` 플래그를 체크하여 현재 디버깅 중인지 확인.
- **isDebuggerPresent**: 런타임에 디버거가 활성화되어 있는지 주기적으로 모니터링.

**3. RASP (Runtime Application Self-Protection)**

- 앱 실행 중에 스스로의 메모리나 코드가 변조(Patching)되는지 감시하고, 탐지 시 즉시 종료하는 기법.

---

### 🧱 다중 방어 체계 (Defense in Depth)

Apple 은 샌드박스 외에도 여러 계층에서 보안을 강화한다.

- **AMFI (Apple Mobile File Integrity)**: 실행 파일의 서명과 Entitlements 를 커널 레벨에서 강제로 검증한다.
- **Memory Security**: **ASLR**(주소 공간 무작위화), **Stack Canary**(버퍼 오버플로우 방지), **NX**(데이터 영역 실행 방지) 등을 기본 적용한다.
- **PAC (Pointer Authentication Code)**: Apple Silicon 에서 포인터 변조를 하드웨어 수준에서 차단한다.

---

### 📚 연관 문서

- [apple-security-entitlements](apple-security-entitlements.md) - 권한 증명 및 프로비저닝 프로파일
- [apple-privacy-and-tcc-details](apple-privacy-and-tcc-details.md) - 프라이버시 승인 및 TCC 데몬 관리
- [apple-security-app-attest](apple-security-app-attest.md) - 앱 무결성 서버 검증
- [mobile-advanced-security-tips](../../cross-platform/mobile-advanced-security-tips.md) - 시니어용 보안 심화 팁 (RASP 구현 등)
- [apple-boot-flow-and-images](../00_foundations/apple-boot-flow-and-images.md) - Secure Boot 및 하드웨어 보안 근간
- [TrustedBSD MAC 프레임워크가 sandbox 판정이 실제로 일어나는 지점이다](../01_system_internals/kernel-and-driver/trustedbsd-mac-and-sandbox-enforcement.md) - 커널에서의 집행
- [AMFI 는 exec 시점에 코드 서명과 entitlement 를 커널에서 강제한다](../01_system_internals/kernel-and-driver/amfi-code-signature-enforcement.md)
