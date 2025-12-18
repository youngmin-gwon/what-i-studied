---
title: git-customization
tags: [git, customization, config, attributes, hooks, env]
aliases: [Git 설정 및 커스터마이즈, Git 자동화, .gitattributes, Git Hooks, 환경 변수]
date modified: 2025-12-18 18:05:00 +09:00
date created: 2025-12-18 16:10:00 +09:00
---

## Git 커스터마이징: 프로젝트에 최적화된 도구로 만들기

Git은 매우 유연한 도구입니다. 설정(`config`), 파일 속성(`attributes`), 스크립트 기반 자동화(`hooks`), 그리고 **환경 변수(Environment Variables)**를 통해 개인과 팀의 워크플로우에 완벽하게 맞출 수 있습니다.

---

### 💡 Why it matters (Context)

- **표준화**: 팀원 간의 줄바꿈 설정(`crlf`)이나 파일 인코딩 문제를 방지합니다.
- **자동화**: 커밋 전 코드 스타일 체크(Lint), 푸시 전 테스트 실행 등을 자동화하여 품질을 유지합니다.
- **프로그래밍 방식 제어**: 환경 변수를 통해 설정 파일 수정 없이 Git의 행동을 일시적으로 제어하거나 스크립팅합니다.

---

## 🏗️ 1. Git 설정 (Configuration)

설정은 적용 범위에 따라 세 단계로 나뉩니다. (System, Global, Local)
> [!TIP] **별칭(Alias) 활용**
> `git config --global alias.co checkout`: `git co`로 단축 사용 가능.
> `git config --global alias.lg "log --graph --oneline --all"`: 히스토리 시각화 단축키.

---

## 🏗️ 2. Git Attributes (`.gitattributes`)

특정 파일이나 디렉토리에 대해 Git이 어떻게 행동해야 하는지 정의합니다.
- **줄바꿈 관리**: `* text=auto` (OS에 따라 자동 변환)
- **바이너리 지정**: `*.jpg binary` (병합 충돌 방지 및 델타 압축 최적화)

---

## 🏗️ 3. Git Hooks (스크립트 자동화)

특정 이벤트(커밋, 푸시 등) 시 자동 실행되는 스크립트입니다.
- **클라이언트 사이드**: `pre-commit`, `commit-msg`, `pre-push`.
- **서버 사이드**: `pre-receive`, `post-receive`.

---

## 🏗️ 4. Git 환경 변수 (Environment Variables) ⭐

Git은 실행 시 특정 환경 변수를 참조하여 설정을 덮어쓰거나 동작을 바꿉니다. 스크립트 작성 시 매우 유용합니다.

### 작성자 정보 덮어쓰기

- `GIT_AUTHOR_NAME`, `GIT_AUTHOR_EMAIL`: 커밋의 '작성자' 정보를 일시적으로 변경합니다.
- `GIT_COMMITTER_NAME`, `GIT_COMMITTER_EMAIL`: 커밋을 '수정한 사람' 정보를 변경합니다.

### 경로 및 위치 제어

- `GIT_DIR`: `.git` 디렉토리의 위치를 직접 지정합니다.
- `GIT_WORK_TREE`: 워킹 디렉토리의 위치를 지정합니다.

### 기타 통제

- `GIT_SSH`: Git이 사용할 SSH 명령어를 지정합니다.
- `GIT_PAGER`: `log` 등을 볼 때 사용할 페이지 프로그램을 설정합니다.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **환경 변수 오염** ❌
   - 쉘 설정 파일(`~/.zshrc` 등)에 Git 환경 변수를 고정해두면, 나중에 원인을 알 수 없는 의도치 않은 커밋 정보 변경이 발생할 수 있습니다. 필요한 경우에만 일시적으로 선언(`export`) 하세요.
2. **훅 스크립트 공유 누락**
   - `.git/hooks`는 레포지토리에 포함되지 않으므로 팀 내 별도 공유 체계가 필요합니다.

---

### 📚 연결 문서

- [[01_strategies/commit-messages|커밋 메시지]] - 훅을 이용한 메시지 규칙 강제화
- [[02_advanced/advanced-workflows|고급 워크플로우]] - 환경 변수를 이용한 자동화 스크립트 작성
- [[00_fundamentals/git-internals|Git 인턴십]] - 설정과 환경 변수가 조회되는 순서 이해