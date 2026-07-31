# RenderThread

앱의 UI 스레드와 별도로 실행:

```java
// View.java
void draw(Canvas canvas) {
    // UI 스레드: View 트리 순회
    drawBackground(canvas);
    onDraw(canvas);
    dispatchDraw(canvas);  // 자식 View
    
    // → RenderThread로 전달
}
```

**RenderThread**:

- DisplayList 구축
- GPU 명령 생성
- VSync 대기
