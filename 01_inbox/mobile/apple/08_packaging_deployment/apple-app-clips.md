---
title: apple-app-clips
tags: [app-clips, apple, apple/packaging, clips, distribution, ios]
aliases: ["App Clips", "경량 앱"]
date modified: 2026-08-10 00:00:00 +09:00
date created: 2026-04-04 00:28:00 +09:00
---

## App Clips Deep Dive

"앱을 설치하지 않고도 즉시 사용하세요."

**App Clips**는 앱의 핵심 기능을 떼어내어 사용자에게 즉석에서 제공하는 경량 버전(Mini-app)이다. NFC 태그, QR 코드, 지도 상의 위치, 사파리 배너 등을 통해 진입하며, 사용자 결제(Apple Pay) 및 로그인(Sign in with Apple)과 결합할 때 최고의 가치를 발휘한다.

>[!NOTE] **Android 비교: Instant Apps vs App Clips**
> - **iOS**: `App Clips` 는 강력한 시스템 통합(NFC, QR, Apple Pay)을 바탕으로 여전히 활발하게 사용되고 있으며, 용량 제한도 최대 50MB(iOS 17+)까지 확장되었다.
> - **Android**: 유사한 기술인 `Instant Apps` 가 있었으나, 구글은 **2025 년 12 월 서비스 종료**를 발표했다. 이제 안드로이드에서는 별도의 인스턴트 모듈 대신 **딥링크(App Links)**를 통한 매끄러운 전체 앱 설치 및 진입을 권장하는 추세다.
>관련 android 문서는 없습니다. (Instant Apps가 2025년 12월 종료되었으므로 직접적인 대응 기술이 없습니다.)

### 1. 설계 및 크기 제한

App Clips 의 핵심은 **속도**이다. 사용자가 클릭 후 2~3 초 내에 기능을 사용할 수 있어야 한다.

**크기 제약 (as of 2025/2026):**

- **기존 (NFC, QR 등):** 최대 **15MB** (iOS 16+)
- **디지털 호출 (사파리, Spotlight 등):** 최대 **50MB** (iOS 17+)
- **주의:** 용량이 클수록 로딩 시간이 비례하므로 최대한 15MB 이하를 유지하는 것이 권장된다.

### 2. 코드 공유 및 타겟 관리

Xcode 프로젝트에서 별도의 **App Clip Target**을 추가한다. 기존 앱의 코드를 최대한 재사용해야 하지만, 불필요한 라이브러리(광고, 분석 툴 등)는 반드시 제거해야 한다.

```swift
// 공유 코드는 Framework 나 Swift Package 로 분리하여 관리
import MySharedLibrary

@main
struct MyClipApp: App {
    var body: some Scene {
        WindowGroup {
            ClipContentView() // 경량화된 UI
                .onContinueUserActivity(NSUserActivityTypeBrowsingWeb) { activity in
                    // 딥링크 및 파라미터 처리
                    handleInvocation(activity)
                }
        }
    }
}
```

### 3. 진입 시나리오 (Invocations)

App Clip 은 시스템에 의해 호출된다. 각 진입 경로는 `Universal Links` 설정을 기반으로 한다.

- **NFC Tag / QR Code**: 오프라인 결제나 체크인 (가장 강력한 시나리오)
- **Safari Smart App Banner**: 웹 브라우징 중 기능 실행
- **Maps**: 특정 장소(PO) 상세 페이지에서 실행
- **Messages**: 친구가 보낸 공유 링크를 통해 실행

---

### 🏛️ 데이터 보존 및 마이그레이션

사용자가 나중에 전체 앱을 설치하면, App Clip 에서 저장한 데이터는 **App Group** 컨테이너를 통해 안전하게 전체 앱으로 인계되어야 한다.

>[!TIP] **Devil's Advocate : App Clip 을 앱의 홍보 수단으로 쓰지 마라**
>App Clip 은 사용자가 당면한 특정 과제(커피 주문, 주차료 결제)를 즉시 해결하기 위한 도구이지, 전체 앱 설치를 유도하는 팝업창이 아니다. 사용자가 과제를 성공적으로 마쳤을 때 자연스럽게 전체 앱의 장점을 보여주는 것이 바람직하다.

### 관찰 가능한 증거

```bash
# App Clip 의 서명·entitlement 는 본체와 별개다
codesign -d --entitlements :- MyApp.app/AppClips/MyClip.app

# 로컬 실행 테스트 (Xcode scheme > Run > Arguments 의 환경 변수)
_XCAppClipURL = https://example.com/clip?item=42
```

**크기 제한이 가장 흔한 실패 원인이다.** App Clip 은 엄격한 상한을 가지며, 초과하면 배포 자체가 거부된다.

```bash
# 산출물 크기 확인 (압축 후 크기가 기준이다)
xcrun bitcode_strip -r MyClip.app/MyClip -o /tmp/stripped
du -sh MyApp.app/AppClips/MyClip.app
```

크기를 줄이는 순서: 에셋 카탈로그 최적화 → 사용하지 않는 의존성 제거 → **동적 프레임워크 제거** → 온디맨드 리소스.

**검증 체크리스트**

- [ ] App Clip 전용 코드 경로가 본체 코드를 과도하게 끌어오지 않는가
- [ ] 로그인 없이 핵심 가치를 전달하는가
- [ ] 본체 앱 설치 후 데이터가 이어지는가 (App Group 공유)

### 더 보기

- [apple-app-lifecycle-and-ui](../02_ui_frameworks/apple-app-lifecycle-and-ui.md) - 딥링크/Universal Links 연동
- [apple-distribution-and-policies](apple-distribution-and-policies.md) - 앱 배포 및 정책 가이드
- [apple-swift-package-manager](apple-swift-package-manager.md) - 코드 공유를 위한 SPM 전략

공식 문서: [App Clips](https://developer.apple.com/documentation/appclip)
