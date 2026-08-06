---
title: G1-in-app-billing
tags: [topic-synthesis, in-app-billing, monetization, google-play]
aliases: [인앱 결제 (Google Play Billing), In-App Billing, Google Play Billing]
date created: 2026-08-04 16:00:00 +09:00
date modified: 2026-08-06 14:54:00 +09:00
---

## 인앱 결제 (Google Play Billing)
**Purpose Statement**: Google Play Billing 라이브러리를 통해 인앱 상품과 구독을 판매하고, 구매 상태를 안전하게 검증 및 관리하는 전체 과정을 조망한다.

### 1. 이 주제를 읽기 전에
- Google Play Console 계정과 앱 서명 방식
- 앱 배포 및 서명 구조
- 백엔드 서버와의 API 연동 및 보안 통신

### 2. 전체 조망도
```mermaid
flowchart TD
    App[Android App\nPlay Billing Library] -->|1. Request Purchase| Play[Google Play App]
    Play -->|2. Purchase Token| App
    App -->|3. Send Token| Backend[Backend Server]
    Backend -->|4. Verify API| GoogleAPI[Google Play Developer API]
    GoogleAPI -->|5. Valid Token| Backend
    Backend -->|6. Grant Entitlement\n& Acknowledge| App
```

### 3. 하위 개념 및 원자 노트 합성

**Play 배포와 결제 프로그램의 경계를 먼저 확인**
Google Play에서 배포되는 앱의 디지털 상품·서비스 결제에는 Google Play Billing이 기본 경로다. 그러나 2026년 현재 eligible app·region·program에 따라 alternative billing, user choice billing, external offers 같은 승인된 경로도 존재한다. 앱의 배포 채널, 사용자 Play country, 상품 유형, 프로그램 등록 여부를 확인하지 않고 모든 외부 결제를 정책 위반이라고 단정하지 않는다. 프로그램 API를 쓰는 경우에도 지원되는 Play Billing Library 버전, 정보 화면, backend reporting 같은 별도 계약을 따라야 한다.
- [Play billing 적용 여부는 상품, 사용자 지역, 등록 프로그램에 따라 결정된다](../../03_packaging_deployment/distribution/billing-contracts/play-billing-requirement-depends-on-product-region-and-enrolled-program.md)

**제품 및 구독의 수명 주기**
일회성 상품(In-app Products)과 정기 결제(Subscriptions)는 서로 다른 상태 및 수명 주기를 가집니다. 구독은 갱신, 취소, 유예 상태 등을 추적해야 합니다.
- [Product and subscription purchases have different lifecycles](../../03_packaging_deployment/distribution/billing-contracts/product-and-subscription-purchases-have-different-lifecycles.md)

**서버 측 검증을 권한 부여의 신뢰 경계로 사용**
클라이언트 callback만으로 entitlement를 부여하지 않는다. 보안 backend에서 purchase token과 purchase state를 확인하고, Real-time Developer Notifications와 주기적 reconciliation으로 환불·취소·갱신을 동기화하는 구성이 권장된다.
- [Server-side purchase token verification is required, not client judgment](../../03_packaging_deployment/distribution/billing-contracts/server-side-purchase-token-verification-is-required-not-client-judgment.md)

**구매 승인(Acknowledge)의 중요성**
결제 완료 후 3일 이내에 앱 또는 서버에서 구매 승인(Acknowledge)을 하지 않으면, 결제가 자동으로 환불되고 사용자의 권한이 회수됩니다.
- [Unacknowledged purchases are refunded within three days](../../03_packaging_deployment/distribution/billing-contracts/unacknowledged-purchases-are-refunded-within-three-days.md)

### 4. 이 주제와 연결된 Worked Example
- [08 Signed Artifact through Play Delivery to Update](../worked-examples/08-signed-artifact-through-play-delivery-to-update.md) (결제 및 배포 파이프라인 연관)

### 5. 이 주제와 연결된 Diagnostic Runbook
- [05 Background Work Delayed or Not Running](../diagnostic-runbooks/05-background-work-delayed-or-not-running.md) (서버 간 결제 상태 동기화 실패 시)
- [08 Install Update Failure](../diagnostic-runbooks/08-install-update-failure.md)

### 6. 더 깊이 들어갈 때 (Learning Spine)
- [03 Source to Installed Package](../learning-spine/03-source-to-installed-package.md) (Play Store 정책과 연관)
- [08 Data Storage Network and Offline Recovery](../learning-spine/08-data-storage-network-and-offline-recovery.md) (결제 내역의 안전한 로컬/서버 동기화)
- [09 Identity Permission and Independent Security Gates](../learning-spine/09-identity-permission-and-independent-security-gates.md) (위변조 방지와 검증 모델)

### 공식 근거

- [Google Play Billing integration](https://developer.android.com/google/play/billing/integrate)
- [External offers integration](https://developer.android.com/google/play/billing/external/integration)
- [Google Play 외부 결제 backend reporting](https://developer.android.com/google/play/billing/outside-gpb-backend)

검증일: 2026-08-06. 기본 Play Billing 경로와 지역·프로그램별 승인 경로를 구분했다.
