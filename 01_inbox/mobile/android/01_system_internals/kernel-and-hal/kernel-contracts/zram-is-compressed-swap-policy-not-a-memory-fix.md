---
title: zram-is-compressed-swap-policy-not-a-memory-fix
tags: [android, android/kernel, android/memory]
aliases: [mmd, zRAM, compressed swap]
date modified: 2026-08-05 14:15:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

## zRAM은 메모리 부족 해결책이 아니라 압축 swap 정책이다

상위 문서: [Kernel contracts](kernel-contracts.md)
배경 지식: [가상 메모리/swap](02_references/operating-systems/virtual-memory.md)

zRAM은 모바일 물리 RAM의 일부를 압축 가상 블록 디바이스(RAM-backed Compressed Block Device)로 마운트하여 익명 메모리(Anonymous Memory: 앱 힙, 스택, 공유 메모리) 페이지를 압축 스왑-아웃(Swap-out)하는 커널 기술이다.

플래시 메모리(NAND Flash)에 수많은 덮어쓰기 I/O를 유발하여 EMMC/UFS 수명을 단축시키는 전통적인 디스크 스왑과 달리, RAM 내부 압축을 통해 Flash 쓰기를 방지하지만 물리 메모리가 늘어나는 것은 아니며 CPU 압축/압축해제 연산 비용과 메모리의 트레이드오프 정책이다.

---

### 메커니즘: zRAM 압축/해제 및 mmd Writeback 흐름

```mermaid
graph TD
    A["Anonymous Memory Allocation\n(App Heap & Stack Pages)"] --> B{"Kernel Memory Pressure (PSI High)"}
    B -->|Page Swap-Out| C["zRAM Driver (/dev/block/zram0)"]
    C -->|Compress Engine: LZ4 / ZSTD| D["Compressed RAM Block"]
    
    E["App accesses swapped page"] -->|Page Fault| F["Decompress Page from zRAM"]
    F -->|Restore Page to Uncompressed RAM| A

    subgraph Modern Android (Android 15+)
        G["mmd (Memory Management Daemon)"] -->|Idle Recompression & Writeback| H["Flash Storage (/dev/block/zram_wb)"]
    end
    C --> G
```

1. **Compression Pipeline (LZ4/ZSTD)**: 익명 페이지가 스왑 아웃될 때 커널 zRAM 드라이버가 4KB 비압축 페이지를 평균 1.5KB~2KB 크기로 압축하여 RAM 블록 메모리에 배치.
2. **Decompression CPU Trade-off**: 앱이 스왑 아웃된 메모리 영역을 재참조할 때 Page Fault가 유발되며, CPU가 즉시 압축 해제 작업을 수행한다. CPU 주파수가 낮거나 압축 해제 작업이 빈번하면 UI Jank가 발생할 수 있다.
3. **`mmd` & ZRAM Writeback**: Android 15+ 메모리 관리 데몬(`mmd`)은 기기가 유휴(Idle) 상태일 때 zRAM의 차가운(Cold) 페이지를 더 강력한 ZSTD 알고리즘으로 재압축하거나, 플래시 메모리 기반의 백킹 파일로 비동기 Writeback을 수행한다.

---

### `fstab` zRAM 마운트 및 커널 파라미터 설정 예시

```text
# /vendor/etc/fstab.hardware 예시
/dev/block/zram0  none  swap  defaults  zramsize=60%,max_comp_streams=8,comp_algorithm=zstd
```

```bash
# zRAM 런타임 설정 및 압축 알고리즘 변경
adb shell "echo zstd > /sys/block/zram0/comp_algorithm"
adb shell "echo 3221225472 > /sys/block/zram0/disksize" # 3GB 설정
adb shell "mkswap /dev/block/zram0"
adb shell "swapon /dev/block/zram0"
```

---

### 실무 규칙

- zRAM 용량을 비이성적으로 너무 크게 설정(예: 물리 RAM의 150% 이상)하면, 압축 불가능한 데이터가 쌓일 때 zRAM 자체가 RAM을 점유하여 LMKD가 적절한 타이밍에 프로세스를 킬하지 못하고 디바이스가 전체 멈춤(System Freeze) 상태에 빠질 수 있다.
- zRAM 효율성을 극대화하려면 물리 RAM 용량에 맞춰 zramsize(보통 50%~75%)를 조정하고, 스와핑 임계값(`vm.swappiness=100`~`180`)을 튜닝해야 한다.

---

### 관측 가능한 증거 (Observable Evidence)

1. **디바이스의 zRAM 압축 상태 및 스왑 점유율 분석 (`zramctl`)**:
   ```bash
   adb shell zramctl
   # NAME       ALGORITHM DISKSIZE  DATA  COMPR  TOTAL STREAMS MOUNTPOINT
   # /dev/block/zram0 zstd       3G  1.2G 400M   450M       8 [SWAP]
   ```
2. **`procfs` / `sysfs` 노드를 통한 메모리 압축 효율 통계 확인**:
   ```bash
   adb shell cat /sys/block/zram0/mm_stat
   # 1234567890 400000000 450000000 0 450000000 8 0 0
   # (orig_data_size, compr_data_size, mem_used_total 순)
   ```
3. **procfs 스왑 요약 정보 출력**:
   ```bash
   adb shell cat /proc/swaps
   # Filename        Type            Size      Used    Priority
   # /dev/block/zram0 partition       3145724   1245000 60
   ```

---

### 관련 문서

- [LMKD는 free memory가 아니라 memory pressure와 process importance로 종료를 결정한다](lmkd-kills-processes-by-memory-pressure-and-process-importance.md)
- [PSI는 free memory가 아니라 stall time을 측정한다](psi-measures-stall-time-for-memory-pressure.md)

공식 문서: [AOSP Memory Management Daemon (mmd)](https://source.android.com/docs/core/perf/mmd), [AOSP Low Memory Killer Daemon](https://source.android.com/docs/core/perf/lmkd)

