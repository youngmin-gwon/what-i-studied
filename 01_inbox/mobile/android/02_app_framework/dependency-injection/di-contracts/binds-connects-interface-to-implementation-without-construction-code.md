---
title: "Binds는 interface와 implementation을 연결하고 생성 코드는 추가하지 않는다"
tags: ["android", "android/app-framework"]
---

# Binds는 interface와 implementation을 연결하고 생성 코드는 추가하지 않는다

Interface를 dependency로 받으면 graph는 어떤 implementation을 넣어야 하는지 알아야 한다. `@Binds` 계열 binding은 이미 constructor injection으로 만들 수 있는 implementation을 interface 타입으로 노출하는 선언이다.

생성 로직이 필요하면 provider가 맞고, 단순히 `SessionStorage -> DataStoreSessionStorage`처럼 타입 관계를 알려주는 일이라면 binds가 맞다. 이 구분을 지키면 module이 불필요한 factory 코드로 커지지 않는다.

## 판단 기준

DI 노트는 객체를 어디서 만들고, 누가 소유하며, 어떤 lifetime 동안 재사용할지를 판단하는 기준으로 읽는다.

## 경계

framework 이름보다 graph boundary, scope, replacement seam, Android component lifetime을 먼저 확인한다.
