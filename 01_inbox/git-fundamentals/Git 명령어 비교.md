# Git 명령어 비교

## 초기 설정
### git init vs git clone
- **git init**: 빈 폴더에서 새로운 Git 저장소를 시작
- **git clone**: 다른 곳에 있는 저장소를 복사해서 가져옴

```bash
git init                    # 현재 폴더를 Git 저장소로 만들기
git clone <url>            # 원격 저장소를 복사해오기
```

## 파일 상태 확인
### git status vs git diff vs git log
- **git status**: 현재 파일들의 상태를 간단히 보여줌
- **git diff**: 파일의 구체적인 변경 내용을 줄 단위로 보여줌
- **git log**: 지금까지의 커밋 기록을 시간순으로 보여줌

```bash
git status                 # 어떤 파일이 변경되었는지 확인
git diff                   # 무엇이 바뀌었는지 자세히 확인
git log                    # 커밋 히스토리 확인
git log --oneline         # 커밋을 한 줄씩 간단히 보기
```

## 파일 추가하기
### git add의 다양한 방법
```bash
git add file.txt          # 특정 파일만 스테이징
git add .                 # 현재 폴더의 모든 변경사항 스테이징
git add -A                # 전체 저장소의 모든 변경사항 스테이징
git add -p                # 변경사항을 부분별로 선택해서 스테이징
```

## 커밋하기
### git commit vs git commit -a
- **git commit**: 스테이징된 파일들만 커밋
- **git commit -a**: 수정된 파일들을 자동으로 스테이징하고 커밋

```bash
git commit -m "메시지"        # 스테이징된 파일들 커밋
git commit -a -m "메시지"     # 수정된 파일들 자동 스테이징 후 커밋
git commit --amend           # 마지막 커밋을 수정
```

## 되돌리기 명령어들
### git reset vs git revert vs git checkout
- **git reset**: 커밋을 완전히 없던 일로 만듦 (위험함)
- **git revert**: 이전 커밋을 취소하는 새로운 커밋을 만듦 (안전함)
- **git checkout**: 특정 커밋이나 브랜치로 이동

```bash
# reset의 세 가지 모드
git reset --soft HEAD~1    # 커밋만 취소, 변경사항은 스테이징에 유지
git reset --mixed HEAD~1   # 커밋과 스테이징 취소, 변경사항은 워킹 디렉토리에 유지
git reset --hard HEAD~1    # 커밋, 스테이징, 변경사항 모두 삭제 (주의!)

# 안전한 되돌리기
git revert HEAD            # 마지막 커밋을 취소하는 새 커밋 생성

# 파일 복구
git checkout -- file.txt  # 특정 파일의 변경사항 취소
git checkout HEAD~1 file.txt  # 이전 커밋에서 파일 복구
```

## 브랜치 작업
### git branch vs git checkout vs git switch
- **git branch**: 브랜치 목록 보기, 생성, 삭제
- **git checkout**: 브랜치 전환 (구버전 명령어)
- **git switch**: 브랜치 전환 (신버전 명령어, 더 명확함)

```bash
# 브랜치 보기와 관리
git branch                 # 브랜치 목록 보기
git branch new-feature     # 새 브랜치 생성
git branch -d old-feature  # 브랜치 삭제

# 브랜치 전환 (둘 다 같은 기능)
git checkout main          # main 브랜치로 전환 (구버전)
git switch main            # main 브랜치로 전환 (신버전)

# 브랜치 생성과 전환을 동시에
git checkout -b new-feature  # 새 브랜치 생성 후 전환 (구버전)
git switch -c new-feature    # 새 브랜치 생성 후 전환 (신버전)
```

## 병합하기
### git merge vs git rebase
- **git merge**: 두 브랜치를 합치는 새로운 커밋을 만듦
- **git rebase**: 한 브랜치의 커밋들을 다른 브랜치 위로 옮김

```bash
git merge feature-branch   # feature-branch를 현재 브랜치에 병합
git rebase main           # 현재 브랜치의 커밋들을 main 위로 옮김
```

**언제 어떤 것을 써야 할까?**
- **merge**: 협업할 때, 브랜치 히스토리를 보존하고 싶을 때
- **rebase**: 깔끔한 히스토리를 원할 때, 개인 브랜치에서만 사용

## 원격 저장소 작업
### git fetch vs git pull
- **git fetch**: 원격 저장소의 변경사항만 가져옴 (자동 병합 안함)
- **git pull**: 원격 저장소의 변경사항을 가져와서 자동으로 병합함

```bash
git fetch origin          # 원격 저장소의 변경사항만 가져오기
git pull origin main      # 원격 저장소의 변경사항을 가져와서 병합

# pull은 사실 fetch + merge의 조합
git fetch origin
git merge origin/main     # 위 두 명령어가 git pull과 같음
```

### git push의 옵션들
```bash
git push origin main            # main 브랜치를 원격으로 전송
git push -u origin feature      # 새 브랜치를 원격에 생성하며 전송
git push --force               # 강제로 푸시 (위험함, 협업 시 금지)
git push --force-with-lease    # 더 안전한 강제 푸시
```

## 정보 확인 명령어들
### git show vs git blame vs git grep
```bash
git show HEAD                  # 최근 커밋의 상세 정보
git blame file.txt            # 각 줄을 누가 언제 수정했는지 확인
git grep "검색어"              # 저장소에서 코드 검색
git log --grep="버그"          # 커밋 메시지에서 검색
```

## 임시 저장
### git stash
```bash
git stash                     # 현재 변경사항을 임시 저장
git stash list               # 저장된 stash 목록 보기
git stash apply              # 가장 최근 stash 적용
git stash pop                # 가장 최근 stash 적용 후 삭제
git stash drop               # stash 삭제
```

## 관련 문서
- [[Git 기본 개념]]
- [[Git 고급 워크플로우]]
- [[Git 트러블슈팅]]
- [[Git 브랜치 전략]]