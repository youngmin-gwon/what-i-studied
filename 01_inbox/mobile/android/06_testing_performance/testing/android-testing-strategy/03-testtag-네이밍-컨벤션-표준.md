# `testTag` 네이밍 컨벤션 표준

Now in Android(NiA) 및 공식 가이드라인에 맞춰 UI 트리의 고유성과 자동화 도구 파싱을 고려한 네임스페이스 규칙을 준수합니다.

### 3-1. 표준 명명 구조

$$\text{Format: } \texttt{\{feature-or-screen\}:\{component\}[:\{sub-element-or-id\}]}$$

- **단일 화면/컨테이너**: `signIn:screen`, `dashboard:root`
- **입력 필드 및 버튼**: `signIn:idInput`, `signIn:passwordInput`, `signIn:submitButton`
- **시각적 아이콘/토글**: `signIn:passwordToggle` (텍스트가 없는 아이콘 버튼)
- **동적 리스트(LazyColumn/LazyGrid) 아이템**: `dashboard:item:${item.id}`
- **로딩 및 상태 요소**: `signIn:loadingProgress`

### 3-2. `testTag` 선별적 부여 기준 (코드 오염 방지)

모든 UI 요소에 무분별하게 `testTag`를 부여하면 코드 오염(Pollution)이 발생합니다. 다음 기준을 따릅니다.

1. **태그 필수 부여 대상**:
   - 텍스트가 없는 아이콘 버튼 (비밀번호 눈 모양 토글, 닫기 X 버튼 등)
   - 동적 목록의 개별 셀 (`LazyColumn` 아이템)
   - 입력 필드 및 주요 상호작용 액션 버튼 (i18n 보호 목적)
   - Macrobenchmark / UI Automator로 탐색해야 하는 주요 스크린 루트
2. **태그 생략 대상**:
   - 화면에 고정 노출되는 단순 타이틀, 설명 문구 (`onNodeWithText`로 검증 가능)

---
