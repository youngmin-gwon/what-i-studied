# Baseline Profile & Macrobenchmark 성능 최적화 가이드

이 문서는 앱의 시작 속도(Startup Time)를 개선하고 화면 전환 시의 프레임 저하(Jank)를 차단하기 위해 **Baseline Profile**과 **Jetpack Macrobenchmark**를 적용하는 방법과 관리 프로세스를 정리합니다. 

본 문서는 Google의 [Baseline Profile 가이드라인](https://developer.android.com/topic/performance/baselineprofiles) 및 최신 Gradle 플러그인 연동 규격을 반영하여 작성되었습니다.

---

---

## 원자 노트

- [성능 최적화 동작 원리 (Baseline Profile, Macrobenchmark & Cloud Profile)](01_inbox/mobile/android/06_testing_performance/performance/baseline-profile-and-macrobenchmark/01-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94-%EB%8F%99%EC%9E%91-%EC%9B%90%EB%A6%AC-baseline-profile-macrobenchmark-cloud-profile.md)
- [Version Catalog (`libs.versions.toml`) 설정](01_inbox/mobile/android/06_testing_performance/performance/baseline-profile-and-macrobenchmark/02-version-catalog-libs-versions-toml-%EC%84%A4%EC%A0%95.md)
- [모듈별 빌드 파일 (`build.gradle.kts`) 설정](01_inbox/mobile/android/06_testing_performance/performance/baseline-profile-and-macrobenchmark/03-%EB%AA%A8%EB%93%88%EB%B3%84-%EB%B9%8C%EB%93%9C-%ED%8C%8C%EC%9D%BC-build-gradle-kts-%EC%84%A4%EC%A0%95.md)
- [최적화 및 벤치마크 코드 구현](01_inbox/mobile/android/06_testing_performance/performance/baseline-profile-and-macrobenchmark/04-%EC%B5%9C%EC%A0%81%ED%99%94-%EB%B0%8F-%EB%B2%A4%EC%B9%98%EB%A7%88%ED%81%AC-%EC%BD%94%EB%93%9C-%EA%B5%AC%ED%98%84.md)
- [실무 운영 및 CI/CD 관리 가이드](01_inbox/mobile/android/06_testing_performance/performance/baseline-profile-and-macrobenchmark/05-%EC%8B%A4%EB%AC%B4-%EC%9A%B4%EC%98%81-%EB%B0%8F-ci-cd-%EA%B4%80%EB%A6%AC-%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- [구글 권장 성능 모니터링 및 추가 최적화 도구 (Google I/O 요약)](01_inbox/mobile/android/06_testing_performance/performance/baseline-profile-and-macrobenchmark/06-%EA%B5%AC%EA%B8%80-%EA%B6%8C%EC%9E%A5-%EC%84%B1%EB%8A%A5-%EB%AA%A8%EB%8B%88%ED%84%B0%EB%A7%81-%EB%B0%8F-%EC%B6%94%EA%B0%80-%EC%B5%9C%EC%A0%81%ED%99%94-%EB%8F%84%EA%B5%AC-google-i-o-%EC%9A%94%EC%95%BD.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
