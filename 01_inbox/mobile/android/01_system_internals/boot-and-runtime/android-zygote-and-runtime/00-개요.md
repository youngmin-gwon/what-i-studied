# android zygote and runtime 개요

---
title: android-zygote-and-runtime
tags: [android, art, dalvik, initialization, internals, zygote]
aliases: [ART, Dalvik, Zygote]
date modified: 2026-07-31 15:23:03 +09:00
date created: 2025-12-16 15:22:42 +09:00
---

## Zygote & Runtime: The Birth of an App

앱 아이콘을 터치하는 순간, 0.1 초 만에 앱이 뜹니다.

리눅스에서 Java 가상머신(JVM) 하나 띄우는 데 1 초가 넘게 걸리는 걸 생각하면 마법 같은 속도입니다.

그 비밀은 **Zygote ("수정란")**에 있습니다.
