---
title: advanced-merging
tags: [git, advanced, merge, strategy, conflict]
aliases: [고급 머지 가이드, 머지 전략, 수동 충돌 해결]
date modified: 2025-12-18 17:10:00 +09:00
date created: 2025-12-18 17:10:00 +09:00
---

## Advanced Merging: 복잡한 병합의 과학과 기술

Git의 자동 머지는 훌륭하지만, 거대한 프로젝트나 복잡한 히스토리에서는 자동 해결이 불가능한 상황이 발생합니다. 이 문서에서는 머지 전략의 종류와 수동으로 충돌을 해결하는 고급 기법을 다룹니다.

---

### 💡 Why it matters (Context)

- **결정적 해결**: 자동 머지가 실패했을 때, 데이터 유실 없이 가장 정확한 병합 지점(Merge Base)을 찾아 해결할 수 있습니다.
- **워크플로우 설계**: 프로젝트 성격에 따라 가장 적합한 머지 전략(Recursive, Octopus 등)을 선택하여 히스토리를 관리합니다.
- **도구 활용**: `ours`, `theirs` 같은 전략적 옵션을 사용하여 반복적인 병합 작업을 효율화합니다.

---

## 🏗️ 1. 머지 전략의 종류 (Merge Strategies)

### Recursive Strategy (기본)
두 브랜치를 합칠 때 공통 조상(Common Ancestor)이 여러 개인 경우, 조상들끼리 먼저 머지하여 가상의 조상을 만든 후 최종 머지를 수행합니다. Git의 기본 전략입니다.

### Octopus Strategy
세 개 이상의 브랜치를 한 번에 머지할 때 사용합니다. 히스토리가 매우 깔끔해지지만, 복잡한 충돌이 예상될 때는 사용하지 않는 것이 좋습니다.

### Resolve Strategy
두 개의 브랜치만 머지할 수 있으며, Recursive 전략보다 단순한 알고리즘을 사용합니다. 아주 드문 케이스의 엣지 케이스에서만 사용됩니다.

---

## 🏗️ 2. 수동 충돌 해결 및 도구 (Conflict Resolution)

### Ours vs. Theirs
충돌 발생 시 한쪽의 내용을 통째로 채택하고 싶을 때 사용합니다.
- `git checkout --ours <file>`: 현재 내 브랜치 내용을 유지.
- `git checkout --theirs <file>`: 병합하려는 브랜치 내용을 채택.

### Merge Base 찾기
충돌이 너무 복잡할 때, 두 브랜치가 갈라진 정확한 지점을 확인하여 변경 사항을 추적합니다.
```bash
git merge-base branch-A branch-B
```

### Manual Three-Way Merge
`git show :1:file`, `:2:file`, `:3:file` 명령어를 통해 공통 조상, 내 버전, 상대 버전을 각각 파일로 추출하여 직접 비교하며 수정할 수 있습니다.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **무조건적인 `theirs` 사용** ❌
   - 코드를 제대로 읽지 않고 `theirs`로 덮어쓰면 내 브랜치에서 정성껏 작성한 다른 기능이 사라질 수 있습니다.
2. **충돌 마커 미제거** ❌
   - `<<<<`, `====`, `>>>>` 마커가 남은 채로 커밋하면 컴파일 에러가 발생합니다.
3. **머지 베이스 오판**
   - 리베이스(Rebase)를 자주 한 프로젝트에서는 머지 베이스가 예상과 다를 수 있으므로 `merge-base` 명령어로 확인하는 습관이 필요합니다.

---

### 📚 연결 문서

- [[02_advanced/command-comparisons|명령어 비교]] - Merge vs. Rebase 상세 비교
- [[02_advanced/troubleshooting|트러블슈팅]] - 기본적인 충돌 해결 방법
- [[00_fundamentals/git-internals|Git 인턴십]] - 머지 커밋의 내부 구조 이해
- [[02_advanced/reset-demystified|Reset 완벽 분석]] - 잘못된 머지 후 상태 복구하기