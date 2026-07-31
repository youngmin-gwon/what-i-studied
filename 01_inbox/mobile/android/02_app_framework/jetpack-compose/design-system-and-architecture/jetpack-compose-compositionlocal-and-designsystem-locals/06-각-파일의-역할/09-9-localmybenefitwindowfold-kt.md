# 9 `LocalMyBenefitWindowFold.kt`

상위 노트: [06-각-파일의-역할](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/jetpack-compose-compositionlocal-and-designsystem-locals/06-%EA%B0%81-%ED%8C%8C%EC%9D%BC%EC%9D%98-%EC%97%AD%ED%95%A0.md)

경로:

```text
core/designsystem/src/main/java/com/benefit/virtualmate/core/designsystem/adaptive/LocalMyBenefitWindowFold.kt
```

역할:

- 현재 fold/hinge만 빠르게 읽을 수 있게 합니다.
- `LocalMyBenefitWindowAdaptivity.current.windowFold`와 같은 의미입니다.

일반 화면은 이 값을 직접 읽기보다 화면별 `AdaptiveLayoutPolicy`에서 읽는 편이 좋습니다.

---
