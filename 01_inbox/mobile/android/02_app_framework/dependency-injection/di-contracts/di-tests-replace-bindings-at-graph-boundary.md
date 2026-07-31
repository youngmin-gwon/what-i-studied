---
title: "DI 테스트는 내부 구현을 건드리지 않고 graph boundary에서 binding을 교체한다"
tags: ["android", "android/app-framework"]
---

# DI 테스트는 내부 구현을 건드리지 않고 graph boundary에서 binding을 교체한다

DI가 테스트에 주는 이점은 production code 내부의 생성 코드를 바꾸지 않고 fake, test dispatcher, in-memory database, fake API를 graph boundary에서 바꿀 수 있다는 점이다.

테스트가 consumer 내부 필드를 직접 덮어쓰거나 singleton registry를 공유하면 순서 의존성과 누수가 생긴다. test graph, module replacement, factory injection처럼 명시적인 교체 지점을 둔다.

## 판단 기준

DI 노트는 객체를 어디서 만들고, 누가 소유하며, 어떤 lifetime 동안 재사용할지를 판단하는 기준으로 읽는다.

## 경계

framework 이름보다 graph boundary, scope, replacement seam, Android component lifetime을 먼저 확인한다.
