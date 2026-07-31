# Baseline Profile & Macrobenchmark 성능 최적화 가이드

이 문서는 앱의 시작 속도(Startup Time)를 개선하고 화면 전환 시의 프레임 저하(Jank)를 차단하기 위해 **Baseline Profile**과 **Jetpack Macrobenchmark**를 적용하는 방법과 관리 프로세스를 정리합니다. 

본 문서는 Google의 [Baseline Profile 가이드라인](https://developer.android.com/topic/performance/baselineprofiles) 및 최신 Gradle 플러그인 연동 규격을 반영하여 작성되었습니다.

---

---

## 원자 노트

- [[01-성능-최적화-동작-원리-baseline-profile-macrobenchmark-cloud-profile|성능 최적화 동작 원리 (Baseline Profile, Macrobenchmark & Cloud Profile)]]
- [[02-version-catalog-libs-versions-toml-설정|Version Catalog (`libs.versions.toml`) 설정]]
- [[03-모듈별-빌드-파일-build-gradle-kts-설정|모듈별 빌드 파일 (`build.gradle.kts`) 설정]]
- [[04-최적화-및-벤치마크-코드-구현|최적화 및 벤치마크 코드 구현]]
- [[05-실무-운영-및-ci-cd-관리-가이드|실무 운영 및 CI/CD 관리 가이드]]
- [[06-구글-권장-성능-모니터링-및-추가-최적화-도구-google-i-o-요약|구글 권장 성능 모니터링 및 추가 최적화 도구 (Google I/O 요약)]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
