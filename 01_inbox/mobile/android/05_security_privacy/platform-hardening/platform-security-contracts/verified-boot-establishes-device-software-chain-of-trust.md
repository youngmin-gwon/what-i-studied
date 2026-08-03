---
title: verified-boot-establishes-device-software-chain-of-trust
tags: ["android", "android/security-privacy"]
aliases: []
date modified: 2026-08-03 18:14:19 +09:00
date created: 2026-08-01 00:03:59 +09:00
---

## Verified Boot 는 기기 소프트웨어의 chain of trust 를 만든다

Verified Boot 는 bootloader, kernel, system partition 같은 기기 소프트웨어가 신뢰된 서명과 해시 체인을 따라 로드되었는지 확인한다. Android Verified Boot 는 부팅 과정과 dm-verity 기반 검증으로 시스템 변조를 탐지한다.

앱 관점에서 Verified Boot 는 앱 내부 보안 로직이 아니라 기기 신뢰도의 바탕이다. Play Integrity 같은 attestation 결과는 이 기기 상태를 포함한 신호를 서버가 판단할 수 있게 해준다.

Verified Boot 가 앱의 authorization 을 대신하지는 않는다. 기기가 green state 에 가깝더라도 사용자의 서버 권한, 세션, 거래 위험은 별도로 검증해야 한다.

공식 문서: [Verified Boot](https://source.android.com/docs/security/features/verifiedboot)

### 판단 기준

Platform security 노트는 앱 권한보다 낮은 계층에서 device integrity 와 mandatory policy 가 어떻게 강제되는지 판단하는 기준으로 읽는다.

### 경계

client-side check 를 authorization 으로 오해하지 않고 server verification, boot trust, sandbox boundary 를 분리한다.
