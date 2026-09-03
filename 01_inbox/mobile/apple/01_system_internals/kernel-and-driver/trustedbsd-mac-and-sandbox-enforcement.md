---
title: trustedbsd-mac-and-sandbox-enforcement
tags: [apple, apple/internals, apple/internals/kernel, mac-framework, sandbox, system-internals, trustedbsd]
aliases: ["TrustedBSD MAC 프레임워크가 sandbox 판정이 실제로 일어나는 지점이다", "TrustedBSD", "MAC Framework", "Sandbox 커널 집행"]
date modified: 2026-09-03 00:00:00 +09:00
date created: 2026-09-03 00:00:00 +09:00
---

## TrustedBSD MAC 프레임워크가 sandbox 판정이 실제로 일어나는 지점이다

### 개념 (What)

sandbox 는 라이브러리도, 사용자 공간 데몬도 아니다. **커널 안의 훅 지점**이다. XNU 는 파일 열기, 소켓 연결, 프로세스 생성 같은 주요 커널 연산마다 **TrustedBSD MAC 프레임워크**의 훅을 호출하고, 등록된 **정책 모듈**들이 그 연산을 허용할지 판정한다. Apple 의 Sandbox 는 그 정책 모듈 중 하나다.

이것이 **강제적 접근 제어(MAC)** 인 이유는 명확하다 — 프로세스가 자기 권한을 스스로 포기할 수는 있어도, 스스로 늘릴 수는 없다.

### 왜 필요한가 (Why)

1. **우회 불가능성**: 판정이 라이브러리 안에 있다면 그 라이브러리를 건너뛰면 그만이다. 시스템 콜 경로 안에 있으면 건너뛸 방법이 없다.
2. **`EPERM` 의 정확한 해석**: 코드가 맞는데 `Operation not permitted` 가 나온다면, 그것은 논리 오류가 아니라 **정책 모듈이 거부한 것**이다. 코드를 고칠 것이 아니라 프로필/entitlement 를 봐야 한다.
3. **게이트가 여러 개라는 사실**: MAC 정책, entitlement, TCC 동의는 각각 다른 계층이다. 하나가 통과해도 다른 것이 막을 수 있다.

### 내부 메커니즘 (How)

```mermaid
flowchart TD
    A["앱: open(\"/private/var/...\")"] --> SC["BSD 시스템 콜 진입"]
    SC --> HOOK["MAC 훅 호출<br/>mac_vnode_check_open"]
    HOOK --> POL["정책 모듈들이 순서대로 판정"]
    POL --> SBX["Sandbox 정책 모듈<br/>프로세스의 프로필과 대조"]
    POL --> AMF["AMFI 정책 모듈<br/>서명/entitlement 확인"]
    SBX --> DEC{"모든 정책이 허용?"}
    AMF --> DEC
    DEC -->|"Yes"| DO["실제 연산 수행"]
    DEC -->|"No"| ERR["EPERM 반환<br/>(+ 위반 로그 기록)"]

    style HOOK fill:#fff8e1,stroke:#f9a825,color:#f57f17
    style ERR fill:#ffe0e0,stroke:#c62828,color:#b71c1c
```

1. **프로필 적용**: 프로세스가 시작될 때 해당 sandbox 프로필이 커널에 로드된다. 프로필은 사람이 읽는 규칙이 아니라 **커널이 평가하는 컴파일된 형태**다.
2. **훅 평가**: 시스템 콜이 들어올 때마다 관련 훅에서 프로필과 대조한다. 모든 정책 모듈이 허용해야 통과한다 — **하나라도 거부하면 거부**다.
3. **로깅**: 거부는 시스템 로그에 남는다. 이것이 진단의 유일한 실마리인 경우가 많다.

### 세 개의 게이트를 구분하기

같은 "접근 실패"라도 원인이 다르면 처방이 다르다.

| 게이트 | 확정 시점 | 실패 증상 | 고치는 곳 |
| :--- | :--- | :--- | :--- |
| **Sandbox 프로필** | 프로세스 시작 | `EPERM`, 커널 로그에 sandbox 위반 | 접근 경로 자체를 바꾼다 (컨테이너 안으로) |
| **Entitlement** | 코드 서명 시 | API 가 실패하거나 실행 자체가 안 됨 | 프로비저닝/서명 재구성 |
| **TCC 동의** | 런타임 사용자 응답 | 프롬프트 거부 또는 조용한 빈 결과 | 사용자 재동의 유도 |

### 관찰 가능한 증거 (macOS)

```bash
# sandbox 거부 로그 실시간 확인
log stream --predicate 'senderImagePath CONTAINS "Sandbox"' --info

# 최근 sandbox 위반 검색
log show --last 5m --predicate 'eventMessage CONTAINS "deny"' --info

# 앱에 봉인된 entitlement 확인 (다른 게이트와 구분하기 위해)
codesign -d --entitlements :- /Applications/MyApp.app
```

iOS 기기에서는 `sysdiagnose` 를 수집해 그 안의 로그에서 같은 항목을 찾는다.

### 연관 문서

- [AMFI 는 exec 시점에 코드 서명과 entitlement 를 커널에서 강제한다](amfi-code-signature-enforcement.md)
- [XNU 는 Mach 가 자원을, BSD 가 인터페이스를 맡는 분업 구조다](xnu-mach-bsd-split.md)
- [apple-sandbox-and-security](../../05_security_privacy/apple-sandbox-and-security.md) - sandbox 진단과 다중 방어
- [apple-privacy-and-tcc-details](../../05_security_privacy/apple-privacy-and-tcc-details.md) - TCC 게이트

공식 문서: [App Sandbox](https://developer.apple.com/documentation/security/app-sandbox)
