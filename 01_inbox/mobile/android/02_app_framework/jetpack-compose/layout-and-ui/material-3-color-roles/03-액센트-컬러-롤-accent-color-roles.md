# 액센트 컬러 롤 (Accent Color Roles)

사용자의 시선을 사로잡거나 UI 요소의 중요도를 표출하기 위해 사용하는 핵심 브랜드 컬러 계열입니다.

### 3-1. Primary (주요 엑센트)

* **역할**: 앱 화면 전체에서 가장 중심이 되는 브랜드 정체성 컬러입니다.
* **사용처**: 주요 동작 버튼(FAB, Filled Button), 활성화 상태(Selected Tabs, Checked Switch, Radio Button), 로딩 바
  등.
* **패밀리**: `Primary` / `OnPrimary` / `PrimaryContainer` / `OnPrimaryContainer`

### 3-2. Secondary (보조 엑센트)

* **역할**: 브랜드 내에서 덜 눈에 띄는 보조적인 영역을 칠할 때 사용하며, 톤을 낮춘 세련된 강조를 원할 때 사용합니다.
* **사용처**: 필터 칩(Filter Chips), 보조 버튼, 덜 중요한 활성 상태 표현 등.
* **패밀리**: `Secondary` / `OnSecondary` / `SecondaryContainer` / `OnSecondaryContainer`

### 3-3. Tertiary (제3의 엑센트)

* **역할**: Primary와 Secondary 사이에서 시각적 균형을 맞추거나, 완전히 다른 카테고리의 요소에 대조 효과를 주어 시선을 집중시키고자 할 때 사용합니다.
* **사용처**: 입력 필드의 포커스 하이라이팅, 신규 알림 배지, 캘린더의 특별한 기념일 표시 등.
* **패밀리**: `Tertiary` / `OnTertiary` / `TertiaryContainer` / `OnTertiaryContainer`

### 3-4. Fixed / Fixed Dim / On Fixed 계열 (라이트/다크 테마 고정 컬러)

M3에서 새롭게 도입된 핵심 개념으로, **라이트 모드와 다크 모드 간에 색상 값이 뒤집히지 않고 동일하게 유지(Fixed)** 되는 액센트 계열입니다.

일반적인 Container 색상들은 테마가 바뀌면 밝기 조절을 위해 색상 값이 서로 스왑되지만, Fixed 계열은 두 테마 환경 모두에서 동일한 비주얼(동일한 명도와 채도)을
나타내야 하는 컴포넌트에 사용합니다.

* **`primaryFixed`**
    * **역할**: 일반 `primaryContainer`처럼 기능하지만, 라이트/다크 모드에 상관없이 항상 동일한 채도와 명도를 가지는 고정 배경색입니다.
* **`primaryFixedDim`**
    * **역할**: `primaryFixed`보다 명도가 한 단계 낮아(Dim), 다크 테마에서 대조도를 살짝 조절하거나 조금 더 차분한 가중치를 부여하고 싶을 때 선택할 수
      있는 대안 고정 배경색입니다.
* **`onPrimaryFixed`**
    * **역할**: `primaryFixed` 및 `primaryFixedDim` 배경 위에 올라가는 가장 선명한 가독성의 전용 글자/아이콘 색상입니다.
* **`onPrimaryFixedVariant`**
    * **역할**: `onPrimaryFixed`보다 한 단계 대비 강도가 낮아, 고정 배경 위에서 보조 설명 글이나 덜 중요한 아이콘에 적합합니다.

> [!NOTE]
> Fixed 계열 롤은 **Primary, Secondary, Tertiary** 3대 핵심 엑센트 그룹 전체에 동일하게 쌍으로 존재합니다.
> * 예: `secondaryFixed`, `secondaryFixedDim`, `onSecondaryFixed`, `onSecondaryFixedVariant` 등

---
