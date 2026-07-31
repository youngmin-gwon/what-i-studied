# 2 `MyBenefitWindowProfile.kt`

상위 노트: [06-각-파일의-역할](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/jetpack-compose-compositionlocal-and-designsystem-locals/06-%EA%B0%81-%ED%8C%8C%EC%9D%BC%EC%9D%98-%EC%97%AD%ED%95%A0.md)

경로:

```text
core/designsystem/src/main/java/com/benefit/virtualmate/core/designsystem/adaptive/MyBenefitWindowProfile.kt
```

역할:

- width/height size class 조합을 앱에서 바로 쓰기 좋은 profile로 정리합니다.
- Android orientation 값이 아니라 현재 app window 모양을 표현합니다.
- feature나 shell이 매번 `width == Compact || height == Compact` 같은 조건을 반복하지 않게 합니다.

대표 값:

```text
CompactPortrait
- 폭이 좁고 높이는 충분한 일반 휴대폰 세로 화면

CompactLandscape
- 폭은 넓을 수 있지만 높이가 낮은 휴대폰 가로 화면 또는 얇은 freeform window

CompactConstrained
- 폭과 높이가 모두 좁은 split-screen/freeform window

Medium / Expanded / Large / ExtraLarge
- 높이가 충분하고 폭 구간에 따라 확장 가능한 window
```

---
