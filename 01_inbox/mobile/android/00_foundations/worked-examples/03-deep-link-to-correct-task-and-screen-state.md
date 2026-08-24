---
title: 03-deep-link-to-correct-task-and-screen-state
tags: ["android", "android/foundations", "worked-example"]
aliases: ["Deep link to correct task and screen state", "Deep Link가 올바른 Task와 화면 상태로 열리기까지"]
date modified: 2026-08-05 13:00:00 +09:00
date created: 2026-08-04 02:30:00 +09:00
---

## Deep Link 가 올바른 Task 와 화면 상태로 열리기까지 (Deep Link to Correct Task & Screen State)

이 예시는 Learning Spine 3·4·5 장을 하나의 외부 진입 경로로 연결한다. 설치 시점 서명 identity 가 웹 도메인 소유 증명(`assetlinks.json`)으로 연동되는 구조(3 장), 매니페스트 컴포넌트 registry 조회를 통한 Intent 매칭과 냉시작 프로세스 분기(4 장), 그리고 딥 링크 클릭 시 단순 단일 화면 렌더링을 넘어 OS Task 와 합성 백 스택(Synthetic Backstack)을 구성하는 화면 상태 관리 계약(5 장)을 다층 서사로 다룬다.

---

### 시작 상태

앱은 `https://www.example.com/product/{id}` 패턴을 App Link 로 처리하도록 매니페스트에 `<intent-filter>`(`ACTION_VIEW`, `CATEGORY_DEFAULT`/`BROWSABLE`, `android:autoVerify="true"`)를 선언해 두었다. 웹 서버의 `https://www.example.com/.well-known/assetlinks.json` 에는 앱 패키지 이름과 APK 서명 SHA-256 지문이 등록되어 OS Domain Verification 검증이 완료된 상태다. 사용자는 현재 미인증(로그아웃) 상태이거나 앱 프로세스가 살아있지 않을 수 있다.

---

### 입력

사용자가 외부 앱(카카오톡, 메세지, 브라우저)에서 전달받은 `https://www.example.com/product/123` 상품 상세 링크를 탭한다.

---

### 다층 계층별 실행 흐름 (Multi-Layer Narrative)

```mermaid
flowchart TD
    subgraph UI["UI Layer"]
        ui1["External App / Browser URL Tap"] --> ui2["Implicit Intent (ACTION_VIEW)"]
    end

    subgraph SYS["System Server / IPC Layer"]
        sys1["DomainVerificationManager / PMS Checks Verified Hosts"] --> sys2["App Link Verified: Direct Target Activity Selection"]
        sys2 --> sys3["ATMS Determines Target Task & Launch Mode"]
        sys3 --> sys4["AMS checks process state (Fork process via Zygote if dead)"]
    end

    subgraph KERNEL["Kernel / Framework Layer"]
        k1"[binder ipc"] --> k2["ActivityThread.main()"]
        k2 --> k3["Target Activity"]
        k3 --> k4["Navigation 3 Route Parser / Canonicalization"]
    end

    subgraph TASK["App State & Task Layer"]
        auth{"Auth State Check"}
        auth -- "Unauthenticated" --> save["Save PendingRoute"]
        save --> login["Open Login Screen"]
        login --> resume["On Success, Consume PendingRoute & Build Synthetic Backstack"]
        auth -- "Authenticated" --> resume
    end

    subgraph DISPLAY["Display UI"]
        disp["Render Target Screen (Product 123) with Stack: Home → List → Detail"]
    end

    ui2 --> sys1
    sys4 --> k1
    k4 --> auth
    resume --> disp
```

1. **UI / 입력 레이어**:
   - 외부 앱에서 URL 탭 시 `Intent(Intent.ACTION_VIEW, Uri.parse("https://www.example.com/product/123"))` 인시클리시트 Intent 가 생성된다.

2. **System Server 및 IPC 레이어**:
   - `DomainVerificationManager` 및 `PackageManagerService`(PMS)는 수신된 HTTPS 도메인이 사전 검증(App Link Verification)된 호스트인지 확인한다.
   - 도메인 검증이 `verified` 상태이면, 사용자에게 앱 선택 대화상자(Disambiguation Dialog)나 웹 브라우저를 띄우지 않고 곧바로 해당 앱 패키지를 최종 수신자로 단독 지정한다.
   - `ActivityTaskManagerService`(ATMS)는 해당 Activity 의 `launchMode` 와 Intent 플래그(`FLAG_ACTIVITY_NEW_TASK` 등)를 참조하여 딥 링크가 실행될 Task 와 백 스택을 계산한다.
   - 앱 프로세스가 죽어있는 경우 [AMS](../../04_system_services/activity-manager-service.md) 가 Zygote fork 경로를 실행한다 (WE1 냉시작 참조).

3. **App Framework 레이어**:
   - Intent 가 대상 Activity(`MainActivity`)로 전달되면, 앱은 `Intent.data` URI 를 정규화(Canonicalization)하고 쿼리 파라미터/경로를 Allowlist 와 비교 검증한다.
   - Android 14/15/16 표준인 Jetpack Navigation 3 / Type-Safe Navigation 모델을 이용하여 단순 문자열이 아닌 `@Serializable` 타입 안전 객체(`ProductDetailRoute(productId = "123")`)로 변환한다.

4. **인증 상태 판정 및 합성 백 스택 (Synthetic Backstack) 구성**:
   - 해당 리소스가 로그인(인증)을 요구하는 경우, 미인증 상태에서는 원본 URI 나 Route 를 `PendingRoute` 저장은 하되 즉시 실행하지 않고 로그인 화면(`LoginRoute`)으로 우회한다.
   - 로그인 성공 시 저장해둔 `PendingRoute` 를 단 1 회 소비하여 원래 요청된 화면으로 이동한다.
   - 딥 링크로 새로 진입한 Task 는 이전 화면 기록이 없으므로, 사용자가 '뒤로 가기' 버튼을 누르면 앱이 곧바로 종료되는 불상사가 발생한다. 따라서 `TaskStackBuilder` 또는 Navigation Controller 를 이용해 합성 백 스택(`Home -> Category -> ProductDetail`)을 만들어 둔다.

---

### Android 14 / 15 / 16 platform specific behaviors

1. **Android 12~16 Strict App Links Domain Verification**:
   - Android 12 이상부터는 `android:autoVerify="true"` 가 선언된 HTTPS 도메인이라도, 서버의 `assetlinks.json` 검증이 실패하면 앱 선택 대화상자를 띄우지 않고 즉시 웹 브라우저로 렌더링을 이관한다.
   - `adb shell pm get-app-links` 명령을 통해 OS 의 검증 도메인 상태가 `verified` 인지 주시해야 한다.

2. **Jetpack Navigation 3 & Type-Safe Navigation**:
   - 기존의 `android-app://` 문자열 기반 navigation URL 매핑 방식에서 벗어나, Kotlin Serialization 의 `@Serializable` 데이터 클래스로 Route 를 정의한다. URL 은 진입 파서에서 일차 타입 검증을 거친 후 순수 도메인 모델로 다뤄진다.

3. **Custom Intent Scheme Security (Android 13 / 14 / 15)**:
   - `myapp://` 형태의 커스텀 스킴 딥 링크는 OS 인증 구조가 없어 딥 링크 하이재킹(Intent Hijacking) 및 피싱 공격에 취약하다. 외부 URI 파싱 시 불필요한 Intent Extra 취득을 제한하고 Strict Allowlist 파싱을 적용해야 한다.

---

### 성공 경로 vs 실패 분기 비교

| 항목 | 성공 경로 (Success Path) | 실패 분기 (Failure Branch 1: Domain Unverified) | 실패 분기 (Failure Branch 2: Unauthenticated Deep Link) |
| :--- | :--- | :--- | :--- |
| **진행 현상** | 링크 탭 즉시 앱이 열리며 로그인 확인 후 상품 상세 화면 표시. 뒤로 가기 시 카테고리/홈 이동 | 탭 시 앱 선택 팝업이 뜨거나 Chrome 브라우저로 웹페이지 접속 | 앱 진입 후 즉시 로그인 화면으로 전환. 로그인 완료 후 상품 상세로 정상 복원 |
| **원인 메커니즘** | App Link 검증 성공 (`verified`), 타입 안전 파싱 완료, 합성 백 스택 구성 | `assetlinks.json` 미배포, SHA-256 서명 불일치, 매니페스트 autoVerify 누락 | 인증 필요 리소스 진입 시 세션 없음. 원본 Route 를 `PendingRouteStore` 에 일시 저장 후 이관 |
| **관측 가능 신호** | `pm get-app-links` -> `verified`, `dumpsys activity activities` 내 합성 Task Stack 인스턴스 확인 | `pm get-app-links` -> `legacy` 또는 `1` (rejected), 브라우저 프로세스 가동 | `logcat: DeepLinkHandler: Session missing. PendingRoute saved: Product(123)` |

---

### CLI 진단 명령어 및 관찰 도구

1. **App Link 도메인 검증 상태 확인**:
   ```bash
   adb shell pm get-app-links com.example.app
   # 출력 예시:
   # com.example.app:
   #   ID: 309d9494-d4b9-4a00-9856-bb6b03378564
   #   Signatures: [A4:C9:...]
   #   Domain verification state:
   #     www.example.com: verified
   ```

2. **딥 링크 강제 트리거 테스트**:
   ```bash
   adb shell am start -a android.intent.action.VIEW \
       -c android.intent.category.BROWSABLE \
       -d "https://www.example.com/product/123" \
       com.example.app
   ```

3. **로컬 테스트용 App Link 도메인 상태 강제 설정**:
   ```bash
   # domain verification 상태를 verified(2)로 강제 변경
   adb shell pm set-app-links --package com.example.app 2 www.example.com
   ```

4. **Task 및 합성 백 스택 구조 진단**:
   ```bash
   adb shell dumpsys activity activities | grep -E "Hist|TaskRecord|Running"
   # 생성된 Task 내 Activity Stack depth 및 Root Activity 확인
   ```

---

### 실전 코드 예시 (Production Code Examples)

```kotlin
// DeepLinkParser.kt
package com.example.app

import android.net.Uri
import kotlinx.serialization.Serializable

@Serializable
sealed interface AppRoute {
    @Serializable
    data object Home : AppRoute
    
    @Serializable
    data object Login : AppRoute

    @Serializable
    data class ProductDetail(val productId: String) : AppRoute
}

object DeepLinkParser {
    private const val ALLOWED_HOST = "www.example.com"
    private const val SCHEME_HTTPS = "https"

    // 1. URI 검증 및 Canonicalization -> 타입 안전 Route 반환
    fun parse(uri: Uri): AppRoute? {
        if (uri.scheme != SCHEME_HTTPS || uri.host != ALLOWED_HOST) return null
        
        val segments = uri.pathSegments
        if (segments.size == 2 && segments[0] == "product") {
            val productId = segments[1].trim()
            if (productId.isNotEmpty() && productId.all { it.isLetterOrDigit() }) {
                return AppRoute.ProductDetail(productId)
            }
        }
        return null
    }
}
```

```kotlin
// DeepLinkNavigationHandler.kt
package com.example.app

import android.content.Context
import androidx.core.app.TaskStackBuilder
import android.content.Intent

class DeepLinkNavigationHandler(
    private val authRepository: AuthRepository,
    private val pendingRouteStore: PendingRouteStore
) {

    // 2. 인증 판정 및 Pending Route 처리
    fun handleRoute(context: Context, route: AppRoute) {
        if (route is AppRoute.ProductDetail && !authRepository.isLoggedIn()) {
            // 미인증 시 원본 검증 객체를 Pending 로 저장 후 로그인 화면으로 전환
            pendingRouteStore.save(route)
            navigateToLogin(context)
            return
        }

        executeNavigation(context, route)
    }

    fun onLoginSuccess(context: Context) {
        val destination = pendingRouteStore.consumeOnce() ?: AppRoute.Home
        executeNavigation(context, destination)
    }

    // 3. 합성 백 스택 (Synthetic Backstack) 구성
    private fun executeNavigation(context: Context, route: AppRoute) {
        when (route) {
            is AppRoute.ProductDetail -> {
                val parentIntent = Intent(context, MainActivity::class.java).apply {
                    putExtra("ROUTE_KEY", "category_list")
                }
                val detailIntent = Intent(context, MainActivity::class.java).apply {
                    putExtra("ROUTE_KEY", "product_${route.productId}")
                }

                // TaskStackBuilder 로 딥 링크 진입 시 뒤로 가기 경로 제공 (Home -> ProductDetail)
                TaskStackBuilder.create(context)
                    .addNextIntent(parentIntent)
                    .addNextIntent(detailIntent)
                    .startActivities()
            }
            else -> { /* 기본 네비게이션 실행 */ }
        }
    }
}
```

---

### 관련 원자 노트

- [Android App Link는 검증된 HTTPS 딥 링크다](../../02_app_framework/navigation/intents-and-deep-links/app-links-verification.md)
- [매니페스트 선언과 assetlinks.json의 역할](../../02_app_framework/navigation/intents-and-deep-links/assetlinks-verification-json.md)
- [외부 URI는 navigation 전에 allowlist와 canonicalization을 거쳐야 한다](../../02_app_framework/navigation/intents-and-deep-links/external-uri-validation.md)
- [인증이 필요한 딥 링크의 pending destination과 백 스택](../../02_app_framework/navigation/intents-and-deep-links/authenticated-deep-links.md)
- [Task와 back stack은 OS가 관리하는 Activity 작업 기록이지 앱 내부 navigation state가 아니다](../../02_app_framework/architecture/app-components/task-and-back-stack.md)
- [AndroidManifest.xml은 OS에 앱의 컴포넌트를 선언한다](../../02_app_framework/navigation/intents-and-deep-links/manifest-component-entry-points.md)

---

### 관련 Learning Spine 장

- [3장 소스에서 설치된 패키지까지](../learning-spine/03-source-to-installed-package.md)
- [4장 매니페스트에서 컴포넌트 실행까지](../learning-spine/04-manifest-to-component-execution.md)
- [5장 화면, 프로세스, task와 사용자 상태는 독립적인 lifetime을 가진다](../learning-spine/05-independent-lifetimes-of-screen-process-task-and-state.md)

---

### 관련 Diagnostic Runbook

- [01-app-launch-slow-or-fails.md](../diagnostic-runbooks/01-app-launch-slow-or-fails.md)
- [03-process-death-state-loss.md](../diagnostic-runbooks/03-process-death-state-loss.md)

---

### 공식 근거

- [Handling Android App Links](https://developer.android.com/training/app-links)
- [Verify Android App Links](https://developer.android.com/training/app-links/verify-site-associations)
- [Type-safety in Navigation Compose](https://developer.android.com/guide/navigation/design/type-safety)
- [Create a synthetic back stack for deep links](https://developer.android.com/guide/navigation/principles#synthetic_back_stack)

검증일: 2026-08-04. Domain Verification `pm get-app-links` 출력, Navigation 3 / Type-Safe Navigation 패턴, 합성 백 스택 구성 로직을 공식 문서를 기준으로 검증함.
