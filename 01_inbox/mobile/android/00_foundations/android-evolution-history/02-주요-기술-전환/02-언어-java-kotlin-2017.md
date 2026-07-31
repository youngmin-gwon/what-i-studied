---
title: 02-언어-java-kotlin-2017
tags: []
aliases: []
date modified: 2026-07-31 15:40:04 +09:00
date created: 2026-07-31 15:38:23 +09:00
---

## 언어: Java → Kotlin (2017+)

상위 노트: [[02-주요-기술-전환]]

**배경**:

- Java 6 (2008-2014): 람다 없음, verbose
- Oracle vs Google 소송 (2010-2021)

**Kotlin 공식 지원** (Google I/O 2017):

```kotlin
// Java (verbose)
button.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        // ...
    }
});

// Kotlin (concise)
button.setOnClickListener {
    // ...
}
```

**현재 상태** (2023):

- Google 공식 권장: Kotlin-first
- 신규 Jetpack 라이브러리: Kotlin 우선 설계
- Coroutine 으로 비동기 처리 간소화
