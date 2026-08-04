---
title: rtl-mirroring-is-automatic-for-start-end-but-manual-for-icons
tags: ["android", "android/app-framework"]
aliases: ["RTL 미러링은 start/end 속성에서는 자동이고 아이콘에서는 수동이다"]
date modified: 2026-08-04 18:00:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## RTL 미러링은 start/end 속성에서는 자동이고 아이콘에서는 수동이다

아랍어, 히브리어 같은 RTL(right-to-left) 로케일에서는 레이아웃 전체가 좌우로 뒤집혀야 자연스럽다. Android 는 [리소스 Qualifier는 런타임 로케일에 따라 문자열을 선택한다](./resource-qualifiers-select-strings-by-runtime-locale.md) 에서 다룬 로케일 선택과 별개로, 레이아웃 방향을 로케일에 맞춰 자동으로 뒤집는 메커니즘을 갖고 있다. 다만 이 자동화는 속성 이름을 방향 중립적으로 쓸 때만 동작하고, 그림처럼 좌우 반전으로 의미가 바뀌는 요소는 자동화 대상에서 제외된다.

### 메커니즘: start/end가 자동 미러링되는 이유

`left`/`right` 는 절대 방향이라 로케일과 무관하게 항상 같은 쪽을 가리킨다. `start`/`end` 는 논리적 방향이라 LTR 에서는 `start=left, end=right` 로, RTL 에서는 `start=right, end=left` 로 해석이 바뀐다. 프레임워크가 레이아웃을 그릴 때 현재 `Configuration.layoutDirection` 을 참조해 `start`/`end` 를 실제 좌표로 변환하기 때문에, 코드/레이아웃은 그대로 두고 값 해석만 로케일에 따라 달라진다.

```xml
<!-- LTR에서만 정확하고 RTL에서는 뒤집히지 않는 예 -->
<TextView
    android:layout_marginLeft="16dp"
    android:gravity="left" />

<!-- 로케일에 따라 자동으로 미러링되는 예 -->
<TextView
    android:layout_marginStart="16dp"
    android:gravity="start" />
```

| LTR 전용 속성 | 자동 미러링 속성 |
|---|---|
| `android:paddingLeft`/`Right` | `android:paddingStart`/`End` |
| `android:layout_marginLeft`/`Right` | `android:layout_marginStart`/`End` |
| `android:gravity="left"`/`"right"` | `android:gravity="start"`/`"end"` |
| `android:drawableLeft`/`Right` | `android:drawableStart`/`End` |

매니페스트에서 `android:supportsRtl="true"` 를 선언해야(`targetSdkVersion` 17 이상 전제) 시스템이 이 미러링을 적용한다.

```xml
<application
    android:supportsRtl="true"
    ... />
```

`Activity` 계층 밖에서 만드는 뷰(다이얼로그, 커스텀 팝업 등)는 `layoutDirection` 을 명시적으로 맞춰줘야 하는 경우가 있다.

```kotlin
val config = context.resources.configuration
customView.layoutDirection = config.layoutDirection
```

### 수동 대응이 필요한 예외: 아이콘과 커스텀 드로잉

방향성이 있는 아이콘(뒤로가기 화살표, 재생/되감기, 챗 말풍선 꼬리)은 좌우가 뒤집혀야 의미가 유지되지만, 비트맵/벡터 자체는 프레임워크가 알아서 뒤집어 주지 않는다. API 19(`KITKAT`) 이상에서는 단순한 형태의 드로어블에 한해 `autoMirrored` 속성으로 자동 반전을 요청할 수 있다.

```xml
<!-- res/drawable/ic_back_arrow.xml -->
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:autoMirrored="true"
    android:viewportWidth="24"
    android:viewportHeight="24">
    <path android:fillColor="#000000" android:pathData="M20,11H7.83l5.59,-5.59L12,4l-8,8 8,8 1.41,-1.41L7.83,13H20v-2z"/>
</vector>
```

`autoMirrored="true"` 는 "단순한" 드로어블에만 유효하다 — 여러 레이어가 겹치거나 반전이 의미를 바꾸는 복합 아이콘(예: 국기, 방향성이 없는 로고)에는 적용하면 안 되고, 커스텀 `View.onDraw()` 안에서 `layoutDirection` 을 직접 확인해 그리는 방식으로 대응해야 한다.

```kotlin
override fun onDraw(canvas: Canvas) {
    val isRtl = layoutDirection == View.LAYOUT_DIRECTION_RTL
    // isRtl에 따라 canvas.scale(-1f, 1f) 등으로 직접 반전 처리
}
```

### 경계

- `autoMirrored` 는 API 19 미만에서는 무시되므로, 최소 API 를 19 미만으로 지원하는 앱은 `layout-ldrtl/` qualifier 디렉터리로 RTL 전용 리소스를 따로 둬야 한다.
- 텍스트 안에 삽입되는 숫자·주소처럼 방향이 혼재된 문자열(bidi text)은 레이아웃 미러링과 별개 문제이며 `BidiFormatter.unicodeWrap()` 으로 처리한다 — 이 노트의 범위(레이아웃 방향)를 벗어난다.

### 관찰 가능한 신호

- 개발자 옵션의 "Force RTL layout direction"(API 19+)을 켜면 시스템 언어를 바꾸지 않고도 RTL 미러링을 테스트할 수 있다.
- `start`/`end` 대신 `left`/`right` 를 쓴 뷰는 RTL 강제 모드에서도 위치가 그대로 남아 레이아웃이 깨진 것처럼 보인다 — 이 차이가 관찰 가능한 회귀 신호다.
- `autoMirrored` 를 빠뜨린 방향성 아이콘은 RTL 모드에서 여전히 LTR 방향을 가리켜, 뒤로가기 화살표가 반대쪽을 가리키는 형태로 눈에 띈다.

관련 노트: [리소스 Qualifier는 런타임 로케일에 따라 문자열을 선택한다](./resource-qualifiers-select-strings-by-runtime-locale.md)

공식 문서: [다양한 언어 지원](https://developer.android.com/training/basics/supporting-devices/languages)

검증일: 2026-08-04. `start`/`end` 자동 미러링 대상 속성 목록, `android:supportsRtl` 요구사항(`targetSdkVersion` 17+), `autoMirrored` 의 API 19+ 제약과 "단순 드로어블" 한정 조건을 공식 문서에서 확인했다.
