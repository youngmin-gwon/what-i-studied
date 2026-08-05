---
title: process-death-recovery-needs-saved-state-and-persistent-source-of-truth
tags: [android, android/app-components, android/architecture]
aliases: ["Process death 복구는 saved state와 persistent source of truth를 필요로 한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Process death 복구는 saved state와 persistent source of truth를 필요로 한다

**시스템 주도 프로세스 강제 종료(System-initiated Process Death)가 발생하면 메모리 내의 모든 ViewModel 및 전역 상태가 완전 파기된다. 프로세스 복구 시 이전 화면 UX 를 재구성하려면 소량의 UI 트랜지션 키(SavedStateHandle)와 대용량 도메인 데이터(Persistent Single Source of Truth / Room DB)의 이중 복구 체계가 필요하다.**

---

### 1. 복구 전략 대조 (What)

1. **`SavedStateHandle` (OS Binder Parcelable)**:
   현재 화면의 탭 인덱스, 텍스트 필드 미완성 입력값, 선택된 Item ID 등 소량(최대 몇십 KB)의 UI 키값을 복구하는 데 사용된다.
2. **Persistent Storage (Room DB / DataStore)**:
   전체 아이템 목록, 사용자 프로필, 결제 장바구니 등 대용량 상태를 Disk 기반으로 영속 저장하여 프로세스 재시작 시 조회 복구한다.

---

### 2. 관련 문서 및 참조

- 상위 문서: [App Component Contracts](./app-component-contracts.md)
- 관련 계약 문서:
  - [SavedStateHandle은 프로세스 데스의 소량 상태를 복구한다](../../state-management/viewmodel/savedstatehandle-restores-small-process-death-state.md)

검증일: 2026-08-05. Process Death 복구 이중화 체계 대조 완료.
