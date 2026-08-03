---
title: constructor-injection-is-default-binding-path
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 18:09:22 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Constructor injection 은 기본 binding 경로다

DI graph 에 타입을 넣는 기본 방법은 constructor injection 이다. 생성자에 필요한 dependency 가 드러나면 graph 는 타입 간 연결을 정적으로 추적할 수 있고, 테스트에서도 생성자가 요구하는 협력 객체가 명확해진다.

`@Provides` 나 factory 가 먼저 떠오른다면 그 타입을 직접 소유하지 않는지, 런타임 값이 필요한지, interface binding 이 빠진 것은 아닌지 확인한다. 소유한 일반 클래스는 constructor injection 으로 시작하는 편이 가장 단순하다.

공식 문서: [Dependency injection in Android](https://developer.android.com/training/dependency-injection)

### 판단 기준

DI 노트는 객체를 어디서 만들고, 누가 소유하며, 어떤 lifetime 동안 재사용할지를 판단하는 기준으로 읽는다.

### 경계

framework 이름보다 graph boundary, scope, replacement seam, Android component lifetime 을 먼저 확인한다.
