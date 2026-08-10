---
title: secure-operating-systems
tags: [operating-systems, security, reference-monitor, tcb, tpm, windows]
aliases: [Secure OS, 보안 운영체제, 운영체제 보안]
date modified: 2026-08-10
date created: 2026-01-08 10:15:25 +09:00
---

## 🌐 개요 (Overview)

**보안 운영체제(Secure OS)** 는 기존 운영체제의 보안 취약점을 보완하기 위해 **커널 수준에서 보안 기능을 강화**한 운영체제입니다. 이 문서는 보안 OS의 핵심 개념들로 안내하는 허브입니다.

---

## 🎯 보안 OS의 주요 개념

### 이론적 기초

**[참조 모니터와 TCB](reference-monitor-and-tcb.md)** 
- 참조 모니터: 모든 접근 요청을 중재하는 추상 머신
- TCB (Trusted Computing Base): 시스템 보안을 담당하는 하드웨어/펌웨어/소프트웨어의 총체
- 보안 커널: 참조 모니터의 실제 구현

### 하드웨어 보안

**[TPM 하드웨어 보안](tpm-hardware-security.md)**
- TPM (Trusted Platform Module): 암호화 키 생성/저장, 시스템 무결성 검증
- PCR (Platform Configuration Register): 부팅 과정의 무결성 측정값 저장
- 신뢰 체인 (Chain of Trust): 부팅 단계별 무결성 검증

### Windows 보안 구현

**[Windows 보안 서브시스템](windows-security-subsystem.md)**
- SAM (Security Account Manager): 사용자 계정 및 해시 저장
- LSA (Local Security Authority): 사용자 인증 및 토큰 생성
- SRM (Security Reference Monitor): 참조 모니터의 Windows 구현
- BitLocker: TPM 기반 디스크 암호화
- Windows 보안 이벤트 로그: 감사 로그 ID 상세 정보

### 접근 통제 모델

**[접근 통제 모델](../../security/fundamentals/access-control-models.md)** (DAC, MAC, RBAC)
- DAC (Discretionary Access Control): 소유자 중심의 임의적 통제
- MAC (Mandatory Access Control): 관리자 중심의 강제적 통제
- RBAC (Role-Based Access Control): 역할 기반의 권한 부여

---

## 💡 기존 OS의 보안 취약점

| 취약점 | 설명 | 해결책 |
|--------|------|--------|
| **root 권한 집중** | 하나의 계정이 모든 권한 보유 | 최소 권한 원칙 적용 |
| **DAC 한계** | 소유자가 권한 임의 변경 가능 | MAC 도입 |
| **취약한 인증** | 패스워드 기반 인증의 한계 | 다중 인증, 생체인증 |
| **커널 취약점** | 커널 버그 시 전체 시스템 침해 | 보안 커널, TCB 최소화 |

---

## 🎓 보안 OS의 목표

1. **최소 권한 원칙 (Principle of Least Privilege)**: 필요한 최소 권한만 부여
2. **강제적 접근 통제 (MAC)**: 시스템 정책에 의한 접근 제어
3. **감사 (Audit)**: 모든 보안 관련 활동 기록
4. **무결성 보장**: 시스템 및 데이터 변조 방지

---

## 🔗 연결 문서 (Related Documents)

- [kernel-structure](kernel-structure.md) - 커널 구조와 Dual Mode
- [selinux](../linux/security/selinux.md) - SELinux 상세 설명
- [linux-account-security](../linux/security/linux-account-security.md) - Linux 계정 보안
- [linux-log-management](../linux/security/linux-log-management.md) - Linux 로그 관리
