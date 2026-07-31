# HAL (Hardware Abstraction Layer)

상위 노트: [android-glossary](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md)

**정의**: 하드웨어와 안드로이드 프레임워크를 연결하는 인터페이스

**상세**:

기기마다 다른 하드웨어 (카메라, 센서, GPS 등) 를 표준 API 로 추상화한다. HIDL(Legacy) 또는 AIDL(Modern) 로 정의되며, Vendor 파티션에 구현체가 위치한다.

**진화**:

```
Legacy HAL (.so 직접 로드)
  ↓
HIDL HAL (C++, Treble)
  ↓
AIDL HAL (다중 언어, 간결)
```

**예시**:

```bash
# HAL 서비스 확인
adb shell lshal

# 출력:
# android.hardware.camera.provider@2.4::ICameraProvider/legacy/0
# android.hardware.audio@7.0::IDevicesFactory/default
```

**관련**: [android-hal-and-kernel](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hal-is-stable-userspace-contract-between-framework-and-vendor.md)

---

---

### L
