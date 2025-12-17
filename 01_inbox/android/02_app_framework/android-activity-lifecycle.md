---
title: android-activity-lifecycle
tags: [android, activity, lifecycle, process-death, viewmodel]
aliases: [Activity Lifecycle, Process Death, SavedStateHandle]
date modified: 2025-12-18 06:10:00 +09:00
date created: 2025-12-16 16:19:14 +09:00
---

# Activity Lifecycle: Beyond onCreate

`onCreate` -> `onStart` -> `onResume`. 누구나 아는 순서입니다.
하지만 **"프로세스 킬(Process Death)"**과 **"구성 변경(Configuration Change)"**의 차이를 모르면 앱은 사용자를 당황하게 만듭니다.

## 💡 Why it matters (Context)

-   **Data Loss**: 사용자가 긴 글을 쓰다가 홈 화면으로 나갔습니다. 유튜브 좀 보다가 돌아왔는데 글이 다 날아갔다면? 이는 **Process Death** 처리를 안 했기 때문입니다.
-   **Wrong Architecture**: `ViewModel`은 회전에는 살아남지만, 프로세스 킬에서는 죽습니다. 이를 모르면 "ViewModel이 만능이다"라고 착각하게 됩니다.
-   **Memory Leaks**: `Context`를 `static` 변수나 싱글톤에 잘못 저장하면 Activity가 영원히 메모리에서 해제되지 않습니다.

---

## 🔄 The Two Types of Destruction

Activity가 파괴되는 시나리오는 두 가지입니다. 이 둘을 구분하는 것이 고수입니다.

### 1. Configuration Change (회전, 다크모드)
-   **상황**: 화면을 소로로 돌렸을 때.
-   **메커니즘**: Activity 인스턴스는 죽고(`onDestroy`), **즉시** 새로운 인스턴스가 `onCreate` 됩니다.
-   **생존자**:
    -   `ViewModel`: 메모리에 살아있음 (Activity보다 오래 산다).
    -   `savedInstanceState`: Bundle에 저장됨.

### 2. Process Death (시스템에 의한 살해)
-   **상황**: 앱을 백그라운드에 두고 딴짓(게임, 카메라)을 하다가 메모리가 부족해짐 -> **LMKD**가 앱 프로세스를 죽임.
-   **메커니즘**: 프로세스 자체가 날아갑니다. `ViewModel`도 메모리에 있으니 당연히 날아갑니다.
-   **복구**: 사용자가 다시 앱을 열면, 시스템은 **죽기 직전의 상태(SavedState)**만 가지고 새로운 프로세스에서 Activity를 `onCreate` 합니다.
-   **생존자**:
    -   `ViewModel`: **사망**. (초기화됨)
    -   `savedInstanceState`: **생존**. (시스템 서버인 AMS가 `Bundle`을 들고 있다가 다시 찔러줌)

> [!IMPORTANT] **The Golden Rule**
> "ViewModel과 SavedStateHandle을 같이 써야 한다."
> - **ViewModel**: 회전 시 데이터 유지 (빠름, 메모리)
> - **SavedStateHandle**: 프로세스 킬 시 데이터 생존 (느림, 직렬화)

---

## 🛠️ ViewModel Internals

"ViewModel은 어떻게 Activity가 죽어도 살아있을까?"

1.  **HolderFragment (Old)**: 예전에는 투명한 Fragment(`setRetainInstance(true)`)를 붙여서 유지했습니다.
2.  **ActivityClientRecord (Modern)**:
    -   `Activity`가 구성 변경으로 파괴될 때, `ActivityThread`가 `NonConfigurationInstances`라는 객체를 따로 챙겨둡니다.
    -   여기에 ViewModelStore가 들어있습니다.
    -   새 Activity가 만들어질 때 `attach()` 과정에서 이 객체를 다시 넘겨받습니다.

---

## 🧟‍♂️ Handling Process Death

### 1. SavedStateHandle (권장)
ViewModel 내부에서 `SavedStateHandle`을 쓰면, 보일러플레이트 코드 없이 프로세스 킬에 대비할 수 있습니다.

```kotlin
class MyViewModel(private val state: SavedStateHandle) : ViewModel() {
    // 값이 바뀌면 자동으로 Bundle에 저장됨
    val searchQuery = state.getLiveData("query", "")
    
    fun setQuery(query: String) {
        state["query"] = query
    }
}
```

### 2. onSaveInstanceState (Old School)
단순한 View 상태(스크롤 위치, EditText 내용)는 View 시스템이 알아서 저장해 주지만, 커스텀 변수는 직접 저장해야 합니다.

```kotlin
override fun onSaveInstanceState(outState: Bundle) {
    super.onSaveInstanceState(outState)
    outState.putInt("score", currentScore) // 1MB 제한 주의!
}
```

---

## 🚦 Lifecycle States vs Callbacks

콜백 메서드보다 **상태(State)**를 보는 것이 더 명확합니다.

-   **CREATED**: `onCreate` ~ `onDestroy`
-   **STARTED**: `onStart` ~ `onStop` (Visible)
-   **RESUMED**: `onResume` ~ `onPause` (Interactive)

### 3. Launch Modes & Tasks
Activity가 스택(Task)에 쌓이는 방식입니다.
-   **SingleTop**: "알림 눌렀을 때 이미 켜져 있으면 그거 재사용해줘" (`onNewIntent`)
-   **SingleTask**: "이 앱의 메인 화면은 딱 하나만 있어야 해" (카카오톡 채팅방 -> 메인)

### 📚 연결 문서
- [[android-architecture-stack]] - LMKD가 프로세스를 죽이는 이유
- [[android-process-and-memory]] - 프로세스 수명주기
- [[android-app-components-deep-dive]] - (Legacy) 컴포넌트 기초
