---
title: "APK와 AAB는 안드로이드 앱을 배포하고 설치하는 패키지 포맷이다"
tags: ["android", "android/glossary"]
aliases: ["AAB", "Android App Bundle", "Android Package", "APK"]
date modified: 2026-08-01 01:07:15 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## APK 와 AAB

정의: APK 는 device 에 설치되는 artifact 이고, AAB 는 Play 가 device 별 APK 를 생성하기 위해 받는 publishing artifact 다.

혼동 방지: AAB 를 올린다고 device 가 AAB 를 실행하는 것은 아니다. 설치, 업데이트, signing compatibility 를 판단할 때는 최종 APK, applicationId, versionCode, signing lineage 를 기준으로 봐야 한다.

정본 링크:

- [AAB publishing artifact](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/aab-is-publishing-artifact-for-play-generated-apks.md)
- [App update compatibility](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/app-updates-require-application-id-version-code-and-signature-compatibility.md)
