---
title: SurfaceFlinger는 보이는 레이어를 HWC와 함께 합성한다
tags: [android, android/graphics, android/system-service]
aliases: [SurfaceFlinger]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

# SurfaceFlinger는 보이는 레이어를 HWC와 함께 합성한다

SurfaceFlinger는 현재 보이는 Surface 레이어들을 받아 최종 display frame으로 합성하는 시스템 서비스다. 앱의 윈도우, 시스템 UI, 동영상 Surface, wallpaper 같은 레이어는 z-order, visible region, transform, alpha 같은 상태를 가진다.

SurfaceFlinger는 모든 합성을 직접 GPU로만 처리하지 않는다. Hardware Composer(HWC)와 협력해 어떤 레이어는 display hardware overlay로 넘기고, 어떤 레이어는 GPU client composition으로 합친다.

이 결정은 기기의 overlay plane 수, 회전·스케일·블렌딩 제한, protected buffer 여부, 전력 상태에 영향을 받는다. 그래서 “레이어가 많으면 항상 느리다”보다 “기기가 HWC로 처리할 수 없는 조합이면 GPU 합성이 늘 수 있다”가 더 정확하다.

앱 개발자는 SurfaceFlinger를 직접 제어하기보다 레이어 수, TextureView/SurfaceView 선택, overdraw, animation, video surface 구성을 통해 간접적으로 합성 비용에 영향을 준다.

관련 노트: [Hardware Composer는 기기 제약 안에서 합성을 offload한다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/hardware-composer-offloads-composition-under-device-constraints.md), [DRM 보호 미디어는 secure codec과 보호된 출력 경로를 요구할 수 있다](01_inbox/mobile/android/01_system_internals/graphics-and-media/graphics-media-contracts/drm-protected-media-needs-secure-codec-and-output-path.md)

근거: [AOSP SurfaceFlinger, Hardware Composer, and virtual displays](https://source.android.com/docs/core/graphics)
