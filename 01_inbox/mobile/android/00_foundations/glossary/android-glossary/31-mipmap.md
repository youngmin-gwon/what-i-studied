---
title: "Mipmap"
tags: ["android", "android/glossary"]
aliases: ["mipmap resource", "launcher icon resource"]
---

# Mipmap

정의: Mipmap은 Android resource qualifier 체계에서 density별 launcher icon과 일부 scaled bitmap resource를 제공할 때 쓰는 resource bucket이다.

혼동 방지: Mipmap은 일반 drawable 최적화의 동의어가 아니다. launcher icon처럼 launcher가 density별 asset을 선택해야 하는 resource와, app 내부 drawable/resource shrinking 문제를 구분해야 한다.

정본 링크:
- [Resource shrinking contract](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/resource-shrinking-removes-unused-resources-after-code-shrinking.md)
- [Resource source-set priority](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/source-set-priority-decides-variant-code-and-resource-conflicts.md)
