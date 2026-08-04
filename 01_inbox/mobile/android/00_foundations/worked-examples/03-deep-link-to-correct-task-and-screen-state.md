---
title: deep link가 올바른 task와 화면 상태로 열리기까지
tags: ["android", "android/foundations", "worked-example"]
aliases: ["Deep link to correct task and screen state"]
date modified: 2026-08-04 02:30:00 +09:00
date created: 2026-08-04 02:30:00 +09:00
---

## deep link가 올바른 task와 화면 상태로 열리기까지

이 예시는 Learning Spine 3·4·5장을 하나의 진입 경로로 잇는다. 3장에서 다룬 서명 identity가 도메인 소유 증명이라는 새로운 역할로 쓰이는 과정, 4장에서 다룬 매니페스트 registry와 프로세스 상태 확인, 5장에서 다룬 task/back stack이 화면 하나가 아니라 사용자의 복귀 경로 전체를 결정한다는 사실을 연결한다.

### 시작 상태

앱은 `https://www.example.com/product/123`을 App Link로 처리하도록 매니페스트에 `intent-filter`(`ACTION_VIEW`, `CATEGORY_DEFAULT`/`BROWSABLE`, `android:autoVerify="true"`, `host=www.example.com`, `pathPrefix=/product`)를 선언해뒀고, 서버는 `https://www.example.com/.well-known/assetlinks.json`에 이 앱의 `package_name`과 서명 인증서 SHA-256 지문을 등록해뒀다. 이 검증은 설치·업데이트 시점에 이미 끝나 있다. 사용자는 로그인하지 않은 상태다. 앱 프로세스는 지금 실행 중이 아니다.

### 입력

사용자가 다른 앱(메시지)에서 공유받은 상품 링크를 탭한다.

### 단계별 흐름

1. **도메인 소유 검증(3장의 identity가 새 역할을 맡는 지점)**: 시스템은 링크를 열 때가 아니라 이미 설치·업데이트 시점에 매니페스트 선언과 `assetlinks.json`을 대조해뒀다. 매니페스트는 앱이 받을 수 있는 URI 범위의 상한을 선언하고, `assetlinks.json`은 그 도메인이 이 서명 인증서를 가진 이 패키지에 URL 처리를 위임했음을 증명한다. 이 둘이 모두 일치해야 시스템은 사용자에게 앱 선택 대화상자를 보여주지 않고 곧바로 이 앱으로 연결한다.
2. **요청과 registry 조회(4장)**: 링크 탭은 `ACTION_VIEW` Intent로 시스템에 전달된다. 시스템은 검증된 App Link이므로 컴포넌트 registry에서 이 host/path에 맞는 필터를 가진 대상 Activity를 명시적으로 찾은 것처럼 처리한다.
3. **프로세스 상태 확인(4장)**: 앱 프로세스가 없으므로 AMS는 Zygote에 fork를 요청하고, specialization 뒤 `ActivityThread`가 framework에 attach한다. 이 경로는 WE1(앱 아이콘 탭에서 첫 프레임까지)의 냉시작 경로와 같다.
4. **URI 검증과 canonicalization**: 대상 Activity는 전달받은 URI를 곧바로 내부 route로 쓰지 않는다. scheme, host, path를 allowlist로 다시 확인하고, percent encoding이나 trailing slash 같은 표현을 정규화한 뒤에야 타입 있는 목적지(`Product(productId = "123")`)로 변환한다.
5. **인증 필요 여부 판정**: 이 상품 상세 화면이 로그인을 요구하는 리소스라면, 앱은 URI 문자열 전체를 그대로 저장하지 않고 검증된 목적지 모델을 "pending destination"으로 저장한다.
6. **Task/back stack 구성(5장)**: 이 진입은 task와 back stack이라는 OS 내비게이션 기록을 새로 만드는 사건이다. 딥 링크로 새로 시작된 task에는 자연스러운 부모 화면이 없다. 그대로 두면 사용자가 상품 화면에서 뒤로 가기를 눌렀을 때 곧바로 앱이 종료되는 것처럼 느껴진다. 그래서 앱은 필요하면 합성 백 스택(예: 홈 → 상품 목록 → 상품 상세)을 만들어 부모 화면을 제공한다.

### 성공 결과(로그인 상태일 때)

사용자가 이미 로그인돼 있다면 앱은 pending destination을 만들 필요 없이 곧바로 상품 상세 화면을 연다. 상품 데이터는 URI에 담긴 값을 신뢰하지 않고 진입 시점에 서버에서 다시 조회한다 — 링크가 공유된 시점과 지금 사이에 상품이 삭제되거나 가격이 바뀌었을 수 있기 때문이다. 뒤로 가기를 누르면 5절에서 구성한 합성 백 스택을 따라 상품 목록으로 이동한다.

### 실패 분기: 로그인이 필요한데 세션이 없다

1. 앱은 4절에서 변환한 `Product(productId="123")` 목적지가 인증을 요구한다고 판정한다.
2. 이 목적지를 즉시 열지 않고 pending destination으로 저장한 뒤 로그인 화면으로 이동한다.
3. 사용자가 로그인에 성공하면, 저장해둔 pending destination을 한 번만 소비해 원래 목적지로 이동한다. 로그인을 취소하거나 세션이 만료되면 안전한 기본 화면(예: 홈)으로 돌아간다.
4. 이 흐름에서 저장하는 것은 원본 URI 문자열이 아니라 이미 검증된 타입 안전한 값이다. 검증되지 않은 원본 문자열을 그대로 저장했다가 로그인 후 다시 파싱하면, 그 사이 검증 로직이 우회될 여지가 생긴다.

### 관찰 가능한 신호

- `adb shell am start -a android.intent.action.VIEW -d "https://www.example.com/product/123"`로 딥 링크 해석 결과를 재현할 수 있다.
- App Link 검증 상태는 `adb shell pm get-app-links <package>`로 확인한다. 도메인이 `verified` 상태가 아니면 시스템은 앱 선택 대화상자를 띄우거나 브라우저로 연다.
- `dumpsys activity activities`로 딥 링크 진입 후 실제 task와 back stack 구성을 확인해, 합성 백 스택이 의도대로 만들어졌는지 검증한다.
- 로그를 통해 원본 URI, canonicalize된 route, pending destination 저장/소비 시점을 기록하면 인증 흐름의 각 단계를 추적할 수 있다.

### 코드 예시

```kotlin
// 4. URI 검증과 canonicalization
fun parseProductDeepLink(uri: Uri): PendingRoute? {
    if (uri.scheme != "https" || uri.host != "www.example.com") return null
    val segments = uri.pathSegments
    if (segments.size != 2 || segments[0] != "product") return null
    val productId = segments[1].takeIf { it.isNotBlank() } ?: return null
    return PendingRoute.Product(productId)
}

// 5~6. 인증 필요 여부 판정과 pending destination
fun handleDeepLink(route: PendingRoute.Product) {
    if (!authRepository.isLoggedIn()) {
        pendingDestinationStore.save(route)
        navigate(LoginDestination)
    } else {
        navigate(ProductDestination(route.productId))
    }
}

// 로그인 성공 후 한 번만 소비
fun onLoginSuccess() {
    val pending = pendingDestinationStore.consumeOnce()
    navigate(pending ?: HomeDestination)
}
```

### 관련 원자 노트

- [Android App Link는 검증된 HTTPS 딥 링크다](../../02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/app-link-is-verified-https-deep-link.md)
- [매니페스트 선언과 assetlinks.json의 역할](../../02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/manifest-and-assetlinks-have-distinct-roles.md)
- [외부 URI는 navigation 전에 allowlist와 canonicalization을 거쳐야 한다](../../02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/external-uri-must-be-validated-before-navigation.md)
- [인증이 필요한 딥 링크의 pending destination과 백 스택](../../02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/authenticated-deep-links-require-pending-destination-and-back-stack.md)
- [Task와 back stack은 OS가 관리하는 Activity 작업 기록이지 앱 내부 navigation state가 아니다](../../02_app_framework/architecture/app-components/app-component-contracts/task-and-back-stack-are-os-activity-navigation-not-app-navigation-state.md)
- [AndroidManifest.xml은 OS에 앱의 컴포넌트를 선언한다](../../02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/android-manifest-declares-os-visible-components-and-entry-points.md)

### 관련 Learning Spine 장

- [3장 소스에서 설치된 패키지까지](../learning-spine/03-source-to-installed-package.md)
- [4장 매니페스트에서 컴포넌트 실행까지](../learning-spine/04-manifest-to-component-execution.md)
- [5장 화면, 프로세스, task와 사용자 상태는 독립적인 lifetime을 가진다](../learning-spine/05-independent-lifetimes-of-screen-process-task-and-state.md)

### 공식 근거

- [About App Links](https://developer.android.com/training/app-links/about)
- [Add Intent filters for App Links](https://developer.android.com/training/app-links/add-applinks)
- [Configure website associations and dynamic rules](https://developer.android.com/training/app-links/configure-assetlinks)

검증일: 2026-08-04. App Link 검증 상태 확인 명령과 assetlinks.json 형식은 공식 문서를 기준으로 실제 구현 시점에 다시 확인한다.
