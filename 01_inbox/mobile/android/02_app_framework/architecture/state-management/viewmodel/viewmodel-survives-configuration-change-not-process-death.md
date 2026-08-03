---
title: ViewModel은 설정 변경 동안 유지되지만 프로세스 사망 복원은 보장하지 않는다
tags: [android, android/architecture, android/state-management, android/viewmodel]
aliases: ["ViewModel은 설정 변경 동안 유지되지만 프로세스 사망 복원은 보장하지 않는다"]
date modified: 2026-08-03 16:35:35 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# ViewModel은 설정 변경 동안 유지되지만 프로세스 사망 복원은 보장하지 않는다

상위 문서: [Android ViewModel](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/viewmodel.md)

### 핵심 주장

화면 회전이나 창 크기 변경처럼 같은 화면이 재생성되는 동안

ViewModel 은 기존 `ViewModelStore` 에 남아 상태를 유지한다.

그러나 시스템이 앱 프로세스를 종료하면 ViewModel 인스턴스도 사라진다.

따라서 ViewModel 자체를 영구 저장소나 복원 메커니즘으로 사용하지 않는다.

### 생명주기

```text
화면 생성 -> ViewModel 생성
설정 변경 -> 화면 재생성, ViewModel 재사용
화면 종료 -> ViewModel 제거, onCleared 호출
프로세스 사망 -> 인스턴스와 메모리 상태 소실
```

`finish()` 로 화면이 완전히 종료되거나,

Fragment 가 해당 소유자에서 제거되면 ViewModel 은 정리 대상이 된다.

그때 `onCleared()` 가 호출되고 `viewModelScope` 도 취소된다.

```kotlin
class UserViewModel : ViewModel() {
    override fun onCleared() {
        // 자체 리소스가 있을 때만 정리한다.
        super.onCleared()
    }
}
```

### 저장 전략

설정 변경만 견디면 되는 화면 상태는 ViewModel 에 둔다.

프로세스 사망 뒤에도 복원해야 하는 작은 값은 `SavedStateHandle` 에 둔다.

대량 데이터나 장기 데이터는 Repository 와 영속 저장소가 담당한다.

ViewModel 에 저장된 목록이 회전 후 남는다고 해서,

앱을 백그라운드에 오래 둔 뒤에도 남는다고 가정하지 않는다.

복원 요구사항을 상태 종류별로 분리하면 저장 비용과 책임이 명확해진다.

### 확인 질문

- 회전 직후에도 다시 계산할 필요가 없는 값인가?
- 프로세스가 새로 시작해도 반드시 되살려야 하는 값인가?
- 값이 커서 Bundle 기반 저장에 부담을 주지 않는가?

첫 번째 질문만 참이면 ViewModel 상태로 충분하다.

두 번째 질문까지 참이면 [SavedStateHandle](01_inbox/mobile/android/02_app_framework/architecture/state-management/viewmodel/savedstatehandle-restores-small-process-death-state.md) 을 검토한다.

세 번째 질문이 참이면 영속 저장소에 원본을 두고 복원 키만 저장한다.

테스트에서는 설정 변경 시 같은 ViewModel 인스턴스가 유지되는지와,

프로세스 복원에 필요한 값이 별도 저장 경로를 사용하는지를 분리해 검증한다.
