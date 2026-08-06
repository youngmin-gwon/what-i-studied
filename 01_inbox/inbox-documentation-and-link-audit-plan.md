---
title: inbox-documentation-and-link-audit-plan
tags: [plan, audit, documentation, android, computer-science]
aliases: [Inbox 전수조사 및 문서 정비 계획]
date modified: 2026-08-06 16:38:00 +09:00
date created: 2026-08-06 16:38:00 +09:00
role: master-plan
---

## 01_inbox 전수조사 및 문서/링크 정비 종합 마스터 플랜 (Master Audit Plan)

### 📌 1. 정비 목적과 배경
본 플랜은 `01_inbox` 내 **1,165개 전체 마크다운 문서**를 대상으로, **(1) 용어 설명의 친절성 보강**과 **(2) 상대 경로 마크다운 링크 100% 결합**을 달성하기 위한 구체적이고 체계적인 정비 지침 및 체크리스트이다.

---

### 🚨 2. 품질 및 작성 표준 규칙 (Quality & Writing Standards)

1. **상대 경로 마크다운 링크 필수 (예: `[Text](../../relative_path.md)`)**
   - ❌ Obsidian 위키링크(`WikiLinks`) 절대 사용 금지.
   - ❌ `file:///Users/youngmin/...` 절대 경로 절대 사용 금지 (환경 이식성 파괴 원인).
   - ⭕ 작성하는 문서의 위치를 기준으로 **상대 경로 마크다운 링크**만 작성한다.

2. **Mermaid 다이어그램 라벨 가독성 보장**
   - ❌ Mermaid 노드 라벨 텍스트 안에 마크다운 링크 구문(`[...]`)을 집어넣지 않는다 (렌더링 깨짐 원인).
   - ⭕ Mermaid 내부 노드는 순수 라벨 텍스트만 유지하고, 링크는 다이어그램 하단 본문에 배치한다.

3. **입문자 친화적 서술 방식 보강 (Beginner-Friendly Explanation)**
   - 전문 용어를 배경 설명 없이 암호문처럼 나열하지 않는다.
   - 처음 접하는 학습자도 "개념 ➔ 작동 원리 ➔ 실전 예시 ➔ 관련 링크" 순서로 쉽게 이해할 수 있도록 입체적으로 설명한다.

---

### 📊 3. 전수조사 현황 데이터 (Full Audit Baseline)

- **총 검사 대상 파일 수**: 1,165개 문서
- **핵심 개념어 미링크(Unlinked) 결함 문서**: 846개 문서 (72.6%)
- **설명 불친절 / 극심한 요약체 문서**: 142개 문서 (12.2%)

---

### 🗓️ 4. 단계별 실행 로드맵 및 체크리스트 (Phase-by-Phase Roadmap)

#### Phase 1: Android Foundations (안드로이드 기본 및 핵심 계약 문서 정비)
> **타겟 경로**: `01_inbox/mobile/android/00_foundations/overview/foundation-contracts/`

- [x] [android-is-layered-mobile-platform-not-just-an-app-sdk.md](mobile/android/00_foundations/overview/foundation-contracts/android-is-layered-mobile-platform-not-just-an-app-sdk.md) (완료)
- [x] [app-launch-crosses-launcher-system-server-zygote-and-activitythread.md](mobile/android/00_foundations/overview/foundation-contracts/app-launch-crosses-launcher-system-server-zygote-and-activitythread.md) (완료)
- [x] [android-security-is-layered-from-uid-sandbox-to-permissions-and-verified-boot.md](mobile/android/00_foundations/overview/foundation-contracts/android-security-is-layered-from-uid-sandbox-to-permissions-and-verified-boot.md) (완료)
- [x] [camera-example-crosses-permission-intent-ui-media-hal-and-storage-boundaries.md](mobile/android/00_foundations/overview/foundation-contracts/camera-example-crosses-permission-intent-ui-media-hal-and-storage-boundaries.md) (완료)
- [x] [android-stack-boundaries-explain-where-a-problem-belongs.md](mobile/android/00_foundations/overview/foundation-contracts/android-stack-boundaries-explain-where-a-problem-belongs.md) (완료)
- [x] [foundation-contracts.md](mobile/android/00_foundations/overview/foundation-contracts/foundation-contracts.md) (완료)

#### Phase 2: Android System Internals & Services (시스템 내부 및 서비스)
> **타겟 경로**: `01_inbox/mobile/android/01_system_internals/`, `01_inbox/mobile/android/04_system_services/`

- [x] [binder-ipc.md](mobile/android/01_system_internals/binder-ipc.md) (완료)
- [x] [hal.md](mobile/android/01_system_internals/hal.md) (완료)
- [x] [art.md](mobile/android/01_system_internals/art.md) (완료)
- [x] [system-server.md](mobile/android/04_system_services/system-server.md) (완료)
- [x] [kernel-and-hal/android-kernel-runtime.md](mobile/android/01_system_internals/kernel-and-hal/android-kernel-runtime.md) (완료)
- [x] [kernel-and-hal/hal-native-boundary.md](mobile/android/01_system_internals/kernel-and-hal/hal-native-boundary.md) (완료)

#### Phase 3: Android App Framework & Compose (앱 프레임워크 및 컴포즈)
> **타겟 경로**: `01_inbox/mobile/android/02_app_framework/`

- [x] [viewmodel.md](mobile/android/02_app_framework/viewmodel.md) (완료)
- [x] [single-source-of-truth.md](mobile/android/02_app_framework/single-source-of-truth.md) (완료)
- [x] [stateflow-and-sharedflow.md](mobile/android/02_app_framework/stateflow-and-sharedflow.md) (완료)
- [x] [recomposition.md](mobile/android/02_app_framework/jetpack-compose/runtime/recomposition.md) (완료)
- [x] [composable-body-must-be-fast-idempotent-and-side-effect-free.md](mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/composable-body-must-be-fast-idempotent-and-side-effect-free.md) (완료)

#### Phase 4: Security, Privacy & Performance (보안 및 성능)
> **타겟 경로**: `01_inbox/mobile/android/05_security_privacy/`, `01_inbox/mobile/android/06_testing_performance/`

- [x] [appops-and-permissions.md](mobile/android/05_security_privacy/appops-and-permissions.md) (완료)
- [x] [android-security-practice-is-defense-in-depth-not-client-trust.md](mobile/android/05_security_privacy/security-practices/security-practice-contracts/android-security-practice-is-defense-in-depth-not-client-trust.md) (완료)
- [x] [heavy-work-does-not-belong-in-composition.md](mobile/android/02_app_framework/jetpack-compose/performance/compose-performance-contracts/heavy-work-does-not-belong-in-composition.md) (완료)

#### Phase 5: Computer Science References (기초 컴퓨터 과학)
> **타겟 경로**: `01_inbox/computer-science/`

- [x] [pure-function.md](computer-science/pure-function.md) (완료)
- [x] [immutability.md](computer-science/immutability.md) (완료)
- [x] [context.md](computer-science/context.md) (완료)
- [x] [structured-concurrency.md](computer-science/structured-concurrency.md) (완료)
- [x] [race-condition-and-deadlock.md](computer-science/race-condition-and-deadlock.md) (완료)
- [x] [linux-kernel.md](operating-systems/linux-kernel.md) (완료)

---

### 🔄 5. 검수 및 관리 절차
1. 각 Phase 의 문서를 정비할 때마다 본 Plan 파일의 체크리스트(`[ ]` ➔ `[x]`)를 즉시 업데이트한다.
2. 개작 완료된 문서는 **(1) 친절한 설명 (2) Mermaid 가독성 (3) 상대 경로 링크** 3대 기준을 통과해야만 체크 표시(`[x]`)한다.
