---
title: Android kernel build는 branch, toolchain, build system 계약이다
tags: [android, android/kernel, android/build]
date modified: 2026-07-31 23:45:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

Android kernel build는 단순히 `make`를 실행하는 작업이 아니다. 올바른 kernel manifest branch, AOSP 제공 LLVM toolchain, Kleaf/Bazel 또는 legacy `build.sh`, device/vendor module 구성, boot image packaging 조건이 맞아야 한다.

최근 kernel은 `repo init -u https://android.googlesource.com/kernel/manifest -b BRANCH`로 source와 build tools를 가져오고, Android 13 이후에는 Bazel/Kleaf 흐름이 중심이다. Android 14 이상에서는 `build.sh`가 지원되지 않는다는 점도 문서에 분리해야 한다.

branch 선택은 제품 Android version, kernel LTS version, device target, vendor module 호환성과 연결된다. 예전 노트에 고정된 ACK branch 표를 복사해 두면 빨리 낡으므로, 정본에서는 공식 branch/build-system 문서를 확인하는 규칙만 남긴다.

custom kernel flashing은 verified boot, rollback protection, SPL downgrade, device wipe 위험과 연결된다. 학습용 Cuttlefish와 실제 Pixel/device flashing은 위험 수준이 다르다.

관련 노트: {link(CONTRACTS / "kernel-debugging-starts-before-logcat-with-bootloader-dmesg-and-trace.md", "Kernel debugging은 logcat 이전의 신호에서 시작한다")}, {link(ANDROID / "01_system_internals/boot-and-runtime/boot-flow-contracts/boot-debugging-starts-before-logcat-with-kernel-pstore-init-logs.md", "Boot debugging starts before logcat")}

근거: [Build kernels](https://source.android.com/docs/setup/build/building-kernels), [Kernel branches and their build systems](https://source.android.com/docs/setup/reference/bazel-support)
