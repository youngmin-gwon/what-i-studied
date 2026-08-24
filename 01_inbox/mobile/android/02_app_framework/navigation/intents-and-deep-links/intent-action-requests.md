---
title: intent-action-requests
tags: [android, android/navigation, android/intent]
aliases: ["Intent는 컴포넌트 실행을 설명하는 메시지다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Intent 는 컴포넌트 실행을 설명하는 메시지다

상위 문서: [Intent & Manifest 계약](intent-manifest.md)

---

### 개념과 내부 구조 (What & How)

1. **개념 (What)**:
   - **Intent**는 안드로이드 애플리케이션 프레임워크에서 컴포넌트 간 작업 수행 의도(Action Request)를 담아 전달하는 **수동적 수송 객체(Passive Data Structure)**다.
2. **구성 요소 (How)**:
   - **Component Name**: 실행할 타겟 컴포넌트의 클래스 패키지 정보.
   - **Action**: 수행할 동작의 이름 (예: `ACTION_VIEW`, `ACTION_SEND`, `ACTION_MAIN`).
   - **Data**: 동작을 수행할 대상 URI (`Uri.parse("https://...")`) 및 MIME 타입.
   - **Category**: 컴포넌트 종류에 대한 추가 정보 (`CATEGORY_LAUNCHER`, `CATEGORY_BROWSABLE`).
   - **Extras**: Key-Value 형태의 부가 데이터 묶음 (`Bundle`).
   - **Flags**: OS 태스크 및 백스택 동작 제어 플래그 (`FLAG_ACTIVITY_NEW_TASK`, `FLAG_ACTIVITY_CLEAR_TOP`).

---

### 관련 상위 및 연관 노트

- 상위 계약: [Intent & Manifest 계약](intent-manifest.md)
- 연관 가이드: [Android Intent 및 IPC 종합 가이드](android-intent-and-ipc.md)
