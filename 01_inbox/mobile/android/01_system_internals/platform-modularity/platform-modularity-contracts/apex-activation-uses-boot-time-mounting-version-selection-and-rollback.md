---
title: "APEX activation은 boot-time mount, version selection, rollback 경계다"
tags: ["android", "android/system-internals"]
aliases: ["APEX activation은 boot-time mount, version selection, rollback 경계다"]
date modified: 2026-08-03 16:30:00 +09:00
date created: 2026-07-31 23:05:30 +09:00
---

# APEX activation은 boot-time mount, version selection, rollback 경계다

APEX update는 설치 즉시 running system을 임의로 바꾸는 모델이 아니다. updated APEX는 기존 built-in package를 shadow할 수 있고, activation은 boot 과정에서 `apexd`(native daemon, system_server보다 이른 단계)가 version을 선택하고 mount하면서 이루어진다. 이 계약은 native/platform 계층 책임이며, 앱 코드는 activation 시점을 관찰할 수만 있고 직접 제어하지 못한다.

Mainline module update는 필요한 module 묶음이 원자적으로 적용되거나 rollback될 수 있어야 한다. 일부만 적용되어 system component set이 어긋나는 상태를 피하는 것이 핵심이다.

Compressed APEX는 업데이트 후 built-in APEX가 차지하는 저장 공간 문제를 줄이기 위한 포맷이다. 성능 최적화 포맷이라기보다 system partition과 `/data` update copy 사이의 storage tradeoff를 다루는 장치다.

## 관찰 가능 신호와 디버깅 진입점

- `adb shell pm list packages --apex-only`로 현재 활성화된 APEX 목록과 버전을 볼 수 있다.
- logcat에서 `apexd` tag를 확인하면 activation, staged install, rollback 시도를 볼 수 있다.
- staged APEX 설치는 재부팅이 있어야 activation이 완료되므로, "설치했는데 반영이 안 됐다"는 보고는 재부팅 여부부터 확인한다.

관련 노트: [APEX package 경계](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apex-packages-lower-level-system-modules-that-apk-cannot-model-well.md), [boot/runtime 정본](01_inbox/mobile/android/01_system_internals/boot-and-runtime/android-boot-and-runtime.md), [platform-modularity hub](01_inbox/mobile/android/01_system_internals/platform-modularity/android-platform-modularity.md).

공식 문서: [How To APEX](https://android.googlesource.com/platform/system/apex/+/refs/heads/main/docs/howto.md)

공식 문서: [APEX file format](https://source.android.com/docs/core/ota/apex)
