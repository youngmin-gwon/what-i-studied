# 🔍 2. 빌드 프로파일링 & 분석 (Build Scanning)

어떤 태스크가 시간을 가장 많이 잡아먹는지 확인하는 것이 최적화의 첫걸음입니다.

- **Build Scan**: `./gradlew assembleDebug --scan`
  - Gradle Enterprise 또는 클라우드 리포트를 통해 태스크 종속성, 네트워크 지연, 캐시 미스 이유를 시각적으로 확인.
- **Profile Report**: `./gradlew assembleDebug --profile`
  - `build/reports/profile` 에 로컬 HTML 리포트 생성.

---
