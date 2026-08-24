---
title: deep-link
tags: [android, android/navigation, android/deep-links]
aliases: ["Deep Link 계약", "Deep Link Contracts"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Deep Link 계약 (Deep Link Contracts)

외부 입력 URI를 수신하여 앱 내부 목적지로 라우팅하고, 도메인 검증 및 백스택 생성을 안전하게 처리하기 위한 딥링크 아키텍처 계약 모음이다.

---

### 핵심 계약 가이드라인

1. **App Link 보안 및 검증 계약**:
   - 커스텀 스키마(`myapp://`)의 하이재킹 위험성을 배제하고, `https` 기반 도메인 소유권 검증(`assetlinks.json`)이 완료된 **Android App Links**를 우선 적용한다.
2. **외부 URI 신뢰 경계 검증 계약**:
   - 외부 URI 파라미터는 검증되지 않은 외부 입력이므로 파싱 후 타당성 검증(Sanitization)을 거쳐 `NavKey`로 전환해야 한다.
3. **인증 및 합성 백스택(Synthetic Back Stack) 계약**:
   - 딥링크 진입 시 사용자 인증이 필요하면 대기 목적지(`Pending NavKey`)로 격리 후 로그인 완료 시 백스택과 함께 복원한다.
   - 푸시 알림이나 외무 진입 시 최상위 루트 화면까지 이어지는 합성 백스택 정책을 명시적으로 구축한다.

---

### 하위 세부 계약 목록

- [App Link는 검증된 https deep link다](app-links-verification.md)
- [Manifest와 assetlinks는 서로 다른 역할을 가진다](assetlinks-verification-json.md)
- [Deep link는 외부 URI 계약이다](deep-link-uri-fundamentals.md)
- [External URI는 navigation 전에 검증되어야 한다](external-uri-validation.md)
- [Authenticated deep link는 대기 목적지와 back stack이 필요하다](authenticated-deep-links.md)
- [Notification deep link는 명시적 task와 back stack 정책이 필요하다](notification-deep-link-back-stack.md)
- [Dynamic App Link는 manifest 범위를 세분화할 뿐 확장하지 않는다](dynamic-app-links.md)
- [Deep link 테스트는 resolution, verification, routing을 함께 검증한다](deep-link-testing-validation.md)

---

### 상위 및 연관 지도

- 상위 가이드: [Android Deep Links 종합 가이드](android-deep-links.md)
- 연관 아키텍처: [Navigation 3 deep link는 URI를 NavKey로 변환한다](../navigation3/navigation3-deep-link-routing.md)
