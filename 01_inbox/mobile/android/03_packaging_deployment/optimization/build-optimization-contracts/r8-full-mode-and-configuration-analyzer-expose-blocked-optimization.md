# R8 Full Mode와 Configuration Analyzer는 막힌 최적화를 드러낸다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [R8와 Gradle 빌드 최적화 계약](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/build-optimization-contracts.md)
관련 노트: [R8 keep 규칙은 최적화 경계다](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/keep-rules-are-optimization-boundaries.md), [R8 결과물은 크기와 런타임 회귀로 검증한다](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/r8-output-must-be-validated-with-size-and-runtime-regression.md)

## 핵심 주장

R8 Full Mode는 호환성 중심 모드보다 더 적극적인 최적화를 허용한다.

AGP 버전에 따라 기본값과 플래그가 달라질 수 있으므로 프로젝트의 실제 버전을 기준으로 확인한다.

오래된 `android.enableR8.fullMode=false` 설정을 무심코 유지하면 최신 최적화 경로를 막을 수 있다.

## Full Mode를 사용할 때의 전제

- 리플렉션 진입점이 명시적인 keep 계약을 가진다.
- 직렬화 모델의 필드와 생성자 계약을 테스트한다.
- JNI 이름 연결과 네이티브 등록 코드를 검증한다.
- 릴리즈 mapping 파일을 배포 버전과 함께 보관한다.
- 실패 시 규칙을 넓히기보다 원인을 먼저 좁힌다.

Full Mode 자체가 런타임 오류를 만드는 것이 아니라, 숨은 동적 계약을 드러내는 경우가 많다.

## Configuration Analyzer의 목적

Configuration Analyzer는 최종 R8 설정이 어디서 왔는지 추적하는 데 사용한다.

앱 규칙, 라이브러리 consumer rule, 기본 규칙이 합쳐진 결과를 사람이 추측하지 않게 해 준다.

특정 keep 규칙이 너무 넓은지, 어떤 라이브러리가 예외를 추가했는지 확인할 수 있다.

분석 순서는 다음과 같다.

1. 재현 가능한 릴리즈 variant를 만든다.
2. 최종 configuration과 관련 분석 리포트를 수집한다.
3. 넓은 keep, 중복 규칙, 오래된 예외를 찾는다.
4. 규칙의 소유 모듈과 런타임 계약을 확인한다.
5. 규칙을 줄인 뒤 결과와 테스트를 비교한다.

## Full Mode 전환 체크리스트

- AGP와 Gradle 버전을 고정하고 변경 이력을 남긴다.
- 기존 릴리즈 APK의 시작과 핵심 흐름을 기준선으로 저장한다.
- `mapping.txt`, `seeds.txt`, `usage.txt`, `configuration.txt`를 비교한다.
- 난독화 후에도 외부 API와 딥링크가 동작하는지 확인한다.
- 오류가 나면 전체 패키지 keep으로 되돌아가지 않는다.

Configuration Analyzer 결과는 최종 설정을 설명하는 증거이지, 테스트를 대체하지 않는다.

참고: [R8 Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer)
