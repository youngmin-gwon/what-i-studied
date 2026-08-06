---
title: 03-source-to-installed-package
tags: ["android", "android/foundations", "learning-spine"]
aliases: ["Source to installed package"]
date modified: 2026-08-04 10:10:34 +09:00
date created: 2026-08-03 19:30:00 +09:00
---

## 소스에서 설치된 패키지까지

2 장은 앱이 API 를 호출했을 때 코드가 어느 프로세스에서 실행되는지 설명했다. 그러나 그 호출의 주체인 앱 자체가 어떻게 기기가 신뢰하는 실행 단위가 되는지는 다루지 않았다. 이 장은 소스 코드 묶음이 어떤 산출물을 거쳐 기기에 등록된 패키지가 되는지를 다룬다.

이 장의 핵심 질문은 다음과 같다.

>소스, 자원과 의존성은 어떤 산출물로 바뀌고, 기기는 그 산출물을 어떻게 검증해 사용자별로 격리된 실행 단위로 등록하는가?

이 장은 Gradle 태스크 이름이나 서명 도구의 명령행 사용법을 가르치지 않는다. 빌드 스크립트 문법, 서명 키 관리 절차, PackageManager 내부 자료구조는 각 원자 노트가 다루는 수준으로 남겨두고, 여기서는 산출물과 검증 경계를 잇는 흐름만 설명한다.

### 1. 소스와 자원은 빌드 변형을 거쳐 하나의 산출물이 된다

소스 코드, 리소스, 매니페스트와 의존성은 그 자체로는 기기에 설치할 수 있는 형태가 아니다. Gradle 과 Android Gradle Plugin(AGP)은 이들을 조합해 하나의 **빌드 변형(build variant)**을 결정한 뒤 산출물로 변환한다.

빌드 변형은 build type(예: debug/release)과 product flavor(예: 무료/유료, 스테이징/프로덕션)라는 서로 다른 축의 조합이다. 같은 소스라도 어떤 변형을 선택하느냐에 따라 코드, 리소스, 심지어 `applicationId` 까지 달라질 수 있다.

변형이 정해지면 빌드는 대략 다음 순서로 진행된다.

| 단계 | 입력 | 처리 | 산출 |
| --- | --- | --- | --- |
| 리소스 처리 | XML 리소스, 매니페스트 | AAPT2 가 리소스를 컴파일하고 병합하며 `R` 클래스와 리소스 ID 를 생성한다 | 컴파일된 리소스 테이블, 병합된 매니페스트 |
| 코드 컴파일과 변환 | Kotlin/Java 소스, 의존성 | 컴파일 후 D8 이 바이트코드를 Android 용 DEX 포맷으로 변환한다 | DEX 파일 |
| 축소·난독화(release) | DEX, 리소스, keep 규칙 | R8 이 도달 불가능한 코드를 제거하고 필요 시 이름을 난독화한다 | 축소된 DEX 와 리소스 |
| 패키징 | 위 산출물 전체 | 하나의 배포 단위로 묶는다 | APK 또는 AAB |

이 표는 정확한 태스크 그래프가 아니라 책임의 순서를 보여주는 지도다. 실제 Gradle 실행은 변형, 증분 빌드 상태와 플러그인 설정에 따라 순서와 병렬성이 달라진다.

release 축소·난독화 단계는 build type 설정에 따라 생략될 수 있다. 이 단계를 건너뛴 debug 산출물과 release 산출물은 크기, 심벌 이름과 일부 동작(예: 로그 수준)이 달라질 수 있다는 점을 기억해야 한다.

### 2. AAB 는 게시 형식이고 APK 는 설치 형식이다

빌드의 최종 산출물은 두 형식 중 하나다. 이름이 비슷해 보여도 역할은 다르다.

| 질문 | APK | Android App Bundle(AAB) |
| --- | --- | --- |
| 기기에 직접 설치할 수 있는가? | 그렇다 | 아니다 |
| 누가 만드는가? | 개발자 빌드 또는 배포자가 생성한 최종 산출물 | 개발자가 업로드하는 게시용 산출물 |
| 실제 설치 파일은 누가 만드는가? | 그 자체가 설치 파일이다 | Google Play 또는 `bundletool` 이 기기 구성에 맞는 APK 집합을 생성한다 |
| 언어·밀도·ABI 최적화는 언제 결정되는가? | 빌드 시점에 고정 | 배포 시점에 대상 기기 조건으로 결정 |

즉 개발자는 AAB 를 만들어 배포자에게 넘기고, 사용자 기기에는 배포자가 그 AAB 로부터 생성한 APK 가 도착한다. `adb install` 로 로컬에 바로 넣을 수 있는 것은 APK 뿐이며, AAB 를 로컬에서 시험하려면 `bundletool` 이나 Android Studio 의 APK 생성 기능으로 먼저 APK 집합을 만들어야 한다.

이 구분을 놓치면 "번들 용량이 곧 사용자 다운로드 용량"이라고 오해하기 쉽다. 실제 사용자가 받는 것은 배포자가 그 기기에 맞게 생성한 APK 이며, 크기는 기기 구성과 배포자의 전달 규칙에 따라 달라진다.

### 3. 서명은 패키지 이름과 다른 축의 신원이다

이 장에서 가장 자주 혼동되는 지점은 다음 세 가지를 하나로 뭉치는 것이다.

- **패키지 이름/`applicationId`**: 개발자가 빌드 설정에서 정하는 문자열 식별자다.
- **서명 인증서**: 그 산출물이 특정 키 소유자로부터 나왔음을 암호학적으로 증명하는 신원이다.
- **숫자 appId**: 기기가 설치 시점에 배정하는 내부 식별자다. 3 절 뒤에서 다시 다룬다.

앞 두 가지는 빌드 시점에 개발자가 준비하지만 서로 독립된 계약이다. `applicationId` 가 같아도 서명이 다르면 시스템은 같은 앱으로 인정하지 않는다.

>"When the system is installing an update to an app, it compares the certificate(s) in the new version with those in the existing version. The system allows the update if the certificates match. If you sign the new version with a different certificate, you must assign a different package name to the app—in this case, the user installs the new version as a completely new app." (Android 개발자 문서, 앱 서명)

Google Play 를 통한 배포에서는 개발자가 서명하는 **업로드 키**와, Play 가 최종 사용자에게 전달하는 APK 에 서명하는 **앱 서명 키**가 분리되어 있을 수 있다(Play App Signing). 이 경우 개발자가 다루는 서명과 기기가 실제로 검증하는 서명이 물리적으로 다른 키일 수 있다는 점을 알아야 한다.

#### 실패 사례: 서명이 바뀐 업데이트

**시작 상태**

- 사용자 기기에 `applicationId` 가 `com.example.app` 인 앱이 설치되어 있다.
- 팀이 CI 환경을 바꾸면서 새 release 빌드가 의도치 않게 다른 keystore 로 서명됐다.

**실패 결과**

새 APK 를 기존 앱 위에 설치하려 하면 시스템은 인증서 불일치를 이유로 설치를 거부한다. `adb install` 은 `INSTALL_FAILED_UPDATE_INCOMPATIBLE` 류의 오류를 반환하고, Play 배포라면 콘솔이 업로드 인증서 불일치를 알린다.

**판단 순서**

1. 이 실패가 `applicationId` 불일치인지 서명 불일치인지 오류 메시지로 구분한다.
2. 서명 불일치라면 CI 가 올바른 업로드 키 또는 release keystore 를 사용하는지 확인한다.
3. 키를 의도적으로 교체해야 한다면 새 `applicationId` 로 별도 앱을 배포할지, 플랫폼이 지원하는 서명 키 교체(proof-of-rotation) 경로를 쓸지 결정한다.

이 실패는 "빌드는 성공했지만 배포가 실패한" 사례다. 컴파일 성공과 설치 가능성은 다른 조건이라는 1 장의 원칙이 여기서도 적용된다.

### 4. 설치 프로그램과 PackageManager 가 전달받은 산출물을 검증·등록한다

기기에 APK 가 도착하면(Play, 사이드로드, 기업 배포 어느 경로든) 기기의 `PackageInstaller` 가 설치 세션을 만들고, 패키지 관리 서비스가 그 내용을 검증한 뒤에만 설치 상태로 등록한다.

검증은 최소한 다음을 확인한다.

| 검증 항목 | 확인 내용 | 통과하지 못하면 |
| --- | --- | --- |
| 서명 일관성 | 기존 설치와 서명 인증서가 일치하는가(신규 설치는 이 검사가 없다) | 업데이트 거부, 새 패키지로도 설치 불가(같은 `applicationId` 인 경우) |
| 매니페스트 일관성 | 선언된 컴포넌트, 권한, `minSdk` 등이 기기와 호환되는가 | 설치 거부 또는 경고 |
| 버전 순서 | 새 `versionCode` 가 기존보다 낮지 않은가 | 업데이트 거부 |
| 저장 공간과 정책 | 기기 저장 공간, 기기 관리 정책, 사용자 제한을 만족하는가 | 설치 거부 |

이 검증을 통과하면 패키지 관리 서비스는 다음을 수행한다.

1. 문자열 `applicationId` 와 이 설치를 연결하는 내부 기록을 만든다.
2. 시스템 전체에서 유일한 **숫자 appId**를 할당한다. 이 숫자는 Linux 사용자 ID(UID)와 직접 연결된다.

   >"Android assigns a unique user ID (UID) to each Android app and runs it in its own process." (Android 보안 문서, 앱 샌드박스)

   즉 "설치된 패키지"는 문자열 식별자로 끝나지 않는다. 커널이 프로세스와 파일 시스템 권한을 격리하는 데 쓰는 실제 숫자 UID 까지 얻어야 완전한 실행 단위가 된다.

3. 사용자(또는 프로필)별 데이터 디렉터리를 만들고 초기 권한 상태를 설정한다. 여러 사용자가 있는 기기에서는 같은 패키지가 사용자마다 별도의 UID 와 데이터 영역을 가질 수 있다.
4. 매니페스트에 선언된 컴포넌트(Activity, Service, Receiver, Provider)를 컴포넌트 registry 에 등록해, 이후 Intent 해석과 컴포넌트 실행의 대상이 될 수 있게 한다.

이 등록이 끝나야 비로소 다른 시스템 서비스와 컴포넌트가 이 앱을 "설치된 패키지"로 인식하고 상호작용할 수 있다. 4 장은 이 컴포넌트 registry 가 어떻게 조회되고 실행되는지 다룬다.

### 5. 업데이트는 새 설치가 아니라 기존 신원의 연속이다

`applicationId` 와 서명이 모두 일치하면, 새 APK 설치는 완전히 새로운 실행 단위를 만드는 것이 아니라 기존 숫자 appId, UID, 데이터 디렉터리와 사용자 권한 상태를 그대로 이어받는 **갱신**이다.

| 시나리오 | UID/데이터 유지 | 사용자 권한 상태 |
| --- | --- | --- |
| 정상 업데이트(서명·`applicationId` 일치, 높은 `versionCode`) | 유지 | 유지(새로 추가된 위험 권한은 별도 승인 필요) |
| 서명 불일치 | 새 UID 로 별도 설치(같은 `applicationId` 면 설치 자체가 거부됨) | 새로 처음부터 |
| 앱 삭제 후 재설치 | 새 UID, 기존 데이터 디렉터리 삭제(백업 복원 정책은 별도) | 새로 처음부터 |
| force-stop | 영향 없음(UID/데이터 그대로, 실행 중 프로세스만 종료) | 유지 |

이 표는 "앱을 다시 설치하면 무슨 일이 일어나는가"라는 흔한 질문에 답하는 지도다. 겉으로 보기에 비슷한 "재설치"라도 삭제 후 재설치와 업데이트는 UID·데이터 연속성이라는 축에서 완전히 다른 사건이다.

### 6. 설치·업데이트 문제를 분류하는 방법

낯선 설치·배포 실패를 만났을 때 다음 순서로 원인을 좁힌다.

1. **어느 산출물 단계에서 멈췄는가?** 빌드 실패(컴파일/리소스/DEX), 서명 실패, 배포자 전달 실패, 기기 설치 실패 중 어디인지 먼저 구분한다.
2. **`applicationId` 가 의도한 값인가?** build variant 나 `applicationIdSuffix` 때문에 다른 식별자로 빌드되지 않았는지 확인한다.
3. **서명이 일관적인가?** 로컬 keystore, CI keystore, 업로드 키, 앱 서명 키 중 이번 빌드가 실제로 사용한 키를 특정한다.
4. **버전 순서가 맞는가?** `versionCode` 가 대상 기기의 기존 설치보다 높은지 확인한다.
5. **기기 쪽 검증에서 멈췄는가, 등록 이후 문제인가?** 설치 자체가 거부됐는지, 설치는 됐지만 컴포넌트 해석이나 권한 상태가 예상과 다른지 구분한다.
6. **UID/데이터 연속성이 기대와 일치하는가?** 업데이트로 기존 데이터가 보존되어야 하는데 삭제됐다면 서명·`applicationId` 불일치나 의도치 않은 삭제·재설치를 의심한다.

### 반드시 교정해야 할 오해

| 오해 | 교정 |
| --- | --- |
| AAB 가 사용자 기기에 설치되는 파일이다. | AAB 는 게시 산출물이고, 사용자는 배포자가 그로부터 생성한 APK 를 받는다. |
| `applicationId` 가 같으면 같은 앱으로 업데이트된다. | 서명 인증서도 일치해야 업데이트로 인정된다. 하나만 같아서는 안 된다. |
| 패키지 이름만 있으면 설치된 앱을 완전히 식별한 것이다. | 시스템은 문자열 식별자와 별도로 숫자 appId/UID 를 배정해야 완전한 실행 단위로 취급한다. |
| release 빌드는 R8 을 항상 거친다. | 축소·난독화는 build type 설정에 따라 켜거나 끌 수 있는 별도 단계다. |
| 앱을 지우고 다시 설치하면 업데이트와 같다. | 삭제 후 재설치는 새 UID 를 받는 별개 사건이며, 데이터·권한 상태가 이어지지 않는다. |
| 서명 키를 개발자가 항상 직접 보관한다. | Play App Signing 을 사용하면 최종 서명 키는 별도로 관리되며 개발자는 업로드 키만 다룬다. |

### 확인 질문

1. 소스, 리소스, 매니페스트, 의존성은 어떤 처리 단계를 거쳐 APK 또는 AAB 가 되는가?
2. AAB 와 APK 는 각각 무엇을 위한 형식이며, 실제 사용자는 어떤 파일을 받는가?
3. `applicationId`, 서명 인증서, 숫자 appId 는 왜 서로 다른 축인가?
4. 업데이트가 성립하려면 어떤 조건이 모두 만족되어야 하는가?
5. 기기의 설치 프로그램과 패키지 관리 서비스는 전달받은 APK 에서 무엇을 검증하는가?
6. 설치된 패키지가 사용자별 UID 와 데이터 경계를 얻는 과정은 어떻게 진행되는가?
7. 업데이트, 서명 불일치 설치, 삭제 후 재설치, force-stop 은 각각 UID 와 데이터 연속성에 어떤 차이를 만드는가?
8. 설치·배포 실패를 조사할 때 가장 먼저 구분해야 할 축은 무엇인가?

### 다음 장으로 이어지는 질문

이 장은 소스가 산출물을 거쳐 신원을 가진 설치된 패키지가 되는 과정을 설명했다. 그러나 그 패키지 안의 어떤 컴포넌트가 언제 실행되는지는 아직 다루지 않았다.

다음 장에서는 매니페스트에 등록된 정보가 실제 실행으로 이어지는 경로를 다룬다.

- 매니페스트의 컴포넌트 선언은 시스템에 무엇을 알리는가?
- Intent 는 어떻게 특정 컴포넌트로 해석되는가?
- 컴포넌트가 실행되려면 어떤 프로세스 상태 확인을 거치는가?
- 하나의 앱이 여러 컴포넌트, 여러 프로세스로 나뉠 수 있는 이유는 무엇인가?

### 관련 정본

- [Android 패키징과 배포 지도](../../03_packaging_deployment/android-packaging-deployment.md)
- [Android 기본 설정은 식별자와 버전 계약을 만든다](../../03_packaging_deployment/build/gradle/gradle-build-contracts/android-default-config-defines-identity-and-version-contracts.md)
- [Build type, product flavor, build variant는 서로 다른 축이다](../../03_packaging_deployment/build/gradle/gradle-build-contracts/build-type-product-flavor-and-build-variant-are-different-axes.md)
- [Play app signing은 업로드 키와 앱 서명 키를 분리한다](../../03_packaging_deployment/distribution/release-distribution-contracts/play-app-signing-separates-upload-key-and-app-signing-key.md)
- [앱 업데이트는 applicationId, versionCode, 서명 호환성으로 결정된다](../../03_packaging_deployment/distribution/release-distribution-contracts/app-updates-require-application-id-version-code-and-signature-compatibility.md)
- [Play App Signing은 업로드 키와 앱 서명 키를 분리한다](../../03_packaging_deployment/distribution/release-distribution-contracts/play-app-signing-separates-upload-key-and-app-signing-key.md)
- [R8은 release 빌드를 축소·최적화·난독화한다](../../03_packaging_deployment/optimization/build-optimization-contracts/r8-shrinks-optimizes-and-obfuscates-release-builds.md)
- [패키지 가시성 제한](../../04_system_services/system-state/package-user-role-contracts/packagemanager-queries-are-limited-by-package-visibility.md)

### 공식 근거

- [Configure your build](https://developer.android.com/build)
- [Android App Bundle 개요](https://developer.android.com/guide/app-bundle)
- [앱 서명](https://developer.android.com/studio/publish/app-signing)
- [Play App Signing 사용](https://support.google.com/googleplay/android-developer/answer/9842756)
- [Application sandbox](https://source.android.com/docs/security/app-sandbox)
- [PackageInstaller API](https://developer.android.com/reference/android/content/pm/PackageInstaller)

검증일: 2026-08-03. 서명·배포 정책과 Play App Signing 의 세부 조건은 변경될 수 있으므로 실제 릴리스 시점에 다시 확인한다.
