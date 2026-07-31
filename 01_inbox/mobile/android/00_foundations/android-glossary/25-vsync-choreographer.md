# Vsync / Choreographer

상위 노트: [[android-glossary]]

**정의**: 화면 주사율 (60Hz, 120Hz) 에 맞춰 프레임 그리기 타이밍을 맞추는 신호

**상세**:

- **Vsync (Vertical Synchronization)**: 디스플레이가 "나 이제 그릴 준비 됐어!"라고 쏘는 하드웨어 신호.
- **Choreographer**: Vsync 신호를 받아서 앱에게 "자, 다음 프레임 그려!"(`doFrame`) 라고 알려주는 지휘자.
- 만약 앱이 Vsync 주기 (16.6ms) 안에 그림을 다 못 그리면 **Jank**(버벅임) 가 발생합니다.

**흐름**:

```
Vsync 발생 -> Choreographer.onVsync() -> App.doFrame() -> Measure/Layout/Draw -> SurfaceFlinger
```

**관련**: [[android-performance-and-debug]], [[android-graphics-and-media]]

---
