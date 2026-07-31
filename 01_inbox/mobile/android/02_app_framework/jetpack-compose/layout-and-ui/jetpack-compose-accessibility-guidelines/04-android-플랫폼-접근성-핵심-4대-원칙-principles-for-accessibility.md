# Android 플랫폼 접근성 핵심 4대 원칙 (Principles for Accessibility)

상위 노트: [jetpack-compose-accessibility-guidelines](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/jetpack-compose-accessibility-guidelines.md)

Jetpack Compose API 적용을 넘어, Android OS 레벨에서 일관되게 강조하는 접근성 기획/디자인 핵심 원칙 4가지는 다음과 같습니다.

### 4-1. 텍스트 대비(Color Contrast) 규격 준수
저시력 사용자나 야외 직사광선 환경의 사용자가 글씨를 명확히 읽을 수 있도록 충분한 대비를 확보해야 합니다.
* **대비율 기준**: 
  * 일반 텍스트: 최소 **4.5:1** 이상의 명도 대비율 필요.
  * 큰 텍스트(18pt/24sp 이상 또는 14pt Bold/19sp Bold 이상): 최소 **3.0:1** 이상의 명도 대비율 필요.
* **Compose 최적화**: 디자인 시스템의 테마 컬러를 설정할 때 Material Theme의 Primary/OnPrimary, Surface/OnSurface 쌍을 확실히 가독성이 검증된 조합으로 매핑해야 합니다.

### 4-2. 색상 하나에만 의존한 정보 전달 금지 (Do not rely on color alone)
색약/색맹 사용자가 UI 상태를 정확하게 구분할 수 있도록 설계해야 합니다.
* **잘못된 설계**: 오류가 발생한 입력창 테두리를 단지 "빨간색"으로만 바꾸고 멘트를 추가하지 않는 것.
* **올바른 설계**: 상태를 나타내는 색상 변화와 함께 **경고 아이콘**, **상태 안내 텍스트("올바르지 않은 형식입니다")** 등의 텍스트/도형 힌트를 반드시 병행 제공합니다.

### 4-3. 시스템 글꼴 크기 설정 존중 (Font Scaling)
Android 시스템 설정에서 사용자가 글자 크기를 기본값보다 크게 또는 작게 조절했을 때, 앱의 UI도 유연하게 대응해야 합니다.
* **폰트 크기 단위**: Compose에서 텍스트의 `fontSize`를 정의할 때는 반드시 **`sp`** 단위를 사용해야 합니다 (`dp`를 사용하면 시스템 글꼴 크기 변경에 반응하지 않아 접근성에 저해됩니다).
* **레이아웃 유연성**: 시스템 글꼴이 커질 때 텍스트가 잘리거나 화면을 벗어나지 않도록, `Height` 값을 하드코딩하기보다 `wrapContentHeight()`나 `scroll` 가능한 컨테이너를 적용해야 합니다.

### 4-4. 하드웨어 키보드 및 D-pad 포커스 내비게이션
사용자가 마우스나 터치 스크린이 아닌 하드웨어 키보드, D-pad, 혹은 보조 입력 장치(Switch Access)를 사용하여 탭(Tab) 키로 항목을 이동할 때, 포커스가 논리적이고 순차적으로 이동할 수 있어야 합니다.
* **Compose 제어**: 포커스 이동 흐름을 바꾸려면 `FocusRequester` 및 `Modifier.focusProperties { next = ... }` 등을 사용해 포커스 순서를 수동 조정할 수 있습니다.

---
