---
title: 08-install-update-failure
tags: ["android", "android/foundations", "diagnostic-runbook"]
aliases: ["Runbook: install or update failure"]
date modified: 2026-08-04 10:28:38 +09:00
date created: 2026-08-04 11:05:00 +09:00
---

## 설치 또는 업데이트가 실패한다

### 증상

`adb install` 이 오류를 반환하거나, Play 를 통한 업데이트가 진행되지 않거나, 사용자가 "업데이트할 수 없습니다"를 본다.

### 재현 조건

- **새 설치**인지 **기존 설치 위의 업데이트**인지 먼저 구분한다. 실패 원인의 범주가 다르다.
- 실패한 기기에 현재 어떤 빌드(로컬 서명? Play 서명? 어느 트랙?)가 설치돼 있는지부터 확인한다. 이것이 조사의 절반을 차지한다.

### 가능한 실패 경계와 우선순위

1. **서명 인증서가 기존 설치와 다르다.** 가장 흔한 원인. `applicationId` 가 같아도 서명이 다르면 시스템은 이를 업데이트로 인정하지 않고 설치 자체를 거부한다. 로컬 서명 빌드와 Play App Signing 을 거친 빌드가 섞였을 때 특히 자주 발생한다.
2. **`versionCode` 가 기존 설치보다 낮거나 같다.** 업그레이드 순서 위반.
3. **`applicationId` 가 build variant(예: `applicationIdSuffix`)로 인해 의도와 다르게 빌드됐다.** 다른 앱으로 취급돼 별도 설치가 되거나, 기대한 컴포넌트가 없다는 오류가 난다.
4. **targetSdkVersion 요구사항을 충족하지 못해 설치 자체가 거부된다.** 예: intent-filter 가 있는 컴포넌트의 `exported` 미선언(targetSdkVersion 31+).
5. **Play 배포 단계에서의 문제.** 여러 트랙의 `versionCode` 가 사용자의 트랙 자격을 의도치 않게 덮거나, 테스터가 opt-in 하지 않은 상태.
6. **저장 공간, 서명되지 않은 APK, 손상된 APK 등 기본적인 설치 실패.**

### 조사 절차

1. **`adb install` 의 실패 코드를 먼저 읽는다.**
   ```bash
   adb install -r app-release.apk
   ```

   `INSTALL_FAILED_UPDATE_INCOMPATIBLE` 이나 서명 관련 오류 메시지가 나오면 1 번(서명 불일치)을 우선 의심한다. `INSTALL_FAILED_VERSION_DOWNGRADE` 라면 2 번(versionCode)이다.

2. **기존 설치와 새 APK 의 서명을 나란히 비교한다.**
   ```bash
   adb shell dumpsys package <pkg> | grep -i signature
   ```

   또는 각 APK 의 서명 인증서 지문을 별도로 추출해 비교한다. Play App Signing 을 쓰는 프로젝트라면, 기기에 설치된 것이 로컬 keystore 서명본인지 Play 가 재서명한 것인지부터 확인한다 — 이 둘은 같은 `applicationId` 를 공유해도 다른 서명이다.

3. **`applicationId` 와 `versionCode` 를 빌드 설정에서 확인한다.**
   실제로 빌드된 변형(build variant)의 `applicationIdSuffix`, flavor 별 설정이 의도한 값과 일치하는지 확인한다.

4. **targetSdkVersion 관련 설치 거부인지 확인한다.**
   최근 targetSdkVersion 을 올렸다면, 그 버전의 공식 behavior changes 문서에서 신규 강제 요구사항(예: exported 명시)을 확인한다. 이 경우 실패 메시지가 서명 문제와 겉보기에 비슷하게 모호할 수 있다.

5. **Play 를 통한 배포라면 Play Console 의 App Signing 페이지와 트랙 설정을 확인한다.**
   - 앱 서명 키 인증서 지문이 예상과 일치하는지.
   - 테스트 트랙이라면 테스터가 opt-in 했는지, 여러 트랙의 `versionCode` 가 사용자가 기대하는 트랙보다 낮거나 높지 않은지.
   - 단계적 출시 중이라면 대상 사용자 비율에 이 기기가 포함됐는지(단계적 출시를 중지해도 이미 받은 사용자는 자동으로 이전 버전으로 돌아가지 않는다는 점도 함께 기억한다).

6. **해결을 위해 기존 설치를 지워야 하는 경우, 그 대가를 명시한다.**
   서명 불일치로 막힌 QA 기기 등에서 문제를 해결하려면 기존 앱을 완전히 삭제한 뒤 재설치해야 한다. 이 경우 새 UID 를 받고 기존 데이터·권한 상태는 이어지지 않는다는 것을 알고 진행한다.

### OS/API/target SDK 조건

- 서명 불일치 시 설치가 거부되는 동작은 Android 버전에 걸쳐 안정적인 플랫폼 계약이다.
- targetSdkVersion 별 설치 거부 조건(예: exported 미선언)은 버전마다 다르므로, 최근 targetSdkVersion 을 올렸다면 그 특정 버전의 문서를 반드시 확인한다.
- Play App Signing 관련 정책과 콘솔 UI 는 시점에 따라 바뀔 수 있으므로 실제 배포 시점에 Play Console 안내를 다시 확인한다.

### 다음 조사 경로

- 서명 불일치가 QA/개발 환경에서 반복적으로 발생한다면 → 로컬 서명 빌드와 Play 트랙 빌드를 같은 기기에서 혼용하지 않는 팀 규칙을 검토
- 특정 targetSdkVersion 업데이트 이후 새로 발생했다면 → [Learning Spine 12장](../learning-spine/12-compatibility-update-and-form-factor.md) 의 compatibility 축 판단 모델로
- 설치는 성공했는데 앱 실행이 실패한다면 → [app launch runbook](01-app-launch-slow-or-fails.md)

### 관련 자료

- [Worked Example: signed artifact가 Play delivery를 거쳐 update되는 과정](../worked-examples/08-signed-artifact-through-play-delivery-to-update.md)
- [Play App Signing은 업로드 키와 앱 서명 키를 분리한다](../../03_packaging_deployment/distribution/release-distribution-contracts/play-app-signing-separates-upload-key-and-app-signing-key.md)
- [앱 업데이트는 applicationId, versionCode, 서명 호환성을 요구한다](../../03_packaging_deployment/distribution/release-distribution-contracts/app-updates-require-application-id-version-code-and-signature-compatibility.md)
- [Play 릴리스 체크리스트는 산출물, 서명, 트랙, 롤백 조건을 고정한다](../../03_packaging_deployment/distribution/release-distribution-contracts/play-release-checklist-freezes-artifact-signing-track-and-rollback-conditions.md)
- [Learning Spine 3장 소스에서 설치된 패키지까지](../learning-spine/03-source-to-installed-package.md)

### 공식 근거

- [앱 서명](https://developer.android.com/studio/publish/app-signing)
- [Play App Signing 사용](https://support.google.com/googleplay/android-developer/answer/9842756)

검증일: 2026-08-04. 이 runbook 은 Learning Spine 3 장과 Worked Example 8 에서 이미 원문 대조를 마친 내용을 재사용했다. `adb install` 오류 코드 목록은 실제 발생 시점에 최신 문서로 재확인한다.
