---
title: car-app-library-restricts-content-to-approved-templates
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-08-03 17:29:10 +09:00
---

## Car App Library 는 운전 중 배포 콘텐츠를 제한된 템플릿으로만 허용한다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](../../android-platforms-and-form-factors.md)

관련 지도: [Android Auto/Automotive 계약](./auto-contracts.md)

### 핵심 정의

Jetpack 의 Car App Library 는 앱이 임의의 View/Compose 레이아웃을 차량 화면에 그리는 것을 허용하지 않는다. 대신 시스템이 미리 정의한 템플릿(목록, 지도, 내비게이션, 메시지 등)에 데이터를 채워 넣는 방식으로만 화면을 구성하게 강제한다. 실제 렌더링은 차량 헤드유닛(또는 Android Auto 호스트)이 수행한다.

### 메커니즘 및 `Screen` 템플릿 구현

앱은 `CarAppService` 및 `Session` 을 정의하고, `Screen` 객체에서 `ListTemplate`, `NavigationTemplate` 같은 호스트 승인 템플릿을 생성해 반환한다.

```kotlin
class MyCarAppService : CarAppService() {
    override fun createHostValidator(): HostValidator =
        HostValidator.ALLOW_ALL_HOSTS_VALIDATOR

    override fun onCreateSession(): Session = object : Session() {
        override fun onCreateScreen(intent: Intent): Screen {
            return MainPoiScreen(carContext)
        }
    }
}

class MainPoiScreen(carContext: CarContext) : Screen(carContext) {
    override fun onGetTemplate(): Template {
        val listBuilder = ItemList.Builder()
            .addItem(
                Row.Builder()
                    .setTitle("EV Charging Station #1")
                    .addText("Available • 150kW DC Fast")
                    .build()
            )

        return ListTemplate.Builder()
            .setSingleList(listBuilder.build())
            .setTitle("Nearby Stations")
            .setHeaderAction(Action.BACK)
            .build()
    }
}
```

### 판단 기준

- 임의의 커스텀 UI 가 필요한 기능은 Car App Library 로 구현할 수 없다는 것을 전제로 제품 요구사항을 잡는다. 이는 버그가 아니라 운전 중 주의 분산을 막기 위한 의도된 제약이다.
- 앱이 지원하려는 카테고리(내비게이션, 파킹, 충전, 메시징 등)에 따라 Google 의 앱 카테고리 검토를 통과해야 배포 및 화이트리스트 등록이 가능하다는 점을 출시 일정에 반영한다.
- 텍스트/목록 길이 제한을 미리 확인해 서버에서 넘어오는 데이터가 잘리지 않고 핵심 정보를 우선 배치하도록 설계한다.

### 경계

- 이 노트는 화면 구성 제약을 다룬다. 두 플랫폼(투영형/내장형)의 근본적 차이는 [Android Auto는 투영이고 Android Automotive OS는 차량에 내장된 독립 OS다](./android-auto-is-projection-android-automotive-os-is-an-embedded-os.md) 가 다룬다.
- 일반 Android 앱의 Play 배포/심사 절차 자체는 `03_packaging_deployment` 가 다룬다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 1. CarAppService 바인딩 상태 및 호환 세션 덤프
adb shell dumpsys activity service CarAppService

# 2. 템플릿 제약(Driver Distraction Rules) 이반 로그캣 모니터링
adb logcat -v threadtime | grep -E "CarAppHost|DriverDistraction|TemplateRestriction"
```

### 공식 문서

- https://developer.android.com/training/cars/apps
- https://developer.android.com/reference/androidx/car/app/model/package-summary

