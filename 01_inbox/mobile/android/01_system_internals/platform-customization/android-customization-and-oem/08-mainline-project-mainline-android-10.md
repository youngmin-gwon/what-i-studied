# Mainline (Project Mainline, Android 10+)

상위 노트: [android-customization-and-oem](01_inbox/mobile/android/01_system_internals/platform-customization/android-customization-and-oem.md)

**APEX 모듈**로 Google Play 를 통해 시스템 컴포넌트 업데이트:

```
com.android.media            # Media 코덱
com.android.wifi             # Wi-Fi 스택
com.android.tethering        # 테더링
com.android.conscrypt        # 암호화 라이브러리
```

**확인**:

```bash
adb shell pm list packages -apex
```

**효과**:

- 보안 패치 빠름
- 버그 수정 신속
- OEM 업데이트 불필요

---
