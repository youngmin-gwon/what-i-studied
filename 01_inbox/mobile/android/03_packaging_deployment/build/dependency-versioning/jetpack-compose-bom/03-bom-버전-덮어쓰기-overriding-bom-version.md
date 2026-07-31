# BOM 버전 덮어쓰기 (Overriding BOM version)

앱 개발 중 특정 기능 사용이나 긴급 버그 픽스를 위해 **특정 컴포즈 라이브러리 하나만 최신 알파/베타 버전**으로 올려야 할 때가 있습니다. 이때는 BOM 설정을 유지한 채 원하는 라이브러리에 명시적으로 버전을 입력하면 됩니다.

```kotlin
dependencies {
    implementation(platform(libs.androidx.compose.bom)) // 기본 2026.06.01 (예: ui 1.8.0)

    // UI 모듈만 최신 1.9.0-alpha01 버전을 강제 사용하도록 재정의
    implementation("androidx.compose.ui:ui:1.9.0-alpha01")
    
    // 나머지 foundation, material3 등은 여전히 BOM에 정의된 안정 버전을 따름
    implementation(libs.androidx.compose.foundation)
}
```

---
