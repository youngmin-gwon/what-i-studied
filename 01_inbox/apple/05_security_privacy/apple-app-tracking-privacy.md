---
title: apple-app-tracking-privacy
tags: [apple, privacy, att, tracking, permissions, ad-tech]
aliases: []
date modified: 2025-12-17 22:10:00 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## App Tracking Transparency (ATT) Deep Dive

iOS 14.5가 모바일 광고 시장을 뒤흔들었죠.
기기 고유 식별자(IDFA)를 가져오려면 이제 사용자의 **명시적 동의**가 필요합니다.
"추적 금지"가 기본값이 된 세상에서 개발자가 알아야 할 생존 전략입니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **수익 악화**: ATT 동의율이 낮으면 광고 단가(eCPM)가 폭락합니다. 사용자를 설득하지 않고 무작정 팝업을 띄우면 100% 거절당합니다.
- **IDFA vs IDFV**: IDFA(광고용)를 못 쓴다면 대안은? IDFV(벤더용)는 같은 개발자 계정 내 앱끼리는 공유됩니다. 이를 활용해야 합니다.
- **Privacy Labels**: 앱스토어에 제출할 때 "이 앱이 수집하는 데이터"를 솔직하게 적어내야 합니다. 거짓말하면 앱이 삭제될 수 있습니다.

---

### 🛡️ Implementation Best Practices

#### 1. IDFA 요청 흐름 (The Flow)

그냥 `requestTrackingAuthorization`을 호출하면 안 됩니다.
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
- `locationManager.accuracyAuthorization`을 체크해서 대처해야 합니다.

#### 2. Limited Photo Library
사진 권한을 `readWrite`로 요청하면 "전체 접근/선택 접근/거부" 3지선다가 뜹니다.
- **Limited Access**: 사용자가 고른 사진 3장만 내 앱에 보입니다.
- **문제**: 나중에 사용자가 사진을 더 추가하려 할 때, 시스템 팝업(`PHPhotoLibrary.shared().presentLimitedLibraryPicker(...)`)을 띄워줘야 합니다. 아니면 3장만 계속 보입니다.

### 더 보기
- [[apple-sandbox-and-security]] - 권한을 관리하는 TCC 데몬의 원리
- [[apple-distribution-and-policies]] - 앱스토어 심사 가이드라인 (Privacy 관련)
