# Gradle 프로젝트 설정 (`app/build.gradle.kts`)

프로젝트의 `release` 빌드 타입에서 R8 수축 및 최적화가 정상 동작하도록 설정합니다.

```kotlin
android {
    buildTypes {
        release {
            optimization {
                enable = true
                // 코드 수축 및 난독화 활성화
                isMinifyEnabled = true
                // 미사용 리소스 제거 (용량 최적화)
                isShrinkResources = true
            }
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
}
```

> [!IMPORTANT]
> `proguard-android-optimize.txt`는 구글이 검증한 최적화 알고리즘이 적용된 ProGuard 기본 파일이므로, 최적화가 없는 일반 `proguard-android.txt` 대신 반드시 `-optimize` 버전 기본 프로필을 사용하는 것을 권장합니다.

---
