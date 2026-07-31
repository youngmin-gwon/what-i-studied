# Treble

상위 노트: [[android-modular-system]]

Vendor 와 System 분리 (Android 8.0+).

**구조:**

```
System Partition (Google)
    ↓ HIDL/AIDL
Vendor Partition (OEM)
    ↓
Hardware
```

**장점:**

- OEM 이 커널/드라이버만 업데이트하면 됨
- Google 이 시스템 업데이트 독립적으로 제공
- 업데이트 속도 향상
