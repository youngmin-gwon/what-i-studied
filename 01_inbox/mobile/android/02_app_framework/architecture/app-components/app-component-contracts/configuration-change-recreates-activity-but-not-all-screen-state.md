---
title: "설정 변경은 Activity를 재생성할 수 있으므로 상태를 화면 인스턴스에서 분리해야 한다"
tags: [android, android/architecture, android/app-components]
aliases: ["설정 변경은 Activity를 재생성할 수 있으므로 상태를 화면 인스턴스에서 분리해야 한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# 설정 변경은 Activity를 재생성할 수 있으므로 상태를 화면 인스턴스에서 분리해야 한다

회전, 언어, 다크 모드, window size 변경 같은 configuration change는 Activity를 파괴하고 새 인스턴스를 만들 수 있다. 이때 Activity 필드나 View/Composable local 변수에만 있던 값은 사라질 수 있다.

모든 상태를 같은 곳에 두면 안 된다. screen/business state는 ViewModel이 적합하고, 작은 transient UI state는 `rememberSaveable`이나 saved instance state가 적합하며, 사용자 데이터나 서버 동기화 결과는 storage/data layer가 source of truth여야 한다.

configuration change는 process death와 다르다. 같은 프로세스에서 Activity만 재생성되는 경우 ViewModel은 살아남을 수 있지만, 프로세스가 사라지면 ViewModel 자체는 복구되지 않는다.

관련 노트: [ViewModel 정본](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md), [프로세스 종료 복구](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/process-death-recovery-needs-saved-state-and-persistent-source-of-truth.md), [persistence 정본](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md).

공식 문서: [Activity state changes](https://developer.android.com/guide/components/activities/state-changes)
