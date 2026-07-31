# `build.gradle.kts`에서 `libs.~`로 바뀌는 이유

TOML 파일에는 `android-navigation-compose`라고 적지만, `build.gradle.kts`에서는
`libs.android.navigation.compose`로 씁니다.

#### 변환 규칙: 하이픈(`-`)이나 언더바(`_`)는 마침표(`.`)로 바뀐다

```
[TOML 파일]  android - navigation - compose
                ⬇          ⬇          ⬇
[KTS 파일]   libs . android . navigation . compose
```

**이유**: `build.gradle.kts`는 **코틀린 코드**입니다. 코틀린 변수명에 하이픈(`-`)을 쓰면 뺄셈 연산자로 인식하므로, 마침표(`.`)로 변환하여 코틀린
객체 계층 구조로 만들어 줍니다.
