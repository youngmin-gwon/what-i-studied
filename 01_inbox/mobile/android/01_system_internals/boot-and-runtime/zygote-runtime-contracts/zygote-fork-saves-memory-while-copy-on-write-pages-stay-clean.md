# Zygote fork의 메모리 이점은 copy-on-write가 유지될 때 생긴다

상위 문서: [Zygote와 ART 런타임 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-runtime-contracts.md)

Zygote fork가 빠른 이유는 부모 메모리를 즉시 복사하지 않고 child process와 page를 공유하기 때문이다. 하지만 공유 page에 쓰기가 발생하면 copy-on-write로 private copy가 생기므로, preload된 상태가 clean하게 유지될수록 메모리 이점이 커진다.

## 실무 의미

- framework class와 immutable resource는 여러 앱 사이에서 공유 이득이 크다.
- 앱 시작 중 많은 전역 상태를 수정하면 COW page가 늘어날 수 있다.
- native heap, JIT code cache, 앱별 class loading은 각 process의 private 비용으로 본다.
- 메모리 분석에서는 RSS 하나만 보지 말고 shared/private page 관점을 함께 본다.

## 관련 문서

- [Android 프로세스와 메모리](01_inbox/mobile/android/01_system_internals/ipc-and-process/android-process-and-memory.md)
- [Zygote는 framework 공통 상태를 preload한 뒤 앱 프로세스를 fork한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-preloads-framework-state-before-app-fork.md)
