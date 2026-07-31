# VSync 와 Choreographer

상위 노트: [android-graphics-and-media](01_inbox/mobile/android/01_system_internals/graphics-and-media/android-graphics-and-media.md)

### VSync

디스플레이 수직 동기화 신호 (60Hz = 16.67ms 마다):

```
VSync ───┬───┬───┬───┬───→ 시간
         │   │   │   │
       Frame Frame Frame
```

**문제 (VSync 없이)**:

```
GPU가 화면 업데이트 중간에 버퍼 교체
→ Screen Tearing (화면 찢어짐)
```

### Choreographer

```kotlin
Choreographer.getInstance().postFrameCallback { frameTimeNanos ->
    // 입력 처리
    processInput()
    
    // 애니메이션
    updateAnimations(frameTimeNanos)
    
    // 레이아웃 측정
    measure()
    layout()
    
    // 그리기
    draw()
    
    // 다음 프레임 예약
    post FrameCallback(this)
}
```

**프레임 파이프라인**:

```
Input → Animation → Measure/Layout → Draw → (다음 VSync) → Display
  2ms      2ms           4ms           6ms        16ms
```

---
