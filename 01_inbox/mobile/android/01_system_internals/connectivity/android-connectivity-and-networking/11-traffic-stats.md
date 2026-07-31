# Traffic Stats

상위 노트: [android-connectivity-and-networking](01_inbox/mobile/android/01_system_internals/connectivity/android-connectivity-and-networking.md)

```kotlin
// 앱별 네트워크 사용량
val uid = android.os.Process.myUid()
val rxBytes = TrafficStats.getUidRxBytes(uid)  // 수신
val txBytes = TrafficStats.getUidTxBytes(uid)  // 송신

Log.d(TAG, "Received: ${rxBytes / 1024} KB")
Log.d(TAG, "Sent: ${txBytes / 1024} KB")

// 총 사용량
val totalRx = TrafficStats.getTotalRxBytes()
val totalTx = TrafficStats.getTotalTxBytes()
```

**eBPF 기반 추적** (Android 9+):

```c
// BPF map으로 UID별 트래픽 카운트
struct stats_key {
    uint32_t uid;
    uint32_t tag;
    uint32_t interface_index;
};

struct stats_value {
    uint64_t rx_bytes;
    uint64_t tx_bytes;
    uint64_t rx_packets;
    uint64_t tx_packets;
};
```

---
