# Git 브랜치 전략

## 브랜치 전략이 필요한 이유
여러 사람이 동시에 작업할 때 코드 충돌을 방지하고, 안정적인 배포를 위해 필요합니다.

## 주요 브랜치 전략들

### 1. Git Flow (가장 복잡, 큰 팀용)

#### 브랜치 구조
- **main**: 배포된 안정적인 코드만
- **develop**: 개발 중인 코드들이 모이는 곳
- **feature/기능명**: 새 기능 개발
- **release/버전**: 배포 준비
- **hotfix/이슈명**: 긴급 수정

#### 작업 흐름
```bash
# 1. 새 기능 개발 시작
git checkout develop
git checkout -b feature/user-login

# 2. 기능 개발 완료
git checkout develop
git merge feature/user-login
git branch -d feature/user-login

# 3. 배포 준비
git checkout develop
git checkout -b release/1.2.0
# 버그 수정, 문서 업데이트 등

# 4. 배포
git checkout main
git merge release/1.2.0
git tag v1.2.0
git checkout develop
git merge release/1.2.0

# 5. 긴급 수정 시
git checkout main
git checkout -b hotfix/critical-bug
# 수정 작업
git checkout main
git merge hotfix/critical-bug
git checkout develop
git merge hotfix/critical-bug
```

**장점**: 체계적, 안정적
**단점**: 복잡함, 오버헤드 큼

### 2. GitHub Flow (가장 간단, 소규모 팀용)

#### 브랜치 구조
- **main**: 모든 작업의 중심
- **feature/기능명**: 모든 새 작업

#### 작업 흐름
```bash
# 1. 새 작업 시작
git checkout main
git pull origin main
git checkout -b feature/add-search

# 2. 작업 완료 후 Push
git push -u origin feature/add-search

# 3. Pull Request 생성 (GitHub에서)
# 4. 코드 리뷰 후 main에 병합
# 5. main에서 즉시 배포
```

**장점**: 단순함, 빠른 배포
**단점**: main 브랜치 안정성 의존

### 3. GitLab Flow (중간 복잡도)

#### 환경별 브랜치
- **main**: 개발 코드
- **pre-production**: 스테이징 환경
- **production**: 실제 서비스

#### 작업 흐름
```bash
# 1. 기능 개발
git checkout main
git checkout -b feature/new-dashboard

# 2. main에 병합
# 3. pre-production에 병합 (테스트)
# 4. production에 병합 (배포)
```

### 4. OneFlow (단순화된 Git Flow)

#### 특징
- main 브랜치만 장기 브랜치로 유지
- 릴리스 브랜치를 기능별로 생성
- 히스토리가 깔끔함

## 브랜치 명명 규칙

### 기능별 분류
```bash
feature/기능명          # 새로운 기능
bugfix/버그명           # 버그 수정
hotfix/긴급수정명       # 긴급 수정
release/버전명          # 릴리스 준비
refactor/리팩토링명     # 코드 리팩토링
docs/문서명             # 문서 작업
style/스타일명          # 코드 스타일 변경
test/테스트명           # 테스트 코드
chore/작업명            # 기타 작업
```

### 예시
```bash
feature/user-authentication
feature/payment-integration
bugfix/login-validation-error
hotfix/security-vulnerability
release/v2.1.0
refactor/database-optimization
docs/api-documentation
```

## 팀 규모별 추천 전략

### 소규모 팀 (1-3명)
- **GitHub Flow** 추천
- 간단하고 빠른 개발 가능
- main 브랜치 중심으로 작업

### 중규모 팀 (4-10명)
- **GitLab Flow** 또는 **simplified Git Flow** 추천
- 환경별 브랜치로 안정성 확보
- 코드 리뷰 프로세스 도입

### 대규모 팀 (10명 이상)
- **Git Flow** 추천
- 체계적인 릴리스 관리
- 명확한 역할 분담

## 브랜치 보호 규칙 설정

### GitHub 설정
```bash
# main 브랜치 보호 설정:
1. Settings > Branches
2. Add rule for main
3. Require pull request reviews
4. Require status checks to pass
5. Restrict pushes to main
```

### 로컬 훅 설정
```bash
# .git/hooks/pre-push
#!/bin/sh
branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$branch" = "main" ]; then
  echo "main 브랜치에 직접 push할 수 없습니다!"
  exit 1
fi
```

## 병합 전략

### 1. Merge Commit (기본)
```bash
git checkout main
git merge feature/new-feature
```
- 브랜치 히스토리 보존
- 병합 지점 명확

### 2. Squash and Merge
```bash
git checkout main
git merge --squash feature/new-feature
git commit -m "새 기능 추가"
```
- 깔끔한 히스토리
- 브랜치의 모든 커밋을 하나로 압축

### 3. Rebase and Merge
```bash
git checkout feature/new-feature
git rebase main
git checkout main
git merge feature/new-feature
```
- 선형적인 히스토리
- 병합 커밋 없음

## 릴리스 관리

### 시맨틱 버저닝
```
MAJOR.MINOR.PATCH
예: 2.1.3

MAJOR: 호환되지 않는 API 변경
MINOR: 하위 호환 가능한 기능 추가
PATCH: 하위 호환 가능한 버그 수정
```

### 태그 관리
```bash
# 태그 생성
git tag v1.0.0
git tag -a v1.0.0 -m "버전 1.0.0 릴리스"

# 태그 푸시
git push origin v1.0.0
git push origin --tags

# 태그 기반 릴리스 브랜치 생성
git checkout -b release/v1.0.0 v0.9.0
```

## 충돌 해결 전략

### 자동 병합 설정
```bash
# merge 시 Fast-forward만 허용
git config --global merge.ff only

# rebase 시 자동으로 stash
git config --global rebase.autoStash true
```

### 충돌 해결 도구
```bash
# 기본 merge 도구 설정
git config --global merge.tool vimdiff
git config --global merge.tool code

# 충돌 해결
git mergetool
```

## 모니터링과 분석

### 브랜치 분석
```bash
# 브랜치별 커밋 수
git for-each-ref --format='%(refname:short) %(committerdate)' refs/heads

# 오래된 브랜치 찾기
git for-each-ref --format='%(refname:short) %(committerdate)' --sort=committerdate refs/heads

# 병합되지 않은 브랜치 찾기
git branch --no-merged main
```

### 개발자별 기여도
```bash
# 커밋 수 통계
git shortlog -sn

# 특정 기간 통계
git shortlog -sn --since="1 month ago"
```

## 자동화 팁

### Git Hooks 활용
```bash
# pre-commit: 커밋 전 검사
#!/bin/sh
npm run lint
npm test

# pre-push: 푸시 전 검사
#!/bin/sh
branch=$(git rev-parse --abbrev-ref HEAD)
if [[ "$branch" =~ ^(main|develop)$ ]]; then
    echo "Protected branch에 직접 push 금지!"
    exit 1
fi
```

### CI/CD 연동
```yaml
# .github/workflows/branch-check.yml
name: Branch Check
on:
  pull_request:
    branches: [main]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: npm ci
      - run: npm test
      - run: npm run lint
```

## 관련 문서
- [[Git 기본 개념]]
- [[Git 명령어 비교]]
- [[Git 고급 워크플로우]]
- [[Git 커밋 메시지 작성법]]