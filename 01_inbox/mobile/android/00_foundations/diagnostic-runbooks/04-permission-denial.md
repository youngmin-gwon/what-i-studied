---
title: 권한이 있는데도 API가 실패하거나 거부된다
tags: ["android", "android/foundations", "diagnostic-runbook"]
aliases: ["Runbook: permission denial despite granted permission"]
date modified: 2026-08-04 10:45:00 +09:00
date created: 2026-08-04 10:45:00 +09:00
---

## 권한이 있는데도 API가 실패하거나 거부된다

### 증상

앱이 런타임 권한을 요청해 사용자가 승인했는데도, 해당 기능(카메라, 위치, 알림 등)이 예외를 던지거나, 조용히 실패하거나, 빈 값을 반환한다.

### 재현 조건

- 정확히 어느 permission을 사용하는 API인지, 그리고 문제가 foreground에서도 나는지 background에서만 나는지 구분한다.
- 재현 기기에서 설정 → 앱 → 권한 화면을 직접 열어 현재 상태(항상 허용/사용 중에만 허용/거부)를 스크린샷으로 남긴다. 코드로 확인하는 grant 상태와 대조하기 위함이다.

### 가능한 실패 경계와 우선순위

권한이 있는데도 실패한다는 증상은 하나의 원인이 아니라 서로 독립적인 여러 gate 중 어느 하나가 막고 있다는 뜻이다. 다음 순서로 좁힌다.

1. **Manifest 선언은 있는가?** 있어야 요청 자체가 성립한다.
2. **Runtime grant 상태는 실제로 granted인가?** 매니페스트 선언과 런타임 grant는 다른 사실이다.
3. **요청한 권한이 여러 단계로 나뉘는 권한인가?**(예: 위치의 foreground/background, Android 12+의 정밀/대략) 한 단계만 승인되고 다른 단계는 승인되지 않았을 수 있다.
4. **AppOps가 실행 시점에 별도로 거부하고 있는가?** permission이 granted여도 AppOps 모드가 `MODE_IGNORED`/`MODE_ERRORED`면 조용히 실패한다.
5. **자원이 다른 프로세스에 의해 점유돼 있는가?**(카메라 등 독점 자원의 경우) 이는 권한/AppOps와 무관한 별도 원인이다.
6. **signature 권한인가?** 서명이 다르면 사용자 승인 자체가 불가능하다.

### 조사 절차

1. **Manifest 선언과 runtime grant 상태를 분리해서 확인한다.**
   ```bash
   adb shell dumpsys package <pkg> | grep -A5 "runtime permissions"
   ```
   `granted=true/false`를 확인한다. 이 시점에 여러 단계로 나뉘는 권한(예: `ACCESS_FINE_LOCATION`과 `ACCESS_BACKGROUND_LOCATION`)이 있다면 **하나만 보지 말고 관련된 모든 권한을 각각 확인한다.**

2. **AppOps 모드를 별도로 확인한다.**
   ```bash
   adb shell dumpsys appops <pkg>
   ```
   해당 op(예: `CAMERA`, `COARSE_LOCATION`)의 모드가 `allow`가 아니면, permission이 granted여도 시스템이 실행을 막고 있다는 뜻이다. 사용자가 설정에서 개별 op를 끌 수 있으므로, permission 화면에는 안 보이는 이 상태를 따로 확인해야 한다.

3. **정확도/범위가 강등됐는지 확인한다(위치의 경우).**
   반환된 `Location.getAccuracy()` 값을 로그로 남긴다. 사용자가 "정확한 위치"를 끄면 `ACCESS_FINE_LOCATION`이 매니페스트에 있어도 좌표가 낮은 해상도로 반환되며, 이것은 예외가 아니라 조용한 값 저하로 나타난다.

4. **자원 점유 여부를 확인한다(카메라 등).**
   ```bash
   adb shell dumpsys media.camera
   ```
   `CameraAccessException`의 오류 코드(`ERROR_CAMERA_IN_USE` 등)로 권한 문제와 점유 문제를 구분한다.

5. **호출자 UID/서명을 확인한다(다른 앱이 이 앱의 컴포넌트나 signature 권한을 요구하는 API를 호출하는 경우).**
   시스템은 앱이 스스로 주장하는 식별자가 아니라 커널이 확인한 실제 UID로 판정한다. `sharedUserId` 구성(레거시)이 있다면 이 구분이 특히 중요하다.

6. **실패 로그의 정확한 문구를 확인한다.**
   "Permission Denial"(SecurityException 계열) 로그는 대체로 명시적인 권한/게이트 거부를 가리키지만, 일부 컴포넌트(Activity의 `exported=false` 거부 등)는 겉보기에 "대상이 없다"는 신호(`ActivityNotFoundException`)로 나타날 수 있다. 예외 이름만으로 원인을 단정하지 않는다.

### OS/API/target SDK 조건

- 위치의 foreground/background 2단계 모델은 Android 10(API 29) 이상에서, background 권한을 시스템 다이얼로그로 즉시 요청할 수 없는 제약은 Android 11(API 30) 이상에서 적용된다.
- 정밀/대략 위치 분리는 Android 12(API 31) 이상에서 적용된다.
- targetSdkVersion 31 이상에서는 intent-filter가 있는 컴포넌트의 `exported` 값을 명시하지 않으면 애초에 설치되지 않는다 — 이 경우는 런타임 실패가 아니라 설치 실패이므로 [install/update runbook](08-install-update-failure.md)을 함께 본다.

### 다음 조사 경로

- AppOps가 원인이면 → 사용자가 설정에서 개별 차단했을 가능성이 크므로 UX상 재요청/안내 경로 설계
- 카메라·마이크 등 독점 자원 점유가 원인이면 → 가용성 콜백을 먼저 등록해 사전에 감지하는 설계로 전환
- 이 실패가 특정 targetSdkVersion 업데이트 직후 새로 생겼다면 → [compatibility 관련 Learning Spine 12장](../learning-spine/12-compatibility-update-and-form-factor.md)에서 해당 버전의 behavior change 확인

### 관련 자료

- [Worked Example: permission이 있는데 API가 실패하는 사례](../worked-examples/06-permission-granted-but-api-fails.md)
- [Worked Example: 사진 촬영, preview, 저장, 업로드까지](../worked-examples/02-photo-capture-preview-save-upload.md)
- [AppOps는 permission 승인 뒤에도 실행 시점 정책을 추가로 거부할 수 있다](../../04_system_services/service-lookup/service-lookup-contracts/appops-can-deny-after-permission-is-already-granted.md)
- [권한 디버깅은 manifest, grant state, AppOps를 분리해 확인한다](../../05_security_privacy/permissions-and-sandbox/permission-contracts/permission-debugging-separates-manifest-grant-and-appops-state.md)
- [Learning Spine 9장 Identity, 권한과 독립적인 security gate](../learning-spine/09-identity-permission-and-independent-security-gates.md)

### 공식 근거

- [Permissions on Android](https://developer.android.com/guide/topics/permissions/overview)
- [Access location permissions](https://developer.android.com/develop/sensors-and-location/location/permissions)

검증일: 2026-08-04. 이 runbook은 Learning Spine 9장과 Worked Example 2·6에서 이미 원문 대조를 마친 내용을 재사용했다.
