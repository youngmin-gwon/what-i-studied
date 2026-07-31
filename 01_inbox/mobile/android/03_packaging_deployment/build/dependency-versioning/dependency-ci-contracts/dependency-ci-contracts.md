# 의존성, 버전, CI 계약

이 지도는 dependency resolution, version catalog, Compose BOM/compiler, KSP/kapt, serialization, CI 게이트를 변경 관리 단위로 나눈다.

## 정본 노트
- [Gradle 의존성 관리는 요청 버전이 아니라 해석 그래프를 관리한다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/gradle-dependency-management-controls-resolution-graph-not-requested-versions.md)
- [Version Catalog는 의존성 좌표와 플러그인 좌표의 이름표다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/version-catalog-names-dependency-and-plugin-coordinates.md)
- [Compose BOM은 Compose 라이브러리 버전 집합을 관리한다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/compose-bom-manages-compose-library-version-set.md)
- [Compose compiler는 BOM이 아니라 Kotlin compiler 흐름에 속한다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/compose-compiler-belongs-to-kotlin-compiler-flow-not-bom.md)
- [KSP는 Kotlin-first 코드 생성이고 kapt는 유지보수 모드다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/ksp-is-kotlin-first-code-generation-and-kapt-is-maintenance-mode.md)
- [kotlinx serialization은 컴파일러 플러그인과 런타임 포맷을 함께 요구한다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/kotlinx-serialization-requires-compiler-plugin-and-runtime-format.md)
- [Android CI/CD 게이트는 빠른 검증과 릴리스 검증을 분리한다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/android-cicd-gates-separate-fast-validation-and-release-validation.md)
- [의존성 변경 체크리스트는 그래프, ABI, 테스트, 배포 위험을 함께 본다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/dependency-change-checklist-reviews-graph-abi-tests-and-release-risk.md)
