# Git 트러블슈팅

## 자주 발생하는 문제들과 해결법

### 1. 잘못된 커밋 수정하기

#### 마지막 커밋 메시지 수정
```bash
git commit --amend -m "새로운 커밋 메시지"
```

#### 마지막 커밋에 파일 추가
```bash
git add forgotten-file.txt
git commit --amend --no-edit
```

#### 여러 커밋 수정 (Interactive Rebase)
```bash
git rebase -i HEAD~3  # 최근 3개 커밋 수정

# 에디터에서:
# pick -> reword: 메시지만 수정
# pick -> edit: 커밋 내용 수정
# pick -> squash: 이전 커밋과 합치기
```

### 2. 파일 되돌리기

#### 워킹 디렉토리의 변경사항 취소
```bash
git checkout -- file.txt        # 특정 파일
git checkout -- .               # 모든 파일
git restore file.txt            # 새로운 방법 (Git 2.23+)
```

#### 스테이징 취소
```bash
git reset HEAD file.txt         # 특정 파일
git reset HEAD .                # 모든 파일
git restore --staged file.txt   # 새로운 방법 (Git 2.23+)
```

#### 커밋 되돌리기
```bash
# 마지막 커밋 취소 (변경사항은 워킹 디렉토리에 유지)
git reset --soft HEAD~1

# 마지막 커밋과 스테이징 취소
git reset --mixed HEAD~1

# 모든 변경사항 완전 삭제 (위험!)
git reset --hard HEAD~1

# 안전한 되돌리기 (새로운 커밋으로)
git revert HEAD
```

### 3. 브랜치 문제 해결

#### 잘못된 브랜치에서 작업한 경우
```bash
# 현재 변경사항을 임시 저장
git stash

# 올바른 브랜치로 이동
git checkout correct-branch

# 변경사항 복원
git stash pop
```

#### 브랜치를 삭제했는데 복구하고 싶을 때
```bash
# 삭제된 브랜치의 커밋 해시 찾기
git reflog

# 브랜치 복구
git checkout -b recovered-branch <commit-hash>
```

#### 원격 브랜치가 삭제되었는데 로컬에 남아있을 때
```bash
# 원격에서 삭제된 브랜치 정리
git remote prune origin

# 또는
git fetch --prune
```

### 4. 병합 충돌 해결

#### 충돌 상황 이해하기
```bash
git status  # 충돌 파일 확인
```

#### 충돌 파일 내용
```
<<<<<<< HEAD
현재 브랜치의 내용
=======
병합하려는 브랜치의 내용
>>>>>>> feature-branch
```

#### 충돌 해결 단계
1. 충돌 파일을 직접 편집
2. 충돌 마커(`<<<<<<<`, `=======`, `>>>>>>>`) 제거
3. 원하는 내용으로 수정
4. 파일을 스테이징
5. 커밋

```bash
# 편집 후
git add resolved-file.txt
git commit -m "충돌 해결"
```

#### 병합 도구 사용
```bash
git mergetool  # 설정된 병합 도구 실행
```

#### 병합 취소
```bash
git merge --abort  # 병합 전 상태로 되돌리기
```

### 5. 원격 저장소 문제

#### Push 거부당했을 때
```bash
# 원격의 변경사항 먼저 가져오기
git fetch origin
git merge origin/main

# 또는
git pull origin main

# 이후 다시 push
git push origin main
```

#### Force Push 필요한 상황 (주의!)
```bash
# 더 안전한 force push
git push --force-with-lease origin main

# 위험한 force push (협업 시 금지!)
git push --force origin main
```

#### 원격 URL 변경
```bash
# 현재 원격 URL 확인
git remote -v

# URL 변경
git remote set-url origin https://github.com/username/repo.git
```

### 6. 스테이시 문제

#### 실수로 stash를 drop했을 때
```bash
# stash 기록 확인
git fsck --unreachable | grep commit

# stash 복구 (해시값 확인 후)
git stash apply <commit-hash>
```

#### 오래된 stash 정리
```bash
git stash list    # 모든 stash 보기
git stash clear   # 모든 stash 삭제
```

### 7. 인증 문제

#### HTTPS 인증 문제
```bash
# 인증 정보 저장 (Windows)
git config --global credential.helper manager

# 인증 정보 저장 (Mac)
git config --global credential.helper osxkeychain

# 인증 정보 저장 (Linux)
git config --global credential.helper store
```

#### SSH 키 문제
```bash
# SSH 키 확인
ssh -T git@github.com

# SSH 키 생성
ssh-keygen -t ed25519 -C "your.email@example.com"

# SSH 에이전트에 키 추가
ssh-add ~/.ssh/id_ed25519
```

### 8. 대용량 파일 문제

#### 실수로 커밋한 대용량 파일 제거
```bash
# 파일 히스토리에서 완전 제거
git filter-branch --force --index-filter \
'git rm --cached --ignore-unmatch large-file.zip' \
--prune-empty --tag-name-filter cat -- --all

# 또는 BFG Repo-Cleaner 사용 (더 빠름)
java -jar bfg.jar --delete-files large-file.zip
```

### 9. 라인 엔딩 문제

#### Windows/Linux 라인 엔딩 충돌
```bash
# Windows
git config --global core.autocrlf true

# Mac/Linux
git config --global core.autocrlf input

# 라인 엔딩 통일
git add --renormalize .
git commit -m "라인 엔딩 정규화"
```

### 10. 성능 문제

#### 느린 Git 작업 최적화
```bash
# 저장소 최적화
git gc --aggressive --prune=now

# 인덱스 재구성
git repack -ad

# 느린 status 해결 (대용량 저장소)
git config core.preloadindex true
git config core.fscache true
git config gc.auto 256
```

## 예방 방법

### 1. 좋은 습관들
- 커밋하기 전에 `git status`와 `git diff` 확인
- 중요한 작업 전에 브랜치 생성
- 정기적으로 원격 저장소와 동기화
- 큰 변경사항은 작은 단위로 나누어 커밋

### 2. 유용한 설정
```bash
# 자동으로 공백 문제 확인
git config --global core.whitespace trailing-space,space-before-tab

# 푸시 전 자동 테스트 (pre-push hook)
# .git/hooks/pre-push 파일 생성
#!/bin/sh
npm test
```

### 3. 백업 전략
```bash
# 중요한 작업 전 백업 브랜치 생성
git checkout -b backup-before-rebase

# 정기적으로 원격에 백업
git push origin feature-branch
```

## 복구 불가능한 상황

### 1. `git reset --hard` 후 변경사항 복구
```bash
# reflog에서 이전 상태 찾기
git reflog

# 이전 상태로 복구
git reset --hard HEAD@{1}
```

### 2. 실수로 삭제한 브랜치 복구
```bash
# reflog에서 브랜치의 마지막 커밋 찾기
git reflog --all

# 브랜치 재생성
git checkout -b recovered-branch <commit-hash>
```

### 3. 강제 푸시로 덮어쓴 원격 브랜치 복구
```bash
# 다른 팀원의 로컬 복사본에서 복구
# 또는 GitHub/GitLab의 보호된 브랜치 기능 활용
```

## 도움이 되는 도구들

### Git GUI 도구
- **GitHub Desktop**: 초보자 친화적
- **Sourcetree**: 고급 기능 지원
- **GitKraken**: 시각적 브랜치 관리
- **VS Code Git**: 에디터 통합

### 명령어 도구
```bash
# 더 예쁜 로그 보기
git log --oneline --graph --decorate --all

# 파일별 변경 통계
git log --stat

# 특정 단어가 언제 추가/삭제되었는지 추적
git log -S "search_term" --source --all
```

## 관련 문서
- [[Git 기본 개념]]
- [[Git 명령어 비교]]
- [[Git 고급 워크플로우]]
- [[Git 브랜치 전략]]