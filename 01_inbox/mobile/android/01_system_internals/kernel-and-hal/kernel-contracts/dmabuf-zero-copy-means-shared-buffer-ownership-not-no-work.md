---
title: DMA-BUF zero-copy는 무작업 보장이 아니라 shared buffer ownership이다
tags: [android, android/kernel, android/memory]
date modified: 2026-07-31 23:45:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

# DMA-BUF zero-copy는 무작업 보장이 아니라 shared buffer ownership이다

DMA-BUF 기반 경로에서 zero-copy라고 말할 때는 “앱이나 중간 계층이 픽셀 데이터를 CPU로 복사하지 않고 buffer ownership 또는 file descriptor를 전달한다”는 뜻으로 좁혀 쓰는 편이 정확하다.

이 표현은 system 전체에 복사가 전혀 없거나, format conversion, cache maintenance, fence wait, IOMMU mapping, compositor work가 없다는 뜻이 아니다. producer와 consumer가 같은 buffer를 공유하더라도 동기화와 hardware access 비용은 남는다.

Camera, GPU, codec, display 파이프라인에서는 DMA-BUF와 Surface/BufferQueue가 함께 등장할 수 있다. 이때 분석 지점은 “복사를 했는가” 하나가 아니라 allocation heap, usage flag, fence, queue depth, protected memory, consumer capability다.

따라서 기존 노트의 “제로카피 달성: 데이터는 한 번만 메모리에 쓰인다”는 설명은 너무 강하다. 정본에서는 “앱 수준 CPU copy를 줄이는 shared buffer contract”로 표현한다.

관련 노트: [Android shared memory는 ashmem, ION, DMA-BUF heaps로 역할이 분화됐다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/android-shared-memory-evolved-from-ashmem-ion-to-dmabuf-heaps.md), [BufferQueue separates producer and consumer with buffer ownership](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/bufferqueue-separates-producer-and-consumer-with-buffer-ownership.md)
