---
title: 11-그래픽-opengl-vulkan-2016
tags: []
aliases: []
date modified: 2026-07-31 15:43:33 +09:00
date created: 2026-07-31 15:38:23 +09:00
---

## 그래픽: OpenGL → Vulkan (2016)

상위 노트: [[02-주요-기술-전환]]

**OpenGL ES** (2008- 현재):

```cpp
// High-level API
glClear(GL_COLOR_BUFFER_BIT);
glDrawArrays(GL_TRIANGLES, 0, 3);
```

**문제**:

- 드라이버 오버헤드
- 멀티스레드 어려움

**Vulkan** (Android 7.0, 2016):

```cpp
// Low-level API
vkCmdBeginRenderPass(...);
vkCmdBindPipeline(...);
vkCmdDraw(...);
vkCmdEndRenderPass(...);
```

**장점**:

- CPU 오버헤드 50% 감소
- 멀티스레드 네이티브 지원
- 더 나은 제어

**현재**:

- OpenGL 은 ANGLE 로 Vulkan 위에서 실행
- 게임/고성능: Vulkan 직접 사용
