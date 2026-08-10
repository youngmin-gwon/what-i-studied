---
title: git-bundle
tags: [advanced, bundle, git, offline, transfer]
aliases: [Git Bundle, 오프라인 전송, 저장소 이동]
date modified: 2026-08-10
date created: 2026-08-10
---

## Git Bundle: 네트워크 없이 저장소를 파일로 전달하기

`git bundle` 은 저장소의 전체 히스토리를 하나의 바이너리 파일로 압축하여, 네트워크 연결 없이 전달할 수 있습니다. 인트라넷 환경, USB 드라이브 전송, 격리된 환경(에어갭)에서 매우 유용합니다.

### 💡 Why it matters (Context)

- **오프라인 환경**: 네트워크가 없거나 느린 환경에서 전체 저장소를 한 번에 전달.
- **빠른 마이그레이션**: 매우 큰 저장소를 효율적으로 이동.
- **보안**: Git 서버를 거치지 않고 직접 전달 (내부 저장소 마이그레이션 등).

---

## 🏗️ Git Bundle 기본 사용법

### 저장소 전체 번들화

```bash
git bundle create repo.bundle HEAD
# 현재 HEAD까지의 전체 히스토리를 repo.bundle로 생성
```

### 특정 브랜치만 번들화

```bash
git bundle create feature.bundle feature-branch
git bundle create release.bundle main develop

# 여러 브랜치
git bundle create backup.bundle --all
```

### 번들 파일 확인

```bash
# 번들에 포함된 커밋 확인
git bundle list-heads repo.bundle

# 번들의 상세 정보
git bundle verify repo.bundle
```

### 번들에서 저장소 복원

```bash
# 방법 1: 새 저장소 생성
git clone repo.bundle -b main new-repo

# 방법 2: 기존 저장소에 merge
cd existing-repo
git fetch ../repo.bundle HEAD:temporary-branch
git merge temporary-branch
```

---

## 🏢 실무 사례 (Expert Techniques)

### 케이스 1: 격리된 개발 환경으로 저장소 전송

```bash
# 메인 개발 환경
git bundle create project-v1.bundle --all

# USB 드라이브에 복사
cp project-v1.bundle /Volumes/USB/

# 격리된 환경에서
git clone /Volumes/USB/project-v1.bundle my-project
cd my-project
# (네트워크 없이도 전체 히스토리 접근 가능)
```

### 케이스 2: 증분 번들로 효율성 증가

```bash
# 초기 번들 생성 (전체)
git bundle create v1.0.bundle v1.0

# 한 달 뒤, v1.0 이후 변경사항만 번들화
git bundle create updates-since-v1.0.bundle v1.0..HEAD

# 받는 쪽
git fetch updates-since-v1.0.bundle HEAD:main
```

### 케이스 3: 저장소 마이그레이션 (서버 간)

```bash
# 출발 서버
git bundle create mirror.bundle --all

# USB 또는 임시 서버에 전송
scp mirror.bundle staging-server:/tmp/

# 도착 서버에서
git clone --mirror /tmp/mirror.bundle new-repo.git
```

---

## 📊 번들 파일 크기 최적화

### 압축된 번들

```bash
# 번들을 압축하여 크기 줄이기
git bundle create repo.bundle.gz --all
gzip repo.bundle

# 또는 직접 압축
git bundle create repo.bundle --all
gzip repo.bundle  # repo.bundle.gz (원본보다 70% 작음)

# 복원
gunzip repo.bundle.gz
git clone repo.bundle
```

### 특정 커밋부터의 변화만 번들화

```bash
# v1.0.0 태그 이후 모든 변경만 포함
git bundle create updates.bundle v1.0.0..HEAD

# 파일 크기 비교
ls -lh v1.0.0.bundle    # 전체: 500MB
ls -lh updates.bundle   # 업데이트만: 50MB
```

---

## 🚨 흔한 실수 (Common Mistakes)

1. **번들 파일의 손상 확인 누락** ❌
   ```bash
   # 잘못된 방법
   git clone repo.bundle my-repo  # 손상되었어도 모를 수 있음

   # 올바른 방법
   git bundle verify repo.bundle  # 먼저 검증
   # OK - contains 123 commits and 5 branches
   git clone repo.bundle my-repo
   ```

2. **증분 번들의 의존성 무시** ❌
   ```bash
   # 순서 문제
   git bundle create updates.bundle v1.0..HEAD
   # 받는 쪽에서
   git fetch updates.bundle  # ❌ v1.0을 먼저 받아야 함

   # 올바른 순서
   git fetch /path/to/v1.0.bundle
   git fetch updates.bundle
   ```

3. **번들과 원격 저장소 혼동** ❌
   ```bash
   # 번들은 원격 저장소가 아님
   git clone repo.bundle
   cd repo
   git push  # ❌ 오류 발생 (번들은 읽기 전용)

   # 대신 원래 저장소로 push
   git push origin main
   ```

---

## 🔧 고급: 선택적 번들화

### 특정 태그 범위만 번들화

```bash
# v1.0부터 v2.0까지의 커밋만
git bundle create v1-to-v2.bundle v1.0..v2.0
```

### 여러 브랜치와 태그 함께

```bash
git bundle create full.bundle \
  --all \
  --tags

# 또는 특정 브랜치만
git bundle create selective.bundle \
  main develop feature/special-feature \
  v1.0 v2.0 v3.0
```

### 번들 검증 및 복구

```bash
# 손상된 번들 확인
git bundle verify repo.bundle

# 만약 손상되었다면 다시 생성
git bundle create repo-new.bundle --all
```

---

## 💡 Bundle vs Clone 비교

| 특징 | Bundle | Clone |
|:---|:---|:---|
| **전송 방식** | 파일 단위 | 네트워크 프로토콜 |
| **오프라인 지원** | 가능 | 불가능 |
| **증분 업데이트** | 가능 (태그 기반) | 가능 (Pull) |
| **파일 크기** | 중간 (압축 가능) | 작음 (네트워크 최적화) |
| **복원 속도** | 매우 빠름 | 네트워크 의존 |

---

### 📚 연결 문서

- [Git 인턴십](../00_fundamentals/git-internals.md) - 저장소 구조와 객체
- [명령어 비교](command-comparisons.md) - Pull vs Bundle
- [트러블슈팅](troubleshooting.md) - 번들 손상 복구
