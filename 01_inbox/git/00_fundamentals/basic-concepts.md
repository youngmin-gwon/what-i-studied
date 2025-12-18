---
title: git-basic-concepts
tags: [git, fundamentals, workflow, state]
aliases: [Git 기본 개념, Git 기초, Git 시작하기]
date modified: 2025-12-18 14:05:00 +09:00
date created: 2025-12-18 14:05:00 +09:00
---

## Git 기본 개념: 협업을 위한 데이터 파이프라인

Git을 단순히 "파일을 저장하는 도구"로 보는 것과 "데이터가 흐르는 세 개의 영역"으로 보는 것은 큰 차이가 있습니다. 기초를 단단히 하면 복잡한 충돌 상황에서도 당황하지 않을 수 있습니다.

---

### 🏢 실무 사례

- **Selective Staging (부분 커밋)**: 하나의 파일에서 여러 기능을 수정했을 때, `git add -p`를 통해 논리적으로 관련된 변경사항만 나누어 커밋함으로써 히스토리를 깔끔하게 관리합니다.
- **Hotfix 대응**: 작업 중이던 내용을 스테이징 영역에 두고, 긴급 버그 수정을 위해 브랜치를 전환하는 등 멀티태스킹의 핵심 구조가 됩니다.
- **품질 관리**: 커밋 전 스테이징 영역에서 `git diff --cached`를 통해 최종적으로 코드를 검토하는 프로세스를 구축합니다.

---

## 🏗️ Git의 핵심 작동 원리

### 1. 세 가지 영역 (The Three Sections)

Git 프로젝트는 크게 세 가지 영역으로 관리됩니다. 이 흐름을 이해하는 것이 Git 마스터의 첫걸음입니다.

```mermaid
graph LR
    subgraph "Local Environment"
        A[Working Directory<br/>(작업 폴더)]
        B[Staging Area<br/>(대기실)]
        C[Local Repository<br/>(저장소)]
    end

    A -->|git add| B
    B -->|git commit| C
    C -->|git checkout/switch| A
```

- **Working Directory**: 실제로 코드를 타이핑하고 파일을 생성하는 물리적 폴더입니다.
- **Staging Area (Index)**: 다음 커밋에 포함될 변경사항을 임시로 모아두는 곳입니다. "장바구니"와 같은 역할을 합니다.
- **Local Repository**: `.git` 폴더 내에 데이터가 영구히 저장된 곳입니다.

#### 🛒 온라인 쇼핑 비유
- **상품 고르기**: Working Directory에서 코드 수정.
- **장바구니 담기**: `git add` 명령으로 스테이징. (여러 개를 담을 수 있음)
- **결제하기**: `git commit` 명령으로 최종 구매 확정(저장).

---

### 2. 파일의 상태 변화 (File Lifecycle)

파일은 네 가지 상태 중 하나에 머무르게 됩니다.

| 상태 | 설명 |
|:---|:---|
| **Untracked** | Git이 관리하지 않는 새 파일. |
| **Unmodified** | 커밋 이후 수정되지 않은 깨끗한 상태. |
| **Modified** | 파일이 수정되었으나 아직 스테이징되지 않음. |
| **Staged** | 수정된 파일이 커밋 대기 상태로 등록됨. |

---

### 3. HEAD 포인터

**HEAD**는 "현재 내가 어디에 서 있는가"를 나타내는 책갈피입니다.
- 보통은 현재 작업 중인 브랜치의 마지막 커밋을 가리킵니다.
- `git checkout <commit_hash>`를 통해 과거로 돌아가면 HEAD가 특정 커밋을 직접 가리키게 되며, 이를 **Detached HEAD** 상태라고 합니다.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **`git add .` 남발** ❌
   - 의도치 않은 임시 파일, 설정 파일, 민감 정보가 스테이징 영역에 포함될 수 있습니다. `.gitignore`를 철저히 관리하거나, 파일을 탐색하며 신중히 추가하세요.
2. **커밋 메시지 없이 커밋** ❌
   - 나중에 "이걸 왜 수정했지?"라는 질문에 답할 수 없게 됩니다. [[01_strategies/commit-messages|좋은 커밋 메시지 작성법]]을 참고하세요.
3. **Staging Area를 거치지 않고 바로 커밋하려 함**
   - `git commit -a`는 편리하지만, 스테이징 영역의 "검토 기능"을 포기하는 것입니다. 의미 있는 단위로 나누어 커밋하는 습관을 들이세요.
4. **추적 중인 파일의 이름 변경/이동**
   - 일반 `mv` 명령어로 파일을 옮기면 Git은 기존 파일 삭제 + 새 파일 생성으로 인식합니다. `git mv`를 쓰면 히스토리를 더 깔끔하게 보존할 수 있습니다.

---

### 📚 연결 문서
- [[00_fundamentals/git-internals|Git 인턴십]] - 객체 모델로 이해하는 데이터 저장 방식
- [[02_advanced/troubleshooting|트러블슈팅]] - 상태를 되돌리는 구체적인 방법들
- [[02_advanced/command-comparisons|명령어 비교]] - `add`, `commit`, `checkout`의 상세 옵션 비교
- [[01_strategies/branching-strategies|브랜치 전략]] - 협업 시의 브랜치 활용