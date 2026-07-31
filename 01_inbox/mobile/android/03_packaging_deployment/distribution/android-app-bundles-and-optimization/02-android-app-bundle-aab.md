# Android App Bundle (.aab)

구글 플레이에 제출하는 단일 아티팩트이지만, 내부적으로는 모든 리소스가 포함된 메타 구조체이다. 구글 플레이는 이를 분석하여 언어별, 이미지 해상도별, CPU 아키텍처별로 **Split APK**를 생성해 각 사용자에게 배포한다.

**장점:**

- 바이너리 용량 감소 (평균 20~30%)
- Unused Code 제거 (Proguard/R8 연계)
- 보안 강화 (Play App Signing 필수)
