---
title: branching-strategies
tags: [branching, collaboration, distributed, git, workflow]
aliases: [Git Flow, Git 브랜치 전략, GitHub Flow, 분산 워크플로우, 브랜치 모델]
date modified: 2025-12-18 15:21:57 +09:00
date created: 2025-12-18 14:10:00 +09:00
---

## Git 브랜치 전략: 팀의 생산성을 결정하는 설계도

브랜치 전략은 팀이 코드를 어떻게 관리하고 배포할지에 대한 **약속**입니다. 단순한 기능 개발을 넘어, 대규모 오픈소스 프로젝트나 대기업의 복잡한 릴리스 프로세스를 지탱하는 핵심 설계도이기도 합니다.

---

### 🏢 실무 사례 (Selection Guide)

- **Early-stage Startup**: 빠른 배포가 생명입니다. 복잡한 Git Flow 대신 **GitHub Flow**나 **Trunk-based Development**를 통해 하루에도 수십 번 배포하는 구조를 지향합니다.
- **Enterprise / FinTech**: 안정성이 최우선입니다. 엄격한 코드 리뷰와 QA 단계를 보장하는 **Git Flow**를 사용하여 정기 배포 주기를 관리합니다.
- **Open Source Project**: 불특정 다수의 기여가 발생하므로 **Fork & Pull Request** (Integration-Manager) 모델을 기본으로 사용합니다.

---

## 🏗️ 분산 환경의 워크플로우 모델 (Distributed Workflows)

Pro Git 에서는 서비스 규모와 참여 방식에 따른 세 가지 주요 분산 워크플로우를 소개합니다.

### 1. 집중형 워크플로우 (Centralized Workflow)

전통적인 SVN 과 유사한 방식입니다. 중앙 저장소 하나를 두고 모든 개발자가 같은 `main` 브랜치에 푸시합니다.

- **장점**: 단순하고 직관적입니다.
- **단점**: 팀원이 늘어날수록 충돌이 잦아지고 배포 안정성이 떨어집니다.

### 2. 통합 관리자 워크플로우 (Integration-Manager Workflow) ⭐

현재 대부분의 오픈소스 프로젝트와 GitHub PR 방식이 채택하는 모델입니다.

- 각 개발자는 자신만의 공개 저장소(Fork)를 가집니다.
- 작업을 마친 후 '통합 관리자'에게 Pull Request 를 보냅니다.
- 관리자는 코드를 검토한 후 '공식 저장소(Canonical Repository)'에 반영합니다.

### 3. 주임무 관리자와 부임무 관리자 워크플로우 (Dictator and Lieutenants)

수천 명의 개발자가 참여하는 **Linux 커널** 같은 초대형 프로젝트에서 사용합니다.

- '리더(Lieutenants)'들이 각 분야의 코드를 1 차 통합합니다.
- 최종적으로 '주임무 관리자(Dictator, 예: 리누스 토발즈)'가 리더들의 코드를 병합합니다.

---

## 🏗️ 주요 브랜치 모델 분석

### 1. Git Flow (전통적 강자)

5 가지 종류의 브랜치를 사용하는 가장 엄격하고 체계적인 모델입니다.

- **Main**: 배포된 프로덕션 코드. 태그로 버전 관리.
- **Develop**: 다음 출시를 위한 메인 개발 라인.
- **Feature**: 기능 개발용 단기 브랜치.
- **Release**: 배포 전 최종 버그 수정 및 문서화.
- **Hotfix**: 프로덕션 긴급 수정용.

### 2. GitHub Flow (단순함의 미학)

`main` 브랜치 하나와 `feature` 브랜치만 사용하는 단순한 구조입니다.

- **원칙**: `main` 은 항상 배포 가능해야 하며, 병합 즉시 배포합니다.

### 3. Trunk-based Development (초고속 개발)

모든 개발자가 하나의 `trunk`(main) 브랜치에 직접 커밋하거나, 수명이 아주 짧은(하루 이내) 브랜치를 사용합니다. **Feature Flag** 기술이 필수적으로 동반됩니다.

---

## 🛠️ 프로젝트 유지보수와 패치 워크플로우 (Maintenance)

대규모 프로젝트나 이메일 기반의 협업(예: Linux 커널) 환경에서는 브랜치 직접 병합 외에 패치(Patch)를 주고받는 방식을 사용합니다.

### 1. 패치 생성 및 적용
- **패치 생성 (`git format-patch`)**: 특정 커밋들을 이메일에 첨부하기 좋은 형식의 텍스트 파일로 만듭니다.
- **패치 적용 (`git am`)**: 이메일 등으로 받은 패치 파일을 읽어 작성자 정보와 커밋 메시지를 유지하면서 내 히스토리에 반영합니다.

### 2. 프로젝트 관리자의 검토 흐름
- **Sign-off**: `git commit -s` 옵션을 사용해 이 코드를 검토하고 승인했음을 기록합니다.
- **선형 히스토리 유지**: 병합 시 `merge --no-ff` 를 쓸지, `rebase` 후 깔끔하게 합칠지를 프로젝트 성격에 맞춰 결정합니다.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **Long-lived Feature Branches** ❌
   - 브랜치를 너무 오래 유지하면 나중에 `main` 과 합칠 때 엄청난 충돌(Merge Hell)을 겪게 됩니다. 작업 단위는 최소화하고 자주 합치세요.
2. **Main 브랜치에 직접 Push** ❌
   - 코드 리뷰 없이 코드가 반영되어 배포 사고로 이어질 위험이 큽니다. 반드시 보호 브랜치(Protected Branch) 설정을 통해 PR 을 강제하세요.
3. **병합 후 브랜치 삭제 누락**
   - 사용이 끝난 로컬/원격 브랜치를 방치하면 관리 피로도가 높아집니다. `git fetch --prune` 등을 통해 주기적으로 정리하세요.

---

### 📚 연결 문서

- [[00_fundamentals/basic-concepts|Git 기본 개념]] - 브랜치 포인터와 Three Trees 이해
- [[02_advanced/reset-demystified|Reset 완벽 분석]] - 브랜치 이동과 데이터 흐름
- [[01_strategies/commit-messages|커밋 메시지]] - 브랜치 작업의 기록 방식
- [[02_advanced/advanced-workflows|고급 워크플로우]] - Rebase vs Merge 선택 기준
