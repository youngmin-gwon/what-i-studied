---
title: play-integrity-token-is-server-verified-risk-signal-not-authorization
tags: ["android", "android/security-privacy"]
aliases: []
date modified: 2026-08-03 18:13:24 +09:00
date created: 2026-08-01 00:03:59 +09:00
---

## Play Integrity token 은 서버가 검증하는 위험 신호이지 권한 자체가 아니다

Play Integrity API 는 앱과 기기, 계정, 요청에 관한 무결성 verdict 를 제공한다. 클라이언트가 token 을 받았다는 사실만으로 신뢰 결론을 내리지 않고, token 은 서버에서 Google Play Developer API 로 검증한다.

request hash 나 nonce 는 token 을 특정 사용자 행동, 세션, 거래 요청에 묶기 위한 replay 방지 경계다. 서버는 검증된 verdict 와 자체 계정 권한, 위험 점수, rate limit, 거래 상태를 함께 판단한다.

무결성 결과는 authorization 을 대체하지 않는다. 기기가 신뢰 가능해 보여도 사용자가 해당 리소스를 볼 권한이 있는지, 요청이 정상 비즈니스 상태인지, 중복 실행이 아닌지는 서버가 별도로 검증해야 한다.

공식 문서: [Play Integrity API overview](https://developer.android.com/google/play/integrity/overview)

### 판단 기준

Platform security 노트는 앱 권한보다 낮은 계층에서 device integrity 와 mandatory policy 가 어떻게 강제되는지 판단하는 기준으로 읽는다.

### 경계

client-side check 를 authorization 으로 오해하지 않고 server verification, boot trust, sandbox boundary 를 분리한다.
