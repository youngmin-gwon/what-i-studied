---
title: "Activity 콜백은 화면 인스턴스의 visibility와 interaction 경계를 알린다"
tags: [android, android/architecture, android/app-components]
aliases: ["Activity 콜백은 화면 인스턴스의 visibility와 interaction 경계를 알린다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Activity 콜백은 화면 인스턴스의 visibility와 interaction 경계를 알린다

Activity lifecycle 콜백은 화면 인스턴스가 생성, 표시, 포커스 획득, 포커스 상실, 정지, 파괴되는 경계를 알려준다. `onCreate`, `onStart`, `onResume`, `onPause`, `onStop`, `onDestroy`는 UI 리소스 연결과 해제를 배치하는 기준이다.

이 콜백을 선형 스크립트처럼 믿으면 안 된다. 사용자 이동, multi-window, configuration change, process reclaim, finish 여부에 따라 경로가 달라진다. 특히 `onDestroy`는 영속 저장이나 서버 반영을 보장하는 마지막 기회가 아니다.

원칙은 콜백을 짧게 유지하고 lifecycle에 묶인 리소스만 다루는 것이다. 화면 상태는 ViewModel과 saved state로, 영속 데이터는 repository/storage로, 지연 가능한 작업은 background work로 보낸다.

관련 노트: [설정 변경과 상태 분리](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/configuration-change-recreates-activity-but-not-all-screen-state.md), [프로세스 종료 복구](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/process-death-recovery-needs-saved-state-and-persistent-source-of-truth.md), [background work 정본](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md).

공식 문서: [Activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle)
