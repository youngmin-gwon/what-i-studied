---
title: android-activity-lifecycle
tags: []
aliases: []
date modified: 2026-04-05 17:42:54 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [[mobile-security]] > [[android-activity-lifecycle]]

### Activity Lifecycle: Process Mastery

안드로이드 `Activity` 의 생성부터 소멸까지의 복잡한 생명주기(Lifecycle) 변화와 **프로세스 킬(Process Death)** 대응 메커니즘을 심층 분석합니다.

단순히 콜백 함수를 호출하는 것을 넘어, 시스템 리소스가 부족할 때 OS 가 어떻게 프로세스를 관리하고, 사용자가 앱으로 돌아왔을 때 상태를 어떻게 복구하는지 이해하는 것이 목표입니다.

---

#### 💡 Context: 생명주기 관리의 실제

현대적인 안드로이드 앱 개발에서는 단일 액티비티 구조(Single-Activity Architecture)가 표준입니다. 콜백 메서드의 순서를 아는 것보다, 구성 변경(Configuration Change)과 프로세스 데스의 차이를 명확히 구분하고 데이터 손실을 방지하는 것이 훨씬 중요합니다.

---

>[!CAUTION] **Devil's Advocate : 다중 Activity 시대의 종말**
>안드로이드 초창기에는 화면마다 `Activity` 를 하나씩 만들어 매니페스트에 등록하는 것이 국룰이었습니다. 하지만, 현재는 **Single-Activity Architecture (단일 액티비티 구조)**가 완전한 표준입니다.
>화면 전환은 Activity 간 `Intent` 통신이 아니라, 하나의 `MainActivity` 위에서 `Compose Navigation` (또는 Fragment) 교체를 통해 이루어집니다. 복잡한 다중 Activity 구조는 명백한 레거시 패턴입니다.

#### 💡 Why it matters (Context)

- **Data Loss**: 사용자가 긴 글을 쓰다가 홈 화면으로 나갔습니다. 유튜브 좀 보다가 돌아왔는데 글이 다 날아갔다면? 이는 **Process Death** 처리를 안 했기 때문입니다.
- **Wrong Architecture**: `ViewModel` 은 회전에는 살아남지만, 프로세스 킬에서는 죽습니다. 이를 모르면 "ViewModel 이 만능이다"라고 착각하게 됩니다.
- **Memory Leaks**: `Context` 를 `static` 변수나 싱글톤에 잘못 저장하면 Activity 가 영원히 메모리에서 해제되지 않습니다.

---

#### 🔄 The Two Types of Destruction

Activity 가 파괴되는 시나리오는 두 가지입니다. 이 둘을 구분하는 것이 고수입니다.

##### 1. Configuration Change (회전, 다크모드)
- **상황**: 화면을 소로로 돌렸을 때.
- **메커니즘**: Activity 인스턴스는 죽고(`onDestroy`), **즉시** 새로운 인스턴스가 `onCreate` 됩니다.
- **생존자**:
    - `ViewModel`: 메모리에 살아있음 (Activity 보다 오래 산다).
    - `savedInstanceState`: Bundle 에 저장됨.

##### 2. Process Death (시스템에 의한 살해)
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

#### 🛠️ ViewModel Internals

"ViewModel 은 어떻게 Activity 가 죽어도 살아있을까?"

1. **HolderFragment (Old)**: 예전에는 투명한 Fragment(`setRetainInstance(true)`)를 붙여서 유지했습니다.
2. **ActivityClientRecord (Modern)**:
    - `Activity` 가 구성 변경으로 파괴될 때, `ActivityThread` 가 `NonConfigurationInstances` 라는 객체를 따로 챙겨둡니다.
    - 여기에 ViewModelStore 가 들어있습니다.
    - 새 Activity 가 만들어질 때 `attach()` 과정에서 이 객체를 다시 넘겨받습니다.

---

#### 🧟‍♂️ Handling Process Death

##### 1. SavedStateHandle (권장)

ViewModel 내부에서 `SavedStateHandle` 을 쓰면, 보일러플레이트 코드 없이 프로세스 킬에 대비할 수 있습니다.

```kotlin
class MyViewModel(private val state: SavedStateHandle) : ViewModel() {
    // 값이 바뀌면 자동으로 Bundle에 저장됨
    val searchQuery = state.getLiveData("query", "")
    
    fun setQuery(query: String) {
        state["query"] = query
    }
}
```

##### 2. onSaveInstanceState (Old School)

단순한 View 상태(스크롤 위치, EditText 내용)는 View 시스템이 알아서 저장해 주지만, 커스텀 변수는 직접 저장해야 합니다.

```kotlin
override fun onSaveInstanceState(outState: Bundle) {
    super.onSaveInstanceState(outState)
    outState.putInt("score", currentScore) // 1MB 제한 주의!
}
```

---

#### 🚦 Lifecycle States vs Callbacks

콜백 메서드보다 **상태(State)**를 보는 것이 더 명확합니다.

- **CREATED**: `onCreate` ~ `onDestroy`
- **STARTED**: `onStart` ~ `onStop` (Visible)
- **RESUMED**: `onResume` ~ `onPause` (Interactive)

##### 3. Launch Modes & Tasks

Activity 가 스택(Task)에 쌓이는 방식입니다.

- **SingleTop**: "알림 눌렀을 때 이미 켜져 있으면 그거 재사용해줘" (`onNewIntent`)
- **SingleTask**: "이 앱의 메인 화면은 딱 하나만 있어야 해" (카카오톡 채팅방 -> 메인)

#### See Also

- [[android-architecture-stack]] - LMKD 가 프로세스를 죽이는 이유
- [[android-process-and-memory]] - 프로세스 수명주기
- [[android-app-components-deep-dive]] - (Legacy) 컴포넌트 기초
