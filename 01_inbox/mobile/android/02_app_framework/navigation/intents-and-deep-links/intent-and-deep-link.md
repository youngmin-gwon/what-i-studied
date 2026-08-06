---
title: intent-and-deep-link
tags: [android, android/navigation, android/intent, android/deep-links]
aliases: ["Intent와 Deep Link 종합 체계", "Intent and Deep Link"]
date modified: 2026-08-06 15:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Intent와 Deep Link 종합 색인은 이전 링크를 정본으로 연결한다

이 문서는 기존 inbound link를 보존하는 호환 색인이다. 현재의 전체 읽기 순서와 계층 구분은 [Android Navigation 진입 계약](../navigation-contracts/navigation-contracts.md)이 소유한다. 여기에는 Intent/Manifest와 Deep Link 두 하위 정본으로 가는 최소 경로만 남긴다.

---

### 두 하위 정본

1. **[Intent & Manifest 계약](intent-manifest-contracts/intent-manifest-contracts.md)**:
   - 안드로이드 OS 컴포넌트(Activity, Service, BroadcastReceiver)의 진입점 선언, 경계 통제(`exported`), 실행 위임 토큰(`PendingIntent`), 라이프사이클 인지 결과 통신(`ActivityResultAPI`)을 규정한다.
2. **[Deep Link 계약](deep-link-contracts/deep-link-contracts.md)**:
   - 외부 URI 입력을 안전한 내비게이션 상태(`NavKey`)로 전환하고, 도메인 소유권을 웹 서버(`assetlinks.json`)와 연동하여 검증(`App Links`)하며, 인증/푸시 상태에서의 백스택 복원 정책을 다룬다.

---

### 보충 가이드

- [Android Intent 및 IPC 종합 가이드](android-intent-and-ipc.md)
- [Android Deep Links 종합 가이드](android-deep-links.md)
