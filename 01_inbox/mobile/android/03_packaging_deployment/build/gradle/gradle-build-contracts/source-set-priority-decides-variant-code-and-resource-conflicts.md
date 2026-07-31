---
title: "Source set 우선순위는 variant별 코드와 리소스 충돌을 결정한다"
tags: ["android", "android/packaging-deployment"]
---

# Source set 우선순위는 variant별 코드와 리소스 충돌을 결정한다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [Gradle 빌드 계약](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/gradle-build-contracts.md)
관련 노트: [Build type, product flavor, build variant는 서로 다른 축이다](01_inbox/mobile/android/03_packaging_deployment/build/gradle/gradle-build-contracts/build-type-product-flavor-and-build-variant-are-different-axes.md)

## Source set이란

Source set은 특정 빌드 대상에 함께 들어갈 Kotlin/Java 코드, 리소스, manifest의 묶음이다.
기본 `main`은 모든 변형의 공통 입력이고, `debug`, flavor, variant 전용 source set은 차이를 표현한다.

## 표준 디렉터리

```text
app/src/main/
app/src/debug/
app/src/release/
app/src/dev/
app/src/devDebug/
app/src/androidTest/
app/src/test/
```

`src/devDebug`는 해당 조합에만 필요한 구현을 담는다.
공통 코드와 리소스는 `main`에 두고, 변형별 차이만 더 구체적인 source set으로 내린다.

## 우선순위

일반적인 우선순위는 다음과 같다.

1. 조합 전용 variant source set
2. build type source set
3. flavor source set
4. `main` source set
5. 라이브러리 의존성

더 높은 우선순위의 리소스가 같은 이름의 낮은 우선순위 리소스를 대체한다.
Kotlin/Java 클래스는 같은 변형에 동일한 정규 이름이 두 번 포함되면 중복 클래스 오류가 난다.

## Manifest 병합

각 source set의 manifest는 변형 구성에 따라 병합된다.
manifest 값을 덮어써야 할 때는 병합 규칙과 `tools:replace` 같은 명시적 의도를 함께 검토한다.
파일이 어느 variant에 들어가는지는 directory 이름과 실제 선택 변형을 함께 확인한다.

## 명시적 경로 설정

표준 구조를 유지하는 것이 우선이며, 필요한 경우 `sourceSets` 블록으로 경로를 매핑할 수 있다.
경로를 바꾸면 IDE, 테스트, lint, CI의 기대 경로도 함께 점검해야 한다.

## 실무 점검

- 같은 클래스가 `main`과 변형 source set에 중복되지 않는가?
- flavor 조합 전용 파일이 예상 variant에만 포함되는가?
- 리소스 대체가 이름 충돌로 조용히 발생하지 않는가?
- 테스트 source set과 앱 source set의 역할이 분리되어 있는가?

## 참고

공식 source set 규칙: https://developer.android.com/build/build-variants
리소스 추가와 병합: https://developer.android.com/studio/write/add-resources
