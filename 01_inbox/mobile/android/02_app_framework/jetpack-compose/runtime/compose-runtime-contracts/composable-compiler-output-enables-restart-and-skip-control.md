---
title: composable-compiler-output-enables-restart-and-skip-control
tags: [android, compose/runtime, jetpack-compose]
aliases: [Compose compiler, restartable, skippable]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Composable compiler 출력은 재시작과 skip 제어를 가능하게 한다

### 1. 개념 정의 (What)
`@Composable` 어노테이션은 단순한 구문 표시(Marker)가 아니라, **Compose Compiler 플러그인이 코틀린 AST(Abstract Syntax Tree)를 정밀 변환하여 바이트코드 레벨에서 런타임 추적 파라미터(`$composer`, `$changed`) 및 재시작/건너뛰기(Restartable & Skippable) 조작 구문을 주입하는 컴파일 타임 툴링 메커니즘**이다.

---

### 2. 컴파일러 바이트코드 변환의 필요성 (Why)
코틀린 언어 규약 자체에는 런타임에 함수의 실행을 중간에 멈추거나, 특정 가비지 콜렉션을 건너뛰거나, 파라미터 상태를 자동 트래킹하는 비동기 UI 제어 기능이 없다.

Compose Compiler 플러그인은 개발자가 작성한 깔끔한 순수 코틀린 코드 위에, 런타임 엔진이 Recomposition 최적화를 수행할 수 있도록 바이트코드를 자동으로 변환·확장하는 역할을 수행한다.

---

### 3. 내부 동작 및 변환 메커니즘 (How)

```
[개발자 소스 코드]
@Composable
fun Header(title: String) {
    Text(text = title)
}

         |  Compose Compiler IR Transformation
         v

[컴파일러 변환 바이트코드 (개념적 코드)]
fun Header(title: String, $composer: Composer?, $changed: Int) {
    $composer.startRestartGroup(12345) // Restart Scope 생성
    
    // Skip 가능성 판단 ($changed 비트마스크 & 파라미터 안정성 검사)
    if ($changed and 0b0001 == 0 && $composer.skipping) {
        $composer.skipToGroupEnd() // 🚀 함수 본문 스킵!
    } else {
        Text(text = title, $composer, ...)
    }
    
    $composer.endRestartGroup()?.updateScope { nextComposer ->
        Header(title, nextComposer, $changed or 0b0001) // Recomposition 재실행 람다
    }
}
```

1. **Synthetic 파라미터 주입**: 모든 `@Composable` 함수에 런타임 제어 객체인 `$composer` 및 변경 트래킹 비트마스크인 `$changed` 파라미터가 자동으로 추가된다.
2. **Restart Group 형성**: 비-inline 함수 본문 앞뒤에 `startRestartGroup()`과 `endRestartGroup()`이 삽입되어 무효화 시 재실행할 수 있는 `RecomposeScope`를 생성한다. (`restartable`)
3. **Skip 가능성 판단 (`skippable`)**: 
   - 함수의 모든 입력 파라미터 타입이 **안정적(Stable)**이거나 `Strong Skipping Mode`(Kotlin 2.0.20+ 기본 활성화) 조건에 부합하면, `$composer.changed(param)` 비교를 통해 이전 값과 동일한 경우 본문 실행을 통째로 스킵한다.

---

### 4. Compiler Metrics 리포트 모니터링

Gradle 설정에 Compose Compiler 리포트 옵션을 활성화하면 빌드 시 컴파일러 분석 결과를 검증할 수 있다:

```kotlin
// build.gradle.kts (Kotlin 2.0.0+)
composeCompiler {
    reportsDestination = layout.buildDirectory.dir("compose_compiler")
    metricsDestination = layout.buildDirectory.dir("compose_compiler")
}
```

생성된 `<module>-composables.txt` 결과 예시:
```text
// ✅ skippable 및 restartable 모두 적용됨
restartable skippable scheme("[[String]]") fun UserCard(
  stable name: String
)

// ❌ unstable 파라미터(List)로 인해 skippable 이 탈락함 (Strong Skipping 미적용 시)
restartable scheme("[[List<User>]]") fun UserList(
  unstable users: List<User>
)
```

- 파라미터가 `unstable`로 판정될 경우, 파라미터에 `@Immutable` / `@Stable` 어노테이션을 부여하거나 `kotlinx.collections.immutable`을 사용하여 `skippable` 최적화를 회복할 수 있다.

---

관련 노트: [Compose 안정성과 strong skipping은 skippability에 영향을 준다](../../performance/compose-performance-contracts/compose-stability-and-strong-skipping-affect-skippability.md), [Composition은 호출 위치 identity로 remember 값을 보존한다](./composition-uses-callsite-identity-to-preserve-remembered-values.md)

출처: [Strong skipping mode](https://developer.android.com/develop/ui/compose/performance/stability/strongskipping), [Jetpack Compose Compiler Architecture](https://github.com/androidx/androidx/tree/androidx-main/compose/compiler)

검증일: 2026-08-05. Compose Compiler IR 변환 단계 및 Strong Skipping Mode 사양을 대조하여 `$composer`, `$changed` 주입, restartable/skippable 판정 및 Compiler Metrics 검증 서술을 정밀 보강했다.
