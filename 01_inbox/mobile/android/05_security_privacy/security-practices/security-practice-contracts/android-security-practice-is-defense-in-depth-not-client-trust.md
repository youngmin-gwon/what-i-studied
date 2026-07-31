---
title: "Android 보안 실무는 클라이언트 신뢰가 아니라 방어 계층 설계다"
tags: ["android", "android/security-privacy"]
---

# Android 보안 실무는 클라이언트 신뢰가 아니라 방어 계층 설계다

Android 보안 실무의 목적은 클라이언트를 완전히 신뢰하게 만드는 것이 아니라 공격 비용을 높이고 서버 검증 지점을 명확히 하는 것이다. 난독화, 루팅 탐지, 동적 분석 탐지, 무결성 검사는 모두 보조 신호다.

exported component, PendingIntent, deep link, ContentProvider, local storage는 각각 다른 입력 경계를 만든다. 민감 동작은 클라이언트에서 숨기는 것보다 서버 권한 검사, replay 방지, idempotency, 감사 로그로 보호한다.

Frida나 Drozer 같은 도구를 막는 코드는 우회될 수 있다. 따라서 앱 내부 방어는 조기 탐지와 abuse cost 상승 수단으로 보고, 실제 권한 결정은 backend, signing, Play Integrity, 데이터 암호화 정책과 함께 설계한다.

관련 노트: [Play Integrity token은 서버가 검증하는 위험 신호이지 권한 자체가 아니다](01_inbox/mobile/android/05_security_privacy/integrity-and-attestation/integrity-contracts/play-integrity-token-is-server-verified-risk-signal-not-authorization.md), [Android 민감 데이터는 암호화와 키 소유권을 함께 설계한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/sensitive-data-requires-encryption-and-key-ownership.md)

## 판단 기준

이 노트는 세부 절차를 모두 담기보다 Android 개념을 판단할 때 유지해야 하는 책임 경계를 고정한다.

## 경계

구현 디테일은 연결된 정본으로 넘기고, 이 노트에는 중복 설명보다 판단 기준을 남긴다.
