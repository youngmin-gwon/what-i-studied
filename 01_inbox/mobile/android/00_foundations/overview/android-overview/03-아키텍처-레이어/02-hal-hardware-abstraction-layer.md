# HAL (Hardware Abstraction Layer)

**역할**: 하드웨어와 안드로이드 연결

**왜 필요한가**:

- 칩셋마다 다른 드라이버
- OEM 별 다른 하드웨어
- → 표준 인터페이스로 추상화

**예시**:

```
Camera HAL → 삼성/LG/Google 카메라 모두 동일 API
Audio HAL → Qualcomm/MediaTek 오디오 칩 통합
```

**상세**: [android-hal-and-kernel](01_inbox/mobile/android/01_system_internals/kernel-and-hal/android-hal-and-kernel.md)

---
