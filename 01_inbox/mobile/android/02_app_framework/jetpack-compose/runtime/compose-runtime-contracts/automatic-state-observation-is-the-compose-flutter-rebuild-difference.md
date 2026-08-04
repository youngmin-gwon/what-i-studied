---
title: automatic-state-observation-is-the-compose-flutter-rebuild-difference
tags: [android, compose/runtime, jetpack-compose]
aliases: [A Compose State of Mind, Compose for Flutter developers]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## 자동 상태 관찰은 Compose 와 Flutter Rebuild 의 차이점이다

Flutter 개발자가 Compose 를 볼 때 가장 먼저 바꿔야 할 관점은 "Widget 객체를 다시 build 한다"가 아니라 "Composable 함수가 어떤 Snapshot State 를 읽었는지 Runtime 이 추적한다"는 점이다.

Flutter 의 `setState` 는 개발자가 dirty 범위를 선언하는 명령에 가깝고, Provider/Riverpod 은 어떤 Widget 이 어떤 provider 를 보는지 별도 라이브러리가 추적한다. Compose 는 observable state read 를 Runtime 모델의 중심에 둔다.

그래서 Compose 성능 판단은 "Composable 이 호출되면 나쁘다"가 아니라 "어디에서 state 를 읽었고, 어떤 parameter 가 skip 을 막고, 어떤 work 가 composition 에 들어갔는가"로 바뀐다. 이것이 `remember`, state hoisting, effect API 가 같은 mental model 위에 놓이는 이유다.

```kotlin
@Composable
fun Counter() {
    var count by remember { mutableStateOf(0) }
    Text("Count: $count")            // 이 scope가 count 읽기를 등록한다
    Button(onClick = { count++ }) { Text("+1") } // 람다 내부는 읽기가 아니라 쓰기다
}
```

`count` 를 증가시키면 `Text` 를 감싼 scope 만 invalidate 되고 `Button` 은 재실행되지 않는다. Android Studio Layout Inspector 의 recomposition count 열을 켜면 실제로 어떤 Composable 이 몇 번 재구성/skip 됐는지 숫자로 확인할 수 있다.

관련 노트: [Snapshot State 관찰은 State를 읽은 scope를 invalidation 대상으로 만든다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/snapshot-state-observation-invalidates-state-read-scopes.md), [Compose state owner는 읽고 쓰는 범위의 가장 낮은 공통 owner다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/compose-state-owner-is-the-lowest-common-owner-that-needs-read-or-write.md)

출처: [Thinking in Compose](https://developer.android.com/develop/ui/compose/mental-model), [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)
