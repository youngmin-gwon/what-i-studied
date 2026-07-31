# GKI (Generic Kernel Image)

상위 노트: [android-modular-system](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system.md)

Android 11+ 에서 커널도 모듈화.

**구조:**

```
GKI (Generic Kernel)
    ↓
Vendor Modules (OEM 드라이버)
```

**장점:**

- 커널 보안 패치 빠르게 배포
- OEM 은 드라이버만 관리
- 파편화 감소
