---
title: apple-rendering-and-media
tags: [apple, apple/ui, apple/ui/rendering, coreanimation, graphics, internals, metal, rendering]
aliases: ["프레임은 앱 프로세스의 Commit 과 Render Server 의 합성이라는 두 예산으로 나뉜다", "Core Animation Pipeline", "렌더링과 Metal"]
date modified: 2026-09-03 00:00:00 +09:00
date created: 2025-12-16 16:09:09 +09:00
---

## 프레임은 앱 프로세스의 Commit 과 Render Server 의 합성이라는 두 예산으로 나뉜다

화면에 픽셀이 나오기까지의 비용은 한 덩어리가 아니다. **앱 프로세스(CPU)** 가 Layout·Display·Prepare 를 거쳐 레이어 트리를 Commit 하는 구간과, **Render Server(GPU)** 가 그 트리를 합성해 V-Sync 에 맞춰 내보내는 구간은 서로 다른 프로세스에서 일어난다. 스크롤이 버벅일 때 어느 쪽 예산을 넘겼는지 먼저 나눠야 고칠 대상이 정해진다.

### 💡 왜 이것을 알아야 하나요? (Why it matters)

- **60fps (ProMotion 120fps) 방어**: 스크롤이 버벅거린다면, 범위는 둘 중 하나입니다. **CPU 가 늦게 커밋했거나(Layout/Prepare)**, **GPU 가 합성을 힘들어하거나(Offscreen)**.
- **배터리 수명**: 불필요한 리드로우(Redraw)는 GPU 를 깨우고 배터리를 갉아먹습니다. `drawRect` 를 함부로 쓰면 안 되는 이유입니다.
- **Zero-copy**: 카메라 영상에 필터를 입힐 때, 메모리 복사 없이(Pointer 만 전달) 처리해야 발열을 잡을 수 있습니다 (`CVPixelBuffer`).

---

### 🎨 Core Animation Pipeline

화면에 픽셀이 그려지기까지의 여정은 크게 4 단계(Layout, Display, Prepare, Commit)로 나뉩니다.

#### 1. App Process (CPU)

앱 내부에서 일어나는 일입니다.

1. **Layout**: `layoutSubviews` 가 호출되어 뷰의 프레임이 결정됩니다.
2. **Display**: `drawRect` (혹은 backing image 설정)가 실행됩니다. Core Graphics (`CGContext`)를 쓰면 여기서 비트맵이 생성됩니다.
3. **Prepare**: 이미지 디코딩, 폰트 래스터화 등이 일어납니다.
4. **Commit**: 변경된 레이어 트리(Layer Tree)를 IPC 를 통해 **Render Server**로 전송합니다. 이 단계가 무거우면 프레임 드랍이 발생합니다.

#### 2. Render Server (GPU)

iOS 에서는 `backboardd`, macOS 에서는 `WindowServer` 프로세스가 담당합니다.

1. **Decode**: 받은 레이어 트리를 디코딩합니다.
2. **Draw Calls**: OpenGL/Metal 명령으로 변환하여 GPU 에 커밋합니다.
3. **Render**: GPU 가 텍스처를 합성(Composite)합니다.
4. **Display**: V-Sync 에 맞춰 프레임버퍼를 화면에 쏩니다.

---

### ⚠️ Performance Bottleneck (Offscreen Rendering)

GPU 가 바로 화면(On-screen) 버퍼에 그리지 못하고, 임시 버퍼(Off-screen)를 만들어 그렸다가 다시 합성해야 하는 현상입니다. 컨텍스트 스위칭 비용이 매우 큽니다.

**주요 원인 및 해결책:**

- `cornerRadius` + `masksToBounds = true`: 내용물까지 잘라야 할 때 발생.
- **해결**: 미리 둥글게 잘린 이미지를 쓰거나, `shadowPath` 를 사용합니다.
- `shadow`: 그림자 모양을 계산하기 위해 알파 채널을 분석해야 함.
- **해결**: `view.layer.shadowPath = UIBezierPath(rect: view.bounds).cgPath` (모양을 미리 알려줌)

---

### ⚙️ Metal Basics

Apple 의 로우 레벨 3D 그래픽 API 입니다. Core Animation 도 내부적으로 Metal 을 사용합니다.

- **Command Queue**: GPU 에 보낼 명령 대기열.
- **Command Buffer**: 실제 명령(Draw Call 등)을 담는 그릇.
- **Pipeline State Object (PSO)**: 셰이더와 상태를 미리 컴파일해 둔 객체. 런타임에 만들면 느리므로 앱 시작 시 만들어야 합니다.

**성능 팁**:

- **Texture Compression**: ASTC 포맷을 적극 사용하여 대역폭을 줄이세요.
- **Triple Buffering**: CPU 가 다음 프레임을 준비하는 동안 GPU 가 현재 프레임을 그리게 하여 병렬성을 극대화하세요.

---

### 관찰 가능한 증거

```
Xcode Debug 메뉴 > Core Animation
  Color Offscreen-Rendered Yellow   → 추가 렌더 패스 발생 영역
  Color Blended Layers              → 오버드로 영역

Instruments
  Animation Hitches   → commit 구간 vs render 구간 분리
  Metal System Trace  → GPU 실제 작업 시간과 렌더 패스 수
  Time Profiler       → CA::Transaction::commit 아래 스택
```

먼저 **어느 구간이 마감을 넘겼는지** 확정한 뒤 처방을 고른다. → [07 런북](../00_foundations/diagnostic-runbooks/07-scroll-hitches.md)

### 더 보기

- [apple-uikit-lifecycle](apple-uikit-lifecycle.md) - 렌더링 루프와 연동
- [apple-animation-and-motion](apple-animation-and-motion.md) - 애니메이션 원칙과 인터럽트 가능한 모션
- [apple-media-pipeline-deep](apple-media-pipeline-deep.md) - AVFoundation 캡처/재생 파이프라인과 zero-copy
- [apple-instruments-profiling](../06_testing_performance/apple-instruments-profiling.md) - Core Animation FPS 및 Offscreen Rendering 감지 방법
- [apple-graphics-and-media](../01_system_internals/graphics-and-media/apple-graphics-and-media.md) - Render Server 이하의 합성 내부
- [Offscreen 렌더링은 추가 패스와 컨텍스트 전환을 강제한다](../01_system_internals/graphics-and-media/offscreen-rendering-cost.md)

공식 문서: [Core Animation](https://developer.apple.com/documentation/quartzcore) · [Metal](https://developer.apple.com/documentation/metal)
