---
title: Hardware Composer는 기기 제약 안에서 합성을 offload한다
tags: [android, android/graphics, android/hal]
date modified: 2026-07-31 23:20:00 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

Hardware Composer(HWC)는 display hardware가 처리할 수 있는 레이어 합성을 SurfaceFlinger에서 넘겨받는 HAL 경계다. 가능한 경우 HWC는 overlay plane을 사용해 GPU가 모든 레이어를 한 버퍼로 다시 그리는 일을 줄일 수 있다.

하지만 HWC offload는 보장된 최적화가 아니다. overlay plane 개수, 레이어 겹침, alpha blending, 회전, scaling, 색 공간, protected content, display mode에 따라 일부 또는 전체 레이어가 GPU composition으로 돌아갈 수 있다.

이 경계는 앱 코드의 API 선택과도 연결된다. 예를 들어 동영상은 SurfaceView를 쓰면 별도 레이어로 display pipeline에 더 직접 연결될 수 있지만, transform과 UI 합성 요구가 많으면 TextureView/Compose interop의 trade-off도 생긴다.

성능 결론은 구현 세부를 추측하기보다 trace와 `dumpsys SurfaceFlinger`로 실제 composition type을 확인해야 한다.

관련 노트: {link(contracts_hub / "surfaceflinger-composes-visible-layers-with-hwc.md", "SurfaceFlinger는 보이는 레이어를 HWC와 함께 합성한다")}, {link(ANDROID / "01_system_internals/kernel-and-hal/android-hal-and-kernel.md", "Android HAL and kernel")} 

근거: [AOSP Hardware Composer HAL](https://source.android.com/docs/core/graphics/hwc)
