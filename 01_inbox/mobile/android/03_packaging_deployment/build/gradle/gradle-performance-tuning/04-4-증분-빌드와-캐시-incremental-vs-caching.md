# 🛡️ 4. 증분 빌드와 캐시 (Incremental vs Caching)

- **Incremental Build**: 이미 처리된 입력값은 건너뛰고 변경된 파일만 컴파일.
- **Configuration Cache**: `settings.gradle`, `build.gradle` 의 실행 결과를 캐싱하여 'Configuring' 단계를 생략. (Kotlin K2 컴파일러와 함께 최상의 궁합)
- **Remote Build Cache**: CI 환경과 로컬 팀원 간에 빌드 아티팩트를 공유하여 'Clean Build' 시간을 획기적으로 절약.

---
