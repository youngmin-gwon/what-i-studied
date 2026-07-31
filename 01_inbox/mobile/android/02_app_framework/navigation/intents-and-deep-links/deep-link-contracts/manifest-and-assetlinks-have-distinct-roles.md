# 매니페스트 선언과 assetlinks.json의 역할

상위 문서: [Deep Link 계약](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-contracts.md)
관련 정본: [AndroidManifest는 OS가 발견할 컴포넌트와 진입점을 선언한다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/android-manifest-declares-os-visible-components-and-entry-points.md)


## 역할 분리

딥 링크 동작은 앱 패키지의 매니페스트 선언과 웹 서버의 검증 파일이 함께 결정한다.
매니페스트는 앱이 수신할 수 있는 Intent와 URI 범위의 정적 상한을 선언한다.
`assetlinks.json`은 해당 웹 도메인이 특정 앱에 URL 처리를 위임했음을 증명한다.
첫 번째는 앱이 받을 수 있는 범위이고 두 번째는 도메인이 신뢰하는 앱이다.
둘은 서로 대체 관계가 아니라 서로 다른 질문에 답한다.

## 매니페스트의 정적 선언

`ACTION_VIEW`는 URI를 보고 화면을 열겠다는 동작을 표현한다.
`CATEGORY_DEFAULT`는 암시적 Intent 수신에 필요한 기본 범주다.
`CATEGORY_BROWSABLE`은 브라우저나 외부 웹 컨텍스트에서 진입할 수 있음을 나타낸다.
`scheme`, `host`, `pathPrefix` 또는 path pattern으로 URL 범위를 좁힌다.
외부에서 호출되는 Activity는 Android 버전에 맞는 `android:exported` 설정을 가져야 한다.
필터를 너무 넓게 잡으면 의도하지 않은 URL까지 앱이 가로채고 검증 비용이 커진다.

```xml
<intent-filter android:autoVerify="true">
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
    <data android:scheme="https" android:host="www.example.com" android:pathPrefix="/product" />
</intent-filter>
```

## assetlinks.json의 증명

파일은 `https://www.example.com/.well-known/assetlinks.json`에서 제공한다.
`relation`은 URL 처리 위임 관계를 표현한다.
`package_name`은 Android 앱의 application ID와 일치해야 한다.
`sha256_cert_fingerprints`는 앱을 서명한 인증서 지문과 일치해야 한다.
서버 파일은 앱의 내부 라우팅을 설명하지 않고 신뢰할 앱의 신원을 설명한다.
경로별 허용·제외 규칙은 지원되는 동적 App Links 문법으로 추가할 수 있다.

## 흔한 오해

assetlinks.json에 경로를 적었다고 매니페스트의 host 범위가 넓어지지는 않는다.
매니페스트에 host가 없으면 서버가 해당 host를 승인해도 앱은 그 host의 App Link가 아니다.
반대로 매니페스트가 넓어도 서버 검증이 실패하면 자동으로 앱 연결이 신뢰되지 않는다.
서명 지문은 Play App Signing, 로컬 release, debug 환경에서 각각 다를 수 있다.
변형별 패키지와 인증서 조합을 배포 전략에 맞게 관리해야 한다.

## 검토 순서

먼저 [Android 딥 링크는 외부 URI 계약이다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-is-external-uri-contract.md)의 URI 범위를 정한다.
그 다음 매니페스트 선언을 작성하고 필요 이상으로 넓지 않은지 확인한다.
서버에는 [assetlinks.json 구성](https://developer.android.com/training/app-links/configure-assetlinks)에 맞는 파일을 배포한다.
검증 결과와 실제 화면 라우팅은 [App Links 테스트와 디버깅](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-testing-validates-resolution-verification-and-routing.md)으로 확인한다.

## 핵심 판단

매니페스트는 허용 가능한 외부 입력의 상한이다.
assetlinks.json은 그 입력을 처리할 앱의 소유 관계를 검증한다.
보안과 운영을 위해 선언과 증명을 같은 파일처럼 취급하지 않아야 한다.

## 공식 문서

- [Configure website associations and dynamic rules](https://developer.android.com/training/app-links/configure-assetlinks)
