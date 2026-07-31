# Zygote는 framework 공통 상태를 preload한 뒤 앱 프로세스를 fork한다

상위 문서: [Zygote와 ART 런타임 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-runtime-contracts.md)

Zygote는 앱마다 새 runtime을 처음부터 만드는 비용을 피하기 위해 framework class, resource, runtime state의 공통 부분을 먼저 올린다. 이후 앱 실행 요청을 받으면 그 상태를 가진 프로세스를 fork해 앱별 specialization을 수행한다.

## 판단 기준

- preload는 앱 시작을 빠르게 하지만 boot time과 Zygote 메모리 footprint를 늘릴 수 있다.
- 모든 앱이 공유할 가능성이 높은 framework 상태만 preload 이득이 크다.
- 앱별 상태를 Zygote preload 영역에 섞으면 copy-on-write 이점을 잃는다.

## 관련 문서

- [Zygote fork의 메모리 이점은 copy-on-write가 유지될 때 생긴다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-fork-saves-memory-while-copy-on-write-pages-stay-clean.md)
- [system_server는 framework service를 한 프로세스 안에서 시작한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-starts-framework-services-in-one-process.md)

공식 문서: [About the Zygote processes](https://source.android.com/docs/core/runtime/zygote)
