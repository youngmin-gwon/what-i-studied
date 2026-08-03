---
title: staged-rollout-is-observable-release-operation
tags: ["android", "android/packaging-deployment"]
aliases: []
date modified: 2026-08-03 18:12:53 +09:00
date created: 2026-07-31 17:52:17 +09:00
---

## 단계적 출시는 관측 가능한 릴리스 운영 절차다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)

관련 지도: [Play 릴리스와 배포 계약](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/release-distribution-contracts.md)

### 목적

단계적 출시는 기존 앱의 업데이트를 사용자 일부에게 먼저 제공하고, 관찰 결과에 따라 대상 비율을 늘리는 production 또는 테스트 트랙의 운영 방식이다.

### 적용 범위

- 앱의 첫 공개 게시에는 사용할 수 없다.
- 기존 앱의 업데이트 릴리스에 적용한다.
- 대상 비율은 자동으로 증가하지 않으므로 운영자가 직접 다음 비율을 지정한다.
- 기본적으로 사용자는 무작위로 선정되지만, 선택한 국가를 대상으로 제한할 수 있다.
- 전체 대상에 반영되기까지 시간이 걸릴 수 있다.

### 운영 순서

1. 변경 범위와 version code 를 릴리스 기록에 고정한다.
2. 내부·비공개 테스트에서 회귀와 설치·업데이트를 확인한다.
3. 작은 비율로 단계적 출시를 시작한다.
4. 충돌률, ANR, 핵심 기능 오류, 환불·문의, 배터리와 네트워크 지표를 관찰한다.
5. 이상이 없을 때만 다음 비율로 수동 확대한다.
6. 100% 이후에는 전체 사용자 영향과 최신 안정 버전을 기록한다.

### 중지와 재개

- 문제를 발견하면 rollout 을 중지하여 아직 받지 않은 사용자에게 추가 제공을 막는다.
- 이미 해당 버전을 받은 사용자의 앱은 자동으로 이전 버전으로 돌아가지 않는다.
- 기존 AAB 에 문제가 없다면 중지한 rollout 을 같은 사용자 집합에 대해 재개할 수 있다.
- AAB 자체에 문제가 있으면 수정한 새 version code 로 새 릴리스를 만든다.
- 100% 출시 후 중지 기능은 이전에 사용 가능한 릴리스가 있는지와 정책 상태를 함께 고려한다.

### 판단 기준

단계적 출시는 모니터링과 긴급 대응을 포함한 운영 절차다. 단순히 1%, 5%, 20% 같은 고정 숫자를 복사하지 말고 사용자 규모, 위험도, 관찰 가능 시간을 기준으로 결정한다.

스토어 등록정보 변경은 업데이트가 100% 진행된 뒤 반영하는 것이 권장될 수 있으므로 릴리스 내용과 등록정보 변경을 분리해 관리한다.

### 관찰 로그

- 각 확대 시점의 대상 비율과 실제 배포 지연을 기록한다.
- 지표 이상이 발생한 version code 와 기기·국가 범위를 남긴다.
- 중지, 재개, 새 릴리스 생성 중 어느 조치를 택했는지 사유를 기록한다.

공식 문서: [단계적 출시로 업데이트 제공](https://support.google.com/googleplay/android-developer/answer/6346149), [완전히 출시된 릴리스 중지](https://support.google.com/googleplay/android-developer/answer/16285429)

기준일: 2026-07-31. 콘솔의 메뉴명과 중지 기능 범위는 변경될 수 있으므로 실제 출시 화면을 기준으로 확인한다.
