# Canvas / Skia

```kotlin
// Custom View
override fun onDraw(canvas: Canvas) {
    canvas.drawRect(0f, 0f, 100f, 100f, paint)
    canvas.drawText("Hello", 50f, 50f, textPaint)
}
```

**Skia**:

- 2D 그래픽 라이브러리
- GPU 가속 (OpenGL/Vulkan 백엔드)
- Chrome 도 사용하는 검증된 엔진
