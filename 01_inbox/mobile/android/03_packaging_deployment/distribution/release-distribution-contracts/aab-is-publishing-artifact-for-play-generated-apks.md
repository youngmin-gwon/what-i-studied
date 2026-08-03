---
title: aab-is-publishing-artifact-for-play-generated-apks
tags: []
aliases: []
date modified: 2026-08-03 18:12:46 +09:00
date created: 2026-07-31 17:52:17 +09:00
---

## AAB 는 Play 가 생성하는 APK 를 위한 퍼블리싱 아티팩트다

### AAB 는 Play 가 기기별 APK 를 생성하는 게시 아티팩트다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)

관련 지도: [Play 릴리스와 배포 계약](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/release-distribution-contracts.md)

#### 핵심 판단

Android App Bundle(`.aab`)은 기기에 직접 설치하는 최종 APK 가 아니라 Google Play 가 기기별 APK 를 생성하도록 제출하는 배포 아티팩트다.

#### 구성

- 기본 모듈은 앱 실행에 필요한 공통 코드와 리소스를 담는다.
- 동적 기능 모듈은 기능별로 분리할 수 있다.
- 언어, 화면 밀도, ABI 같은 변형 정보는 Play 의 최적화된 전달 대상이 된다.
- 개발자는 AAB 를 만들고 업로드하지만, 사용자는 Play 가 생성하고 서명한 APK 세트를 받는다.

#### APK 와의 관계

- AAB 는 로컬 기기에서 `adb install` 하는 파일이 아니다.
- 로컬 설치가 필요하면 Android Studio 의 APK 생성 기능이나 `bundletool` 로 기기용 APK 세트를 만든다.
- Play Console 의 App bundle explorer 는 업로드된 번들과 생성된 산출물을 확인하는 기준점이다.
- AAB 의 분할 결과는 기기 구성, Play 의 전달 규칙, 출시 트랙에 따라 달라질 수 있다.

#### 용량 최적화

- 최적화 효과를 고정 비율로 약속하지 않는다. 앱의 리소스와 대상 기기에 따라 달라진다.
- R8 축소와 리소스 축소는 별도의 빌드 설정이며, AAB 자체가 사용하지 않는 코드를 자동으로 모두 제거하지는 않는다.
- 초기 설치 크기와 이후 요청되는 기능·에셋 크기를 각각 측정한다.
- 기능 모듈은 실행 시점 요구사항에 따라 install-time, on-demand 등의 전달 방식을 선택한다.
- 대용량 게임 에셋은 Play Asset Delivery 의 전달 모델을 검토한다.

#### 배포 전 확인

1. release variant 로 AAB 를 생성한다.
2. application ID 와 version code 를 확인한다.
3. 업로드 키로 번들을 서명한다.
4. Play Console 의 App integrity 와 App bundle explorer 에서 인증서와 생성 APK 를 확인한다.
5. 대표 기기와 ABI, 언어, 최소 SDK 조합으로 설치·업데이트를 검증한다.

#### 기록할 정보

- 빌드 커밋과 Gradle release 설정을 기록한다.
- Play 가 생성한 기기별 APK 를 재현할 때 사용한 기기 조건을 남긴다.
- 용량 비교는 같은 기기 조건과 같은 압축·네트워크 조건에서 수행한다.

새 앱의 Google Play 게시에는 AAB 가 기본 요구 형식이며, 큰 앱은 공식 예외와 전달 제품의 적용 조건을 함께 확인한다. 정책은 변경될 수 있으므로 릴리스 시점 문서를 다시 확인한다.

공식 문서: [Android App Bundle 개요](https://developer.android.com/guide/app-bundle), [Android App Bundle 개요](https://developer.android.com/guide/app-bundle), [내부 앱 공유](https://support.google.com/googleplay/android-developer/answer/9844679)

기준일: 2026-07-31. 이 문서는 AAB 의 배포 모델을 설명하며, 특정 앱의 실제 용량 절감률을 보장하지 않는다.
