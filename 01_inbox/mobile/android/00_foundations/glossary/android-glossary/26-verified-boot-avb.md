# Verified Boot (AVB)

상위 노트: [android-glossary](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md)

**정의**: 부팅 이미지의 무결성을 검증하는 메커니즘

**상세**:

부트로더가 vbmeta 를 검증하고, vbmeta 가 system/vendor 파티션을 검증한다. 변조된 이미지는 부팅이 차단되거나 경고가 표시된다.

**검증 체인**:

```
OEM Key (eFuse) 
  → vbmeta.img
    → boot.img
    → system.img (dm-verity)
    → vendor.img (dm-verity)
```

**상태**:

```
Green:  OEM key 검증됨 (정상)
Yellow: User key 검증됨 (커스텀 ROM)
Orange: Bootloader unlocked (경고)
Red:    검증 실패 (부팅 차단)
```

**확인**:

```bash
adb shell getprop ro.boot.verifiedbootstate

# green / yellow / orange / red
```

**관련**: [android-security-sandbox](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/android-security-sandbox.md), [android-boot-flow](01_inbox/mobile/android/01_system_internals/boot-and-runtime/android-boot-flow.md)

---

### W
