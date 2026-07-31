# Jetpack Compose 접근성 가이드라인 (Accessibility: a11y)

이 문서는 Android 앱을 모든 사용자(시각, 청각, 운동 능력 또는 인지 장애가 있는 사용자 포함)가 장벽 없이 사용할 수 있도록 Jetpack Compose에서 제공하는 **접근성(Accessibility, 줄여서 a11y)** 관련 핵심 API와 모범 설계 패턴을 설명합니다.

본 문서는 Google의 [Accessibility in Jetpack Compose Codelab](https://developer.android.com/codelabs/jetpack-compose-accessibility)의 핵심 실무 학습 단계를 바탕으로 구성되었습니다.

---

---

## 원자 노트

- [접근성을 챙겨야 하는 이유](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/jetpack-compose-accessibility-guidelines/01-%EC%A0%91%EA%B7%BC%EC%84%B1%EC%9D%84-%EC%B1%99%EA%B2%A8%EC%95%BC-%ED%95%98%EB%8A%94-%EC%9D%B4%EC%9C%A0.md)
- [접근성 향상을 위한 7대 핵심 실무 가이드](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/jetpack-compose-accessibility-guidelines/02-%EC%A0%91%EA%B7%BC%EC%84%B1-%ED%96%A5%EC%83%81%EC%9D%84-%EC%9C%84%ED%95%9C-7%EB%8C%80-%ED%95%B5%EC%8B%AC-%EC%8B%A4%EB%AC%B4-%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- [고급 접근성 제어: 탐색 순서 및 Semantics 재정의](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/jetpack-compose-accessibility-guidelines/03-%EA%B3%A0%EA%B8%89-%EC%A0%91%EA%B7%BC%EC%84%B1-%EC%A0%9C%EC%96%B4-%ED%83%90%EC%83%89-%EC%88%9C%EC%84%9C-%EB%B0%8F-semantics-%EC%9E%AC%EC%A0%95%EC%9D%98.md)
- [Android 플랫폼 접근성 핵심 4대 원칙 (Principles for Accessibility)](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/jetpack-compose-accessibility-guidelines/04-android-%ED%94%8C%EB%9E%AB%ED%8F%BC-%EC%A0%91%EA%B7%BC%EC%84%B1-%ED%95%B5%EC%8B%AC-4%EB%8C%80-%EC%9B%90%EC%B9%99-principles-for-accessibility.md)
- [접근성 디버깅 및 테스트 방법 (a11y Testing)](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/jetpack-compose-accessibility-guidelines/05-%EC%A0%91%EA%B7%BC%EC%84%B1-%EB%94%94%EB%B2%84%EA%B9%85-%EB%B0%8F-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EB%B0%A9%EB%B2%95-a11y-testing.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
