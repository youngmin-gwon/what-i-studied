# R8 결과물은 크기와 런타임 회귀로 검증한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [R8와 Gradle 빌드 최적화 계약](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/build-optimization-contracts.md)
관련 노트: [R8 Full Mode와 Configuration Analyzer는 막힌 최적화를 드러낸다](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/r8-full-mode-and-configuration-analyzer-expose-blocked-optimization.md), [Play 릴리스 체크리스트는 산출물, 서명, 트랙, 롤백 조건을 고정한다](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/play-release-checklist-freezes-artifact-signing-track-and-rollback-conditions.md)

## 핵심 주장

R8 성공은 빌드가 끝났다는 뜻이지 앱 동작이 보존되었다는 뜻이 아니다.

결과 파일과 실제 설치 테스트를 함께 사용해야 수축, 최적화, 난독화의 효과와 부작용을 알 수 있다.

## 주요 결과 파일

- `mapping.txt`: 원래 이름과 난독화된 이름, 라인 번호의 대응표다.
- `seeds.txt`: keep 규칙으로 보존된 클래스와 멤버를 보여 준다.
- `usage.txt`: R8이 제거한 코드 목록을 보여 준다.
- `configuration.txt`: 병합된 최종 규칙을 확인하는 근거다.
- APK Analyzer: DEX, 리소스, 네이티브 라이브러리의 실제 패키징을 확인한다.

mapping 파일은 충돌 분석과 Crashlytics de-obfuscation에 필요한 배포 산출물이다.

버전별 mapping을 덮어쓰지 말고 앱 버전과 함께 보관한다.

## 실패 증상별 접근

`ClassNotFoundException`이면 동적 로딩 대상이 제거되었는지 먼저 본다.

`NoSuchMethodError`이면 메서드 시그니처 또는 생성자 계약이 바뀌었는지 확인한다.

직렬화 실패이면 모델 필드 이름, 애노테이션, 기본 생성자 보존 여부를 확인한다.

JNI 오류이면 네이티브 등록 이름과 난독화 예외를 대조한다.

리소스 오류이면 `usage.txt`가 아니라 리소스 수축 리포트와 동적 이름 경로를 조사한다.

## 최소 보정 루프

1. 릴리즈에서 오류를 재현한다.
2. stack trace를 mapping으로 복원한다.
3. 문제 심볼이 `usage.txt`에 있는지 확인한다.
4. 필요한 최소 단위에만 keep 또는 이름 보존을 추가한다.
5. 같은 테스트와 크기 측정을 반복한다.

보정 전후의 DEX 메서드 수와 다운로드 크기를 비교해 과도한 보존을 감시한다.

## CI 검증 항목

- 릴리즈 assemble 성공
- 대표 딥링크와 알림 진입
- 로그인, 결제, 직렬화, 이미지 로딩
- 난독화 stack trace 복원
- APK/AAB 크기 임계치
- mapping 업로드와 보관

참고: [Decode obfuscated stack traces](https://developer.android.com/studio/debug/stacktraces)

참고: [Analyze your build with APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer)
