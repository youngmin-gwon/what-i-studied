---
title: apple-system-services
tags: [apple, system, daemons, tcc, sensors, privacy]
aliases: []
date modified: 2025-12-17 21:40:00 +09:00
date created: 2025-12-16 16:13:15 +09:00
---

## System Services & Sensors Deep Dive

"앱이 마이크를 쓰려고 합니다."
이 단순한 팝업 뒤에는 **TCC (Transparency, Consent, and Control)**라는 거대한 프라이버시 감시 시스템이 있습니다.
개발자로서 시스템 데몬(`tccd`, `locationd`)이 어떻게 내 앱을 감시하고 제어하는지 이해해야 합니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **권한 거부 대응**: 사용자가 "허용 안 함"을 누르면 앱은 어떻게 동작해야 할까요? 그냥 크래시 나거나 빈 화면을 보여주면 안 됩니다. `Settings`로 유도하는 UX가 필요합니다.
- **배터리 드레인**: 위치 서비스(`Core Location`)나 센서를 계속 켜두면 `locationd` 데몬이 CPU를 잡아먹어 배터리 소모의 주범으로 지목됩니다.
- **Privacy Indicators**: 마이크/카메라 사용 시 상태 표시줄에 뜨는 주황색/초록색 점은 시스템 레벨 강제 사항입니다. 몰래 녹음/촬영은 불가능합니다.

---

### 🛡️ TCC (Transparency, Consent, Control)

모든 민감한 데이터 접근은 `tccd` 데몬이 중개합니다.
앱이 연락처에 접근하려 하면, 커널이 이를 가로채고 `tccd`에게 물어봅니다. "이 앱, 허락 받았어?"

1. **Info.plist**: `NSCameraUsageDescription` 같은 키가 없으면 아예 물어보지도 않고 앱을 강제 종료(Crash)시킵니다. "왜 쓰는지" 설명하는 것이 필수입니다.
2. **Consent**: 사용자에게 팝업을 띄웁니다. 한 번 거절되면 앱 내에서 다시 띄울 수 없습니다 (OS 정책).
3. **Database**: 승인 여부는 `/Library/Application Support/com.apple.TCC/TCC.db`에 저장됩니다 (탈옥/루트 권한 없이는 접근 불가).

---

### 📡 주요 시스템 데몬 (The Hidden Workers)

앱은 직접 하드웨어를 제어하지 않습니다. XPC를 통해 데몬에게 요청할 뿐입니다.

#### 1. locationd (위치 서비스)
- **특징**: 배터리 소모가 가장 큽니다. GPS, Wi-Fi, 셀룰러 기지국, 블루투스 비콘을 모두 사용해 위치를 삼각측량합니다.
- **최적화**: `desiredAccuracy`를 최대로 설정하지 마세요. "3km 오차 허용"(`kCLLocationAccuracyThreeKilometers`)으로 설정하면 GPS를 끄고 기지국만 사용하여 배터리를 아낍니다.

#### 2. mediaserverd (카메라/오디오)
- 카메라 캡처, 오디오 입출력을 총괄합니다.
- 카메라 셔터 소리는 이 데몬이 강제로 발생시킵니다 (국가별 정책 적용).
- **Crash**: 만약 `mediaserverd`가 죽으면(너무 많은 리소스 사용 등), 앱의 카메라 프리뷰가 갑자기 멈춥니다. `AVCaptureSessionRuntimeError` 알림을 받아 세션을 재시작해야 합니다.

#### 3. biometrickitd (FaceID / TouchID)
- 생체 정보는 **Secure Enclave (SEP)** 하드웨어에만 저장되며, 앱은 물론 OS조차 원본 이미지를 볼 수 없습니다.
- 데몬은 오직 "일치함/불일치함"이라는 Bool 값만 리턴해줍니다.

---

### 🛠️ 실무 패턴 및 주의사항

#### 1. 권한 요청 시점 (The Right Time)
앱 켜자마자 위치/오디오/카메라 권한 3개를 연속으로 띄우지 마세요. 사용자는 반사적으로 "허용 안 함"을 누릅니다.
**Best Practice**: 실제로 그 기능이 필요한 순간(예: "지도 보기" 버튼을 눌렀을 때)에 요청하세요.

```swift
func requestCameraPermission() {
    let status = AVCaptureDevice.authorizationStatus(for: .video)
    switch status {
    case .notDetermined:
        // 아직 결정 안 함 -> 요청
        AVCaptureDevice.requestAccess(for: .video) { granted in ... }
    case .denied:
        // 거절됨 -> 설정으로 유도하는 얼럿 띄우기
        showSettingsAlert()
    default:
        break
    }
}
```

#### 2. 시뮬레이터 테스트
시뮬레이터는 하드웨어 센서가 없습니다.
- **위치**: 메뉴의 `Features > Location`에서 모의 주행(City Run) 등을 설정할 수 있습니다.
- **권한 리셋**: 터미널에서 `xcrun simctl privacy booted reset all` 명령어로 권한 상태를 초기화할 수 있습니다.

### 더 보기
- [[apple-interprocess-and-xpc]] - 데몬과 통신하는 원리
- [[apple-background-tasks]] - 위치 서비스를 백그라운드에서 쓰기 위한 조건
