---
title: binds-connects-interface-to-implementation-without-construction-code
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 18:09:19 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Binds 는 interface 와 implementation 을 연결하고 생성 코드는 추가하지 않는다

Interface 를 dependency 로 받으면 graph 는 어떤 implementation 을 넣어야 하는지 알아야 한다. `@Binds` 계열 binding 은 이미 constructor injection 으로 만들 수 있는 implementation 을 interface 타입으로 노출하는 선언이다.

생성 로직이 필요하면 provider 가 맞고, 단순히 `SessionStorage -> DataStoreSessionStorage` 처럼 타입 관계를 알려주는 일이라면 binds 가 맞다. 이 구분을 지키면 module 이 불필요한 factory 코드로 커지지 않는다.

### 판단 기준

DI 노트는 객체를 어디서 만들고, 누가 소유하며, 어떤 lifetime 동안 재사용할지를 판단하는 기준으로 읽는다.

### 경계

framework 이름보다 graph boundary, scope, replacement seam, Android component lifetime 을 먼저 확인한다.
