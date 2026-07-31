# A/B Update (Seamless Update)

### 개념

```
Slot A: [boot_a, system_a, vendor_a] ← 현재 부팅
Slot B: [boot_b, system_b, vendor_b] ← 업데이트 다운로드 중
```

**업데이트 과정**:

1. 백그라운드에서 Slot B 에 다운로드
2. 완료 후 boot control 변경: active=B
3. 재부팅 → Slot B 로 부팅
4. 성공 시 Slot B 확정, 실패 시 Slot A 로 자동 롤백

### Virtual A/B (Android 11+)

```
Slot A: [실제 파티션]
Slot B: [Snapshot (COW)] ← 공간 절약
```

**변경 부분만** 스냅샷으로 저장 → 공간 50% 절약

---
