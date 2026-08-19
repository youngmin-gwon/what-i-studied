---
title: assistant-agent
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-10 16:07:45 +09:00
date created: 2026-07-31 17:42:24 +09:00
---

## Assistant 와 에이전트 통합 계약

이 지도는 App Actions 와 AppFunctions 를 하나의 AI 연동으로 뭉치지 않고, 외부 실행 표면별 계약으로 나눈다.

### 읽는 순서

1. [Android 외부 실행 표면은 App Actions와 AppFunctions로 나뉜다](./android-external-execution-surfaces-split-app-actions-and-appfunctions.md) 로 두 표면의 호출자와 결과 계약을 구분한다.
2. UI fulfillment 라면 [App Actions는 Assistant 질의를 앱 fulfillment로 연결한다](./app-actions-map-assistant-queries-to-app-fulfillment.md) 를 읽는다.
3. 함수 발견·실행이라면 [AppFunctions는 에이전트용 앱 기능 계약이다](./appfunctions-are-app-capability-for-agents.md) 를 읽고 Android 16+, preview, 호출자 권한 조건을 확인한다.
4. [외부 의도 실행은 의미 해석, 전달, 검증, 실행을 분리한다](./external-intent-execution-separates-meaning-delivery-validation-and-action.md) 와 [Assistant와 에이전트 호출은 앱 내부 권한 검사를 대체하지 않는다](./assistant-and-agent-calls-do-not-replace-app-authorization.md) 로 도메인 경계를 설계한다.
5. [App Actions와 AppFunctions 도입은 preview와 호출 표면을 검증해야 한다](./app-actions-and-appfunctions-require-surface-and-preview-validation.md) 로 출시 전 검증한다.

### 문제 분류

| 문제 | 먼저 구분할 것 |
| --- | --- |
| Assistant 질의가 앱을 열지 못함 | BII/custom intent, locale, preview, fulfillment 매핑 |
| 앱은 열리지만 잘못된 대상을 선택함 | 의미 추출값과 앱 도메인 입력 검증 |
| AppFunction 이 검색되지 않음 | Android 16+, 등록 schema, 함수 활성 상태, preview 노출 |
| 검색되지만 실행 권한 오류 | 호출자의 플랫폼 권한과 함수의 앱 내부 권한 |
| 같은 상태 변경이 반복됨 | 호출 재시도와 도메인 멱등성 |

### 표면 경계

- App Actions 는 Google Assistant 가 BII 또는 custom intent 를 fulfillment Android intent 로 바꾸는 제품 표면이다.
- AppFunctions 는 Android OS registry 에 함수 metadata 를 제공하고 승인된 호출자가 로컬 함수를 실행하는 플랫폼·Jetpack preview 다.
- 두 표면 모두 외부 입력의 의미 정확성, 로그인 상태, 리소스 소유권, 민감 작업 확인을 보장하지 않는다.

### 노트 목록

- [Android 외부 실행 표면은 App Actions와 AppFunctions로 나뉜다](./android-external-execution-surfaces-split-app-actions-and-appfunctions.md)
- [App Actions는 Assistant 질의를 앱 fulfillment로 연결한다](./app-actions-map-assistant-queries-to-app-fulfillment.md)
- [AppFunctions는 에이전트용 앱 기능 계약이다](./appfunctions-are-app-capability-for-agents.md)
- [외부 의도 실행은 의미 해석, 전달, 검증, 실행을 분리한다](./external-intent-execution-separates-meaning-delivery-validation-and-action.md)
- [Assistant와 에이전트 호출은 앱 내부 권한 검사를 대체하지 않는다](./assistant-and-agent-calls-do-not-replace-app-authorization.md)
- [App Actions와 AppFunctions 도입은 preview와 호출 표면을 검증해야 한다](./app-actions-and-appfunctions-require-surface-and-preview-validation.md)

검증일: 2026-08-03. AppFunctions 는 Android 16+ experimental preview 이며 Gemini 통합은 제한된 preview 상태이므로 [AppFunctions 개요](https://developer.android.com/ai/appfunctions) 와 [Jetpack release notes](https://developer.android.com/jetpack/androidx/releases/appfunctions) 를 릴리스마다 다시 확인한다.
