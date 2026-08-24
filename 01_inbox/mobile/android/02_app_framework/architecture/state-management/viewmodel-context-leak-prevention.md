---
title: viewmodel-context-leak-prevention
tags: [android, android/architecture, android/state-management, android/viewmodel]
aliases: ["ViewModel은 UI 컨트롤러와 Android Context를 장기 보관하지 않는다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## ViewModel 은 UI 컨트롤러와 Android Context 를 장기 보관하지 않는다

상위 문서: [Android ViewModel](./viewmodel.md)

### 핵심 주장

ViewModel 은 Activity, Fragment, View 같은 UI 객체를 필드로 보관하지 않는다.

일반적인 `Context` 도 장기 보관하지 않는다.

이 객체들은 화면 생명주기에 묶여 있으므로,

ViewModel 이 보관하면 이전 화면 인스턴스가 회수되지 않을 수 있다.

### 보관하지 않을 것

- `Activity`
- `Fragment`
- `View` 와 View binding
- 화면에 연결된 `Context`
- UI listener 와 adapter
- 다른 ViewModel

ViewModel 은 화면 객체 대신 값과 상태를 노출한다.

UI 가 필요한 동작은 상태 관찰 또는 일회성 이벤트 수집으로 표현한다.

```kotlin
class BadViewModel(private val activity: Activity) : ViewModel()

class GoodViewModel : ViewModel() {
    private val _message = MutableStateFlow<String?>(null)
    val message = _message.asStateFlow()

    fun showMessage() {
        _message.value = "저장되었습니다"
    }
}
```

화면이 메시지를 수집한 뒤 자신의 `Context` 로 Toast 를 표시한다.

ViewModel 은 Toast 를 생성하거나 navigation 을 직접 수행하지 않는다.

### Context 가 필요한 경우

리소스 접근이나 시스템 서비스가 필요하면 책임을 다른 계층으로 이동한다.

Repository 나 전용 객체가 필요한 의존성을 받도록 한다.

앱 전체에 안전한 `Application` Context 가 꼭 필요한 경우에는

`AndroidViewModel` 을 사용할 수 있지만, 기본 선택은 아니다.

그 경우에도 Activity Context 와 View 는 전달하지 않는다.

```kotlin
class SettingsViewModel(
    private val settings: SettingsRepository
) : ViewModel()
```

이 규칙은 메모리 누수 방지와 단위 테스트 가능성을 함께 지킨다.
