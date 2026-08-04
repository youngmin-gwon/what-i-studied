---
title: signed artifact가 Play delivery를 거쳐 update되는 과정
tags: ["android", "android/foundations", "worked-example"]
aliases: ["Signed artifact through Play delivery to update"]
date modified: 2026-08-04 03:20:00 +09:00
date created: 2026-08-04 03:20:00 +09:00
---

## signed artifact가 Play delivery를 거쳐 update되는 과정

이 예시는 Learning Spine 3·11장을 하나의 배포 파이프라인으로 잇는다. 3장에서 다룬 서명·버전 identity가 Play App Signing이라는 실제 배포 인프라를 거치며 어떻게 유지되는지, 11장에서 다룬 테스트 트랙과 단계적 출시가 이 identity 위에서 어떻게 작동하는지를 연결한다.

### 시작 상태

앱은 이미 production에 배포돼 있고, 사용자 기기에 설치돼 있다. Play App Signing이 활성화돼 있어 개발자는 업로드 키만 갖고 있고, 최종 배포 APK에 서명하는 앱 서명 키는 Google이 보관한다. 개발자는 새 버전(더 높은 `versionCode`)을 준비했다.

### 입력

개발자가 release variant로 AAB를 빌드해 등록된 업로드 키로 서명하고, Play Console에 업로드한다.

### 단계별 흐름

1. **빌드와 서명(3장)**: AAB는 release build type으로 생성되고, 업로드 키로 서명된다. `applicationId`는 기존 Play 앱과 같아야 하고, `versionCode`는 기존 배포 버전보다 높아야 한다.
2. **Play 서버의 재서명**: Play는 업로드 키 서명을 검증한 뒤, 이 AAB로부터 기기별 최적화된 APK 세트를 생성하고, 그 APK들을 Google이 보관하는 앱 서명 키로 다시 서명한다. 사용자 기기에 도달하는 최종 서명은 개발자의 업로드 키가 아니라 이 앱 서명 키다.
3. **사전 검증 트랙(11장)**: 내부 테스트에서 설치·업데이트가 정상 동작하는지 먼저 확인하고, 필요하면 비공개 테스트로 넓힌다. 이 단계에서 실제로 재서명된 APK의 설치·업데이트 결과를 확인한다.
4. **단계적 출시 시작(11장)**: 문제가 없으면 production 트랙에서 작은 비율의 사용자부터 단계적 출시를 시작한다. 충돌률, ANR, 핵심 기능 오류 지표를 관찰한 뒤에만 대상 비율을 수동으로 늘린다.
5. **기기에서의 설치(3장)**: 대상 사용자의 기기에서 Play 앱이 새 APK를 내려받는다. 기기의 PackageInstaller/PackageManager는 이 APK가 기존 설치와 같은 `applicationId`를 갖는지, 서명 인증서(이번에는 Play의 앱 서명 키)가 기존 설치와 일치하는지, `versionCode`가 더 높은지를 검증한다.
6. **검증 통과 시 갱신**: 세 조건이 모두 만족되면 이것은 새 설치가 아니라 기존 숫자 appId, UID, 데이터 디렉터리를 그대로 이어받는 업데이트로 처리된다.

### 성공 결과

사용자는 기존 앱 데이터와 로그인 상태를 유지한 채 새 버전을 사용한다. 단계적 출시 지표에 이상이 없으면 개발자는 대상 비율을 100%까지 수동으로 확대한다.

### 관찰 가능한 신호

- Play Console의 App Signing 페이지에서 앱 서명 키 인증서 지문을 확인할 수 있다.
- 단계적 출시 대시보드에서 각 확대 시점의 대상 비율과 충돌률·ANR 지표를 확인한다.
- 기기 쪽에서는 `adb shell dumpsys package <pkg>`로 설치된 버전의 `versionCode`와 서명 정보를 확인할 수 있다.
- 문제 발견 시 rollout을 중지하면 아직 받지 않은 사용자에게 확산이 멈추지만, 이미 받은 사용자는 자동으로 이전 버전으로 돌아가지 않는다 — 이 사실 자체가 배포 전 반드시 알아야 할 관찰 신호다.

### 실패 분기: 서명이 일치하지 않아 업데이트가 거부된다

1. QA 담당자의 테스트 기기에는 로컬 keystore로 직접 서명한 release 빌드가 이미 설치돼 있다(예: CI가 아직 Play 트랙을 거치지 않은 초기 검증용 빌드).
2. 이후 이 기기에 Play를 통해 같은 `applicationId`, 더 높은 `versionCode`를 가진 새 버전을 설치하려 한다. 이번에는 서명이 Play의 앱 서명 키다.
3. 기기의 PackageManager는 `applicationId`는 같지만 서명 인증서가 기존 설치와 다르다는 것을 확인한다.
4. 시스템은 이를 업데이트로 인정하지 않는다. 같은 `applicationId`를 가진 상태에서 서명만 다르면 설치 자체가 거부된다.
5. 사용자(또는 QA)는 "업데이트가 안 된다"는 모호한 실패를 만난다. 원인을 좁히려면 기존 설치의 서명과 새 APK의 서명을 나란히 비교해야 한다.

이 실패는 `applicationId`가 같다는 사실 하나만으로 "같은 앱으로 업데이트된다"고 가정하면 안 된다는 3장의 원칙을 그대로 보여준다. 로컬 서명 빌드와 Play App Signing을 거친 빌드가 같은 `applicationId`를 공유하는 상황은 개발 초기에 흔히 발생하며, 해결하려면 QA 기기에서 기존 설치를 완전히 삭제한 뒤 Play 경로로 다시 설치해야 한다(이 경우 UID와 데이터는 새로 시작된다).

### 관련 원자 노트

- [Play App Signing은 업로드 키와 앱 서명 키를 분리한다](../../03_packaging_deployment/distribution/release-distribution-contracts/play-app-signing-separates-upload-key-and-app-signing-key.md)
- [앱 업데이트는 applicationId, versionCode, 서명 호환성을 요구한다](../../03_packaging_deployment/distribution/release-distribution-contracts/app-updates-require-application-id-version-code-and-signature-compatibility.md)
- [AAB는 Play가 생성하는 APK를 위한 퍼블리싱 아티팩트다](../../03_packaging_deployment/distribution/release-distribution-contracts/aab-is-publishing-artifact-for-play-generated-apks.md)
- [Play 릴리스 체크리스트는 산출물, 서명, 트랙, 롤백 조건을 고정한다](../../03_packaging_deployment/distribution/release-distribution-contracts/play-release-checklist-freezes-artifact-signing-track-and-rollback-conditions.md)
- [Google Play 테스트 트랙은 배포 대상과 피드백 범위를 나눈다](../../03_packaging_deployment/distribution/release-distribution-contracts/google-play-testing-tracks-split-audience-and-feedback-scope.md)
- [단계적 출시는 관측 가능한 릴리스 운영 절차다](../../03_packaging_deployment/distribution/release-distribution-contracts/staged-rollout-is-observable-release-operation.md)

### 관련 Learning Spine 장

- [3장 소스에서 설치된 패키지까지](../learning-spine/03-source-to-installed-package.md)
- [11장 관찰, 테스트와 품질 feedback](../learning-spine/11-observation-testing-and-quality-feedback.md)

### 공식 근거

- [앱 서명](https://developer.android.com/studio/publish/app-signing)
- [Play App Signing 사용](https://support.google.com/googleplay/android-developer/answer/9842756)
- [단계적 출시로 업데이트 제공](https://support.google.com/googleplay/android-developer/answer/6346149)

검증일: 2026-08-04. 이 예시는 3·11장에서 이미 원문 대조를 마친 서명·배포 관련 원자 노트를 재사용했다.
