# OTA (Over-The-Air)

상위 노트: [[android-glossary]]

**정의**: 무선으로 시스템 업데이트를 전송하는 방식

**상세**:

사용자가 Wi-Fi 를 통해 업데이트를 다운로드하고 설치한다. A/B 업데이트는 백그라운드에서 설치하고 재부팅 시 교체하여 중단 없는 업데이트를 제공한다.

**방식**:

```
Full OTA: 전체 시스템 이미지
Incremental OTA: 변경된 부분만

A/B Seamless:
  Slot A (현재) + Slot B (업데이트) → 재부팅 시 교체
```

**확인**:

```bash
# 현재 슬롯
adb shell getprop ro.boot.slot_suffix

# 출력: _a 또는 _b
```

**관련**: [[android-boot-flow]], [[android-customization-and-oem]]

---

### P
