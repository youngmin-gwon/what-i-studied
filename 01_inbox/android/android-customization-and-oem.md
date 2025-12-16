---
title: android-customization-and-oem
tags: [android, android/customization, android/oem, aosp]
aliases: []
date modified: 2025-12-16 16:02:59 +09:00
date created: 2025-12-16 15:25:24 +09:00
---

## Customization & OEM Workflows android android/oem android/customization aosp

제조사가 AOSP 를 제품으로 만들 때 건드리는 부분을 쉽게 정리했다. 용어는 [[android-glossary]].

### AOSP→제품
- AOSP 코드 위에 device/vendor/odm 트리를 얹어 기기별 설정과 HAL 을 넣는다.
- CTS/VTS/GTS 등 호환성 테스트를 통과해야 한다.
- system_ext/product 파티션으로 SKU/통신사별 차이를 나눈다.

### 리소스 오버레이
- [[android-glossary#rro|RRO]] 로 UI 나 동작을 덮어씌워 바꾼다 (config_* 값 등).
- DeviceConfig/서버 플래그와 조합해 기능을 켜고 끌 수 있다.

### 커널/드라이버
- GKI 위에 벤더 모듈을 올린다. DTBO 로 하드웨어 차이를 반영한다.
- 전원/온도/메모리 정책을 기기 특성에 맞춰 조정한다.

### 시스템 서비스 확장
- 필수 기능은 system/privileged 앱으로 추가하고, signature 권한으로 보호한다.
- Mainline 이 늘어날수록 오버레이/플래그를 통한 변경 범위가 더 현실적이다.

### OTA 전략
- [[android-glossary#ota|A/B/Virtual A/B]] 업데이트로 중단 없는 배포를 노린다.
- 롤백/데이터 마이그레이션 계획을 함께 세운다.

### 엔터프라이즈/MDM
- DevicePolicyManager/Work Profile 로 기업 정책을 구현한다.
- Zero-touch/QR/NFC 로 프로비저닝을 자동화한다.

### 통신사/지역화
- CarrierConfig/APN/IMS 설정으로 통신사 요구를 반영한다.
- Locale/언어/규제 (EMF/SAR 등) 에 따라 기능을 조정한다.

### 빌드 타입
- user/userdebug/eng: 보안·디버그 허용 수준이 다르다. eng 는 가장 열려 있지만 제품용으로는 쓰지 않는다.

### Mainline 영향
- [[android-glossary#apex|APEX]] 모듈 (ART/Media/NetworkStack 등) 업데이트로 시스템 일부가 독립 배포된다.
- OEM 은 커널/HAL/오버레이 위주로 변경하고, 나머지는 호환성 규칙을 따른다.

### 링크

[[android-architecture-stack]], [[android-hal-and-kernel]], [[android-boot-flow]], [[android-adb-and-images]], [[android-security-and-sandboxing]].
