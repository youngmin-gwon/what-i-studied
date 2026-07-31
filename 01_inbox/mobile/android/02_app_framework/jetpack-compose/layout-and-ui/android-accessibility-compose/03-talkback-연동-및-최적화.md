# TalkBack 연동 및 최적화

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
