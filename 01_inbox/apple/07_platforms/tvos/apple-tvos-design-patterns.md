# tvOS Design Patterns #apple #tvos #design

거실 환경에 맞는 tvOS UI/UX 패턴을 쉽게 정리했다. 용어는 [apple-glossary](../../00_foundations/apple-glossary.md).

## 포커스 중심 내비게이션
- 포커스 엔진이 기본. 포커스 이동 경로를 단순하게 설계하고, 포커스된 항목은 크기/빛/음향으로 명확히 표시.
- 포커스가 사라지거나 모호한 상태가 없도록, 가로/세로 리스트/그리드의 시작/끝 처리를 신경 쓴다.

## 레이아웃
- 큰 화면, 멀리서 보기: 큰 카드/텍스트/버튼. 여백/라인 수를 적당히 유지해 읽기 쉽도록.
- 히어로 영역 + 그리드/리스트 조합이 흔하다. 스크롤 시 상단 고정 메뉴를 제공하면 탐색이 쉽다.

## 검색/입력
- Siri 음성 검색을 적극 제공. 텍스트 입력은 음성/아이폰 키보드/리모컨 제스처 지원.
- 추천/최근 검색/자동 완성으로 입력 부담을 줄인다.

## 미디어 발견
- 카테고리/추천/큐레이션으로 빠르게 콘텐츠를 찾게 한다.
- 미리보기 자동 재생은 선택적으로, 소리/자막/데이터 사용을 고려해 토글 제공.

## 애니메이션/피드백
- 포커스 이동/선택 시 부드러운 스케일/패럴랙스. 과한 회전/깜빡임은 피한다.
- 햅틱 대신 사운드/시각 피드백을 사용.

## 다중 사용자
- 다중 사용자 프로필 지원 시 빠른 전환 UI 제공. 추천/시청 기록을 분리.

## 접근성
- 자막/오디오 설명, 색 대비, Reduce Motion, VoiceOver/Zoom을 지원.
- 리모컨 제스처를 사용하지 못할 때를 대비해 방향키 입력도 매핑.

## 성능/네트워크
- 이미지/비디오 프리로드, 적응형 비트레이트. 버퍼링 상태를 명확히 표시.
- On-Demand Resources로 초기 앱 크기를 줄이고, 백그라운드에서 필요한 리소스를 내려받는다.

## 링크
[apple-tvos-media](apple-tvos-media.md), [apple-animation-and-motion](../../../../../../../apple-animation-and-motion.md), [apple-network-basics](../../../../../../../apple-network-basics.md), [apple-accessibility-and-internationalization](../../02_ui_frameworks/apple-accessibility-and-internationalization.md).
