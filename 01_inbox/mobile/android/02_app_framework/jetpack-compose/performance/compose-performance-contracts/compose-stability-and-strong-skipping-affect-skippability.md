---
title: compose-stability-and-strong-skipping-affect-skippability
tags: [android, compose/performance, jetpack-compose]
aliases: [Compose stability, Strong skipping]
date modified: 2026-08-06 14:48:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Compose stability와 strong skipping은 호출의 skip 가능성을 바꾼다

Compose compiler는 Composable을 `restartable`·`skippable`로 분류하고 parameter의 stability를 추론한다. Kotlin 2.0.20부터 strong skipping이 기본 활성화되어 restartable Composable은 unstable parameter가 있어도 skippable이 될 수 있다.

strong skipping의 비교 메커니즘은 parameter 분류에 따라 다르다.

```text
stable parameter   -> equals()
unstable parameter -> instance equality (===)
모든 비교가 같음   -> 호출 skip 가능
```

따라서 새 `List` instance를 매 recomposition마다 만들면 unstable parameter는 여전히 달라진다.

```kotlin
@Immutable
data class ContactUi(val id: Long, val name: String)

@Composable
fun ContactRow(contact: ContactUi, onClick: (Long) -> Unit) {
    ListItem(
        headlineContent = { Text(contact.name) },
        modifier = Modifier.clickable { onClick(contact.id) },
    )
}
```

`@Immutable`은 모든 공개 속성이 불변이라는 개발자의 약속이다. 실제로 내부가 변하는 타입에 붙이면 compiler가 변화를 놓칠 수 있으므로 성능 표식처럼 사용하지 않는다. 표준 `List`, `Set`, `Map` 인터페이스는 compiler가 실제 불변성을 보장할 수 없어 unstable로 판단할 수 있다.

release build의 compiler report를 켜서 추론 결과를 확인한다.

```kotlin
composeCompiler {
    reportsDestination = layout.buildDirectory.dir("compose_compiler")
    metricsDestination = layout.buildDirectory.dir("compose_compiler")
}
```

관찰 증거는 `<module>-composables.txt`의 `restartable skippable`과 각 parameter의 stable/unstable 표시다. Layout Inspector의 skip/recomposition count와 benchmark도 함께 비교한다. 모든 Composable을 skippable로 만드는 것이 목표는 아니다. 실제 병목이 있는 호출만 모델 변경의 유지보수 비용과 교환한다.

관련 노트: [@Composable 컴파일 결과는 restart와 skip 제어를 가능하게 한다](../../runtime/compose-runtime-contracts/composable-compiler-output-enables-restart-and-skip-control.md), [Compose 성능 최적화는 측정·진단·개선 순환으로 진행한다](./compose-performance-starts-with-measure-debug-improve-loop.md)

출처: [Strong skipping mode](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping), [Compose stability 진단](https://developer.android.com/develop/ui/compose/performance/stability/diagnose)
