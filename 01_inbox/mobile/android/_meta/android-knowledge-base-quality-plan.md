---
title: "Android 개인 지식 베이스 고품질화 계획"
tags: ["android", "knowledge-base", "quality-plan"]
---

# Android 개인 지식 베이스 고품질화 계획

이 문서는 `01_inbox/mobile/android`를 구조적으로 정리된 문서 묶음에서 실제로 오래 쓸 수 있는 개인 지식 베이스로 끌어올리기 위한 작업 계획이다.

현재 상태는 권장 종료 기준을 통과했다.

- Android 문서 수: 586개
- redirect stub: 0개
- broken markdown link: 0개
- wikilink: 0개
- file URI link: 0개
- duplicate stem/body: 0개
- frontmatter/H1 누락: 0개
- 14줄 이하 활성 노트: 0개

다음 단계의 목표는 기계 검증을 통과한 문서를 사람이 읽어도 충분히 좋은 원자 노트로 바꾸는 것이다.

## 목표

최종 목표는 Android 지식 베이스가 다음 역할을 하게 만드는 것이다.

- 문제를 만났을 때 어느 Android 계층의 문제인지 빠르게 분류한다.
- Flutter, Kotlin, Compose, Android framework, AOSP 개념을 이름 매핑이 아니라 책임 경계로 이해한다.
- 각 노트가 단독으로 읽혀도 핵심 판단 기준을 제공한다.
- 지도 노트는 학습 순서와 탐색 경로를 제공하고, 개별 노트는 하나의 의미 단위만 설명한다.
- 오래된 튜토리얼 조각이나 중복 요약이 다시 쌓이지 않게 운영 규칙을 남긴다.

## 완료 기준

정말 좋은 개인 지식 베이스로 간주하려면 모든 활성 노트가 아래 기준을 만족해야 한다.

### 원자 노트 기준

- 하나의 노트는 하나의 판단 단위만 다룬다.
- 제목은 API 이름보다 판단 명제를 우선한다.
- 본문은 최소한 `정의`, `판단 기준`, `경계`, `관련 노트` 중 3개 이상의 역할을 수행한다.
- 같은 설명을 다른 노트에 반복하지 않는다.
- 다른 노트로 넘길 내용은 짧게 요약하고 markdown link로 연결한다.

### 지도 노트 기준

- 하위 노트 목록만 나열하지 않는다.
- 읽는 순서, 계층 구조, 문제 분류 기준을 제공한다.
- 비슷해 보이는 하위 노트의 차이를 한 문장씩 설명한다.
- 해당 폴더의 새 노트 생성 규칙을 암시할 정도로 경계가 분명해야 한다.

### 기술 정확성 기준

- Android Developers, AOSP 문서, 공식 Jetpack 문서와 충돌하지 않는다.
- 버전 의존 내용은 Android version, API level, Jetpack library version, compile/runtime 조건을 분리한다.
- 공식 문서가 빠르게 변할 수 있는 영역은 날짜와 검증 출처를 남긴다.
- 추정성 표현은 `추정`, `일반적으로`, `버전에 따라`처럼 명시한다.

### 운영 기준

- Obsidian link는 markdown link만 사용한다.
- 삭제된 legacy 경로를 다시 참조하지 않는다.
- `docs/`, repo-local 경로, absolute path, local file URI 링크를 넣지 않는다.
- 동일 stem, 동일 본문, 120줄 초과 비허브 노트를 만들지 않는다.
- 새로 추가하는 노트는 frontmatter, H1, 관련 노트를 갖춘다.

## 작업 원칙

이 작업은 한 명의 에이전트가 전부 쓰는 방식보다 여러 AI agent를 병렬로 쓰는 것이 효율적이다. 단, 최종 결정권은 감독 에이전트가 가진다.

### 감독 에이전트

역할:

- 전체 구조와 완료 기준을 유지한다.
- 작업 단위를 나누고 에이전트별 write scope를 분리한다.
- 외부 AI agent 결과를 그대로 반영하지 않고 검증한다.
- 최종 링크, 중복, 내용 품질, 문체를 검수한다.

감독 에이전트는 직접 고쳐야 하는 영역과 위임해야 하는 영역을 분리한다. 다음 경우는 감독 에이전트가 직접 처리한다.

- 폴더 구조 변경
- 노트 삭제 또는 병합
- cross-folder link retargeting
- 최종 validation script 실행
- `_meta` 계획과 작업 기록 업데이트

### 작업 에이전트

작업 에이전트는 하나의 폴더 또는 하나의 주제군만 맡는다.

허용 작업:

- 노트 내용 재작성
- 판단 기준 보강
- 관련 노트 추가
- 공식 문서 기반 검증 메모 추가
- 중복 후보 보고

금지 작업:

- 다른 폴더의 파일 삭제
- 전역 링크 일괄 변경
- 폴더 구조 변경
- redirect 생성
- 확인하지 않은 최신 정보 단정

### 외부 AI agent

다른 AI agent는 아래 역할로 사용한다.

- Research agent: 공식 문서와 AOSP 기준으로 사실 검증
- Editor agent: 문장 품질과 중복 표현 정리
- Graph agent: 관련 노트 연결과 누락된 entrypoint 탐지
- Reviewer agent: 논리 충돌, 오래된 정보, 과잉 일반화 지적
- Migration agent: markdown link, frontmatter, 제목 규칙 같은 기계적 수정

외부 agent 결과는 항상 다음 형태로 받아야 한다.

```text
범위:
수정한 파일:
주요 변경:
검증한 출처:
불확실한 내용:
추가로 검토할 링크:
```

## 품질 등급

각 노트는 작업 중 임시로 아래 등급을 붙여 평가한다. 이 등급은 frontmatter에 영구적으로 남기지 않아도 된다.

### A 등급

- 단독으로 읽어도 판단 기준이 분명하다.
- 다른 노트와 책임이 겹치지 않는다.
- 최신 공식 문서와 충돌하지 않는다.
- 관련 노트가 충분하다.

### B 등급

- 핵심 설명은 맞지만 예시, 경계, 관련 노트가 부족하다.
- 지도 노트라면 읽는 순서가 약하다.
- 개별 노트라면 오판 방지 문장이 부족하다.

### C 등급

- 기계 기준은 통과하지만 내용이 얇다.
- 일괄 보강 문장이 남아 있다.
- 제목과 본문이 명확한 판단 단위로 맞지 않는다.

### D 등급

- 중복되거나 오래된 정보가 있다.
- 사실 검증이 필요하다.
- 병합 또는 삭제 후보이다.

최종 목표는 모든 활성 노트를 A 또는 B 등급으로 만드는 것이다. C 등급은 마지막에 남기지 않는다.

## 전체 페이즈

### Phase 1. 기준선 스냅샷

목표: 현재 586개 문서의 품질 상태를 재측정한다.

작업:

- 폴더별 문서 수, line count, link count, outbound/inbound link 수를 추출한다.
- `판단 기준`, `경계`, `관련 노트`, `공식 문서` 섹션 존재 여부를 측정한다.
- 지도 노트와 개별 노트를 분리한다.
- C/D 등급 후보를 자동 선별한다.

산출물:

- `_meta/android-kb-quality-audit.tsv`
- `_meta/android-kb-quality-dashboard.md`

권장 담당:

- Migration agent: metrics 추출
- Graph agent: inbound/outbound link 분석
- 감독 에이전트: 기준 확정

### Phase 2. 지도 노트 고품질화

목표: 각 폴더의 진입점을 실제 navigation map으로 만든다.

대상:

- `00_foundations`
- `01_system_internals`
- `02_app_framework`
- `03_packaging_deployment`
- `04_system_services`
- `05_security_privacy`
- `06_testing_performance`
- `07_platforms`

작업:

- 각 최상위 지도 노트에 읽는 순서를 추가한다.
- 하위 계약 묶음의 차이를 설명한다.
- 문제 상황별 진입 경로를 추가한다.
- 중복 지도 노트가 있으면 상위 map과 contract map 역할을 분리한다.

완료 기준:

- 사용자가 `Android 앱이 죽는다`, `Compose가 느리다`, `권한이 있는데 API가 실패한다` 같은 문제에서 적절한 하위 노트로 이동할 수 있다.

권장 담당:

- 감독 에이전트: 최상위 지도 작성
- Graph agent: 누락 링크 탐지
- Editor agent: 지도 문장 정리

### Phase 3. 기계 보강 문장 제거

목표: Phase 37에서 일괄 추가된 `판단 기준`, `경계` 문장을 사람이 쓴 문장으로 바꾼다.

우선 대상:

- `02_app_framework/dependency-injection`
- `01_system_internals/platform-modularity`
- `00_foundations`
- `05_security_privacy/permissions-and-sandbox`
- `02_app_framework/ui`

작업:

- 일괄 보강 문장이 실제 노트 주제에 맞는지 확인한다.
- 같은 폴더의 모든 노트가 같은 문장으로 끝나는 경우 주제별 문장으로 재작성한다.
- 예시가 필요한 노트에는 짧은 Android/Kotlin 예시를 넣는다.
- 예시가 오히려 노트를 길게 만들면 관련 노트 링크로 대체한다.

완료 기준:

- 어떤 노트도 generic filler처럼 보이지 않는다.
- `판단 기준`과 `경계`가 해당 노트 제목에 직접 대응한다.

권장 담당:

- Editor agent: 문장 재작성
- Research agent: 기술 용어 검증
- 감독 에이전트: 중복 방지

### Phase 4. App Framework 심화 pass

목표: Android 앱 개발자가 가장 자주 보는 영역을 실사용 품질로 올린다.

대상:

- `02_app_framework/architecture`
- `02_app_framework/data`
- `02_app_framework/dependency-injection`
- `02_app_framework/jetpack-compose`
- `02_app_framework/navigation`
- `02_app_framework/ui`

핵심 질문:

- ViewModel, Repository, UseCase, UI state 책임이 명확한가?
- Compose state/effect/runtime 노트가 같은 내용을 반복하지 않는가?
- DI 노트가 framework 비교가 아니라 graph/lifetime 판단 기준을 제공하는가?
- Navigation 노트가 route, back stack, deep link, adaptive navigation의 경계를 분리하는가?

완료 기준:

- 각 하위 폴더에 A 등급 지도 노트가 있다.
- 모든 개별 노트가 관련 노트 2개 이상으로 연결된다.
- Compose 관련 노트는 `UI = f(state)`, automatic state observation, recomposition, effect boundary를 서로 중복 없이 연결한다.

권장 담당:

- Compose specialist agent
- Android architecture agent
- Editor agent
- 감독 에이전트

### Phase 5. System Internals 정확성 pass

목표: 앱 개발 관점과 AOSP/system 관점이 섞이지 않게 정리한다.

대상:

- `01_system_internals/boot-and-runtime`
- `01_system_internals/kernel-and-hal`
- `01_system_internals/ipc-and-process`
- `01_system_internals/graphics-and-media`
- `01_system_internals/connectivity`
- `01_system_internals/platform-modularity`
- `01_system_internals/platform-customization`

핵심 질문:

- 앱 API, framework service, native service, kernel boundary가 구분되는가?
- system_server, Zygote, Binder, HAL, SELinux 같은 용어가 정확히 연결되는가?
- AOSP/OEM customization 내용이 앱 개발 가이드처럼 보이지 않는가?
- graphics/media 노트가 UI rendering과 compositor/media pipeline을 분리하는가?

완료 기준:

- 각 노트가 어느 계층의 책임인지 명시한다.
- AOSP 출처가 필요한 노트는 공식 링크 또는 검증 메모를 갖는다.
- 앱 개발자가 직접 제어할 수 없는 영역은 `관찰 가능 신호`와 `디버깅 진입점`으로 설명한다.

권장 담당:

- AOSP research agent
- System internals reviewer
- Graph agent
- 감독 에이전트

### Phase 6. Security, Privacy, Storage 정확성 pass

목표: 보안 문서를 실무적으로 위험하지 않게 만든다.

대상:

- `05_security_privacy/permissions-and-sandbox`
- `05_security_privacy/platform-hardening`
- `05_security_privacy/secure-storage`
- `05_security_privacy/integrity-and-attestation`
- `05_security_privacy/security-practices`

핵심 질문:

- permission, AppOps, sandbox, SELinux, Verified Boot가 섞이지 않는가?
- Play Integrity를 authorization으로 오해하지 않게 설명하는가?
- Keystore, AES-GCM, BiometricPrompt, backup boundary가 정확한가?
- client trust 한계를 명시하는가?

완료 기준:

- 보안 노트는 추상적 권장사항보다 threat boundary를 설명한다.
- 암호화 예시는 nonce/IV, key ownership, backup/restore, biometric auth 조건을 빠뜨리지 않는다.
- 최신 정책이 필요한 항목은 검증 날짜를 남긴다.

권장 담당:

- Security research agent
- Reviewer agent
- 감독 에이전트

### Phase 7. Packaging, Testing, Performance 운영 pass

목표: 빌드, 배포, 테스트, 성능 노트를 실제 의사결정 체크리스트로 만든다.

대상:

- `03_packaging_deployment`
- `06_testing_performance`

핵심 질문:

- Gradle/AGP/Kotlin/Compose compiler/BOM 관계가 정확한가?
- AAB/APK/signing/release track/rollback 경계가 분명한가?
- Macrobenchmark, Baseline Profile, Perfetto, profiler의 역할이 구분되는가?
- 테스트 노트가 feedback cost와 release risk 기준을 제공하는가?

완료 기준:

- 각 운영 노트는 checklist 또는 decision table을 가진다.
- 최신 버전 의존 내용은 공식 문서 확인이 필요하다고 표시한다.
- 성능 노트는 측정 전 최적화를 경계한다.

권장 담당:

- Build/release agent
- Performance agent
- Research agent
- 감독 에이전트

### Phase 8. Platforms and Form Factors pass

목표: large screen, XR, multi-window를 phone UI 확장판이 아니라 별도 form factor contract로 정리한다.

대상:

- `07_platforms/large-screens`
- `07_platforms/xr`

핵심 질문:

- window size class와 device type을 구분하는가?
- adaptive layout이 scale 변경이 아니라 structure 변경임을 설명하는가?
- XR 내용이 최신성과 실험성을 명시하는가?

완료 기준:

- 각 form factor 노트는 입력 방식, lifecycle, layout, system UI, 테스트 관점을 포함한다.
- 최신성이 불안정한 XR 문서는 검증 날짜와 출처를 남긴다.

권장 담당:

- Research agent
- Product/design reviewer
- 감독 에이전트

### Phase 9. Graph 정리

목표: 노트들이 실제로 탐색 가능한 지식 그래프가 되게 만든다.

작업:

- inbound link가 0인 고립 노트를 찾는다.
- 과도하게 많은 outbound link를 가진 노트를 정리한다.
- 각 최상위 지도에서 모든 주요 contract cluster로 갈 수 있게 한다.
- 비슷한 주제의 노트는 양방향 관련 링크를 추가한다.
- glossary는 정본 대체가 아니라 entrypoint 역할만 유지한다.

완료 기준:

- 중요한 노트 중 orphan이 없다.
- 각 영역의 지도 노트에서 2단계 이내로 주요 개별 노트에 도달한다.
- 관련 링크 라벨이 stem이 아니라 사람이 읽는 제목이다.

권장 담당:

- Graph agent
- Migration agent
- 감독 에이전트

### Phase 10. 최종 검수와 운영 문서화

목표: 이후에도 문서가 다시 비대해지지 않도록 운영 규칙을 남긴다.

작업:

- 최종 validation script를 `_meta` 또는 repo scratch로 보존할지 결정한다.
- 새 Android 노트 작성 템플릿을 만든다.
- monthly audit checklist를 만든다.
- 외부 AI agent 작업 시 전달할 prompt template을 만든다.

완료 기준:

- 새 노트를 추가할 때 지켜야 할 규칙이 문서화되어 있다.
- 검증 command가 재현 가능하다.
- 품질 기준이 사람의 감이 아니라 checklist로 남아 있다.

권장 담당:

- 감독 에이전트
- Reviewer agent

## 병렬 작업 설계

작업은 아래처럼 병렬화한다.

### Batch A. App Framework

범위:

- `02_app_framework/architecture`
- `02_app_framework/data`
- `02_app_framework/dependency-injection`
- `02_app_framework/jetpack-compose`
- `02_app_framework/navigation`
- `02_app_framework/ui`

에이전트 구성:

- Compose agent
- Architecture/Data agent
- DI/Navigation agent
- Editor agent

감독 포인트:

- Compose와 UI system 노트의 중복
- ViewModel/StateFlow/Compose state 책임 중복
- DI graph lifetime 설명의 일관성

### Batch B. System Internals

범위:

- `01_system_internals`

에이전트 구성:

- Boot/runtime agent
- Kernel/HAL agent
- IPC/graphics/connectivity agent
- AOSP fact-check agent

감독 포인트:

- 앱 개발자가 제어 가능한 것과 system 관찰만 가능한 것의 구분
- AOSP/OEM 내용의 정확성
- Binder, system_server, SELinux, HAL 용어의 일관성

### Batch C. Security and Operations

범위:

- `03_packaging_deployment`
- `05_security_privacy`
- `06_testing_performance`

에이전트 구성:

- Security agent
- Build/release agent
- Performance/testing agent
- Reviewer agent

감독 포인트:

- 최신 정책과 버전 의존성
- 보안상 위험한 단정
- 성능 측정과 진단 도구의 구분

### Batch D. Foundations and Platforms

범위:

- `00_foundations`
- `04_system_services`
- `07_platforms`

에이전트 구성:

- Learning path editor
- System services agent
- Form factor research agent
- Graph agent

감독 포인트:

- 학습 순서가 실제 Android 계층 이해로 이어지는지
- background work, notification, FCM, App Functions의 경계
- large screen/XR 최신성

## 에이전트 작업 프롬프트 템플릿

### 재작성 에이전트용

```text
범위: <folder>

목표:
- 각 노트를 원자 노트로 유지한다.
- 중복 설명을 만들지 않는다.
- markdown link만 사용한다.
- frontmatter와 H1은 유지한다.

작업:
1. 활성 노트를 읽고 A/B/C/D 등급으로 분류한다.
2. C/D 노트만 재작성한다.
3. 지도 노트는 읽는 순서와 문제 분류 기준을 보강한다.
4. 개별 노트는 정의, 판단 기준, 경계, 관련 노트를 보강한다.
5. 공식 검증이 필요한 문장은 출처 또는 불확실성을 남긴다.

금지:
- 폴더 구조 변경
- 파일 삭제
- redirect 생성
- 다른 폴더의 링크 일괄 변경

보고:
- 수정 파일
- 병합/삭제 후보
- 공식 검증이 필요한 문장
- 중복 위험
- 실행한 검증
```

### 사실 검증 에이전트용

```text
범위: <files>

목표:
- Android Developers, AOSP, Jetpack 공식 문서 기준으로 사실 오류를 찾는다.

작업:
1. 버전 의존 문장을 표시한다.
2. 오래된 API, deprecated API, 정책 변경 가능성이 있는 문장을 찾는다.
3. 공식 문서와 충돌하는 설명을 지적한다.
4. 출처가 필요한 문장에 공식 링크를 제안한다.

보고:
- 파일 경로
- 문제 문장
- 왜 문제인지
- 권장 수정
- 공식 출처
```

### 그래프 에이전트용

```text
범위: <folder>

목표:
- 지식 그래프 탐색성을 높인다.

작업:
1. orphan note를 찾는다.
2. 지도 노트에서 접근할 수 없는 노트를 찾는다.
3. 관련 노트가 부족한 개별 노트를 찾는다.
4. 같은 주제를 다루는 중복 후보를 찾는다.
5. markdown link 라벨이 부자연스러운 곳을 고친다.

보고:
- orphan 후보
- link 추가 후보
- 중복 후보
- 지도 노트 보강 후보
```

## 검증 스크립트 기준

각 batch가 끝날 때 최소한 아래 항목을 확인한다.

```text
android_md
wikilink_files_left
file_uri_link_files
template_artifact_files
markdown_internal_links_broken
absolute_internal_links
repo_docs_links
agent_internal_links
duplicate_android_stems
exact_duplicate_groups
long_nonhub_120
active_missing_frontmatter
active_missing_h1
active_very_short_14
orphan_active_notes
```

최종 검증에서는 Android 폴더뿐 아니라 vault 전체에서 삭제된 Android path를 가리키는 링크도 확인한다.

## 예상 기간

작업량은 586개 활성 노트 전체의 내용 품질을 올리는 기준이다.

### 집중 작업 기준

- 자동 audit와 dashboard 작성: 0.5일
- 지도 노트 고품질화: 0.5~1일
- App Framework pass: 1~2일
- System Internals pass: 1~2일
- Security/Operations/Platforms pass: 1~2일
- Graph 정리와 최종 검수: 0.5~1일

총 예상: 4~8일.

### 여러 AI agent 병렬 사용 기준

에이전트를 4개 batch로 동시에 돌리고 감독 에이전트가 검수하면 2~4일로 줄일 수 있다. 단, 사실 검증이 필요한 security, platform, XR, 최신 Jetpack 영역은 병렬 처리해도 감독 검수 시간을 줄이면 안 된다.

## 우선순위

가장 먼저 품질을 올릴 영역은 다음 순서다.

1. `02_app_framework/dependency-injection`
2. `02_app_framework/ui`
3. `02_app_framework/jetpack-compose`
4. `05_security_privacy`
5. `01_system_internals/platform-modularity`
6. `01_system_internals/connectivity`
7. `03_packaging_deployment`
8. `06_testing_performance`
9. `07_platforms`
10. `00_foundations`

이 순서는 현재 기계 보강 문장이 많이 남아 있을 가능성, 사용 빈도, 기술 오해 위험을 함께 고려한 것이다.

## 리스크

### 과도한 재작성

모든 노트를 길게 만들면 원자성이 깨진다. 좋은 노트는 긴 노트가 아니라 판단 기준이 분명한 노트다.

대응:

- 개별 노트는 40~90줄을 목표로 한다.
- 120줄을 넘으면 지도 노트인지 확인하고, 아니면 분리한다.

### AI hallucination

AI agent가 Android 내부 동작을 그럴듯하게 잘못 설명할 수 있다.

대응:

- AOSP/system/security 최신성 영역은 Research agent와 Reviewer agent를 분리한다.
- 공식 문서가 필요한 문장은 출처를 남긴다.
- 감독 에이전트가 최종 병합한다.

### 링크 그래프 붕괴

병렬 에이전트가 서로 다른 링크 라벨과 경로를 만들 수 있다.

대응:

- batch 단위 write scope를 분리한다.
- 전역 link retargeting은 감독 에이전트만 수행한다.
- 매 batch 후 validation을 실행한다.

### 다시 커지는 inbox

새로운 자료를 그대로 붙여 넣으면 이전 상태로 돌아간다.

대응:

- 새 자료는 먼저 `00_foundations/learning` 또는 별도 inbox에 임시로 둔다.
- 정본으로 승격할 때는 기존 노트에 흡수하거나 새 원자 노트 하나만 만든다.
- 출처 요약과 개인 판단을 분리한다.

## 다음 액션

1. Phase 1 audit script를 만든다.
2. 586개 활성 노트에 대해 품질 dashboard를 생성한다.
3. `02_app_framework/dependency-injection`을 pilot batch로 선정한다.
4. 같은 범위에 대해 재작성 agent, reviewer agent, graph agent를 동시에 실행한다.
5. 감독 에이전트가 결과를 병합하고 validation을 통과시킨다.
6. pilot 결과를 기준으로 나머지 batch prompt를 조정한다.
