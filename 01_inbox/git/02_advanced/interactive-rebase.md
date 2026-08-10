---
title: interactive-rebase
tags: [advanced, git, rebase, workflow]
aliases: [Git Interactive Rebase, Rebase -i, 히스토리 정리]
date modified: 2026-08-10
date created: 2026-08-10
---

## Interactive Rebase: 커밋 히스토리를 자유자재로 정리하기

`git rebase -i` (Interactive Rebase)는 커밋 히스토리를 다시 쓰는 강력한 도구입니다. 단순히 선형 히스토리를 만드는 것을 넘어, 커밋을 합치고(Squash), 메시지를 수정하고(Reword), 불필요한 커밋을 제거(Drop)할 수 있습니다.

### 💡 Why it matters (Context)

- **깔끔한 커밋 메시지**: 작업 중 남긴 "WIP", "Fix typo" 같은 무의미한 커밋 메시지를 최종본으로 수정합니다.
- **의미 있는 커밋 단위**: 여러 파일의 변경사항을 하나의 로직적 커밋으로 묶습니다.
- **히스토리 가독성**: 나중에 코드 리뷰나 추적(blame)을 할 때 각 커밋이 명확한 의도를 드러냅니다.

---

## 🏗️ Interactive Rebase의 주요 기능

### 기본 사용법

```bash
git rebase -i HEAD~3
# 최근 3개의 커밋을 대화형 모드로 재편성
```

에디터가 열리면 다음과 같은 화면이 보입니다:

```
pick a1b2c3d 첫 번째 커밋
pick e4f5g6h 두 번째 커밋
pick i7j8k9l 세 번째 커밋

# Rebase commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup <commit> = like "squash", but discard this commit's log message
# d, drop <commit> = remove commit
```

### 주요 명령어

| 명령어 | 효과 |
|:---|:---|
| `pick` | 해당 커밋 그대로 사용 |
| `reword` | 커밋은 유지하되 메시지만 수정 |
| `squash` | 이전 커밋과 병합 (메시지 포함) - 여러 커밋을 하나로 합치는 것 |
| `fixup` | 이전 커밋과 병합 (메시지 제외) |
| `drop` | 커밋 완전 제거 |

---

## 🏢 실무 사례 (Expert Techniques)

### 케이스 1: 무의미한 커밋 정리하기

```bash
# 작업 중에 남겨진 커밋들
pick a1b2c3d 새로운 기능 추가
pick e4f5g6h WIP: 테스트 작성
pick i7j8k9l Fix: 버그 수정
pick k1l2m3n Fix typo
```

다음과 같이 수정:

```bash
pick a1b2c3d 새로운 기능 추가
squash e4f5g6h WIP: 테스트 작성
squash i7j8k9l Fix: 버그 수정
squash k1l2m3n Fix typo
```

결과: 4개의 산발적 커밋이 1개의 명확한 커밋으로 통합됨.

### 케이스 2: 커밋 순서 변경하기

```bash
pick a1b2c3d 기능 A 추가
pick e4f5g6h 기능 B 추가
pick i7j8k9l 기능 A 수정
```

다음과 같이 수정 (같은 기능의 커밋들을 연속으로 배열):

```bash
pick a1b2c3d 기능 A 추가
pick i7j8k9l 기능 A 수정
pick e4f5g6h 기능 B 추가
```

### 케이스 3: 특정 커밋 선택적 편집 (`edit`)

```bash
reword a1b2c3d 새로운 기능 추가
edit e4f5g6h 테스트 작성
pick i7j8k9l Fix: 버그 수정
```

`edit` 지점에서 Rebase가 중단되며, 그 시점의 코드를 수정할 수 있습니다:

```bash
# 파일 수정 후
git add .
git rebase --continue
```

---

## 🚨 흔한 실수 (Common Mistakes)

1. **이미 Push 한 커밋을 Rebase 하기** ❌
   - 공용 브랜치(main, develop)의 히스토리를 재구성하면 팀원들의 작업이 꼬입니다. 로컬 브랜치에서만 사용하세요.

2. **Rebase 중 충돌 방치** ❌
   - 충돌이 발생하면 반드시 해결한 후 `git rebase --continue` 를 실행하세요. 실수로 `--abort` 하면 처음부터 다시 시작해야 합니다.

3. **Squash 후 메시지 누락** ❌
   - 여러 커밋을 Squash 할 때 최종 메시지를 작성하는 창이 나옵니다. 이 메시지를 정성스럽게 작성하지 않으면 나중에 히스토리 추적이 어렵습니다.

---

### 📚 연결 문서

- [명령어 비교](command-comparisons.md) - Merge vs Rebase 선택 기준
- [Git 인턴십](../00_fundamentals/git-internals.md) - Rebase가 커밋 해시를 왜 변경하는지
- [트러블슈팅](troubleshooting.md) - Rebase 중 발생하는 충돌 해결
