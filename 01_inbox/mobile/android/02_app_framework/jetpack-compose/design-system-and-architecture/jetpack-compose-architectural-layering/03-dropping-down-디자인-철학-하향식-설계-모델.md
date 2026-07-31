# "Dropping Down" 디자인 철학 (하향식 설계 모델)

Jetpack Compose는 개발자가 원하는 대로 **하위 레이어로 직접 하강(Drop Down)**하여 유연하게 커스터마이징을 할 수 있는 아키텍처적 유연성을 보장합니다.

### 3-1. 동작 원리: 래퍼(Wrapper) 구조
Compose의 고수준 컴포넌트들은 마법처럼 새로운 것을 띄우는 것이 아니라, 하위 레이어의 기본 컴포넌트들을 감싼 **래퍼(Wrapper)** 형태로 구현되어 있습니다.
* 예: `androidx.compose.material.Text` (Material)는 내부적으로 `androidx.compose.foundation.text.BasicText` (Foundation)를 호출하며 테마 스타일을 입힌 구조입니다.
* 발견 가능성(Discoverability)을 높이기 위해 가장 일반적이고 직관적인 명칭(`Text`)은 최상위 Material 레이어에 부여하고, 하위 레이어 컴포넌트에는 접두사(`BasicText`)를 붙여 구별합니다.

### 3-2. 언제 Drop Down해야 하는가?
1. **커스텀 디자인 시스템 구축**: 프로젝트가 Material Design을 전혀 사용하지 않고 자체적인 디자인 가이드라인을 갖는 경우, Material을 빼고 **Foundation**이나 **Compose UI**를 기반으로 전용 컴포넌트를 설계합니다.
2. **극단적인 커스터마이징**: 상위 컴포넌트가 제공하는 파라미터 한계를 초과하는 변형이 필요할 때, 하위 컴포넌트(`Basic...`)를 가져와 새롭게 구현합니다.

---
