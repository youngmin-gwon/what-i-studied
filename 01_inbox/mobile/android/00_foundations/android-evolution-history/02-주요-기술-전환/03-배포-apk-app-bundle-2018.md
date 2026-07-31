---
title: 03-배포-apk-app-bundle-2018
tags: []
aliases: []
date modified: 2026-07-31 15:40:22 +09:00
date created: 2026-07-31 15:38:23 +09:00
---

## 배포: APK → App Bundle (2018)

상위 노트: [[02-주요-기술-전환]]

**APK (Android Package)**:

- 모든 리소스/코드 포함
- 모든 기기에 동일한 파일 → 비효율

**AAB (Android App Bundle, 2018)**:

```
Before (APK):
  app-release.apk (50MB)
  ├─ arm64-v8a libs
  ├─ armeabi-v7a libs  ← 불필요 (기기가 arm64일 때)
  ├─ x86 libs          ← 불필요
  ├─ xxhdpi resources
  └─ xxxhdpi resources ← 불필요

After (AAB):
  Play Store가 기기별 APK 생성
  Pixel 6 Pro → arm64 + xxxhdpi만 (30MB)
```

**효과**:

- 평균 15% 크기 감소
- Dynamic Feature Module 지원
