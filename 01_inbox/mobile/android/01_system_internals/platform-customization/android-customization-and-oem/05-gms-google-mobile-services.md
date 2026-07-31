# GMS (Google Mobile Services)

상위 노트: [android-customization-and-oem](01_inbox/mobile/android/01_system_internals/platform-customization/android-customization-and-oem.md)

### GMS Core

```
com.google.android.gms (Google Play Services)
```

**포함**:

- Location Services
- Firebase Cloud Messaging
- Google Sign-In
- SafetyNet / Play Integrity
- Google Pay

**없으면**:

- 대부분의 앱 작동 불가 (FCM 의존)
- 지도 API 사용 불가
- 위치 정확도 낮아짐

### GMS 인증

OEM 이 Google 인증 받으려면:

1. **CTS (Compatibility Test Suite)** 통과
2. **VTS (Vendor Test Suite)** 통과 (Treble)
3. **GTS (GMS Test Suite)** 통과
4. 계약 체결 및 비용 지불

**인증 실패 시**:

- Play Store 없음
- GMS 없음
- "Android" 상표 사용 불가

---
