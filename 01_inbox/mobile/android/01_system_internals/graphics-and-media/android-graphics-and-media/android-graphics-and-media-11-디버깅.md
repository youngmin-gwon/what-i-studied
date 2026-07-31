# 디버깅

상위 노트: [android-graphics-and-media](01_inbox/mobile/android/01_system_internals/graphics-and-media/android-graphics-and-media.md)

### dumpsys

```bash
# SurfaceFlinger 상태
adb shell dumpsys SurfaceFlinger

# Graphics 통계
adb shell dumpsys gfxinfo

# Media 코덱
adb shell dumpsys media.codec

# Audio
adb shell dumpsys media.audio_flinger
```

### GPU 렌더링

```bash
# 렌더링 프로파일 활성화
adb shell setprop debug.hwui.profile true

# 화면에 표시
adb shell setprop debug.hwui.profile visual_bars
```

---
