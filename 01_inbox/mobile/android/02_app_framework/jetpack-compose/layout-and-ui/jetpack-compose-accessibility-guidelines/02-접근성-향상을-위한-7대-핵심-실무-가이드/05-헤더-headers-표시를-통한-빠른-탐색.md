# 헤더(Headers) 표시를 통한 빠른 탐색
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
