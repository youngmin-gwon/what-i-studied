---
title: mobile-android-foundation-security
tags: [android, android/security, hub]
aliases: [Android Security MOC]
date modified: 2026-04-05 17:43:42 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [[mobile-security]] > [[mobile-android-foundation-security]]

### Android Platform Foundation Security (MOC)

안드로이드 플랫폼의 보안은 하드웨어부터 앱 계층까지 여러 층의 보안 메커니즘이 협력하여 사용자 데이터와 시스템을 보호합니다. 이 문서는 각 핵심 보안 영역에 대한 인덱스 역할을 합니다.

---

#### 🛡️ Core Security Architecture (핵심 아키텍처)

안드로이드 보안의 근간을 이루는 시스템 레벨의 격리 기술입니다.

- [[android-security-sandbox]]: **UID 기반 격리** 및 파일 시스템/프로세스 독립성.
- [[android-security-selinux]]: **MAC (강제적 접근 통제)** 및 도메인 격리 정책.
- [[android-security-verified-boot]]: **Chain of Trust** 및 `dm-verity` 기반의 부팅 무결성.

---

#### 🔑 Access Control & Storage (접근 제어 및 저장소)

앱이 데이터에 접근하는 방식과 이를 보호하는 메커니즘입니다.

- [[android-security-permissions]]: **런타임 권한**, 일회성 권한 및 `AppOps` 제어.
- [[android-security-storage]]: **Scoped Storage**, **FBE (파일 기반 암호화)** 및 Direct Boot.
- [[mobile-android-secure-storage]]: **Android Keystore** 및 하드웨어 보안 모듈(StrongBox).

---

#### 🌐 Advanced Integrity & Practices (무결성 및 실무)

앱의 변조를 감지하고 보안을 강화하는 실무적 내용입니다.

- [[android-security-play-integrity]]: **Play Integrity API**를 활용한 앱/기기 무결성 검증.
- [[android-security-practices]]: **Frida/Drozer** 진단 대응 및 법규(**정통망법, 개인정보 보호법**) 준수.
- [[android-deep-links]]: 딥링크 보안 및 **App Links** 검증.

---

#### 📚 학습 로드맵 및 연관 문서
- [[mobile-security]]: 모바일 보안 전체 로드맵
- [[mobile-vulnerability-check]]: 취약점 진단 체크리스트
- [[android-apple-2026-comparison]]: 플랫폼 보안 비교 (2026)
