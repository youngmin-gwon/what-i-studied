# APK/AAB (Android Package / Android App Bundle)

상위 노트: [[android-glossary]]

**정의**: 안드로이드 앱 배포 형식

**상세**:

- **APK**: 모든 리소스/코드를 포함한 단일 파일
- **AAB**: Play Store 가 기기별로 최적화된 APK 생성

**차이**:

```
APK (50MB):
  └─ 모든 기기용 리소스/라이브러리

AAB → Play Store → Split APKs (30MB):
  ├─ base.apk (공통)
  ├─ arm64.apk (기기 CPU)
  └─ xxxhdpi.apk (화면 밀도)
```

**명령어**:

```bash
# APK 설치
adb install app.apk

# AAB 빌드
./gradlew bundleRelease
```

---
