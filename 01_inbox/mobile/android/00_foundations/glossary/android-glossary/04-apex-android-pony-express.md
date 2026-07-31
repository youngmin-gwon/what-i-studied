# APEX (Android Pony EXpress)

상위 노트: [android-glossary](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md)

**정의**: 모듈식 시스템 컴포넌트 업데이트 형식

**상세**:

Android 10 부터 도입되어 시스템 모듈을 APK 처럼 Google Play 를 통해 업데이트할 수 있다. ART, Media, NetworkStack 등 핵심 모듈이 APEX 로 제공된다.

**예시**:

```bash
# APEX 모듈 확인
adb shell pm list packages -apex

# 출력:
# com.android.media
# com.android.wifi
# com.android.runtime
```

**구조**:

```
/apex/com.android.media@330000000/
├─ lib64/
├─ bin/
└─ apex_manifest.json
```

**관련**: [android-customization-and-oem](01_inbox/mobile/android/01_system_internals/platform-customization/android-customization-and-oem.md)

---
