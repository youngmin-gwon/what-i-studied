---
title: git-migration
tags: [git, migration, svn, mercurial, p4]
aliases: [Git 마이그레이션, 타 VCS에서 전환, Git 상호운용성]
date modified: 2025-12-18 17:40:00 +09:00
date created: 2025-12-18 17:40:00 +09:00
---

## Git Migration: 다른 버전 관리 시스템에서 Git으로 갈아타기

이미 대규모 프로젝트가 SVN, Perforce, Mercurial 등으로 관리되고 있다면 Git으로의 전환은 단순한 파일 복사 이상의 작업이 필요합니다. 히스토리를 보존하면서 안전하게 이동하는 방법을 다룹니다.

---

### 💡 Why it matters (Context)

- **히스토리 보존**: 과거의 커밋 로그, 태그, 브랜치를 그대로 유지한 채 Git으로 옮겨야 과거의 맥락을 잃지 않습니다.
- **상호운용성**: 팀 전체가 한꺼번에 바꿀 수 없을 때, 일정 기간 동안 타 VCS와 Git을 병행해서 사용하는 기술이 필요합니다.
- **도구 선택**: 각 VCS마다 최적화된 공식 마이그레이션 도구를 활용하여 실수를 줄입니다.

---

## 🏗️ 1. Subversion(SVN)에서 마이그레이션

가장 흔한 케이스이며, Git에는 `git svn`이라는 강력한 내장 도구가 있습니다.

### Git을 SVN 클라이언트로 사용하기
```bash
git svn clone http://my-svn-repo.com/trunk -T trunk -b branches -t tags
```
- 이후 로컬에서는 Git 브랜치로 작업하고, `git svn dcommit`으로 SVN 서버에 반영할 수 있습니다.

### 완전히 전환하기
1. 사용자 매핑 파이 작성 (SVN 사용자명 -> Git 이름/이메일).
2. `git svn clone`으로 전체 히스토리 가져오기.
3. SVN 전용 태그와 브랜치를 Git 형식으로 정리.
4. 원격 Git 저장소 설정 후 Push.

---

## 🏗️ 2. 기타 VCS 마이그레이션

### Mercurial (Hg)
- `hg-fast-export` 같은 커스텀 스크립트를 사용하여 Git으로 변환합니다.

### Perforce (P4)
- Git 내장 도구인 `git p4`를 사용하여 Perforce 저장소와 동기화하거나 데이터를 가져옵니다.

---

## 🏗️ 3. 마이그레이션 후 체크리스트

1. **데이터 무결성 확인**: `git count-objects -v`로 모든 오브젝트가 정상적인지 확인합니다.
2. **.gitignore 설정**: SVN의 `ignore` 속성 등을 `.gitignore` 파일로 변환하여 적용합니다.
3. **바이너리 처리**: 대용량 바이너리 파일이 많다면 마이그레이션 직후 `git lfs`로 분리하는 작업을 고려해야 합니다.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **사용자 매핑 누락** ❌
   - 작성자를 매핑하지 않으면 Git 히스토리에 SVN 계정명이 그대로 남아 가독성이 떨어집니다.
2. **비어있는 브랜치/태그 방치**
   - SVN의 독특한 브랜치 구조가 Git으로 오면서 불필요한 디렉토리로 남을 수 있으니 정리가 필요합니다.
3. **점진적 전환의 함정**
   - Git과 SVN을 동시에 쓰면 '양방향 동기화' 과정에서 충돌이 나기 매우 쉽습니다. 가능한 짧은 기간 내에 완전히 전환하는 것이 좋습니다.

---

### 📚 연결 문서

- [[02_advanced/advanced-workflows|고급 워크플로우]] - 마이그레이션 후 대용량 파일 처리를 위한 `filter-repo`
- [[00_fundamentals/git-internals|Git 인턴십]] - 타 VCS와 Git의 데이터 모델 차이 이해
- [[03_tools/git-customization|Git 커스텀]] - 마이그레이션 후 필요한 설정 최적화