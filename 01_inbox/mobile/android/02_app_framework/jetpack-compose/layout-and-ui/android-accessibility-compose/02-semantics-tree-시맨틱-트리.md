# Semantics Tree (시맨틱 트리)

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
