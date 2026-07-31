# OEM 주요 커스터마이징

상위 노트: [[android-customization-and-oem]]

### Samsung One UI

**주요 변경**:

1. **UI 재디자인**:
   - 큰 헤더 (한 손 조작)
   - 둥근 모서리
   - 커스텀 아이콘

2. **추가 기능**:
   - Edge Panel
   - Bixby
   - DeX (데스크톱 모드)
   - Good Lock (고급 커스터마이징)

3. **시스템 수정**:
   - Permission Monitor
   - Game Launcher / Game Booster
   - Secure Folder (Knox 기반)

**구현**:

```java
// frameworks/base 수정
// SystemUI 완전 재작성
// Settings 앱 재작성
```

### Xiaomi MIUI

**특징**:

- iOS 스타일 디자인
- 광고 내장 (일부 지역)
- MIUI 최적화 (배터리, 성능)
- 테마 스토어

### Google Pixel

**추가 기능**:

- Pixel Launcher
- Call Screen (전화 스크리닝)
- Now Playing (음악 인식)
- Magic Eraser (사진 편집)

**구현**: APK 형태로 추가 (AOSP 는 수정 최소화)

---
