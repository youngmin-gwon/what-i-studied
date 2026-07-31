# 💡 3. Version Catalog (libs.versions.toml)

최근에는 하드코딩 대신 `libs` 접근자를 사용하는 것이 표준입니다.

```toml
[versions]
agp = "8.7.0"
kotlin = "2.0.21"

[libraries]
androidx-core-ktx = { group = "androidx.core", name = "core-ktx", version.ref = "core-ktx" }

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
```

---
