# git 커맨드 요약
## git reset vs revert
- 요약
	- reset: 로컬의 커밋을 되돌리고 싶을 때 사용(기록 남지 않음)
	- revert: 공유 repository의 커밋을 되돌리고 싶을 때 사용(기록 남음)
- 상세
	- reset
		- 새로운 커밋을 남기지 않고 되돌림
		- 세가지 옵션
			- --soft: commit -> staging area
			- --mixed(default): commit -> working directory
			- --hard: commit -> none
	![[git_reset.png]]
	- revert
		- 커밋 내역을 그대로 남겨둔 채 새로운 커밋을 생성해서 되돌림
		![[git_revert_1.png]]
```shell
git revert 5lk4er
git revert 76sdeb
```
![[git_revert_2.png]]
- 그대로 남겨둔채 새로운 커밋을 생성함
```