# 3 `LocalMyBenefitWindowAdaptivity.kt`

상위 노트: [[06-각-파일의-역할]]

경로:

```text
core/designsystem/src/main/java/com/benefit/virtualmate/core/designsystem/adaptive/LocalMyBenefitWindowAdaptivity.kt
```

역할:

- `MyBenefitWindowAdaptivity`를 Compose tree 전체에 전달합니다.
- 앱 전체 adaptive 상태를 읽는 최상위 Local입니다.

제공 위치:

```text
ProvideMyBenefitWindowAdaptivity
```

읽는 위치 예:

```text
MainShellAdaptivePolicy
DashboardAdaptiveLayoutPolicy
각 feature의 layout policy
```

이 값은 "현재 adaptive 환경을 화면별 정책이 어떻게 해석할지"가 필요할 때 읽습니다.

---
