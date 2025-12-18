---
title: troubleshooting
tags: [git, troubleshooting, recovery, reset, revert, fsck, reflog]
aliases: [Git 트러블슈팅, 실수 해결기, Git 복구, 데이터 심폐소생술]
date modified: 2025-12-18 16:20:00 +09:00
date created: 2025-12-18 14:25:00 +09:00
---

## Git 트러블슈팅: 실수를 기회로 바꾸는 복구의 기술

Git의 진가는 성공할 때가 아니라 **실수했을 때** 나타납니다. 모든 변경사항을 스냅샷으로 저장하는 Git의 특성을 활용하면, 지워진 브랜치나 분실한 커밋도 99% 복구가 가능합니다.

---

### 🏢 실무 사례 (Disaster Recovery)

- **삭제된 브랜치 복구**: 중요한 로직이 담긴 브랜치를 실수로 삭제했을 때, 커밋 해시만 알면 1초 만에 되살릴 수 있습니다.
- **잘못된 Force Push 복구**: 원격 저장소 히스토리가 파괴되었을 때, 내 로컬의 `reflog`를 뒤져 파괴 직전의 상태로 강제로 되돌립니다.
- **댕글링 커밋(Dangling Commit) 구출**: 브랜치에도 없고 로그에도 안 보이는, 하지만 분명히 존재했던 코드를 `git fsck`로 찾아냅니다.

---

## 🏗️ 3단계 되돌리기 가이드 (Undo Levels)

실수를 발견한 시점에 따라 해결 방법이 달라집니다. (자세한 원리는 [[02_advanced/reset-demystified|Reset 완벽 분석]] 참조)

### 1단계: Working Directory (작업 중 실패)
- **명령어**: `git restore <file>`
- **결과**: 현재 수정 중인 내용을 버리고 마지막 커밋 상태로 복구합니다.

### 2단계: Staging Area (`git add` 취소)
- **명령어**: `git restore --staged <file>`
- **결과**: 파일 수정 내용은 유지하되 커밋 대기 목록에서 제외합니다.

### 3단계: Local Repository (커밋 취소)
- **명령어**: `git reset --soft HEAD~1` (수정 사항 보존), `git reset --hard HEAD~1` (완전 파기)

---

## 🔥 전문가의 복구 도구: Reflog & FSCK

단순한 `log` 명령어로 찾을 수 없는 데이터는 다음 도구들을 사용합니다.

### 1. Git Reflog (최근 이동 기록)
HEAD 포인터가 지나간 모든 커밋 해시를 기록합니다. `reset`이나 `commit --amend`로 사라진 커밋도 여기서 찾을 수 있습니다.
```bash
git reflog
# a1b2c3d HEAD@{0}: reset: moving to HEAD~1
# e4f5g6h HEAD@{1}: commit: 중요한 버그 수정 완료  <-- 삭제된 커밋 발견!

git checkout -b recovered-branch e4f5g6h
```

### 2. Git FSCK (객체 무결성 검사)
어떤 브랜치나 태그에서도 참조되지 않는 '미아 객체(Dangling Objects)'를 찾아냅니다.
```bash
git fsck --full --unreachable
# unreachable commit e4f5g6h7... <-- 부모를 잃고 떠도는 커밋 해시
```
- **팁**: 찾은 해시값을 `git show <hash>`로 확인하여 내가 찾는 코드가 맞는지 확인한 후 브랜치를 새로 만듭니다.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **이미 Push한 커밋을 `reset` 하기** ❌
   - 협업 중인 브랜치에서 `reset` 후 `force push`를 하면 팀원들의 히스토리가 꼬여 '병합 지옥'이 시작됩니다. 이 경우 `git revert`를 사용하여 '취소하는 커밋'을 새로 만드세요.
2. **충돌 해결 중 마커(`<<<<`) 남기기** ❌
   - 충돌 마커를 포함해 커밋하면 빌드 에러가 발생합니다. `git status`로 충돌 파일을 확인하고 완벽히 해결한 후 커밋하세요.
3. **`reset --hard` 남발**
   - 현재 작업 중인 내용을 백업(`stash`)하지 않고 실행하면 복구가 불가능한 데이터 유실이 발생할 수 있습니다.
4. **가비지 컬렉션(`gc`) 수행** ⚠️
   - `git gc`를 실행하면 연결되지 않은 유실 객체들이 영구히 삭제될 수 있습니다. 복구 작업 중에는 절대 실행하지 마세요.

---

### 📚 연결 문서

- [[00_fundamentals/git-internals|Git 인턴십]] - 객체가 물리적으로 어떻게 저장되는지
- [[02_advanced/reset-demystified|Reset 완벽 분석]] - 영역별 데이터 이동의 원리
- [[02_advanced/advanced-workflows|고급 워크플로우]] - Rebase 중 발생하는 충돌 해결
- [[03_tools/git-customization|Git 커스텀]] - 사고를 예방하는 훅(Hook) 설정