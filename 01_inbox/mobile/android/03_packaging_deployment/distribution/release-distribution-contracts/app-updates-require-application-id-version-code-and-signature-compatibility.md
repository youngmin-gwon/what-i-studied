---
title: "앱 업데이트는 applicationId, versionCode, 서명 호환성으로 결정된다"
tags: ["android", "android/packaging-deployment"]
---

# 앱 업데이트는 applicationId, versionCode, 서명 호환성으로 결정된다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [Play 릴리스와 배포 계약](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/release-distribution-contracts.md)

## Android가 업데이트를 받아들이는 조건

기존 설치 앱을 업데이트하려면 다음 조건을 만족해야 한다.

- application ID, 즉 패키지 식별자가 기존 앱과 같아야 한다.
- 업데이트 서명 인증서가 기존 설치 앱의 인증서와 같아야 한다.
- 인증서 키 교체를 사용한다면 Android가 인정하는 유효한 proof-of-rotation을 포함해야 한다.
- 일반 업데이트는 설치된 앱보다 낮은 version code를 허용하지 않는다.
- Play Console에서 기존 앱의 업데이트를 제출할 때는 현재 버전보다 높은 version code를 사용해야 한다.

실무상 Play 배포 업데이트는 같은 application ID, 호환되는 서명 체계, 증가한 version code를 기준으로 설계한다. version name은 사용자에게 보이는 식별자이며 업데이트 순서를 결정하지 않는다.

## 트랙과 version code

- 사용자는 자신이 받을 자격이 있는 트랙 중 호환되는 가장 높은 version code를 받는다.
- Production은 모든 사용자에게 기본적으로 자격이 있다.
- 테스트 참여자는 해당 트랙에 포함되고 opt-in해야 한다.
- 내부 테스트 참여자는 open 또는 closed 테스트의 높은 version code를 받지 않는 예외가 생길 수 있다.
- 따라서 테스트 트랙 간 version code를 무심코 앞서게 하지 않는다.

## 서명 점검

1. 기존 Play 앱의 앱 서명 인증서 지문을 확인한다.
2. 새 AAB의 업로드 인증서가 등록된 업로드 키와 일치하는지 확인한다.
3. Play가 생성한 배포 APK의 앱 서명 인증서를 확인한다.
4. 외부 인증 서비스에 등록된 지문과 환경별 지문을 비교한다.
5. application ID, version code, min/target SDK, ABI를 release 기록에 남긴다.

## 실패를 예방하는 질문

- 새 빌드가 다른 application ID로 생성되지 않았는가?
- version name만 올리고 version code를 잊지 않았는가?
- CI가 debug keystore 또는 오래된 업로드 키를 사용하지 않는가?
- API 제공자에 로컬 업로드 인증서만 등록하지 않았는가?
- 키 업그레이드 후 App Links와 공유 사용자 정의 권한을 검증했는가?

## 업데이트 실패 시 분류

- application ID 오류는 다른 앱으로 식별된 빌드 문제다.
- version code 오류는 릴리스 번호 정책 또는 트랙 우선순위 문제다.
- 인증서 오류는 업로드 키, 앱 서명 키, 외부 서비스 지문을 분리해 조사한다.
- Play 업로드 오류와 기기 설치 오류를 같은 원인으로 단정하지 않는다.

공식 문서: [앱 업데이트 또는 게시 취소](https://support.google.com/googleplay/android-developer/answer/9859350), [앱 버전 관리](https://developer.android.com/studio/publish/versioning), [인앱 업데이트](https://developer.android.com/guide/playcore/in-app-updates)

기준일: 2026-07-31. Play 정책과 Android 플랫폼의 키 회전 동작은 대상 API 수준에 따라 달라질 수 있다.
