---
title: credential-storage
tags: [git, security, credentials, keychain, auth]
aliases: [Git 인증 관리, 비밀번호 저장, Git Credential Helper]
date modified: 2025-12-18 17:30:00 +09:00
date created: 2025-12-18 17:30:00 +09:00
---

## Git Credential Storage: 매번 비밀번호를 입력하지 않는 법

HTTP(S) 프로토콜을 사용하여 Git 서버와 통신할 때, 매번 아이디와 비밀번호(또는 Token)를 입력하는 것은 매우 번거로운 일입니다. Git은 이를 안전하고 편리하게 관리해주는 **Credential Helper** 시스템을 제공합니다.

---

### 💡 Why it matters (Context)

- **사용자 경험**: 매번 입력하는 피로도를 줄여 개발 생산성을 높입니다.
- **보안**: 비밀번호를 텍스트 파일이나 쉘 히스토리에 남기지 않고, OS의 전용 키체인(Keychain)이나 보안 매니저에 저장합니다.
- **자동화**: CI/CD 환경이나 스크립트에서 인증 과정을 자동화할 수 있습니다.

---

## 🏗️ 1. Credential Helper의 종류

시스템 환경에 따라 적합한 헬퍼를 선택하여 설정합니다.

### OS 전용 관리자 (가장 안전)
- **Mac**: `git config --global credential.helper osxkeychain` (시스템 키체인 활용)
- **Windows**: `git config --global credential.helper manager` (Git Credential Manager 활용)
- **Linux (GUI)**: `git config --global credential.helper libsecret`

### 범용 방식
- **Cache**: 정보를 메모리에 잠시 보관합니다. `git config --global credential.helper 'cache --timeout=3600'`
- **Store**: 정보를 **평문 텍스트**로 파일에 저장합니다. **(보안상 권장되지 않음)** `git config --global credential.helper store`

---

## 🏗️ 2. 개인용 액세스 토큰 (PAT) 활용

최근 GitHub를 비롯한 대부분의 서비스는 보안을 위해 일반 비밀번호 대신 **Personal Access Token** 사용을 강제합니다.
1. 서비스 설정에서 토큰을 생성합니다.
2. 처음 인증 시 비밀번호 대신 이 토큰을 입력합니다.
3. 설정된 Credential Helper가 이를 기억하여 다음부터는 자동으로 사용합니다.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **`store` 헬퍼 사용** ❌
   - `store` 방식은 `~/.git-credentials` 파일에 비밀번호를 평문으로 저장합니다. 컴퓨터를 분실하거나 파일이 유출되면 계정이 완전히 털릴 수 있으므로 절대 쓰지 마세요.
2. **토큰 유효기간 만료**
   - 인증이 갑자기 안 된다면 토큰의 유효기간이 지났을 가능성이 큽니다. 새 토큰을 발급받아 업데이트하세요.
3. **URL에 비밀번호 포함** ❌
   - `https://user:password@github.com` 형식을 사용하면 쉘 히스토리나 `.git/config`에 비밀번호가 남습니다. 반드시 Credential Helper를 사용하세요.

---

### 📚 연결 문서

- [[02_advanced/git-server|Git 서버]] - HTTP vs SSH 프로토콜의 인증 차이
- [[03_tools/git-customization|Git 커스텀]] - 설정 파일의 계층 구조 이해
- [[01_strategies/github-mastery|GitHub 마스터]] - GitHub 토큰 생성 및 관리