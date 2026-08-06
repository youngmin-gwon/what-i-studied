---
title: android-shared-memory-evolved-from-ashmem-ion-to-dmabuf-heaps
tags: [android, android/kernel, android/memory]
aliases: [ashmem, DMA-BUF, ION]
date modified: 2026-08-05 16:00:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

## Android shared memory는 ashmem, ION, DMA-BUF heaps로 역할이 분화됐다

상위 문서: [Kernel contracts](kernel-contracts.md)
배경 지식: [SELinux](../../../../../linux/security/selinux.md)

Android의 공유 메모리(Shared Memory) 메커니즘은 CPU 프로세스 간 텍스트/데이터 버퍼 전달부터 카메라/GPU/Display/H/W Codec 간 저지연 Zero-copy 버퍼 공유까지 진화하며 역할이 분화되어 왔다.

과거 Android 전용 out-of-tree 커널 드라이버였던 `ashmem`과 `ION`은 Modern Linux 커널 표준인 `memfd` 및 `DMA-BUF heaps` 규격으로 완벽히 대체되었다.

---

### 메커니즘: 공유 메모리 메커니즘의 진화 과정

```mermaid
graph TD
    subgraph Legacy Out-of-tree (Android 11 이전)
        A1["ashmem (/dev/ashmem)\n(CPU IPC Shared Memory & Memory Pinned/Unpinned)"]
        A2["ION Allocator (/dev/ion)\n(System, Contiguous(CMA), Custom Heap Allocation)"]
    end
    subgraph Modern Standard (Android 12+ GKI 2.0)
        B1["memfd (memfd_create)\n(Linux Upstream POSIX Shared Memory File Descriptor)"]
        B2["DMA-BUF Heaps (/dev/dma_heap/*)\n(Upstream Linux DMA-BUF Interface & Independent Sepolicy)"]
    end
    A1 -->|Replaced by| B1
    A2 -->|Replaced by| B2
```

1. **`ashmem` -> `memfd`**:
   - `ashmem`(Anonymous Shared Memory)은 메모리 영역에 이름을 부여하고 `unpin` 기능을 통해 LMK 시 메모리를 버릴 수 있도록 지원했으나, Linux upstream에 통합되지 못함.
   - Android 10+부터 `memfd_create()` 및 `ASHMEM_SET_NAME` 호환 래퍼로 전환되었으며, NDK의 `ASharedMemory_create()` 역시 내부적으로 `memfd`를 사용.
2. **`ION` -> `DMA-BUF Heaps`**:
   - `ION`은 하나의 `/dev/ion` 문자 디바이스 노드와 비표준 ioctl 번호를 공유했다. 이 때문에 어떤 프로세스가 어떤 파일/디바이스에 접근할 수 있는지를 소유자가 아니라 커널이 정책 파일 기준으로 강제하는 **SELinux**(mandatory access control 을 구현하는 리눅스 보안 모듈)를 노드 단위로 분리 적용하기 어려웠고, 그만큼 샌드박싱도 느슨해졌다.
   - `DMA-BUF heaps`는 힙 유형별로 별도의 디바이스 노드(`/dev/dma_heap/system`, `/dev/dma_heap/linux,cma` 등)를 노출하여 각 힙별 SELinux 접근 권한을 독립적으로 제어 가능.

---

### DMA-BUF Heap 및 ASharedMemory Allocator C++ 사용 예시

```cpp
// 1. Modern Android NDK Shared Memory (memfd 기반)
#include <android/sharedmem.h>
#include <sys/mman.h>

int allocate_shared_memory(size_t size) {
    int fd = ASharedMemory_create("MySharedBuffer", size);
    if (fd < 0) return -1;

    // Read/Write Mmap
    void* addr = mmap(NULL, size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    // Binder IPC를 통해 다른 프로세스(Client)로 fd 전달
    return fd;
}

// 2. DMA-BUF Heap Allocator C++ (BufferAllocator 라이브러리 사용)
#include <BufferAllocator/BufferAllocator.h>

int allocate_dmabuf_heap(size_t size) {
    BufferAllocator allocator;
    // system-uncached 또는 system heap에서 DMA 버퍼 할당
    int dmabuf_fd = allocator.Alloc("system", size);
    if (dmabuf_fd < 0) return -1;

    // GPU / Camera / Display HAL로 dmabuf_fd 넘김 (Zero-copy)
    return dmabuf_fd;
}
```

---

### 실무 규칙

- 앱 개발 시 그래픽/비디오 버퍼는 `AHardwareBuffer` API를 사용해야 하며, 이 API가 하위 레벨에서 `DMA-BUF` 버퍼 바인딩과 라이프사이클 관리를 자동으로 수행한다.
- `/dev/ion` 파일에 직접 의존하는 legacy native C/C++ 라이브러리는 GKI 커널 5.10 이상 기기에서 동작하지 않으므로 `libdmabufheap` (`BufferAllocator`)으로 마이그레이션해야 한다.

---

### 관측 가능한 증거 (Observable Evidence)

1. **디바이스 내 DMA-BUF Heap 노드 활성화 상태 확인**:
   ```bash
   adb shell ls -la /dev/dma_heap/
   # crw-rw-rw- 1 system system 10, 55 system
   # crw-rw-rw- 1 system system 10, 56 system-uncached
   # crw-rw-rw- 1 system system 10, 57 linux,cma
   ```
2. **dumpsys를 통한 프로세스별 DMA-BUF 메모리 점유량 분석**:
   ```bash
   adb shell dumpsys meminfo | grep -E "DMA-BUF|ion"
   # Output: DMA-BUF: 145000 KB (System total DMA-BUF allocation)
   ```
3. **procfs를 통한 DMA-BUF 버퍼 통계 및 디버그 노드 조회**:
   ```bash
   adb shell cat /proc/meminfo | grep DmaBufTotal
   # DmaBufTotal:       148480 kB
   ```

---

### 관련 문서

- [DMA-BUF zero-copy는 무작업 보장이 아니라 shared buffer ownership이다](dmabuf-zero-copy-means-shared-buffer-ownership-not-no-work.md)
- [Surface based media pipeline avoids app-level pixel copy](../../graphics-and-media/graphics-media-contracts/surface-based-media-pipeline-avoids-app-level-pixel-copy.md)

공식 문서: [AOSP DMA-BUF Heaps](https://source.android.com/docs/core/architecture/kernel/dma-buf-heaps)

