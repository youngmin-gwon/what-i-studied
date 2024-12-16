---
aliases: []
date created: 2024-12-09 21:31:10 +09:00
date modified: 2024-12-16 12:21:06 +09:00
tags: [command, git]
title: git commands
---

## git reset

### 1. HEAD 가 가리키는 브랜치를 옮김 (--soft or hash key)

`checkout` 명령처럼 HEAD 가 가리키는 브랜치를 바꾸지 않음

HEAD 는 계속해서 현재 브랜치를 가리키고 있고, 현재 브랜치가 가리키는 커밋을 바꿈

### 2. Index 를 HEAD 가 가리키는 상태로 만듬 (--mixed)

reset 기본 옵션

### 3. 워킹 디렉토리를 Index 상태로 만듬 (--hard)

`--hard` 옵션은 되돌리는 것이 없기 때문에 항상 주의

reset 명령을 위험하게 만드는 유일한 옵션

특정 커밋을 명시하면 `git` 은 HEAD 에서 파일을 가져오는 것이 아니라 그 커밋에서 파일을 가져옴

합치기 (squash) 역할도 가능함

- 명령어가 따로 있지만 reset 으로도 가능함

```shell
git reset --soft HEAD~2 # 이와 같은 명령으로 몇 단계 전으로 돌려서 다시 커밋할 수 있음
```

### 다른 command 와의 차이점

#### [1] git reset vs revert

##### 요약

`reset`: 로컬의 커밋을 되돌리고 싶을 때 사용 (기록 남지 않음)

`revert`: 공유 repository 의 커밋을 되돌리고 싶을 때 사용 (기록 남음)

##### 상세

`reset`

새로운 커밋을 남기지 않고 되돌림

세가지 옵션

```plaintext
--soft: commit -> staging area
--mixed(default): commit -> working directory
--hard: commit -> none
```

![[../_assets/git/git_reset.png]]

커밋을 지정하지 않으면 staging area 에 있는 변경사항만 처리

`revert`

커밋 내역을 그대로 남겨둔 채 새로운 커밋을 생성해서 되돌림

![[../_assets/git/git_revert_1.png]]

```shell
git revert 5lk4er
git revert 76sdeb
```

![[../_assets/git/git_revert_2.png]]

그대로 남겨둔채 새로운 커밋을 생성함

#### [2] git reset --hard vs git clean

`git reset --hard`: staging area 에 있는 변경 사항 삭제

`git clean`: working directory 에 있는 변경 사항 삭제

#### [3] git reset vs git checkout

##### {1} 경로 없음

`git reset --hard [branch]` 명령과 비슷하게 [branch] 스냅샷을 기준으로 세 트리를 조작하지만 두가지 사항이 다름

1. 워킹 디렉토리를 안전하게 다뤄 저장하지 않은 것을 날리지 않음
2. reset 명령은 HEAD 가 가리키는 브랜치를 움직이지만, checkout 명령은 HEAD 자체를 다른 브랜치로 옮김

결과적으로 같은 커밋을 가리키게 되지만 방식은 완전히 다름

``` shell
# 1
git reset master
# 2
git checkout master
```

![[../_assets/git/git-reset-checkout.png]]

##### {2} 경로 있음

reset 명령과 비슷하게 HEAD 는 움직이지 않음

`git reset [branch] file` 명령과 비슷함

Index 내용이 해당 커밋 버전으로 변경될 뿐만 아니라 워킹 디렉토리의 파일도 해당 커밋 버전으로 변경됨

완전히 `git reset --hard [branch] file` 명령의 동직이랑 같다 → 워킹 디렉토리가 안전하지 않다는 의미

`git reset` 이나 `git add` 명령처럼 `git checkout` 명령도 `--patch` 옵션을 사용해서 Hunk 단위로 되돌릴수 있음

## git checkout

reset 과 마찬가지로 HEAD, Index, Working Directory 트리를 조작함

checkout 역시 파일 경로를 쓰느냐 안쓰느냐에 따라 동작이 다름

## git clean

> working directory 에 있는 변경 사항 삭제

옵션을 주지 않으면 사용할 수 없음

- 위험한 결과를 초래할 수 있는 명령어 이기 때문에 의도하지 않은 사용 막은 것

옵션

```plaintext
-i : interactive 하게 보여줌
-n : dry run, 시뮬레이션 결과만 보여주고 실제 삭제하지는 않음
-f : 강제 삭제
-x : ignore된 파일도 포함해서 삭제
-X :  ignore된 파일만 삭제
```

## git diff

파일이 변경됐다는 사실이 아니라 어떤 내용이 변경됐는지 살펴볼 때 사용하는 명령어
