# BOM을 사용한 의존성 설정 방법

Version Catalog(`libs.versions.toml`)와 Gradle 스크립트를 사용하여 BOM을 설정하면 개별 Compose 라이브러리의 버전 선언을 모두 생략할 수 있습니다.

### 2-1. `libs.versions.toml` 등록
BOM 버전을 관리할 뼈대를 추가합니다.
```toml
[versions]
composeBom = "2026.06.01"

[libraries]
androidx-compose-bom = { group = "androidx.compose", name = "compose-bom", version.ref = "composeBom" }
androidx-compose-ui = { group = "androidx.compose.ui", name = "ui" } # 버전 생략
androidx-compose-material3 = { group = "androidx.compose.material3", name = "material3" } # 버전 생략
```

### 2-2. `build.gradle.kts` 반영
의존성 블록 내에 `platform(...)` 키워드를 사용해 BOM 라이브러리를 가져온 후, 나머지 라이브러리들은 별칭(alias)으로 버전 없이 선언합니다.
```kotlin
dependencies {
    // 1. BOM 플랫폼 선언 (이 시점에 호환 버전 목록이 내부 로드됨)
    implementation(platform(libs.androidx.compose.bom))

    // 2. 하위 라이브러리 선언 (버전 번호 기입 불필요)
    implementation(libs.androidx.compose.ui)
    implementation(libs.androidx.compose.material3)
}
```

---
