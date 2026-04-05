---
title: android-accessibility-compose
tags: []
aliases: []
date modified: 2026-04-05 17:42:51 +09:00
date created: 2026-04-04 00:28:14 +09:00
---

## [[mobile-security]] > [[android-accessibility-compose]]

### Accessibility: Inclusive Design with Compose

장애가 있는 사용자를 포함한 모든 사용자가 앱을 동등하게 사용할 수 있도록 돕는 **안드로이드 접근성(Accessibility)**과 **Semantics Tree** 설계 기법을 분석합니다.

단순히 시각적 UI 를 구현하는 것을 넘어, 선언형 프레임워크인 Compose 에서 접근성 정보를 어떻게 구조화하고 TalkBack 등의 보조 기술과 유기적으로 통신할지 이해하는 것이 목표입니다.

---

#### 💡 Context: 접근성의 가치와 책임

접근성은 선택이 아닌 필수입니다. 모든 사용자를 포용하는 디자인은 앱의 품질을 높일 뿐만 아니라, 법적 요구사항을 준수하고 브랜딩에 긍정적인 영향을 미칩니다. [[android-ui-system]] 과 [[android-compose-internals]] 위에서 시맨틱 정보를 견고하게 구축해야 합니다.

>[!NOTE] **상호 참조**
>iOS 의 접근성 지원 방식은 [[apple-accessibility-and-internationalization]] 을 참고하세요.

---

#### 1. Semantics Tree (시맨틱 트리)

Compose 상계(UI Tree)의 각 노드는 '의미'를 담은 시맨틱 노드와 연결될 수 있다.

##### 기본 속성 설정

```kotlin
@Composable
fun UserProfileImage(description: String) {
    Image(
        painter = painterResource(R.drawable.profile),
        contentDescription = null, // 시각적 요소가 아닌 정보는 null
        modifier = Modifier.semantics {
            // 명시적으로 역할과 설명을 부여
            contentDescription = description
            role = Role.Image
        }
    )
}
```

#### 2. TalkBack 연동 및 최적화

TalkBack 은 시맨틱 트리를 탐색하며 사용자에게 정보를 읽어준다.

##### 요소 그룹화 및 병합 (Merge)

작은 요소들이 흩어져 있으면 TalkBack 사용자가 일일이 클릭해야 하므로 불편하다. 관련된 정보는 하나로 병합하는 것이 UX 에 좋다.

```kotlin
@Composable
fun PostItem(post: Post) {
    Row(
        modifier = Modifier.semantics(mergeDescendants = true) {
            // 하위 요소들의 시맨틱 정보를 하나로 합쳐서 읽어줌
            contentDescription = "${post.author}의 게시글: ${post.content}"
        }
    ) {
        Avatar(post.author)
        Text(post.content)
    }
}
```

#### 3. 커스텀 액션 (Custom Actions)

스와이프나 롱클릭 등 시각적 제스처를 접근성 서비스가 이해할 수 있도록 명시한다.

```kotlin
Modifier.semantics {
    customActions = listOf(
        CustomAccessibilityAction("삭제") { 
            viewModel.deleteItem()
            true 
        }
    )
}
```

>[!CAUTION] **Devil's Advocate : 테스트를 위해 접근성을 희생하지 마라**
>Compose UI 테스트에서 요소를 찾기 위해 `testTag` 를 남발하는 대신, 실제 사용자가 접근성 엔진을 통해 보는 정보인 `contentDescription` 이나 `role` 을 기반으로 테스트를 작성하라. 이는 테스트 안정성과 접근성 품질을 동시에 높이는 방법이다.

#### 📊 플랫폼별 주요 개념 매핑

| 특징 | Android (Compose) | iOS (SwiftUI) |
| :--- | :--- | :--- |
| **스크린 리더** | TalkBack | VoiceOver |
| **의미 노드** | Semantics Node | Accessibility Element |
| **요소 병합** | `mergeDescendants = true` | `.accessibilityElement(children: .combine)` |
| **역할 정의** | `Role` | `AccessibilityTrait` |

#### See Also

- [[android-ui-system]]
- [[android-compose-internals]]
- [[android-testing-and-quality]]
