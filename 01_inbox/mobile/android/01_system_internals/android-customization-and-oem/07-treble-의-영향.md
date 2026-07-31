# Treble 의 영향

상위 노트: [[android-customization-and-oem]]

### Before Treble (Android 7.x)

```
/system
├─ framework
├─ vendor 코드 섞임
└─ HAL 구현 섞임
```

업데이트 시 vendor 코드 재빌드 필요 → 지연

### After Treble (Android 8.0+)

```
/system  (Google, 독립 업데이트)
/vendor  (OEM/Chipset, 고정)
```

**VINTF**로 호환성 보장:

```xml
<!-- /vendor/etc/vintf/manifest.xml -->
<hal>
    <name>android.hardware.camera.provider</name>
    <version>2.4</version>
</hal>
```

**이점**:

- Google 이 /system 만 업데이트 가능
- OEM 작업 최소화
- 업데이트 빨라짐

---
