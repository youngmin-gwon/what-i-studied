---
title: livedata
tags: ["android", "android/app-framework", "android/lifecycle"]
aliases: ["LiveData는 lifecycle-aware 옵저버 패턴의 레거시 핫 스트림이다"]
date modified: 2026-08-10 15:22:00 +09:00
date created: 2026-08-10 15:22:00 +09:00
---

## LiveData는 lifecycle-aware 옵저버 패턴의 레거시 핫 스트림이다

### 정의 (What)
**LiveData**는 Android Framework 의존성(`androidx.lifecycle`)을 지닌 핫 스트림으로, 현재 상태값을 메모리에 보유하고 있으면서 옵저버 패턴(Observer Pattern)으로 변경사항을 구독자에게 통지한다. 수명주기(Lifecycle)를 감시하여 Active 상태 구독자에게만 이벤트를 전달하는 lifecycle-aware 특성을 가진다.

### 왜 필요한가 (Why)
1. **Lifecycle 자동 관리**: Activity나 Fragment의 `DESTROYED` 상태에서 자동으로 구독을 해제하여 메모리 누수를 방지한다.
2. **Active 상태 최적화**: `STARTED` 이상의 Active 상태에서만 관찰 대상으로 등록하여 불필요한 이벤트 전달을 차단한다.
3. **Configuration Change 복원**: Activity 회전 시 새로 생성된 UI는 `observe()` 호출 시점에 최신 `value`를 즉시 받아 동기적 상태 복원을 한다.

### 내부 메커니즘 (How)

#### 1. Lifecycle-aware 옵저버 패턴
```kotlin
// LiveData 생성 및 관찰
val userLiveData = MutableLiveData<User>()

// Activity에서 observe() 호출
userLiveData.observe(this) { user ->
    // this: LifecycleOwner (Activity/Fragment)
    // lifecycle.addObserver()를 내부적으로 등록
    updateUI(user)
}

// Activity가 destroy되면 자동으로 removeObserver() 호출
```

**내부 원리**:
- `observe(LifecycleOwner, Observer)`는 LifecycleOwner의 내부 Lifecycle을 감시한다.
- Lifecycle 상태가 `STARTED` 이상이면 LiveData 이벤트를 Observer에게 전달한다.
- Lifecycle 상태가 `STOPPED` 이하이면 이벤트를 버린다 (Stopped observer는 관찰하지 않음).
- Lifecycle이 `DESTROYED` 되면 Observer 자동 제거.

#### 2. 옵저버 등록 메커니즘
```kotlin
// 레거시 옵저버 방식
userLiveData.observe(lifecycleOwner, Observer { user ->
    // active state에서만 호출됨
    updateUI(user)
})

// 또는 MutableLiveData를 직접 조작
val mutableLiveData = MutableLiveData<String>()
mutableLiveData.value = "new value"      // 메인 스레드에서만 호출
mutableLiveData.postValue("new value")   // 백그라운드 스레드에서 호출
```

### 코드 예시

#### 기본 사용 패턴
```kotlin
// ViewModel에서 LiveData 정의
class UserViewModel : ViewModel() {
    private val _userLiveData = MutableLiveData<User>()
    val userLiveData: LiveData<User> = _userLiveData
    
    fun fetchUser(userId: String) {
        // 백그라운드 작업
        viewModelScope.launch {
            try {
                val user = userRepository.getUser(userId)
                _userLiveData.postValue(user)  // 메인 스레드에 post
            } catch (e: Exception) {
                _userLiveData.postValue(null)
            }
        }
    }
}

// Activity에서 관찰
class UserActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        val viewModel = ViewModelProvider(this).get(UserViewModel::class.java)
        
        // lifecycle owner가 this이므로 자동으로 lifecycle 연결
        viewModel.userLiveData.observe(this) { user ->
            if (user != null) {
                updateUI(user)
            }
        }
    }
}
```

#### 변환 및 조합 (Transformation)
```kotlin
class UserViewModel : ViewModel() {
    private val _userId = MutableLiveData<String>()
    
    // LiveData 변환
    val userName: LiveData<String> = Transformations.map(_userId) { userId ->
        // userId가 변경될 때마다 이 블록이 호출되고 결과만 전달
        userRepository.getUserName(userId)
    }
    
    // 여러 LiveData 조합
    val userWithPosts: LiveData<Pair<User, List<Post>>> = Transformations.switchMap(_userId) { userId ->
        // userId 변경될 때마다 새 LiveData를 반환하여 자동 전환
        userRepository.getUserWithPosts(userId)
    }
}
```

### 레거시 특성과 제약

| 특성 | 설명 |
|---|---|
| **Android Framework 의존** | `androidx.lifecycle` 라이브러리 필수 → 도메인 레이어에서 사용 불가 (테스트 시 Android SDK mock 필요) |
| **Null Safety 약함** | `liveData.value`가 nullable → null check 필수 |
| **메인 스레드 강제** | `setValue()`는 메인 스레드에서만 호출 가능, `postValue()`는 비동기 |
| **Configuration Change 시 값 재전달** | `observe()` 호출 시 최신 값을 즉시 전달 → 동기적 복원은 유리하나 중복 전달 가능성 |
| **no Conflation 제어** | 동일 값이 발행되어도 항상 observer에게 통지 |

### StateFlow와 비교

자세한 비교는 [StateFlow 대 LiveData 차이점](../../async-flow/flow-state/stateflow-vs-flow.md)을 참고하세요.

**핵심 차이**:
- **LiveData**: Android Framework 의존, Lifecycle-aware 자동 관리, 메인 스레드 강제
- **StateFlow**: Pure Kotlin, Multiplatform(KMP) 지원, 도메인 레이어 사용 가능, Conflation 내장

현대 Android 개발에서는 StateFlow 사용을 권장합니다.

### 관찰 가능한 증거 (Observable Evidence)

```bash
# Android Studio Logcat에서 LiveData 변경 추적
adb logcat | grep -i livedata

# ViewModel의 LiveData 생명주기 확인
adb shell dumpsys activity | grep -A5 -B5 ViewModel
```

### 공식 문서
- [LiveData Overview](https://developer.android.com/topic/libraries/architecture/livedata)
- [LifecycleOwner](https://developer.android.com/reference/androidx/lifecycle/LifecycleOwner)
