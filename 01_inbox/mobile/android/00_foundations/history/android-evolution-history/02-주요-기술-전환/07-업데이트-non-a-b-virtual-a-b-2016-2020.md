---
title: 07-업데이트-non-a-b-virtual-a-b-2016-2020
tags: []
aliases: []
date modified: 2026-07-31 15:42:50 +09:00
date created: 2026-07-31 15:38:23 +09:00
---

## 업데이트: Non-A/B → Virtual A/B (2016-2020)

상위 노트: [02-주요-기술-전환](01_inbox/mobile/android/00_foundations/history/android-evolution-history/02-%EC%A3%BC%EC%9A%94-%EA%B8%B0%EC%88%A0-%EC%A0%84%ED%99%98.md)

**Non-A/B** (~Android 6.x):

```
1. 업데이트 다운로드
2. Recovery 모드 재부팅
3. 설치 (10-20분, 사용 불가)
4. 재부팅
5. 완료
```

**A/B Seamless Update** (Android 7.0, 2016):

```
Slot A (현재 부팅)
  ├─ boot_a
  ├─ system_a
  └─ vendor_a

Slot B (업데이트 설치 중)
  ├─ boot_b   ← 백그라운드 다운로드
  ├─ system_b
  └─ vendor_b

재부팅 → Slot B 부팅 (빠름!)
실패 시 → Slot A 자동 롤백
```

**문제**: 2 배 저장 공간 필요

**Virtual A/B** (Android 11, 2020):

```
Slot A (실제 파티션)
Slot B (스냅샷, 변경된 부분만)
  → 공간 50% 절약
```
