# 외부 라이브러리 및 클래스를 위한 Stability Configuration File 활용
수정 권한이 없는 외부 라이브러리/SDK 클래스(예: Java Time API, Ktor 객체, Google Maps SDK 등)가 UI State에 포함될 경우, Compose 컴파일러는 이를 `Unstable`로 오인할 수 있습니다.

이를 해결하기 위해 프로젝트 루트에 `compose_compiler_config.conf` 파일 지정을 통해 명시적으로 Stable 지정을 수행합니다:

1. **`compose_compiler_config.conf` 설정**:
   ```text
   // Java Standard & Network / Time APIs
   java.time.Instant
   java.time.LocalDate
   java.time.LocalDateTime
   java.time.ZonedDateTime

   // Ktor & Network Models
   io.ktor.http.Url
   ```

2. **Compose를 사용하는 각 모듈의 `build.gradle.kts` 설정**:
   ```kotlin
   composeCompiler {
       stabilityConfigurationFiles.add(rootProject.layout.projectDirectory.file("compose_compiler_config.conf"))
   }
   ```

---
