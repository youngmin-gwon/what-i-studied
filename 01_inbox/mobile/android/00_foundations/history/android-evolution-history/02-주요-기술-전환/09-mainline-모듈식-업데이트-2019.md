---
title: 09-mainline-모듈식-업데이트-2019
tags: []
aliases: []
date modified: 2026-07-31 15:42:36 +09:00
date created: 2026-07-31 15:38:23 +09:00
---

## Mainline: 모듈식 업데이트 (2019)

상위 노트: [[02-주요-기술-전환]]

**문제**:

- 보안 패치도 OEM 업데이트 대기
- 중요 버그 수정 느림

**Mainline Modules** (Android 10):

```
com.android.media            # MediaCodec
com.android.wifi             # Wi-Fi 스택
com.android.tethering        # 테더링
com.android.conscrypt        # TLS/SSL

→ Google Play 통해 독립 업데이트
```

**APEX (Android Pony EXpress)**:

```
/apex/com.android.media/
  ├─ lib/
  ├─ bin/
  └─ apex_manifest.json
```

**효과**:

- 월별 보안 패치 → 주간 업데이트 가능
- OEM 무관하게 수정
