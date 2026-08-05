---
title: manifest-declares-components-permissions-features-and-exported-boundaries
tags: [android, android/app-components, android/architecture]
aliases: ["Manifest는 컴포넌트, 권한, 기능, exported 경계를 선언한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Manifest는 컴포넌트, 권한, 기능, exported 경계를 선언한다

`AndroidManifest.xml` 파일은 단순한 서술서가 아니다. **안드로이드 OS(PackageManagerService)가 APK 패키지를 분석하여 앱의 4대 컴포넌트 존재 여부, 필요 시스템 권한(`<uses-permission>`), 기기 하드웨어 요구사항(`<uses-feature>`), 그리고 외부 진입 경계(`android:exported`)를 최종 확인하는 메인 아키텍처 명세서**다.

---

### 1. 관련 문서 및 참조

- 상위 문서: [App Component Contracts](./app-component-contracts.md)
- 공식 문서: [App Manifest Overview](https://developer.android.com/guide/topics/manifest/manifest-intro)

검증일: 2026-08-05. Manifest 역할 검증 완료.
