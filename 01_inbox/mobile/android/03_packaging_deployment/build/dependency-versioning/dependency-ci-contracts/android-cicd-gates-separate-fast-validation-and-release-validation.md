# Android CI/CD 게이트는 빠른 검증과 릴리스 검증을 분리한다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [의존성, 버전, CI 계약](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/dependency-ci-contracts.md)
관련 노트: [의존성 변경 체크리스트는 그래프, ABI, 테스트, 배포 위험을 함께 본다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/dependency-change-checklist-reviews-graph-abi-tests-and-release-risk.md), [Play release checklist는 artifact, signing, track, rollback 조건을 고정한다](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/play-release-checklist-freezes-artifact-signing-track-and-rollback-conditions.md)

## 목적

CI는 모든 변경을 동일한 환경에서 검증하고, CD는 검증된 산출물을 정해진 채널로 배포하는 자동화다.
핵심은 도구 이름보다 어떤 조건이 다음 단계로 넘어가는지 명확히 하는 것이다.
실패를 숨기지 않고, 재현 가능한 Gradle 명령과 보안된 자격 증명을 사용한다.

## 권장 게이트

1. **검사**: 포맷, Android Lint, 정적 분석을 실행한다.
2. **단위 테스트**: 순수 Kotlin·도메인·ViewModel 테스트를 실행한다.
3. **컴파일 검증**: 필요한 debug variant를 컴파일한다.
4. **통합·UI 테스트**: 대표 기기와 핵심 흐름을 검증한다.
5. **릴리스 산출물**: 서명 전후의 APK 또는 AAB를 만든다.
6. **배포 승인**: 브랜치, 태그, 승인, 변경 범위를 확인한 뒤 배포한다.

각 단계는 앞 단계 성공을 조건으로 연결한다.
빠른 피드백이 필요한 PR에는 검사·단위 테스트를 먼저 두고, 비용이 큰 기기 테스트와 배포는 별도 job으로 분리할 수 있다.

## Gradle 실행

```bash
./gradlew --no-daemon --stacktrace check
./gradlew --no-daemon :app:assembleDebug
./gradlew --no-daemon :app:bundleRelease
```

실제 task 이름은 프로젝트의 모듈·variant에 맞춰 고정한다.
의존성 캐시는 빌드 재현성을 훼손하지 않는 범위에서 사용하고, 캐시 키에는 Gradle·JDK·lockfile 등 입력을 반영한다.

## 보안과 산출물

- keystore, 비밀번호, 배포 토큰은 CI secret 저장소에서 주입한다.
- 로그에 secret과 서명 파일 내용을 출력하지 않는다.
- PR 빌드에서는 운영 배포 권한을 부여하지 않는다.
- 릴리스 산출물의 versionName, versionCode, 서명, mapping 파일을 확인한다.
- 배포 job은 빌드가 다시 코드를 가져오지 않고 검증된 artifact를 사용한다.

## 실패 처리

실패한 게이트는 재시도만으로 통과시키지 말고 원인과 flaky 여부를 기록한다.
UI 테스트가 불안정하면 격리된 재시도 정책을 두되, 최종 상태는 실패로 남길 수 있어야 한다.
배포 뒤에는 설치, 시작, 핵심 경로, 크래시 모니터링을 확인한다.

CI 최적화는 먼저 병목을 측정한 뒤 Gradle 캐시·병렬화·작업 분할을 적용한다.
의존성 그래프와 빌드 task를 이해하려면 [Gradle 의존성 관리](https://docs.gradle.org/current/userguide/core_dependency_management.html)를 참조한다.
