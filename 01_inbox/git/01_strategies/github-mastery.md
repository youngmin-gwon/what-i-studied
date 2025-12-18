---
title: github-mastery
tags: [actions, collaboration, git, github, pr]
aliases: [GitHub 마스터 가이드, GitHub 활용법, 협업 워크플로우]
date modified: 2025-12-18 15:22:00 +09:00
date created: 2025-12-18 17:00:00 +09:00
---

## GitHub Mastery: 세계 최대의 오픈소스 협업 플랫폼 정복하기

GitHub 는 단순한 Git 호스팅 서비스를 넘어, 기업과 오픈소스 생태계의 표준 협업 툴입니다. 복잡한 Pull Request 과정부터 프로젝트 관리, 자동화까지 GitHub 의 정수를 다룹니다.

---

### 💡 Why it matters (Context)

- **협업 프로토콜**: Pull Request 와 Code Review 를 통해 코드 품질을 높이고 지식을 공유합니다.
- **워크플로우 가시성**: Issue 관리와 Projects 보드를 통해 프로젝트의 진행 상황을 한눈에 파악합니다.
- **현대적 개발 문화**: 전 세계 개발자들과 소통하며 오픈소스 기여(Contribution) 습관을 기릅니다.

---

## 🏗️ 1. Professional Collaboration (Pull Requests)

GitHub 협업의 핵심은 **PR(Pull Request)**입니다.

- **Fork & Pull**: 원본 저장소 권한이 없을 때, 자신의 계정으로 복사(Fork)하여 작업 후 원본에 반영을 요청합니다.
- **Code Review**: 줄 단위 댓글, 제안(Suggestions), 승인(Approve) 프로세스를 통해 팀의 코드 품질을 상향 평준화합니다.
- **Draft PR**: 작업이 진행 중이지만 미리 공유하여 피드백을 받고 싶을 때 사용합니다.

---

## 🏗️ 2. Project Management (Beyond Code)

- **Issues**: 버그 추적, 기능 제안, 질문 등을 관리합니다. Labels 와 Milestones 를 통해 우선순위를 정합니다.
- **GitHub Projects**: 칸반 보드 스타일로 작업 카드를 관리하며 연관된 Issue/PR 과 실시간으로 연동됩니다.
- **Wiki & Pages**: 프로젝트 문서화와 간단한 정적 웹사이트 호스팅을 지원합니다.

---

## 🏗️ 3. Automation (GitHub Actions Basics)

GitHub 내장 CI/CD 도구로, 특정 이벤트 발생 시 자동으로 스크립트를 실행합니다.

- **Trigger**: `push`, `pull_request`, `schedule` 등.
- **Workflow**: `.github/workflows/*.yml` 파일로 정의합니다.
- **예시**: 테스트 실행, 린트(Lint) 체크, 서버 자동 배포.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **대형 PR (Mammoth PRs)** ❌
   - 수천 줄의 코드를 한 번에 PR 보내면 리뷰어가 내용을 파악하기 어렵고 리뷰 품질이 떨어집니다. 작은 단위로 쪼개서 자주 보내세요.
2. **충돌(Conflict) 방치**
   - PR 을 보낸 후 원본 브랜치가 업데이트되어 충돌이 발생하면, 반드시 본인이 로컬에서 해결 후 다시 푸시해야 관리자가 머지할 수 있습니다.
3. **무의미한 커밋 히스토리**
   - 작업 중 발생한 수많은 "fix typo", "test" 커밋들을 합치지 않고 PR 을 보내면 히스토리가 지저분해집니다. `git rebase -i` 로 정리 후 푸시하세요.

---

### 📚 연결 문서

- [브랜치 전략](branching-strategies.md) - GitHub Flow 와 Git Flow 의 실무 적용
- [Git 커스텀](../03_tools/git-customization.md) - GitHub Actions 의 기반이 되는 Git Hooks 이해
- [Git 서버](../02_advanced/git-server.md) - GitHub 가 내부적으로 사용하는 전송 프로토콜
