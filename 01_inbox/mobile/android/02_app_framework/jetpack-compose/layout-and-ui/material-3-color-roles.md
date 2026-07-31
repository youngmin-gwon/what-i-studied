# Material 3 컬러 롤 가이드 (Material 3 Color Roles)

이 문서는 Material Design 3(M3) 컬러 시스템의 핵심 개념인 **컬러 롤(Color Roles)** 의 역할과 구성 요소, 그리고 각 색상군이 UI에서 실제로
어떻게 적용되어야 하는지 한글로 상세하게 번역 및 요약하여 설명합니다.

본 문서는 공식 [Material 3 Color Roles Spec](https://m3.material.io/styles/color/roles)의 표준 설계 방식을 기반으로
작성되었습니다.

---

## 1. M3 컬러 시스템 및 컬러 롤 개요

### 1-1. 컬러 롤(Color Role)이란?

컬러 롤은 구체적인 색상 값(예: `#6200EE` 또는 "파란색") 대신 **"이 영역이 UI에서 어떤 역할(Role)을 수행하는지"** 를 나타내는 의미론적 이름(
Semantic Label)입니다.

* **연결 고리**: 개별 UI 컴포넌트는 실제 색상 값에 직접 묶이지 않고 `primary`, `surfaceContainer` 등의 컬러 롤에 매핑됩니다.
* **접근성 및 동적 매칭**: 사용자의 배경화면에서 추출된 Dynamic Color 시스템이나 라이트/다크 모드에 맞춰 색상 값 자체가 변경되더라도, 사전에 설정된 컬러 롤의
  상대적 대비(Contrast) 법칙 덕분에 글자 가독성과 화면 레이아웃의 선명도가 자동으로 보장됩니다.

```text
[브랜드 팔레트 / Dynamic Color]
          ↓ (컬러 스키마 빌드)
  [컬러 롤 (Color Roles)]  ← 예: primary, surface, onPrimary
          ↓ (의미론적 적용)
[UI 컴포넌트 (Components)]  ← 예: Button, Card, Dialog
```

---

## 2. 컬러 명명법의 규칙 (Suffixes & Modifiers)

M3에서는 일관된 대비 보장을 위해 컬러 이름 끝에 다음과 같은 접미사/변형 규칙을 적용합니다.

| 이름 형태                   | 설명                                                 | 사용 예시                                |
|:------------------------|:---------------------------------------------------|:-------------------------------------|
| **`{Base}`**            | 컴포넌트의 가장 기본이 되는 핵심 배경/칠(Fill) 색상                   | `Primary`, `Secondary`, `Error`      |
| **`On{Base}`**          | Base 색상 위에 얹어지는 **글자(Text), 아이콘(Icon)** 전용 색상      | `OnPrimary`, `OnSecondary`           |
| **`{Base}Container`**   | Base보다 톤이 낮고 채도가 부드러운 **넓은 면적의 용기(Container)** 배경색 | `PrimaryContainer`, `ErrorContainer` |
| **`On{Base}Container`** | Container 색상 위에 얹어지는 글자 및 아이콘 전용 색상                | `OnPrimaryContainer`                 |

> [!IMPORTANT]
> **접근성(Accessibility) 대비 규칙**
> * `{Base}`와 `On{Base}` 쌍은 스크린 리더 없이 일반 사용자가 글씨를 명확히 읽을 수 있도록 상호간에 **충분한 대비(최소 4.5:1 이상)** 가 나도록
    설계되어 있습니다.
> * `{Base}Container`와 `On{Base}Container` 역시 상호간에 **최소 3:1 이상의 대비**를 만족합니다.

---

## 3. 액센트 컬러 롤 (Accent Color Roles)

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

## 4. 표면 및 배경 컬러 롤 (Surface & Background Roles)

이전의 Material Design 2에서는 입체감을 나타내기 위해 z-축 높이(Elevation)가 높아질수록 흰색 반투명 레이어를 올려 배경을 밝게 틴팅하는
Elevational Overlay 방식을 썼습니다.

**Material 3에서는 이를 완전히 폐지하고**, 서로 다른 밝기 단계를 가진 **전용 표면 컬러 롤**을 정의하여 깊이감과 가독성을 해결합니다.

### 4-1. Background (바탕 배경)

* **역할**: 앱의 가장 바닥 레이어를 차지하는 배경색입니다.
* **패밀리**: `Background` / `OnBackground` (그 위의 글씨)

### 4-2. Surface Base (기본 표면)

* **역할**: 카드, 시트, 다이얼로그 등 본문 콘텐츠를 담는 컴포넌트의 디폴트 배경입니다.
* **패밀리**: `Surface` / `OnSurface` / `SurfaceVariant` (연한 변형) / `OnSurfaceVariant`

### 4-3. Surface Dim & Bright (표면 조도)

* **역할**: 기본 Surface를 기점으로 조도를 달리하여 공간을 구조화합니다.
* **`Surface Dim`**: 기존 배경보다 조금 더 어둡고 차분한 톤. 다크 모드 등에서 화면 심도를 낮추는 영역에 배치.
* **`Surface Bright`**: 기본 배경보다 더 밝고 뚜렷한 톤. 모달 팝업 등 주의 환기가 집중되어 위로 치솟아야 할 영역에 배치.

### 4-4. Surface Container 계층 구조 (가장 중요)

컴포넌트의 중요도와 입체감 높이에 따라 **배경과의 대조도를 5단계로 세분화**하여 제공하는 컨테이너 전용 표면 그룹입니다.

| 컬러 롤 이름                         | 상대적 강조도          | 주요 추천 사용처                                       |
|:--------------------------------|:-----------------|:------------------------------------------------|
| **`Surface Container Lowest`**  | 가장 낮음            | 화면 상에서 시각적 깊이가 가장 깊은 최하단 영역의 레이아웃 또는 기본 앱 배경    |
| **`Surface Container Low`**     | 낮음               | 그리드 배경, 리스트 스크롤 영역 카드 컴포넌트 배경                   |
| **`Surface Container`**         | **중간 (Default)** | 가장 일반적으로 사용되는 컴포넌트 수납 영역 (예: 카드 뷰, 내비게이션 드로어)   |
| **`Surface Container High`**    | 높음               | 플로팅 카드, 컨텐츠 영역 위에 놓이는 다이얼로그나 설정 바텀시트            |
| **`Surface Container Highest`** | 가장 높음            | 팝업 메뉴, 플로팅 툴팁 등 화면의 가장 최상층에서 명확히 구분되어야 하는 임시 UI |

---

## 5. 기타 특수 목적 유틸리티 컬러 롤

### 5-1. Error (경고/오류 상태)

* **역할**: 유효성 검사 실패, 삭제 시 주의 환기, 시스템 에러 등 부정적인 경고 상태를 사용자에게 명확히 인지시킵니다.
* **사용처**: 입력창 하단 경고 문구, "영구 삭제" 버튼 배경, 실패 다이얼로그 테두리 등.
* **패밀리**: `Error` / `OnError` / `ErrorContainer` / `OnErrorContainer`

### 5-2. Outline (경계 및 아웃라인)

* **역할**: 컴포넌트 간의 물리적 경계와 분할을 강조 또는 격리할 때 사용합니다.
* **`Outline`**: 텍스트 필드의 입력 테두리, 보조 버튼의 외곽선 등 높은 대조가 필요한 선에 사용.
* **`Outline Variant`**: 리스트 항목 구분선(Divider)이나 장식적인 경계선 등 낮은 대조가 요구되는 영역에 사용.

### 5-3. Inverse (역톤 색상)

* **역할**: 전체 화면 테마가 밝을 때 잠시 어두운 패널(혹은 반대)을 보여주어 명확한 시각 대비를 주고 싶을 때 사용합니다.
* **사용처**: 잠깐 나왔다 사라지는 **스낵바(Snackbar)** 컴포넌트 배경 및 글자색.
* **패밀리**: `InverseSurface` / `InverseOnSurface` / `InversePrimary`

---

## 6. Material 3 Expressive와 컬러 스키마 변형 (Color Scheme Variants)

Material Design 3의 진화 단계인 **Material 3 Expressive** 시스템은 획일화된 컬러 시스템에서 벗어나, 더욱 브랜드 지향적이고 감정 중심의 UI(
Emotion-driven UX)를 구현할 수 있도록 **컬러 스키마 변형(Color Scheme Variants)** 을 제공합니다.

시드 컬러(Seed Color) 하나를 기반으로 Tonal Palette를 생성할 때, 수학적 알고리즘을 조절하여 아래의 5가지 다른 "무드(Vibe)"를 만들 수 있습니다.

### 6-1. 대표적인 5대 컬러 스키마 변형

1. **Tonal Spot (톤 스팟 - 기본값)**
    * **특징**: M3의 디폴트 스키마입니다. 채도(Chroma)를 적당히 억제하여 전반적으로 부드럽고 차분한 파스텔 톤을 형성합니다.
    * **목적**: 균형 잡힌 가독성과 대중적인 접근성 제공.
2. **Vibrant (바이브런트 - 활기참)**
    * **특징**: 기본 엑센트(Primary, Secondary)의 채도와 선명도를 최대로 올려 색을 매우 진하고 밝게 만듭니다.
    * **목적**: 역동적이고 에너지가 필요한 피트니스, 엔터테인먼트 앱 등에 적합.
3. **Expressive (익스프레시브 - 개성/고대비)**
    * **특징**: Primary와 Secondary/Tertiary 사이의 **색조(Hue) 차이를 의도적으로 크게 넓혀** 배치합니다 (예: 메인색이 파란색일 때 보조색을
      따뜻한 주황색 계열로 90도 회전). 또한 채도를 높여 개성 있고 강렬한 시각적 대비를 이끌어냅니다.
    * **목적**: 브랜드 정체성을 극대화하거나 다채롭고 독특한 아트워크 중심의 UI 연출.
4. **Neutral (뉴트럴 - 중립)**
    * **특징**: 컬러의 채도를 극단적으로 낮추어 무채색(Grayscale)에 가깝게 만듭니다.
    * **목적**: 콘텐츠(사진, 비디오) 자체가 다채로워 UI 컬러가 시선을 빼앗지 않아야 하는 경우, 혹은 극도의 정갈함과 프로페셔널한 톤앤매너가 필요한 커머스나 핀테크
      앱.
5. **Content / Fidelity (콘텐츠 / 피델리티 - 원본 지향)**
    * **특징**: 입력된 브랜드 로고나 대표 이미지(앨범 커버 등)의 고유한 색상 특성(Hue, Chroma)을 왜곡하지 않고 고스란히 반영하여 파생 롤들을 생성합니다.
    * **목적**: 앨범 아트를 기반으로 재생화면 테마를 실시간으로 맞출 때 유용.

### 6-2. Jetpack Compose 구현 힌트

안드로이드의 기본 동적 컬러 API(`dynamicLightColorScheme`)는 내부적으로 `Tonal Spot`을 기본 알고리즘으로 채택합니다. 만약 `Vibrant`나
`Expressive` 같은 감각적인 스키마를 명시적으로 표현하려면, 구글의 오픈소스 라이브러리인 **`Material Color Utilities`** 를 사용하여 직접 테마
스키마를 파싱하거나, 생성된 스태틱 컬러 세트를 테마에 매핑해주어야 합니다.

