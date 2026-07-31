# BoxWithConstraints 사용 시 주의사항 및 대체 방안

상위 노트: [jetpack-compose-performance-guidelines](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines.md)

`BoxWithConstraints`는 하위 컴포저블의 레이아웃 제약조건(`maxWidth`, `maxHeight` 등)을 사전에 확인하여 분기 UI를 그릴 때 매우 유용한 컴포저블입니다.

### 6-1. 성능상 오버헤드와 남용 금지 이유
* **Subcomposition(하위 구성) 오버헤드**: `BoxWithConstraints`는 레이아웃 측정(Measurement) 단계에서 제약조건을 파악한 뒤, 람다 내부의 컴포저블을 비동기로 다시 컴포지션(Subcomposition)합니다.
* 이 과정은 일반 `Box`나 `Column`보다 **훨씬 큰 리컴포지션 오버헤드와 CPU 파이프라인 지연**을 유발하므로 리스트 아이템 내부나 스크롤이 잦은 UI에서 남용하면 심각한 프레임 드랍(Jank)의 원인이 됩니다.

### 6-2. 올바른 사용 조건 vs 대체 방안
* ❌ **지양해야 할 케이스**: 단순 `Modifier` 크기 계산, 스크롤 영역 내부 아이템 렌더링.
* 🐳 **권장 케이스**: 화면 폭에 따라 전혀 다른 형태의 UI 구조(예: 싱글 뷰 vs 스플릿 뷰)로 분기해야 하는 최상위 윈도우/스크린 레이아웃.
* 💡 **대체 방안**:
  1. `Modifier.layout` 확장 함수 사용: 단기 측정 및 크기 조정만 필요한 경우 1단계 Subcomposition을 건너뛰고 2단계 Layout에서만 작업 수행.
  2. `WindowSizeClass` 활용: 화면 폭에 따른 분기는 `BoxWithConstraints` 대신 WindowSizeClass(Compact/Medium/Expanded)를 사용해 최상단에서 전역으로 분기.

---
