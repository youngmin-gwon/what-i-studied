# Runtime Resource Overlay (RRO)

상위 노트: [android-customization-and-oem](01_inbox/mobile/android/01_system_internals/platform-customization/android-customization-and-oem.md)

### Static Overlay

빌드 시 리소스 교체:

```xml
<!-- AOSP: frameworks/base/core/res/res/values/colors.xml -->
<color name="system_accent">@color/google_blue</color>

<!-- OEM Overlay: vendor/overlay/framework/res/values/colors.xml -->
<color name="system_accent">@color/samsung_blue</color>
```

**빌드 결과**: OEM 색상으로 교체됨

### Dynamic Overlay (Android 10+)

런타임에 교체:

```bash
# Overlay 목록
adb shell cmd overlay list

# 활성화
adb shell cmd overlay enable com.example.overlay

# 비활성화
adb shell cmd overlay disable com.example.overlay
```

**사용 예**:

- 테마 변경 (다크 모드)
- 폰트 변경
- 아이콘 스타일

---
