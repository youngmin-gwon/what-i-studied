---
title: 03-the-two-types-of-destruction
tags: []
aliases: []
date modified: 2026-07-31 16:28:46 +09:00
date created: 2026-07-31 16:26:40 +09:00
---

## 🔄 The Two Types of Destruction

Activity 가 파괴되는 시나리오는 두 가지입니다. 이 둘을 구분하는 것이 고수입니다.

### 1. Configuration Change (회전, 다크모드)

- **상황**: 화면을 소로로 돌렸을 때.
- **메커니즘**: Activity 인스턴스는 죽고(`onDestroy`), **즉시** 새로운 인스턴스가 `onCreate` 됩니다.
- **생존자**:
    - `ViewModel`: 메모리에 살아있음 (Activity 보다 오래 산다).
    - `savedInstanceState`: Bundle 에 저장됨.

### 2. Process Death (시스템에 의한 살해)

- **상황**: 앱을 백그라운드에 두고 딴짓(게임, 카메라)을 하다가 메모리가 부족해짐 -> **LMKD**가 앱 프로세스를 죽임.
- **메커니즘**: 프로세스 자체가 날아갑니다. `ViewModel` 도 메모리에 있으니 당연히 날아갑니다.
- **복구**: 사용자가 다시 앱을 열면, 시스템은 **죽기 직전의 상태(SavedState)**만 가지고 새로운 프로세스에서 Activity 를 `onCreate` 합니다.
- **생존자**:
    - `ViewModel`: **사망**. (초기화됨)
    - `savedInstanceState`: **생존**. (시스템 서버인 AMS 가 `Bundle` 을 들고 있다가 다시 찔러줌)

>[!IMPORTANT] **The Golden Rule**
>"ViewModel 과 SavedStateHandle 을 같이 써야 한다."
> - **ViewModel**: 회전 시 데이터 유지 (빠름, 메모리)
> - **SavedStateHandle**: 프로세스 킬 시 데이터 생존 (느림, 직렬화)

---
