# 언제 직접 Local을 읽어도 되나?

상위 노트: [[jetpack-compose-compositionlocal-and-designsystem-locals]]

직접 읽어도 되는 경우:

- spacing/gap이 필요해서 `LocalMyBenefitLayoutMetrics`를 읽는 경우
- 화면별 `AdaptiveLayoutPolicy`가 posture에 따라 variant를 고르는 경우
- app shell처럼 navigation chrome을 직접 결정해야 하는 경우

가능하면 피해야 하는 경우:

- 단순히 화면 padding을 얻기 위해 모든 화면에서 직접 Local을 읽는 것
- feature 화면마다 tablet/foldable 분기를 직접 만드는 것
- `ViewModel`, repository, callback 같은 화면별 의존성을 Local로 숨기는 것

권장 순서:

```text
1. 일반 container가 필요하면 MyBenefitAdaptiveScreen을 사용한다.
2. 화면별 adaptive 차이가 필요하면 feature 안에 AdaptiveLayoutPolicy를 둔다.
3. 간격이 필요하면 LocalMyBenefitLayoutMetrics를 읽는다.
4. 정말 posture별 기능 차이가 필요할 때만 LocalMyBenefitWindowPosture를 읽는다.
5. AndroidX WindowManager 타입은 feature에서 직접 읽지 않는다.
```

---
