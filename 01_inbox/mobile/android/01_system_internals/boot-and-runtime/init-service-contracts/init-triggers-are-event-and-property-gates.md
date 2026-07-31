---
title: "init trigger는 event와 property 조건을 결합하는 실행 gate다"
tags: [android, android/system-internals, android/boot-runtime, android/init]
aliases: ["init trigger는 event와 property 조건을 결합하는 실행 gate다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# init trigger는 event와 property 조건을 결합하는 실행 gate다

상위 문서: [init와 네이티브 서비스 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-service-contracts.md)

init action은 trigger가 만족될 때만 command queue에 들어간다. trigger는 `early-init`, `init`, `late-init`, `boot` 같은 event trigger와 `property:name=value` 형태의 property trigger로 나뉘며, 하나의 action은 event trigger 하나와 여러 property trigger를 조합할 수 있다.

## 주의할 점

- property trigger는 `boot` event command가 끝난 뒤 최소 한 번 평가된다.
- 그 이후에는 property가 새로 만들어지거나 값이 바뀔 때 다시 평가된다.
- `on property:a=b && post-fs`는 `post-fs` event 시점에 property가 이미 맞아야 하며, 나중에 property가 바뀐다고 실행되지 않는다.
- trigger 순서에 의존하는 서비스는 boot stage와 mount stage를 명확히 분리해야 한다.

## 관련 문서

- [property service는 전역 상태 저장소이자 제한된 제어 plane이다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/property-service-is-global-state-store-and-restricted-control-plane.md)
- [First stage init은 second stage가 읽을 최소 파일시스템을 만든다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/first-stage-init-builds-minimal-filesystem-for-second-stage.md)

공식 문서: [Android Init Language](https://android.googlesource.com/platform/system/core/+/master/init/README.md)
