# Init Process

**First Stage**:

- `/dev`, `/proc`, `/sys` 마운트
- SELinux early init

**Second Stage**:

- RC 스크립트 파싱 (`/system/etc/init/`, `/vendor/etc/init/`)
- 트리거 실행 (`on early-init`, `on init`, `on boot`)
- 서비스 시작

**상세**: [android-init-and-services](01_inbox/mobile/android/01_system_internals/boot-and-runtime/android-init-and-services.md)
