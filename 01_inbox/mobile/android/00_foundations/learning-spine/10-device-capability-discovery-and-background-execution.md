---
title: 10-device-capability-discovery-and-background-execution
tags: ["android", "android/foundations", "learning-spine"]
aliases: ["Device capability discovery and background execution"]
date modified: 2026-08-04 10:10:46 +09:00
date created: 2026-08-03 23:30:00 +09:00
---

## 기기 기능 발견과 background execution

9 장은 권한이 있어 보이는 호출도 여러 독립적인 gate 를 모두 통과해야 성공한다는 것을 다뤘다. 그러나 그 gate 들은 애초에 그 기능이 이 기기에 존재한다는 것을 전제로 한다. 기능이 아예 없는 기기에서는 permission 을 아무리 잘 처리해도 소용이 없다. 이 장은 그 앞 단계, 즉 기능이 있는지 발견하는 일과 그 기능을 이용한 작업을 화면 없이도 지속시키는 일을 다룬다.

이 장의 핵심 질문은 다음과 같다.

>앱은 기기 기능과 지속 작업을 어떤 시스템 계약으로 발견하고 사용하며, capability 가 없거나 거부됐을 때 어느 단계에서 이를 확인하고 대체해야 하는가?

이 장은 개별 시스템 서비스(위치, 센서, 생체 인증 등)의 세부 API 를 처음부터 가르치지 않는다. 각 영역의 상세 계약은 `04_system_services` 의 원자 노트가 다루는 수준으로 남겨두고, 여기서는 앞선 장들이 설명한 실행 경로(2·6 장)와 보안 gate(9 장)가 실제로는 "기능 발견"이라는 선행 단계 위에서 조합된다는 것, 그리고 지속 작업이 durable state(8 장)·scheduler(6 장)와 함께 사용자에게 보이는 결과(알림)로 이어져야 완결된다는 것을 연결한다.

### 1. 기능 사용은 발견에서 시작하지, 권한 확인에서 시작하지 않는다

9 장의 gate 들은 모두 "이 기능이 이 기기에 존재한다"는 것을 전제로 작동한다. 그 전제를 확인하는 것이 이 장의 출발점이다.

매니페스트의 `<uses-feature>` 선언은 이 확인을 대신하지 않는다. 공식 문서는 이 선언의 성격을 분명히 한다.

>"Declared `<uses-feature>` elements are informational only, meaning that the Android system itself doesn't check for matching feature support on the device before installing an application."
>
>"Google Play uses the `<uses-feature>` elements declared in your app manifest to filter your app from devices that don't meet its hardware and software feature requirements."

즉 `<uses-feature>` 는 Google Play 가 배포 대상 기기를 걸러내는 데 쓰는 선언이지, 시스템이 설치 시점이나 실행 시점에 강제하는 계약이 아니다. sideload 된 앱이나 이 필터링을 우회한 배포 경로에서는 기능이 없는 기기에도 앱이 설치될 수 있다. 그래서 실제 실행 시점에는 앱이 직접 확인해야 한다.

이 확인은 여러 층위로 나뉜다.

- 하드웨어/소프트웨어 기능 존재: `PackageManager.hasSystemFeature()`
- API 표면 존재: `Build.VERSION.SDK_INT`, `SdkExtensions.getExtensionVersion()`
- 사용자 쪽 사전 조건: `BiometricManager.canAuthenticate()` 처럼 하드웨어는 있지만 사용자가 아직 설정하지 않은 상태까지 구분하는 API

이 확인은 9 장의 permission/AppOps gate 보다 먼저, 또는 그와 별개로 이뤄져야 한다. `getSystemService()` 가 `null` 을 반환하는 것과, 매니저는 정상적으로 반환됐지만 그 뒤의 하드웨어가 없어 호출이 실패하는 것은 같은 증상처럼 보여도 다른 층위의 부재다.

### 2. 같은 기능이라도 AOSP platform, Google 서비스, OEM 구현 중 어디서 오는지가 다르다

1 장에서 다룬 위치 기능 사례를 다시 떠올려 보자. 앱은 운영체제가 제공하는 위치 API 와 Google Play services 가 제공하는 위치 API 중 하나를 선택할 수 있고, 두 경로는 구현·업데이트 주체와 대체 경로 책임이 다르다.

이 구분은 위치에만 해당하지 않는다. 새로운 기능을 마주쳤을 때는 다음을 물어야 한다.

- 이 기능은 AOSP platform 이 모든 호환 기기에 제공하는가?
- 이 기능은 Google Play services 가 있어야만(지원 기기에서만) 동작하는가?
- 이 기능은 특정 OEM 이 자사 기기에 추가한 확장인가?

이 판단에 따라 fallback 설계가 달라진다. Google 서비스가 없는 호환 기기라면 플랫폼 API 로 대체할 수 있는지 확인해야 하고, OEM 확장이라면 그 확장이 없는 다른 제조사 기기에서 핵심 기능이 아예 동작하지 않아야 하는지부터 다시 물어야 한다.

### 3. 발견된 capability 를 실제로 쓰는 경로는 앞 장들이 이미 설명했다

기능이 존재한다고 확인된 뒤의 호출 경로는 이 장이 새로 설명하지 않는다. 2 장이 설명한 것처럼 앱의 manager/proxy 호출은 Binder 를 거쳐 system_server 의 서비스로 가고, 필요하면 HAL 과 하드웨어까지 내려간다. 6 장이 설명한 것처럼 이 호출이 어느 스레드에서 실행되는지는 Dispatcher 와 Binder thread pool 이 결정한다. 9 장이 설명한 것처럼 이 호출은 permission, AppOps, foreground 상태 같은 독립적인 gate 를 통과해야 한다.

이 장이 더하는 것은 이 모든 경로 앞에 "이 기능이 존재하는가"라는 확인이 있어야 한다는 것, 그리고 그 확인 결과에 따라 경로 전체가 아예 시작되지 않을 수 있다는 것이다. 즉 전체 순서는 다음과 같다.

`기능 존재 확인 → manager/proxy(2·6장) → permission/AppOps/foreground 상태(9장) → system/native service → 필요하면 HAL/hardware(2장) → callback, error 또는 fallback`

### 4. capability 부재, 권한 거부, 실행 시점 실패는 서로 다른 처리를 요구한다

세 가지 실패는 증상이 비슷해 보여도 원인과 처방이 다르다.

- **하드웨어/기능 자체가 없다.** `BIOMETRIC_ERROR_NO_HARDWARE` 처럼, 이 기기에는 애초에 그 기능이 없다는 뜻이다. 이 경우 사용자에게 권한을 요청하는 것은 의미가 없고, 대체 기능이나 기능 비활성화가 맞는 처리다.
- **하드웨어는 있지만 사용자가 사전 조건을 채우지 않았다.** `BIOMETRIC_ERROR_NONE_ENROLLED` 처럼, 이 경우는 설정 화면으로 안내하는 것이 맞는 처리다.
- **권한이나 AppOps 가 거부했다(9 장).** 이 경우는 권한 재요청이나 대체 기능 제공이 맞는 처리다.

같은 "생체 인증 버튼을 눌렀는데 아무 일도 안 일어난다"는 증상이라도, 이 세 가지 중 어디인지 구분하지 않고 하나의 오류 메시지로 처리하면 사용자는 무엇을 해야 할지 알 수 없다.

### 5. 지속 작업은 durable state, scheduler, 사용자 가시성이라는 별도의 축을 필요로 한다

기능을 성공적으로 호출했다고 해서 그 결과가 사용자에게 항상 보이는 것은 아니다. 화면이 없는 동안에도 이어져야 하는 작업이라면 6 장에서 다룬 것처럼 화면의 lifetime 이 아니라 WorkManager 나 foreground service 같은 durable 한 소유자가 필요하고, 8 장에서 다룬 것처럼 그 작업의 상태는 메모리가 아니라 영속 저장소에 있어야 한다.

여기에 이 장이 더하는 것은 그 작업의 결과를 사용자에게 어떻게 알리는가다. FCM 은 메시지를 전달하는 수단이고, Android 알림은 그것을 사용자에게 표시하는 수단이다. 이 둘은 서로 다른 계약이며, 하나의 성공이 다른 하나를 보장하지 않는다. 서버가 메시지를 성공적으로 보냈어도, 알림 권한이 거부됐거나 채널이 차단됐다면 사용자는 아무것도 보지 못한다.

화면 없이 실행되는 작업이 사용자에게 의미가 있으려면, 그 작업의 durable 한 실행(6·8 장)과 결과의 가시성(알림)이 함께 설계돼야 한다. 어느 하나만 있으면 "작업은 성공했는데 사용자는 아무것도 몰랐다"는 상황이 된다.

### Worked example: 위치 기반 도착 알림 기능

사용자가 특정 장소에 도착하면 알림을 보내는 기능을 생각해 보자.

1. **기능 발견**: 위치 서비스가 켜져 있는지, Google Play services 가 있는 기기라면 그 실행 환경이 존재하는지 확인한다(1·2 절).
2. **권한 gate**: foreground/background 위치 권한 단계를 순서대로 요청한다(9 장).
3. **호출 경로**: `FusedLocationProviderClient`(Google client API, local proxy)를 통해 위치 갱신을 구독한다(2·6 장).
4. **지속성**: 화면이 꺼져도 이 감지가 이어져야 하므로, 화면의 lifetime 이 아니라 적절한 background 실행 수단에 위임한다(6 장). 도착 조건이 만족됐는지는 durable 한 상태로 추적한다(8 장).
5. **결과 가시성**: 도착이 감지되면 로컬 알림을 표시하거나, 서버가 FCM 으로 메시지를 보내 앱이 알림을 표시하게 한다. 이 두 계약(전달과 표시)은 각각 별도로 확인해야 한다.

이 기능 하나가 실패할 수 있는 지점은 최소 다섯 곳이다. 위치 서비스 자체가 꺼져 있을 수도, 권한 단계 중 하나가 거부됐을 수도, background 실행이 시스템에 의해 제한됐을 수도, 도착 조건 추적 상태가 유실됐을 수도, 알림이 채널 차단으로 표시되지 않았을 수도 있다.

### 실패 사례: 성공한 작업이 사용자에게 보이지 않는다

앱이 백그라운드 동기화를 성공적으로 마쳤지만, 사용자는 그 결과를 알리는 알림을 보지 못한다. 로그를 보면 서버 전송과 클라이언트 수신 콜백까지는 정상이다. 원인은 알림 자체의 문제일 수 있다. `POST_NOTIFICATIONS` 권한이 거부됐거나, 해당 알림 채널이 사용자 설정에서 꺼져 있었을 수 있다. 이 경우 "작업이 실패했다"고 진단하면 잘못된 방향으로 조사가 흘러간다. 실제로는 durable 작업(6·8 장)은 성공했고, 그 결과를 사용자에게 알리는 별도 계약(알림)만 끊긴 것이다.

### 조사 방법: 어느 축에서 실패했는지 분류한다

1. **기능이 이 기기에 존재하는가?** `hasSystemFeature()`, `canAuthenticate()` 류의 사전 확인 결과부터 본다.
2. **어느 실행 환경에 의존하는가?** AOSP platform, Google 서비스, 특정 OEM 확장 중 무엇이 필요한지 먼저 분류한다.
3. **9 장의 gate 를 통과했는가?** permission, AppOps, foreground 상태를 순서대로 확인한다.
4. **작업이 durable 하게 예약됐는가?** `WorkInfo.state` 나 서비스 상태로 실행 여부를 확인한다(6·8 장).
5. **결과가 사용자에게 표시됐는가?** 알림 권한, 채널, FCM 전달·표시·탭 지표를 분리해서 본다.

### 반드시 교정해야 할 오해

| 오해 | 교정 |
| --- | --- |
| `<uses-feature>` 를 선언하면 시스템이 기능 없는 기기에 설치를 막아 준다. | 이 선언은 Google Play 의 배포 필터링에 쓰일 뿐이며 시스템 자체는 설치 시점에 이를 검사하지 않는다. |
| 매니저 객체가 정상적으로 반환되면 그 기능을 실제로 쓸 수 있다. | 매니저 반환과 하드웨어/기능의 실제 존재는 다른 확인이며, 후자는 별도 API 로 미리 확인해야 한다. |
| 권한을 거부당한 것과 기능 자체가 없는 것은 같은 처리로 충분하다. | 하드웨어 부재, 사용자 사전 조건 미충족, 권한 거부는 각각 다른 UX(대체 기능, 설정 안내, 재요청)가 필요하다. |
| 같은 기능이면 모든 Android 호환 기기에서 같은 방식으로 동작한다. | 같은 기능이라도 AOSP platform, Google 서비스, OEM 구현 중 어디서 오는지에 따라 존재 여부와 대체 경로가 다르다. |
| 백그라운드 작업이 성공하면 사용자가 자동으로 그 결과를 안다. | 결과를 사용자에게 보이게 하려면 전달(FCM 등)과 표시(알림 권한·채널)를 별도로 확인해야 한다. |
| FCM 전송 성공이 곧 알림 표시 성공이다. | FCM 은 전달 수단이고 Android 알림은 표시 수단이며 하나의 성공이 다른 하나를 보장하지 않는다. |

### 확인 질문

1. `<uses-feature>` 선언과 `hasSystemFeature()` 런타임 확인은 각각 무엇을 책임지는가?
2. 매니저 객체가 반환되는 것과 하드웨어가 실제로 존재하는 것은 왜 다른 확인인가?
3. 같은 기능이 AOSP platform, Google 서비스, OEM 구현 중 어디서 오는지 구분해야 하는 이유는 무엇인가?
4. 기능 발견은 9 장의 permission/AppOps gate 와 어떤 순서 관계에 있는가?
5. 하드웨어 부재, 사전 조건 미충족, 권한 거부는 왜 서로 다른 UX 가 필요한가?
6. 지속 작업이 사용자에게 의미가 있으려면 durable 실행 외에 무엇이 더 필요한가?
7. FCM 과 Android 알림이 서로 다른 계약이라는 것은 실무에서 어떤 진단 규칙으로 이어지는가?
8. 위치 기반 도착 알림 예시에서 실패할 수 있는 다섯 지점은 각각 어느 장의 모델과 연결되는가?

### 다음 장으로 이어지는 질문

이 장은 기능 발견에서 지속 작업과 사용자 가시성까지 이어지는 계약을 다뤘다. 그러나 지금까지 이 Learning Spine 이 설명한 여러 주장들이 실제로 옳다는 것을 어떻게 증거로 확인하는지는 아직 다루지 않았다.

다음 장에서는 보이지 않는 Android 상태를 어떤 증거로 확인하는지, 그리고 재현부터 로그/상태/trace, 테스트/벤치마크, 배포 이후 피드백까지 어떻게 연결되는지를 다룬다.

- 지금까지의 장들이 언급한 `dumpsys`, Perfetto, logcat 같은 도구는 각각 어떤 종류의 증거를 제공하는가?
- 재현 가능한 문제와 재현하기 어려운 문제는 조사 방법이 어떻게 달라지는가?
- 테스트와 벤치마크는 실제 기기의 다양성과 릴리스 이후 피드백을 어떻게 보완하는가?

### 관련 정본

- [Android 시스템 서비스와 기기 기능 지도](../../04_system_services/android-system-services-and-device-capabilities.md)
- [시스템 서비스 접근 공통 계약](../../04_system_services/service-lookup/service-lookup/service-lookup.md)
- [앱은 Mainline package 이름보다 API와 feature availability를 확인해야 한다](../../01_system_internals/platform-modularity/platform-modularity/apps-should-check-api-feature-availability-not-mainline-package-names.md)
- [BiometricManager.canAuthenticate는 실행 전에 확인해야 하는 사전 조건이다](../../04_system_services/device-capabilities/biometrics-credential/biometricmanager-canauthenticate-is-a-precondition-check.md)
- [센서 접근 계약](../../04_system_services/device-capabilities/sensors/sensor.md)
- [위치 접근 계약](../../04_system_services/device-capabilities/location/location.md)
- [백그라운드 작업 계약](../../04_system_services/background-and-notifications/background-work/background-work.md)
- [알림과 FCM 메시징 계약](../../04_system_services/background-and-notifications/notification-messaging/notification-messaging.md)

### 공식 근거

- [The `<uses-feature>` element](https://developer.android.com/guide/topics/manifest/uses-feature-element)
- [Permissions on Android](https://developer.android.com/guide/topics/permissions/overview)
- [Background tasks overview](https://developer.android.com/develop/background-work/background-tasks)
- [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging)

검증일: 2026-08-03. `<uses-feature>`/Google Play 필터링 정책, 개별 서비스의 오류 코드 목록, FCM/알림 정책은 버전과 정책 변경에 따라 달라지므로 실제 적용 시점에 다시 확인한다.
