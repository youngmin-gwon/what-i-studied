---
title: revision-selection
tags: [fundamentals, git, ranges, revisions, sha]
aliases: [Git 리비전 선택, 커밋 범위 지정, 특정 커밋 지칭하기]
date modified: 2025-12-18 16:08:04 +09:00
date created: 2025-12-18 16:40:00 +09:00
---

## Revision Selection: 특정 커밋을 정확히 지칭하는 법

Git 에서 특정 작업을 수행할 때(show, log, checkout 등), 어떤 커밋을 대상으로 할지 지정하는 방법은 단순히 SHA-1 해시값 이상으로 다양합니다.

---

### 💡 Why it matters (Context)

- **정교한 탐색**: 수만 개의 커밋 히스토리 중 내가 원하는 지점을 빠르고 정확하게 찾아낼 수 있습니다.
- **로그 가독성**: 필요한 범위의 커밋만 필터링하여 복잡한 머지 히스토리를 명확히 분석합니다.
- **자동화**: 스크립트에서 부모 커밋이나 상대적 위치를 사용하여 동적인 작업을 수행합니다.

---

## 🏗️ 1. 단일 리비전 선택 (Single Revisions)

### SHA-1 해시 (전체 & 부분)
- 전체 40 자 해시를 다 쓸 필요는 없습니다. 프로젝트 내에서 고유하기만 하다면 앞의 4~10 자만 사용해도 됩니다. (`git show a1b2c3d`)

### 브랜치 및 태그 참조
- 브랜치 이름(`main`, `dev`)이나 태그 이름(`v1.0.0`)은 결국 특정 커밋 해시를 가리키는 포인터입니다.

### Reflog 참조 (`HEAD@{n}`)
- 최근에 HEAD 가 가리켰던 기록을 사용합니다. (`git show HEAD@{5}`: 5 단계 전의 HEAD 상태) Natural language 로도 가능합니다: `HEAD@{yesterday}`.

### 계보 참조 (Ancestry References)
- **Tilde (`~`)**: 수직적인 부모를 찾아갑니다. `HEAD~2` 는 할아버지 커밋입니다.
- **Caret (`^`)**: 머지 커밋에서 **몇 번째 부모**인지를 지정합니다. `HEAD^2` 는 머지된 두 번째 브랜치의 부모입니다.

---

## 🏗️ 2. 커밋 범위 선택 (Commit Ranges)

### Double Dot (`..`): "A 에는 없지만 B 에는 있는 것"
- 주로 "내가 이 브랜치에서 작업한 내용이 무엇인가?"를 볼 때 사용합니다.
- `git log main..feature`: `main` 브랜치 이후 `feature` 브랜치에만 있는 커밋들.

### Triple Dot (`…`): "A 와 B 양쪽에 공통되지 않은 것"
- 두 브랜치가 서로 다른 길을 간 모든 커밋을 보여줍니다. (Symmetric Difference)
- `--left-right` 옵션과 함께 쓰면 어느 커밋이 어느 쪽에 속하는지도 알 수 있습니다.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **`~` 와 `^` 의 혼동** ❌
   - `~2` 는 증조할아버지가 아니라 할아버지(2 단계 위)입니다.
   - 머지 커밋이 아닌 일반 커밋에서 `^2` 를 사용하면 에러가 발생합니다.
2. **짧은 해시 충돌**
   - 매우 큰 프로젝트에서는 4 자리 해시가 중복될 수 있습니다. 최소 7 자리 이상 사용을 권장합니다.
3. **Double Dot 의 방향**
   - `git log main..feature` 와 `git log feature..main` 은 완전히 반대의 결과를 보여줍니다. "시작점..끝점" 순서를 기억하세요.

---

### 📚 연결 문서
- [Git 인턴십](git-internals.md) - SHA-1 해시가 생성되는 원리
- [트러블슈팅](../02_advanced/troubleshooting.md) - `reflog` 를 이용한 유실 커밋 복구
- [Reset 완벽 분석](../02_advanced/reset-demystified.md) - 대상 커밋을 지정할 때의 리비전 활용
