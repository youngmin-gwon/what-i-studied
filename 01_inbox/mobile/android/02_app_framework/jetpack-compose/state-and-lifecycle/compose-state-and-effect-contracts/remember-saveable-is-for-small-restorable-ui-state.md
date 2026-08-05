---
title: remember-saveable-is-for-small-restorable-ui-state
tags: ["android", "android/app-framework"]
aliases: [rememberSaveable, Restorable UI State]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 16:53:16 +09:00
---

## Composable 수명보다 오래 필요한 작은 복원 상태에만 rememberSaveable 을 사용한다

### 1. 개념 정의 (What)
`rememberSaveable`은 일반 `remember`와 달리 **화면 회전(Activity Recreation) 및 안드로이드 OS에 의한 프로세스 강제 종료(System-initiated Process Death) 시에도 상태 값을 Android `Bundle` 인스턴스에 저장하여 복원하는 API**다.

---

### 2. rememberSaveable과 경량 상태 규약의 필요성 (Why)
일반 `remember`는 RAM 메모리의 Slot Table에만 보존되므로 Activity가 재생성되면 파괴된다. 

반면 `rememberSaveable`은 Binder IPC 통신을 통해 OS의 `SavedStateRegistry`로 상태를 전달한다. 따라서:
- **Bundle 바인딩 한계**: Android 시스템 Binder 버퍼는 앱 전체 합산 약 **1MB 미만의 크기 제약**을 가진다.
- **TransactionTooLargeException 위험**: 이미지 라이브러리 객체, 대용량 리스트 전체, 비트맵 데이터를 `rememberSaveable`에 넣으면 앱이 크래시된다.

따라서 `rememberSaveable`은 텍스트 필드 입력값, 선택된 탭 인덱스, 폼 스크롤 위치 등 **복원 가능한 작은 용량의 UI 상태(Small Restorable State)**로 사용 범위가 엄격히 제한되어야 한다.

---

### 3. Saver 구현 메커니즘 (How)

```
[Default Bundle Type: Primitive, String, Parcelable]
  ---> 자동 Bundle 마샬링 처리
  
[Custom Class / Non-Parcelable Object]
  |--> Saver(save = { ... }, restore = { ... }) 인터페이스 제공 필요
  |--> listSaver / mapSaver 유틸리티 사용
```

1. **Saver 인스턴스**: 기본 프리미티브 타입(Int, String 등)과 `Parcelable`, `Serializable`은 자동 보존된다.
2. **커스텀 데이터 타입 Saver 등록**: 복잡한 커스텀 객체는 `Saver` 인터페이스를 직접 구현하거나 `listSaver`, `mapSaver`를 사용하여 마샬링 및 언마샬링 로직을 전달해야 한다.

---

### 4. Custom Saver 구현 및 올바른 활용 예제

```kotlin
data class UserDraftInput(val title: String, val content: String)

// ✅ Custom Saver 정의: 데이터 클래스를 Saver 레벨로 변환
val UserDraftSaver: Saver<UserDraftInput, Any> = listSaver(
    save = { listOf(it.title, it.content) },
    restore = { UserDraftInput(title = it[0] as String, content = it[1] as String) }
)

@Composable
fun ArticleDraftScreen() {
    // ✅ Custom Saver 를 적용하여 rememberSaveable 로 복원
    var draftInput by rememberSaveable(saver = UserDraftSaver) {
        mutableStateOf(UserDraftInput(title = "", content = ""))
    }

    Column {
        TextField(
            value = draftInput.title,
            onValueChange = { draftInput = draftInput.copy(title = it) },
            label = { Text("Title") }
        )
        TextField(
            value = draftInput.content,
            onValueChange = { draftInput = draftInput.copy(content = it) },
            label = { Text("Content") }
        )
    }
}
```

---

상위 문서: [Compose 상태와 Effect 계약](./compose-state-and-effect-contracts.md)

관련 노트: [remember는 일반 cache가 아니라 Composition에 귀속된 저장공간이다](../../runtime/compose-runtime-contracts/remember-is-composition-scoped-storage-not-general-cache.md), [Compose 상태 API는 필요한 수명에 맞춰 선택한다](./compose-state-api-selection-by-lifetime.md)

출처: [Save UI state in Compose](https://developer.android.com/develop/ui/compose/state-saving)

검증일: 2026-08-05. Compose 공식 SavedState 가이드를 대조하여 Bundle IPC 1MB 용량 한계, TransactionTooLargeException 방지 및 Custom Saver 구현 서술을 정밀 보강했다.
