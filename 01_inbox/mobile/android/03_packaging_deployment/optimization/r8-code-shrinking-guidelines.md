# R8 컴파일러 & 코드 최적화(Code Shrinking) 가이드

## 원자 노트

### 개요
- [r8-code-shrinking-guidelines-00-개요](01_inbox/mobile/android/03_packaging_deployment/optimization/r8-code-shrinking-guidelines/r8-code-shrinking-guidelines-00-%EA%B0%9C%EC%9A%94.md)

### 1. R8 컴파일러의 5대 핵심 기능
- [01-r8-컴파일러의-5대-핵심-기능](01_inbox/mobile/android/03_packaging_deployment/optimization/r8-code-shrinking-guidelines/01-r8-%EC%BB%B4%ED%8C%8C%EC%9D%BC%EB%9F%AC%EC%9D%98-5%EB%8C%80-%ED%95%B5%EC%8B%AC-%EA%B8%B0%EB%8A%A5.md)

### 2. R8 Full Mode vs Compatibility Mode
- [02-r8-full-mode-vs-compatibility-mode](01_inbox/mobile/android/03_packaging_deployment/optimization/r8-code-shrinking-guidelines/02-r8-full-mode-vs-compatibility-mode.md)

### 3. Kotlin & Compose 환경에서의 R8 극대화 지침
- [03-kotlin-compose-환경에서의-r8-극대화-지침](01_inbox/mobile/android/03_packaging_deployment/optimization/r8-code-shrinking-guidelines/03-kotlin-compose-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C%EC%9D%98-r8-%EA%B7%B9%EB%8C%80%ED%99%94-%EC%A7%80%EC%B9%A8.md)

### 4. Gradle 프로젝트 설정 (`app/build.gradle.kts`)
- [04-gradle-프로젝트-설정-app-build-gradle-kts](01_inbox/mobile/android/03_packaging_deployment/optimization/r8-code-shrinking-guidelines/04-gradle-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%84%A4%EC%A0%95-app-build-gradle-kts.md)

### 5. R8 프로가드 규칙 (`proguard-rules.pro`) 작성 모범 사례
- [05-r8-프로가드-규칙-proguard-rules-pro-작성-모범-사례](01_inbox/mobile/android/03_packaging_deployment/optimization/r8-code-shrinking-guidelines/05-r8-%ED%94%84%EB%A1%9C%EA%B0%80%EB%93%9C-%EA%B7%9C%EC%B9%99-proguard-rules-pro-%EC%9E%91%EC%84%B1-%EB%AA%A8%EB%B2%94-%EC%82%AC%EB%A1%80.md)

### 6. R8 결과물 분석 및 디버깅 툴링
- [06-r8-결과물-분석-및-디버깅-툴링](01_inbox/mobile/android/03_packaging_deployment/optimization/r8-code-shrinking-guidelines/06-r8-%EA%B2%B0%EA%B3%BC%EB%AC%BC-%EB%B6%84%EC%84%9D-%EB%B0%8F-%EB%94%94%EB%B2%84%EA%B9%85-%ED%88%B4%EB%A7%81.md)

### 7. Profile-Guided R8 최적화 및 Android Studio 툴링연동
- [07-profile-guided-r8-최적화-및-android-studio-툴링연동](01_inbox/mobile/android/03_packaging_deployment/optimization/r8-code-shrinking-guidelines/07-profile-guided-r8-%EC%B5%9C%EC%A0%81%ED%99%94-%EB%B0%8F-android-studio-%ED%88%B4%EB%A7%81%EC%97%B0%EB%8F%99.md)

### 8. Google Play Console 연동 및 실서비스 모니터링 (App Size & Vitals)
- [08-google-play-console-연동-및-실서비스-모니터링-app-size-vitals](01_inbox/mobile/android/03_packaging_deployment/optimization/r8-code-shrinking-guidelines/08-google-play-console-%EC%97%B0%EB%8F%99-%EB%B0%8F-%EC%8B%A4%EC%84%9C%EB%B9%84%EC%8A%A4-%EB%AA%A8%EB%8B%88%ED%84%B0%EB%A7%81-app-size-vitals.md)
