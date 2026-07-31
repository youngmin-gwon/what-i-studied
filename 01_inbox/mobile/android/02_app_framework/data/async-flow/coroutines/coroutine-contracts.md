# Coroutine Contracts

- [Coroutine은 thread가 아니라 취소 가능한 경량 작업이다](01_inbox/mobile/android/02_app_framework/data/async-flow/coroutines/coroutine-is-lightweight-cancellable-work-not-thread.md)
- [suspend 함수는 thread가 아니라 coroutine을 멈춘다](01_inbox/mobile/android/02_app_framework/data/async-flow/coroutines/suspend-function-suspends-coroutine-without-blocking-thread.md)
- [Structured concurrency는 부모 scope가 자식 작업의 수명을 소유하게 한다](01_inbox/mobile/android/02_app_framework/data/async-flow/coroutines/structured-concurrency-parent-owns-child-lifetime.md)
- [Dispatcher는 실행 위치를 고르고 Scope는 작업 수명을 소유한다](01_inbox/mobile/android/02_app_framework/data/async-flow/coroutines/dispatcher-selects-execution-context-not-work-lifetime.md)
- [Coroutine 예외 전파는 builder와 supervision boundary가 결정한다](01_inbox/mobile/android/02_app_framework/data/async-flow/coroutines/exception-propagation-needs-supervision-boundary.md)
- [병렬 Coroutine은 부모 scope와 실패 정책을 먼저 정해야 한다](01_inbox/mobile/android/02_app_framework/data/async-flow/coroutines/parallel-coroutines-need-explicit-parent-and-failure-policy.md)
