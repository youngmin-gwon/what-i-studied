---
title: Activity Result API는 lifecycle-aware 결과 반환 계약이다
tags: [android, android/intents, android/navigation]
aliases: ["Activity Result API는 lifecycle-aware 결과 반환 계약이다"]
date modified: 2026-08-03 16:36:27 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Activity Result API는 lifecycle-aware 결과 반환 계약이다

Activity Result API 는 다른 Activity 나 system UI 를 실행하고 typed result 를 받는 계약이다. `registerForActivityResult()` 는 callback 과 `ActivityResultContract` 를 등록하고, 반환된 launcher 가 실제 실행을 담당한다.

Callback 은 process/activity recreation 뒤에도 결과를 받을 수 있어야 하므로 매번 같은 순서로 조건 없이 등록한다. `launch()` 는 lifecycle 이 `CREATED` 이상일 때 호출하고, 결과 처리에 필요한 추가 상태는 이 API 와 별도로 저장/복원해야 한다.

권한 요청, Photo Picker, SAF, 카메라 촬영은 모두 같은 Activity Result boundary 를 통과하지만 각각의 permission/storage 의미는 별도 정본에서 판단한다.

### 판단 기준

- launcher 등록은 조건문 안에서 순서가 바뀌지 않게 둔다.
- result callback 은 UI controller 수명과 복원 상태를 함께 고려한다.
- 외부 Activity 가 반환하는 data 를 내부 trusted state 처럼 바로 취급하지 않는다.
- Photo Picker, SAF, permission request 는 각각 storage/permission 정본과 연결한다.

관련 노트: [Android 권한 계약](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/permission-contracts.md), [파일 접근 계약](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/file-access-contracts.md)

공식 문서: [Get a result from an activity](https://developer.android.com/training/basics/intents/result)
