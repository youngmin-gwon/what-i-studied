# Profile-Guided R8 최적화 및 Android Studio 툴링연동

R8 컴파일러는 단순히 정적 분석으로만 코드를 자르는 것을 넘어, **Baseline Profile 및 Startup Profile 지도를 입력받아 실행 최적화를 극대화**합니다.

### 7-1. Baseline Profile & Startup Profile과 R8의 시너지 (Profile-Guided Optimization)
* R8은 Baseline Profile(`baseline-prof.txt`) 및 Startup Profile(`startup-prof.txt`)에 기록된 코드 경로를 기반으로:
  1. **Startup Hot Path 메서드의 인라이닝 우선순위 결정**: 시작 단계에서 호출되는 메서드를 더 적극적으로 호출부에 Direct Inlining시킵니다.
  2. **DEX Layout 최적화 (Dex Layout Reordering / DEX Layout Optimization)**: 핫 코드를 DEX 파일의 첫 번째 페이지(First Page)로 모아 배치함으로써, 앱 구동 시 OS가 메모리 페이지를 가져오는 디스크 I/O 횟수와 Page Fault 오버헤드를 최소화합니다.

### 7-2. APK Analyzer를 활용한 R8 검증
Android Studio의 **APK Analyzer** (`Build > Analyze APK...`)를 활용하면:
* R8 적용 전후의 DEX 메서드 수(DEX count) 변화 추이 확인.
* 특정 패키지 및 라이브러리가 R8에 의해 얼마나 줄어들었는지 바이트 단위로 실시간 확인 및 검증할 수 있습니다.

---
