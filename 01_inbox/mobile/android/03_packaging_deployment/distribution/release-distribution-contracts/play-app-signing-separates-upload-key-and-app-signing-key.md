---
title: play-app-signing-separates-upload-key-and-app-signing-key
tags: ["android", "android/packaging-deployment"]
aliases: []
date modified: 2026-08-03 18:12:50 +09:00
date created: 2026-07-31 17:52:17 +09:00
---

## Play App Signing 은 업로드 키와 앱 서명 키를 분리한다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)

관련 지도: [Play 릴리스와 배포 계약](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/release-distribution-contracts.md)

### 두 키를 분리한다

Play App Signing 에서는 업로드 키와 앱 서명 키의 역할이 다르다.

- 업로드 키: 개발자가 AAB 를 Play Console 에 올리기 전에 서명한다.
- 앱 서명 키: Google Play 가 사용자에게 전달할 APK 에 서명한다.
- 업로드 키를 잃어버려도 앱 서명 키를 바꾸지 않고 업로드 키 재설정을 요청할 수 있다.
- 앱 서명 키의 비밀키는 Play App Signing 설정 후 개발자가 내려받는 방식으로 관리하지 않는다.

### 설정 원칙

신규 앱은 Play App Signing 을 전제로 준비한다. 기존 APK 앱을 전환할 때는 기존 앱 서명 키의 보존과 Play 의 등록 절차를 확인한다.

- release AAB 는 등록된 업로드 키로 서명한다.
- Play 에 전달되는 최종 APK 의 인증서는 Play Console 의 앱 서명 인증서다.
- Google API, OAuth, Maps, App Links 등 인증서 지문을 요구하는 서비스에는 앱 서명 인증서 지문을 등록한다.
- 로컬 빌드용 업로드 인증서만 등록하면 Play 에서 설치된 앱과 인증서가 달라질 수 있다.

### 키 분실과 침해

- 업로드 키 분실 또는 비밀번호 문제는 업로드 키 재설정 절차의 대상이다.
- 앱 서명 키 침해 또는 더 강한 키가 필요한 경우에는 앱 서명 키 업그레이드의 영향 범위를 검토한다.
- 키 업그레이드는 단순한 업로드 키 교체가 아니다.
- 공유 데이터, 사용자 정의 권한, App Links 인증서처럼 지문을 저장하는 연동 지점을 함께 점검한다.
- 운영 중인 키 변경은 기존 Android 버전과 Play 보호 동작이 달라질 수 있으므로 별도 마이그레이션 계획을 둔다.

### 운영 규칙

1. 업로드 키 keystore 와 비밀번호를 비밀 저장소에 둔다.
2. CI 에는 최소 권한의 업로드 계정과 서명 설정만 제공한다.
3. Play Console 의 앱 무결성 화면에서 업로드·앱 서명 인증서 지문을 기록한다.
4. release 후보의 AAB 인증서를 `jarsigner` 또는 Play 검증 결과로 확인한다.
5. 키를 교체하기 전 외부 API 와 설치된 구버전의 호환성을 시험한다.

### 릴리스 기록

- 어떤 키로 서명했는지와 Play 에서 확인한 인증서 지문을 릴리스마다 남긴다.
- 키 변경 요청의 승인자와 적용 버전을 기록한다.
- CI 에서 사용하는 업로드 키와 개발자 로컬 키를 같은 것으로 취급하지 않는다.

공식 문서: [앱 서명](https://developer.android.com/studio/publish/app-signing), [Play App Signing 사용](https://support.google.com/googleplay/android-developer/answer/9842756), [AAB FAQ의 서명 설명](https://developer.android.com/guide/app-bundle/faq)

기준일: 2026-07-31. 여기서 "배포 키"라는 표현은 혼동을 피하기 위해 사용하지 않고, 업로드 키와 앱 서명 키를 구분한다.
