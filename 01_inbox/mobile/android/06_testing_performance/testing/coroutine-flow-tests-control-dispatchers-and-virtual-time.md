# Coroutine과 Flow 테스트는 dispatcher와 virtual time을 통제해야 한다

Coroutine/Flow 테스트는 실제 background thread와 실제 delay에 의존하면 flaky해진다. `runTest`는 test scope와 scheduler를 제공하고, `TestDispatcher`는 새 coroutine 실행 순서와 virtual time을 통제하게 한다.

Code under test가 dispatcher를 직접 고정하면 테스트가 제어할 수 없다. dispatcher나 scope를 DI로 주입하고, 테스트에서는 `StandardTestDispatcher`, `UnconfinedTestDispatcher`, `Dispatchers.Main` replacement를 상황에 맞게 사용한다.

여러 `TestDispatcher`를 만들더라도 같은 `TestCoroutineScheduler`를 공유해야 시간 인식이 어긋나지 않는다. `advanceUntilIdle` 같은 virtual-time 제어는 pending coroutine과 Flow emission assertion을 결정적으로 만든다.

공식 문서: [Testing Kotlin coroutines on Android](https://developer.android.com/kotlin/coroutines/test)
