---
title: "프로세스 종료 복구에는 saved state와 영속 source of truth가 필요하다"
tags: [android, android/architecture, android/app-components]
aliases: ["프로세스 종료 복구에는 saved state와 영속 source of truth가 필요하다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# 프로세스 종료 복구에는 saved state와 영속 source of truth가 필요하다

Android는 메모리 확보를 위해 background 프로세스를 종료할 수 있다. 이 경로는 Activity가 명시적으로 끝난 것과 다르며, 앱이 임의의 cleanup 콜백을 받을 것을 전제로 하면 안 된다.

복구 전략은 데이터 성격으로 나눈다. navigation argument, text field draft, selected tab처럼 작고 직렬화 가능한 상태는 saved state 계층에 둘 수 있다. 사용자 계정, cached domain data, 동기화 결과처럼 의미 있는 데이터는 repository와 storage가 source of truth여야 한다.

ViewModel은 configuration change에는 유용하지만 process death persistence가 아니다. ViewModel 안의 값은 재생성 이후 새로 만들어질 수 있으므로, 복구해야 하는 최소 정보는 `SavedStateHandle`이나 durable storage에 남겨야 한다.

관련 노트: [ViewModel 정본](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md), [SavedStateHandle 정본](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/savedstatehandle-restores-small-process-death-state.md), [persistence 정본](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md).

공식 문서: [Activity state changes](https://developer.android.com/guide/components/activities/state-changes)
