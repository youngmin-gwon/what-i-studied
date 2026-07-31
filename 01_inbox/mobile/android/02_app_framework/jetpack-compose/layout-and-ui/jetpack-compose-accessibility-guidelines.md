# Jetpack Compose 접근성 가이드라인 (Accessibility: a11y)

이 문서는 Android 앱을 모든 사용자(시각, 청각, 운동 능력 또는 인지 장애가 있는 사용자 포함)가 장벽 없이 사용할 수 있도록 Jetpack Compose에서 제공하는 **접근성(Accessibility, 줄여서 a11y)** 관련 핵심 API와 모범 설계 패턴을 설명합니다.

본 문서는 Google의 [Accessibility in Jetpack Compose Codelab](https://developer.android.com/codelabs/jetpack-compose-accessibility)의 핵심 실무 학습 단계를 바탕으로 구성되었습니다.

---

---

## 원자 노트

- [[01-접근성을-챙겨야-하는-이유|접근성을 챙겨야 하는 이유]]
- [[02-접근성-향상을-위한-7대-핵심-실무-가이드|접근성 향상을 위한 7대 핵심 실무 가이드]]
- [[03-고급-접근성-제어-탐색-순서-및-semantics-재정의|고급 접근성 제어: 탐색 순서 및 Semantics 재정의]]
- [[04-android-플랫폼-접근성-핵심-4대-원칙-principles-for-accessibility|Android 플랫폼 접근성 핵심 4대 원칙 (Principles for Accessibility)]]
- [[05-접근성-디버깅-및-테스트-방법-a11y-testing|접근성 디버깅 및 테스트 방법 (a11y Testing)]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
