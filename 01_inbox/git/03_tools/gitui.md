---
title: gitui
tags: [git, rust, tools, tui]
aliases: [Git 터미널 UI, GitUI 가이드, 터미널 Git GUI]
date modified: 2025-12-18 15:22:33 +09:00
date created: 2025-12-18 14:40:00 +09:00
---

## GitUI: 터미널 기반 고성능 Git UI 가이드

**GitUI**는 Rust 로 작성된 매우 빠르고 효율적인 터미널 기반 Git 인터페이스입니다. 키보드 중심의 조작을 통해 Git CLI 의 복잡한 문법을 외우지 않고도 강력한 Git 기능을 활용할 수 있게 해줍니다.

---

### 🏢 실무 사례 (Why use GitUI?)

- **빠른 부분 스테이징 (Hunk Staging)**: 하나의 파일에서 수정된 여러 부분 중 특정 부분(Hunk)만 골라서 스테이징할 때, CLI 보다 시각적으로 훨씬 빠르고 정확하게 작업할 수 있습니다.
- **대규모 레포지토리 탐색**: 수만 개의 커밋이 있는 대규모 프로젝트에서도 Rust 기반의 속도 덕분에 지연(Lag) 없이 히스토리를 훑어볼 수 있습니다.
- **마우스 없는 코딩 환경**: 서버 인스턴스(SSH) 환경이나 터미널 중심의 워크플로우를 가진 개발자에게 마우스 없이도 GUI 급의 편리함을 제공합니다.

---

## 🏗️ 주요 기능 및 조작

### 1. 기본 조작

- **실행**: `gitui`
- **창 이동**: `Tab` (다음), `Shift + Tab` (이전)
- **탭 전환**: 숫자키 `1`~`5` (Status, Logs, Files, Stashing, Stashes)
- **도움말**: `?` (현재 화면의 단축키 목록)

### 2. 핵심 작업 (Status & Logs)

- **스테이징**: 파일 선택 후 `Enter`.
- **Hunk/Line 선택**: `l` (상세 diff 모드) 진입 후 특정 코드 라인만 스테이징 가능.
- **커밋**: `c` 키 입력 후 메시지 작성.
- **커밋 수정 (Amend)**: `A` (Shift + a).
- **Push/Pull**: `p` (Push), `u` (Pull).

---

## 🚨 흔한 실수 (Common Mistakes)

1. **단축키 오동작 (Caps Lock)** ❌
   - GitUI 는 대문자 단축키가 많습니다(예: `A` for Amend). Caps Lock 이 켜져 있으면 의도치 않은 기능이 실행될 수 있으니 주의하세요.
2. **에디터 설정 미흡**
   - 커밋 메시지 작성 시 GitUI 가 갑자기 종료되거나 반응이 없다면, 환경 변수(`$EDITOR`)가 제대로 설정되지 않은 경우가 많습니다. `export EDITOR='vim'` 등으로 설정 확인이 필요합니다.
3. **병합 충돌 시 CLI 병행**
   - GitUI 에서도 충돌 해결을 지원하지만, 복잡한 3-way merge 의 경우 전용 머지 도구(VS Code 등)와 CLI 를 사용하는 것이 더 안전할 때가 있습니다.

---

### 📚 연결 문서

- [[00_fundamentals/basic-concepts|Git 기본 개념]] - 스테이징과 커밋의 원리
- [[02_advanced/troubleshooting|트러블슈팅]] - CLI 를 통한 고급 복구
- [[02_advanced/command-comparisons|명령어 비교]] - GitUI 내부에서 일어나는 명령어 분석
