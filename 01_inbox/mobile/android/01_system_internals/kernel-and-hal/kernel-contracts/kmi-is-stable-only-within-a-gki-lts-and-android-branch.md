---
title: KMI 안정성은 같은 GKI LTS/Android branch 안에서만 성립한다
tags: [android, android/kernel, android/gki]
aliases: [KMI, Kernel Module Interface]
date modified: 2026-07-31 23:45:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

Kernel Module Interface(KMI)는 GKI kernel과 vendor module 사이에서 안정적으로 유지해야 하는 kernel symbol interface다. vendor module은 허용된 KMI symbol에 의존해야 하며, GKI와 별도 tree에서 빌드되더라도 함께 빌드된 것처럼 동작해야 한다.

KMI 안정성은 무제한 ABI 안정성이 아니다. 공식 문서 기준으로 KMI는 같은 LTS와 Android version의 kernel branch 안에서만 유지된다. 예를 들어 `android14-6.1`과 `android15-6.6` 사이의 KMI 호환을 가정하면 안 된다.

Linux mainline은 일반적으로 in-kernel ABI 안정성을 보장하지 않는다. GKI가 가능한 이유는 `gki_defconfig`, AOSP LLVM toolchain, symbol list, branch freeze 같은 제한된 환경을 전제로 하기 때문이다.

따라서 vendor module 개발이나 kernel update 문서에서는 “모듈 재컴파일 불필요”를 절대 규칙으로 쓰지 않는다. 같은 KMI version 안에서, KMI symbol만 사용하고, branch/toolchain 조건을 지켰을 때의 계약으로 적는다.

관련 노트: {link(CONTRACTS / "gki-splits-generic-core-from-vendor-modules.md", "GKI는 공통 core kernel과 vendor module을 분리한다")}

근거: [Maintain a stable KMI](https://source.android.com/docs/core/architecture/kernel/stable-kmi), [GKI versioning scheme](https://source.android.com/docs/core/architecture/kernel/gki-versioning)
