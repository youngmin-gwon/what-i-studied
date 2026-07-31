# START/STOP 또는 RESUME/PAUSE에 맞춘 작업

상위 노트: [jetpack-compose-state-lifetime-api-selection](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection.md)

데이터를 화면에 그리기 위한 Flow 수집이 아니라, lifecycle 상태에 맞춰 외부 리소스를 시작/정리해야 하면 lifecycle-aware effect를 씁니다.

START/STOP에 맞춘 작업:

```kotlin
@Composable
fun LocationUpdates(
    locationClient: LocationClient,
) {
    LifecycleStartEffect(locationClient) {
        locationClient.start()

        onStopOrDispose {
            locationClient.stop()
        }
    }
}
```

RESUME/PAUSE에 맞춘 작업:

```kotlin
@Composable
fun CameraPreview(
    camera: CameraController,
) {
    LifecycleResumeEffect(camera) {
        camera.resume()

        onPauseOrDispose {
            camera.pause()
        }
    }
}
```

선택 기준:

- 화면이 보이는 동안만 필요하면 START/STOP
- 사용자가 실제로 상호작용 가능한 foreground 상태에서만 필요하면 RESUME/PAUSE
- 단순 화면 state Flow 수집이면 `collectAsStateWithLifecycle()`

---
