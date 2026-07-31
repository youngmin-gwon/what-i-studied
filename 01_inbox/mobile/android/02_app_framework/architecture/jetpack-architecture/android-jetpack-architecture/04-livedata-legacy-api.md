# LiveData (Legacy API)

상위 노트: [android-jetpack-architecture](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture.md)

>[!WARNING] **Devil's Advocate : LiveData 걷어내기**
>젯팩 컴포넌트 등장 초기를 주도한 기술이지만, 현재는 **Kotlin StateFlow**로 대체되어야 마땅한 구시대 유물입니다.
>비동기 처리나 스레드 전환 시 `Transformations` 지옥에 빠지기 쉬우며, 도메인 레이어로의 독립성을 해치는 주범입니다. (안드로이드 프레임워크 종속성)

생명주기를 인식하는 Observable 데이터 홀더. (View 시스템에서만 제한적 사용 권장)

```kotlin
// MutableLiveData 생성
private val _counter = MutableLiveData<Int>(0)
val counter: LiveData<Int> = _counter

// 값 업데이트
_counter.value = 1 // 메인 스레드
_counter.postValue(1) // 백그라운드 스레드

// 관찰
counter.observe(viewLifecycleOwner) { value ->
    textView.text = value.toString()
}

// Transformations
val doubledCounter: LiveData<Int> = Transformations.map(counter) { it * 2 }

val userLiveData: LiveData<User> = Transformations.switchMap(userIdLiveData) { id ->
    repository.getUserById(id)
}

// MediatorLiveData (여러 소스 결합)
val combined = MediatorLiveData<String>().apply {
    addSource(liveData1) { value = combineValues() }
    addSource(liveData2) { value = combineValues() }
}
```
