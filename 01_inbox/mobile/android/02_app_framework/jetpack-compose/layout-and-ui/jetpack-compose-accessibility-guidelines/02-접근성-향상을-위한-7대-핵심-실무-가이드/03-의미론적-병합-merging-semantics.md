# 의미론적 병합 (Merging Semantics)
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
