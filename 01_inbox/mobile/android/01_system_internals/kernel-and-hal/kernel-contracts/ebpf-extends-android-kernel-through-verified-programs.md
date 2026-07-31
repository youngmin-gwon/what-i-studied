---
title: eBPF는 검증된 프로그램으로 Android kernel 기능을 확장한다
tags: [android, android/kernel, android/ebpf]
aliases: [eBPF, BPF]
date modified: 2026-07-31 23:45:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

eBPF는 kernel 안에서 실행되는 작은 프로그램을 통해 statistics 수집, monitoring, debugging, packet filtering 같은 기능을 확장하는 mechanism이다. 프로그램은 `bpf(2)` syscall로 load되고, verifier를 통과해야 kernel에서 실행될 수 있다.

Android는 boot 중 `/system/etc/bpf/`에 있는 eBPF program을 load하는 BPF loader와 library를 제공한다. AOSP 예시에는 netd traffic monitor, CPU frequency time-in-state, GPU memory profiling 같은 사용이 있다.

eBPF는 아무 native code나 kernel에 넣는 방법이 아니다. verifier, 허용된 helper, map, hook type, SELinux policy, Android build system을 통과해야 한다. 그래서 kernel module보다 안전한 확장 지점을 제공하지만, 일반 앱의 임의 확장 API는 아니다.

성능 설명도 단순화하면 안 된다. 특정 firewall/statistics 경로에서 eBPF가 효율적일 수 있지만, 모든 iptables/nftables 대체나 모든 query가 O(1)이라는 일반 명제로 쓰면 부정확하다.

관련 노트: {link(ANDROID / "01_system_internals/connectivity/connectivity-contracts/netd-enforces-routing-dns-firewall-and-tethering-operations.md", "netd enforces routing DNS firewall and tethering operations")}

근거: [Extend the kernel with eBPF](https://source.android.com/docs/core/architecture/kernel/bpf)
