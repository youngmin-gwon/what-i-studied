# OEM Customization 과 AOSP

상위 노트: [android-customization-and-oem](01_inbox/mobile/android/01_system_internals/platform-customization/android-customization-and-oem.md)

안드로이드는 **오픈소스**(AOSP)이지만, 실제 출시되는 기기는 각 제조사(OEM)가 커스터마이징한다. Samsung 의 One UI, Xiaomi 의 MIUI, Google 의 Pixel Experience 는 모두 AOSP 를 기반으로 하지만 매우 다른 경험을 제공한다.

### 왜 OEM Customization 이 필요한가

#### AOSP 의 한계

**AOSP (Android Open Source Project)**:

- Google 이 공개하는 기본 안드로이드
- Google Play Services **없음**
- 기본 앱만 포함 (전화, 메시지, 설정 등)
- 하드웨어 드라이버 없음

**OEM 이 해야 할 일**:

1. 하드웨어 지원 (칩셋, 카메라, 센서 등)
2. Google 인증 (GMS, CTS, VTS)
3. 차별화된 기능
4. 지역별 요구사항 (통신사, 규제)

---
