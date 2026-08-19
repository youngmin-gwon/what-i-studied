---
title: 01-android-ecosystem-and-contract-surfaces
tags: ["android", "android/foundations", "learning-spine"]
aliases: ["Android ecosystem and contract surfaces"]
date modified: 2026-08-04 10:10:28 +09:00
date created: 2026-08-03 17:42:05 +09:00
---

## Android 생태계와 계약 접점

Android 는 하나의 회사가 완제품으로 제공하는 단일 소프트웨어가 아니다. 공개 플랫폼 소스, 공통 호환성 규칙, 반도체와 기기 제조사의 구현, 앱에 포함되는 라이브러리, 선택적으로 탑재되는 Google 서비스, 앱 배포 경로가 서로 맞물린 생태계다.

이 구조를 모르고 API 이름부터 외우면 서로 다른 것을 같은 것으로 오해하기 쉽다. Jetpack 을 운영체제에 내장된 기능으로 생각하거나, Google Play services 가 모든 Android 기기에 있다고 가정하거나, 빌드에 성공한 API 가 모든 지원 기기에서 똑같이 동작할 것이라고 기대하게 된다.

이 장의 목표는 개별 API 사용법을 배우는 것이 아니다. 새로운 기능을 만났을 때 다음 질문에 답할 수 있는 전체 지도를 만드는 것이다.

>누가 이 기능의 사양을 정하고, 구현은 어디에 있으며, 무엇과 함께 배포·업데이트되고, 사용할 수 없을 때 어떤 책임이 앱에 남는가?

여기서 **계약**은 한 주체가 다른 주체에게 무엇을 제공하고 보장하며, 어떤 조건과 실패 처리를 상대에게 남기는지를 뜻한다. **계약 접점(contract surface)**은 그 약속이 API, 라이브러리, 패키지, 호환성 규칙 또는 배포 경계로 드러나는 지점이다. 이 문서에서 계약은 법률 문서만을 뜻하지 않는다. API 명세처럼 개발자가 기대할 수 있는 기술적 약속도 포함한다.

이 장은 일반적인 운영체제, 라이브러리와 API 의 의미만 알고 있다고 가정한다. Android 앱을 빌드해 본 경험은 요구하지 않는다. 빌드 체계, Binder, 권한 판정과 프로세스 내부 동작은 여기서 구조를 파악하는 데 필요한 만큼만 언급하고 후속 장에서 다룬다.

### 1. Android 라는 이름은 하나의 대상을 가리키지 않는다

Android 를 이해하려면 먼저 같은 이름으로 불리는 대상을 분리해야 한다.

#### AOSP 는 공개 소스 기반이다

Android Open Source Project(AOSP)는 Android 플랫폼을 구성하는 공개 소스와 문서의 기반이다. 운영체제의 공통 계층과 기기 구현에 필요한 여러 구성 요소가 이 소스 트리에서 개발된다.

그러나 `AOSP 소스를 사용했다` 는 사실만으로 그 기기가 모든 Android 앱과 호환된다는 뜻은 아니다. 제조사가 소스를 가져와 하드웨어와 제품 요구에 맞게 구현하는 과정에서 공통 앱 계약을 지켜야 한다.

#### Android 호환 기기는 호환성 계약을 만족한 기기다

Android 호환성 프로그램은 기기 구현이 지켜야 할 Compatibility Definition Document(CDD)와 이를 검사하는 Compatibility Test Suite(CTS)를 중심으로 공통 실행 기반을 정의한다. Android 호환 기기(Android-compatible device)는 해당 Android 릴리스의 CDD 요구사항을 따르고 CTS 를 통과한 기기다.

호환성 계약의 목적은 모든 기기를 똑같이 만드는 것이 아니다. 앱 개발자가 공통 API 와 동작을 기대할 수 있게 하면서도 제조사가 CDD 의 기기 유형별 필수 요구사항 안에서 하드웨어, 화면 구성, 시스템 앱과 사용자 경험을 차별화할 여지를 남기는 것이다.

따라서 호환성이 보장하는 것과 보장하지 않는 것을 나눠야 한다.

| 호환성 계약이 보호하는 것 | 기기마다 달라질 수 있는 것 |
| --- | --- |
| 공개 Android SDK API 를 사용하는 제 3 자 앱의 공통 실행 기반 | CDD 가 요구하지 않는 선택 하드웨어의 존재 여부 |
| 릴리스와 기기 유형별 필수 API·하드웨어 요구사항 | 제조사의 시스템 앱, UI 와 제품 기능 |
| 기기가 지원 기능을 선언하고 앱이 이를 조회하는 공통 규칙 | 선택 하드웨어의 정확도, 성능과 전력 특성 |
| 앱 설치·실행 환경이 따라야 할 최소 호환 기준 | 선택적 Google 서비스와 OEM 고유 기능의 포함 여부 |

#### Google 서비스 포함 여부는 별도 조건이다

Android 호환성을 만족한 기기는 Google Mobile Services(GMS) 사용을 위한 별도 사용 허가를 검토할 수 있다. GMS 는 Google Play Store, Google Play services 등을 포함할 수 있는 Google 의 기기용 앱·서비스 묶음이다. 호환성 통과와 GMS 포함은 같은 사건이 아니다.

이 차이는 앱 설계에 직접 영향을 준다. Android 호환 기기라도 Google Play services 가 없을 수 있다. 앱이 Google API 에 의존한다면 해당 실행 환경이 실제로 존재하고 사용할 수 있는지 확인하거나, 요구 기능에 맞는 대체 경로를 준비해야 한다.

정리하면 다음 세 문장은 서로 다르다.

1. AOSP 소스를 기반으로 만든 기기다.
2. Android 호환성 계약을 만족한 기기다.
3. GMS 와 Google Play Store 를 포함한 기기다.

두 번째가 첫 번째와 관련은 있지만 자동으로 따라오지 않으며, 세 번째도 두 번째와 분리된 조건이다.

### 2. Android 는 여러 주체가 나누어 만든다

한 주체가 Android 기술 계층 전체를 만들고 업데이트하지 않는다. 기능이 어디에서 바뀌는지 이해하려면 주체와 산출물을 함께 봐야 한다.

#### 플랫폼과 호환성 규칙

Google 의 Android 플랫폼·호환성 조직은 주요 플랫폼 방향, 공개 API, 릴리스별 CDD 와 호환성 프로그램을 관리한다. 외부 개발자는 AOSP 에 코드와 문서를 기여할 수 있지만, 공개 기여와 Android 릴리스·호환성 관리가 같은 책임은 아니다.

#### SoC 공급자와 OEM/ODM

SoC 공급자는 칩셋, 펌웨어와 기기 구동에 필요한 저수준 구현의 일부를 제공한다. OEM/ODM 은 이를 보드와 제품 구성, 시스템 이미지, 시스템 앱, UI, 지역·통신사 요구사항과 결합해 실제 판매 기기를 만든다.

이 때문에 같은 Android API 를 사용하는 두 기기도 하드웨어 기능, 성능, 전력 사용과 일부 선택 동작이 다를 수 있다. 이 차이 자체가 곧 호환성 위반을 의미하지는 않는다. 공통 계약이 보장하는 범위와 제조사가 선택할 수 있는 범위를 분리해야 한다.

#### 라이브러리와 Google 실행 환경

Jetpack/AndroidX 제작자는 앱과 함께 배포되는 라이브러리를 만든다. Google Play services 제작자는 앱이 포함하는 클라이언트 라이브러리와 지원 기기에 설치된 공유 Google 실행 환경을 함께 제공한다. 둘은 모두 Google 이 제공할 수 있지만 코드가 존재하는 위치와 업데이트 경로가 다르다.

#### 앱 개발자, 배포자와 기기 설치 프로그램

앱 개발자는 앱 코드와 자원을 묶은 APK 또는 게시 형식인 Android App Bundle(AAB) 같은 산출물과 앱이 사용하는 백엔드 계약을 만든다. AAB 를 받는 스토어 같은 배포자는 기기 구성에 맞는 APK 집합을 만들어 전달할 수 있다. 기기에 실제로 설치되는 단위는 APK 다.

기기의 설치 프로그램과 패키지 관리 서비스는 전달받은 APK 를 검증하고 설치 상태로 등록한다. 즉, **배포자는 전달하고 기기 플랫폼은 설치를 검증·등록한다.** Google Play 를 거치지 않는 기업 배포나 외부 설치(sideload)도 전달 경로는 다르지만 마지막에는 기기의 설치 계약을 통과해야 한다.

#### 사용자와 관리자의 결정도 계약 일부다

기능 사용 가능성은 제작자만 결정하지 않는다. 사용자는 권한(permission), 역할(role), 특별 접근 권한(special access)과 기기 설정을 선택할 수 있다. 업무 프로필이나 조직 관리 기기에서는 관리자가 별도 정책을 적용할 수 있다.

이 장에서는 각 정책의 세부 판정 순서를 다루지 않는다. 중요한 점은 API 가 존재한다는 사실과 현재 사용자·관리 환경에서 허용된다는 사실이 다르다는 것이다.

#### 산출물마다 업데이트 주체가 다르다

| 산출물 또는 구성 요소 | 주된 제작·통합 주체 | 대표 업데이트 경로 |
| --- | --- | --- |
| 공통 Android 플랫폼 소스와 공개 API | Google 과 AOSP 기여자 | Android 릴리스 |
| 특정 기기의 시스템 이미지와 프레임워크 | OEM·기기 구현자와 SoC 공급자의 통합 | OEM 시스템 OTA |
| 펌웨어와 기기 저수준 구현 | SoC 공급자와 OEM | 펌웨어 또는 시스템 OTA |
| Mainline 모듈 | 해당 플랫폼 모듈 제작자와 OEM 통합 | 모듈에 따라 지원되는 별도 경로 또는 OEM 경로 |
| Google Play services 실행 환경 | Google | 지원 기기의 Google 실행 환경 업데이트 |
| Jetpack/AndroidX 와 일반 라이브러리 | 라이브러리 제작자와 앱 팀 | 새 의존성을 포함한 앱 릴리스 |
| 설치된 앱 | 앱 제작자와 배포자 | Play, 다른 스토어, 기업 배포 또는 외부 설치 |
| 백엔드 동작 | 앱 또는 서비스 운영자 | 서버 배포 |

`최신 Android` 라는 말만으로는 상태를 설명할 수 없다. OS 릴리스는 최신이지만 앱에 포함된 라이브러리는 오래됐을 수 있고, 반대 상황도 가능하다. Mainline 은 운영체제의 일부 구성 요소를 전체 시스템 이미지와 분리해 갱신할 수 있게 한 방식이지만, 실제 전달 경로는 모듈과 기기 지원에 따라 다르다. 문제를 조사할 때는 어느 구성 요소와 업데이트 경로를 말하는지 먼저 특정해야 한다.

### 3. 앱이 만나는 세 계약 접점

앱 개발자가 자주 만나는 접점은 크게 Android 플랫폼 API, Jetpack/AndroidX, Google Play services 로 나눌 수 있다. 세 접점은 API 모양이 비슷해 보여도 구현 위치와 배포 방식이 다르다.

#### Android 플랫폼 API

Android SDK 는 앱이 플랫폼 기능을 호출할 수 있도록 공개 API 명세와 빌드 도구를 제공한다. `compileSdk` 의 공개 SDK 접점으로 노출된 Android 플랫폼 API 는 대부분 `android.*` 패키지에 속한다. 그러나 AOSP 소스에서 발견한 모든 `android.*` 기호가 일반 앱에 보장되는 공개 API 인 것은 아니다. 실제 프레임워크와 시스템 서비스 구현은 기기의 Android 시스템 이미지에 있다.

따라서 `compileSdk` 에서 공개 API 가 보인다는 사실은 **그 API 를 대상으로 빌드할 수 있다**는 뜻이다. 실제 기기에서 호출할 수 있는지는 기기의 Android 버전, API 수준 또는 확장 SDK 수준(extension SDK level), 하드웨어 기능과 현재 시스템 상태를 별도로 확인해야 한다. 비공개 SDK 인터페이스는 일반 앱의 호환성 계약으로 간주할 수 없다.

#### Jetpack/AndroidX

Jetpack 은 Android 앱 개발을 돕는 라이브러리 모음이며, 대부분 Maven 의존성으로 선택해 앱과 함께 배포한다. 의존성은 앱이 빌드되고 실행될 때 필요로 하는 외부 코드 단위다. Lifecycle, Room, WorkManager, Compose 같은 라이브러리가 여기에 속한다.

Jetpack 코드가 모두 앱 프로세스 안에서 끝나는 것은 아니다. WorkManager 처럼 내부에서 플랫폼 스케줄러를 사용할 수도 있다. 그래도 Jetpack 라이브러리 버전은 기기 OS 버전과 같은 축이 아니다. 앱 팀이 의존성을 올리고 새 앱을 배포해야 라이브러리 코드가 바뀌는 경우가 많다.

#### Google Play services

Google Play services API 는 보통 앱에 포함되는 가벼운 클라이언트 라이브러리와 기기의 Google Play services 앱 안에서 실행되는 공유 서비스가 협력한다. Google 실행 환경은 OS 나 앱과 별도의 주기로 업데이트될 수 있다.

Google Play services 는 Google Play Store 의 다른 이름이 아니다.

- Google Play services 는 앱이 Google 기능을 호출할 때 사용하는 클라이언트·실행 환경 접점이다.
- Google Play Store 는 앱 검색, 게시, 배포와 업데이트를 제공하는 스토어 제품이다.

Google Play services 가 없는 기기에서는 해당 공유 구현을 전제할 수 없다. 앱은 존재 여부와 지원 상태를 확인하고 기능을 제한하거나 다른 계약 접점을 선택해야 한다.

#### 세 접점을 물리적인 위치로 비교한다

| 질문 | Android 플랫폼 API | Jetpack/AndroidX | Google Play services |
| --- | --- | --- | --- |
| 앱이 컴파일할 API 는 어디에서 오는가? | Android SDK | Maven 라이브러리 산출물 | Google Maven 의 클라이언트 라이브러리 |
| 주된 구현은 어디에 있는가? | 기기 시스템 이미지와 시스템 서비스 | 주로 앱 APK 안의 라이브러리 코드 | 앱의 클라이언트 라이브러리와 기기의 공유 Google 실행 환경 |
| 누가 버전을 선택하는가? | `compileSdk` 는 앱 팀, 실제 구현은 기기 OS | 앱 팀이 의존성 버전 선택 | 앱의 클라이언트 버전과 기기의 서비스 버전이 각각 존재 |
| 무엇과 함께 업데이트되는가? | 주로 시스템 또는 관련 플랫폼 모듈 | 앱 릴리스 | 클라이언트는 앱 릴리스, 공유 서비스는 Google 실행 환경 업데이트 |
| 앱이 확인할 것은 무엇인가? | OS/API, 기능, 시스템 상태 | 라이브러리와 플랫폼 요구사항 | 실행 환경 존재·활성·지원 상태와 기기 기능 |

이 구분은 라이브러리 이름을 분류하기 위한 암기표가 아니다. 기능이 실패했을 때 앱 코드, 앱 의존성, Google 실행 환경과 기기 OS 중 어디를 먼저 확인할지 정하는 조사 지도다.

### 4. 위치 기능 실패를 생태계 경계로 해석한다

현재 위치를 지도에 표시하는 앱을 생각해 보자. 앱은 Android 플랫폼의 위치 접점이나 Google Play services 의 위치 접점을 선택할 수 있다. 어느 쪽을 사용하든 위치 권한, 기기 설정과 실제 위치 기능이 필요하지만 구현 위치와 가용성 조건은 다르다.

#### 시작 상태

- 앱은 Google Play services 위치 접점만 사용한다.
- 개발·테스트 기기에는 Google Play services 가 있어 기능이 정상 동작했다.
- 앱은 Google 실행 환경이 없는 Android 호환 기기에도 별도 제한 없이 배포됐다.

#### 실패 결과

대상 기기에는 앱에 포함된 클라이언트 라이브러리가 요청을 넘길 공유 Google 실행 환경이 없다. Android 호환 기기라는 사실은 Google Play services 의 존재를 보장하지 않으므로 앱은 기존 전제로 위치 결과를 받을 수 없다.

이 실패를 `Android 위치 기능이 없다` 고 해석하면 원인을 잘못 찾는다. 기기에 플랫폼 위치 기능이 있을 수 있지만, 앱이 선택한 **Google 계약 접점의 실행 환경**이 없는 것이다.

#### 판단 순서

1. 앱이 사용한 API 가 플랫폼, Jetpack 또는 Google 접점 중 어디에 속하는지 확인한다.
2. 해당 접점의 실제 구현이 앱 APK, 기기 OS 또는 공유 Google 실행 환경 중 어디에 있는지 확인한다.
3. 요구 실행 환경과 기능이 현재 기기에 있는지 확인한다.
4. 기능 요구사항을 다른 접점으로도 충족할 수 있는지 비교한다.

#### 대체 경로는 동일 기능을 뜻하지 않는다

운영체제 위치 API 가 있다고 해서 Google 위치 접점의 모든 정확도, 전력 특성, 편의 기능을 그대로 대체한다고 가정할 수는 없다. 제품이 요구하는 품질을 플랫폼 위치 접점으로 충족할 수 있을 때만 대체한다.

충족할 수 없다면 앱은 조용히 다른 동작을 가장하지 말고 기능을 제한하거나 사용할 수 없음을 명확히 알려야 한다. 대체 경로는 `다른 API가 존재하는가` 가 아니라 `동일한 사용자 요구를 허용 가능한 품질로 충족하는가` 로 판정한다.

#### 실패 흐름 요약

`Google 위치 접점 선택`

→ `Google 실행 환경이 없는 호환 기기에서 요청을 처리할 구현 부재`

→ `앱이 접점과 실행 환경을 식별`

→ `플랫폼 위치 접점이 요구 품질을 충족하면 대체`

→ `충족하지 못하면 기능을 제한하고 이유를 표시`

이 사례는 다른 기능에도 적용된다. 어떤 API 를 보았을 때 `Android 기능` 이라고 뭉뚱그리지 말고 소유자, 구현 위치, 배포 단위와 존재 조건을 찾아야 한다.

### 5. 새로운 기능을 생태계 안에 배치하는 방법

낯선 Android API 나 라이브러리를 만났을 때 다음 여섯 질문을 순서대로 사용한다.

#### 1. 누가 계약을 정의하는가?

Android 플랫폼, Jetpack 라이브러리, Google 서비스, OEM 또는 제 3 자 라이브러리 가운데 어느 주체가 공개 계약을 소유하는지 확인한다. 문서 도메인과 패키지 이름은 출발점이지만 구현 위치를 자동으로 증명하지는 않는다.

#### 2. 앱은 무엇을 의존성으로 받는가?

Android SDK 의 API 를 컴파일하는지, Maven 산출물을 앱에 포함하는지, 별도 클라이언트 라이브러리가 필요한지 구분한다. 이 질문은 기능의 코드가 앱 APK 에 들어오는지 판단하는 단서다.

#### 3. 실제 구현은 어디에서 실행되는가?

앱 프로세스 안의 라이브러리 코드인지, 기기 OS 의 시스템 서비스인지, 별도 Google 실행 환경인지, 원격 백엔드인지 구분한다. 자세한 프로세스와 Binder 경계는 다음 장에서 다룬다.

#### 4. 누가 업데이트하는가?

기능 수정이 앱 릴리스, 라이브러리 의존성 업데이트, Google 실행 환경 업데이트, Mainline 또는 시스템 OTA 중 어느 경로로 전달되는지 확인한다. 같은 API 문제처럼 보여도 기다려야 할 업데이트 주체가 다를 수 있다.

#### 5. 현재 환경에 실제로 존재하고 허용되는가?

빌드 성공과 실행 시점의 가용성을 구분한다. OS/API 수준, 기능, 별도 실행 환경, 사용자 설정과 정책 가운데 어떤 조건이 필요한지 해당 API 의 공식 계약에서 확인한다.

#### 6. 없거나 실패할 때 무엇을 보장할 것인가?

대체 접점이 같은 사용자 요구를 충족하는지, 품질을 낮출 수 있는지, 기능을 끄고 이유를 보여야 하는지 결정한다. `try/catch` 로 예외를 숨기는 것은 대체 경로가 아니다.

#### 여섯 질문을 위치 사례에 적용한다

| 질문 | 위치 사례의 답 |
| --- | --- |
| 계약 소유자 | Google Play services 위치 API |
| 앱 의존성 | Google Maven 의 클라이언트 라이브러리 |
| 실제 구현 위치 | 앱 클라이언트와 기기의 공유 Google 실행 환경 |
| 업데이트 주체 | 앱 의존성과 Google 실행 환경이 서로 독립적 |
| 존재 조건 | 지원되는 Google 실행 환경과 기기 위치 기능 |
| 실패 시 책임 | 요구 품질을 만족하는 플랫폼 대체 경로 또는 명시적 기능 제한 |

이 분류를 마치면 문제를 `Android가 이상하다` 가 아니라 다음과 같이 구체화할 수 있다.

>앱에 클라이언트 라이브러리는 있지만 대상 기기에 공유 Google 실행 환경이 없으며, 제품이 허용할 대체 위치 접점의 품질을 아직 정의하지 않았다.

### 반드시 교정해야 할 오해

| 오해 | 교정 |
| --- | --- |
| Android 는 Google 이 전부 만드는 하나의 제품이다. | AOSP, 호환성 계약, 기기 구현, 선택적 Google 제품과 앱 생태계를 구분한다. |
| AOSP 소스를 사용한 모든 기기는 Android 앱과 호환된다. | Android 호환성은 CDD 준수와 CTS 통과라는 별도 계약이다. |
| Android 호환 기기에는 항상 Google Play services 가 있다. | GMS 와 Google Play services 포함 여부는 호환성 통과와 분리된 조건이다. |
| Jetpack 은 OS 에 내장되어 있다. | Jetpack 은 대체로 앱 의존성으로 포함되며 필요할 때 플랫폼 기능에 위임한다. |
| Google Play services 와 Play Store 는 같다. | 전자는 Google API 의 클라이언트·실행 환경 접점이고 후자는 앱 스토어다. |
| 빌드에 성공하면 기능은 모든 지원 기기에서 동작한다. | 빌드 가능성, 실행 환경 존재, 기능과 정책 허용은 서로 다른 조건이다. |
| OEM 차이는 모두 Android 호환성 위반이다. | 호환성 계약 안에서 허용되는 제품 차이와 계약 위반을 구분한다. |
| OS 가 최신이면 모든 구성 요소가 최신이다. | OS, Mainline, Google 실행 환경, 라이브러리와 앱은 서로 다른 업데이트 축을 가진다. |

### 확인 질문

1. AOSP 소스를 사용한 기기, Android 호환 기기와 GMS 를 포함한 기기는 어떤 관계인가?
2. Android 호환성 계약은 무엇을 공통으로 만들고 무엇을 기기 제조사의 선택으로 남기는가?
3. Android 플랫폼 API, Jetpack 과 Google Play services 의 구현 위치와 업데이트 경로는 어떻게 다른가?
4. Google Play services 와 Google Play Store 는 각각 어떤 역할을 맡는가?
5. 앱 코드, 앱에 포함된 라이브러리, 기기 OS 와 Google 실행 환경은 물리적으로 어디에 존재하는가?
6. 위치 기능 사례에서 Google 실행 환경이 없을 때 실패한 것은 Android 플랫폼인가, 앱이 선택한 계약 접점인가?
7. 운영체제 위치 API 가 존재해도 자동 대체를 결정할 수 없는 이유는 무엇인가?
8. 기능이 다르게 동작할 때 앱, 의존성, Google 실행 환경과 OS/OEM 중 어느 업데이트를 확인할지 어떻게 판단하는가?

### 다음 장으로 이어지는 질문

이 장은 누가 무엇을 제공하고 업데이트하는지 설명했다. 그러나 API 를 호출했을 때 코드가 실제로 어느 프로세스와 스레드에서 실행되는지는 아직 설명하지 않았다.

다음 장에서는 Android 플랫폼 계층을 따라 다음 질문에 답한다.

- 앱 프로세스 안에서 끝나는 라이브러리 호출과 시스템 경계를 넘는 호출은 어떻게 다른가?
- 프레임워크 관리자는 언제 시스템 서비스로 요청을 전달하는가?
- 시스템 서비스, 네이티브 서비스, HAL 과 커널은 어떤 책임을 나누는가?
- 요청 결과와 콜백은 어떤 경계를 거쳐 앱으로 돌아오는가?

### 관련 정본

- [Android System Map](../overview/android-system-map.md)
- [Android는 계층형 모바일 플랫폼이다](../overview/foundation/android-is-layered-mobile-platform-not-just-an-app-sdk.md)
- [AOSP는 완전한 Google 기기 경험이 아니다](../../01_system_internals/platform-customization/platform-customization/aosp-is-base-platform-not-complete-google-device-experience.md)
- [GMS는 AOSP와 분리된 사용 허가 기반 Google 서비스 계층이다](../../01_system_internals/platform-customization/platform-customization/gms-is-licensed-google-services-layer-not-aosp.md)
- [플랫폼 호환성 테스트는 기기 계약을 검증한다](../../01_system_internals/platform-customization/platform-customization/platform-compatibility-tests-validate-device-not-app-features.md)
- [SDK/API/target version 축](../history/history/api-level-codename-extension-level-and-target-sdk-are-different-version-axes.md)

### 공식 근거

- [Platform architecture](https://developer.android.com/guide/platform)
- [Android Compatibility program overview](https://source.android.com/docs/compatibility/overview)
- [Android Compatibility FAQ](https://source.android.com/docs/compatibility/compatibility-faq)
- [AndroidX releases](https://developer.android.com/jetpack/androidx/versions)
- [Google Play services overview](https://developers.google.com/android/guides/overview)
- [Google Play services availability](https://developers.google.com/android/guides/setup#check_whether_google_play_services_is_installed)
- [PackageInstaller API](https://developer.android.com/reference/android/content/pm/PackageInstaller)
- [비공개 SDK 인터페이스 제한](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces)

검증일: 2026-08-03. 지원 API 수준, Google Play services 지원 범위, 스토어 정책과 개별 Mainline 모듈의 전달 방식은 변경될 수 있으므로 구체적인 제품 결정을 내릴 때 다시 확인한다.
