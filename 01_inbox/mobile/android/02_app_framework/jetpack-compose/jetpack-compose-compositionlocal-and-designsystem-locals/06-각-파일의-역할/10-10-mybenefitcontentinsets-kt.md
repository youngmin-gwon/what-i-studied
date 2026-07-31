# 10 `MyBenefitContentInsets.kt`

상위 노트: [[06-각-파일의-역할]]

경로:

```text
core/designsystem/src/main/java/com/benefit/virtualmate/core/designsystem/layout/MyBenefitContentInsets.kt
```

역할:

- layout metrics가 아니라 runtime overlay inset을 표현합니다.
- floating toolbar처럼 실제 크기를 측정해야 알 수 있는 UI 여백을 하위 화면에 전달합니다.

중요한 차이:

```text
screen padding
- 화면 기본 여백
- MyBenefitLayoutMetrics가 담당

content inset
- floating toolbar, navigation chrome 때문에 scroll content가 추가로 피해야 하는 여백
- MyBenefitContentInsets가 담당
```

특히 compact main shell의 floating toolbar는 overlay입니다.

따라서 화면 전체를 위로 밀면 안 됩니다.

```text
잘못된 방식:
전체 화면 Modifier.padding(bottom = toolbarHeight)

의도한 방식:
LazyColumn contentPadding(bottom = toolbarHeight)
```

그래야 content는 floating bar 아래까지 뻗고, 마지막 item만 bar 뒤에 가려지지 않습니다.

---
