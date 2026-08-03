---
title: "Android 부팅과 런타임 지도"
tags: [android, android/system-internals, android/boot-runtime]
aliases: ["Android 부팅과 런타임 지도"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Android 부팅과 런타임 지도

Android 부팅과 런타임은 기기가 신뢰 가능한 OS 이미지를 선택하고, `init`이 네이티브 서비스를 세우고, Zygote와 `system_server`가 앱 프레임워크를 여는 과정이다. 네 묶음은 서로 다른 책임 계층이며, 앱 코드가 개입할 수 있는 지점은 `system_server`가 앱 프로세스를 fork한 이후부터다.

## 정본 노트
- [부팅 흐름 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-flow-contracts.md) — bootloader/kernel 계층. 신뢰 검증과 파티션/OTA 경계를 다룬다.
- [init와 네이티브 서비스 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-service-contracts.md) — native userspace 계층. PID 1인 `init`이 세우는 서비스와 property를 다룬다.
- [Zygote와 ART 런타임 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-runtime-contracts.md) — process/runtime 계층. 앱 프로세스가 어떻게 만들어지고 DEX가 어떻게 실행되는지를 다룬다.
- [system_server와 ActivityManager 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md) — framework service 계층. app API가 호출하는 Binder endpoint와 lifecycle 정책을 다룬다.

## 읽는 순서

1. bootloader가 신뢰 상태와 부팅 slot을 결정한다.
2. kernel이 userspace의 첫 프로세스인 `init`을 실행한다.
3. `init`이 파일시스템, property, SELinux, 네이티브 서비스를 세운다.
4. Zygote가 framework 공통 상태를 미리 올리고 앱 프로세스를 fork한다.
5. `system_server`가 framework service를 시작하고 앱 lifecycle을 관리한다.

## 문제 분류 기준

- 기기가 부팅 루프에 빠지거나 OTA 후 못 켜진다 -> [부팅 흐름 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-flow-contracts.md)의 slot/AVB/partition 노트부터 본다.
- 특정 native daemon이나 HAL 관련 서비스가 안 뜬다 -> [init와 네이티브 서비스 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-service-contracts.md)에서 rc 선언과 property trigger를 본다.
- 앱 프로세스가 예상보다 자주 죽거나 시작이 느리다 -> [Zygote와 ART 런타임 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-runtime-contracts.md)에서 fork/specialization/ART 컴파일 상태를 본다.
- 앱 API 호출이 정책 때문에 거절되거나 ANR/프로세스 우선순위 문제로 보인다 -> [system_server와 ActivityManager 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md)에서 dumpsys/AMS/ATMS를 본다.
- 이 네 계층 모두 앱 코드가 직접 호출하는 public API가 아니므로, 원인 분석은 `dumpsys`, `logcat` tag, `getprop` 같은 관찰 가능 신호로 시작하고 해당 계약 노트의 디버깅 절로 이동한다.
