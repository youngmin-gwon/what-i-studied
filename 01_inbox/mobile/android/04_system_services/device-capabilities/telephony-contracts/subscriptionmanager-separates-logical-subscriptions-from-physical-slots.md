---
title: subscriptionmanager-separates-logical-subscriptions-from-physical-slots
tags: ["android", "android/system-services"]
aliases: ["SubscriptionManager는 멀티 SIM에서 논리적 구독과 물리 슬롯을 분리한다"]
date modified: 2026-08-06 14:59:18 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## SubscriptionManager는 멀티 SIM에서 논리적 구독과 물리 슬롯을 분리한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [텔레포니 접근 계약](./telephony-contracts.md)

### 핵심 정의

듀얼 SIM(또는 `eSIM`: embedded SIM, 물리 카드 교체 없이 소프트웨어 프로필로 회선을 변경하는 내장형 SIM 포함 멀티 SIM) 기기에서 `SubscriptionManager`(각 통신 회선 구독 정보를 관리하는 시스템 서비스)는 각 통신 회선을 "구독(subscription)"이라는 논리적 단위로 다룬다. 구독 ID는 물리적 SIM 슬롯 번호와 일대일로 고정되지 않는다. 사용자가 eSIM 프로필을 전환하거나 SIM을 교체하면 슬롯은 그대로여도 구독 ID가 바뀔 수 있다.

### 메커니즘

`TelephonyManager`의 기본 인스턴스는 시스템이 정한 기본 데이터/음성/SMS 구독을 대상으로 동작한다. 특정 SIM을 명시적으로 지정하려면 `TelephonyManager.createForSubscriptionId(subId)`로 해당 구독 전용 인스턴스를 얻어야 한다. `SubscriptionManager.getActiveSubscriptionInfoList()`로 현재 활성 구독 목록과 각 구독의 표시 이름, 캐리어 이름, slot index를 조회할 수 있다.

### 판단 기준

- 통화/SMS/데이터 관련 기능에서 "이 기기의 SIM"이라고 가정하지 않는다. 듀얼 SIM 기기에서는 항상 어떤 구독을 대상으로 하는지 명시할 수 있는 UX(발신 SIM 선택 등)를 고려한다.
- subscription ID를 캐싱해서 오래 재사용하지 않는다. eSIM 전환이나 SIM 교체로 ID가 바뀔 수 있으므로 `SubscriptionManager.addOnSubscriptionsChangedListener()`로 `OnSubscriptionsChangedListener`를 등록해 변경을 갱신한다.
- 슬롯 번호(물리적 위치)와 구독 ID(논리적 회선)를 혼동하지 않는다. UI에 "SIM 1/SIM 2"를 보여줄 때도 내부 로직은 구독 ID를 기준으로 동작해야 한다.

### 최소 안전 갱신 흐름

활성 목록 조회에는 `READ_PHONE_STATE` 또는 해당 구독의 carrier privilege가 필요할 수 있다. 목록을 한 번 읽고 끝내지 말고, 프로세스 수명에 맞춰 리스너를 등록·해제하면서 구독별 `TelephonyManager`를 다시 만든다.

```kotlin
val subscriptions = context.getSystemService(SubscriptionManager::class.java)
val telephony = context.getSystemService(TelephonyManager::class.java)

val listener = object : SubscriptionManager.OnSubscriptionsChangedListener() {
    override fun onSubscriptionsChanged() {
        val active = try {
            subscriptions.activeSubscriptionInfoList.orEmpty()
        } catch (_: SecurityException) {
            emptyList()
        } catch (_: UnsupportedOperationException) {
            emptyList()
        }

        val managers = active.associate { info ->
            info.subscriptionId to
                telephony.createForSubscriptionId(info.subscriptionId)
        }
        renderSubscriptions(active, managers)
    }
}

subscriptions.addOnSubscriptionsChangedListener(context.mainExecutor, listener)
// 소유 컴포넌트 종료 시 removeOnSubscriptionsChangedListener(listener)
```

빈 목록은 곧바로 "SIM 없음"을 뜻하지 않는다. 권한 부족, 호출자에게 보이는 활성 구독 없음, 텔레포니 기능 부재를 각각 구분해야 한다. 최신 SDK에서는 목록의 null 계약이 완화됐어도 구버전 호환 코드에서는 `orEmpty()`가 안전하다.

### 경계

- 이 노트는 구독과 슬롯의 데이터 모델을 다룬다. 조회 자체의 permission 계층은 [TelephonyManager 권한은 READ_PHONE_STATE와 READ_PHONE_NUMBERS로 세분화된다](./telephonymanager-permissions-split-into-phone-state-and-phone-numbers.md)가 다룬다.
- eSIM 프로필 다운로드/관리(GSMA RSP) 프로토콜 세부는 이 지도의 범위 밖이다.

### 관찰 가능한 신호

리스너 콜백 시점과 `subscriptionId` 집합을 로그로 남기고, `adb shell dumpsys telephony.registry` 또는 `adb shell dumpsys isub`의 활성 구독·슬롯 매핑과 대조한다. eSIM 전환 전후에 같은 슬롯의 ID가 바뀌고 구독별 콜백 대상도 갱신되는지 검증한다.

### 공식 문서

- https://developer.android.com/reference/android/telephony/SubscriptionManager

검증일: 2026-08-06. 활성 구독 목록은 권한 또는 carrier privilege를 요구할 수 있고, 노출되는 활성 구독 수가 바뀌면 `OnSubscriptionsChangedListener`로 통지된다는 계약을 확인했다.
