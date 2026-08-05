---
title: play-billing-library-is-the-only-approved-in-app-purchase-path
tags: ["android", "billing", "play-policy"]
aliases: ["Play Billing Library는 Android 인앱 결제의 유일하게 승인된 경로다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## Play Billing Library는 Android 인앱 결제의 유일하게 승인된 경로다

### 내부 메커니즘 (Internal Mechanism)

구글의 공식 배포 정책인 **Google Play Developer Distribution Agreement(구글 플레이 개발자 분배 협약)**는 안드로이드 앱 내부에서 사용자가 디지털 상품, 가상 화폐, 프리미엄 기능 해금, 구독 서비스 등을 구매할 때 반드시 구글의 공식 결제 클라이언트 SDK인 **Play Billing Library (`BillingClient`)**를 통해서만 결제를 처리해야 한다고 강제 규정한다. (물리적 실물 상품 배송, 택시/운송, 실생활 서비스 예약 등은 예외 정책 적용).

이 계약이 기술적으로 강제되는 지점은 Gradle 컴파일 타임이 아니라, 개발자가 AAB를 제출하는 **Google Play Console 심사 및 라이브 정책 감사 파이프라인**이다. 앱이 자체 결제 모듈(외부 웹뷰 신용카드 결제, 외부 PG 연동 등)로 디지털 콘텐츠를 우회 판매하다 적발될 경우 스토어 게시 거부, 앱 강제 차단, 계정 정지 조치가 단행된다.

`BillingClient` API는 런타임 환경에서 안드로이드 OS 커널의 **Binder IPC (Inter-Process Communication, 프로세스 간 통신)** 인프라를 통해 기기에 설치된 Google Play Store 시스템 앱 프로세스와 보안 RPC 통신을 주고받는다. 따라서 기기에 Google Play Store 앱이 존재하지 않거나 구글 계정으로 로그인되어 있지 않은 환경(예: 자체 커스텀 ROM, 특정 대륙 에코시스템)에서는 `startConnection()` 호출 시 `BILLING_UNAVAILABLE` 오류를 반환하며 인앱 결제 서비스 진입이 차단된다.

### 코드 예시 (BillingClient 초기화와 연결)

```kotlin
class BillingRepository(context: Context) : PurchasesUpdatedListener {

    private val billingClient = BillingClient.newBuilder(context)
        .setListener(this)
        .enablePendingPurchases(
            PendingPurchasesParams.newBuilder()
                .enableOneTimeProducts()
                .build()
        )
        .build()

    fun startConnection(onReady: () -> Unit) {
        billingClient.startConnection(object : BillingClientStateListener {
            override fun onBillingSetupFinished(result: BillingResult) {
                if (result.responseCode == BillingClient.BillingResponseCode.OK) {
                    onReady()
                }
            }

            override fun onBillingServiceDisconnected() {
                // 재연결 로직 없이는 이후 launchBillingFlow 호출이 모두 실패한다
            }
        })
    }

    override fun onPurchasesUpdated(result: BillingResult, purchases: List<Purchase>?) {
        if (result.responseCode == BillingClient.BillingResponseCode.OK && purchases != null) {
            purchases.forEach { handlePurchase(it) }
        }
    }

    private fun handlePurchase(purchase: Purchase) { /* ... */ }
}
```

`BillingClient` 는 내부적으로 Play Store 앱의 시스템 결제 서비스와 Binder IPC로 통신한다. Play Store 앱이 기기에 없거나 로그인되지 않으면 `startConnection` 자체가 `BillingResponseCode.BILLING_UNAVAILABLE` 로 실패한다 — 즉 이 경로는 Google Play 생태계 존재를 전제로 한다.

### 관측 가능 증거 (Observable Evidence)

```bash
# Play Console: Policy Center > 정책 상태에서 결제 정책 위반 여부 확인
# 위반 시 게시 콘솔에 다음과 유사한 경고가 노출된다:
#   "Your app allows users to pay for digital goods or services outside of Google Play's billing system."

# 클라이언트 측 연결 실패 로그
adb logcat -s BillingClient:* | grep BILLING_UNAVAILABLE
```

### 경계

- 이 노트는 "왜 우회할 수 없는가"만 다룬다. 상품/구독별 실제 purchase lifecycle 은 [상품과 구독은 서로 다른 purchase lifecycle을 가진다](product-and-subscription-purchases-have-different-lifecycles.md) 를 참조한다.
- Play App Signing, AAB 등 배포 아티팩트 계약은 [Play 릴리스와 배포 계약](../release-distribution-contracts/release-distribution-contracts.md) 이 다룬다. 이 노트는 결제 채널 정책만 다룬다.

관련 노트: [상품과 구독은 서로 다른 purchase lifecycle을 가진다](product-and-subscription-purchases-have-different-lifecycles.md), [Google Play Billing 계약](billing-contracts.md)
