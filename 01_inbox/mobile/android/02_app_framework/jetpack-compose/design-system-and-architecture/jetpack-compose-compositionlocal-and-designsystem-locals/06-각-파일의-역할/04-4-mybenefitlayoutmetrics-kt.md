# 4 `MyBenefitLayoutMetrics.kt`

상위 노트: [06-각-파일의-역할](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/jetpack-compose-compositionlocal-and-designsystem-locals/06-%EA%B0%81-%ED%8C%8C%EC%9D%BC%EC%9D%98-%EC%97%AD%ED%95%A0.md)

경로:

```text
core/designsystem/src/main/java/com/benefit/virtualmate/core/designsystem/adaptive/MyBenefitLayoutMetrics.kt
```

역할:

- window size에 따라 달라지는 화면 padding과 gap을 표현합니다.
- `MyBenefitSpacing` 같은 원시 token을 화면 의미 단위로 매핑합니다.
- metrics 선택은 raw `widthDp`가 아니라 `MyBenefitWindowProfile`을 기준으로 합니다.
- 그래서 휴대폰 가로 화면처럼 width는 넓지만 height가 낮은 window는 compact metrics를 사용합니다.

차이:

```text
MyBenefitSpacing
- 8.dp, 16.dp, 24.dp 같은 원시 spacing token

MyBenefitLayoutMetrics
- screenHorizontalPadding, contentGap, paneGap 같은 화면 의미 token
```

feature 화면은 가능하면 `16.dp`를 직접 쓰지 않고 `LocalMyBenefitLayoutMetrics.current`를 읽습니다.

---
