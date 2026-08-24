---
title: 10-foot-ui-focus-navigation
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-08-03 17:27:04 +09:00
---

## 10-foot UI 는 포커스 기반 탐색을 요구한다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](../android-platforms-and-form-factors.md)

관련 지도: [Android TV 계약](./tv.md)

### 핵심 정의

"10-foot UI"는 시청자가 약 3 미터(10 피트) 거리에서 TV 화면을 보는 상황을 가정한 디자인 기준이다. 이 거리에서는 휴대폰 화면 대비 훨씬 큰 텍스트, 넓은 여백, 명확한 포커스 표시가 필요하며, 콘텐츠 탐색은 그리드/행(row) 기반 카드 목록을 방향키로 이동하는 패턴이 표준이다.

### 메커니즘 및 Compose for TV 구현

Jetpack 의 Leanback 라이브러리(View 기반) 및 Compose for TV (`androidx.tv.material3`) 컴포넌트는 `TvLazyRow`, `TvLazyColumn`, `Card` 컴포저블로 카테고리별 가로 스크롤 행을 구성하며, 포커스 진입 시 1.1배 확대 및 테두리 강조 효과를 자동 제공한다.

```kotlin
@Composable
fun TvCatalogRow(
    categoryTitle: String,
    items: List<MovieItem>
) {
    Column(modifier = Modifier.padding(vertical = 16.dp)) {
        Text(
            text = categoryTitle,
            style = MaterialTheme.typography.headlineMedium,
            modifier = Modifier.padding(start = 32.dp, bottom = 12.dp)
        )
        
        TvLazyRow(
            contentPadding = PaddingValues(horizontal = 32.dp),
            horizontalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            items(items) { item ->
                Card(
                    onClick = { onMovieSelect(item) },
                    modifier = Modifier.size(width = 200.dp, height = 120.dp)
                ) {
                    MovieCardContent(item)
                }
            }
        }
    }
}
```

### 판단 기준

- 텍스트 크기와 히트 영역을 휴대폰 기준 dp 값을 그대로 재사용하지 않는다. TV 는 시청 거리가 멀기 때문에 최소 텍스트 크기와 카드 크기 기준이 다르다.
- 콘텐츠 카탈로그형 앱은 처음부터 행 기반 브라우즈 패턴(Leanback 스타일)을 채택하는 것이 커스텀 그리드를 처음부터 설계하는 것보다 d-pad 탐색 일관성을 얻기 쉽다.
- 포커스 확대/강조 애니메이션이 없으면 사용자가 현재 선택된 항목을 인지하기 어렵다. 시각적 포커스 표시를 생략하지 않는다.

### 경계

- 이 노트는 레이아웃과 탐색 패턴을 다룬다. d-pad 입력 자체의 전달 메커니즘은 [Android TV는 d-pad/리모컨을 1차 입력으로 가정한다](android-tv-dpad-input.md) 가 다룬다.
- 큰 화면 적응형 레이아웃(태블릿/폴더블)의 window size class 모델은 `07_platforms/large-screens` 가 다루며, TV 의 10-foot 기준과는 별개의 문제다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 1. 10-foot UI 포커스 노드 스택 및 현재 포커스 카드 좌표 확인
adb shell dumpsys activity top | grep -i "Focus"

# 2. TV UI 계층 렌더링 프레임 덤프
adb shell dumpsys window windows | grep -E "mFocusedApp|mCurrentFocus"
```

### 공식 문서

- https://developer.android.com/training/tv/start/layouts
- https://developer.android.com/training/tv/playback/browse

