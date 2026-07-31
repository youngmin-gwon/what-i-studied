# 💡 Context: UI 패러다임의 변화

안드로이드 UI 개발은 최근 몇 년간 큰 변화를 겪었습니다. 기존 XML 기반의 명령형(Imperative) 방식에서 Kotlin 코드로 UI 를 정의하는 선언형(Declarative) 방식으로의 전환은 개발 생산성과 유지보수성을 획기적으로 개선했습니다.

---

- **Performance**: `ConstraintLayout` 은 View 계층 깊이를 줄여 성능을 높였지만, 여전히 XML 파싱과 리플렉션 비용이 큽니다. Compose 는 코드로 컴파일되므로 이 비용이 없습니다.
- **State Sync**: View 시스템에서는 데이터가 바뀌면 `setText()` 를 수동으로 호출해야 합니다. 실수하면 UI 와 데이터가 틀어집니다. Compose 는 **Single Source of Truth**를 강제합니다.
- **Animations**: View 애니메이션은 "시작점과 끝점"을 정의하고 보간(Interpolation)하는 방식이지만, Compose 는 "상태 A 에서 상태 B 로의 전환"으로 정의합니다. 훨씬 직관적입니다.

---
