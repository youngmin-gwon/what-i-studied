---
title: 01-런타임-dalvik-art-2014
tags: []
aliases: []
date modified: 2026-07-31 15:40:25 +09:00
date created: 2026-07-31 15:38:23 +09:00
---

## 런타임: Dalvik → ART (2014)

상위 노트: [[02-주요-기술-전환]]

**배경**:

- Dalvik (2008-2013): JIT (Just-In-Time) 컴파일
- 앱 시작 시마다 컴파일 → 느린 시작
- 배터리 소모

**ART (Android Runtime)**:

- Android 4.4 (2013): 옵션으로 제공
- Android 5.0 (2014): 기본값

**장점**:

```
Dalvik (JIT):
  앱 시작 → DEX 해석 → 느림
  
ART (AOT):
  설치 시 → Native 코드 컴파일 → 빠른 시작
  
ART (현대, Profile-Guided):
  설치 → 부분 컴파일
  사용 → 프로파일 수집
  유휴 시 → 최적화 컴파일
```

**성능 개선**:

- 앱 시작: 2 배 빨라짐
- 배터리: 15-20% 절약
- GC 개선: Stop-the-World → Concurrent
