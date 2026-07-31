# Surface / SurfaceFlinger

상위 노트: [android-glossary](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md)

**정의**: 화면에 표시될 픽셀 데이터를 담는 원시 버퍼

**상세**:

- **Surface**: 앱 (Producer) 이 그림을 그리는 도화지. 텍스처나 비트맵 데이터가 들어있습니다.
- **SurfaceFlinger**: 여러 앱의 Surface 들을 수거해서 물리적 디스플레이에 최종 합성 (Composition) 하는 시스템 서비스입니다.
- **BufferQueue**: Surface 와 SurfaceFlinger 사이의 파이프라인. (Producer -> Buffer -> Consumer)

**구조**:

```
App (Canvas/OpenGL) -> Surface -> BufferQueue -> SurfaceFlinger -> Hardware Composer -> Display
```

**관련**: [android-graphics-and-media](01_inbox/mobile/android/01_system_internals/graphics-and-media/android-graphics-and-media.md)

---
