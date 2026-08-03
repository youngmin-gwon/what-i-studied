---
title: 31-mipmap
tags: ["android", "android/glossary"]
aliases: ["launcher icon resource", "mipmap resource"]
date modified: 2026-08-03 17:21:26 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## Mipmap 은 기기의 디스플레이 밀도에 맞춰 최적화된 런처 아이콘을 제공하는 리소스 폴더다

정의: Mipmap 은 Android resource qualifier 체계에서 density 별 launcher icon 과 일부 scaled bitmap resource 를 제공할 때 쓰는 resource bucket 이다.

혼동 방지: Mipmap 은 일반 drawable 최적화의 동의어가 아니다. launcher icon 처럼 launcher 가 density 별 asset 을 선택해야 하는 resource 와, app 내부 drawable/resource shrinking 문제를 구분해야 한다.

정본 링크:

- [Resource shrinking contract](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/resource-shrinking-removes-unused-resources-after-code-shrinking.md)
- [Resource source-set priority](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/source-set-priority-decides-variant-code-and-resource-conflicts.md)
