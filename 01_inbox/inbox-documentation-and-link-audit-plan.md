# 📋 Master Vault Documentation & Link Audit Plan (v2.0)

> **목적**: `01_inbox` 내의 모든 마크다운 파일(총 1,175개)에 대해 단일 책임 원칙(원자성 100%), 상대 경로 마크다운 링킹, Mermaid 시각화, 초보자 친화적 서술 표준을 전면 적용한다.

---

## 🚨 1. Vault 마스터 4대 정비 원칙 (Master Standards)

1. **원자성 및 단일 책임 원칙 (Single Responsibility Principle & Atomicity)**
   - 한 문서에는 오직 그 개념/기술 단 하나의 정체성과 핵심 원리만 원자적으로 포함한다.
   - **원자성 훼손 기준**:
     1. 문서 본문 내에 두 기술의 대규모 비교 파트(`## ... vs ...`)가 직접 포함된 경우 ➔ 독립 비교 노드(`...-vs-....md`)로 분리 전출!
     2. 200줄 이상의 거대 파일(Monolithic file)에 하위 서브 도구, 알고리즘, 파이프라인이 뭉쳐있는 경우 ➔ 독립 레퍼런스 노드로 전면 모듈화 분리!
     3. 서브 도구 및 보조 메커니즘(예: `dex2oat`, `mmap`, `reflection`, `compile-time-code-generation` 등)은 무조건 독립 노드로 분리 후 상대 링크로 연결!

2. **100% 상대 경로 마크다운 링크 필수 (`[Text](../../relative_path.md)`)**
   - ❌ Obsidian 위키링크(`**...**`) 및 `file:///Users/youngmin/...` 절대 경로 절대 금지.
   - ⭕ 작성하는 문서의 위치를 기준으로 **디스크 상에 실존하는 100% 검증된 상대 경로 마크다운 링크**만 사용한다.

3. **시각화 및 다이어그램 규칙 (Mermaid)**
   - ❌ ASCII 아트 박스 그림(`┌──┐`, `+---+`, `[...]` 텍스트 박스) 100% 전면 금지.
   - ⭕ 반드시 Mermaid 다이어그램(` ```mermaid `)을 사용한다.
   - ⭕ 라벨이나 subgraph 이름에 소괄호 `()`나 특수문자가 들어갈 경우 문법 오류 예방을 위해 무조건 큰따옴표 `""`로 감싼다.

4. **초보자 친화적 서술 표준 (Beginner-Friendly Writing)**
   - 개요(Overview) ➔ 직관적 비유(Analogy) ➔ 핵심 원리(Mechanism) ➔ 실전 사용예/안티패턴 ➔ 연관 상대링크 5단계 표준 서술 적용.

---

## 🔍 2. Vault 전수 스캔 적발 결과 (Total 1,175 Files)

- 🔴 **원자성 훼손 (Atomicity Violation) 파일**: **268개 적발** (본문 내 대규모 inline vs 비교 파트 및 200줄 이상 비대 모놀리식 파일)
- 🔴 **Obsidian 위키링크 (`**...**`) 사용 파일**: **204개 적발**
- 🔴 **ASCII 텍스트 박스 아크 사용 파일**: **50개 적발**
- 🔴 **절대 경로 (`file://`) 사용 파일**: **1개 적발**

---

## 🗓️ 3. 단계별 원자성 수술 및 링크 전수 교정 로드맵

### 🚀 Phase A: CS 핵심 및 최근 생성 노드 원자성 전면 수술
- [ ] `compile-time-code-generation.md` ➔ APT vs KSP 비교 파트를 `apt-vs-ksp.md` 로 원자성 분리 전출
- [ ] `reflection.md` ➔ Java vs Kotlin Reflection 비교 파트를 `java-vs-kotlin-reflection.md` 로 원자성 분리 전출
- [ ] `pure-function.md` ➔ Pure vs Impure 비교 파트를 `pure-vs-impure-function.md` 로 원자성 분리 전출
- [ ] `structured-concurrency.md` ➔ Unstructured vs Structured 비교 파트를 `structured-vs-unstructured-concurrency.md` 로 원자성 분리 전출

### 🚀 Phase B: Networking 도메인 원자성 수술 & ASCII ➔ Mermaid 전면 교정 (30개 파일)
- [ ] `tcp-udp-protocols.md` (233줄) ➔ `tcp-vs-udp.md` 분리 및 ASCII 아크 ➔ Mermaid 수술
- [ ] `tcp-ip-model.md` (247줄) ➔ `osi-vs-tcpip.md` 분리
- [ ] `dhcp-nat-protocols.md` (210줄) ➔ `dhcp-vs-static-ip.md` 분리
- [ ] `ip-header-structure.md` (199줄) ➔ `ipv4-vs-ipv6.md` 분리
- [ ] `dns-fundamentals.md` (327줄) ➔ `a-record-vs-cname.md` 분리

### 🚀 Phase C: Security 도메인 원자성 수술 & 모놀리식 노드 분리 (25개 파일)
- [ ] `cryptography-basics.md` (423줄) ➔ 대칭키 vs 비대칭키 `symmetric-vs-asymmetric-crypto.md` 분리
- [ ] `block-cipher-modes.md` (238줄) ➔ 스트림 암호 vs 블록 암호 `stream-vs-block-cipher.md` 분리
- [ ] `access-control-models.md` (189줄) ➔ `blp-vs-biba.md` 분리
- [ ] `digital-content-protection.md` ➔ `watermarking-vs-fingerprinting.md` 분리

### 🚀 Phase D: Mobile & OS 전체 268개 원자성 훼손 노드 전수 분리 수술
- 파이썬 자동 원자성 분리 헬퍼 스크립트를 적용하여 본문 내 내장 비교 파트를 독립 `-vs-` 마크다운 노드로 자동 추출 생성하고, 원본 문서에는 상대 링크로 참조 변경.
