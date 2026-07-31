# 내부 앱 공유는 릴리스 트랙이 아니라 빠른 아티팩트 공유다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [Play 릴리스와 배포 계약](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/release-distribution-contracts.md)

## 목적

Internal App Sharing은 Play Console에서 AAB 또는 APK를 빠르게 올리고 다운로드 링크로 팀과 테스터에게 공유하는 별도 검증 경로다.

## 테스트 트랙과의 차이

- 내부 앱 공유 아티팩트는 App bundle explorer에 표시되지 않는다.
- 내부 앱 공유 아티팩트는 내부·비공개·공개 테스트나 production 릴리스에 포함할 수 없다.
- 정식 트랙의 version code 규칙을 대신하지 않는다.
- Play가 전달하는 서명·분할 결과를 빠르게 확인할 때 유용하다.

## 업로드와 접근

1. Play Console에서 권한이 있는 업로더가 AAB 또는 APK를 업로드한다.
2. 업로드가 끝나면 생성된 링크를 복사한다.
3. 테스터는 Play Store에서 Internal App Sharing을 활성화한다.
4. 링크를 열어 설치하고 기기·계정·스토어 등록 가능 여부를 확인한다.

## 버전과 서명 특성

- 내부 앱 공유에서는 version code가 새롭거나 전역적으로 고유할 필요가 없고 재사용할 수 있다.
- 디버그 가능 AAB/APK도 공유할 수 있다.
- 업로드 파일은 production 또는 upload key로 서명할 필요가 없다.
- Play는 내부 앱 공유 전용 키로 아티팩트를 다시 서명한다.
- 따라서 API 제공자 연동 테스트에는 내부 앱 공유 인증서 지문을 별도로 등록해야 할 수 있다.

## 링크와 테스터 제한

- 하나의 링크로 다운로드할 수 있는 사용자는 최대 100명이다.
- 링크는 업로드 후 60일이 지나면 만료된다.
- 더 많은 사용자나 새 유효기간이 필요하면 같은 아티팩트를 다시 업로드하여 새 링크를 만든다.
- 앱이 해당 사용자의 국가·계정에서 Play에 제공되지 않으면 링크가 있어도 설치할 수 없다.

## 적합한 용도

- Play가 생성한 전달 APK를 빠르게 확인한다.
- 특정 커밋의 AAB를 QA 팀에 공유한다.
- 정식 트랙 version code를 소모하지 않고 설치 흐름을 재현한다.

운영 환경과 같은 정식 업데이트 경로를 검증하려면 내부 테스트 트랙 또는 비공개 테스트를 사용하고, 내부 앱 공유 결과를 production 품질의 승인으로 간주하지 않는다.

공식 문서: [AAB와 APK 내부 공유](https://support.google.com/googleplay/android-developer/answer/9844679), [테스트 트랙 설정](https://support.google.com/googleplay/android-developer/answer/9845334)

기준일: 2026-07-31. 링크 만료·사용자 상한·재서명 조건은 최신 Play Console Help 기준이다.
