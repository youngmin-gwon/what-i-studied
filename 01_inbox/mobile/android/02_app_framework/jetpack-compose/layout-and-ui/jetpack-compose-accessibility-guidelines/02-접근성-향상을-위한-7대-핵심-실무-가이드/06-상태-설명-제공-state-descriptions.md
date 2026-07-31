# 상태 설명 제공 (State Descriptions)
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
