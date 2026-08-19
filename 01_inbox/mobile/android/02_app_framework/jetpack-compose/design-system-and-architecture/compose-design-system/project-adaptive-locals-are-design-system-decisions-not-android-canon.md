---
title: project-adaptive-locals-are-design-system-decisions-not-android-canon
tags: [android, compose/design-system, jetpack-compose]
aliases: [project adaptive locals, custom CompositionLocal]
date modified: 2026-08-06 14:40:00 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

## 프로젝트 Adaptive Local은 Android 표준이 아니라 앱의 설계 결정이다

프로젝트가 만든 `LocalAppLayoutMode` 같은 이름·분할·기본값은 Android나 Compose의 공통 API가 아니다. Jetpack이 제공하는 adaptive API에서 입력을 얻더라도, 이를 어떤 UI 정책으로 축약해 Local에 넣을지는 앱의 design-system 계약이다.

```kotlin
enum class AppLayoutMode { SinglePane, TwoPane }

val LocalAppLayoutMode = staticCompositionLocalOf<AppLayoutMode> {
    error("AppLayoutMode provider가 필요합니다")
}

@Composable
fun AdaptiveBoundary(
    windowIsWide: Boolean,
    content: @Composable () -> Unit,
) {
    val mode = if (windowIsWide) AppLayoutMode.TwoPane else AppLayoutMode.SinglePane
    CompositionLocalProvider(LocalAppLayoutMode provides mode, content = content)
}
```

문서에는 최소한 다음 선택 메커니즘을 기록한다.

```text
플랫폼/Jetpack 입력 -> 프로젝트 분기 규칙 -> Local 타입과 기본값
                    -> provider 위치 -> 실제 consumer
```

화면 하나만 쓰는 값은 매개변수가 더 명확하다. 여러 하위 컴포넌트가 같은 UI 환경으로 소비하고 중간 계층이 알 필요가 없을 때 Local을 고려한다. `LocalWindowSizeClass`, `LocalAdaptiveInfo`처럼 보이는 이름도 실제 의존성의 artifact·버전을 확인하고 프로젝트 정의와 혼동하지 않는다.

검증은 `SinglePane`과 `TwoPane` provider를 각각 주입한 UI test로 분기 결과를 assert하고, 창 크기 변경 시 Layout Inspector에서 예상 consumer만 다시 실행되는지 본다. 이 증거가 없으면 Local은 숨은 전역 상태가 되기 쉽다.

관련 노트: [Design system provider는 MaterialTheme과 프로젝트 Local을 구성한다](./design-system-provider-composes-material-theme-and-project-locals.md), [CompositionLocal은 트리 범위 UI 환경을 암묵적으로 전달한다](./compositionlocal-passes-tree-scoped-ui-environment-implicitly.md)

출처: [Locally scoped data with CompositionLocal](https://developer.android.com/develop/ui/compose/compositionlocal), [Build adaptive layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive)
