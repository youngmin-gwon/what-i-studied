---
title: apple-app-tracking-privacy
tags: [ad-tech, apple, apple/security, att, permissions, privacy, tracking]
aliases: ["ATT", "App Tracking Transparency", "앱 추적 투명성"]
date modified: 2026-04-06 18:12:25 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## App Tracking Transparency (ATT) Deep Dive

iOS 14.5 가 모바일 광고 시장을 뒤흔들었죠.

기기 고유 식별자(IDFA)를 가져오려면 이제 사용자의 **명시적 동의**가 필요합니다.

"추적 금지"가 기본값이 된 세상에서 개발자가 알아야 할 생존 전략입니다.

### 💡 왜 이것을 알아야 하나요? (Context)

- **수익 악화**: ATT 동의율이 낮으면 광고 단가(eCPM)가 폭락합니다. 사용자를 설득하지 않고 무작정 팝업을 띄우면 100% 거절당합니다.
- **IDFA vs IDFV**: IDFA(광고용)를 못 쓴다면 대안은? IDFV(벤더용)는 같은 개발자 계정 내 앱끼리는 공유됩니다. 이를 활용해야 합니다.
- **Privacy Labels**: 앱스토어에 제출할 때 "이 앱이 수집하는 데이터"를 솔직하게 적어내야 합니다. 거짓말하면 앱이 삭제될 수 있습니다.

---

### 🛡️ Implementation Best Practices

#### 1. IDFA 요청 흐름 (The Flow)

그냥 `requestTrackingAuthorization` 을 호출하면 안 됩니다.

**Pre-prompt (사전 설명 화면)**가 필수입니다.

"왜 추적을 허용해야 하는지" (예: "더 관련성 있는 광고를 보여드려요" 또는 "앱을 무료로 유지하는 데 도움이 됩니다")를 설명하고, 그 다음에 시스템 팝업을 띄워야 동의율이 올라갑니다.

```swift
import AppTrackingTransparency
import AdSupport // IDFA 접근용

func requestPermission() {
    // 1. 상태 확인
    let currentStatus = ATTrackingManager.trackingAuthorizationStatus
    guard currentStatus == .notDetermined else { return }
    
    // 2. 시스템 팝업 노출 (반드시 앱 활성화 상태에서)
    ATTrackingManager.requestTrackingAuthorization { status in
        switch status {
        case .authorized:
            // 3. IDFA 접근 가능
            let idfa = ASIdentifierManager.shared().advertisingIdentifier
            print("IDFA: \(idfa)")
        case .denied:
            print("추적 거부됨. 일반 광고만 노출")
        default:
            break
        }
    }
}
```

#### 2. Info.plist 필수 (The Key)

`NSUserTrackingUsageDescription` 키가 없으면 앱이 바로 크래시납니다.

- **Bad**: "광고를 위해 필요합니다." (성의 없음)
- **Good**: "회원님에게 딱 맞는 상품을 추천하기 위해 사용됩니다. 허용하지 않아도 앱 사용에는 지장이 없습니다."

---

### 📍 기타 민감 권한 (Location & Photos)

#### 1. Location (정확도 선택)

사용자는 이제 "정확한 위치(Precise Location)"를 끌 수 있습니다.

- 내비게이션 앱이 아니라면, 대략적인 위치(반경 몇 km)만으로도 날씨 정보를 주는 데 충분합니다.
- `locationManager.accuracyAuthorization` 을 체크해서 대처해야 합니다.

#### 2. Limited Photo Library

사진 권한을 `readWrite` 로 요청하면 "전체 접근/선택 접근/거부" 3 지선다가 뜹니다.

- **Limited Access**: 사용자가 고른 사진 3 장만 내 앱에 보입니다.
- **문제**: 나중에 사용자가 사진을 더 추가하려 할 때, 시스템 팝업(`PHPhotoLibrary.shared().presentLimitedLibraryPicker(…)`)을 띄워줘야 합니다. 아니면 3 장만 계속 보입니다.

### 관찰 가능한 증거

```bash
# ATT 상태를 시뮬레이터에서 조작해 각 분기를 테스트
xcrun simctl privacy booted grant  user-tracking com.example.app
xcrun simctl privacy booted revoke user-tracking com.example.app
xcrun simctl privacy booted reset  user-tracking com.example.app
```

```swift
// 상태를 가정하지 말고 매번 확인한다
switch ATTrackingManager.trackingAuthorizationStatus {
case .authorized:    /* IDFA 사용 가능 */ break
case .denied, .restricted: /* IDFA 는 0으로 채워진 값 */ break
case .notDetermined: /* 아직 요청 안 함 */ break
@unknown default: break
}
```

> [!IMPORTANT] 요청 타이밍
> `notDetermined` 상태에서 **앱이 전경 활성 상태일 때만** 프롬프트가 뜬다. `didFinishLaunching` 에서 바로 호출하면 프롬프트가 나타나지 않고 조용히 실패한다.

**심사 대비**: 서드파티 SDK 가 추적을 수행하면 그것도 ATT 대상이다. `PrivacyInfo.xcprivacy` 에 SDK 의 수집 항목까지 반영해야 한다.

```bash
# 번들에 포함된 모든 Privacy Manifest 확인
find MyApp.app -name "PrivacyInfo.xcprivacy"
```

### 더 보기

- [apple-sandbox-and-security](apple-sandbox-and-security.md) - 권한을 관리하는 TCC 데몬의 원리
- [apple-distribution-and-policies](../08_packaging_deployment/apple-distribution-and-policies.md) - 앱스토어 심사 가이드라인 (Privacy 관련)

공식 문서: [App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency)
