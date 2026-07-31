# Android 부팅과 런타임 지도

Android 부팅과 런타임은 기기가 신뢰 가능한 OS 이미지를 선택하고, `init`이 네이티브 서비스를 세우고, Zygote와 `system_server`가 앱 프레임워크를 여는 과정이다.

## 정본 노트
- [부팅 흐름 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/boot-flow-contracts.md)
- [init와 네이티브 서비스 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-service-contracts.md)
- [Zygote와 ART 런타임 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-runtime-contracts.md)
- [system_server와 ActivityManager 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md)

## 읽는 순서

1. bootloader가 신뢰 상태와 부팅 slot을 결정한다.
2. kernel이 userspace의 첫 프로세스인 `init`을 실행한다.
3. `init`이 파일시스템, property, SELinux, 네이티브 서비스를 세운다.
4. Zygote가 framework 공통 상태를 미리 올리고 앱 프로세스를 fork한다.
5. `system_server`가 framework service를 시작하고 앱 lifecycle을 관리한다.
