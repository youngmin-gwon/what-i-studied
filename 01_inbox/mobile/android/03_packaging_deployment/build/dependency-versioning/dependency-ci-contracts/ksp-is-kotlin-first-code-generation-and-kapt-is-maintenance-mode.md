---
title: ksp-is-kotlin-first-code-generation-and-kapt-is-maintenance-mode
tags: ["android", "android/packaging-deployment"]
aliases: []
date modified: 2026-08-03 18:12:26 +09:00
date created: 2026-07-31 17:52:17 +09:00
---

## KSP 는 Kotlin-first 코드 생성이고 kapt 는 유지보수 모드다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)

관련 지도: [의존성, 버전, CI 계약](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/dependency-ci-contracts.md)

관련 노트: [kotlinx serialization은 컴파일러 플러그인과 런타임 포맷을 함께 요구한다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/kotlinx-serialization-requires-compiler-plugin-and-runtime-format.md), [Compose compiler는 BOM이 아니라 Kotlin compiler 흐름에 속한다](01_inbox/mobile/android/03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/compose-compiler-belongs-to-kotlin-compiler-flow-not-bom.md)

### KAPT

KAPT 는 Kotlin 코드에 Java annotation processor 를 연결하기 위한 호환 계층이다.

일반적으로 Kotlin 소스를 Java stub 형태로 준비한 뒤 기존 Java processor 를 실행한다.

이 과정의 비용과 제약 때문에 새 도구가 KSP 를 지원한다면 마이그레이션을 검토할 수 있다.

다만 processor 가 KAPT 만 지원한다면 무리하게 교체하지 말고 해당 라이브러리의 공식 지원 범위를 따른다.

```kotlin
plugins {
    kotlin("kapt")
}

dependencies {
    kapt("group:processor:version")
}
```

### KSP

KSP 는 Kotlin 프로그램의 심볼을 분석해 생성 소스 코드를 만드는 API 다.

Kotlin 의 선언과 타입을 이해하는 장점이 있지만 모든 문장·표현식을 분석하거나 기존 소스를 직접 수정하지는 않는다.

따라서 KSP processor 는 생성할 코드와 입력 소스의 계약이 명확해야 한다.

```kotlin
plugins {
    id("com.google.devtools.ksp")
}

dependencies {
    ksp("group:processor:version")
}
```

KSP 가 항상 특정 배수만큼 빠르다고 일반화하지 않는다.

프로젝트 크기, processor, 증분 처리, 캐시 상태에 따라 결과가 달라지므로 CI 에서 실제 시간을 측정한다.

### 컴파일러 플러그인

컴파일러 플러그인은 Kotlin 컴파일 과정에 연결되어 코드 생성이나 컴파일 동작을 확장한다.

Serialization 과 Compose compiler 는 이 범주의 예다.

KSP 로 해결되지 않는 언어 의미 변경이 필요할 때도 custom compiler plugin 은 유지 비용이 크므로 마지막 수단으로 둔다.

### 선택 기준

- Java processor 를 반드시 써야 하면 KAPT 를 유지한다.
- 지원되는 processor 가 Kotlin 심볼 분석과 소스 생성을 요구하면 KSP 를 검토한다.
- 컴파일러 단계 통합이 공식 제공되는 기능은 해당 plugin 을 적용한다.
- `implementation`, `kapt`, `ksp`, `plugins` 를 서로 대체 개념으로 보지 않는다.

공식 기준은 [KSP 개요](https://kotlinlang.org/docs/ksp-overview.html) 와

[Kotlin compiler plugins](https://kotlinlang.org/docs/compiler-plugins-overview.html) 이다.
