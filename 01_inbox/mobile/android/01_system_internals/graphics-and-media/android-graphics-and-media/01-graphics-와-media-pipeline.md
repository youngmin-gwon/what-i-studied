# Graphics 와 Media Pipeline

상위 노트: [android-graphics-and-media](01_inbox/mobile/android/01_system_internals/graphics-and-media/android-graphics-and-media.md)

안드로이드의 그래픽 시스템은 **하드웨어 가속 렌더링**과 **다층 합성**을 통해 부드러운 60fps(또는 90/120fps) 화면을 제공한다. Media Framework 는 카메라 캡처부터 비디오 재생까지 담당한다.

### 왜 복잡한 그래픽 파이프라인이 필요한가

#### 모바일 그래픽의 도전

**데스크톱**:

- 단일 앱의 전체 화면
- GPU 리소스 독점
- 60Hz 고정

**모바일**:

- 여러 앱 레이어 (상태바, 네비게이션, 플로팅 윈도우, 키보드)
- 제한된 GPU/배터리
- 다양한 화면 주사율 (60/90/120Hz)
- 터치 지연 최소화 필요

**해결**: 하드웨어 기반 다층 합성

---
