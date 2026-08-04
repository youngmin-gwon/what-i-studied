---
title: android-knowledge-base-quality-plan
tags: ["android", "knowledge-base", "quality-plan"]
aliases: []
date modified: 2026-08-04 12:05:00 +09:00
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

### 독자 경로와 전제 지식

이 지식 베이스에서 "초심자"는 프로그래밍이나 IDE 사용을 처음 배우는 사람이 아니라 **Android 생태계의 구성과 동작 관계를 처음 체계적으로 이해하려는 독자**를 뜻한다. Kotlin/Java 문법, Android Studio 설치, 버튼 위치, 첫 앱 따라 만들기 같은 일반 개발 입문 과정은 이 계획의 범위가 아니다.

독자 경로는 깊이로 나눈다.

- **개념 Learning Spine**: Android 경험이 적은 독자가 AOSP, Google, OEM, SoC vendor, SDK, Jetpack, Google Play services, 앱 artifact, runtime 계층, system service, security, form factor와 배포의 관계를 순서대로 이해한다. 개별 API 사용법보다 주체, 소유권, 호출, identity, state와 update 경계를 설명한다.
- **심화 reference와 진단 경로**: Learning Spine의 전체 모델을 바탕으로 AOSP/kernel/HAL, Binder, rendering, background policy, security gate, 성능과 배포 문제를 원자 노트와 runbook에서 깊게 확인한다.

개념 경로는 세부 내부 동작을 생략하는 요약본이 아니다. 처음 접하는 독자가 원자 노트를 읽을 수 있도록 필요한 인과관계를 본문에서 직접 설명하는 정본이다. 심화 경로는 개념 경로를 대체하지 않으며, 개념 경로도 링크 목록으로 심화 설명을 떠넘기지 않는다.

### 최종 목표

Android 지식 베이스는 개념 Learning Spine과 심화 reference를 통해 서로 다른 네 역할을 수행해야 한다.

1. Android 생태계 경험이 적은 독자가 Android의 전체 구성과 실행 모델을 순서대로 이해한다.
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

1. Android 생태계와 계약 접점
2. Android 플랫폼 실행 계층과 호출 경로
3. 소스에서 설치된 패키지까지
4. 매니페스트와 앱 컴포넌트
5. 태스크, 프로세스, 수명주기와 상태
6. 메인 스레드, Binder, 코루틴과 작업 수명
7. 입력, 리소스와 화면 프레임
8. 데이터, 저장소, 네트워크와 오프라인 복구
9. 식별 정보, 권한과 보안 경계
10. 시스템 기능과 백그라운드 실행
11. 관찰, 테스트와 품질 피드백
12. 호환성, 업데이트와 폼 팩터

각 장은 선행 지식, 실제 메커니즘, end-to-end 흐름, 최소 예시, 확인 질문, 다음 장을 포함한다.

현재 교육과정 준비 작업본은 [Android 생태계 개념 Learning Spine 준비](./android-ecosystem-conceptual-spine-preparation.md)에서 관리한다. 이 문서에는 생태계 개념 범위표, 12장 구조와 1·2장의 상세 개요가 있다. 검수를 반영한 실제 본문은 [1장 Android 생태계와 계약 접점](../00_foundations/learning-spine/01-android-ecosystem-and-contract-surfaces.md), [2장 Android 플랫폼 실행 계층과 호출 경로](../00_foundations/learning-spine/02-android-platform-execution-layers-and-call-paths.md), [3장 소스에서 설치된 패키지까지](../00_foundations/learning-spine/03-source-to-installed-package.md), [4장 매니페스트에서 컴포넌트 실행까지](../00_foundations/learning-spine/04-manifest-to-component-execution.md), [5장 화면, 프로세스, task와 사용자 상태는 독립적인 lifetime을 가진다](../00_foundations/learning-spine/05-independent-lifetimes-of-screen-process-task-and-state.md), [6장 메인 스레드, Binder, coroutine과 durable scheduler는 서로 다른 실행 책임을 진다](../00_foundations/learning-spine/06-main-thread-binder-coroutine-and-durable-work-lifetime.md), [7장 입력, 리소스 선택과 화면 프레임](../00_foundations/learning-spine/07-input-resource-selection-and-display-frame.md), [8장 데이터, 저장소, 네트워크와 offline recovery](../00_foundations/learning-spine/08-data-storage-network-and-offline-recovery.md), [9장 Identity, 권한과 독립적인 security gate](../00_foundations/learning-spine/09-identity-permission-and-independent-security-gates.md), [10장 기기 기능 발견과 background execution](../00_foundations/learning-spine/10-device-capability-discovery-and-background-execution.md), [11장 관찰, 테스트와 품질 feedback](../00_foundations/learning-spine/11-observation-testing-and-quality-feedback.md), [12장 호환성, update와 form factor](../00_foundations/learning-spine/12-compatibility-update-and-form-factor.md)에서 관리한다. Learning Spine 12개 장 전체가 완성됐다. 3~12장은 저작 세션 자체 검증만 마쳤고 별도 세션의 독립 검수는 아직이다.

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

#### 문서 작성 형식과 언어

- frontmatter가 있는 모든 Markdown 문서는 닫는 `---` 다음의 첫 번째 비어 있지 않은 텍스트를 반드시 `##` 제목으로 작성한다.
- 문서의 최상위 제목에 `#`을 사용하지 않는다. `##` 아래의 하위 구조는 `###`, `####` 순서로 작성한다.
- 제목과 설명 문장은 한글을 기본으로 작성한다.
- API, class, method, package, command, 도구, library, product, protocol처럼 번역하면 식별이나 정확성이 떨어지는 공식 용어는 영문을 유지한다.
- 일반 개념은 가능한 한 한글로 설명하고, 필요한 경우 첫 등장에 `한글 설명(English term)` 형태로 병기한다.
- `surface`, `lifetime`, `identity`, `state`, `artifact`, `boundary` 같은 영문 일반어를 장식적으로 반복하지 않는다. 문맥에 맞는 `접점`, `수명`, `식별 정보`, `상태`, `산출물`, `경계`를 우선 사용한다.
- 코드 식별자와 명령은 원문 그대로 backtick으로 감싼다.

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
- 먼저 `Android 생태계와 계약 접점`에서 생태계 주체, API 접점, 산출물, 업데이트 권한과 호환성 계약을 정의한다.
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

**진행 기록(2026-08-04): 필수 8개 Worked Example 작성 완료.** `00_foundations/worked-examples/`에 다음 8개 파일을 작성했다(Learning Spine에 지정된 폴더 경로가 없어 `learning-spine/`과 나란한 새 폴더로 배치).

1. [앱 아이콘 탭에서 첫 프레임까지](../00_foundations/worked-examples/01-app-icon-tap-to-first-frame.md) — 4·5·6·7·11장 연결. 실패 분기: 냉시작 중 ANR.
2. [사진 촬영, preview, 저장, 업로드까지](../00_foundations/worked-examples/02-photo-capture-preview-save-upload.md) — 7·8·9·10장 연결. 실패 분기: 카메라 접근 실패(권한/AppOps/점유 중 3원인 구분).
3. [deep link가 올바른 task와 화면 상태로 열리기까지](../00_foundations/worked-examples/03-deep-link-to-correct-task-and-screen-state.md) — 3·4·5장 연결. 실패 분기 대신 성공/인증필요 두 경로를 대비.
4. [FCM 전송에서 notification 표시와 탭 복구까지](../00_foundations/worked-examples/04-fcm-to-notification-display-and-tap-recovery.md) — 5·6·9·10·11장 연결. 실패 분기: 전달은 성공했지만 권한/채널로 표시가 막히는 사례.
5. [process death 뒤 편집 상태와 background work 복구](../00_foundations/worked-examples/05-process-death-recovery-of-edit-state-and-background-work.md) — 4·5·6·8장 연결. 실패 분기: draft 텍스트가 ViewModel에만 있어 소실되는 사례.
6. [permission이 있는데 API가 실패하는 사례](../00_foundations/worked-examples/06-permission-granted-but-api-fails.md) — 9·10장 연결. foreground/background 위치 권한 분리를 실제 버그 리포트로 추적.
7. [Compose jank를 UI state에서 SurfaceFlinger까지 좁히는 사례](../00_foundations/worked-examples/07-compose-jank-from-ui-state-to-surfaceflinger.md) — 7·11장 연결. 실패 분기: recomposition 횟수만 보고 잘못 진단하는 사례.
8. [signed artifact가 Play delivery를 거쳐 update되는 과정](../00_foundations/worked-examples/08-signed-artifact-through-play-delivery-to-update.md) — 3·11장 연결. 실패 분기: 로컬 서명 빌드와 Play 서명 빌드 간 서명 불일치로 업데이트가 거부되는 사례.

각 예시는 최소 3개 이상의 Android 책임 계층(요청/데이터/identity/thread-process/lifecycle/실패 신호)을 끊기지 않는 서사로 연결했고, 코드 예시와 관찰 가능한 신호(adb/dumpsys 명령, 로그, trace)를 포함했다. 새로 도입한 사실 주장은 WebFetch로 공식 문서 원문을 대조했고(예: TTID/TTFD와 `reportFullyDrawn()`, cold/warm/hot start 정의, `am start -W` 출력), 나머지는 Learning Spine 각 장에서 이미 검증한 인용을 재사용했다. 8개 파일 전체의 내부 링크(원자 노트·Learning Spine 장)와 외부 공식 문서 링크를 전수 확인해 broken 0건이다.

**상태: 저작 세션 자체 검증 완료 / 별도 세션의 독립 검수는 아직 미실시.**

**독립 검수(2026-08-04).** Author/Reviewer 분리 원칙에 따라 4개 subagent에 2개씩 병렬 위임(WE1~2, WE3~4, WE5~6, WE7~8). 각 subagent는 완료 기준(시작상태/입력/단계/성공결과/실패분기, 3계층 이상 연결, 코드+관찰신호, 링크 없이도 이해 가능한 서사) 충족 여부, 내부·외부 링크 전수 재확인, 핵심 인용 WebFetch 재대조, Learning Spine과의 일관성(특히 4장의 exported/ActivityNotFoundException 정정과 모순 없는지)을 검증했다.

- WE1, WE2, WE5, WE7, WE8: 발견 사항 없음 또는 선택적 개선 제안만 있어 PASS.
- **WE6 사실 오류(수정 완료).** "대략적 위치는 약 3km **반경**"이라고 썼으나, 공식 문서(`training/location/permissions`)는 "accurate to within about 3 square kilometers"로 **면적**을 말한다. 반경으로 잘못 읽으면 실제보다 약 9배 넓은 오차 범위를 암시한다. WE6과, 이 오류의 근원이었던 원자 노트 `04_system_services/device-capabilities/location-contracts/precise-and-approximate-location-are-separate-permissions.md`를 함께 "약 3제곱킬로미터 면적"으로 정정했다.
- **WE3 표기 혼동(수정 완료).** "1장 worked example의 냉시작 경로"라는 표현이 본문 전체가 "N장"을 Learning Spine 챕터를 가리키는 데만 쓰는 관습과 충돌해, 독자가 Learning Spine 1장에 냉시작 내용이 있다고 오해할 수 있었다. "WE1(앱 아이콘 탭에서 첫 프레임까지)"로 명확히 정정했다.
- **WE4 인용 목록 누락(수정 완료).** 본문에서 4장(프로세스 재진입)과 8장(누락 복구)을 명시적으로 인용하면서도 상단 요약 문장과 "관련 Learning Spine 장" 목록에는 5·6·9·10·11장만 있었다. 두 곳 모두 4·8장을 추가했다.
- 부가로 WE5의 리다이렉트된 WorkManager URL을 canonical URL로, WE7의 부정확한 코드 주석 1건을 다듬었다(둘 다 사소, 판정에 영향 없음).

8개 전 파일 재검증 결과 내부 링크는 여전히 전수 resolve, 신규 사실 주장은 모두 공식 문서 원문과 일치 확인. **최종 상태: 8개 Worked Example 독립 검수 완료, 발견된 오류 모두 수정 반영. 사용자 최종 검수만 남음.**

#### Phase 4. Diagnostic Runbook 작성

- app launch, ANR, process death, permission denial, background delay, notification missing, jank, install/update 실패를 우선한다.
- 공식 도구와 실제 명령을 검증한다.
- 정상/실패 출력과 분기 기준을 기록한다.

완료 조건:

- reviewer 가 문서만 보고 재현과 첫 조사 단계를 수행할 수 있다.

**진행 기록(2026-08-04): 8개 필수 장애군 Diagnostic Runbook 작성 완료.** `00_foundations/diagnostic-runbooks/`에 Worked Example과 나란히 배치했다.

1. [앱 실행이 느리거나 첫 프레임이 뜨지 않는다](../00_foundations/diagnostic-runbooks/01-app-launch-slow-or-fails.md)
2. [ANR(Application Not Responding)이 발생한다](../00_foundations/diagnostic-runbooks/02-anr.md)
3. [process death 뒤 화면 상태가 사라진다](../00_foundations/diagnostic-runbooks/03-process-death-state-loss.md)
4. [권한이 있는데도 API가 실패하거나 거부된다](../00_foundations/diagnostic-runbooks/04-permission-denial.md)
5. [백그라운드 작업이 지연되거나 실행되지 않는다](../00_foundations/diagnostic-runbooks/05-background-work-delayed-or-not-running.md)
6. [알림이 오지 않는다(FCM 전달은 성공했는데 표시되지 않는다)](../00_foundations/diagnostic-runbooks/06-notification-missing.md)
7. [화면이 끊긴다(jank, dropped frames)](../00_foundations/diagnostic-runbooks/07-jank-dropped-frames.md)
8. [설치 또는 업데이트가 실패한다](../00_foundations/diagnostic-runbooks/08-install-update-failure.md)

각 runbook은 필수 구성(증상과 재현 조건, 실패 경계의 우선순위, 사용할 adb/dumpsys/cmd/logcat/trace 명령과 그 필드를 보는 이유, 정상/실패 신호, 다음 조사 경로, OS/API/target SDK 조건)을 모두 갖췄다. 이미 Learning Spine과 Worked Example에서 공식 문서로 검증한 사실을 우선 재사용했고, 새로 등장한 구체적 도구·필드(`Displayed` 로그 형식, ANR의 5가지 공식 트리거 조건과 `/data/anr/` trace 경로, `dumpsys jobscheduler`의 constraint/quota/standby bucket 필드)는 이번에 WebFetch로 공식 문서 원문을 대조했다. 8개 파일 전체 내부 링크(64개)와 외부 공식 문서 링크(16개)를 전수 확인해 broken 0건이다.

각 runbook은 대응하는 Worked Example로 상호 링크했다(예: RB1↔WE1, RB3↔WE5, RB4↔WE2·WE6, RB6↔WE4, RB7↔WE7, RB8↔WE8). Runbook은 "증상이 있을 때 무엇을 어느 순서로 확인할지"를 다루고, Worked Example은 "왜 그런 일이 일어나는지"를 다루도록 역할을 분리했다.

**독립 검수(2026-08-04).** 4개 subagent에 2개씩 병렬 위임(RB1~2, RB3~4, RB5~6, RB7~8). 완료 기준 충족 여부, 명령어 문법 정확성, 내부·외부 링크, 핵심 인용 WebFetch 재대조, Worked Example·Learning Spine과의 일관성을 검증했다.

- RB3, RB4, RB5, RB6: 발견 사항 없음(PASS).
- **RB1 수정.** 3단계(TTFD 확인)만 다른 단계와 달리 관찰 명령이 없어 보강했다(`reportFullyDrawn()` 호출 시 logcat에 남는 `Fully drawn ... +1s54ms` 형식을 공식 문서로 확인해 추가). 1단계의 "ANR 메시지와 함께 끝난다"는 근거를 확인하지 못한 서술을 "비정상적으로 오래 걸리거나 응답 없이 멈춘다"로 완화했다.
- **RB2 수정.** 1단계 `adb root`가 production(user) 빌드 기기에서는 실패한다는 점과 그 대안(`adb bugreport`, API 30+ `ApplicationExitInfo.getTraceInputStream()`, Android vitals ANR 리포트)이 누락돼 있어 추가했다 — 이 runbook이 다루는 "Play Console에서 ANR율 상승" 시나리오의 상당수가 정확히 이 production 빌드 케이스였다.
- **RB7 수정.** `dumpsys gfxinfo <pkg>` 명령에 `adb shell` 접두사가 빠져 있어 정정하고 코드블록으로 분리했다. 이 단계에 정상/실패 신호 설명이 없어 보강했다.
- **RB8 수정.** "targetSdkVersion 미충족 시 설치 자체가 거부된다"는 서술이, 실제로는 대부분 **설치 이전 빌드 단계**(manifest merger 오류)에서 걸러진다는 사실과 다르게 "설치 거부"로 단정하고 있어 정정했다. 구버전 툴체인에서 우회된 경우에만 설치 시점 `INSTALL_FAILED_VERIFICATION_FAILURE`로 나타난다는 점을 명시했다.

수정 후 8개 파일 전체 내부 링크 재확인 결과 broken 0건. **최종 상태: 8개 Diagnostic Runbook 독립 검수 완료, 발견된 문제 모두 수정 반영.**

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

1. 1장 `Android 생태계와 계약 surface` 상세 outline을 사용자와 독립 Reader/Research reviewer가 검수한다.
2. 검수 결과를 반영해 1장 본문을 작성한다.
3. `Build/Install에서 앱 첫 frame까지` pilot을 작성한다.
4. pilot을 독립 Reader/Research reviewer와 사용자 검수에 통과시킨다.
5. 1장과 pilot 기준이 확정된 뒤에만 나머지 장과 폴더 pass를 병렬화한다.

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

#### Phase 1. Taxonomy 와 범위 확정 (2026-08-03)

착수 전 사용자와 함께 "독자 트랙과 전제 지식" 분리를 먼저 확정했다(위 섹션). 그 뒤 8 개 top-level 폴더의 실제 노트 수와 하위 구조를 전수 조사해 coverage matrix 를 작성했다.

**Coverage matrix**

| 폴더 | 노트 수 | 최상위 map | 실제 하위 범위 | 제목 대비 평가 |
| --- | --- | --- | --- | --- |
| `00_foundations` | 53 | 있음 (`android-foundation-map`) | glossary, history, learning, overview | Batch D 재감사 기준 curriculum 역할 미흡 (기존 기록 유지) |
| `01_system_internals` | 153 | **없음** (하위 클러스터별 map 만 존재: `android-boot-and-runtime`, `android-connectivity` 등) | boot-and-runtime, connectivity, graphics-and-media, ipc-and-process, kernel-and-hal, platform-customization, platform-modularity | 통합 진입 지도 부재 — 독자가 폴더 전체를 2 단계 이내로 조망할 단일 지점이 없음 |
| `02_app_framework` | 227 | **없음** (하위 클러스터별 map 만 존재) | architecture, data, dependency-injection, jetpack-compose, navigation, ui | vault 최대 규모 폴더인데 통합 지도 부재는 Graph Gate 리스크 |
| `03_packaging_deployment` | 42 | 있음 (`android-packaging-deployment`) | build/sign/배포/CI 4 축 | 제목과 일치 |
| `04_system_services` | 28 | 있음 (`android-system-services-and-device-capabilities`) | background-work, notification/FCM, assistant/agent, NFC 4 개뿐 | **제목(system services 전체)이 실제 범위(4 개 표면)보다 훨씬 넓음** |
| `05_security_privacy` | 28 | 있음 (`android-security-and-privacy`) | integrity, permission/sandbox, platform-hardening, secure-storage, security-practices | 제목과 일치 |
| `06_testing_performance` | 27 | 있음 (`android-performance-quality-and-build-optimization`, performance 하위) | performance-contracts(8)+benchmark-baseline-contracts(6), testing-quality-contracts(6), debugging-contracts(3) | **반대 방향 불일치**: 제목("성능, 품질, 빌드 최적화")이 실제보다 좁다. testing/debugging 클러스터가 이미 충실한데 제목에 드러나지 않는다 |
| `07_platforms` | 27 | 있음 (`android-platforms-and-form-factors`) | large-screen, windowing, XR 3 개뿐 | **제목(폼팩터 전체)이 실제 범위보다 넓음. TV/Wear OS/Auto/ChromeOS 전무** |

**System Services 와 Platforms 결정 (사용자 확정)**

두 폴더 모두 **이름 유지 + 범위 확장**으로 결정했다 (rename 으로 축소하지 않음).

- `04_system_services` 목표 범위: 현재 4 개(background-work, notification/FCM, assistant/agent, NFC)에 location, sensors, power, package/user/role, media/audio/camera, biometrics/credentials, telephony, input/accessibility 를 추가한다. `Context.getSystemService()` 공통 lookup 모델과 Binder/system_server, caller UID, permission/AppOps 공통 계약도 별도 클러스터로 필요하다(계획 원문 line 300-307 유지).
- `07_platforms` 목표 범위: 현재 3 개(large-screen, windowing, XR)에 TV, Wear OS, Auto/Automotive, ChromeOS 고유 계약을 추가한다. 각 폼팩터는 input/lifecycle/layout/system UI/capability/distribution/testing 관점을 갖춰야 한다.
- **이 확장은 Phase 1 안에서 즉시 작성하지 않는다.** 신규 클러스터 작성은 우선순위 목록의 "6. System Services 와 Platforms 의 expand/rename"에 해당하며, Learning Spine pilot(Phase 2-3) 이후 착수한다. 지금은 두 map 노트에 목표 범위와 현재 공백을 명시적으로 기록해 제목과 내용의 불일치를 정직하게 드러내는 것까지만 한다(아래).
- `04_system_services`/`07_platforms` map 노트에 "포함 예정이나 아직 없음" 목록을 추가해 Coverage Gate("빠진 영역은 추가하거나 제목과 map 에서 명시적으로 제외한다")를 임시 조건부로 충족시켰다. 실제 신규 노트 작성 전까지 이 상태는 "확장 결정 + 공백 공개"이지 "완료"가 아니다.

**새로 발견된 taxonomy 문제**

- `01_system_internals`(153 개)와 `02_app_framework`(227 개, vault 최대)에는 하위 클러스터 map 만 있고 폴더 전체를 조망하는 통합 진입 지도가 없다. `00/03/04/05/06/07`은 모두 통합 map 이 있어 구조가 비대칭적이다. Foundation map 에서 이 두 폴더로 진입할 때 어느 하위 클러스터부터 읽어야 하는지 판단할 단일 지점이 없다는 뜻이며, Graph Gate(2 단계 이내 도달)와 직결된다. Phase 6(Graph 재구성) 전에 두 폴더의 통합 map 신설 여부를 별도로 결정해야 한다.
- `06_testing_performance` testing 비중을 후속 조사했다(2026-08-03). 가설("성능/빌드 최적화 편중")은 사실이 아니었다. 실제로는 `testing`(6개: 테스트 레이어 선택 기준, unit/integration/UI/E2E 실패 신호 구분, Compose UI 테스트 selector, screenshot testing, flaky/regression, coroutine/flow 테스트)과 `debugging`(3개: ADB/에뮬레이터/실기기 매트릭스와 PR/nightly 배치, Gradle Managed Devices, logcat/crash/ANR/debugger 구분) 클러스터가 이미 개념적으로 충실하다. 대신 반대 방향 문제를 발견했다: 최상위 map 제목("Android 성능, 품질, 빌드 최적화 지도")이 이미 존재하는 testing/debugging 클러스터를 반영하지 못해 제목이 실제 범위보다 좁다(04/07 폴더와 반대 패턴). 추가로 확인된 실제 공백: CI/디바이스 팜 통합(Firebase Test Lab, 파이프라인 sharding)은 몇 문장씩만 산발적으로 언급되고 전용 클러스터가 없으며, 접근성 테스트(TalkBack 등)는 다루지 않는다. Phase 6(Graph 재구성) 또는 Phase 1 coverage 재검토 시 map 제목을 실제 범위(성능·테스트·디버깅·빌드 최적화)에 맞게 조정할지 결정이 필요하다.

완료 조건 대비 상태:

- 모든 top-level map 에 포함/제외 범위가 있다 → `04_system_services`/`07_platforms` 는 이번에 보강, 나머지는 기존 상태 유지.
- 이름과 실제 내용이 충돌하지 않는다 → rename 대신 "확장 결정 + 공백 명시"로 임시 충족. 실제 신규 클러스터 작성 전까지 잠정적.

상태: **Phase 1 taxonomy 결정 및 coverage matrix 작성 완료 / 신규 클러스터 저작은 Phase 2-3 이후 후속 작업으로 이월 / `01_system_internals`·`02_app_framework` 통합 map 신설 여부는 미결정으로 기록**

#### Phase 1 후속. system_services/platforms 신규 노트 표본 fact-check (2026-08-03)

1장 Learning Spine 본문 작성과 병행 가능한 작업으로, Phase 1에서 확장 작성한 `04_system_services`/`07_platforms` 13개 클러스터·52개 신규 노트에 계획의 리스크 대응란("최소 하나의 concrete API/state/command claim을 표본 대조한다")을 적용했다.

- 버전·동작 종속적 주장 6건을 공식 1차 출처(WebFetch)로 표본 대조: 대략적 위치 permission 분리(Android 12) 확인, background 위치 permission 시스템 다이얼로그 제거(Android 11) 확인, 패키지 가시성 제한(Android 11) 확인, CredentialManager의 패스키/비밀번호/연동 로그인 통합 확인, carrier privilege의 UICC 인증서 해시 대조 메커니즘과 `hasCarrierPrivileges()` 확인. RoleManager의 Android 10 도입 시점은 공식 reference 페이지가 JS 렌더링이라 자동 도구로 재확인하지 못해 수동 확인이 필요한 항목으로 남겼다.
- 사실 오류 1건 수정: `location-permission-splits-into-foreground-and-background-tiers.md`에서 "foreground/background 권한을 동시에 요청하면 시스템이 foreground만 부여할 수 있다"는 서술이 공식 문서("the system ignores the request and doesn't grant your app either permission")와 달랐다. 실제로는 두 권한 모두 거부됨으로 정정했다.
- broken 외부 링크 5건 수정: RoleManager(잘못된 default-apps URL), FusedLocationProviderClient(developer.android.com이 아니라 developers.google.com 도메인), SubscriptionManager 노트의 존재하지 않는 multisim 가이드 링크(삭제), Android Automotive 개요(`what_is_android_automotive` → `what_automotive`), Wear OS 개요(`training/wearables/overview` → `training/wearables`).
- 52개 신규 노트 전체의 외부 링크 68개를 재수집해 전수 재검증했다. 남은 broken link 0건.
- 상태: **13개 클러스터 표본 fact-check 및 broken link 전수 수정 완료 / RoleManager 도입 시점 등 일부 항목은 수동 재확인 필요로 표시 / 나머지 39개 노트의 세부 주장 전수 검증은 미실시(표본 조사 범위)**

#### Phase 2. Android 생태계 개념 Learning Spine (2026-08-03)

- [Android 생태계 개념 Learning Spine 준비](./android-ecosystem-conceptual-spine-preparation.md)에 생태계 개념 범위표와 12장 후보 구조를 작성했다.
- AOSP, Google, OEM/ODM, SoC 공급자, Android 플랫폼 API, NDK/JNI, Jetpack/AndroidX, Google Play services, Google Play와 설치 프로그램의 소유·배포 경계를 분리했다.
- 앱 산출물, 설치 식별 정보, 실행 계층, 독립 수명, UI 입출력, 데이터 복구, 보안 관문, 시스템 기능, 폼 팩터와 호환성 축의 연결 공백을 기록했다.
- 1장 `Android 생태계와 계약 접점`의 상세 개요, 핵심 도표, 대표 사례, 오해 교정과 독자 확인 질문을 작업본에 추가했다.
- [1장 Android 생태계와 계약 접점](../00_foundations/learning-spine/01-android-ecosystem-and-contract-surfaces.md) 본문을 작성했다. AOSP·호환성·GMS, 생태계 주체, 플랫폼 API·Jetpack·Google Play services, 위치 기능 실패 사례와 새 기능 분류 질문을 하나의 개념 흐름으로 연결했다.
- 실제 본문에 대해 독자 관점, 플랫폼 사실관계, 후속 실행 계층과의 장 경계를 독립 검수하고 High·Medium 지적을 수정했다.
- 2장 `Android 플랫폼 실행 계층과 호출 경로`의 상세 개요와 [실제 본문](../00_foundations/learning-spine/02-android-platform-execution-layers-and-call-paths.md)을 작성했다. 로컬 호출, 시스템 서비스 호출, 하드웨어 기능 호출을 구분하고 센서 제어 요청과 이벤트 반환을 대표 흐름으로 연결했다.
- 2장 실제 본문을 독자, 플랫폼 사실관계와 후속 장 경계 관점에서 독립 검수하고 지적 사항을 반영했다.
- **별도 세션의 2차 독립 검수(2026-08-03).** 1장·2장 저작 세션과 무관한 검수자가 재검수했다. 내부 링크 17개·외부 공식 출처 링크 14개 전수 확인(broken 0건), 버전·플랫폼 사실 3건 표본 대조(WebFetch): 비공개 SDK 인터페이스 제한 서술 확인, HAL binderized/same-process 배치가 Android 버전·기기 구조에 따라 달라진다는 서술 확인, Binder의 caller UID 보존 서술은 인용한 특정 문서에 명시되어 있지 않으나 잘 알려진 사실이라 오류로 보지 않음. Reader 관점에서 1장 확인 질문 8개·2장 확인 질문 10개 중 표본을 문서만 읽고 직접 답변 가능함을 확인. 발견된 오류나 broken link 없음.
- 상태: **Phase 2 진행 중 / 1장·2장 본문 작성 완료 / 저작 세션 자체 검수 + 별도 세션 2차 독립 검수 모두 완료(추가 지적 없음) / 사용자 검수 대기**
- **3장 `소스에서 설치된 패키지까지` 본문을 별도 세션이 작성했다(2026-08-03).** [실제 본문](../00_foundations/learning-spine/03-source-to-installed-package.md)에서 build variant→AAPT2/D8/R8→APK·AAB 산출물, AAB(게시)/APK(설치) 역할 분리, `applicationId`·서명 인증서·숫자 appId라는 세 가지 다른 축의 식별자, PackageInstaller/PackageManager의 검증·UID 할당·컴포넌트 registry 등록, 업데이트·서명불일치·삭제후재설치·force-stop의 UID·데이터 연속성 차이를 하나의 흐름으로 연결했다. 서명 불일치로 업데이트가 거부되는 사례를 실패 흐름으로 포함했다. 2장의 "다음 장으로 이어지는 질문" 5개를 모두 본문에서 직접 답했다.
- 저작과 동시에 공식 출처 대조: Android 앱 서명 문서에서 "인증서가 다르면 업데이트가 거부되고 새 패키지로 설치된다"는 서술을, Android 보안 문서(app sandbox)에서 "앱마다 고유 UID를 할당해 프로세스를 격리한다"는 서술을 확인 후 인용했다. 내부 링크 8개, 외부 링크 6개 전수 확인(broken 0건).
- 기존 `03_packaging_deployment`의 AAB/서명/버전 관련 원자 노트(Play 서명 키 분리, applicationId/versionCode 계약, R8 등)를 재사용하고 링크로 연결했다. Phase 2 준비 문서가 지적한 "PackageManager가 설치된 앱을 OS-visible entity로 만드는 중간 연결"(문자열 식별자 → 검증 → 숫자 appId/UID → 컴포넌트 registry)은 기존 원자 노트에 없던 내용이라 이 장에서 새로 연결했다.
- 상태: **3장 본문 작성 완료 / 저작 세션 자체 링크·사실 검증 완료 / 별도 세션의 독립 Reader·Research 검수와 사용자 검수는 아직 미실시**
- **4장 `매니페스트에서 컴포넌트 실행까지` 본문을 작성했다(2026-08-03).** [실제 본문](../00_foundations/learning-spine/04-manifest-to-component-execution.md)에서 매니페스트 선언의 컴포넌트 registry 등록, 명시적/암시적 Intent의 해석 방식(action/category/data 매칭), exported·permission·package visibility라는 서로 다른 게이트, 컴포넌트 활성화 요청이 AMS→Zygote fork→specialization→ActivityThread attach 순으로 프로세스 상태를 확인하는 과정, `android:process`로 한 앱이 여러 프로세스로 나뉠 때의 IPC 통신 계약 전환을 하나의 흐름으로 연결했다. exported=false 컴포넌트를 외부에서 명시적으로 호출했을 때 권한 거부로 실패하는 사례를 실패 흐름으로 포함했다. 3장의 "다음 장으로 이어지는 질문" 4개를 모두 본문에서 직접 답했다.
- 저작과 동시에 공식 출처 대조(WebFetch): `<activity>` exported 문서에서 intent-filter가 있을 때의 기본값·권장값 서술을, Android 12 behavior changes 문서에서 "intent-filter가 있는 컴포넌트의 exported 미선언 시 Android 12 이상 기기에 설치 자체가 불가능하다"는 경고문을 원문으로 확인 후 인용했다. Processes and app lifecycle 문서에서 프로세스 생성 조건과 5단계 중요도 계층을 확인했다. 내부 링크 12개, 외부 링크 6개 전수 확인(broken 0건).
- 기존 `02_app_framework`(manifest/component/intent-filter/exported/package-visibility 원자 노트)와 `01_system_internals`(AMS, Zygote socket, ActivityThread attach, process priority 원자 노트)를 재사용하고 링크로 연결했다. 두 클러스터가 이미 개별 계약은 갖고 있었지만, "매니페스트 선언 → registry → Intent resolution → AMS의 프로세스 상태 확인 → Zygote fork" 로 이어지는 인과 순서를 하나의 서사로 잇는 문서는 없었다.
- 상태: **4장 본문 작성 완료 / 저작 세션 자체 링크·사실 검증 완료 / 별도 세션의 독립 Reader·Research 검수와 사용자 검수는 아직 미실시**
- **5장 `화면, 프로세스, task와 사용자 상태는 독립적인 lifetime을 가진다` 본문을 작성했다(2026-08-03).** [실제 본문](../00_foundations/learning-spine/05-independent-lifetimes-of-screen-process-task-and-state.md)에서 준비 문서의 "독립적인 lifetime" 모델(설치된 패키지 identity, Linux process, task/back stack, component 인스턴스, ViewModel, transient UI state, 영속 저장소)을 6개 사건(configuration change, 뒤로 가기로 인한 finish, task 제거, 시스템에 의한 process death, force-stop, uninstall) × lifetime 비교표로 연결했다. 이는 Phase 1 종료 전 준비 작업 3번이 요구한 "5장의 독립 lifetime 표와 configuration change/process death/task removal/force-stop/uninstall 비교 사례"에 해당한다. 화면 회전 직후 입력값 소실(configuration change)과 오랜 백그라운드 이후 선택 상태 소실(process death)을 대비되는 실패 사례로 포함했다. 4장의 "다음 장으로 이어지는 질문" 3개를 모두 본문에서 직접 답했다.
- 저작과 동시에 공식 출처 대조(WebFetch): Activity state changes 문서에서 "시스템이 프로세스를 종료할 때 onDestroy 호출이 보장되지 않는다"는 원문과 configuration change의 onPause→onStop→onDestroy→재생성 콜백 순서를, Activity lifecycle 문서에서 `rememberSaveable`/`ViewModel`/영속 저장소를 조합하라는 공식 권장 서술을 원문으로 확인 후 인용했다. force-stop 이후 자동 재시작이 억제되는 정확한 조건은 이번 세션에서 fetch 가능한 공식 문서로 재확인하지 못해 본문과 검증일 각주에 "수동 확인 필요"로 명시했다(RoleManager 사례와 동일한 처리 원칙). 내부 링크 9개, 외부 링크 5개 전수 확인(broken 0건).
- 기존 `02_app_framework`(configuration change, process death recovery, activity lifecycle, task/back stack, ViewModel, SavedStateHandle, context-registered receiver 원자 노트)와 `01_system_internals`(AMS, process priority 원자 노트)를 재사용하고 링크로 연결했다. 3장의 UID/데이터 연속성 표(force-stop/재설치/서명불일치)는 반복하지 않고 링크로만 연결해 이 장은 lifetime 축에만 집중했다.
- 상태: **5장 본문 작성 완료 / 저작 세션 자체 링크·사실 검증 완료 / force-stop 자동 재시작 억제 조건 1건은 수동 확인 필요로 명시 / 별도 세션의 독립 Reader·Research 검수와 사용자 검수는 아직 미실시**
- **6장 `메인 스레드, Binder, coroutine과 durable scheduler는 서로 다른 실행 책임을 진다` 본문을 작성했다(2026-08-03).** [실제 본문](../00_foundations/learning-spine/06-main-thread-binder-coroutine-and-durable-work-lifetime.md)에서 main thread/Looper·Handler(실행 순서), Binder/thread pool(프로세스 경계와 동시성), coroutine의 Dispatcher(실행 위치)·Scope(취소 가능한 lifetime), foreground service·WorkManager(사용자 가시성과 process 재시작을 넘는 지속성)를 "무엇을 결정하고 무엇을 결정하지 않는가" 비교표로 연결했다. "지금 동기화" 버튼 클릭이 네 계층을 모두 통과하는 worked example과, coroutine 안에서 느린 동기 Binder 호출을 main dispatcher로 기다리다 ANR로 이어지는 실패 사례를 포함했다. viewModelScope가 configuration change는 견디지만 지속성 요구와는 반대라는 점을 5장의 lifetime 모델과 직접 연결했다. 5장의 "다음 장으로 이어지는 질문" 3개를 모두 본문에서 직접 답했다.
- 저작과 동시에 공식 출처 대조(WebFetch): Processes and threads 문서에서 main thread가 같은 프로세스 호출을 직렬 처리한다는 서술과 다른 프로세스 호출이 Binder thread pool에서 실행된다는 서술을, Coroutines best practices 문서에서 viewModelScope가 configuration change를 자동으로 견딘다는 서술과 GlobalScope를 피해야 하는 이유를 원문으로 확인 후 인용했다. 내부 링크 14개, 외부 링크 5개 전수 확인(broken 0건).
- 기존 `01_system_internals`(IPC/process contracts, Binder transaction lifetime, Binder thread pool, ANR)와 `02_app_framework`(coroutine, ViewModel scope, foreground service, Service), `04_system_services`(WorkManager, 백그라운드 제한) 원자 노트를 재사용하고 링크로 연결했다. 개별 계약은 이미 있었지만 "이 네 계층이 같은 요청 하나를 놓고 서로 다른 축(순서/경계/취소/지속성)을 책임진다"는 통합 비교는 없었다.
- 상태: **6장 본문 작성 완료 / 저작 세션 자체 링크·사실 검증 완료 / 별도 세션의 독립 Reader·Research 검수와 사용자 검수는 아직 미실시**
- **7장 `입력, 리소스 선택과 화면 프레임` 본문을 작성했다(2026-08-03).** [실제 본문](../00_foundations/learning-spine/07-input-resource-selection-and-display-frame.md)에서 물리 입력이 EventHub→InputReader→InputDispatcher를 거쳐 대상 윈도우로 라우팅되는 경로, `ViewRootImpl`이 그 윈도우의 View 트리와 WindowManagerService를 잇는 다리라는 사실, 입력이 6장의 main thread 큐를 거쳐야 처리된다는 연결, configuration change가 단순 값 변경이 아니라 리소스 재선택을 요구해 5장의 Activity 재생성으로 이어지는 이유, View/Compose가 만든 그리기 명령이 Surface→BufferQueue→SurfaceFlinger/HWC 합성을 거쳐 화면이 되는 과정, 그리고 앱은 Surface만 받고 WindowManager가 SurfaceControl을 쥔 채 화면상 배치를 결정한다는 점을 하나의 루프로 연결했다. 이는 Phase 1 종료 전 준비 작업 4번이 지목한 "Window, ViewRootImpl, WindowManagerService와 SurfaceControl 공백"을 공식 문서 근거로 채운 것이다. 화면 회전 하나가 5·6·7장 모델을 모두 지나가는 worked example을 포함했다. 6장의 "다음 장으로 이어지는 질문" 3개를 모두 본문에서 직접 답했다.
- 저작과 동시에 공식 출처 대조(WebFetch/WebSearch): AOSP Input pipeline 문서에서 "InputReader sends input events to the InputDispatcher which forwards them to the appropriate window"를, AOSP SurfaceFlinger/WindowManager 문서에서 "WindowManager keeps the SurfaceControl instance to manipulate the appearance of the app on the screen"과 layer가 surface+SurfaceControl의 조합이라는 정의를, Handle configuration changes 문서에서 Activity 재생성이 대체 리소스 자동 재로드를 위한 것이라는 서술을 원문으로 확인 후 인용했다. ViewRootImpl↔WindowManagerService 간 window session 통신 세부는 WebSearch로 교차 확인했으나 1차 공식 문서 원문 인용은 아니므로 검증일 각주에 명시했다. 내부 링크 12개, 외부 링크 6개 전수 확인(broken 0건).
- 기존 `01_system_internals/graphics-and-media`(rendering pipeline, Surface, BufferQueue, SurfaceFlinger, RenderThread, VSync/Choreographer, jank)와 `02_app_framework`(configuration change, View/Compose 비교, Compose frame pipeline), `04_system_services`(InputManager) 원자 노트를 재사용하고 링크로 연결했다. 그래픽 파이프라인 뒷부분(Surface 이후)은 원자 자료가 이미 강했지만, "입력이 어느 윈도우로 갈지 결정되는 과정"과 "그 판단이 ViewRootImpl을 거쳐 View 트리·main thread로 연결되는 과정"은 이 장에서 새로 연결했다.
- 상태: **7장 본문 작성 완료 / 저작 세션 자체 링크·사실 검증 완료 / 별도 세션의 독립 Reader·Research 검수와 사용자 검수는 아직 미실시**
- **8장 `데이터, 저장소, 네트워크와 offline recovery` 본문을 작성했다(2026-08-03).** [실제 본문](../00_foundations/learning-spine/08-data-storage-network-and-offline-recovery.md)에서 준비 문서의 "UI event/in-memory state → repository/local transaction → durable source of truth/outbox → scheduler constraint/quota → network/server reconciliation → local state 갱신 → UI observation" 흐름을 5장(ViewModel이 process death를 못 견딤)·6장(WorkManager 지속성)과 명시적으로 연결해 하나의 순환으로 완성했다. 데이터 수명·소유권 기준 저장소 선택표, 공식 문서의 "lazy writes"(로컬 우선 쓰기 + 지연된 서버 알림) 패턴, WorkManager 재시도의 idempotency·checkpoint 요구, 앱 API가 보는 네트워크 상태와 시스템 정책 상태의 구분을 연결했다. 오프라인 즐겨찾기 추가라는 worked example과, Room·DataStore 두 저장소 쓰기를 하나의 트랜잭션으로 착각하는 실패 사례를 포함했다. 7장의 "다음 장으로 이어지는 질문" 3개를 모두 본문에서 직접 답했다.
- 저작과 동시에 공식 출처 대조(WebFetch): App architecture data layer/offline-first 문서에서 "local data source가 canonical source of truth"라는 원칙과 "lazy writes"(로컬 우선 쓰기 후 네트워크 알림 큐잉) 정의를, WorkManager 문서에서 동기화 실패 시 `Result.retry()`로 지수 백오프 재시도한다는 서술을 원문으로 확인 후 인용했다. 내부 링크 11개, 외부 링크 4개 전수 확인(broken 0건).
- 기존 `02_app_framework/data`(Repository/Flow/StateFlow/저장소 선택), `04_system_services/background-and-notifications`(WorkManager, 실패 비용 기반 API 선택, 영속 작업 상태), `01_system_internals/connectivity`(ConnectivityManager vs ConnectivityService/netd 계층) 원자 노트를 재사용하고 링크로 연결했다. 개별 계약은 강했지만 "화면 관찰 → 로컬 우선 쓰기 → 지연된 동기화 → idempotent 재시도 → 다시 로컬 관찰로 복귀"라는 순환 서사, 그리고 이것이 5·6장의 lifetime/지속성 모델과 어떻게 맞물리는지는 이 장에서 새로 연결했다.
- 상태: **8장 본문 작성 완료 / 저작 세션 자체 링크·사실 검증 완료 / 별도 세션의 독립 Reader·Research 검수와 사용자 검수는 아직 미실시**
- **9장 `Identity, 권한과 독립적인 security gate` 본문을 작성했다(2026-08-03).** [실제 본문](../00_foundations/learning-spine/09-identity-permission-and-independent-security-gates.md)에서 3장의 package/서명 identity·UID가 모든 보안 판정의 입력이 된다는 점을 출발점으로, sandbox(UID/프로세스 경계) → Binder 호출의 커널 검증 UID/PID(6장과 연결) → manifest 선언·protection level(normal/dangerous/signature, signature는 3장의 서명 identity와 직결) → runtime permission 사용자 승인 → AppOps(permission과 독립적인 실행 시점 거부) → special app access(설정 기반) → SELinux(root로도 우회 불가한 mandatory policy) → 서버 authorization(클라이언트 무결성 신호는 대체 불가)까지 8개 gate를 "판정 주체/시점/독립성" 비교표로 연결했다. 카메라 촬영 실패를 다섯 gate 순으로 좁혀가는 worked example과, 권한을 한 번만 확인하고 AppOps 자동 회수를 놓치는 실패 사례를 포함했다. 8장의 "다음 장으로 이어지는 질문"은 이번 장이 직접 다루는 주제는 아니었으나, 대신 준비 문서의 "Framework API에서 hardware capability까지" 흐름 중 권한 판정 구간을 이 장이 전담해 채웠다.
- 저작과 동시에 공식 출처 대조(WebFetch): Permissions on Android 문서에서 normal/dangerous/signature protection level 정의(특히 signature 권한이 "같은 인증서로 서명된 경우에만" 부여된다는 서술)와 "권한이 이미 부여됐다고 가정하지 말라"는 경고를, Play Integrity 개요 문서에서 token이 서버 검증 대상이라는 서술을 원문으로 확인 후 인용했다. 내부 링크 12개, 외부 링크 3개 전수 확인(broken 0건).
- 기존 `05_security_privacy`(sandbox, permission-contracts, SELinux, Play Integrity, defense-in-depth)와 `04_system_services/service-lookup`(호출자 UID/PID 검사, AppOps 이중 게이트, getSystemService의 Binder 위임) 원자 노트를 재사용하고 링크로 연결했다. 개별 게이트는 각자 잘 설명돼 있었지만 "이것들이 하나의 순차 파이프라인이 아니라 서로 다른 시점에 서로 다른 주체가 내리는 독립 판정"이라는 통합 모델, 그리고 3장의 identity가 그 모든 판정의 공통 입력이라는 연결은 이 장에서 새로 만들었다.
- 상태: **9장 본문 작성 완료 / 저작 세션 자체 링크·사실 검증 완료 / 별도 세션의 독립 Reader·Research 검수와 사용자 검수는 아직 미실시**
- **10장 `기기 기능 발견과 background execution` 본문을 작성했다(2026-08-03).** [실제 본문](../00_foundations/learning-spine/10-device-capability-discovery-and-background-execution.md)에서 `<uses-feature>`(Google Play 배포 필터링용, 시스템 강제 아님)와 `hasSystemFeature()`/`canAuthenticate()` 같은 런타임 발견이 9장의 permission/AppOps gate보다 먼저 또는 별개로 필요하다는 점, 같은 기능이 AOSP platform/Google 서비스/OEM 구현 중 어디서 오는지에 따라 대체 경로가 달라진다는 점(1장 위치 사례의 일반화), 발견된 capability의 실제 호출 경로는 2·6·9장이 이미 설명한 것을 그대로 재사용한다는 명시, 하드웨어 부재/사용자 사전조건 미충족/권한거부라는 세 가지 실패가 서로 다른 UX를 요구한다는 점, 그리고 지속 작업이 durable state(8장)·scheduler(6장)에 더해 "결과의 사용자 가시성"(FCM은 전달, 알림은 표시라는 별개 계약)까지 갖춰야 완결된다는 점을 하나로 연결했다. 위치 기반 도착 알림 기능이 다섯 지점에서 실패할 수 있는 종합 worked example과, "durable 작업은 성공했지만 알림 채널 차단으로 사용자가 보지 못한" 실패 사례를 포함했다.
- 저작과 동시에 공식 출처 대조(WebFetch): `<uses-feature>` element 문서에서 "Android 시스템 자체는 설치 전 기능 지원 여부를 확인하지 않으며 이 선언은 정보성이고 Google Play 필터링에 쓰인다"는 서술을 원문으로 확인 후 인용했다. 내부 링크 8개, 외부 링크 4개 전수 확인(broken 0건).
- 기존 `04_system_services` 최상위 지도(내가 Phase 1에서 작성한 android-system-services-and-device-capabilities.md)와 `service-lookup-contracts`, `01_system_internals/platform-modularity`(feature availability 확인), `biometrics-credential-contracts`, `sensor-contracts`, `location-contracts`, `background-work-contracts`, `notification-messaging-contracts`를 재사용하고 링크로 연결했다. 개별 지도는 이미 "문제 분류" 표를 갖추고 있었지만, "기능 발견이 권한 확인보다 선행한다"는 순서, AOSP/Google/OEM 구분의 일반화, "durable 실행 성공과 사용자 가시성은 별개"라는 통합 논지는 이 장에서 새로 연결했다.
- 상태: **10장 본문 작성 완료 / 저작 세션 자체 링크·사실 검증 완료 / 별도 세션의 독립 Reader·Research 검수와 사용자 검수는 아직 미실시**
- **11장 `관찰, 테스트와 품질 feedback` 본문을 작성했다(2026-08-03).** [실제 본문](../00_foundations/learning-spine/11-observation-testing-and-quality-feedback.md)에서 1~10장에 흩어져 있던 진단 신호 언급(2장 `dumpsys location`, 4장 Permission Denial 로그, 6장 Perfetto main thread/Binder 구간, 8장 `WorkInfo`/`dumpsys jobscheduler`, 9장 `dumpsys appops`/`package`, 10장 `canAuthenticate()` 반환값)을 표로 회고한 뒤, logcat/crash/ANR/debugger/Profiler/Perfetto/dumpsys/Macrobenchmark가 서로 다른 질문에 답한다는 원칙, 테스트 레이어를 피드백 비용으로 고르는 기준, 회귀·flaky test가 릴리스 게이트 신뢰도 자체를 훼손한다는 점, 그리고 릴리스 이후 Google Play 테스트 트랙 → 단계적 출시 → Android vitals(현장 분포)로 이어지는 피드백 루프를 "재현 조건 고정 → 원인 좁히기 → 테스트 전환 → 회귀 판정 → 배포 → 현장 관찰 → 재현" 하나의 순환으로 연결했다. 특정 기기에서만 앱 시작이 느리다는 현장 리포트를 이 순환 전체로 조사하는 worked example과, 디버거 연결이 타이밍을 바꿔 race/ANR을 감추는 실패 사례를 포함했다.
- 저작과 동시에 공식 출처 대조(WebFetch): Android vitals 개요 문서에서 "사용자 동의 시 기기가 안정성·성능·배터리·권한 지표를 추적해 Play Console에서 확인 가능하다"는 서술과 "기기 하드웨어/소프트웨어 문제가 높은 오류율의 원인일 수 있고 RAM·OS 버전·프로세서 종류와의 연관성을 알려준다"는 서술을 원문으로 확인 후 인용했다. 내부 링크 8개, 외부 링크 6개 전수 확인(broken 0건).
- 기존 `06_testing_performance`(debugging-contracts, profiler/Perfetto/dumpsys, measure-before-optimizing, test-layer 선택, unit/integration/UI/E2E, flaky test)와 `03_packaging_deployment/distribution`(Google Play 테스트 트랙, 단계적 출시) 원자 노트를 재사용하고 링크로 연결했다. 개별 도구·정책은 이미 잘 설명돼 있었지만, "지금까지의 장이 각자 언급한 진단 신호가 사실 하나의 방법론이었다"는 회고적 연결과 "테스트 통과 → 배포 → 현장 피드백 → 재현"이라는 릴리스 이후 순환은 이 장에서 새로 만들었다.
- 상태: **11장 본문 작성 완료 / 저작 세션 자체 링크·사실 검증 완료 / 별도 세션의 독립 Reader·Research 검수와 사용자 검수는 아직 미실시**
- **12장(최종 장) `호환성, update와 form factor` 본문을 작성했다(2026-08-04).** [실제 본문](../00_foundations/learning-spine/12-compatibility-update-and-form-factor.md)에서 compileSdk/minSdk/targetSdkVersion(각각 빌드 시 API 표면/설치 하한/compatibility 동작 기준이라는 다른 질문), 기기 실제 SDK_INT, SDK Extension(SDK_INT만으로는 false negative가 생기는 API 존재), Mainline 모듈 버전(같은 API level 안에서도 기기별 차이), 라이브러리 버전(1장의 플랫폼 API-vs-Jetpack 구분과 연결), Play policy(런타임과 별개인 배포 조건), OEM 구현, form factor까지 10개 축을 "언제/누가/무엇을 제한하는가" 통합표로 정리했다. targetSdkVersion을 올렸더니 기존 기능이 깨지는 실패 사례(compatibility 동작이 꺼진 것)와, "같은 API가 특정 기기에서만 다르게 동작한다"를 10개 축 순서로 좁히는 worked example을 포함했다. 마지막으로 "이 Learning Spine을 마치며" 절에서 1~12장 전체가 이룬 순환을 요약하고 Worked Example/Diagnostic Runbook/Atomic Reference로의 다음 단계를 명시했다.
- 저작과 동시에 공식 출처 대조(WebFetch): `<uses-sdk>` 문서에서 targetSdkVersion이 "시스템에 이 버전까지 테스트했음을 알리고, 플랫폼 API level이 target보다 높으면 시스템이 compatibility 동작을 활성화할 수 있다"는 서술을 원문으로 확인 후 인용했다. 내부 링크 7개, 외부 링크 5개 전수 확인(broken 0건).
- 기존 `00_foundations/history`(API level/codename/extension/target 축, history를 contract 변화 지도로 보는 원칙), `01_system_internals/platform-modularity`(SDK Extension, Mainline), `03_packaging_deployment`(defaultConfig의 identity/버전 계약), `07_platforms`(폼 팩터 지도) 원자 노트를 재사용하고 링크로 연결했다. 개별 축은 이미 각자 잘 설명돼 있었지만, 10개 축을 "언제 결정되고 누가 통제하는가"라는 하나의 표로 통합하고 1~11장의 구체적 사례(4장 exported, 9장 permission, 10장 AOSP/Google/OEM, 11장 vitals)와 각 축을 직접 연결하는 것은 이 장에서 새로 만들었다.
- 상태: **12장(최종 장) 본문 작성 완료 / 저작 세션 자체 링크·사실 검증 완료 / 별도 세션의 독립 Reader·Research 검수와 사용자 검수는 아직 미실시**
- **Learning Spine 12개 장 전체(1~12장) 본문 작성이 완료됐다(2026-08-04).** 1~2장은 별도 세션이 작성하고 이 세션이 독립 검수했다(오류 없음, Phase 2 진행 중 로그 참고). 3~12장은 이 세션이 작성하고 저작 세션 자체 링크·사실 검증만 마쳤다.

#### Phase 2. 3~12장 독립 검수(2026-08-04)

Author와 Reviewer 분리 원칙에 따라, 저작 세션과 무관한 독립 검수를 5개 subagent에 2개 장씩 병렬로 위임했다(3~4, 5~6, 7~8, 9~10, 11~12장). 각 subagent는 (1) Reader 검수(확인 질문에 본문만으로 답할 수 있는지), (2) 내부 링크 전수 재확인, (3) 외부 링크 HTTP 상태 재확인, (4) 핵심 인용문 3개 이상을 WebFetch로 원문 재대조, (5) 장 간 bridge 질문이 다음 장에서 실제로 다뤄지는지를 검증하도록 지시했다. 11~12장 담당 agent는 비정상적으로 지연되어(다른 4개는 5~7분, 이 agent는 완료까지 약 8시간) 저작 세션이 직접 동일한 체크리스트로 11~12장을 검수했고, 이후 지연됐던 agent도 뒤늦게 완료되어 결과를 대조했다.

**실제 오류로 확인되어 수정한 항목:**

1. **4장 사실 오류(가장 중요).** "exported=false 컴포넌트를 외부에서 호출하면 남는 신호는 '컴포넌트 없음'이 아니라 '권한 거부'"라고 서술했으나, `<activity>` exported 속성 공식 문서를 재확인한 결과 Activity의 경우 정확히 `ActivityNotFoundException`이 발생한다는 것을 확인했다(원문: "If this element is set to false and an app tries to start the activity, the system throws an ActivityNotFoundException."). 즉 원래 서술이 사실과 정반대였다. 3절, 6절(실패 사례), 8절(조사 방법 6번), 오해 교정표를 모두 "예외 이름만으로는 registry 미등록과 exported 거부를 구분할 수 없다"는 정정된 논지로 재작성했다.
2. **5장 편집 오류.** "이 구분은 3절 '설치된 패키지 identity' 층위와는 다른 층위"라는 자기지시적 오류(해당 개념은 1절에서 도입됨)를 "1절"로 정정했다. 확인 질문 2개(configuration change에서 프로세스가 유지되는 이유, onDestroy 미보장에서 나오는 실무 규칙)의 근거가 본문에 명시적으로 없어 각각 한두 문장을 보강했다.
3. **8장 커버리지 공백.** 7장이 예고한 "로컬과 서버 상태가 다를 때 어떻게 조정하는가"를 8장이 다루지 않고 있어, 공식 문서의 conflict resolution/"last write wins" 정책을 원문 인용으로 6절에 보강했다.
4. **9장 커버리지 공백.** 8장이 예고한 "실패가 앱 코드/framework policy/kernel-platform policy 중 어디에 속하는가"라는 질문에 9장의 gate 비교표가 명시적으로 답하지 않고 있어, 표에 "실패 시 의심할 층위" 열을 추가했다.
5. **12장 요약 명확성.** "이 Learning Spine을 마치며" 절에서 8~10장을 요약하는 문장이 9장을 중복 언급하며 뒤엉켜 있었고, 10장의 "background execution·결과 가시성" 축이 누락돼 있었다. 8/9/10장을 각각 독립된 절로 분리해 재작성했다. 1장 요약도 "계약(contract)" 프레임을 명시하도록 보강했다.

**검증 결과 사실로 확인된(수정 불필요) 항목:** 8장의 WorkManager 인용문("If the synchronization fails, the doWork() method returns with Result.retry()...")은 한 subagent가 원문에서 찾지 못했다고 보고했으나, 저작 세션이 재확인한 결과 offline-first 공식 문서에 정확히 존재하는 문장이었다(subagent의 WebFetch false negative로 판단).

**최종 판정:** 3, 6, 7, 10, 11장은 발견 사항 없음(PASS). 4, 5, 8, 9, 12장은 위 수정을 반영해 PASS로 전환했다. 모든 장의 내부 링크·외부 링크(전수)는 이 검수 라운드에서 재확인해 broken 0건이다. 3~12장 각 장의 "확인 질문"은 모두 본문 텍스트만으로 답변 가능함을 독립 검수로 확인했다.

**남은 것:** 이 라운드는 코드 리뷰 방식의 오류 탐지·수정이며, 사용자가 Reader로서 직접 읽고 확인 질문에 답해보는 최종 사용자 검수는 아직 실시되지 않았다.

다음 단계 후보: (a) 사용자 최종 검수, (b) Worked Example 8개 작성(Phase 3), (c) Diagnostic Runbook 작성(Phase 4), (d) 나머지 Atomic Reference 품질 재검토(Phase 5).
