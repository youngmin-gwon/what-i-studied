---
title: appwidgetprovider-lifecycle-runs-through-broadcasts-not-a-persistent-process
tags: [android, android/app-widgets]
aliases: ["AppWidgetProvider lifecycle은 지속 프로세스가 아니라 broadcast로 갱신된다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## AppWidgetProvider lifecycle은 지속 프로세스가 아니라 broadcast로 갱신된다

AppWidgetProvider(또는 Glance 의 `GlanceAppWidgetReceiver`)의 생명주기는 메인 UI Activity 처럼 메모리에 상주하면서 화면 갱신을 지속적으로 처리하는 프로세스 생명주기가 아니다. 위젯의 갱신 신호는 OS 및 시스템 서비스(`AppWidgetManager`)가 발행하는 **Broadcast Intent**를 통해 순간적으로 수신되며, 브로드캐스트 리시버 실행 타임아웃 예산(약 10초) 내에서 처리되고 즉시 프로세스가 회수 대기 상태로 전환되는 짧은 수명 계약을 갖는다.

---

### 1. 개념 및 핵심 명제 (What)

- **이벤트 전용 짧은 생명주기 (Short-lived Event Lifecycle)**: `AppWidgetProvider` 는 `BroadcastReceiver` 를 상속받은 특수 컴포넌트다. 위젯 갱신 이벤트(`ACTION_APPWIDGET_UPDATE`), 생명주기 변경(`onEnabled`, `onDisabled`, `onDeleted`, `onRestored`) 시점에만 인스턴스가 동적으로 생성되고 execution 콜백이 끝나면 바로 파기 대상이 된다.
- **현대 표준 GlanceAppWidgetReceiver**: Jetpack Glance 도 이 브로드캐스트 기반 생명주기 원칙을 그대로 따른다. `GlanceAppWidgetReceiver` 는 `BroadcastReceiver` 를 상속받아 `ACTION_APPWIDGET_UPDATE` 신호를 받으면 내장 코루틴 렌더러를 통해 `GlanceAppWidget.provideGlance()` 를 실행하고 `RemoteViews` 를 발행한다.

---

### 2. 왜 지속 프로세스가 아닌가? (Why)

1. **시스템 리소스 보존 (Battery & Memory Optimization)**: 홈 화면 위젯은 기기 부팅 시점부터 상시 노출될 수 있다. 모든 설치된 앱의 위젯이 별도 실행 프로세스나 바인딩된 서비스(Bound Service)를 유지한다면 Background Process Limit 을 초과하여 스마트폰 사용이 불가능해진다.
2. **비동기 이탈 및 작업 위임 (Asynchronous Delegation)**: 위젯 update 콜백(`onUpdate` / Glance `provideGlance`) 내에서 동기적 네트워크 IO 나 중량 DB 쿼리를 수행하면 시스템은 리시버 타임아웃을 감지하여 ANR(Application Not Responding)을 유발하거나 프로세스를 강제 종료한다. 따라서 비동기 데이터 로딩은 **WorkManager**로 위임하고 결과가 준비되었을 때 위젯을 명시적으로 재갱신해야 한다.

---

### 3. 내부 메커니즘 (How)

```mermaid
sequenceDiagram
    participant Host as "AppWidgetHost (Launcher)"
    participant AWM as "AppWidgetManager (System Server)"
    participant App as "앱 프로세스 (없을 경우 임시 생성)"
    participant Provider as "GlanceAppWidgetReceiver / AppWidgetProvider"
    participant WM as "WorkManager (비동기 작업)"

    Host->>AWM: "위젯 갱신 주기 도달 또는 버튼 클릭"
    AWM->>App: "ACTION_APPWIDGET_UPDATE Broadcast 발송"
    App->>Provider: "onReceive() 호출 (인스턴스 생성)"
    alt 간단한 로컬 캐시 데이터 갱신
        Provider->>AWM: "RemoteViews 생성 후 updateAppWidget() 전달"
    else 장기 실행 / 네트워크 조회 필요
        Provider->>WM: "WorkManager 작업 등록 (OneTimeWorkRequest)"
        Provider-->>AWM: "임시 Loading RemoteViews 즉시 반환"
        WM->>App: "백그라운드 비동기 데이터 수신"
        WM->>AWM: "GlanceAppWidget.update() 호출하여 최종 RemoteViews 주입"
    end
    Note over App,Provider: "onReceive() 종료 후 프로세스는 즉시 Cached 상태로 전환"
```

#### 주요 생명주기 콜백 계약

- `onEnabled()`: 해당 Provider 의 위젯 인스턴스가 홈 화면에 **최초 1개 생성**되었을 때 단 한 번 호출된다. (알람 등록, 배경 작업 초기화 지점)
- `onUpdate()`: 위젯 ID 목록(`appWidgetIds`)에 대한 UI 갱신이 필요할 때 호출된다.
- `onDeleted()`: 개별 위젯 인스턴스가 홈 화면에서 **삭제**될 때 해당 `appWidgetIds` 와 함께 호출된다. (특정 위젯의 설정값/DataStore 캐시 삭제 지점)
- `onDisabled()`: 홈 화면에서 해당 Provider 의 **마지막 위젯 인스턴스까지 모두 삭제**되었을 때 호출된다. (주기적 알람/스케줄러 해제 지점)

---

### 4. 현대 표준 예시 (Jetpack Glance vs 레거시 XML)

#### Modern Jetpack Glance Implementation

```kotlin
// 1. GlanceAppWidget 선언
class WeatherGlanceWidget : GlanceAppWidget() {
    override async fun provideGlance(context: Context, id: GlanceId) {
        // 로컬 DataStore 또는 빠른 Caching 레포지토리에서 데이터 수신
        val temp = WeatherRepository.getCachedTemperature(context)

        provideContent {
            GlanceTheme {
                Column(modifier = GlanceModifier.fillMaxSize()) {
                    Text(text = "현재 기온: ${temp}°C")
                    Button(
                        text = "새로고침",
                        onClick = actionRunCallback<RefreshWeatherAction>()
                    )
                }
            }
        }
    }
}

// 2. GlanceAppWidgetReceiver 선언 (BroadcastReceiver 표준 계약 연동)
class WeatherGlanceWidgetReceiver : GlanceAppWidgetReceiver() {
    override val glanceAppWidget: GlanceAppWidget = WeatherGlanceWidget()
}
```

```xml
<!-- AndroidManifest.xml -->
<receiver
    android:name=".WeatherGlanceWidgetReceiver"
    android:exported="true">
    <intent-filter>
        <action android:name="android.appwidget.action.APPWIDGET_UPDATE" />
    </intent-filter>
    <meta-data
        android:name="android.appwidget.provider"
        android:resource="@xml/weather_widget_info" />
</receiver>
```

---

### 5. 관측 가능 증거 및 진단 (Observability)

- **위젯 브로드캐스트 수신 및 프로세스 생명주기 관측**:
  ```bash
  adb logcat -s ActivityManager AppWidgetManager GlanceAppWidgetReceiver
  ```
- **리시버 execution 타임아웃(ANR) 확인**:
  `onUpdate` 내에서 `Thread.sleep(15000)` 과 같이 동기 지연을 유발하면 다음 로그 발생:
  `ANR in <package> (Broadcast of Intent { act=android.appwidget.action.APPWIDGET_UPDATE })`

---

### 6. 관련 문서 및 참조

- 상위 문서: [Android 앱 아키텍처는 UI 패턴보다 수명과 OS 진입점을 나누는 문제다](../../architecture/android-app-architecture.md)
- 관련 계약 문서:
  - [App Widget 계약](./app-widget-contracts.md)
  - [RemoteViews는 위젯 layout을 고정된 View 부분집합으로 제한한다](./remoteviews-restricts-widget-layouts-to-a-fixed-view-subset.md)
  - [WorkManager는 지연 가능한 보장 작업의 기본 선택이다](../../../04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md)
- 공식 문서: [AppWidgetProvider API Reference](https://developer.android.com/reference/android/appwidget/AppWidgetProvider)

검증일: 2026-08-05. BroadcastReceiver 기반 수명 및 GlanceAppWidgetReceiver 동작 가이드 검증 완료.
