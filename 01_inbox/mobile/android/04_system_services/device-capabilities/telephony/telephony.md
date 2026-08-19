---
title: telephony
tags: ["android", "android/system-services"]
aliases: ["텔레포니 접근 계약"]
date modified: 2026-08-10 16:08:10 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## 텔레포니 접근 계약

이 지도는 통신 상태 조회 권한 계층, 멀티 SIM/구독 모델, 통신사 서명 기반 특권이라는 세 계약을 분리한다.

### 읽는 순서

1. [TelephonyManager 권한은 READ_PHONE_STATE와 READ_PHONE_NUMBERS로 세분화된다](./telephonymanager-permissions-split-into-phone-state-and-phone-numbers.md) 에서 필요한 정보에 맞는 최소 권한을 고른다.
2. [SubscriptionManager는 멀티 SIM에서 논리적 구독과 물리 슬롯을 분리한다](./subscriptionmanager-separates-logical-subscriptions-from-physical-slots.md) 에서 듀얼 SIM 기기의 데이터 모델을 본다.
3. [Carrier privilege는 런타임 권한 없이 통신사 서명 인증서로 부여된다](./carrier-privilege-is-granted-by-carrier-signed-certificates-not-runtime-permission.md) 에서 통신사 앱의 특권 모델을 본다.

### 문제 분류

| 증상 | 먼저 확인할 경계 |
| --- | --- |
| 전화번호/IMEI 조회가 실패 | 요청한 정보에 맞는 정확한 permission 인지(전체 조회는 대부분 시스템 앱 전용) |
| 듀얼 SIM 기기에서 통화/데이터가 엉뚱한 SIM 으로 감 | subscription ID 를 명시적으로 지정했는지 |
| 통신사 전용 기능이 일반 앱에서 실패 | carrier privilege 가 필요한 API 인지, UICC 인증서 서명이 있는지 |

### 책임 경계

- 대부분의 개인 식별 통신 정보(IMEI, 전화번호 등)는 Android 10 이후 일반 서드파티 앱이 조회할 수 없도록 강하게 제한됐다. 이 지도는 그 제한의 구조를 다루되, 우회 방법을 다루지 않는다.
- Carrier privilege 는 permission 시스템과 별도의 신뢰 경로이며, 사용자 승인이 아니라 SIM 에 내장된 통신사 서명으로 결정된다.

### 노트 목록

- [TelephonyManager 권한은 READ_PHONE_STATE와 READ_PHONE_NUMBERS로 세분화된다](./telephonymanager-permissions-split-into-phone-state-and-phone-numbers.md)
- [SubscriptionManager는 멀티 SIM에서 논리적 구독과 물리 슬롯을 분리한다](./subscriptionmanager-separates-logical-subscriptions-from-physical-slots.md)
- [Carrier privilege는 런타임 권한 없이 통신사 서명 인증서로 부여된다](./carrier-privilege-is-granted-by-carrier-signed-certificates-not-runtime-permission.md)

검증일: 2026-08-03. [TelephonyManager 문서](https://developer.android.com/reference/android/telephony/TelephonyManager)와 [UICC carrier privileges](https://source.android.com/docs/core/connect/uicc) 를 기준으로 확인했다.
