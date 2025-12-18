---
title: git-internals
tags: [architecture, git, internals, maintenance, objects, packfiles, refspec]
aliases: [GC, Git 내부 구조, Git 데이터 모델, Git 원리, Git 인턴십, Prune]
date modified: 2025-12-18 16:08:01 +09:00
date created: 2025-12-18 14:00:00 +09:00
---

## Git Internals: 데이터로 보는 Git 의 본질

Git 은 단순한 버전 관리 도구가 아니라, **"콘텐츠 주소지정 파일 시스템 (Content-Addressable File System)"** 위에 구현된 버전 관리 도구입니다.

---

### 💡 Why it matters (Context)
- **무결성 보장**: 파일 내용이 1 비트만 바뀌어도 해시값이 달라집니다.
- **효율적인 저장**: 동일한 내용의 파일은 물리적으로 단 하나만 저장합니다.
- **불변성 (Immutability)**: 한번 저장된 오브젝트는 바뀌지 않습니다.

---

## 🏗️ Git Object 모델 (Master Level)

Git 은 모든 데이터를 `.git/objects` 디렉토리에 SHA-1 해시를 이름으로 하는 파일로 저장합니다.

- **Blob**: 파일 내용 저장.
- **Tree**: 디렉토리 구조 저장. (파일명, 모드 매핑)
- **Commit**: 스냅샷 정보. (작성자, 부모 커밋, 메시지)
- **Tag**: 특정 커밋 포인터.

---

## 📦 저장 최적화: Packfiles

Git 은 처음에는 각 파일을 개별적인 'Loose Object'로 저장하지만, 효율을 위해 이를 'Packfile'로 묶어 관리합니다.

- **델타 압축**: 비슷한 파일 간의 차이점만 저장하여 용량을 획기적으로 줄입니다.
- **최신성 우선**: 최신 버전을 그대로 저장하고 옛날 버전을 델타로 관리하여 성능을 높입니다.

---

## 🔗 원격 통신: The Refspec

원격 저장소와 데이터를 주고받을 때(`fetch`, `push`) 사용하는 매핑 규칙입니다.

- `+refs/heads/*:refs/remotes/origin/*`

---

## 🛰️ 데이터 전송 프로토콜: Smart vs. Dumb

- **Smart Protocol**: 서버와 클라이언트가 필요한 데이터만 지능적으로 협상하여 전송. (SSH, HTTP)
- **Dumb Protocol**: 서버 로직 없이 정적 파일을 직접 요청하는 비효율적 방식. (레거시)

---

## 🧹 내부 관리 및 유지보수: GC & Prune ⭐

Git 은 데이터베이스의 건강을 위해 주기적으로 '청소' 작업을 수행합니다.

### 1. Git GC (Garbage Collection)

수많은 Loose Object 를 Packfile 로 묶고, 불필요한 객체들을 정리합니다.

- `git gc`: 자동으로 실행되기도 하지만, 레포지토리가 너무 무거워지면 수동으로 실행합니다.
- 최근 사용하지 않는(댕글링) 객체들을 임시 보관소로 옮기거나 삭제 준비를 합니다.

### 2. Git Prune

어떤 브랜치나 태그에서도 참조되지 않는 '미아(Dangling)' 객체들을 실제로 삭제합니다.

- `git prune`: 참조되지 않는 모든 객체를 영구 제거합니다.
- **주의**: `reflog` 에 기록이 남아있는 객체는 삭제되지 않습니다. 진짜 삭제하려면 `reflog expire` 와 병행해야 합니다.

---

## 🛠️ 실전 트레이닝: 수동 커밋 만들기

`git hash-object`, `git update-index`, `git write-tree`, `git commit-tree` 순서로 내부 동작을 재현할 수 있습니다.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **대용량 바이너리 파일 커밋** ❌
2. **`.git` 폴더 수동 조작** ❌
3. **복구 중 `gc` 실행** ⚠️
   - 데이터 복구 작업 중에 `gc` 나 `prune` 을 실행하면, 실수로 지운 커밋 객체가 영구적으로 삭제되어 영영 되살릴 수 없게 됩니다.

---

### 📚 연결 문서

- [트러블슈팅](../02_advanced/troubleshooting.md) - `fsck` 로 댕글링 오브젝트 찾기
- [Reset 완벽 분석](../02_advanced/reset-demystified.md) - 영역별 데이터 이동
- [보안 및 스테이징](../03_tools/git-security-and-staging.md) - 서명된 객체의 내부 구조
