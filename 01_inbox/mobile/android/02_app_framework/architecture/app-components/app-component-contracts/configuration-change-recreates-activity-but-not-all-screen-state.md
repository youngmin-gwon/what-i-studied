---
title: configuration-change-recreates-activity-but-not-all-screen-state
tags: [android, android/app-components, android/architecture]
aliases: ["Configuration change는 Activity를 재생성하지만 모든 화면 상태를 잃지 않는다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Configuration change는 Activity를 재생성하지만 모든 화면 상태를 잃지 않는다

화면 회전, 언어 변경, 다크 모드 전환 등 **구성 변경(Configuration Change)이 발생하면 안드로이드 OS 는 현재 Activity 인스턴스를 파기(`onDestroy`)하고 새 디스플레이 리소스가 적용된 새 Activity 인스턴스를 즉시 재설계(`onCreate`)한다.** 이 과정에서 화면 상태가 유실되지 않도록 **`ViewModel` 및 `rememberSaveable` 메커니즘**이 구동된다.

---

### 1. 개념 및 핵심 구조 (What)

- **Activity 파기 및 재생성**:
  기존 Activity 인스턴스는 즉시 Destroy 되므로 인메모리 Activity 멤버 변수는 모두 초기화된다.
- **ViewModel 수명 보존 메커니즘**:
  `ViewModelStoreOwner` 인 `ComponentActivity` 가 파기되더라도 OS 는 internal `ViewModelStore` 참조를 새 Activity 인스턴스로 그대로 이관하여 ViewModel 내부의 `StateFlow` 상태가 완벽히 보존되도록 보장한다.

---

### 2. 관련 문서 및 참조

- 상위 문서: [App Component Contracts](./app-component-contracts.md)
- 관련 계약 문서:
  - [ViewModel 수명과 프로세스 데스 계약](../../state-management/viewmodel/viewmodel-survives-configuration-change-not-process-death.md)
- 공식 문서: [Handle configuration changes](https://developer.android.com/guide/topics/resources/runtime-changes)

검증일: 2026-08-05. Configuration Change 재생성 동작 대조 완료.
