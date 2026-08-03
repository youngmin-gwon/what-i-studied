---
title: release-distribution-contracts
tags: ["android", "android/packaging-deployment"]
aliases: []
date modified: 2026-08-03 17:20:50 +09:00
date created: 2026-07-31 17:52:17 +09:00
---

## Play 릴리스와 배포 계약

이 지도는 Android App Bundle 제출, Play App Signing, 업데이트 조건, 테스트 트랙, staged rollout, 내부 공유를 릴리스 운영 단위로 나눈다.

### 정본 노트

- [AAB는 Play가 기기별 APK를 생성하는 게시 아티팩트다](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/aab-is-publishing-artifact-for-play-generated-apks.md)
- [Play App Signing은 업로드 키와 앱 서명 키를 분리한다](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/play-app-signing-separates-upload-key-and-app-signing-key.md)
- [앱 업데이트는 applicationId, versionCode, 서명 호환성으로 결정된다](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/app-updates-require-application-id-version-code-and-signature-compatibility.md)
- [Google Play 테스트 트랙은 배포 대상과 피드백 범위를 나눈다](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/google-play-testing-tracks-split-audience-and-feedback-scope.md)
- [단계적 출시는 관측 가능한 릴리스 운영 절차다](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/staged-rollout-is-observable-release-operation.md)
- [내부 앱 공유는 릴리스 트랙이 아니라 빠른 아티팩트 공유다](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/internal-app-sharing-is-fast-artifact-sharing-not-release-track.md)
- [Play 릴리스 체크리스트는 산출물, 서명, 트랙, 롤백 조건을 고정한다](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/play-release-checklist-freezes-artifact-signing-track-and-rollback-conditions.md)

관련 지도: [Play Delivery 계약](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/play-delivery-contracts.md), [의존성, 버전, CI 계약](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/dependency-ci-contracts.md)
