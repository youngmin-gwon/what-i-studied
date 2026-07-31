---
title: 08-treble-system-vendor-분리-2017
tags: []
aliases: []
date modified: 2026-07-31 15:42:55 +09:00
date created: 2026-07-31 15:38:23 +09:00
---

## Treble: System/Vendor 분리 (2017)

상위 노트: [02-주요-기술-전환](01_inbox/mobile/android/00_foundations/history/android-evolution-history/02-%EC%A3%BC%EC%9A%94-%EA%B8%B0%EC%88%A0-%EC%A0%84%ED%99%98.md)

**Before Treble**:

```
/system
  ├─ framework
  ├─ vendor 코드 (섞여있음)
  └─ HAL 구현

업데이트 시 vendor 재빌드 필요 → 지연
```

**After Treble** (Android 8.0):

```
/system (Google 관리)
  ├─ framework
  └─ 일반 HAL 인터페이스

/vendor (OEM 관리)
  ├─ HAL 구현
  └─ 드라이버

VINTF로 호환성 보장
```

**효과**:

- 업데이트 속도 향상
- Google 이 /system 만 업데이트 가능
- OEM 부담 감소
