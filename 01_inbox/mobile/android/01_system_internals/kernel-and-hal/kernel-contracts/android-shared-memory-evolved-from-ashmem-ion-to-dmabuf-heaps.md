---
title: android-shared-memory-evolved-from-ashmem-ion-to-dmabuf-heaps
tags: [android, android/kernel, android/memory]
aliases: [ashmem, DMA-BUF, ION]
date modified: 2026-08-03 17:25:57 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

## Android shared memory 는 ashmem, ION, DMA-BUF heaps 로 역할이 분화됐다

Android 의 shared memory 문제는 하나가 아니다. 앱과 system service 사이의 CPU 접근 가능한 공유 메모리, camera/GPU/codec/display 사이의 DMA buffer 공유, protected media buffer 는 서로 다른 요구를 가진다.

ashmem 은 anonymous shared memory 를 file descriptor 로 표현해 Binder 로 전달할 수 있게 만든 초기 Android 메커니즘이다. CPU 가 접근하는 공유 메모리에는 유용했지만, GPU 나 camera 같은 device DMA buffer 문제를 모두 해결하는 모델은 아니다.

ION 은 device/SoC 별 heap 을 통해 multimedia buffer allocation 을 다루던 Android-specific allocator 였다. 그러나 heap id/flag 와 `/dev/ion` 단일 접근 모델은 표준화와 sepolicy 분리에 약했다.

Android 12 의 GKI 2.0 에서는 kernel 5.10 계열에서 ION allocator 가 DMA-BUF heaps 로 대체되는 방향을 갖는다. DMA-BUF heaps 는 heap 별 character device 와 upstream ABI 안정성을 통해 vendor/device buffer allocation 을 더 명확히 분리한다.

CMA(Contiguous Memory Allocator)는 device DMA 를 위해 물리적으로 연속된 영역이 필요한 경우를 지원할 수 있지만, 모든 camera/GPU/codec 경로가 항상 물리 연속 메모리를 요구한다는 뜻은 아니다. IOMMU, heap 종류, driver 요구사항에 따라 필요한 allocation 제약이 달라진다.

관련 노트: [DMA-BUF zero-copy는 무작업 보장이 아니라 shared buffer ownership이다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/dmabuf-zero-copy-means-shared-buffer-ownership-not-no-work.md), [Surface based media pipeline avoids app-level pixel copy](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/surface-based-media-pipeline-avoids-app-level-pixel-copy.md)

근거: [Transition from ION to DMA-BUF heaps](https://source.android.com/docs/core/architecture/kernel/dma-buf-heaps)
