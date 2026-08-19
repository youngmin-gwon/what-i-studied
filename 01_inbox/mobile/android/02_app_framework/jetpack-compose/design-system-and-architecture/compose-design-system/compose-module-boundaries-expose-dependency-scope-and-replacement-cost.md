---
title: compose-module-boundaries-expose-dependency-scope-and-replacement-cost
tags: [android, compose/design-system, jetpack-compose]
aliases: [Compose modules]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## Compose 모듈 경계는 의존성 범위와 교체 비용을 노출한다

Compose artifact 와 package 경계는 어떤 계층에 의존하는지 보여주는 단서다. 앱 design system 은 Material 3 위에서 token 을 적용할 수도 있고, Foundation/UI 위에서 자체 component 를 만들 수도 있다.

모듈을 작게 가져가면 필요한 기능만 의존할 수 있지만, 상위 component 가 제공하던 기본 동작을 직접 책임질 가능성이 커진다. dependency 를 줄이는 결정과 구현 책임은 함께 움직인다.

예를 들어 `androidx.compose.material3:material3` 는 `androidx.compose.foundation:foundation` 과 `androidx.compose.ui:ui` 위에 있다. Material 3 대신 Foundation 까지만 의존하면 Material component 와 token 시스템을 잃는 대신 결합도와 apk 크기를 줄일 수 있다.

정확한 artifact 이름과 내부 구성은 Compose 버전에 따라 달라질 수 있다. 일반 정본에는 계층 사고만 두고, 프로젝트 dependency version 과 build 설정은 별도 build 문서에서 확인한다.

관련 노트: [Compose는 상위 컴포넌트가 맞지 않을 때 낮은 계층으로 내려갈 수 있게 설계됐다](./compose-layers-let-you-drop-down-when-higher-level-components-do-not-fit.md), [Gradle build contracts](../../../../03_packaging_deployment/build/gradle/gradle-build/gradle-build.md)

출처: [Compose architectural layering](https://developer.android.com/develop/ui/compose/layering)
