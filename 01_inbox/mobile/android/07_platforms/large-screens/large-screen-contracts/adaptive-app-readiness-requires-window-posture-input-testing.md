---
title: adaptive-app-readiness-requires-window-posture-input-testing
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-07-31 18:06:11 +09:00
---

## 적응형 앱 준비도는 창, posture, 입력 테스트로 판단한다

상위 문서: [큰 화면 적응 계약](./large-screen-contracts.md)

큰 화면 대응 완료 여부는 특정 태블릿에서 화면이 넓게 보이는지로 판단하지 않는다. compact, medium, expanded, large, extra-large 창 크기와 폴더블 posture, multi-window, 입력 장치 조합에서 핵심 과업이 유지되는지로 판단한다.

### Adaptive Quality Tier 및 매커니즘

| Tier | Level Name | Core Requirements |
| :--- | :--- | :--- |
| **Tier 3** | **Ready** | Letterboxing 방지, 기본 Multi-Window 지원, Resize 시 Activity Crash 없음, 기본 키보드 포커스 탐색 가능 |
| **Tier 2** | **Optimized** | Window Size Class에 따른 Canonical Layout (List-Detail 등) 적용, Foldable Posture 대응, Drag & Drop 수신 |
| **Tier 1** | **Differentiated** | Multi-Instance 지원, Stylus 하드웨어 압력/인앱 손바닥 거부(Palm Rejection), Spatial UI/데스크톱 윈도잉 생산성 극대화 |

### 창 크기 변경 자동화 테스트 메커니즘 (ActivityScenarioRule)

```kotlin
@Test
fun testLayoutResizingContract() {
    val scenario = ActivityScenario.launch(MainActivity::class.java)
    
    // 1. Compact Width (360dp) 검증
    scenario.onActivity { activity ->
        val bounds = activity.windowManager.currentWindowMetrics.bounds
        assertThat(bounds.width()).isLessThan(600)
    }
    
    // 2. Expanded Width 시뮬레이션
    scenario.onActivity { activity ->
        activity.requestedOrientation = ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE
    }
    onView(withId(R.id.detail_pane)).check(matches(isDisplayed()))
}
```

### 체크 기준

- portrait, landscape, split screen, freeform resize 에서 정보 손실과 overlap 이 없어야 한다.
- activity recreation 또는 window size 변화 후에도 화면 상태가 복원되어야 한다.
- fold/unfold, tabletop, book posture 에서 주요 콘텐츠와 조작부가 hinge 또는 접힘 영역을 피해야 한다.
- keyboard navigation, pointer hover/right-click/scroll, stylus 입력을 실제 기기 또는 emulator 로 검증한다.
- 현재 Adaptive app quality 의 Tier 3 ready, Tier 2 optimized, Tier 1 differentiated 체크리스트를 출시 전 기준으로 사용한다.
- breakpoint 바로 전후와 compact height 를 포함해 레이아웃 전환 경계를 테스트한다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 1. 다양한 윈도우 크기 분할 시뮬레이션 (ADB)
adb shell am stack split-screen 1 2

# 2. 시스템 UI 크기 및 밀도 동적 스크립팅 테스트
adb shell wm size 1200x1920
adb shell wm size 800x1280
adb shell wm size reset

# 3. Activity configuration 변경 덤프 관측
adb shell dumpsys activity top | grep -E "config|overrideConfig"
```

### 관련 문서

- [데스크톱 윈도잉 준비도는 작은 화면 호환성이 아니라 생산성 검증이다](../windowing-multitasking-contracts/desktop-windowing-readiness-is-productivity-validation.md)

공식 문서: [Adaptive app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality), [Get started with large screens](https://developer.android.com/guide/topics/large-screens)

검증일: 2026-08-03. 기존 large screen quality 지침은 Adaptive app quality 로 대체되었으므로 archive 가 아니라 현재 tier 와 compatibility tests 를 기준으로 한다.

