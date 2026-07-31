# 성능 최적화 동작 원리 (Baseline Profile, Macrobenchmark & Cloud Profile)

상위 노트: [baseline-profile-and-macrobenchmark](01_inbox/mobile/android/06_testing_performance/performance/baseline-profile-and-macrobenchmark.md)

### 1-1. Baseline Profile 이란?
안드로이드 앱이 실행될 때 ART(Android Runtime)는 JIT(Just-In-Time) 컴파일과 인터프리터를 통해 기계어로 코드를 해석합니다. 이 과정에서 최초 앱 구동 시 CPU 부하가 집중되어 성능이 저하될 수 있습니다.
* **Baseline Profile**은 앱 내의 **자주 실행되는 주요 코드 경로(Hot Paths)**를 파일 형태(`baseline-prof.txt`)로 기록하여 배포 패키지(AAB/APK)에 동반시키는 기술입니다.
* 사용자가 Google Play 스토어에서 앱을 다운로드 및 설치할 때, 스토어 인스톨러가 프로필 데이터를 보고 최적화 대상을 파악하여 **미리 AOT(Ahead-Of-Time) 컴파일**을 완료합니다.
* 이를 통해 첫 실행(Cold Start) 속도가 최대 30~40% 이상 빨라지고 가시적인 프레임 버벅임이 대폭 줄어듭니다.

### 1-2. Cloud Profile과의 상호 보완 관계 (배포 시 운영 가이드)
Google Play 콘솔은 앱 배포 이후 실제 사용자들의 사용 데이터를 익명으로 수집(JIT 프로필 수집)하여 **Cloud Profile**을 자동으로 생성합니다.
* **Cloud Profile의 특징**: 개발자가 별도의 코드를 작성하거나 수동으로 추출하여 파일로 관리할 필요가 없으며, Google Play 서비스가 배포 완료 후 백그라운드에서 자동으로 관리하고 병합(Merge)합니다.
* **상호 보완 필요성 (Cold Start / Day 1 문제)**:
  * 신규 버전이 배포된 직후(Day 1)에는 아직 사용자가 사용한 데이터가 없어 **Cloud Profile이 존재하지 않는 공백기**가 생깁니다. 이 시기에는 최적화 가이드가 없어 사용자들이 앱이 버벅인다고 느낄 수 있습니다.
  * 개발자가 배포 시점에 **Baseline Profile**을 함께 패키징해 배포하면, Cloud Profile이 아직 생성되지 않은 버전 출시 극초기에도 **첫 다운로드 즉시 강력한 최적화 성능을 확보**할 수 있습니다.
  * 시간이 흐른 뒤 유저 데이터가 누적되면 Google Play가 [Baseline Profile] + [Cloud Profile]을 결합하여 더욱 정교한 최적화 맵으로 자동 갱신해 다운로드 처리를 돕습니다.
* **배포 관리 프로세스**:
  * 매 개발 빌드마다 재생성할 필요는 없으며, **운영 서버 배포(Production Release) 직전에만 1회 생성**하여 업데이트된 `baseline-prof.txt` 파일을 Git에 올려 배포 본체에 반영하는 사이클로 운영하면 번거로움을 최소화할 수 있습니다.

### 1-3. Macrobenchmark의 역할
* 벤치마크 테스트 코드를 통해 앱의 실제 성능 변화를 밀리초(ms) 단위의 리포트 및 성능 추적 파일(Trace)로 출력합니다.
* Baseline Profile이 있을 때와 없을 때(`CompilationMode.None` vs `CompilationMode.Partial`)의 속도 지표를 객관적으로 측정 및 검증하는 역할을 수행합니다.

---
