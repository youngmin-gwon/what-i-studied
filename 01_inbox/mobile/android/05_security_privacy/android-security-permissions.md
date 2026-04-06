---
title: android-security-permissions
tags: [android, android/permissions, android/security]
aliases: []
date modified: 2026-04-05 21:04:23 +09:00
date created: 2026-04-05 16:29:23 +09:00
---

## [[mobile-security]] > [[android-security-permissions]]

### Android Permissions System

권한 시스템은 앱이 민감한 사용자 데이터(연락처, 사진)나 시스템 기능(카메라, 위치)에 접근하는 것을 제어하는 핵심 보안 레이어입니다. 이는 [[android-security-sandbox]] 의 연장선이며, 사용자 프라이버시 보호의 핵심입니다.

---

#### 🛡️ 보호 수준 (Protection Levels)

| 수준 | 설명 | 승인 방식 |
|------|------|----------|
| **Normal** | 낮은 위험 (인터넷, 진동 등) | 설치 시 자동 승인 |
| **Dangerous** | 높은 위험 (위치, 카메라, 연락처) | **런타임 시 사용자 승인** |
| **Signature** | 동일한 서명의 앱끼리만 공유 가능 | 시스템 자동 승인 |
| **Internal** | 시스템 내부 전용 | 일반 앱 접근 불가 |

---

#### 런타임 권한 (Android 6.0+)

**위험 권한(Dangerous Permissions)** 은 앱 실행 중에 요청해야 하며, 사용자는 이를 거부할 권리가 있습니다.

```kotlin
// 현대적인 권한 요청 패턴 (ActivityResultLauncher)
private val requestPermissionLauncher = registerForActivityResult(
    ActivityResultContracts.RequestPermission()
) { isGranted: Boolean ->
    if (isGranted) {
        // 권한 허용됨: 기능 수행
    } else {
        // 권한 거부됨: 사용자에게 필요성 설명 또는 기능 제한
    }
}

fun checkAndRequestCamera() {
    when {
        ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA) == PERMISSION_GRANTED -> {
            accessCamera()
        }
        shouldShowRequestPermissionRationale(Manifest.permission.CAMERA) -> {
            // 이전에 거부했을 경우 교육용 UI 표시
            showRationaleDialog { requestPermissionLauncher.launch(Manifest.permission.CAMERA) }
        }
        else -> {
            requestPermissionLauncher.launch(Manifest.permission.CAMERA)
        }
    }
}
```

---

#### 📍 특수 권한 및 세분화된 제어

##### 1. 위치 권한 (Android 10~12)

- **포그라운드/백그라운드 분리**: 백그라운드 위치 권한은 별도의 설정 화면 이동이 필요합니다.
- **정확도 제어 (Android 12+)**: 사용자가 "정확한 위치" 대신 "대략적인 위치"만 허용할 수 있습니다.

##### 2. 특수 접근권 (Special App Access)

일반 다이얼로그로 요청 불가하며, 시스템 설정 페이지로 이동시켜야 합니다.

- `SYSTEM_ALERT_WINDOW`: 다른 앱 위에 그리기.
- `WRITE_SETTINGS`: 시스템 설정 수정.
- `MANAGE_EXTERNAL_STORAGE`: 모든 파일 접근 (구글 플레이 검토 시 엄격한 제한).

##### 3. 알림 권한 (Android 13+)

- `POST_NOTIFICATIONS` 가 런타임 권한으로 추가되었습니다.

##### 4. 미디어 접근 세분화 (Android 14+)

- **부분 사진 허용 (Selected Photos Access)**: `READ_MEDIA_VISUAL_USER_SELECTED` 권한을 통해 사용자가 전체 갤러리가 아닌 **선택한 특정 사진/비디오**에만 접근권을 부여할 수 있습니다.
- **연속성 유지**: 사용자 경험을 위해 `READ_MEDIA_IMAGES` 와 함께 요청하며, 시스템이 자동으로 선택 UI 를 제공합니다.

##### 5. 프라이버시 및 보안 강화 (Android 15+)

- **스크린샷 탐지 (Screenshot Detection)**: `Activity.setScreenCaptureCallback()` 을 통해 앱이 활성화된 상태에서 스크린샷이 찍혔음을 감지하고 대응(예: 민감 정보 가리기)할 수 있습니다.
- **백그라운드 활동 제한**: 앱이 백그라운드 상태에서 다른 앱의 Activity 를 무단으로 시작하는 것이 더욱 엄격하게 제한됩니다.
- **개인정보 보호 공간 (Private Space)**: 민감한 앱을 별도의 격리된 공간에 설치하고 생체 인증으로 잠글 수 있는 기능이 추가되었습니다.

---

#### ⚙️ AppOps (Fine-grained Monitoring)

`AppOps` 는 권한보다 더 세분화된 실행 단위의 기록과 제어를 담당합니다.

- **상태바 인디케이터 (Privacy Indicators)**: 마이크나 카메라 사용 시 오렌지/그린 점으로 사용자에게 실시간 알림.
- **Privacy Dashboard (Android 12+)**: 사용자가 지난 24 시간 동안의 권한 사용 타임라인(언제, 어떤 앱이 위치/카메라 등을 썼는지)을 확인하고 제어할 수 있는 통합 대시보드.
- **자동 리셋**: 3 개월간 사용하지 않은 앱의 권한을 시스템이 자동으로 회수.

```bash
# 특정 앱의 AppOps 상태 조회
adb shell appops get com.example.app
```

---

#### 💡 베스트 프랙티스

1. **최소 권한의 원칙**: 기능 구현에 반드시 필요한 최소한의 권한만 요청하십시오.
2. **컨텍스트 기반 요청**: 앱 시작 시점이 아닌, 해당 기능이 실제로 사용되는 시점(Point of Use)에 요청하십시오.
3. **투명한 설명**: `shouldShowRequestPermissionRationale` 을 활용하여 권한이 왜 필요한지 명확히 설명하십시오.

#### 디버깅 팁

```bash
# 권한 강제 부여/취소
adb shell pm grant com.example.app android.permission.CAMERA
adb shell pm revoke com.example.app android.permission.CAMERA

# 특정 앱의 현재 권한 상태 확인
adb shell dumpsys package com.example.app | grep "granted=true"
```

#### 연관 문서

- [[android-security-sandbox]] - UID 기반 격리
- [[android-storage-systems]] - Scoped Storage 및 파일 접근 보안
- [[mobile-vulnerability-check]] - 보안 취약점 점검표
