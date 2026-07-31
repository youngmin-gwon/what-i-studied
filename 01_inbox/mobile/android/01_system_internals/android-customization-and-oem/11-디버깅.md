# 디버깅

상위 노트: [[android-customization-and-oem]]

### Build Fingerprint

```bash
adb shell getprop ro.build.fingerprint

# 출력:
# samsung/galaxy/SM-G991B:13/TP1A.220624.014/G991BXXU5DVKB:user/release-keys
```

**형식**:

```
brand/product/device:version/ID/incremental:type/tags
```

### Overlay 확인

```bash
# 활성 RRO
adb shell dumpsys overlay

# 어떤 리소스가 오버라이드되었는지
adb shell dumpsys package overlays
```

### Treble 검증

```bash
# VNDK 버전
adb shell getprop ro.vndk.version

# Treble 지원 여부
adb shell getprop ro.treble.enabled
```

---
