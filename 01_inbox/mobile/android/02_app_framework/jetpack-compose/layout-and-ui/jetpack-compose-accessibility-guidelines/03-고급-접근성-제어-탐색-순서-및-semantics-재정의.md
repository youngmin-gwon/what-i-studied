# 고급 접근성 제어: 탐색 순서 및 Semantics 재정의

상위 노트: [[jetpack-compose-accessibility-guidelines]]

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
