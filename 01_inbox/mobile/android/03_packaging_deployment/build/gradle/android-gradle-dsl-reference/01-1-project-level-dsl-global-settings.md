# 🧩 1. Project-level DSL (Global Settings)

```kotlin
// root build.gradle.kts
plugins {
    alias(libs.plugins.android.application) apply false
    alias(libs.plugins.kotlin.android) apply false
}
```

---
