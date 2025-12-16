# UI Performance Guide (공통) #apple #ui #performance #common

각 플랫폼에서 UI를 부드럽게 만드는 기본기를 쉽게 정리했다. 용어는 [[apple-glossary]].

## 핵심 목표
- 프레임 시간 16ms(60fps) 또는 8ms(120fps) 안에 끝내기.
- 메인 스레드(메인 런루프)를 오래 막지 않기.
- 레이아웃/그리기/애니메이션을 단순화.

## SwiftUI 팁
- 상태 최소화: `@State`/`@StateObject`/`@EnvironmentObject`를 필요한 뷰에만 전달.
- id 안정화: 리스트/ForEach에 안정된 id 제공.
- 조건부 뷰/중첩을 줄이고, ViewBuilder를 단순하게.
- 비싼 작업은 Task/async로 분리, 메인 액터는 UI만.

## UIKit/AppKit 팁
- Auto Layout 제약 최소화, 적은 뷰 계층.
- 셀 재사용(테이블/컬렉션)과 프리패칭 사용.
- 비동기 이미지 디코딩, 적절한 캐시.
- Core Animation 레이어 수/효과(그림자/블러/마스크) 줄이기.

## 애니메이션
- Core Animation/SwiftUI Transactions 사용: GPU로 오프로드.
- 물리 효과는 UIKit Dynamics/SwiftUI `spring` 등 기본 API 활용.
- watchOS/visionOS는 너무 화려한 효과보다 가벼운 애니메이션 권장.

## 텍스처/이미지
- 해상도 맞추기: 기기 scale에 맞는 자산 준비.
- Asset Catalog/Variants를 사용해 메모리를 줄인다.
- SF Symbols로 벡터 아이콘 활용.

## 입력/터치
- 터치/제스처 처리 후 빠르게 반환. 긴 작업은 백그라운드 큐로.
- Debounce/Throttle로 과도한 이벤트 처리 방지.

## ProMotion/가변 주사율
- 필요하면 `preferredFrameRateRange`로 목표 프레임을 낮춰 전력 절약.
- 빠른 스크롤/게임은 높은 프레임, 정적 화면은 낮은 프레임.

## 접근성/다국어
- Dynamic Type로 폰트 크기 변화에 대응, 텍스트 길이 확장 고려.
- 레이아웃이 RTL/큰 글자에서도 잘 동작하는지 확인.

## 측정과 디버깅
- Instruments(Core Animation, Time Profiler, Allocations).
- `UIView.setAnimationsEnabled(false)`로 레이아웃 문제 분리 테스트.
- SwiftUI Previews로 빠른 반복, `os_signpost`로 구간 측정.

## 흔한 병목 사례
- 메인 스레드에서 이미지 디코딩/파일 I/O.
- 큰 JSON 파싱을 동기 수행.
- 과도한 리드/라이팅으로 Run Loop가 돌지 못함.
- 중첩된 LazyVStack/List에 복잡한 뷰(캐싱/프리패치 필요).

## 체크리스트
- 메인 스레드 차단 코드가 있는가? → 비동기/백그라운드로 이동.
- 이미지/데이터는 필요한 만큼만 읽고 그리는가? → 캐시/리사이즈 적용.
- 애니메이션/레이어 효과가 과도한가? → 단순화.
- 프레임 드랍이 보이면 Instruments/Frame Capture로 병목 위치 파악.

## 링크
[[apple-performance-and-debug]], [[apple-rendering-and-media]], [[apple-accessibility-and-internationalization]], [[apple-platform-differences]].
