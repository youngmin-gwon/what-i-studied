# Graphics & Media Pipeline #android #android/graphics #android/media

화면에 그림을 띄우고 소리를 재생하는 길을 쉽게 정리했다. 용어는 [[android-glossary]].

## 화면이 그려지는 길
- 앱(UI Toolkit/Compose/View)이 버퍼를 만든다.
- RenderThread/Skia가 GPU 친화적으로 꾸민다.
- BufferQueue를 통해 SurfaceFlinger로 보내고, SurfaceFlinger가 HWC와 함께 최종 합성한다.
- VSync/Choreographer가 타이밍을 맞춰 끊김을 줄인다.

## Compose와 View
- Compose는 선언형 UI, View는 전통적인 트리 구조. 둘 다 같은 렌더 경로를 쓴다.
- ComposeView/AndroidView로 서로 섞어 쓸 수 있다. 느려지면 재구성이 자주 일어나는지 확인한다.

## 그래픽 메모리
- gralloc/DMABuf로 큰 버퍼를 공유한다. 복사를 줄여 속도와 배터리를 아낀다.
- 보호된 콘텐츠(드라마/영화 DRM)는 안전한 경로로만 렌더링한다.

## 입력과 렌더링
- InputDispatcher가 포커스 창에 이벤트를 준다.
- Choreographer가 “입력→애니메이션→그리기→합성” 순서를 일정하게 반복한다.

## 카메라·미디어 캡처
- Camera HAL3가 요청/응답으로 버퍼를 주고받는다. MediaCodec이 인코딩해 저장/스트리밍한다.
- 권한(카메라/마이크/저장소)과 [[android-glossary#scoped-storage|Scoped Storage]] 규칙을 따른다.

## 미디어 재생
- ExoPlayer가 스트리밍(DASH/HLS)과 로컬 재생을 맡는다.
- AudioTrack/AAudio/Oboe가 소리를 낸다. AudioFocus로 앱끼리 소리 충돌을 피한다.
- DRM은 MediaDrm으로 키를 받아 안전하게 디코딩한다.

## 디버깅
- `dumpsys SurfaceFlinger/gfxinfo`로 프레임 지연을 본다.
- `dumpsys media.audio_flinger/audio_policy/media.codec`으로 오디오/코덱 상태를 확인한다.
- Perfetto/AGI로 GPU·미디어 타임라인을 살핀다.

## 더 보기
[[android-binder-and-ipc]](버퍼 전달), [[android-adb-and-images]](트레이스 수집), [[android-evolution-history]](그래픽·미디어 변화).
