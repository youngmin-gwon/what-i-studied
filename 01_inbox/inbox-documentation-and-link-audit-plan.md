---
title: inbox-documentation-and-link-audit-plan
tags: ["vault", "documentation", "quality-plan", "meta"]
aliases: ["Vault 문서 품질 통합 계획", "Master Vault Documentation Plan v3"]
date modified: 2026-08-10 00:00:00 +09:00
date created: 2026-08-06 16:45:53 +09:00
---

## Vault 문서 품질 통합 계획 (v3.0 — 검증 기반 재작성)

### 이 문서의 위치

이 문서는 v2.0(2026-08-06 작성, 4대 원칙과 "268/204/50/1건 적발"이라는 미검증 수치만 있고 실행은 전혀 없던 버전)을 대체한다. 또한 `01_inbox/mobile/android/_meta/android-knowledge-base-quality-plan.md`(장기간 여러 세션이 작업, 1484줄)와 `android-knowledge-base-phase12-audit-report.md`도 이 문서로 흡수되어 **폐기 대상**이다(android 전용 plan은 삭제 예정 — 아래 "폐기 결정" 참고).

**왜 다시 썼는가.** v2.0은 자동 스캔으로 위반 건수만 세고 단 하나도 고치지 않은 채 방치됐다. 그동안 `01_inbox/mobile/android/`는 별도로 12번의 Phase를 거치며 "완료"를 여러 번 선언했지만, 사용자가 직접 읽을 때마다 실제 결함이 발견되는 패턴이 반복됐다(문체 불친절, 원자 노트 미완결, 코드/frontmatter 오염 등). 2026-08-07~08 사용자 요청으로 vault 전체(1,097개 기술 문서 대상)를 8개 도메인으로 나눠 독립 subagent가 **실제로 파일을 열어** 재검증했고, 그 결과를 이 문서에 반영한다.

### 핵심 교훈 (다음 세션이 반드시 먼저 읽을 것)

1. **자동 스캔 수치는 그 자체로 신뢰하면 안 된다.** v2.0의 "위키링크 204건, ASCII 50건" 같은 수치는 코드 안의 `[[0]*(n+1)...]`(2차원 리스트), Objective-C 메시지 문법 `[[Obj method]]`, HTML `<code>file:///etc/passwd</code>` 예시 문자열 같은 **오탐**을 걸러내지 않은 결과였다. 이번 재검증(1,097개 파일 기준)에서 실제 위키링크는 사실상 0건(시험자료 내부 TOC 목적 1개 파일 제외), 절대경로/`file://`도 0건이었다. **반대로** "완료"라고 기록된 항목(예: android Phase 11의 인라인 gloss 작업) 안에 새로운 결함(frontmatter/Mermaid/코드블록에 링크가 잘못 삽입됨)이 숨어 있었다. 즉 **자동화는 과대 적발도 하고 과소 적발도 한다** — 반드시 표본을 직접 열어 대조해야 한다.
2. **진행 기록 문서(plan/report)는 실제 편집보다 항상 뒤처진다.** android 검증 subagent가 확인한 바로는, `phase12-audit-report.md`(2026-08-06 14:45 작성)가 지적한 P0 오류 30건 중 26건이 보고서 작성 **이후** 이미 수정돼 있었다 — 그러나 어느 진행 기록에도 이 수정이 반영되지 않았다. 반대로 v2.0(계획서)은 Phase A의 4개 항목이 이미 완료됐는데도 체크박스가 안 채워져 "0% 진행"으로 보였다. **결론: 문서 상태를 판단할 때 plan의 체크박스나 로그를 믿지 말고, 항상 대상 파일의 `date modified`/실제 내용을 직접 대조한다.**
3. **자동 "키워드 → 링크" 치환 스크립트는 문맥을 가리지 않고 실행되면 위험하다.** 이번 재검증에서 최소 4개 도메인(android, apple, operating-systems, algorithm)에서 다음 패턴이 발견되고 수정됐다:
   - YAML frontmatter `title:` 필드 안에 마크다운 링크 삽입(파일 slug 자체가 깨짐)
   - Mermaid 다이어그램 라벨 안에 링크 삽입(Mermaid는 마크다운 링크 문법을 해석하지 않으므로 깨진 텍스트만 노출됨)
   - 코드 펜스(Kotlin/Swift/Python 등) 안에 링크 삽입 — **여러 건이 실제로 컴파일/실행 불가능한 코드**를 만들었다(예: `val userId: [stateflow](경로)<String?>`, `heap = **weight, [char, ""**...]`처럼 마크다운 볼드가 Python 리스트 리터럴을 깨뜨린 사례도 있었다)
   - 인라인 코드 스팬(백틱) 안에 링크 삽입
   - 존재하지 않는 문서를 굵은 텍스트(`**android-xxx-yyy**`)로 참조(링크는 아니라 안 깨지지만 막다른 참조) — apple 폴더에서 13건, android `00_foundations/topics/`에서도 과거에 동일 패턴(지어낸 Learning Spine 장 인용) 발견 이력 있음
   **앞으로 vault 전체에 적용하는 어떤 자동 치환 스크립트도 frontmatter/코드펜스/Mermaid 블록/인라인 코드 스팬을 제외하고 실행하거나, 최소한 이 4개 영역만 별도로 dry-run 검토해야 한다.**
4. **"완료" 표시가 있다고 실제로 그런 것은 아니다 — 그러나 정반대로 과도하게 의심할 필요도 없다.** 이번 재검증에서 android는 실제로 상당수(사실 오류 30건 중 26건, 원자 노트 4대 요소 등)가 진짜로 좋아져 있었다. computer-science도 v2.0이 "손도 안 댔다"고 적은 4개 파일 중 3개는 실제로 이미 올바르게 분리돼 있었다(단, 나머지 1개 `structured-concurrency.md`는 검증 subagent도 "이미 됐다"고 잘못 보고했다가 2026-08-10 재검증에서 실제로는 안 돼 있었음이 드러나 그때 가서야 분리했다 — 아래 computer-science 절 참고). **과거 세션도, subagent의 검증 보고도 무조건 믿지 말고, 표본을 직접 열어 확인한 뒤 판단한다.**

### 적용 범위

`01_inbox/` 중 아래 9개 "기술 지식베이스" 폴더에 적용한다(총 1,097개 파일, 2026-08-07 기준):

| 폴더 | 파일 수 |
|---|---:|
| `mobile/android` | 772 |
| `mobile/apple` | 81 |
| `mobile/cross-platform` + `mobile/*.md` | 7 |
| `linux` | 70 |
| `security` | 50 |
| `algorithm` | 41 |
| `computer-science` | 38 |
| `operating-systems` | 19 |
| `git` | 19 |

**제외 폴더(다른 장르, 이 계획의 원자성/문체 규칙을 강제하지 않음):** `books/`(35, 독서 요약), `highlighted/`(15, 책 하이라이트), `writings/`(2, 개인 에세이), `visual-design/`(20, 디자인 시스템 레퍼런스 — 필요 시 별도 검토), `monorepo/`(1), `linux-master-1/`(15, 번호가 매겨진 커리큘럼 구조라 원자 노트가 아닌 챕터 형식). `security/certification/`의 시험 대비 챕터·퀴즈 파일(12개)도 "빠른 암기용 요약/Q&A" 장르라 원자성 규칙 대상에서 제외한다(위키링크 기반 문서 내 TOC는 정상 기능으로 인정).

### 4대 표준 (v2.0 계승 + 실제 검증으로 다듬음)

#### 1. 원자성 (Atomicity)

기준 사례: `01_inbox/computer-science/jit-compilation.md`(개념 단독 설명) + `01_inbox/computer-science/jit-vs-aot-compilation.md`(비교만 별도 문서, 상호 링크). **위반 판정 기준을 v2.0보다 정교화한다**:

- **진짜 위반**: 본문 절반 가까이를 차지하는 "X vs Y" 비교, 또는 서로 독립적인 여러 도구/개념을 한 파일에 묶은 경우(예: `git/02_advanced/advanced-workflows.md`가 rebase/stash/bisect/blame/rerere/bundle 7개를 한 파일에 묶음). → 독립 파일로 분리하고 상호 링크.
- **위반 아님(허용)**: (a) 하나의 명제를 설명하며 이웃 개념과의 경계만 짧게(전체 분량의 1/4 미만) 비교하는 경우 — android의 "관련 문서" 패턴, HIDL 노트가 AIDL을 한 단락만 비교하고 별도 파일로 링크하는 식. (b) android처럼 명사형 "개념 허브" 파일(`viewmodel.md`, `stateflow-and-sharedflow.md`)이 이미 있고 문장형 명제 파일들이 거기로 역링크하는 구조 — 이것도 jit 패턴의 변형으로 인정한다. (c) 시험 자료, 커리큘럼 챕터처럼 장르 자체가 다른 문서.
- **새 하위 기준(이번 감사로 추가)**: 여러 파일에 **같은 비교표가 내용까지 다르게 중복**된 경우(예: algorithm 폴더의 "N 크기별 허용 복잡도" 표가 3개 파일에서 서로 다른 경계값으로 존재)는 원자성 위반이자 사실 불일치이므로 최우선 처리 대상이다.
- **비교 대상 자체가 없는 경우**: 한 파일이 "X vs Y"를 다루는데 Y가 vault에 독립 문서로 존재하지 않으면(예: android의 `stateflow-is-for-current-screen-state-flow-is-for-source-stream.md`가 LiveData 비교표를 안에 품고 있는데 `livedata.md`가 vault에 없음), Y 문서를 새로 만들지 비교를 삭제할지 결정한 뒤에만 분리한다.

#### 2. 상대 마크다운 링크만 사용

위키링크(`[[...]]`), 절대경로(`/`로 시작), `file:///` 전부 금지. **1,097개 파일 재검증 결과 이 축은 이미 거의 충족 상태**(진짜 위반 0건, 시험자료 TOC 목적 위키링크 1개 파일만 예외 인정). 앞으로는 새 파일 작성 시 관례만 지키면 된다 — 별도 대규모 작업 불필요.

#### 3. Mermaid 우선, ASCII는 예외적으로만

상태 전이, 시퀀스, 여러 컴포넌트 관계, 트리/그래프 구조는 Mermaid로. 디렉터리 트리, 터미널 출력 예시, 단순 2~3개 정적 나열은 ASCII/plaintext 유지 가능. **주의**: 코드 펜스(` ```bash ` 등)로 잘못 감싼 일반 산문(체크리스트, 콜아웃)은 "ASCII 다이어그램"이 아니라 별개의 결함이다(아래 6번).

#### 4. 초심자 친화적 서술 + 모호한 용어의 정의 연결

전문용어가 처음 등장하는 문장에서 인라인 정의(괄호/동격구)를 갖추고, 일반 CS/보안/네트워킹 개념은 가능하면 그 개념의 정본 문서로 링크한다(`배경 지식:` 관례). **개념 허브 링크**: 문장형 원자 노트는 해당 개념의 명사형 허브 파일(있다면)이나 상위 학습 문서(Learning Spine 등)로 역링크해야 한다 — 없다면 신설을 백로그에 올린다.

#### 5. (신규) 기계적 무결성 — frontmatter/코드/다이어그램 오염 금지

위 "핵심 교훈 3"에서 설명한 오염 패턴이 없어야 한다. `title:` frontmatter, 코드 펜스, Mermaid 라벨, 인라인 코드 스팬 안에는 마크다운 링크 문법이 있으면 안 된다(전부 plain text). 코드 펜스는 실제 실행 가능한 코드/명령만 담고, 산문·콜아웃은 펜스 밖에 둔다.

### 도메인별 현재 상태와 백로그 (2026-08-07 검증 기준)

#### `mobile/android` (772개) — 상태: 양호, 추적 문서만 신뢰 불가였음

- 사실/코드 오류 P0 30건 중 26건 기수정 확인. 자동 링크화 오염 68건(1차) + 4건(2차, frontmatter/Mermaid/코드펜스) 수정 완료.
- **남은 백로그**: (1) `stateflow-is-...-source-stream.md`의 LiveData 비교표 — `livedata.md` 신설 또는 비교 축소 결정 필요. (2) `dependency-injection/di-contracts/di-tool-comparison.md` thin 문서(mechanism/code/evidence 없음) 보강. (3) `00_foundations/topics/`의 27개 파일이 `합니다/됩니다`체 + 영어 섹션 제목, 나머지(A1/A2/B1-B4)는 `-다`체 — 문체 통일 필요. (4) Learning Spine 11·12장의 `feedback`/`trace`/`flaky`/`surface`/`lifecycle` 인라인 풀이 누락. (5) System Internals(155)/Security(28)/Platforms(43) 전체에 Learning Spine 직접 링크 없음 — top-level map에 추가 필요. (6) DI 19개, Compose design-system/accessibility 14개 등 thin 원자 노트 병합·보강.

#### `mobile/apple` + `cross-platform` (87개) — 상태: 핵심 문서는 android와 대등, 주변부 약함

- 자동 링크화 오염(viewmodel) 4건, 깨진 코드펜스 1건, 중복 frontmatter 1건, 깨진 링크 1건 수정 완료.
- **백로그**: (1) 존재하지 않는 android 파일을 가리키는 가짜 참조 13건(파일별 목록은 위 subagent 보고 참고) — 실제 android 경로로 재연결하거나 문장 삭제. (2) `07_platforms/` 하위 11개 파일(ios/ipados/macos/tvos/visionos/watchos 체크리스트)이 코드·다이어그램·서사 없이 약어 나열만 함 — 다른 apple 문서 수준으로 재작성 필요. (3) visionOS 관련 5개 문서, 보안 샌드박스 관련 2개 문서 간 중복 — 역할 재분담. (4) 앱 생명주기/렌더 루프/터치 이벤트 흐름 등 여러 곳에 다이어그램이 아예 없음 — Mermaid 신설.

#### `computer-science` (38개) — 상태: 핵심부 우수, 구형 networking 잔재만 남음

- 오염 0건. jit-compilation 패턴이 핵심 CS 개념 3종(`compile-time-code-generation`/`apt-vs-ksp`, `reflection`/`java-vs-kotlin-reflection`, `pure-function`/`pure-vs-impure-function`) + 네트워킹 5쌍(TCP/UDP, OSI/TCPIP, A/CNAME, IPv4/IPv6, DHCP/StaticIP)에 이미 정확히 적용돼 있었음(v2.0의 "미완료" 기록은 틀림, 체크박스만 안 갱신됨).
- **2026-08-10 재검증에서 발견·수정**: `structured-concurrency.md`는 사실 분리가 **안 돼 있었다** — 이전 라운드의 subagent 보고가 이 파일도 이미 분리됐다고 잘못 판단했다(4종이 아니라 3종만 진짜였음). 제목 자체가 "구조화된 동시성 & 비구조화 동시성 비교"였고 본문에 전체 비교 섹션(비유/표/코드)이 그대로 있었다. `structured-vs-unstructured-concurrency.md`를 신설해 비교 섹션을 옮기고 원본은 개념 설명만 남기도록 이번에 실제로 분리했다. **교훈: subagent의 "이미 완료됨" 판단도 파일을 직접 열어 재확인해야 한다 — 이 문서 자체가 그 교훈을 스스로 증명한 사례다.**
- 재검증 중 별도로 `mobile/android/.../compose-state-and-effect-contracts.md`의 Mermaid 다이어그램 라벨 5곳에 남아있던 자동 링크화 오염(존재하는 파일을 가리키는 링크였지만 Mermaid 노드 라벨 안이라 깨짐)도 추가로 발견해 수정했다. 1,119개 파일 전체 재스캔 결과 frontmatter/Mermaid/코드펜스/인라인 코드 오염과 broken link는 모두 0건으로 재확인됨(2026-08-10).
- **백로그(진짜 남은 것)**: `networking/dhcp-nat-protocols.md`(NAT 미분리), `ip-addressing.md`(IPv4/IPv6 표가 `ipv4-vs-ipv6.md`와 완전 중복 — 링크로 대체, 완료), `http-protocol.md`(GET/POST, HTTP버전 비교 내장 → 분리), `ftp-protocol.md`(TFTP 결합 → 분리), `race-condition-and-deadlock.md`(3개 개념 결합 → 분리). 구형 networking 5개 파일(`arp`, `icmp`, `snmp`, `network-devices`, `routing-basics/protocols`)은 비유/친절 서술 표준이 적용 안 됨 + ASCII 박스 5곳을 Mermaid로.

#### `operating-systems` (19개) — 상태: 좋은 예(IPC)와 나쁜 예(보안/커널)가 공존

- 코드펜스 안 링크 오염 1건 수정.
- **백로그**: `secure-operating-systems.md`(6개 개념 결합), `linux-kernel.md`(범용 커널 문서에 Android 특화 내용 과반 — android 폴더와 중복 정리), `kernel-structure.md`(OS 개론 수준으로 범위 초과) 분리 검토. `ipc-contracts/` 4개 파일이 폴더 내 다른 문서보다 훨씬 학술적/불친절 — 톤 통일. `**kernel**`처럼 볼드만 있고 링크 없는 forward-reference 다수(실제 파일은 `kernel-structure.md`) — 링크로 전환.

#### `linux` (70개) — 상태: 렌더링 결함이 예상보다 광범위했음, 이미 수정 완료

- **가장 큰 수확**: 코드펜스에 갇힌 콜아웃/불릿(6개 파일), "연결 문서" 섹션의 가짜 볼드 참조 11개 파일 13건, Bash `[[ ]]` 문법이 `**...**`로 깨진 렌더링 오염 7개 파일 — 총 20여 건을 이번에 전부 발견해 수정 완료. 오타 4건도 수정.
- **남은 백로그**: `commands/log-analysis-commands.md` ↔ `security/linux-log-management.md`, `network-standards.md` ↔ `network-fundamentals.md`, `run-levels.md` ↔ `commands/service-management-commands.md` 사이 중복 콘텐츠 정리(단일 정본 + 상호링크). `container-basics.md`의 비교 서술이 코드 아닌데 ```bash``` 펜스로 감싸인 것 정리.

#### `security` (50개) — 상태: 최상위권, 결함 거의 없음

- 링크 누락 2건만 수정. `fundamentals/`는 원자 노트 모범 사례. android → security/fundamentals 역링크(Certificate Pinning, Root of Trust) 유효성 재확인 완료.
- **백로그**: `attacks/`, `protocols/`, `management/`, `incident-response/`가 더 오래된 "토픽 묶음" 컨벤션(내용은 정확하나 원자성 규칙 이전 스타일) — 우선순위 낮음, 필요시 후속 리팩터링. `certification/README.md`의 실기 문제 색인 3건 누락, 관련 없는 `docker run` 코드블록 잔재는 사용자 확인 후 정리.

#### `git` (19개) — 상태: 기계적으로 완벽, 원자성만 개선 여지

- 오염 0건, 링크 0건 결함.
- **백로그**: `advanced-workflows.md`(7개 도구 통합 → 개별 분리), `git-security-and-staging.md`(GPG+Staging 결합 → 분리), `branching-strategies.md`의 이메일 패치 워크플로우 섹션(범위 이탈 → 분리). rebase/squash 최초 등장 시 정의 누락, `cherry-pick`이 "100% 완전 가이드"를 표방하는 `git-study-guide.md`에 아예 없음.

#### `algorithm` (41개) — 상태: 코드 정확성 결함 발견, 원자성/중복 이슈 다수

- **가장 심각한 발견**: `greedy.md`의 Huffman coding 코드가 마크다운 볼드 문법 침투로 `SyntaxError` 상태였음 — `ast.parse`로 검증하며 복구 완료.
- **백로그**: DP/Greedy/분할정복 3자 비교가 3개 파일에 중복 산재, 메모이제이션/타뷸레이션 비교가 3개 파일에 중복, "N 크기별 허용 복잡도" 표가 3개 파일에서 서로 다른 숫자로 존재(사실 불일치, 최우선). Union-Find/Heap/Trie의 ASCII 트리 3곳을 Mermaid로.
  - ✅ **완료 (2026-08-10)**: `segment-tree.md`(Fenwick Tree → `fenwick-tree.md` 분리), `two-pointers.md`(Sliding Window → `sliding-window.md` 분리), `specialized-queues.md`(Deque → `deque.md`, Monotonic Stack → `monotonic-stack.md`, Monotonic Queue → `monotonic-queue.md` 각각 분리). 관련 링크 11개 파일에서 업데이트(`algorithm-study-guide.md`, `stack-and-queue.md`, `linear.md`, `prefix-sum.md` 등).

### 처리 원칙 (다음 실행 단계에서 지킬 것)

1. **기계적 결함(broken link, frontmatter/코드/Mermaid 오염, 코드펜스 오용)은 발견 즉시 고친다** — 이미 이번 라운드에서 대부분 처리했다.
2. **원자성 분리, 문체 통일, 중복 병합은 사용자 승인 후 진행한다.** 위 백로그는 "무엇을 어떻게 나눌지" 제안까지만 담았고 실행하지 않았다 — 판단이 갈릴 수 있는 편집(예: 파일 분리는 링크 재배선 비용이 크다)이기 때문이다.
3. **새로 대량 자동 스크립트(예: 키워드 자동 링크화)를 돌릴 때는 frontmatter/코드펜스/Mermaid 블록을 제외하거나 별도 dry-run으로 사람이 diff를 검토한 뒤 적용한다.**
4. **"완료" 선언 전에 표본을 직접 열어 대조한다.** 로그나 체크박스만으로 상태를 판단하지 않는다.
5. 이 문서 자체도 시간이 지나면 stale해진다 — 다음 세션은 이 문서의 "도메인별 현재 상태"를 무조건 믿지 말고, 특히 오래된 항목(작성일 기준 한 달 이상)은 재확인 후 갱신한다.

### 폐기 결정

- `01_inbox/mobile/android/_meta/android-knowledge-base-quality-plan.md` — **삭제**(이 문서로 대체됨, 필요 시 git 이력에서 복구 가능: 삭제 직전 커밋 참고).
- `01_inbox/mobile/android/_meta/android-knowledge-base-phase12-audit-report.md`, `android-atomic-rewrite-plan.md`, `android-kb-batch-d-foundations-platforms-report.md`, `android-ecosystem-conceptual-spine-preparation.md` — 내용은 이 문서의 "android" 절에 요약 흡수됨. 원문이 필요하면 git 이력에 남아있다.
