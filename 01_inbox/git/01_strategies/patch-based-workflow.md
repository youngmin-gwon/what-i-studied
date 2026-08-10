---
title: patch-based-workflow
tags: [git, patch, workflow, email, format-patch, am]
aliases: [패치 워크플로우, 이메일 기반 협업, format-patch, Sign-off]
date modified: 2026-08-10
date created: 2025-12-18
---

## 패치 기반 워크플로우: 이메일로 전하는 코드

대규모 프로젝트나 이메일 기반의 협업(예: Linux 커널) 환경에서는 브랜치 직접 병합 외에 패치(Patch)를 주고받는 방식을 사용합니다. 이는 역사가 깊고, 분산 환경에서 매우 효율적인 협업 방식입니다.

---

### 💡 Why it matters (Context)

- **이메일 기반 협업**: GitHub PR이 없는 시대(또는 인프라)에서도 코드 리뷰와 협업이 가능합니다.
- **작성자 정보 보존**: 패치 적용 시 원본 작성자와 작성 시간이 그대로 유지됩니다.
- **Linux 커널 표준**: 오픈소스의 정점인 Linux 커널 개발에서 표준 방식입니다.

---

## 🏗️ 1. 패치 생성 및 적용

### 패치 생성 (`git format-patch`)

특정 커밋들을 이메일에 첨부하기 좋은 형식의 텍스트 파일로 만듭니다.

```bash
# 마지막 3개 커밋을 패치 파일로 생성
git format-patch -3

# 특정 커밋부터 현재까지를 패치로 생성
git format-patch <base-commit>

# 패치를 표준 출력으로 출력 (이메일에 붙여넣기 용)
git format-patch -1 --stdout
```

### 패치 적용 (`git am`)

이메일 등으로 받은 패치 파일을 읽어 작성자 정보와 커밋 메시지를 유지하면서 내 히스토리에 반영합니다.

```bash
# 패치 파일 적용
git am 0001-fix-bug.patch

# 여러 패치 한번에 적용
git am *.patch

# 충돌 발생 시 해결 후 재개
git am --continue

# 적용 취소
git am --abort
```

---

## 🏗️ 2. 프로젝트 관리자의 검토 흐름

### Sign-off

작성자가 코드를 검토하고 승인했음을 기록합니다.

```bash
# 커밋에 Sign-off 추가
git commit -s

# 또는 이미 작성된 커밋에 추가
git commit --amend -s
```

Sign-off는 다음과 같이 커밋 메시지 하단에 기록됩니다:

```
Signed-off-by: Your Name <your.email@example.com>
```

### 선형 히스토리 유지

병합 시 `merge --no-ff` 를 쓸지, `rebase` 후 깔끔하게 합칠지를 프로젝트 성격에 맞춰 결정합니다.

- **Merge**: 전체 브랜치 히스토리를 보존 (복잡하지만 정보 손실 없음)
- **Rebase**: 선형 히스토리 (깔끔하지만 원본 작성 시간 정보 변경)

---

## 🚨 흔한 실수 (Common Mistakes)

1. **패치 파일 직접 편집** ❌
   - 패치 파일의 형식을 무시하고 수정하면 `git am`이 정상 작동하지 않습니다.
2. **Sign-off 없는 리뷰** ⚠️
   - 특히 오픈소스 프로젝트에서는 검토자의 Sign-off가 법적/관습적 책임을 의미합니다.
3. **충돌 해결 후 `add` 빠뜨리기** ❌
   - `git am --continue` 전에 `git add .`로 변경사항을 스테이징해야 합니다.

---

### 📚 연결 문서

- [브랜치 전략](branching-strategies.md) - 분산 워크플로우 모델
- [커밋 메시지](commit-messages.md) - 패치의 메시지 작성법
- [Reset 완벽 분석](../02_advanced/reset-demystified.md) - 패치 적용 중 Rebase 이해
- [GitHub 협업](github-mastery.md) - 현대의 Pull Request 방식
