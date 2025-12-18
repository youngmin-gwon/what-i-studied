---
title: git-security-and-staging
tags: [git, gpg, interactive, security, signing, staging]
aliases: [Git 보안 및 상세 스테이징, 대화형 스테이징, 커밋 서명]
date modified: 2025-12-18 15:22:31 +09:00
date created: 2025-12-18 17:55:00 +09:00
---

## Git Security & Interactive Staging: 정교한 커밋과 신뢰의 기술

마스터 레벨의 개발자는 단순히 코드를 올리는 것을 넘어, 코드의 **신뢰성**을 보장하고 커밋의 **핵심만** 골라 담는 정교함을 갖추어야 합니다.

---

### 💡 Why it matters (Context)

- **신원 보증**: GPG 서명을 통해 "이 커밋은 정말 내가 작성했다"는 것을 증명하여 사칭을 방지합니다.
- **커밋 정제**: 하나의 파일에서 여러 수정을 했더라도, 논리적으로 연관된 부분만 골라 여러 개의 깔끔한 커밋으로 나눕니다.
- **보안 표준**: 기업용 리포지토리나 오픈소스 메인테이너 활동 시 서명된 커밋은 필수 요구사항인 경우가 많습니다.

---

## 🏗️ 1. Interactive Staging (`git add -i`)

작업한 내용을 한꺼번에 `add` 하는 대신, 대화형 인터페이스를 통해 선택적으로 스테이징합니다.

- **Patch Mode (`git add -p` / `-patch`)**: ⭐ 가장 많이 쓰이는 기능입니다. 파일 내의 변경 사항을 덩어리(Hunk)로 나누어 보여주며, 각 덩어리를 스테이징할지(`y`), 건너뛸지(`n`), 아니면 더 작게 쪼갤지(`s`) 결정할 수 있습니다.
- **Untracked 관리**: 새로 생성된 파일들만 골라서 스테이징할 수 있습니다.

---

## 🏗️ 2. Signing Your Work (GPG Signing)

커밋과 태그에 디지털 서명을 추가하여 위조 불가능한 신뢰를 구축합니다.

### 설정 방법
1. GPG 키 생성: `gpg --gen-key`
2. Git 에 키 등록: `git config --global user.signingkey <key_id>`
3. 자동 서명 활성화: `git config --global commit.gpgsign true`

### 사용 및 확인
- **태그 서명**: `git tag -s v1.5 -m 'my signed tag'`
- **서명 확인**: `git log --show-signature`. GitHub 에서는 서명된 커밋 옆에 **Verified** 배지가 표시됩니다.

---

## 🏗️ 3. Interactive Reset

스테이징된 내용 중 일부만 되돌리고 싶을 때도 대화형 모드를 사용할 수 있습니다.

- `git reset -p`: 스테이징된 변경 사항 중 특정 덩어리만 언스테이징합니다.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **너무 큰 Hunk 무작정 승인** ❌
   - `git add -p` 도중 연관 없는 수정 사항이 섞여 있다면 `s`(split) 명령어로 더 쪼개서 분리해야 합니다.
2. **GPG Passphrase 관리 부실**
   - 커밋할 때마다 비밀번호를 묻는 게 번거롭다면 `gpg-agent` 를 설정하여 메모리에 캐싱하세요.
3. **서명 없는 릴리스 태그** ⚠️
   - 공식 릴리스용 태그는 반드시 서명(`-s`)하여 배포판의 무결성을 증명해야 합니다.

---

### 📚 연결 문서

- [[00_fundamentals/basic-concepts|Git 기본 개념]] - 스테이징 영역(Index)의 기본 원리
- [[01_strategies/commit-messages|커밋 메시지]] - 정제된 커밋을 위한 메시지 작성법
- [[02_advanced/reset-demystified|Reset 완벽 분석]] - Reset 과 스테이징의 관계
- [[03_tools/credential-storage|인증 관리]] - 보안 키와 자격 증명 관리
