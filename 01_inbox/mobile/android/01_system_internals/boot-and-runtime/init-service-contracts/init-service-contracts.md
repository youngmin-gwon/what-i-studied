---
title: "init와 네이티브 서비스 계약"
tags: [android, android/system-internals, android/boot-runtime, android/init]
aliases: ["init와 네이티브 서비스 계약"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# init와 네이티브 서비스 계약

`init`은 Android userspace의 첫 프로세스이며, `.rc` 선언을 읽어 파일시스템, property, SELinux, native daemon, Zygote 시작 순서를 조율한다. 이 묶음은 native/OS 계층 책임이며, 앱 API나 framework service(system_server) 정책이 아니라 그보다 먼저 세워지는 기반을 다룬다.

## 읽는 순서

1. [init는 PID 1이자 Android userspace의 부트스트랩 정책 엔진이다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-is-pid1-and-userspace-bootstrap-policy-engine.md) — 전체 역할 정의.
2. [First stage init은 second stage가 읽을 최소 파일시스템을 만든다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/first-stage-init-builds-minimal-filesystem-for-second-stage.md), [fstab은 mount와 검증 플래그를 묶은 부팅 계약이다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/fstab-is-boot-time-mount-and-verification-contract.md) — 파일시스템이 준비되는 순서.
3. [init rc 언어는 actions, services, options, imports를 선언한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-rc-language-declares-actions-services-options-and-imports.md), [init trigger는 event와 property 조건을 결합하는 실행 gate다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-triggers-are-event-and-property-gates.md) — `.rc` 선언과 실행 조건 문법.
4. [init service는 재시작 정책을 가진 supervised process다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-service-is-supervised-process-with-explicit-lifecycle.md), [service option은 identity, resource, class, socket 계약을 고정한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/service-options-fix-identity-resource-class-and-socket-contracts.md) — 개별 native service의 lifecycle과 권한.
5. [property service는 전역 상태 저장소이자 제한된 제어 plane이다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/property-service-is-global-state-store-and-restricted-control-plane.md), [ueventd는 kernel uevent를 dev node 권한으로 변환한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/ueventd-turns-kernel-uevents-into-dev-node-permissions.md) — init이 관리하는 시스템 전역 상태와 device node.
6. [init 보안은 SELinux domain과 capability 경계로 정의된다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-security-is-selinux-domain-and-capability-boundary.md) — 위 모든 것을 가로지르는 권한 경계.
7. [init 디버깅은 로그, property, service 상태를 함께 본다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-debugging-uses-logs-properties-and-service-state.md) — 문제가 생겼을 때 진입점.

## 경계 규칙

- `init rc 언어`는 문법(선언 구조) 정본이고, `init trigger`는 그 문법 중 실행 조건(when) 하나만 분리해 다룬다. 둘을 같은 노트에 합치지 않는다.
- `init service` 노트는 서비스의 lifecycle(재시작 정책)을 다루고, `service option` 노트는 그 서비스에 붙는 개별 옵션(권한/자원/socket)을 다룬다 — 겹치는 예시를 새로 만들지 않는다.
- SELinux/capability 세부 구현은 [플랫폼 보안 정본](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/platform-security-contracts.md)이 아니라 이 폴더가 init 도메인 한정으로 다루고, 앱 sandbox 자체의 UID/프로세스 경계는 security 정본으로 넘긴다.
- Zygote 시작 이후의 process/runtime 정책은 이 묶음이 아니라 [Zygote와 ART 런타임 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-runtime-contracts.md)이 정본이다.
