# 🛠️ App Process Initialization

앱 프로세스가 fork 된 직후 실행되는 순서입니다:

1. **Zygote Init**: `fork()` 후 쓰레드 풀 초기화.
2. **Runtime Init**: C++ 네이티브 브릿지 설정.
3. **Application bind**: `ActivityThread.main()` 실행.
4. **Attach**: `AMS` 에게 "나 살았어요"라고 신고.
5. **Instrumentation**: `Application.onCreate()` 실행. (여기서부터 개발자 영역)

#### 📚 연결 문서

- [android-boot-flow](01_inbox/mobile/android/01_system_internals/boot-and-runtime/android-boot-flow.md) - Zygote 가 시작되는 시점
- [android-binder-and-ipc](01_inbox/mobile/android/01_system_internals/ipc-and-process/android-binder-and-ipc.md) - AMS 가 Zygote 에게 fork 요청을 보내는 통로
- [android-process-and-memory](01_inbox/mobile/android/01_system_internals/ipc-and-process/android-process-and-memory.md) - 프로세스별 메모리 구조
