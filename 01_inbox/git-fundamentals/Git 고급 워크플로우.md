# Git 고급 워크플로우

## Git Flow
팀에서 사용하는 대표적인 브랜치 관리 전략

### 브랜치 종류
- **main/master**: 배포 가능한 안정적인 코드
- **develop**: 개발 중인 코드들이 모이는 곳
- **feature/**: 새로운 기능 개발용 브랜치
- **release/**: 배포 준비용 브랜치
- **hotfix/**: 긴급 버그 수정용 브랜치

```bash
# feature 브랜치 작업 흐름
git checkout develop
git checkout -b feature/login-page
# 개발 작업...
git add .
git commit -m "로그인 페이지 구현"
git checkout develop
git merge feature/login-page
git branch -d feature/login-page
```

## GitHub Flow
간단하고 실용적인 워크플로우

### 기본 원칙
1. main 브랜치는 항상 배포 가능한 상태
2. 새 기능은 브랜치에서 개발
3. Pull Request로 코드 리뷰
4. 테스트 통과 후 main에 병합
5. main에 병합하면 즉시 배포

```bash
# GitHub Flow 예시
git checkout main
git pull origin main
git checkout -b feature/user-profile
# 개발 작업...
git push -u origin feature/user-profile
# GitHub에서 Pull Request 생성
```

## Rebase vs Merge 전략

### Interactive Rebase
커밋 히스토리를 깔끔하게 정리

```bash
git rebase -i HEAD~3      # 최근 3개 커밋을 인터랙티브하게 수정

# 옵션들:
# pick: 커밋 그대로 사용
# reword: 커밋 메시지 수정
# edit: 커밋 내용 수정
# squash: 이전 커밋과 합치기
# drop: 커밋 삭제
```

### 언제 Rebase를 사용할까?
- 개인 브랜치에서 커밋 히스토리 정리할 때
- 공개되지 않은 로컬 커밋들을 정리할 때
- 깔끔한 히스토리를 원할 때

**주의사항**: 이미 원격에 올라간 커밋은 rebase하지 말기!

### 언제 Merge를 사용할까?
- 협업하는 브랜치에서
- 브랜치의 히스토리를 보존하고 싶을 때
- 안전하게 작업하고 싶을 때

## 고급 명령어들

### Cherry-pick
다른 브랜치의 특정 커밋만 가져오기

```bash
git cherry-pick abc1234   # 특정 커밋을 현재 브랜치에 적용
git cherry-pick abc1234..def5678  # 범위의 커밋들 적용
```

### Bisect
버그가 생긴 커밋을 찾기

```bash
git bisect start         # bisect 시작
git bisect bad          # 현재 커밋에 버그 있음
git bisect good v1.0    # v1.0에는 버그 없었음
# Git이 중간 커밋으로 이동
# 테스트 후 good 또는 bad 입력
git bisect good/bad
# 반복하면 문제 커밋을 찾아줌
git bisect reset        # bisect 종료
```

### Reflog
Git의 모든 행동 기록 보기

```bash
git reflog              # Git 행동 기록 보기
git reset --hard HEAD@{2}  # 2번째 이전 상태로 되돌리기
```

## 협업 시 주의사항

### Commit Convention
팀에서 정한 커밋 메시지 규칙 따르기

```
feat: 새로운 기능 추가
fix: 버그 수정
docs: 문서 변경
style: 코드 포맷팅
refactor: 코드 리팩토링
test: 테스트 코드
chore: 빌드 업무, 패키지 매니저 설정

예시:
feat: 사용자 로그인 기능 추가
fix: 패스워드 유효성 검사 버그 수정
```

### Force Push 주의사항
```bash
# 위험한 명령어 (협업 시 금지!)
git push --force

# 더 안전한 방법
git push --force-with-lease
```

### 대용량 파일 관리
Git LFS (Large File Storage) 사용

```bash
git lfs track "*.psd"    # .psd 파일을 LFS로 관리
git add .gitattributes
git add design.psd
git commit -m "디자인 파일 추가"
```

## 브랜치 보호 규칙
GitHub/GitLab에서 설정 가능한 보호 규칙들:

1. **Required reviews**: Pull Request에 최소 리뷰 개수 설정
2. **Status checks**: CI/CD 통과 필수
3. **Restrict pushes**: 직접 push 금지
4. **Require signed commits**: 서명된 커밋만 허용

## 고급 설정

### Git Hooks
특정 Git 이벤트 시 자동으로 실행되는 스크립트

```bash
# .git/hooks/pre-commit 파일 생성
#!/bin/sh
npm run lint      # 커밋 전 린트 검사
npm test         # 커밋 전 테스트 실행
```

### Git Aliases
자주 사용하는 명령어 단축키 설정

```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual '!gitk'
```

### 유용한 Git 설정
```bash
# 글로벌 사용자 정보
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 편집기 설정
git config --global core.editor "code --wait"

# 줄바꿈 설정 (Windows)
git config --global core.autocrlf true

# 줄바꿈 설정 (Mac/Linux)
git config --global core.autocrlf input

# 색깔 활성화
git config --global color.ui auto

# Push 기본 설정
git config --global push.default simple
```

## 성능 최적화

### 대용량 저장소 관리
```bash
# 저장소 최적화
git gc --aggressive

# 참조되지 않는 객체 정리
git prune

# 저장소 크기 확인
git count-objects -vH

# 특정 파일의 히스토리에서 완전 삭제
git filter-branch --force --index-filter \
'git rm --cached --ignore-unmatch huge-file.zip' \
--prune-empty --tag-name-filter cat -- --all
```

### Shallow Clone
히스토리를 제한해서 빠르게 클론

```bash
git clone --depth 1 <url>    # 최신 커밋만 가져오기
git clone --depth 5 <url>    # 최근 5개 커밋만 가져오기
```

## 관련 문서
- [[Git 기본 개념]]
- [[Git 명령어 비교]]
- [[Git 트러블슈팅]]
- [[Git 브랜치 전략]]
- [[Git 커밋 메시지 작성법]]