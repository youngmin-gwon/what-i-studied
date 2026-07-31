# Jetpack Compose 접근성 가이드라인 (Accessibility: a11y)

이 문서는 Android 앱을 모든 사용자(시각, 청각, 운동 능력 또는 인지 장애가 있는 사용자 포함)가 장벽 없이 사용할 수 있도록 Jetpack Compose에서 제공하는 **접근성(Accessibility, 줄여서 a11y)** 관련 핵심 API와 모범 설계 패턴을 설명합니다.

본 문서는 Google의 [Accessibility in Jetpack Compose Codelab](https://developer.android.com/codelabs/jetpack-compose-accessibility)의 핵심 실무 학습 단계를 바탕으로 구성되었습니다.

---

## 1. 접근성을 챙겨야 하는 이유

Android 기기에는 다양한 접근성 서비스(스크린 리더인 **TalkBack**, 스위치 제어 등)가 탑재되어 있습니다. 선언형 UI인 Compose는 내부적으로 **Semantics(의미론적 트리)** 를 생성하여 이러한 접근성 서비스에 UI의 구조와 의미를 전달합니다.
* **Semantics**: 화면에 어떻게 그려지는지(Layout)가 아니라, **그 요소가 무엇을 의미하고 어떤 동작을 수행할 수 있는지**를 기술하는 메타데이터입니다.
* **개발자의 역할**: Compose가 자동으로 만들어내는 Semantics 트리를 보완하여 스크린 리더 등이 화면을 자연스럽고 풍부하게 소리 내어 읽을 수 있도록 만들어야 합니다.

---

## 2. 접근성 향상을 위한 7대 핵심 실무 가이드

### 2-1. 터치 대상 크기 확보 (Touch Target Sizes)
* **요구사항**: 터치하거나 클릭할 수 있는 모든 UI 요소는 최소 **48dp x 48dp** 이상의 크기를 가져야 합니다.
* **Compose 최적화**: Material Design 컴포저블(Button, IconButton, Switch 등)은 내부적으로 최소 터치 크기 요건을 자동으로 충족하도록 설계되어 있습니다. 하지만 작은 텍스트 버튼이나 커스텀 클릭 컴포저블을 직접 구현할 때는 누락되기 쉽습니다.

```kotlin
// ❌ 안 좋은 예: 아이콘 크기가 24dp여서 손의 미세 제어가 어려운 사용자는 터치하기 힘듦
Icon(
    imageVector = Icons.Default.Share,
    contentDescription = "공유",
    modifier = Modifier.clickable { onShare() }
)

//  올바른 예: IconButton 또는 minimumTouchTargetSize 확보
IconButton(onClick = onShare) {
    Icon(
        imageVector = Icons.Default.Share,
        contentDescription = "공유"
    )
}
```

---

### 2-2. 대체 텍스트 제공 (Content Descriptions)
* **원칙**: 화면의 텍스트가 아닌 시각적 요소(Image, Icon)는 스크린 리더가 읽을 수 있도록 설명 텍스트를 제공해야 합니다.
* **장식용 이미지 처리**: 레이아웃 장식용이거나 화면의 텍스트 정보와 완벽히 중복되는 이미지에는 `contentDescription = null`을 명시하여 TalkBack이 해당 요소를 건너뛰고 포커스를 잡지 않도록 유도해야 합니다.

```kotlin
// Case 1: 의미를 가진 이미지 - 상세한 묘사 제공
Image(
    painter = painterResource(R.drawable.post_image),
    contentDescription = "VirtualMate 운동 가이드 화면 캡처 이미지"
)

// Case 2: 단순 데코레이션/장식용 이미지 - null 설정 (TalkBack 포커스 스킵)
Image(
    painter = painterResource(R.drawable.ic_decorator_star),
    contentDescription = null
)
```

---

### 2-3. 의미론적 병합 (Merging Semantics)
* **문제점**: 뉴스 리스트의 카드 항목처럼 여러 요소(제목, 날짜, 작가 이름)가 모여 있는 경우, TalkBack은 이를 개별적으로 포커스하여 하나씩 읽어줍니다. 이는 사용자에게 매우 피로감을 줍니다.
* **해결책**: 관련성 높은 하위 노드들을 하나의 카드 스코프로 묶고, 하위 노드들의 Semantics를 하나로 병합(`mergeDescendants = true`)합니다.

```kotlin
//  올바른 예: Row 전체를 하나의 접근성 블록으로 묶어 한 번에 읽도록 설정
Row(
    modifier = Modifier
        .fillMaxWidth()
        .clickable { onPostClick() }
        .semantics(mergeDescendants = true) { // 자식 노드들의 텍스트/정보를 병합
            // 필요한 경우 추가적인 접근성 속성 설정
        }
) {
    Image(
        painter = painterResource(R.drawable.thumbnail),
        contentDescription = null // 전체 카드 맥락에서 읽으므로 개별 이미지는 스킵
    )
    Column {
        Text("오늘의 런닝 루틴")
        Text("시간: 30분 | 난이도: 중")
    }
}
```
* **결과**: TalkBack은 카드를 선택 시 한꺼번에 "오늘의 런닝 루틴. 시간: 30분, 난이도: 중. 두 번 탭하면 활성화됩니다."로 한 번에 읽습니다.

---

### 2-4. 커스텀 클릭 레이블 지정 (Custom Click Labels)
* **원칙**: 일반적인 `Modifier.clickable`을 지정하면 TalkBack은 끝에 자동으로 "두 번 탭하면 활성화됩니다(Double tap to activate)"라는 안내 멘트를 붙입니다.
* **개선**: 이 버튼이 구체적으로 어떤 동작을 하는지 클릭 레이블(`onClickLabel`)을 커스텀하여 전달하면 훨씬 명확해집니다.

```kotlin
//  올바른 예: 클릭 시 작동하는 의미를 레이블로 구체화
Row(
    modifier = Modifier
        .clickable(
            onClickLabel = "글 상세 보기", // TalkBack은 "두 번 탭하면 글 상세 보기을(를) 실행합니다" 등으로 안내
            onClick = onPostClick
        )
) {
    Text("상세 정보 읽기")
}
```

---

### 2-5. 헤더(Headers) 표시를 통한 빠른 탐색
* **원칙**: 긴 텍스트 화면이나 스크롤 화면에서 사용자가 섹션 타이틀만 빠르게 훑어보며 이동할 수 있도록(TalkBack 헤더 네비게이션 모드), 특정 텍스트가 섹션의 대표 제목임을 의미론적으로 표시해줍니다.

```kotlin
Text(
    text = "신체 계측 정보",
    style = MaterialTheme.typography.titleLarge,
    modifier = Modifier.semantics { 
        heading() // 접근성 서비스가 헤더로 인식하여 제목 단위 점프 네비게이션이 가능해짐
    }
)
```

---

### 2-6. 상태 설명 제공 (State Descriptions)
* **원칙**: 토글 버튼이나 활성화/비활성화 상태의 컴포넌트를 만들 때, 단순히 시각적 상태뿐만 아니라 의미론적인 상태도 제공해야 합니다.
* **사용 API**: `stateDescription` 속성을 이용해 현재 커스텀 위젯의 특수한 상태 정보를 한글/영어 텍스트로 치환할 수 있습니다.

```kotlin
val isMuted = remember { mutableStateOf(false) }

IconButton(
    onClick = { isMuted.value = !isMuted.value },
    modifier = Modifier.semantics {
        // TalkBack 포커스 시 단순히 "선택됨/선택 안 됨" 대신 구체적인 상태 안내
        stateDescription = if (isMuted.value) "음소거 됨" else "소리 켬"
    }
) {
    Icon(
        imageVector = if (isMuted.value) Icons.Default.VolumeOff else Icons.Default.VolumeUp,
        contentDescription = "음소거 전환 버튼"
    )
}
```

---

### 2-7. 커스텀 동작 지원 (Custom Accessibility Actions)
* **원칙**: 화면의 아이템을 스와이프해서 삭제(`Swipe-to-Dismiss`)하는 등 복잡한 물리 제스처가 동반되는 인터랙션의 경우, 시각 장애를 가진 사용자는 해당 제스처를 수행하기 곤란합니다.
* **해결책**: 스와이프 등의 행동을 대체할 수 있는 접근성 커스텀 액션(`customActions`)을 제공하여 메뉴 선택만으로 동작을 완수할 수 있게 합니다.

```kotlin
Row(
    modifier = Modifier
        .fillMaxWidth()
        .semantics {
            // TalkBack 사용자에게 "사용 가능한 작업이 있습니다. 보려면 스와이프..." 형태의 알림이 가며,
            // 별도의 접근성 작업 메뉴를 통해 '삭제' 액션을 트리거할 수 있습니다.
            customActions = listOf(
                CustomAccessibilityAction(
                    label = "이 알림 삭제",
                    action = { 
                        onDismissNotification() 
                        true // 처리 성공 반환
                    }
                )
            )
        }
) {
    Text("새로운 알림이 도착했습니다.")
}
```

---

## 3. 고급 접근성 제어: 탐색 순서 및 Semantics 재정의

### 3-1. 탐색 순서 제어 (Traversal Order: isTraversalGroup, traversalIndex)
* **원칙**: TalkBack과 같은 스크린 리더는 화면에 표시되는 요소를 기본적으로 위에서 아래로, 왼쪽에서 오른쪽으로 읽습니다. 하지만 논리적으로 하나의 덩어리로 묶여서 읽혀야 하거나, 시각적 레이아웃 배치가 독특할 경우 읽는 순서가 꼬일 수 있습니다.
* **해결책**: `isTraversalGroup`을 설정해 자식 요소들의 탐색 범위를 그룹화하고, `traversalIndex`를 활용하여 순서를 수동으로 제어합니다.
* **사용 API**:
  * `isTraversalGroup`: 컨테이너 컴포저블에 설정하여 해당 컨테이너 내부의 모든 요소를 먼저 다 읽은 뒤 밖으로 나가도록 지정합니다.
  * `traversalIndex`: 읽히는 순서를 결정하는 실수값(`Float`)입니다. 값이 작을수록 먼저 읽힙니다. (기본값은 `0f`)

```kotlin
// 1) Row를 하나의 탐색 그룹으로 묶고
Row(
    modifier = Modifier.semantics { isTraversalGroup = true }
) {
    // 2) traversalIndex를 설정하여 읽는 순서를 제어
    Text(
        text = "두 번째로 읽히는 텍스트",
        modifier = Modifier.semantics { traversalIndex = 1f }
    )
    Text(
        text = "첫 번째로 읽히는 텍스트",
        modifier = Modifier.semantics { traversalIndex = -1f } // 더 작으므로 먼저 읽힘
    )
}
```

---

### 3-2. Semantics 강제 초기화 및 재정의 (clearAndSetSemantics)
* **원칙**: 하위 요소들의 기본 접근성 정보가 너무 세분화되어 노이즈가 많거나 불필요한 경우, 하위 노드의 모든 Semantics 메타데이터를 제거하고 현재 노드 기준으로 단 하나의 간단한 의미 설명으로 완전히 재정의할 수 있습니다.
* **사용 API**: `Modifier.clearAndSetSemantics`
* **예제 코드**:

```kotlin
// 하위 이미지, 텍스트 정보에 대한 개별 TalkBack 포커스를 차단하고 카드 전체 설명 1개로 대체
Card(
    modifier = Modifier.clearAndSetSemantics {
        contentDescription = "회원 프로필 카드. 이름 홍길동, 직급 수석 디자이너"
    }
) {
    Column {
        Text("홍길동")
        Text("수석 디자이너")
        Image(
            painter = painterResource(R.drawable.badge),
            contentDescription = "인증 마크" // clearAndSetSemantics에 의해 스크린 리더가 스킵함
        )
    }
}
```

---

### 3-3. 접근성 서비스 무시 및 테스트 시 탐색 가능성 (hideFromAccessibility vs clearAndSetSemantics)

* **차이점 핵심 요약**:
  * `hideFromAccessibility()`는 **접근성 서비스(TalkBack 등)에만 보이지 않게 감추고, UI 테스트(testRule) 코드에서는 찾아서 상호작용할 수 있게 유지**하고 싶을 때 사용합니다.
  * 반면, 빈 중괄호의 `clearAndSetSemantics { }`는 **접근성 트리는 물론 UI 테스트 환경(Semantics Tree)에서도 의미 정보가 완전히 지워지므로** 테스트 찾기(Finder)도 영향을 받습니다.

#### 1) hideFromAccessibility()의 특징과 UI 테스트
* **정의**: 특정 노드를 접근성 서비스에서만 건너뛰도록 플래그를 세웁니다. (기존 `invisibleToUser()`가 Deprecated되며 대체된 최신 API)
* **테스트 탐색 가능**: TalkBack은 이 노드를 스킵하지만, `composeTestRule.onNodeWithTag` 또는 `onNodeWithText` 등 **테스트 코드 내의 Finder는 이 노드를 정상적으로 찾아낼 수 있습니다.**
* **자동화 검사 패스**: 테스트에서 `enableAccessibilityChecks()`를 켜둔 상태라면, 해당 노드는 접근성 검사(ATF) 대상에서 자동으로 안전하게 제외됩니다.

```kotlin
// UI 테스트 코드는 아래 노드를 찾아서 클릭할 수 있지만, TalkBack 스크린 리더는 읽지 않고 무시합니다.
Text(
    text = "Decorative Watermark",
    modifier = Modifier
        .testTag("watermark_text")
        .semantics { 
            hideFromAccessibility() 
        }
)

// UI 테스트 코드에서 정상 동작 검증 가능
// composeTestRule.onNodeWithTag("watermark_text").assertExists()
```

#### 2) clearAndSetSemantics { }의 특징과 UI 테스트
* **정의**: 자신과 하위 모든 요소의 의미론적(Semantics) 정보를 깨끗이 지웁니다.
* **테스트 탐색 불가**: 만약 중괄호 내부에 아무것도 선언하지 않으면, 의미론적으로 아무 정보도 없는 노드가 되므로 테스트 Finder(`onNodeWithText` 등)로 찾아내는 것이 거의 불가능해집니다.

```kotlin
// 접근성 서비스와 UI 테스트(Finder) 모두에서 찾을 수 없게 됩니다.
Box(
    modifier = Modifier.clearAndSetSemantics { }
) {
    Text("이 텍스트는 테스트 코드가 onNodeWithText로 찾을 수 없습니다.")
}
```

---

## 4. Android 플랫폼 접근성 핵심 4대 원칙 (Principles for Accessibility)

Jetpack Compose API 적용을 넘어, Android OS 레벨에서 일관되게 강조하는 접근성 기획/디자인 핵심 원칙 4가지는 다음과 같습니다.

### 4-1. 텍스트 대비(Color Contrast) 규격 준수
저시력 사용자나 야외 직사광선 환경의 사용자가 글씨를 명확히 읽을 수 있도록 충분한 대비를 확보해야 합니다.
* **대비율 기준**: 
  * 일반 텍스트: 최소 **4.5:1** 이상의 명도 대비율 필요.
  * 큰 텍스트(18pt/24sp 이상 또는 14pt Bold/19sp Bold 이상): 최소 **3.0:1** 이상의 명도 대비율 필요.
* **Compose 최적화**: 디자인 시스템의 테마 컬러를 설정할 때 Material Theme의 Primary/OnPrimary, Surface/OnSurface 쌍을 확실히 가독성이 검증된 조합으로 매핑해야 합니다.

### 4-2. 색상 하나에만 의존한 정보 전달 금지 (Do not rely on color alone)
색약/색맹 사용자가 UI 상태를 정확하게 구분할 수 있도록 설계해야 합니다.
* **잘못된 설계**: 오류가 발생한 입력창 테두리를 단지 "빨간색"으로만 바꾸고 멘트를 추가하지 않는 것.
* **올바른 설계**: 상태를 나타내는 색상 변화와 함께 **경고 아이콘**, **상태 안내 텍스트("올바르지 않은 형식입니다")** 등의 텍스트/도형 힌트를 반드시 병행 제공합니다.

### 4-3. 시스템 글꼴 크기 설정 존중 (Font Scaling)
Android 시스템 설정에서 사용자가 글자 크기를 기본값보다 크게 또는 작게 조절했을 때, 앱의 UI도 유연하게 대응해야 합니다.
* **폰트 크기 단위**: Compose에서 텍스트의 `fontSize`를 정의할 때는 반드시 **`sp`** 단위를 사용해야 합니다 (`dp`를 사용하면 시스템 글꼴 크기 변경에 반응하지 않아 접근성에 저해됩니다).
* **레이아웃 유연성**: 시스템 글꼴이 커질 때 텍스트가 잘리거나 화면을 벗어나지 않도록, `Height` 값을 하드코딩하기보다 `wrapContentHeight()`나 `scroll` 가능한 컨테이너를 적용해야 합니다.

### 4-4. 하드웨어 키보드 및 D-pad 포커스 내비게이션
사용자가 마우스나 터치 스크린이 아닌 하드웨어 키보드, D-pad, 혹은 보조 입력 장치(Switch Access)를 사용하여 탭(Tab) 키로 항목을 이동할 때, 포커스가 논리적이고 순차적으로 이동할 수 있어야 합니다.
* **Compose 제어**: 포커스 이동 흐름을 바꾸려면 `FocusRequester` 및 `Modifier.focusProperties { next = ... }` 등을 사용해 포커스 순서를 수동 조정할 수 있습니다.

---

## 5. 접근성 디버깅 및 테스트 방법 (a11y Testing)

1. **TalkBack 활성화 후 직접 테스트**:
   * Android 설정 -> 접근성 -> TalkBack을 켭니다.
   * 손가락 제스처 및 볼륨 버튼 등을 통해 UI 포커스가 논리적인 순서로 이동하는지 확인합니다.
2. **접근성 검사기 (Accessibility Scanner) 사용**:
   * Google Play Store에서 `Accessibility Scanner` 앱을 다운로드하여 켭니다.
   * 대상 앱 화면을 캡처하면 터치 타깃 크기 부족, 텍스트 대비(Contrast) 불충분, 대체 텍스트 누락 지점을 화면에 사각형 박스로 하이라이팅하여 진단해 줍니다.
3. **Android Studio Layout Inspector**:
   * Layout Inspector의 `Semantics Tre` 뷰를 이용하면, 렌더링된 컴포저블 트리가 겉보기 UI가 아닌 접근성 시스템에 전달하는 Semantics 속성 구조를 시각적으로 디버깅할 수 있습니다.
4. **UI 테스트 코드에서 자동화된 접근성 검사 (Automated Accessibility Checks)**:
   * **원칙**: Compose UI 테스트 코드가 동작하는 과정에서 접근성 규칙 위반을 자동으로 잡아내어 테스트를 실패시킬 수 있습니다.
   * **설정 및 사용**:
     * `AndroidComposeTestRule` 인스턴스에 `enableAccessibilityChecks()`를 설정합니다. (Accessibility Test Framework 연동)
     * 이 검사는 클릭(`performClick`) 등 사용자의 물리 제스처가 동반되는 노드가 수행될 때 해당 화면의 대비 비율, 터치 크기, 대체 텍스트 누락 등을 자동으로 감사합니다.
   * **예제 코드**:
     ```kotlin
     @Rule
     @JvmField
     val composeTestRule = createAndroidComposeRule<MainActivity>()

     @Before
     fun setUp() {
         // 테스트 실행 중 자동 접근성 검사 활성화
         composeTestRule.enableAccessibilityChecks()
     }

     @Test
     fun sampleTest() {
         // 노드 상호작용 발생 시 자동으로 접근성 유효성을 검사하여 위반 시 실패처리
         composeTestRule.onNodeWithContentDescription("공유").performClick()
     }
     ```

