---
title: android-security-practices
tags: [android, compliance, security, tools, vulnerability]
aliases: [Android Security Engineering, Drozer, Frida, 법규 준수]
date modified: 2026-04-05 17:43:37 +09:00
date created: 2026-04-05 16:29:38 +09:00
---

## [[mobile-security]] > [[android-security-practices]]

### Android Security Engineering & Compliance

이 문서는 안드로이드 앱의 보안을 진단하는 도구와 개발 단계에서 준수해야 할 법적 규제 및 실무 기법을 다룬다.

#### 1. 동적 분석 및 진단 도구

- **Frida**: 런타임에 JavaScript 를 삽입하여 함수 호출을 가로채거나 변조(Hooking)하는 도구.
    - *Defense*: 포트 스캔(27042), `ptrace` 안티 디버깅, 바이너리 섹션 무결성 검사.
- **Drozer**: 안드로이드 컴포넌트(`Activity`, `Provider`)의 유출 경로 및 인텐트 취약점을 탐색.
    - *Defense*: `android:exported="false"` 명시 및 서명 기반 권한(`signature`) 적용.

#### 2. 보안 코딩 모범 사례 (S-SDLC)

- **Input Validation**: `SQL Injection` 방지를 위해 반드시 `SelectionArgs` 바인딩 사용.
- **Secure Intent**: 민감한 데이터를 전송할 경우 명시적 인텐트(Explicit Intent)를 사용하고, `PendingIntent` 는 반드시 `FLAG_IMMUTABLE` 을 지정한다.
- **Log Management**: 프로덕션 빌드에서는 ProGuard/R8 도구를 사용하여 `Log.d` 등을 제거한다.

#### 3. 법규 및 컴플라이언스 (Compliance)

**대한민국 개인정보 보호법** 및 **정통망법** 준수 사항:

- **접근권한 고지**: 필수적 접근권한(앱 실행 필수)과 선택적 접근권한(거부 가능)을 명확히 구분하여 사용자에게 동의를 받아야 한다.
- **민감정보 보호**: 주민번호, 계좌번호 등은 단말기에 평문으로 저장할 수 없으며, 반드시 [[android-security-storage]] 의 Keystore 암호화가 적용되어야 한다.

#### 연관 문서

- [[mobile-vulnerability-check]] - 상세 체크리스트
- [[android-security-play-integrity]] - 무결성 검증의 실무 적용
