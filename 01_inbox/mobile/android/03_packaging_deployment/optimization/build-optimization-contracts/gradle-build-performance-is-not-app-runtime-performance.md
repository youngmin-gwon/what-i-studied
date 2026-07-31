---
title: "Gradle 빌드 성능은 앱 런타임 성능과 다르다"
tags: ["android", "android/packaging-deployment"]
---

# Gradle 빌드 성능은 앱 런타임 성능과 다르다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [R8와 Gradle 빌드 최적화 계약](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/build-optimization-contracts.md)
관련 노트: [증분 빌드, 캐시, 구성 캐시는 빌드 작업량을 줄인다](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/incremental-build-cache-and-configuration-cache-reduce-build-work.md), [Gradle 빌드 계약](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/gradle-build-contracts.md)

## 핵심 주장

Gradle 빌드가 빠른 것과 앱이 빠르게 실행되는 것은 서로 다른 성능 문제다.

빌드 성능은 개발자 피드백 시간과 CI 처리량을 다룬다.

런타임 성능은 설치 후 시작, 프레임, 상호작용, 배터리와 메모리를 다룬다.

R8은 두 영역을 모두 건드릴 수 있지만 측정 방법과 원인은 다르다.

## Gradle 빌드의 네 단계

1. 초기화: settings와 포함된 빌드를 읽는다.
2. 구성: 플러그인과 빌드 스크립트를 평가한다.
3. 실행: 입력이 바뀐 태스크를 수행한다.
4. 산출물 처리: APK, AAB, 테스트 결과를 저장하거나 업로드한다.

Configuration Cache는 구성 단계의 결과를 재사용한다.

Incremental Build는 입력과 출력이 같은 태스크를 건너뛴다.

Build Cache는 동일한 입력을 가진 태스크의 출력을 재사용한다.

이 세 가지를 같은 캐시라고 부르면 병목 원인을 잘못 진단한다.

## 측정 방법

- `--profile`로 로컬 프로파일 리포트를 만든다.
- Build Scan으로 태스크 시간, 캐시 적중, 네트워크 지연을 확인한다.
- 동일한 작업을 warm build와 clean build로 나눠 측정한다.
- 개발 빌드, 테스트 빌드, 릴리즈 빌드를 별도 기준선으로 둔다.

릴리즈 R8 시간이 길다고 해서 앱 시작이 느리다는 결론을 내리지 않는다.

반대로 빌드가 빨라졌다고 런타임 최적화가 증명되는 것도 아니다.

## 설정 원칙

`org.gradle.configuration-cache=true`는 호환되지 않는 플러그인과 코드를 드러낼 수 있다.

`org.gradle.caching=true`는 반복 가능한 입력과 안정적인 출력이 있을 때 효과가 크다.

JVM 힙은 무조건 크게 잡지 말고 GC와 메모리 압박을 함께 측정한다.

병렬 실행은 프로젝트 의존성과 머신 코어 수를 고려해 적용한다.

참고: [Improve the performance of Gradle builds](https://docs.gradle.org/current/userguide/performance.html)

참고: [Gradle build cache](https://docs.gradle.org/current/userguide/build_cache.html)
