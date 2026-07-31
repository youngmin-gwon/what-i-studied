# 구글 권장 성능 모니터링 및 추가 최적화 도구 (Google I/O 요약)

상위 노트: [baseline-profile-and-macrobenchmark](01_inbox/mobile/android/06_testing_performance/performance/baseline-profile-and-macrobenchmark.md)

Google I/O ("What's new in app performance") 세션에서 제시한 안드로이드 앱 성능 극대화를 위한 로드맵 및 핵심 도구 요약입니다.

### 6-1. JankStats를 이용한 실시간 UI 버벅임(Jank) 추적
로컬 개발 단계(Macrobenchmark)를 넘어, **실제 프로덕션 사용자 환경에서 일어나는 프레임 드랍(Jank)을 모니터링**하기 위해 Jetpack **JankStats** 라이브러리 도입을 권장합니다.
* **동작 원리**: 앱이 렌더링하는 매 프레임의 드로잉 성능을 모니터링하여, 프레임이 일정 기준(예: 16ms / 60Hz, 8.3ms / 120Hz)을 초과할 때 리스너를 호출합니다.
* **사용자 상태 바인딩(Context)**: 버벅임이 발생했을 때 단순히 "버벅였다"는 사실만 수집하는 것이 아니라, 사용자가 현재 어떤 화면을 스크롤 중이었는지, 어떤 Composable이 활성화되어 있었는지의 **UI 상태 정보(State)**를 결합하여 Firebase Performance Monitoring이나 분석 도구로 원격 전송할 수 있습니다.

### 6-2. App Startup 라이브러리를 통한 초기화 시간 단축
여러 오픈소스 및 타사 라이브러리(SDK)들이 앱 실행 단계에서 각각 `ContentProvider` 등을 사용해 개별적으로 초기화를 시도하면 Startup 타임에 큰 오버헤드가 발생합니다.
* **App Startup**을 활용하면 단일 Content Provider 내부에서 모든 종속 라이브러리의 초기화 순서를 결합하여 지연 실행(Lazy Initialization) 및 순차 실행 처리를 단순화하고 시작 속도를 더욱 개선할 수 있습니다.

### 6-3. 프로덕션 최적화 모니터링 루프
구글은 다음과 같은 순환 구조(Performance Loop)를 구축할 것을 권장합니다.
1. **모니터링**: Play Console (Android Vitals) 및 실서비스 **JankStats**를 통해 프레임 저하 및 ANR 유발 요소 상시 분석.
2. **현지화 및 재현**: **Macrobenchmark** 테스트 코드로 의심되는 시나리오(스크롤, 시작 등)를 작성하여 로컬에서 문제를 재현하고 성능 캡처.
3. **최적화 구현**: 비효율적인 Layout 및 Composable 재설계, 무거운 초기화 라이브러리 지연 처리(App Startup), 그리고 최종 배포 전 **Baseline Profile** 업데이트.
