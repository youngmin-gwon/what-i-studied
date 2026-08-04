---
title: 12-compatibility-update-and-form-factor
tags: ["android", "android/foundations", "learning-spine"]
aliases: ["Compatibility, update, and form factor"]
date modified: 2026-08-04 10:10:49 +09:00
date created: 2026-08-04 00:30:00 +09:00
---

## 호환성, update 와 form factor

11 장은 보이지 않는 상태를 증거로 확인하고 릴리스 이후 현장 피드백까지 잇는 순환을 다뤘다. 그 순환에서 흔히 나오는 결론 중 하나는 "같은 코드가 기기마다 다르게 동작한다"는 것이다. 이 마지막 장은 그 차이를 만드는 축들을 이름 붙이고 분리한다.

이 장의 핵심 질문은 다음과 같다.

>같은 앱이 기기와 Android 버전에 따라 달라지는 축은 무엇이며, 각 축은 서로 다른 시점에 서로 다른 주체가 결정하는가?

이 장은 새로운 실행 경로나 시스템 서비스를 소개하지 않는다. 대신 지금까지 1 장부터 11 장까지 각 장에서 이미 등장했던 축(3 장의 identity/버전, 9 장의 identity 기반 gate, 10 장의 AOSP/Google/OEM 구분, 11 장의 릴리스 정책)을 하나의 호환성 판단 모델로 재조합한다.

### 1. compileSdk, minSdk, targetSdk 는 서로 다른 세 가지 질문에 답한다

3 장은 소스가 산출물이 되는 과정에서 `applicationId`, 서명, 숫자 appId 라는 서로 다른 축의 identity 를 다뤘다. 같은 방식으로, 앱의 버전 설정도 하나가 아니라 세 개의 서로 다른 질문에 답한다.

- **`compileSdk`**: 소스가 어떤 SDK API 로 컴파일될 수 있는가. 이것은 빌드 시점의 질문이다.
- **`minSdk`**: 앱이 지원해야 하는 최소 API 수준은 무엇인가. 이것은 이 기준보다 낮은 기기에서 앱이 아예 설치되지 않는다는, runtime 하한과 fallback 책임의 질문이다.
- **`targetSdkVersion`**: 앱이 어떤 API 수준을 대상으로 테스트되고 설계됐다고 시스템에 알리는가. 공식 문서는 이 값의 효과를 이렇게 설명한다.

>"This attribute informs the system that you have tested against the target version, and the system doesn't enable any compatibility behaviors to maintain your app's forward-compatibility with the target version."
>
>"if the API level of the platform is higher than the version declared by your app's targetSdkVersion, the system can enable compatibility behaviors so that your app continues to work the way you expect."

즉 기기의 Android 버전이 앱의 `targetSdkVersion` 보다 높으면, 시스템은 앱이 예상한 대로 계속 동작하도록 호환성 동작을 대신 켜줄 수 있다. 4 장에서 다룬 `exported` 속성의 targetSdkVersion 31 강제 요구사항이나, 9 장에서 다룬 permission 관련 변경들이 바로 이 계약을 통해 적용되거나 유예된다.

### 2. 기기의 실제 API level 은 이 세 값과 독립적으로 존재한다

빌드 설정의 세 값과, 사용자 손에 들린 기기가 실제로 실행하는 Android 버전(`Build.VERSION.SDK_INT`)은 또 다른 축이다. 이 값은 앱이 빌드될 때가 아니라 기기가 실행되는 시점에 결정되며, 앱이 통제할 수 없다.

앱은 자신의 `minSdk` 보다 높지만 `compileSdk` 보다는 낮은 기기, 혹은 `targetSdkVersion` 보다 훨씬 높은 기기 등 다양한 조합에서 실행될 수 있다. 이 조합의 수만큼 "같은 코드가 다르게 동작하는" 경우의 수가 생긴다.

### 3. SDK Extension 은 API level 하나로 환원되지 않는 API 존재를 만든다

10 장은 기능 발견이 `hasSystemFeature()` 만으로 끝나지 않는다는 것을 다뤘다. 버전 축에서도 같은 원리가 적용된다. `Build.VERSION.SDK_INT` 하나만으로는 API 존재 여부를 정확히 판단할 수 없는 경우가 있다.

SDK Extension 은 modular system component update 를 통해 일부 API 가 더 낮은 platform API level 기기에도 나중에 제공될 수 있음을 표현한다. `SDK_INT >= 33` 같은 확인은 여전히 유효하지만, 어떤 API 는 더 낮은 platform API level 에서도 특정 extension version 이상이면 사용 가능할 수 있다. 그래서 `SDK_INT` 만 보면 실제로는 사용 가능한 API 를 없다고 잘못 판단(false negative)할 수 있다. 앱은 `SdkExtensions.getExtensionVersion()` 으로 이를 별도로 확인해야 한다.

### 4. Mainline 은 OS 릴리스 밖에서 일부 시스템 컴포넌트를 업데이트한다

1 장은 AOSP 와 실제 기기 구현, Google 서비스가 서로 다른 배포·업데이트 주체를 갖는다는 것을 다뤘다. Mainline 은 이 구분을 플랫폼 내부에서 한 번 더 만든다. Mainline 은 일부 system component 를 Android 전체 OS release 와 분리해 더 빠르게 배포하는 modular 구조이며, Google Play system update 인프라나 partner OTA 로 전달된다.

이 말은, 같은 API level 의 두 기기라도 어떤 Mainline 모듈 버전을 갖고 있는지에 따라 실제 동작이 다를 수 있다는 뜻이다. 앱은 특정 Mainline 모듈의 패키지 이름이나 버전을 직접 추적하기보다, 10 장에서 다룬 것처럼 공개된 API/feature availability 만 신뢰해야 한다.

### 5. 라이브러리 버전은 플랫폼 API 와 다른 사이클로 움직이는 독립 축이다

1 장은 Android 플랫폼 API 와 Jetpack/AndroidX 를 같은 업데이트 단위로 보면 안 된다는 것을 다뤘다. 라이브러리는 앱과 함께 패키징되어 배포되는 산출물이므로, 플랫폼 자체의 API level 과는 별개의 버전과 최소 요구사항(minSdk)을 갖는다. 같은 플랫폼 API level 기기라도 앱에 포함된 라이브러리 버전이 다르면 동작이 달라질 수 있다.

### 6. Play policy 는 런타임과 별개인 제출·배포 조건이다

11 장에서 다룬 Google Play 테스트 트랙과 단계적 출시는 플랫폼 런타임의 동작이 아니라 배포자와 스토어 사이의 별도 계약이다. Play policy 는 특정 capability(예: 10 장에서 다룬 special app access)의 사용을 제한하거나, 특정 targetSdkVersion 미만의 앱 제출을 거부하는 식으로 작동한다. 이 축은 기기에서 실행되는 코드의 동작을 바꾸는 것이 아니라, 그 코드가 애초에 사용자에게 도달할 수 있는지를 결정한다.

### 7. OEM 구현과 device feature 는 API level 하나로 설명되지 않는다

10 장은 같은 기능이 AOSP platform, Google 서비스, OEM 구현 중 어디서 오는지에 따라 존재 여부와 대체 경로가 다르다는 것을 다뤘다. 같은 API level, 같은 Mainline 모듈 버전이라도 OEM 이 자체적으로 구현하거나 커스터마이징한 부분(전력 관리 정책, 알림 처리, 특정 하드웨어 드라이버)에서 동작이 갈릴 수 있다. 이 축은 공식 문서 하나로 표준화되지 않으며, 11 장에서 다룬 Android vitals 같은 현장 신호로 실제 분포를 확인해야 한다.

### 8. Form factor 는 이 모든 축 위에 추가되는 입력·창 모델의 차이다

지금까지의 축이 모두 같은 "휴대폰 형태의 실행 환경"을 전제로 했다면, form factor 축은 그 전제 자체를 바꾼다. 큰 화면과 폴더블에서는 창의 width/height class 와 hinge posture 가, 데스크톱 윈도잉에서는 resize 와 여러 창 인스턴스가, XR 에서는 2D 화면 실행과 공간 UI 가 분리된 문제다. TV/Wear OS/Auto 처럼 터치가 없거나 제한된 표면에서는 대체 입력 경로(d-pad, 리모컨, 음성, 마우스/키보드)로 모든 기능에 도달 가능한지를 별도로 검증해야 한다.

문제를 조사할 때는 기기 이름이 아니라 현재 앱 창의 크기·비율, 그리고 해당 폼 팩터가 요구하는 입력·lifecycle 계약에서 원인을 찾아야 한다.

### 하나의 판단 모델로 정리한다

| 축 | 언제 결정되는가 | 누가 통제하는가 | 무엇을 제한하는가 |
| --- | --- | --- | --- |
| `compileSdk` | 빌드 시점 | 개발자 | 소스가 참조할 수 있는 API 표면 |
| `minSdk` | 빌드 시점 | 개발자 | 설치 가능한 기기의 하한 |
| `targetSdkVersion` | 빌드 시점 | 개발자 | 시스템이 적용할 compatibility 동작의 기준 |
| 기기 실제 API level(`SDK_INT`) | 기기 실행 시점 | 사용자·OEM 의 OS 업데이트 | 실제로 존재하는 platform API |
| SDK Extension | 기기 실행 시점, Mainline 업데이트로 변경 가능 | Google(Mainline 배포) | `SDK_INT` 와 독립적인 일부 API 의 실제 존재 |
| Mainline 모듈 버전 | 기기별·시점별로 변경됨 | Google, 부분적으로 OEM/OTA | 플랫폼 내부 일부 컴포넌트의 실제 동작 |
| 라이브러리(Jetpack 등) 버전 | 빌드 시점 | 개발자(의존성 선택) | 앱에 포함된 API 표면과 최소 요구사항 |
| Play policy | 제출·배포 시점 | Google Play | 앱이 사용자에게 도달할 수 있는지 여부 |
| OEM 구현 | 기기 제조 시점 | OEM/ODM | 표준 API 의 실제 세부 동작과 커스터마이징 |
| Form factor | 기기·창 구성 시점 | 기기 종류, 사용자의 창 조작 | 입력 방식과 창/lifecycle 모델 자체 |

이 표가 보여주는 것은 "이 기능이 왜 이 기기에서만 다르게 동작하는가"라는 질문에 하나의 답이 없다는 것이다. 열 개의 서로 다른 축 중 어느 것이 원인인지 순서대로 좁혀야 한다.

### Worked example: 같은 API 가 특정 사용자 기기에서만 다르게 동작한다

1. 앱의 `compileSdk` 가 이 API 를 인식할 수 있는 버전인지 확인한다(빌드 자체가 되는가).
2. `minSdk`/`targetSdkVersion` 이 이 API 의 compatibility 동작에 어떻게 영향을 주는지 확인한다.
3. 문제가 보고된 기기의 실제 `SDK_INT` 와, 필요하다면 SDK Extension 버전을 확인한다.
4. 이 API 가 Mainline 모듈에 속한다면 그 기기의 모듈 버전을, 그렇지 않다면 OEM 커스터마이징 가능성을 의심한다.
5. 문제가 특정 창 크기나 입력 방식에서만 나타난다면 form factor 축(폴더블 posture, TV 의 d-pad 등)을 확인한다.
6. 11 장의 방법론대로 이 가설을 재현 가능한 조건으로 좁히고, Android vitals 로 이 조합의 실제 분포를 확인한다.

### 실패 사례: targetSdkVersion 을 올렸더니 잘 되던 기능이 깨졌다

앱이 `targetSdkVersion` 을 최신으로 올렸더니, 이전에는 잘 동작하던 기능이 갑자기 실패한다. 이것은 버그가 새로 생긴 것이 아니라, 그동안 시스템이 낮은 target 을 위해 켜주던 compatibility 동작이 꺼졌기 때문일 수 있다. 4 장에서 다룬 `exported` 명시 요구사항이나 9 장에서 다룬 권한 변경들이 대표적이다. 이런 실패를 "회귀"로 분류하기 전에, 먼저 해당 targetSdkVersion 의 공식 behavior changes 문서에서 이 버전이 무엇을 새로 강제하는지 확인해야 한다.

### 반드시 교정해야 할 오해

| 오해 | 교정 |
| --- | --- |
| minSdk, targetSdk, compileSdk 는 사실상 같은 숫자를 다르게 부르는 것이다. | 셋은 각각 설치 하한, compatibility 동작 기준, 빌드 시 API 표면이라는 다른 질문에 답한다. |
| `SDK_INT` 만 확인하면 특정 API 의 존재 여부를 항상 정확히 알 수 있다. | SDK Extension 으로 제공되는 API 는 `SDK_INT` 만으로는 false negative 가 생길 수 있다. |
| 같은 Android 버전이면 모든 기기에서 플랫폼 동작이 동일하다. | Mainline 모듈 버전과 OEM 커스터마이징이 같은 API level 안에서도 실제 동작을 다르게 만들 수 있다. |
| Play policy 가 막는 것은 곧 플랫폼이 막는 것과 같다. | Play policy 는 배포·제출 조건이며, 플랫폼 런타임이 기기에서 그 코드의 실행을 막는 것과는 다른 층위다. |
| targetSdkVersion 을 올리는 것은 위험이 없는 단순 설정 변경이다. | target 을 올리면 시스템이 대신 켜주던 compatibility 동작이 사라지므로 기존 기능이 깨질 수 있다. |
| 폼 팩터 문제는 기기 이름으로 분류하면 충분하다. | 같은 이름의 기기라도 창 크기·posture·입력 방식이 실행 시점에 달라질 수 있으므로 기기 이름이 아니라 현재 창/입력 조건으로 분류해야 한다. |

### 확인 질문

1. `compileSdk`, `minSdk`, `targetSdkVersion` 은 각각 어떤 시점에 누가 결정하는 값인가?
2. targetSdkVersion 을 낮게 유지하면 시스템은 무엇을 대신 해주는가?
3. `SDK_INT` 만으로 API 존재를 판단하면 어떤 경우에 잘못된 결론에 이르는가?
4. Mainline 모듈이 같은 API level 안에서도 기기별 차이를 만드는 이유는 무엇인가?
5. 라이브러리 버전이 플랫폼 API level 과 독립적인 축인 이유는 1 장의 어떤 구분과 연결되는가?
6. Play policy 와 플랫폼 런타임 동작은 왜 같은 층위로 취급하면 안 되는가?
7. OEM 구현 차이를 조사할 때 공식 문서 하나로 표준화되지 않는 이유는 무엇이며, 11 장의 어떤 도구로 이를 보완하는가?
8. 폼 팩터 문제를 기기 이름이 아니라 무엇으로 분류해야 하는가?

### 이 Learning Spine 을 마치며

12 개 장은 하나의 순서로 이어진다. 1 장은 이 생태계를 이루는 주체들이 서로 무엇을 계약(contract)으로 제공·보장하는지 나눴고, 2 장은 요청이 지나는 실행 계층을 다뤘다. 3~4 장은 소스가 설치된 패키지와 실행 중인 컴포넌트가 되는 과정을 다뤘고, 5~7 장은 그 컴포넌트를 둘러싼 여러 lifetime 과 실행 계약, 입력·출력 경로를 다뤘다. 8 장은 데이터의 owner 와 offline recovery 를, 9 장은 그 접근을 판정하는 identity 기반의 독립적인 security gate 들을, 10 장은 기기 기능을 발견하고 지속 작업을 사용자에게 보이는 결과로 이어가는 계약을 다뤘다. 11 장은 이 모든 주장을 증거로 검증하는 방법을, 그리고 이 12 장은 그 검증 결과가 왜 기기·버전마다 달라지는지를 다뤘다.

이 장들이 제공한 것은 API 목록이 아니라, 새로운 문제를 만났을 때 "이것은 어느 층위의, 어느 축의 문제인가"를 묻는 방법이다. 이후의 심화 학습은 Worked Example, Diagnostic Runbook, 그리고 각 영역의 Atomic Reference 노트에서 이어진다.

### 관련 정본

- [API level, codename, extension level, targetSdkVersion은 서로 다른 version 축이다](../history/history-contracts/api-level-codename-extension-level-and-target-sdk-are-different-version-axes.md)
- [SDK Extensions는 SDK_INT만으로 표현되지 않는 API availability를 나타낸다](../../01_system_internals/platform-modularity/platform-modularity-contracts/sdk-extensions-express-api-availability-beyond-sdk-int.md)
- [Mainline은 선택된 system component를 정규 플랫폼 release 밖에서 업데이트한다](../../01_system_internals/platform-modularity/platform-modularity-contracts/mainline-updates-selected-system-components-outside-normal-platform-releases.md)
- [앱은 Mainline package 이름보다 API와 feature availability를 확인해야 한다](../../01_system_internals/platform-modularity/platform-modularity-contracts/apps-should-check-api-feature-availability-not-mainline-package-names.md)
- [Android 기본 설정은 식별자와 버전 계약을 만든다](../../03_packaging_deployment/build/gradle/gradle-build-contracts/android-default-config-defines-identity-and-version-contracts.md)
- [Android history는 기능 목록이 아니라 platform contract 변화 지도다](../history/history-contracts/android-history-is-a-map-of-platform-contract-changes-not-a-feature-list.md)
- [Android 폼 팩터와 플랫폼 확장 지도](../../07_platforms/android-platforms-and-form-factors.md)

### 공식 근거

- [`<uses-sdk>`](https://developer.android.com/guide/topics/manifest/uses-sdk-element)
- [Build.VERSION](https://developer.android.com/reference/android/os/Build.VERSION)
- [SDK Extensions](https://developer.android.com/guide/sdk-extensions)
- [Mainline](https://source.android.com/docs/core/ota/modular-system)
- [Adaptive app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality)

검증일: 2026-08-04. API level/extension level 구체 수치, Mainline 모듈 지원 종료 시점, Play policy 세부 조건은 릴리스마다 바뀌므로 실제 적용 시점에 다시 확인한다.
