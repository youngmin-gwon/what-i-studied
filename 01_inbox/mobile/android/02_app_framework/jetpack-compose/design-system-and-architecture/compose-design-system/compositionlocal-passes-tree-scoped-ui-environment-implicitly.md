---
title: compositionlocal-passes-tree-scoped-ui-environment-implicitly
tags: [android, compose/design-system, jetpack-compose]
aliases: [CompositionLocal]
date modified: 2026-08-06 14:40:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## CompositionLocal은 트리 범위 UI 환경을 암묵적으로 전달한다

`CompositionLocal`은 Composition의 특정 하위 트리에 값을 제공한다. 소비자가 `LocalX.current`를 읽으면 가장 가까운 조상 `CompositionLocalProvider`의 값을 얻는다. 중간 Composable이 값을 전달할 필요는 없지만, 의존성이 함수 시그니처에서 보이지 않는 비용이 생긴다.

```kotlin
data class AppSpacing(val compact: Dp, val normal: Dp)

val LocalAppSpacing = staticCompositionLocalOf<AppSpacing> {
    error("AppSpacing이 제공되지 않았습니다")
}

@Composable
fun AppTheme(content: @Composable () -> Unit) {
    val spacing = AppSpacing(compact = 8.dp, normal = 16.dp)
    CompositionLocalProvider(LocalAppSpacing provides spacing, content = content)
}

@Composable
fun ProfileCard() {
    Card(Modifier.padding(LocalAppSpacing.current.normal)) { /* ... */ }
}
```

값 탐색과 무효화 메커니즘은 다음과 같다.

```text
provider A(8dp) -> child read = 8dp
                  -> provider B(12dp) -> grandchild read = 12dp
provider 값 변경 -> 그 Local을 관찰한 범위가 다시 실행됨
```

`compositionLocalOf`는 `current` 읽기를 추적해 값 변경 시 읽은 지점을 무효화한다. `staticCompositionLocalOf`는 읽기를 추적하지 않아 값이 바뀌면 provider의 `content` 전체가 다시 구성될 수 있으므로, 테마처럼 거의 바뀌지 않는 값에만 적합하다. 화면 상태나 필수 입력은 매개변수로 드러내는 편이 낫다.

검증할 때는 중첩 provider를 테스트에 구성하고 각 노드가 가장 가까운 값을 표시하는지 assert한다. Layout Inspector의 [recomposition](../../runtime/recomposition.md) count로 Local 변경 시 예상보다 넓은 범위가 실행되지 않는지도 확인한다.

관련 노트: [CompositionLocal, 파라미터, DI는 서로 다른 문제를 푼다](./compositionlocal-parameters-and-di-solve-different-problems.md), [Design system provider는 Material theme과 프로젝트 Local을 함께 제공한다](./design-system-provider-composes-material-theme-and-project-locals.md)

출처: [Locally scoped data with CompositionLocal](https://developer.android.com/develop/ui/compose/compositionlocal)
