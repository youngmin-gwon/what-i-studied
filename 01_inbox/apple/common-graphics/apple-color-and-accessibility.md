# Color, Text, and Accessibility (공통) #apple #ui #accessibility #graphics

색/텍스트/가독성을 맞추는 방법을 쉽게 정리했다. 용어는 [[apple-glossary]].

## 색상
- 시스템 색상(Semantic Colors)을 사용하면 라이트/다크 모드에서 자동 조정.
- 대비: WCAG 가이드라인(일반 텍스트 4.5:1 권장). 투명도/블러 남용 금지.
- HDR/SDR: visionOS/iPhone Pro 등은 HDR 표시 가능. 과한 밝기/채도는 피로를 줄 수 있음.
- 색약/고대비 모드: 색만으로 상태를 표시하지 말고 아이콘/텍스트도 사용.

## 텍스트
- Dynamic Type 지원: SwiftUI 기본, UIKit에서는 Auto Layout/단위 폰트 사용.
- 지역화: 길이가 늘어도 줄바꿈/압축이 되도록. RTL도 확인.
- 시스템 폰트(SF) 사용 시 가독성이 좋고, 굵기/크기/가변 폰트 지원.

## 아이콘/이미지
- SF Symbols: 자동 크기 조절/다크 모드 대응/가변 굵기.
- 벡터/멀티 해상도 자산 준비. 메모리/대역폭 절약.
- 시각적 일관성: 여백/라인 두께/모서리 반경을 통일.

## 애니메이션과 편안함
- Reduce Motion 설정을 존중해 과한 패럴랙스/스케일 애니메이션을 줄인다.
- 손/시선 입력(visionOS)/포인터(iPadOS)에서 포커스/상호작용을 명확히.
- watchOS는 작은 화면이므로 큰 전환보다 단순 페이드/슬라이드 권장.

## 접근성
- VoiceOver/Voice Control: 커스텀 컨트롤에 라벨/힌트/값 제공.
- 히트 영역: 최소 44x44pt(워치 40x40pt). 손/포인터/시선 모두에 충분한 크기.
- Focus 이동: 키보드/리모컨/포인터/시선 입력에서 자연스럽게 흐르도록 순서 설정.

## 테스트 체크리스트
- 다크/라이트, High Contrast, Reduce Motion, 큰 글자, RTL, 여러 언어.
- HDR/SDR 디스플레이, ProMotion vs 60Hz.
- 컬러만으로 상태를 구분하지 않았는지 확인.

## 성능/전력
- 불필요한 레이어 효과(블러/그림자/마스크) 줄이기.
- 이미지 디코딩/리사이즈를 백그라운드에서 처리.

## 링크
[[apple-ui-performance-guide]], [[apple-accessibility-and-internationalization]], [[apple-rendering-and-media]], [[apple-performance-and-debug]].
