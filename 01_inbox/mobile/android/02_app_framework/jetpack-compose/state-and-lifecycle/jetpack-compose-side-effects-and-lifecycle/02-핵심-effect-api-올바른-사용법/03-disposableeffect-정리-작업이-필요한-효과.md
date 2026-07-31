# `DisposableEffect` (정리 작업이 필요한 효과)
* **목적**: 컴포저블이 화면에 나타나고 사라질 때(Composition 진입 및 소멸) 자원 등록 및 해제 쌍을 안전하게 관리합니다.
* **동작**: 블록이 실행된 후, 마지막 줄에 반드시 `onDispose` 블록을 정의하여 정리 작업을 작성해야 합니다. `key`가 변경되면 기존 작업을 해제(`onDispose`)하고 새로 다시 등록합니다.
* **주요 사용처**: 리스너(Listener) 등록 및 해제, SDK 초기화 및 정리, 센서 모니터링 시작 및 중단.

```kotlin
@Composable
fun SensorMonitor(sensorManager: SensorManager) {
    DisposableEffect(sensorManager) {
        val listener = SensorEventListener { /* 센서 데이터 처리 */ }
        sensorManager.registerListener(listener, ...)

        // 컴포저블이 화면에서 제거되거나 sensorManager가 바뀔 때 실행
        onDispose {
            sensorManager.unregisterListener(listener)
        }
    }
}
```

---
