---
title: "APK와 AAB"
tags: ["android", "android/glossary"]
aliases: ["APK", "AAB", "Android Package", "Android App Bundle"]
---

# APK와 AAB

정의: APK는 device에 설치되는 artifact이고, AAB는 Play가 device별 APK를 생성하기 위해 받는 publishing artifact다.

혼동 방지: AAB를 올린다고 device가 AAB를 실행하는 것은 아니다. 설치, 업데이트, signing compatibility를 판단할 때는 최종 APK, applicationId, versionCode, signing lineage를 기준으로 봐야 한다.

정본 링크:
- [AAB publishing artifact](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/aab-is-publishing-artifact-for-play-generated-apks.md)
- [App update compatibility](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/app-updates-require-application-id-version-code-and-signature-compatibility.md)
