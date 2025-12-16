---
title: apple-accessibility-and-internationalization
tags: [a11y, apple, i18n]
aliases: []
date modified: 2025-12-16 16:15:11 +09:00
date created: 2025-12-16 16:11:46 +09:00
---

## Accessibility & Internationalization apple a11y i18n

접근성과 다국어 지원을 쉽게 정리했다. 용어는 [[apple-glossary]].

### 접근성 기본
- VoiceOver: 스크린 리더. 모든 UI 요소에 접근성 라벨/힌트 제공.
- Dynamic Type: 폰트 크기 조정. Auto Layout/SwiftUI 는 자동 대응하지만 커스텀 레이아웃은 검토 필요.
- 색 대비/투명도: 색약/고대비 모드, Reduce Motion, Reduce Transparency 옵션을 존중.
- 포커스 순서: 키보드/스위치 제어로도 탐색 가능해야 한다.

### 플랫폼 별 포인트
- watchOS: 작은 화면, 손목 올림/탭틱 피드백. 음성/제스처 제어 비중 높음.
- visionOS: 시선 + 손 제스처, 오디오 큐, 공간 오브젝트의 접근성 속성 부여 필요.
- macOS: 보이스컨트롤/딕테이션, 스위치 제어, 풀 키보드 내비게이션.

### 국제화
- 지역/언어/달력/숫자/날짜 포맷을 Locale-aware API 로 처리.
- 오른쪽→왼쪽 (RTL) 레이아웃 지원. Auto Layout/SwiftUI 는 기본 지원, 커스텀 드로잉은 확인.
- 텍스트 확장 (긴 번역) 에도 UI 가 깨지지 않도록 대응.
- 단위 (섭씨/화씨, 미터/피트), 통화/숫자 포맷을 Locale 로 변환.

### 입력법/키보드
- 다국어 키보드/IME 변환, 하드웨어 키보드 단축키, 포인터/트랙패드 제스처.

### 심사와 가이드라인
- App Store 는 접근성/프라이버시 가이드를 따르는지 본다. 접근성 미지원은 거절 사유가 될 수 있다.
- Photos/Contacts 등 민감 권한 문구를 사용자 언어로 제공해야 한다.

### 테스트
- Accessibility Inspector, VoiceOver Rotor, Switch Control, Dynamic Type 변경, Reduce Motion 테스트.
- 다국어 빌드, pseudo-localization, 스냅샷 테스트로 UI 깨짐 확인.

### 링크

[[apple-app-lifecycle-and-ui]], [[apple-testing-and-quality]], [[apple-platform-differences]].
