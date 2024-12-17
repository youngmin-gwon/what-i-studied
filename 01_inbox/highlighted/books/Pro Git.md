## Metadata
- Author: Scott Chacon
- [Apple Books Link](ibooks://assetid/80CD3C03D7A40678ED51F4140647F20B)

## Highlights
Git은 데이터를 파일 시스템 스냅샷의 연속으로 취급하고 크기가 아주 작다

---
되돌리기

---
Staging Area는 Git 디렉토리에 있다. 단순한 파일이고 곧 커밋할 파일에 대한 정보를 저장

---
CVS, Subversion, Perforce, Bazaar 등의 시스템은 각 파일의 변화를 시간순으로 관리하면서 파일들의 집합을 관리한다(보통 델타 기반 버전관리 시스템이라 함).

---
git rm

---
Committed, Modified, Staged

---
가장 큰 차이점은 데이터를 다루는 방법

---
체크섬은 Git에서 사용하는 가장 기본적인(Atomic) 데이터 단위이자 Git의 기본 철학이다.
Git 없이는 체크섬을 다룰 수 없어서 파일의 상태도 알 수 없고 심지어 데이터를 잃어버릴 수도 없다.

---
단순히 파일이 변경됐다는 사실이 아니라 어떤 내용이 변경됐는지 살펴보려면

---
Git에서는 기술용어로는 “Index” 라고 하지만, “Staging Area” 라는 용어를

---
--until

---
차이가 아니라 스냅샷

---
Git은 데이터를 추가할 뿐
          

---
단순히 파일의 마지막 스냅샷을 Checkout 하지 않는다. 그냥 저장소를 히스토리와 더불어 전부 복제한다.

---
일단 스냅샷을 커밋하고 나면 데이터를 잃어버리기 어렵다.

---
git diff --staged

---
무결성

---
git commit --amend

---
git log 주요 옵션

---
오프라인 상태이거나 VPN에 연결하지 못해도 막힘 없이 일 할 수 있다

---
파일이 달라지지 않았으면 Git은 성능을 위해서 파일을 새로 저장하지 않는다. 단지 이전 상태의 파일에 대한 링크만 저장

---
--staged 와 --cached 는 같은 옵션이다

---
Git 디렉토리는 Git이 프로젝트의 메타데이터와 객체 데이터베이스를 저장하는 곳

---
세 가지 상태
          

---
--since

---
거의 모든 명령을 로컬에서 실행

---
Git의 핵심

---
git rm --cached

---
하드디스크에 있는 파일은 그대로 두고 Git만 추적하지 않게 한다

---
Git의 핵심

---
되돌리거나 데이터를 삭제할 방법이 없다.

---
git diff

---
Git은 데이터를 스냅샷의 스트림처럼 취급

---
워킹 트리는 프로젝트의 특정 버전을 Checkout 한 것

---
git log --pretty=format

---
gitignore 파일에 입력하는 패턴은 아래 규칙을 따른다.





---
Git은 데이터를 저장하기 전에 항상 체크섬을 구하고 그 체크섬으로 데이터를 관리한다

---
git status -s

---
git rm

---
git mv 명령은