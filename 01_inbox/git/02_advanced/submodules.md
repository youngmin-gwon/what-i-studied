---
title: submodules
tags: [git, advanced, submodules, collaboration]
aliases: [Git 서브모듈 가이드, 외부 저장소 연동, Sub-projects]
date modified: 2025-12-18 15:50:00 +09:00
date created: 2025-12-18 15:50:00 +09:00
---

## Git 서브모듈: 프로젝트 안의 프로젝트 관리하기

실무에서는 하나의 레포지토리 안에 다른 외부 라이브러리나 공통 모듈을 포함시켜야 하는 경우가 많습니다. **Git Submodule**은 이를 위한 공식적인 해결책으로, 외부 저장소를 내 저장소의 특정 디렉토리에 '박제'하는 기능을 제공합니다.

---

### 💡 Why it matters (Context)

- **의존성 분리**: 공통 라이브러리를 복사-붙여넣기 하지 않고, 원본 저장소의 특정 커밋을 가리키게 하여 업데이트를 체계적으로 관리합니다.
- **버전 고정**: 외부 라이브러리가 업데이트되어도 내 프로젝트가 의존하는 특정 '황금 버전'을 유지할 수 있습니다.
- **대규모 아키텍처**: 수십 개의 마이크로서비스(MSA) 환경에서 공통 스키마나 툴킷을 공유할 때 필수적입니다.

---

## 🏗️ 서브모듈 핵심 워크플로우

### 1. 서브모듈 추가하기
```bash
git submodule add https://github.com/user/library.git external/lib
```
- 결과: `.gitmodules`라는 설정 파일이 생성되고, 해당 디렉토리에 외부 코드가 들어옵니다.

### 2. 프로젝트 클론 및 서브모듈 초기화
서브모듈이 포함된 프로젝트를 처음 클론하면 서브모듈 디렉토리는 비어있습니다.
```bash
# 한 번에 가져오기
git clone --recursive https://github.com/user/main-project.git

# 이미 클론한 후라면
git submodule update --init --recursive
```

### 3. 서브모듈 업데이트하기
외부 저장소에 새 커밋이 올라왔을 때 내 프로젝트에 반영하려면:
```bash
cd external/lib
git fetch
git merge origin/main
cd ../..
git add external/lib  # 서브모듈이 가리키는 커밋 해시가 변경됨을 커밋해야 함
```

---

## 🚨 흔한 실수 (Common Mistakes)

1. **Detached HEAD 상태에서의 수정** ❌
   - 서브모듈은 기본적으로 특정 '커밋 해시'를 가리키므로 브랜치가 없는 상태가 되기 쉽습니다. 이 상태에서 코드를 고치고 커밋하면 브랜치가 없어 나중에 찾기 힘들어집니다. 수정 전 반드시 `git checkout main`으로 브랜치를 잡으세요.
2. **서브모듈 커밋 누락** ❌
   - 서브모듈 내부에서 커밋만 하고, 상위(Main) 프로젝트에서 "서브모듈 포인터 변경 사항"을 커밋/푸시하지 않으면 팀원들이 코드를 받을 때 에러가 발생합니다.
3. **로컬 경로 문제**
   - `.gitmodules` 파일에 상대 경로가 아닌 절대 경로를 적으면 다른 환경(CI 서버 등)에서 클론할 때 인증 문제나 경로 오류가 발생할 수 있습니다. 가능한 상대 경로를 사용하세요.

---

### 📚 연결 문서

- [[01_strategies/branching-strategies|브랜치 전략]] - 대규모 프로젝트에서의 모듈 구조 설계
- [[02_advanced/advanced-workflows|고급 워크플로우]] - 서브모듈을 포함한 복잡한 히스토리 관리
- [[00_fundamentals/git-internals|Git 인턴십]] - 서브모듈이 왜 '파일'이 아닌 '커밋 해시 포인터'로 저장되는지 이해