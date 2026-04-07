---
title: apple-sandbox-and-security
tags: [apple, apple/security, mobile-security, sandbox]
aliases: [apple-security-models, apple-sandbox-and-security, App Sandbox Model, 보안 모듈]
date modified: 2026-04-06 18:13:28 +09:00
date created: 2026-04-06 17:50:00 +09:00
---

## [[mobile-security]] > [[apple-sandbox-and-security]]

### Apple Sandbox & Security Diagnosis

Apple 플랫폼의 보안은 격리된 실행 환경인 **App Sandbox** 와 시스템 무결성을 보호하기 위한 실시간 **보안 진단(Security Diagnosis)** 기법의 결합으로 완성됩니다. 앱이 시스템 리소스에 접근하는 커널 수준의 차단과, 외부 공격(탈옥, 디버깅)으로부터 앱 자체를 보호하는 전략을 다룹니다.

---

#### 🛡️ 메커니즘: App Sandbox (Seatbelt)

모바일 플랫폼(iOS/iPadOS)의 모든 앱은 **Container** 라는 격리된 공간 내에서만 동작하며, 외부 리소스 접근은 **Seatbelt** 엔진이 관리하는 정책(Sandbox Profile)에 따라 철저히 통제됩니다.

1. **MAC (Mandatory Access Control)**: 사용자 권한과 상관없이 커널이 강제로 리소스 접근을 제한하는 방식입니다. **TrustedBSD MAC** 프레임워크를 기반으로 합니다.
2. **Entitlements (권한 명세)**: 앱이 샌드박스를 넘어서 특정 시스템 기능(Push, iCloud, HealthKit 등)을 사용하겠다고 선언한 명세서입니다. Code Signing 시 포함되어 위변조가 불가능합니다.
3. **Container 격리**:
    - **Bundle Container**: 앱의 바이너리와 정적 리소스가 포함된 읽기 전용 영역.
    - **Data Container**: 앱이 생성한 데이터를 저장하는 영역 (`Documents`, `Library`, `tmp`).
    - **Cloud Container**: iCloud 싱크를 위한 전용 영역.

---

#### 🚨 보안 진단 기법 (Security Diagnosis)

앱의 런타임 무결성을 보장하기 위해 개발자가 직접 구현하거나 시스템이 제공하는 공격 탐지 기술입니다.

**1. 탈옥 탐지 (Anti-Jailbreak)**

- **파일 시스템 검사**: `Cydia`, `Sileo`, `/bin/bash` 등 특정 경로의 존재 여부 확인.
- **API 후킹 탐지**: `Stat` 함수를 직접 호출(SVC Instruction)하여 표준 라이브러리가 오염되었는지 확인.
- **샌드박스 상태 확인**: 샌드박스 외부의 파일(예: `/private/jailbreak.txt`)을 생성할 수 있는지 테스트.

**2. 디버깅 및 분석 방지 (Anti-Debugging)**

- **ptrace(PT_DENY_ATTACH)**: LLDB 와 같은 디버거가 프로세스에 붙는 것을 거부합니다.
- **sysctl 검사**: `P_TRACED` 플래그를 체크하여 현재 디버깅 중인지 확인.
- **isDebuggerPresent**: 런타임에 디버거가 활성화되어 있는지 주기적으로 모니터링.

**3. RASP (Runtime Application Self-Protection)**

- 앱 실행 중에 스스로의 메모리나 코드가 변조(Patching)되는지 감시하고, 탐지 시 즉시 종료하는 기법입니다.

---

#### 🧱 다중 방어 체계 (Defense in Depth)

Apple 은 샌드박스 외에도 여러 계층에서 보안을 강화합니다.

- **AMFI (Apple Mobile File Integrity)**: 실행 파일의 서명과 Entitlements 를 커널 레벨에서 강제로 검증합니다.
- **Memory Security**: **ASLR**(주소 공간 무작위화), **Stack Canary**(버퍼 오버플로우 방지), **NX**(데이터 영역 실행 방지) 등을 기본 적용합니다.
- **PAC (Pointer Authentication Code)**: Apple Silicon 에서 포인터 변조를 하드웨어 수준에서 차단합니다.

---

#### 📚 연관 문서

- [[apple-security-sandbox]] - 샌드박스 기본 개념 및 MAC 프레임워크
- [[apple-security-entitlements]] - 권한 증명 및 프로비저닝 프로파일
- [[apple-security-tcc-compliance]] - 프라이버시 승인 및 TCC 데몬 관리
- [[mobile-advanced-security-tips]] - 시니어용 보안 심화 팁 (RASP 구현 등)
- [[apple-boot-flow-and-images]] - Secure Boot 및 하드웨어 보안 근간
