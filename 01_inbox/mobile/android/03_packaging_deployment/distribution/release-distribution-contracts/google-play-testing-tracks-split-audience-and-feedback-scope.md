# Google Play 테스트 트랙은 배포 대상과 피드백 범위를 나눈다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [Play 릴리스와 배포 계약](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/release-distribution-contracts.md)

## 트랙의 역할

Play Console에는 내부 테스트, 비공개 테스트, 공개 테스트가 있다. 각 트랙은 배포 대상과 피드백 범위가 다르며 production 출시의 대체물이 아니다.

## 내부 테스트

- 최대 100명의 테스터를 대상으로 빠르게 검증한다.
- 새 AAB는 일반적으로 수분 내 테스터에게 제공되지만 첫 게시나 콘솔 상태에 따라 지연될 수 있다.
- 앱이 완전히 설정되지 않은 초기 QA에도 활용할 수 있다.
- 내부 테스트 앱은 일반 검색으로 발견되지 않을 수 있으므로 Play Store URL을 공유한다.

## 비공개 테스트

- 지정한 이메일 목록 또는 그룹을 대상으로 더 넓은 사전 출시 검증을 한다.
- 여러 비공개 트랙을 만들어 제품 영역이나 국가별 집단을 분리할 수 있다.
- 기존 앱 사용자는 해당 테스트 그룹에 포함되어야 테스트 버전을 받는다.

## 공개 테스트

- Play에 테스트 버전이 노출되고 사용자가 참여할 수 있다.
- 공개 전환 전에 스토어 등록정보와 앱 상태가 외부 사용자에게 공개되어도 되는지 확인한다.
- 테스트 피드백은 공개 평점과 분리되어 처리된다.

## 트랙 선택 순서

권장 흐름은 내부 테스트 -> 소규모 비공개 테스트 -> 필요 시 공개 테스트 -> production이다.

- 내부 테스트를 중단해도 설치된 앱이 자동으로 제거되지는 않는다.
- 내부 테스트에 opt-in한 사용자는 open/closed 테스트 자격과 충돌할 수 있다.
- 사용자가 여러 트랙의 자격을 가지면 호환되는 가장 높은 version code가 선택된다.
- 테스트 트랙의 version code가 production보다 높으면 테스트 참가자가 production 버전을 받지 않을 수 있다.

## 테스터 안내

- 테스터에게 Play Store URL과 opt-in 방법을 함께 제공한다.
- 테스트 참여 상태와 설치된 version code를 버그 보고에 포함하게 한다.
- 테스트 종료 후에도 이미 설치된 앱이 남을 수 있으므로 제거 또는 production 전환 절차를 안내한다.
- 테스트 계정의 국가와 조직 관리 설정도 접근 문제의 원인으로 확인한다.
- 새 릴리스가 보이지 않을 때는 opt-in, 트랙 자격, version code를 순서대로 점검한다.

공식 문서: [내부·비공개·공개 테스트 설정](https://support.google.com/googleplay/android-developer/answer/9845334), [앱 게시 상태](https://support.google.com/googleplay/android-developer/answer/9859751)

기준일: 2026-07-31. 개발자 개인 계정 생성 시점에 따른 사전 테스트 요구사항 등 정책성 조건은 출시 전에 Play Console 안내를 재확인한다.
