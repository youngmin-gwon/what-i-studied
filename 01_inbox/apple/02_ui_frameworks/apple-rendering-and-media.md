---
title: apple-rendering-and-media
tags: [apple, graphics, metal, coreanimation, rendering, internals, animation]
aliases: []
date modified: 2025-12-18 02:00:00 +09:00
date created: 2025-12-16 16:09:09 +09:00
---

## Rendering, Metal, and Animation

Apple 기기의 화면이 왜 그렇게 부드러운지(Smooth), 그리고 어떻게 그 부드러움을 유지할 수 있는지 기술적으로 분석합니다.
Core Animation 파이프라인에서 시작해, Metal로 가속되는 렌더링, 그리고 사용자가 느끼는 애니메이션 감각까지 **"픽셀이 눈에 보이기까지"**의 여정입니다.

### 💡 왜 이것을 알아야 하나요? (Why it matters)
- **60fps (ProMotion 120fps) 방어**: 스크롤이 버벅거린다면, 범위는 둘 중 하나입니다. **CPU가 늦게 커밋했거나(Layout/Prepare)**, **GPU가 합성을 힘들어하거나(Offscreen)**.
- **배터리 수명**: 불필요한 리드로우(Redraw)는 GPU를 깨우고 배터리를 갉아먹습니다. `drawRect`를 함부로 쓰면 안 되는 이유입니다.
- **Zero-copy**: 카메라 영상에 필터를 입힐 때, 메모리 복사 없이(Pointer만 전달) 처리해야 발열을 잡을 수 있습니다 (`CVPixelBuffer`).

---

### 🎨 Core Animation Pipeline

화면에 픽셀이 그려지기까지의 여정은 크게 4단계(Layout, Display, Prepare, Commit)로 나뉩니다.

#### 1. App Process (CPU)
앱 내부에서 일어나는 일입니다.
1.  **Layout**: `layoutSubviews`가 호출되어 뷰의 프레임이 결정됩니다.
2.  **Display**: `drawRect` (혹은 backing image 설정)가 실행됩니다. Core Graphics (`CGContext`)를 쓰면 여기서 비트맵이 생성됩니다.
3.  **Prepare**: 이미지 디코딩, 폰트 래스터화 등이 일어납니다.
4.  **Commit**: 변경된 레이어 트리(Layer Tree)를 IPC를 통해 **Render Server**로 전송합니다. 이 단계가 무거우면 프레임 드랍이 발생합니다.

#### 2. Render Server (GPU)
iOS에서는 `backboardd`, macOS에서는 `WindowServer` 프로세스가 담당합니다.
1.  **Decode**: 받은 레이어 트리를 디코딩합니다.
2.  **Draw Calls**: OpenGL/Metal 명령으로 변환하여 GPU에 커밋합니다.
3.  **Render**: GPU가 텍스처를 합성(Composite)합니다.
4.  **Display**: V-Sync에 맞춰 프레임버퍼를 화면에 쏩니다.

---

### ⚠️ Performance Bottleneck (Offscreen Rendering)

GPU가 바로 화면(On-screen) 버퍼에 그리지 못하고, 임시 버퍼(Off-screen)를 만들어 그렸다가 다시 합성해야 하는 현상입니다. 컨텍스트 스위칭 비용이 매우 큽니다.

**주요 원인 및 해결책:**
- `cornerRadius` + `masksToBounds = true`: 내용물까지 잘라야 할 때 발생.
- **해결**: 미리 둥글게 잘린 이미지를 쓰거나, `shadowPath`를 사용합니다.
- `shadow`: 그림자 모양을 계산하기 위해 알파 채널을 분석해야 함.
- **해결**: `view.layer.shadowPath = UIBezierPath(rect: view.bounds).cgPath` (모양을 미리 알려줌)

---

### ⚙️ Metal Basics

Apple의 로우 레벨 3D 그래픽 API입니다. Core Animation도 내부적으로 Metal을 사용합니다.

- **Command Queue**: GPU에 보낼 명령 대기열.
- **Command Buffer**: 실제 명령(Draw Call 등)을 담는 그릇.
- **Pipeline State Object (PSO)**: 셰이더와 상태를 미리 컴파일해 둔 객체. 런타임에 만들면 느리므로 앱 시작 시 만들어야 합니다.

**성능 팁**:
- **Texture Compression**: ASTC 포맷을 적극 사용하여 대역폭을 줄이세요.
- **Triple Buffering**: CPU가 다음 프레임을 준비하는 동안 GPU가 현재 프레임을 그리게 하여 병렬성을 극대화하세요.

---

### 🎬 Animation Principles (Motion)

애니메이션은 단순히 예쁜 것이 아니라 "상태 변화를 설명하는 도구"입니다.

1.  **Response**: 사용자의 터치에 즉각 반응해야 합니다. (지연 시간 < 100ms)
2.  **Interruptibility**: 애니메이션 중 사용자가 다시 조작하면, 즉시 그 손가락을 따라가야 합니다. (additive animation, spring)
3.  **Spring Physics**: 실제 물리 법칙(질량, 강성, 감쇠)을 시뮬레이션하여 자연스러운 움직임을 만드세요. `UIView.animate(duration:...)` 대신 `UIViewPropertyAnimator`나 SwiftUI `spring`을 쓰세요.

---

### 🎞️ Media Pipeline (AVFoundation)

동영상 처리의 핵심은 **"복사하지 않는 것"**입니다.

- **CVPixelBuffer**: 이미지 데이터를 담는 컨테이너입니다.
- **Zero-copy Flow**: 카메라 -> Metal -> 인코더까지 데이터 복사 없이 메모리 주소만 넘깁니다.

### 더 보기
- [[apple-uikit-lifecycle]] - 렌더링 루프와 연동
- [[apple-instruments-profiling]] - Core Animation FPS 및 Offscreen Rendering 감지 방법
