# BufferQueue

프로듀서(앱)- 컨슈머(SurfaceFlinger) 패턴:

```cpp
// 앱 쪽 (Producer)
ANativeWindow_Buffer buffer;
ANativeWindow_lock(window, &buffer, nullptr);
// buffer에 픽셀 쓰기
ANativeWindow_unlockAndPost(window);

// SurfaceFlinger 쪽 (Consumer)
acquireBuffer(&buffer);
// buffer 합성
releaseBuffer(&buffer);
```

**트리플 버퍼링**:

```
Front Buffer:  화면에 표시 중
Back Buffer 1: GPU가 렌더링 중
Back Buffer 2: CPU가 다음 프레임 준비 중
```
