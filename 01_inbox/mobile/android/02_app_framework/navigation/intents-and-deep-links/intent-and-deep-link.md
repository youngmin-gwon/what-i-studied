---
title: intent-and-deep-link
tags: [android, android/navigation, android/intent, android/deep-links]
aliases: ["Intent와 Deep Link 종합 체계", "Intent and Deep Link"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Intent & Deep Link 종합 체계

안드로이드 OS 컴포넌트 간 통신 메시지인 **Intent**와 외부 엔트리 포인트인 **Deep Link**를 통합 관리하는 맵 노드다.

---

### 아키텍처 두 축 (Two Architecture Pillars)

안드로이드 애플리케이션의 외부 연결과 내부 컴포넌트 바인딩은 다음 두 핵심 축으로 구성된다:

1. **[Intent & Manifest 계약](intent-manifest-contracts/intent-manifest-contracts.md)**:
   - 안드로이드 OS 컴포넌트(Activity, Service, BroadcastReceiver)의 진입점 선언, 경계 통제(`exported`), 실행 위임 토큰(`PendingIntent`), 라이프사이클 인지 결과 통신(`ActivityResultAPI`)을 규정한다.
2. **[Deep Link 계약](deep-link-contracts/deep-link-contracts.md)**:
   - 외부 URI 입력을 안전한 내비게이션 상태(`NavKey`)로 전환하고, 도메인 소유권을 웹 서버(`assetlinks.json`)와 연동하여 검증(`App Links`)하며, 인증/푸시 상태에서의 백스택 복원 정책을 다룬다.

---

### 정본 가이드 링크

- [Android Intent 및 IPC 종합 가이드](android-intent-and-ipc.md)
- [Android Deep Links 종합 가이드](android-deep-links.md)
- [Android Navigation 진입 계약](../navigation-contracts/navigation-contracts.md)
