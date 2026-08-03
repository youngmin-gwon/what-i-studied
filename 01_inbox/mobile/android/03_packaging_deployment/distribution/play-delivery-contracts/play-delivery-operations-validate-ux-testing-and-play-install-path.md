---
title: play-delivery-operations-validate-ux-testing-and-play-install-path
tags: ["android", "android/packaging-deployment"]
aliases: []
date modified: 2026-08-03 18:12:43 +09:00
date created: 2026-07-31 17:52:17 +09:00
---

## Play Delivery 운영은 UX, 테스트, Play 설치 경로를 함께 검증한다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)

관련 지도: [Play Delivery 계약](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/play-delivery-contracts.md)

관련 노트: [Google Play 테스트 트랙은 배포 대상과 피드백 범위를 나눈다](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/google-play-testing-tracks-split-audience-and-feedback-scope.md), [Play 릴리스 체크리스트는 산출물, 서명, 트랙, 롤백 조건을 고정한다](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/play-release-checklist-freezes-artifact-signing-track-and-rollback-conditions.md)

### 사용자 흐름

- 다운로드가 필요한 기능의 진입 버튼에 예상 크기와 상태를 표시한다.
- 진행률, 설치 중, 완료, 실패, 사용자 확인, Wi-Fi 대기를 구분한다.
- 네트워크 실패와 저장 공간 부족에 재시도·취소 경로를 제공한다.
- 다운로드 중 화면을 닫았다가 돌아와도 session 상태를 복원한다.
- 기능이 준비되기 전에는 관련 코드와 리소스를 호출하지 않는다.
- 로그인·결제처럼 실패 비용이 큰 흐름은 모듈 준비를 먼저 확인한다.

### 모듈 검증

- base 만 설치해 앱의 최소 실행 경로를 확인한다.
- 각 dynamic feature 를 on-demand 로 요청하고 설치 완료 뒤 진입한다.
- 이미 설치된 모듈을 다시 요청할 때 중복 UI 가 나오지 않는지 확인한다.
- 앱 업데이트 후 모듈 버전과 캐시가 일치하는지 확인한다.
- 모듈 제거 후 재요청, 앱 데이터 삭제 후 재설치를 확인한다.
- 낮은 API, 국가, RAM, 기기 모델, system feature 조건을 각각 검증한다.
- Play 내부 테스트에서 실제 Play split 전달을 확인한다.

### Asset pack 검증

- install-time 리소스는 첫 실행에서 즉시 읽을 수 있는지 확인한다.
- fast-follow 완료 전에도 게임의 최소 실행이 가능한지 확인한다.
- on-demand 요청의 크기 고지와 200MB 모바일 데이터 확인 흐름을 검증한다.
- 업데이트 중 asset pack 위치 변경과 일시적 미가용 상태를 처리한다.
- 로컬 테스트 결과를 Play 운영 결과로 간주하지 않는다.

### 관측 지표

모듈별 요청 횟수, 성공률, 실패 코드, 평균 다운로드 시간, 취소율을 기록한다.

기능 진입 실패와 앱 시작 ANR 을 배포 모드별로 분리해 본다.

asset pack 은 pack 상태와 실제 콘텐츠 로딩 실패를 따로 기록한다.

사용자 개인정보나 링크 파라미터를 불필요하게 로그에 남기지 않는다.

### 출시 전 확인

- 새 bundle 의 모듈 목록과 delivery 선언을 리뷰한다.
- Play Console 경고와 기기별 생성 APK 를 확인한다.
- 느린 네트워크와 오프라인 재진입을 수동으로 테스트한다.
- 사용자가 취소한 뒤 기능을 다시 요청할 수 있는지 확인한다.
- 롤백 버전에서도 설치된 모듈을 안전하게 인식하는지 확인한다.
- 종료된 Instant 경로가 릴리스 산출물과 링크 라우팅에 남아 있지 않은지 확인한다.

### 공식 문서

- [UX best practices for on-demand delivery](https://developer.android.com/guide/playcore/feature-delivery/ux-guidelines)
- [Manage installed modules](https://developer.android.com/guide/playcore/feature-delivery/on-demand#manage-installed-modules)
- [Play as you Download best practices](https://developer.android.com/google/play/play-as-you-download/best-practices)
