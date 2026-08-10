---
title: interactive-staging
tags: [git, staging, interactive, add-patch]
aliases: [대화형 스테이징, Interactive Staging, add -p]
date modified: 2026-08-10
date created: 2025-12-18
---

## Interactive Staging: 정교한 커밋 준비

마스터 레벨의 개발자는 단순히 코드를 올리는 것을 넘어, 커밋의 **핵심만** 골라 담는 정교함을 갖추어야 합니다.

---

### 💡 Why it matters (Context)

- **커밋 정제**: 하나의 파일에서 여러 수정을 했더라도, 논리적으로 연관된 부분만 골라 여러 개의 깔끔한 커밋으로 나눕니다.
- **코드 리뷰 효율**: 하나의 커밋이 한 가지 목적을 가질 때, 리뷰어가 변경 사항의 의도를 더 쉽게 파악할 수 있습니다.
- **히스토리 추적**: 나중에 `git blame`이나 `git log`로 변경 내역을 추적할 때 정제된 커밋이 매우 유용합니다.

---

## 🏗️ 1. Interactive Staging (`git add -i`)

작업한 내용을 한꺼번에 `add` 하는 대신, 대화형 인터페이스를 통해 선택적으로 스테이징합니다.

- **Patch Mode (`git add -p` / `-patch`)**: ⭐ 가장 많이 쓰이는 기능입니다. 파일 내의 변경 사항을 덩어리(Hunk)로 나누어 보여주며, 각 덩어리를 스테이징할지(`y`), 건너뛸지(`n`), 아니면 더 작게 쪼갤지(`s`) 결정할 수 있습니다.
- **Untracked 관리**: 새로 생성된 파일들만 골라서 스테이징할 수 있습니다.

---

## 🏗️ 2. Interactive Reset

스테이징된 내용 중 일부만 되돌리고 싶을 때도 대화형 모드를 사용할 수 있습니다.

- `git reset -p`: 스테이징된 변경 사항 중 특정 덩어리만 언스테이징합니다.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **너무 큰 Hunk 무작정 승인** ❌
   - `git add -p` 도중 연관 없는 수정 사항이 섞여 있다면 `s`(split) 명령어로 더 쪼개서 분리해야 합니다.

---

### 📚 연결 문서

- [Git 기본 개념](../00_fundamentals/basic-concepts.md) - 스테이징 영역(Index)의 기본 원리
- [커밋 메시지](../01_strategies/commit-messages.md) - 정제된 커밋을 위한 메시지 작성법
- [Reset 완벽 분석](../02_advanced/reset-demystified.md) - Reset 과 스테이징의 관계
- [GPG 서명](git-gpg-signing.md) - 신뢰의 기술
