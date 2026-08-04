---
title: play-billing-library-is-the-only-approved-in-app-purchase-path
tags: ["android", "billing", "play-policy"]
aliases: ["Play Billing Library는 Android 인앱 결제의 유일하게 승인된 경로다"]
date modified: 2026-08-04 18:00:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## Play Billing Library는 Android 인앱 결제의 유일하게 승인된 경로다

### 내부 메커니즘 (Internal Mechanism)

Google Play Developer Distribution Agreement 는 앱 내 기능이나 콘텐츠에 대한 결제가 필요하거나 허용되는 경우 Google Play의 결제 시스템, 즉 Play Billing Library 를 사용해야 한다고 규정한다. 이 요구사항은 가상 화폐, 구독, 광고 제거, 클라우드 소프트웨어 등 **디지털 상품과 서비스**에 적용된다. 물리적 상품/서비스(식료품, 의류, 운송, 항공권), 개인 간 송금, 온라인 경매, 실제 돈이 걸린 도박은 예외이며 다른 결제 수단을 쓸 수 있다. 일부 국가에서는 프로그램 등록 후 대체 결제 시스템을 병행할 수 있지만, 이는 별도 프로그램 승인이 필요한 예외이지 기본 규칙을 대체하지 않는다.

이 계약이 코드 레벨에서 강제되는 지점은 앱이 아니라 **Google Play 심사와 앱 게시 파이프라인**이다. 앱이 디지털 상품을 다른 결제 수단(자체 신용카드 결제, 웹뷰로 우회한 외부 결제 페이지 등)으로 판매하면 정책 위반으로 앱이 거부되거나 게시가 중단된다. 즉 `BillingClient` API를 안 쓴다고 즉시 빌드가 실패하는 것이 아니라, Play Console 심사와 정책 감사 단계에서 앱 배포 자체가 막힌다. 이는 Gradle 컴파일 타임 계약이 아니라 배포 정책 계약이라는 점에서 다른 Android API 제약과 다르다.

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
