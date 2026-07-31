# SurfaceFlinger

모든 레이어를 합성:

```
Layer Stack:
  [Status Bar]       Z-order: 100
  [Navigation Bar]            90
  [App Window]                50
  [Wallpaper]                 10
```

**합성 방법**:

1. **GPU Composition**: OpenGL 로 모든 레이어 합성
2. **HWC Overlay**: 하드웨어가 직접 합성 (전력 절약)

```cpp
// SurfaceFlinger.cpp
void SurfaceFlinger::composite() {
    for (Layer* layer : layers) {
        if (hwc->canUseOverlay(layer)) {
            hwc->setLayerBuffer(layer);  // 하드웨어 오버레이
        } else {
            gpu->compositeLayer(layer);  // GPU 합성
        }
    }
}
```

---
