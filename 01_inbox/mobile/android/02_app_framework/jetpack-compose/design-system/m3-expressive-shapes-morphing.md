---
title: m3-expressive-shapes-morphing
tags: [android, compose/design-system, material3, m3-expressive, shape-morphing]
aliases: ["Material 3 Expressive shape 스케일과 상호작용 shape 변형"]
date modified: 2026-08-06 14:42:00 +09:00
date created: 2026-08-05 15:10:00 +09:00
---

## Material 3 Expressive의 shape 변형은 지원하는 컴포넌트 API에서 설정한다

Material 3의 `Shapes`는 theme 수준의 corner scale을 제공한다. 상호작용에 따른 shape 변형은 모든 컴포넌트의 암묵적 규칙이 아니다. 예를 들어 최신 expressive `Button` overload는 `ButtonShapes`를 받아 기본/pressed shape 사이를 전환하며, 두 값이 `CornerBasedShape`이면 morphing한다.

```kotlin
@OptIn(ExperimentalMaterial3ExpressiveApi::class)
@Composable
fun MorphingSaveButton(onClick: () -> Unit) {
    Button(
        onClick = onClick,
        shapes = ButtonDefaults.shapes(
            shape = MaterialTheme.shapes.extraLarge,
            pressedShape = MaterialTheme.shapes.medium,
        ),
        modifier = Modifier.testTag("save"),
    ) {
        Text("저장")
    }
}
```

상태 전이 메커니즘은 단순하다.

```text
idle -- press --> pressedShape
pressed -- release/cancel --> shape
CornerBasedShape 쌍: 모서리를 보간
그 밖의 Shape 포함: 상태에 맞는 Shape로 전환
```

corner 값을 12dp, 전환 시간을 100ms처럼 앱 문서에서 Material의 보편 규격으로 고정하지 않는다. 기본값은 사용하는 Material3 artifact의 `ButtonDefaults.shapes()`가 정본이다. 브랜드가 shape를 덮어쓰면 press·focus·disabled 상태와 clipping 비용까지 앱 계약으로 소유한다.

관찰 증거는 idle/press 상태 screenshot과 touch sequence다. 실제 touch down 후 release/cancel에서 원래 shape로 돌아오는지 보고, UI test는 `performTouchInput { down(center) }` 상태에서 이미지를 캡처하고 `up()` 뒤 다시 비교할 수 있다. 접근성 의미와 클릭 동작은 shape 변화와 독립적으로 유지되어야 한다.

이 overload와 opt-in 표시는 Material3 버전에 따라 달라질 수 있다. 도입 전 프로젝트의 API reference와 컴파일 결과를 확인하고, 미지원 버전에서는 단일 `shape` parameter를 사용한다.

관련 노트: [Material 3 Expressive 디자인 시스템 및 컴포넌트 아키텍처](m3-expressive-architecture.md), [Material 3 Expressive 컴포넌트 크기와 토큰 선택](m3-expressive-sizing-tokens.md)

출처: [Material 3 Button API](https://developer.android.com/reference/kotlin/androidx/compose/material3/Button.composable), [Material 3 Shapes](https://developer.android.com/reference/kotlin/androidx/compose/material3/Shapes)
