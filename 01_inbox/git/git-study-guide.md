---
title: git-study-guide
tags: [git, index, pro-git, roadmap]
aliases: [Git 인덱스, Git 학습 가이드, Pro Git 마스터 가이드]
date modified: 2025-12-18 15:37:56 +09:00
date created: 2025-12-18 13:58:00 +09:00
---

## 📚 Git Knowledge Base (The Complete Pro Git)

*Scott Chacon 의 Pro Git(2nd Edition) 전 범위를 아우르는 100% 완전 통합 가이드입니다.*

---

### 🧭 학습 로드맵

#### 🎯 Phase 1: 기초 및 원리 (Fundamentals)

Git 의 내부 구조를 이해하여 모든 명령어의 작동 원리를 파악합니다.

1. [Git 인턴십 (내부 구조)](00_fundamentals/git-internals.md) ⭐
   - Object 모델, Packfiles, Refspec, **Smart/Dumb 프로토콜**, **GC & Prune**.
2. [Git 기본 개념](00_fundamentals/basic-concepts.md)
   - **Three Trees** (HEAD, Index, Working Directory) 프레임워크.
3. [리비전 선택 및 범위](00_fundamentals/revision-selection.md)
   - SHA-1, Reflog, Ancestry(`~`, `^`), Ranges(`..`, `…`).

---

#### 🚀 Phase 2: 실무 전략 및 GitHub (Strategies)

팀 협업과 현대적인 워크플로우를 마스터합니다.

1. [브랜치 관리 전략](01_strategies/branching-strategies.md) ⭐
   - 분산 워크플로우, **프로젝트 유지보수(git am, patches)**.
2. [GitHub 협업 마스터](01_strategies/github-mastery.md) ⭐
   - PR, Code Review, Projects, **Actions Basics**.
3. [커밋 메시지 작성법](01_strategies/commit-messages.md)
   - Semantic Commits 가이드.

---

#### 🔥 Phase 3: 고급 파워 도구 (Advanced Power Tools)

실수를 복구하고 복잡한 상황을 제어하는 전문가 기술입니다.

1. [Reset 완벽 분석](02_advanced/reset-demystified.md) ⭐
   - 핵심 3 단계 원리와 `checkout` 비교.
2. [고급 머지 전략](02_advanced/advanced-merging.md)
   - Recursive/Octopus 전략, **수동 충돌 해결 (Ours/Theirs)**.
3. [Git 트러블슈팅](02_advanced/troubleshooting.md) ⭐
   - `reflog` 와 `fsck` 를 이용한 전문 데이터 복구.
4. [Git 서브모듈](02_advanced/submodules.md)
   - 의존성 관리 및 서브프로젝트 제어.
5. [고급 워크플로우](02_advanced/advanced-workflows.md)
   - `bisect`, `rerere`, **Worktree**, **Blame**, **Replace**, **Bundling**.
6. [주요 명령어 비교](02_advanced/command-comparisons.md)
   - Merge vs. Rebase 등 결정적 차이 요약.

---

#### 🛠️ Phase 4: 보안, 맞춤화 및 관리 (Management)

생산성, 보안, 그리고 시스템 전화를 위한 도구들입니다.

1. [보안 및 상세 스테이징](03_tools/git-security-and-staging.md) ⭐
   - **GPG 서명**, **Interactive Staging(`add -p`)**.
2. [Git 커스텀 및 자동화](03_tools/git-customization.md)
   - Config, Attributes, Hooks, **환경 변수**.
3. [인증 및 보안 가이드](03_tools/credential-storage.md)
   - Credential Helpers, Keychain, PAT(Tokens).
4. [마이그레이션 및 상호운용성](03_tools/git-migration.md)
   - SVN/P4/Mercurial 에서 Git 으로 전환.
5. [GitUI 가이드](03_tools/gitui.md)
   - Rust 기반 고속 TUI 활용.

---

**가이드**: 이 지식 저장소는 단순 요약이 아닌, Git 의 모든 매커니즘을 심층적으로 다룹니다. 궁금한 주제가 있다면 하단의 **연결 문서**를 따라 지식의 그물을 넓혀보세요.
