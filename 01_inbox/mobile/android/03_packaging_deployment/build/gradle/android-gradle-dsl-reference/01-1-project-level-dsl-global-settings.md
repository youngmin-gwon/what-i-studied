---
title: 01-1-project-level-dsl-global-settings
tags: []
aliases: []
date modified: 2026-07-31 17:38:16 +09:00
date created: 2026-07-31 16:26:40 +09:00
---

## 🧩 1. Project-level DSL (Global Settings)

```kotlin
// root build.gradle.kts
plugins {
    alias(libs.plugins.android.application) apply false
    alias(libs.plugins.kotlin.android) apply false
}
```
