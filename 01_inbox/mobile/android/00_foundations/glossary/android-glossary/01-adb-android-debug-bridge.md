---
title: "ADB는 기기와 통신하며 디버깅과 제어를 수행하는 브리지다"
tags: ["android", "android/glossary"]
aliases: ["adb", "Android Debug Bridge"]
date modified: 2026-08-01 01:07:08 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

# ADB는 기기와 통신하며 디버깅과 제어를 수행하는 브리지다

정의: ADB 는 개발 머신이 emulator 또는 device 와 통신해 app 설치, shell 실행, log 수집, port forwarding, test automation 을 수행하는 debugging bridge 다.

혼동 방지: ADB 는 Android app API 가 아니라 host-to-device control plane 이다. 앱 코드의 동작 모델을 설명할 때는 ADB command 자체보다 device state, build variant, permission, process 상태를 함께 봐야 한다.

정본 링크:

- [ADB, emulator, device tools](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/adb-emulator-and-device-tools-control-test-environment.md)
- [Android debugging contracts](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/debugging-contracts.md)
