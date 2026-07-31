# 중요: Compose Compiler는 BOM 관리 대상이 아님

> [!IMPORTANT]
> **Compose BOM은 Compose Compiler의 버전을 제어하지 않습니다.**

* **이유**: Compose Compiler는 빌드 시점에 Kotlin 코드를 트랜스파일하는 특수한 컴파일러 플러그인이기 때문에, 화면 렌더링용 Compose 라이브러리가 아닌 Kotlin 컴파일러 버전에 긴밀하게 종속됩니다.
* **해결**: Kotlin 2.0 이상부터는 Compose Compiler Gradle Plugin(`org.jetbrains.kotlin.plugin.compose`)을 통해 Kotlin 버전과 통합하여 따로 관리해야 합니다.
