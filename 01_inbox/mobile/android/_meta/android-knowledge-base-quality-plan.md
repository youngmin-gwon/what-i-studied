---
title: android-knowledge-base-quality-plan
tags: ["android", "knowledge-base", "quality-plan"]
aliases: []
date modified: 2026-08-03 17:01:16 +09:00
date created: 2026-08-03 16:20:03 +09:00
---

## Android 개인 지식 베이스 고품질화 계획

### 교정 배경

이 계획의 이전 버전은 링크, frontmatter, 길이, 중복, `판단 기준` 과 `경계` 섹션 같은 구조 지표를 내용 품질의 대리 지표로 사용했다. 그 결과 형식은 정돈됐지만 다음 문제가 남았다.

- Foundations 가 Android 를 설명하는 학습 계층이 아니라 다른 노트로 보내는 routing layer 가 되었다.
- 지도와 contract map 이 링크 및 노트 운영 규칙을 반복하고, 독자가 배워야 할 인과 모델은 얕았다.
- System Services 와 Platforms 의 폴더 이름이 실제 주제 범위보다 넓었다.
- 체크리스트와 추상 원칙이 구체적인 상태 흐름, 예시, 관찰 신호, 디버깅 절차를 대신했다.
- 기계 검증을 통과한 문서에도 사실 오류가 남았다.
- 최상위 지도에서 전체 Android 노트로 이어지는 학습 경로와 그래프 도달성이 충분하지 않았다.

따라서 이 계획은 `원자 노트 정리` 중심에서 `학습 서사 + worked example + 진단 runbook + 원자 reference` 의 다층 구조로 전환한다.

### 현재 기준선

2026-08-03 재감사 기준:

- 활성 Android 노트: 585 개 (`_meta` 제외)
- Batch D 재감사: 108 개 전수 읽기
- Batch D 의미 품질: A 45 / B 42 / C 20 / D 1
- 최상위 Foundation map 에서 도달 가능: 543 / 585
- Foundation map 에서 2 단계 이내 도달 가능: 111 / 585
- 도달 불가: 42 개
- broken Markdown link, duplicate stem/body, wikilink, file URI: 0 개

기계 기준은 저장소 위생 상태만 나타낸다. 내용 완료를 의미하지 않는다.

#### 확인된 대표 문제

- `00_foundations` 는 용어 색인과 routing 에는 유용하지만 Android 입문 curriculum 이 아니다.
- `04_system_services` 는 background work, FCM, Assistant/AppFunctions, NFC 만 다루며 Android system service 전체를 대표하지 않는다.
- `07_platforms` 는 large screen, desktop windowing, XR 에 집중하며 TV, Wear OS, Auto/Automotive 를 다루지 않는다.
- 재감사 당시 AlarmManager 노트는 PendingIntent 식별에서 Intent extras 의 역할을 잘못 설명했다. Phase 0 에서 수정했다.
- 재감사 당시 Background work 선택 모델에는 JobScheduler, user-initiated data transfer job, DownloadManager 와 task-specific API 가 빠져 있었다. Phase 0 에서 보강했다.
- Batch D 의 Foundations 와 Platforms 에는 구현 예시와 실행 가능한 진단 절차가 거의 없다.

### 최종 목표

Android 지식 베이스는 서로 다른 네 역할을 수행해야 한다.

1. 처음 읽는 사람이 Android 의 전체 실행 모델을 순서대로 이해한다.
2. 실제 기능과 장애를 end-to-end 로 추적하며 계층 사이 인과관계를 이해한다.
3. 문제를 만났을 때 관찰 신호를 근거로 실패 경계를 좁힌다.
4. 특정 판단이 필요할 때 짧은 원자 reference 로 빠르게 돌아온다.

최종 사용자는 다음 질문에 자신의 말로 답할 수 있어야 한다.

- APK/AAB 가 빌드, 서명, 설치된 뒤 앱 프로세스와 첫 Activity 가 어떻게 시작되는가?
- Manifest, component, Intent, task, process, lifecycle 은 어떻게 연결되는가?
- configuration change 와 process death 는 상태에 어떤 차이를 만드는가?
- main thread, coroutine, Binder thread, scheduler 의 책임은 어떻게 다른가?
- UI state 가 Compose/View 를 거쳐 frame 과 Surface 로 어떻게 이어지는가?
- permission, AppOps, UID sandbox, SELinux, platform policy 는 어디서 각각 거절하는가?
- 저장, 네트워크, background work 는 실패와 재시작을 어떻게 견디는가?
- build, signing, target SDK, runtime version, distribution 정책은 어떻게 분리되는가?
- 증상을 만났을 때 어떤 log, state, trace, command 를 먼저 확인해야 하는가?

### 지식 구조

#### 1. Learning Spine

Android 를 처음부터 끝까지 읽는 순차 문서다. 링크 목록이 아니라 인과관계를 설명한다.

필수 장:

1. Android 앱과 플랫폼의 전체 구조
2. Build, package, signing, install
3. Manifest 와 app component
4. Intent, task, back stack, process
5. Lifecycle, configuration change, process death, saved state
6. Main thread, Looper, coroutine, Binder 와 concurrency
7. UI state, View/Compose, rendering 과 frame
8. Data ownership, persistence, network, offline recovery
9. Permission, sandbox, AppOps 와 security boundary
10. Background execution, notification 과 user-visible work
11. Testing, debugging, performance measurement
12. Release, update, compatibility 와 form factor

각 장은 선행 지식, 실제 메커니즘, end-to-end 흐름, 최소 예시, 확인 질문, 다음 장을 포함한다.

#### 2. Worked Examples

여러 계층을 하나의 기능이나 장애로 연결한다.

필수 예시:

- 앱 아이콘 탭에서 첫 frame 까지
- 사진 촬영, preview, 저장, 업로드까지
- deep link 가 올바른 task 와 화면 상태로 열리기까지
- FCM 전송에서 notification 표시와 탭 복구까지
- process death 뒤 편집 상태와 background work 복구
- permission 이 있는데 API 가 실패하는 사례
- Compose jank 를 UI state 에서 SurfaceFlinger 까지 좁히는 사례
- signed artifact 가 Play delivery 를 거쳐 update 되는 과정

각 예시는 요청, 데이터, identity, thread/process, lifecycle, 실패 신호를 단계별로 추적한다.

#### 3. Diagnostic Runbooks

증상에서 조사 행동으로 바로 이어지는 문서다.

필수 구성:

- 증상과 재현 조건
- 가능한 실패 경계와 우선순위
- 사용할 `adb`, `dumpsys`, `cmd`, logcat, trace 또는 profiler
- 기대되는 정상 신호
- 실패 신호와 해석
- 다음 조사 경로
- OS/API/target SDK 조건

명령만 나열하지 않고 출력의 어떤 필드를 왜 보는지 설명한다.

#### 4. Atomic References

현재 contract 노트의 주 역할이다. 이미 배운 개념을 다시 판단할 때 사용한다.

원자 reference 는 모든 배경 설명을 반복할 필요는 없지만, 최소한 다음을 갖는다.

- 핵심 명제
- 동작 메커니즘 또는 상태 흐름
- 선택 기준이나 tradeoff
- 이웃 개념과의 경계
- 짧은 사례 또는 관찰 가능한 신호
- 관련 learning spine, example, runbook 링크
- 변동 가능할 경우 공식 출처와 검증일

#### 5. Maps and Glossary

- Map 은 범위, 포함하지 않는 범위, 읽는 순서, 대표 문제 경로를 보여준다.
- Map 은 독자가 배워야 할 설명을 대체하지 않는다.
- Glossary 는 짧은 정의와 혼동 방지, 정본 링크만 제공한다.
- Glossary 와 map 은 자체 역할을 잘 수행해도 learning spine 의 완료를 대신하지 않는다.

### 내용 완료 기준

#### 의미 품질 기준

다음 항목 중 문서 역할에 필요한 항목을 실제 내용으로 충족해야 한다.

- **Mental model**: 구성 요소 목록이 아니라 관계와 인과를 설명한다.
- **Mechanism**: 호출, 상태, 데이터, identity 또는 lifecycle 이 어떻게 이동하는지 설명한다.
- **Decision**: 어느 조건에서 무엇을 선택하고 무엇을 포기하는지 설명한다.
- **Worked example**: 최소 하나의 구체적인 입력과 결과를 보여준다.
- **Observable evidence**: log, callback, state, trace, exception 또는 command 결과를 제시한다.
- **Boundary**: 무엇을 설명하지 않는지뿐 아니라 이웃 개념과 동작 차이를 설명한다.
- **Accuracy**: 공식 문서와 충돌하지 않고 버전 조건을 분리한다.

`정의`, `판단 기준`, `경계`, `관련 노트` 라는 제목만 존재하는 것은 충족으로 계산하지 않는다.

#### 역할별 완료 기준

##### Learning Spine 장

- 선행 장을 읽은 독자가 따라갈 수 있다.
- 하나 이상의 end-to-end 흐름을 설명한다.
- 최소 예시와 확인 질문이 있다.
- 장을 읽은 뒤 독자가 답할 수 있어야 하는 질문이 명시되어 있다.
- 단순 링크 목록이나 노트 운영 규칙이 본문의 절반을 넘지 않는다.

##### Worked Example

- 시작 상태, 입력, 단계, 성공 결과, 실패 분기를 갖는다.
- 최소 세 개 이상의 Android 책임 계층을 연결한다.
- 코드 또는 상태 예시와 관찰 신호가 있다.
- 관련 원자 노트로 분해되지만, 예시 자체의 서사가 끊기지 않는다.

##### Diagnostic Runbook

- 재현 가능한 절차와 명령이 있다.
- 정상/실패 출력의 차이를 설명한다.
- 관찰 결과에 따라 다음 행동이 달라진다.
- 실제 기기, emulator, OS/API 조건을 구분한다.

##### Atomic Reference

- 제목의 명제를 본문이 실제 메커니즘으로 뒷받침한다.
- 추상적인 `확인한다`, `검증한다`, `분리한다` 만 반복하지 않는다.
- 예시 또는 관찰 신호가 최소 하나 있다. 순수 glossary 항목은 예외다.
- 같은 주제의 map 이나 checklist 와 내용을 불필요하게 반복하지 않는다.

##### Map

- 실제 범위와 제목이 일치한다.
- 포함하지 않는 영역을 밝힌다.
- learning spine 과 주요 cluster 로 가는 경로가 있다.
- 모든 링크를 복제하지 않고 차이와 선택 기준을 보여준다.

### 품질 등급

등급은 문서 역할을 고려하되 내용 깊이를 평가한다.

#### A 등급

- 역할에 필요한 mental model 또는 mechanism 을 충분히 설명한다.
- 실제 예시나 관찰 증거로 명제를 검증할 수 있다.
- 독자가 읽은 뒤 구체적인 판단이나 조사 행동을 할 수 있다.
- 사실 오류, 중복, 범위 과장이 없다.

#### B 등급

- 정확하고 제한된 reference 역할에는 유용하다.
- mechanism, example, evidence 중 하나가 약하다.
- 다른 learning 문서와 함께 읽으면 판단에 사용할 수 있다.

#### C 등급

- 링크 라우팅, 추상 원칙, 체크리스트 또는 API 이름 나열에 머문다.
- 독자가 왜 그런지 설명하거나 실제 행동으로 옮기기 어렵다.
- 제목이 약속한 범위를 충분히 다루지 않는다.

#### D 등급

- 사실 오류, 위험한 단정, 중복, 잘못된 범위 또는 폐기된 정보가 있다.
- 병합, 삭제 또는 공식 문서 기반 재작성 대상이다.

모든 노트를 무조건 A 로 만들지 않는다. Glossary 와 좁은 reference 는 B 여도 된다. 대신 각 핵심 learning cluster 에는 A 등급 spine 장, worked example, runbook 이 있어야 한다.

### 완료 게이트

#### 1. Coverage Gate

- 폴더 제목과 실제 범위가 일치한다.
- 빠진 영역은 추가하거나 제목과 map 에서 명시적으로 제외한다.
- System Services 와 Platforms 는 확장 또는 rename 결정을 먼저 완료한다.

#### 2. Learning Gate

- Learning Spine 12 개 장이 연결된 순서로 존재한다.
- 각 장의 확인 질문을 독립 reviewer 가 문서만 읽고 답할 수 있다.
- Foundations 는 다른 폴더로 보내기 전에 최소 mental model 을 직접 설명한다.

#### 3. Mechanism Gate

- 핵심 cluster 마다 호출·상태·데이터·identity·lifecycle 중 관련 흐름이 설명돼 있다.
- 구성 요소 이름만 나열한 문서는 완료로 계산하지 않는다.

#### 4. Example and Diagnostic Gate

- 필수 worked example 8 개가 있다.
- 주요 장애군마다 실행 가능한 runbook 이 있다.
- 예시와 runbook 에는 정상/실패 관찰 신호가 있다.

#### 5. Accuracy Gate

- Author 와 별도의 Research/Reviewer agent 가 공식 1 차 출처로 검증한다.
- API, policy, version 수치는 공식 문서 링크와 검증일을 남긴다.
- fact-check 가 끝나기 전에는 A 등급을 부여하지 않는다.

#### 6. Graph Gate

- Foundation map 에서 모든 top-level cluster 가 도달 가능하다.
- 핵심 learning 장과 cluster map 은 2 단계 이내에 도달한다.
- 원자 노트 전체를 무조건 2 단계로 만들 필요는 없지만 unreachable note 는 0 개여야 한다.
- link 수가 아니라 실제 독자 경로를 reviewer 가 검증한다.

#### 7. Machine Hygiene Gate

- broken Markdown link 0
- wikilink 와 file URI 0
- duplicate stem/body 0
- frontmatter 와 title heading 누락 0
- 삭제된 legacy 경로 참조 0
- 비허브 120 줄 초과는 분리 검토

이 게이트는 필요조건이지만 내용 완료의 충분조건이 아니다.

### 범위 재설계

#### Foundations

역할을 routing layer 에서 learning entry layer 로 바꾼다.

필수 보강:

- 설치에서 첫 frame 까지의 전체 서사
- app components, lifecycle/process/state/resource curriculum
- thread, Binder, coroutine, scheduler 관계
- 증상에서 관찰 신호로 가는 최소 진단 예시
- app framework 중심 glossary 보강

#### System Services and Device Capabilities

다음 중 하나를 선택한다.

1. 폴더를 실제 범위에 맞게 `background-messaging-assistant-nfc` 로 rename 한다.
2. 현재 이름을 유지하고 system service 공통 모델과 주요 capability 를 보강한다.

이름을 유지할 경우 필수 범위:

- `Context.getSystemService()` 와 service lookup
- Binder/system_server, caller UID, permission/AppOps
- service availability, callback lifetime, IPC/service death
- connectivity, location, sensors, Bluetooth/connected device
- power, package/user/role, media/audio/camera
- biometrics/credentials, telephony, input/accessibility
- background work 의 WorkManager, JobScheduler, UIDT, DownloadManager, task-specific API 선택

#### Platforms and Form Factors

다음 중 하나를 선택한다.

1. 폴더를 `adaptive-large-screen-and-xr` 로 rename 한다.
2. 현재 이름을 유지하고 TV, Wear OS, Auto/Automotive 와 ChromeOS 고유 계약을 추가한다.

각 form factor 는 input, lifecycle, layout, system UI, capability, distribution, testing 관점을 갖는다.

### 작업 페이즈

#### Phase 0. 잘못된 완료 판정 철회와 오류 수정

- Batch A 와 D 의 `완료` 를 구조 pass 완료로만 기록한다.
- Batch D 의미 등급을 A45 / B42 / C20 / D1 로 교체한다.
- 확인된 PendingIntent/exact alarm 오류를 공식 문서 기준으로 수정한다.
- Background work 선택 모델의 누락을 보강한다.
- 전체 585 개에 동일한 의미 품질 audit 을 적용할 준비를 한다.

완료 조건:

- 사실 오류 D 노트가 먼저 수정된다.
- 이전 보고서가 의미 품질 완료를 주장하지 않는다.

#### Phase 1. Taxonomy 와 범위 확정

- top-level 폴더 제목과 실제 책임 범위를 비교한다.
- System Services 와 Platforms 의 expand/rename 을 결정한다.
- phone app baseline, AOSP/system, form factor, Google service surface 를 구분한다.
- 빠진 필수 cluster 와 과대 대표된 cluster 를 coverage matrix 에 기록한다.

완료 조건:

- 모든 top-level map 에 포함/제외 범위가 있다.
- 이름과 실제 내용이 충돌하지 않는다.

#### Phase 2. Learning Spine 작성

- 12 개 필수 장의 순서와 prerequisite 를 먼저 설계한다.
- 기존 원자 노트를 재료로 사용하되 링크 모음으로 끝내지 않는다.
- 각 장에 하나 이상의 실제 흐름과 확인 질문을 넣는다.
- 우선 pilot 은 `Build/Install에서 앱 첫 frame까지` 로 한다.

완료 조건:

- 독립 reviewer 가 pilot 문서만 읽고 설치, process start, component launch, first frame 의 책임을 설명한다.
- 사용자 검수 뒤 나머지 장을 확장한다.

#### Phase 3. Worked Example 작성

- 필수 예시 8 개를 작성한다.
- 예시마다 관련 계층과 원자 노트를 연결한다.
- 코드, 상태 전이, 관찰 신호를 필요한 만큼 포함한다.

완료 조건:

- 각 예시가 최소 세 계층을 끊기지 않는 서사로 연결한다.
- 링크를 열지 않아도 예시의 핵심 흐름을 이해할 수 있다.

#### Phase 4. Diagnostic Runbook 작성

- app launch, ANR, process death, permission denial, background delay, notification missing, jank, install/update 실패를 우선한다.
- 공식 도구와 실제 명령을 검증한다.
- 정상/실패 출력과 분기 기준을 기록한다.

완료 조건:

- reviewer 가 문서만 보고 재현과 첫 조사 단계를 수행할 수 있다.

#### Phase 5. Atomic Reference 의미 품질 pass

순서:

1. App components, lifecycle, process, state
2. UI/rendering, data, concurrency
3. Background, notification, system capability
4. Security, storage, networking
5. Build, testing, performance, release
6. AOSP/system internals 와 form factor

작업:

- C/D 노트를 사실, mechanism, example, evidence 기준으로 재평가한다.
- 추상 체크리스트를 상태 흐름이나 실제 선택 사례로 바꾼다.
- 중복 노트는 병합 후보로 올리고 감독 에이전트가 결정한다.
- 문서 역할보다 큰 제목은 rename 또는 scope 축소한다.

#### Phase 6. Graph 재구성

- Foundation map 을 learning spine 중심으로 바꾼다.
- top-level cluster map 누락 링크를 복구한다.
- 현재 unreachable 42 개를 0 개로 만든다.
- map → spine/example/runbook → atomic reference 순으로 탐색 계층을 분리한다.

#### Phase 7. 독립 독자 검수

Author 가 아닌 Reviewer 가 다음 테스트를 수행한다.

- 문서만 읽고 확인 질문에 답한다.
- worked example 의 단계와 실패 지점을 다시 설명한다.
- runbook 의 명령과 결과 해석을 검증한다.
- 범위 누락, 잘못된 단정, self-referential 문장을 찾는다.

사용자 검수 표본을 통과하기 전에는 batch 를 완료 처리하지 않는다.

#### Phase 8. 최종 운영화

- semantic audit dashboard 를 보존한다.
- 새 노트 템플릿을 역할별로 분리한다.
- 월간 link hygiene 와 분기별 content audit 을 분리한다.
- 최신성 영역에는 재검증 주기를 기록한다.

### 병렬 작업 원칙

학습 spine 과 taxonomy 가 확정되기 전에는 폴더별 대량 재작성을 병렬 실행하지 않는다. 잘못된 구조를 빠르게 확대할 수 있기 때문이다.

역할:

- Curriculum Architect: 학습 순서와 prerequisite 설계
- Author: spine, example, runbook 또는 atomic reference 작성
- Researcher: 공식 문서로 사실 검증
- Diagnostic Reviewer: 명령, 출력, 실패 분기 검증
- Reader Reviewer: 사전 지식이 적은 독자 관점에서 이해 가능성 평가
- Graph Reviewer: 실제 탐색 경로와 unreachable note 분석
- Supervisor: scope, 병합, rename, cross-folder link, 최종 등급 결정

Author 와 최종 Reviewer 는 분리한다. 작성자가 자신의 노트에 A 등급을 확정하지 않는다.

### 에이전트 보고 형식

```text
범위:
문서 역할: learning spine | worked example | diagnostic runbook | atomic reference | map | glossary
독자가 읽기 전에 알아야 할 것:
독자가 읽은 뒤 답할 수 있는 질문:
설명한 mechanism/state flow:
사용한 example 또는 observable evidence:
검증한 공식 출처:
불확실한 내용:
중복 또는 범위 문제:
독립 등급과 근거:
실행한 검증:
```

`수정 파일 수`, `링크 수`, `섹션 수`, `line count` 는 참고 지표로만 보고한다.

### 검증 지표

#### 기계 지표

```text
android_md
markdown_internal_links_broken
absolute_internal_links
repo_docs_links
agent_internal_links
duplicate_android_stems
exact_duplicate_groups
long_nonhub_120
active_missing_frontmatter
active_missing_title_heading
active_very_short_14
orphan_active_notes
foundation_unreachable_notes
foundation_two_hop_cluster_maps
```

#### 의미 지표

```text
learning_spine_chapters_complete
worked_examples_complete
diagnostic_runbooks_complete
clusters_without_mechanism
clusters_without_example
clusters_without_observable_evidence
scope_title_mismatches
unverified_version_claims
known_fact_errors
independent_reader_questions_passed
semantic_grade_A_B_C_D
```

### 리스크와 대응

#### Routing-only 문서 증가

대응:

- map 수를 늘리기 전에 learning spine 의 빈 장을 채운다.
- `자세한 내용은 다른 노트` 라는 문장만 있는 문서는 C 로 평가한다.

#### 추상 체크리스트 증가

대응:

- 각 checklist 에는 최소 하나의 실제 scenario 와 판정 결과를 연결한다.
- 실행 방법과 관찰 신호가 없으면 runbook 으로 인정하지 않는다.

#### 최신 정보가 영속적 원리를 압도

대응:

- stable mechanism 과 version snapshot 을 분리한다.
- 버전 번호보다 변경 가능한 계약과 재검증 지점을 설명한다.

#### AI hallucination

대응:

- 공식 1 차 출처만 사실 검증 근거로 사용한다.
- Author 와 Researcher/Reviewer 를 분리한다.
- 최소 하나의 concrete API/state/command claim 을 표본 대조한다.

#### 과도한 원자화

대응:

- 학습 서사와 worked example 에서는 필요한 중복을 허용한다.
- reference 중복과 교육을 위한 문맥 반복을 구분한다.
- 독자가 링크를 계속 열어야만 문장을 이해할 수 있으면 지나치게 분리된 것으로 본다.

### 수정된 우선순위

1. 알려진 사실 오류 수정
2. top-level taxonomy 와 scope 결정
3. Learning Spine pilot: build/install 에서 first frame 까지
4. app component/lifecycle/process/state curriculum
5. launch, permission, background, notification, jank runbook
6. System Services 와 Platforms 의 expand/rename
7. 나머지 atomic reference 의미 품질 pass
8. graph 와 운영 자동화

### 다음 액션

1. System Services 와 Platforms 의 expand/rename 결정을 내린다.
2. 12 장 Learning Spine 의 상세 목차와 확인 질문을 작성한다.
3. `Build/Install에서 앱 첫 frame까지` pilot 을 작성한다.
4. 독립 Reader/Research reviewer 와 사용자 검수를 통과시킨다.
5. pilot 기준이 확정된 뒤에만 나머지 장과 폴더 pass 를 병렬화한다.

### 진행 기록

#### Batch A. App Framework 구조 pass (2026-08-03)

- generic filler 제거와 원자 노트 구조 정리는 수행했다.
- 의미 품질과 독자 학습 가능성은 새 기준으로 재감사하지 않았다.
- 상태: **구조 pass 완료 / semantic completion 미확정**

#### Batch D. Foundations and Platforms 구조 pass 및 재감사 (2026-08-03)

- 구조 pass 당시 A71 / B37 / C0 / D0 으로 평가했으나 내용 중심 재감사에서 과대평가로 확인됐다.
- 재감사 결과: A45 / B42 / C20 / D1.
- `00_foundations`: routing 과 glossary 에는 유용하지만 curriculum 역할 실패.
- `04_system_services`: 개별 주제는 일부 유용하지만 scope 대표성 실패 및 사실 오류 1 건 확인.
- `07_platforms`: adaptive large screen/XR reference 로는 유용하지만 form factor 전체 범위와 구현·진단 깊이 부족.
- 상태: **구조 pass 완료 / semantic completion 철회 / Phase 0 완료 / Phase 1 taxonomy 대상**

#### Phase 0. 완료 판정 철회와 알려진 오류 수정 완료 (2026-08-03)

- Batch D 보고서에 재감사 A45 / B42 / C20 / D1 과 semantic completion 철회를 반영했다.
- PendingIntent identity 에서 extras 를 비교한다는 오류를 수정하고 충돌/정상 예시와 `dumpsys alarm` 관찰 절차를 추가했다.
- exact alarm 의 OS·target SDK·전달 방식·permission 조건을 공식 API reference 기준으로 분리했다.
- Background work 를 coroutine, WorkManager, JobScheduler, UIDT, FGS, AlarmManager, DownloadManager/task-specific API 로 다시 분류했다.
- expedited/long-running Worker, Android 16 quota, stop reason, checkpoint 와 실행 가능한 진단·테스트 절차를 보강했다.
- Author 와 별도의 감독 검수에서 Android Developers 공식 1 차 출처를 다시 대조했다.
- 상태: **Phase 0 완료 / 다음 단계 Phase 1 taxonomy 와 scope 확정**

#### Batch B. System Internals 구조 + 정확성 pass (2026-08-03)

이 batch 는 이 문서가 `Phase 1-10 / Batch A-D` 구조였던 시점의 지시(`01_system_internals` 전체를 폴더별 3 개 작업 에이전트로 병렬 재작성)에 따라 실행됐다. 작업 도중 이 문서가 Learning Spine/Worked Example/Diagnostic Runbook/Atomic Reference 구조로 교체되었고, 새 `병렬 작업 원칙` 은 "학습 spine 과 taxonomy 가 확정되기 전에는 폴더별 대량 재작성을 병렬 실행하지 않는다"고 명시한다. 그 원칙이 확정되기 전에 시작된 작업이므로, 아래는 구조/사실 정확성 개선 기록이며 새 기준의 semantic completion 판정이 아니다.

- 범위: `boot-and-runtime`(+`platform-modularity`), `kernel-and-hal`(+`platform-customization`), `ipc-and-process`/`graphics-and-media`/`connectivity` — 3 개 작업 에이전트, 전체 153 개 활성 노트 열람, 20 개 파일 수정.
- 계층 구분(app API/framework service/native service/kernel-HAL) 명시, 관찰 가능 신호·디버깅 진입점 보강, 지도 노트(`android-boot-and-runtime`, `init-service-contracts`, `hal-native-contracts`, `hal-native-boundary`, `platform-customization-contracts`, `platform-modularity-contracts`, `connectivity-contracts`, `android-connectivity`, `ipc-process-contracts`, `graphics-media-contracts`)에 읽는 순서·문제 분류 기준·비슷한 노트 차이 보강.
- 확인된 사실 오류 수정: HIDL deprecation 시점이 "Android 13"으로 잘못 서술된 것을 공식 문서(source.android.com) 기준 "Android 10"으로 정정하고, AIDL-for-HAL 도입 시점(Android 11)과의 시차를 명시.
- 감독 검수: git diff 20 개 파일 확인, wikilink/file URI/절대경로 링크/repo docs 링크/broken markdown link/duplicate stem 전체 0 건 재검증. `platform-modularity` 13 개 파일에 누락되어 있던 `aliases`/`date modified`/`date created` frontmatter 필드를 vault 관례에 맞춰 보강(기계 위생 정리, 이번 batch 에서 발견).
- 새 기준(mechanism, worked example, observable evidence, accuracy) 대비 미실시: 각 노트에 구체적 code/state 예시를 추가하는 작업, Author 와 분리된 Researcher/Reviewer 의 별도 fact-check pass, Learning Spine/Worked Example/Diagnostic Runbook 과의 연결.
- 상태: **구조 + 정확성 pass 완료 / 신규 기준 semantic completion 미확정 / 추가 batch 병렬 작업은 새 계획의 Phase 0(사실 오류 수정)·Phase 1(taxonomy 확정) 완료 전까지 보류**
