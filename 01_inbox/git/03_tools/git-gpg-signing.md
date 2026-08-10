---
title: git-gpg-signing
tags: [git, gpg, security, signing]
aliases: [GPG 서명, 커밋 서명, 디지털 서명]
date modified: 2026-08-10
date created: 2025-12-18
---

## Git GPG Signing: 신뢰의 기술

마스터 레벨의 개발자는 단순히 코드를 올리는 것을 넘어, 코드의 **신뢰성**을 보장하는 정교함을 갖추어야 합니다.

---

### 💡 Why it matters (Context)

- **신원 보증**: GPG 서명을 통해 "이 커밋은 정말 내가 작성했다"는 것을 증명하여 사칭을 방지합니다.
- **보안 표준**: 기업용 리포지토리나 오픈소스 메인테이너 활동 시 서명된 커밋은 필수 요구사항인 경우가 많습니다.
- **배포판 무결성**: 릴리스 태그에 서명하여 다운로드한 코드가 위조되지 않았음을 증명할 수 있습니다.

---

## 🏗️ 1. Signing Your Work (GPG Signing)

커밋과 태그에 디지털 서명을 추가하여 위조 불가능한 신뢰를 구축합니다.

### 설정 방법
1. GPG 키 생성: `gpg --gen-key`
2. Git 에 키 등록: `git config --global user.signingkey <key_id>`
3. 자동 서명 활성화: `git config --global commit.gpgsign true`

### 사용 및 확인
- **태그 서명**: `git tag -s v1.5 -m 'my signed tag'`
- **서명 확인**: `git log --show-signature`. GitHub 에서는 서명된 커밋 옆에 **Verified** 배지가 표시됩니다.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **GPG Passphrase 관리 부실**
   - 커밋할 때마다 비밀번호를 묻는 게 번거롭다면 `gpg-agent` 를 설정하여 메모리에 캐싱하세요.
2. **서명 없는 릴리스 태그** ⚠️
   - 공식 릴리스용 태그는 반드시 서명(`-s`)하여 배포판의 무결성을 증명해야 합니다.

---

### 📚 연결 문서

- [Git 기본 개념](../00_fundamentals/basic-concepts.md) - 커밋의 기본 원리
- [인증 관리](credential-storage.md) - 보안 키와 자격 증명 관리
- [대화형 스테이징](interactive-staging.md) - 선택적 커밋 준비
