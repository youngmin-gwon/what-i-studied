# Animation & Motion Patterns #apple #animation #ui #common

애니메이션을 자연스럽고 가볍게 만드는 법을 쉽게 정리했다. 용어는 [[apple-glossary]].

## 왜 애니메이션이 중요할까?
- 상태 변화를 눈에 보이게 해 혼란을 줄인다.
- 방향/맥락을 알려 사용자가 “어디서 어디로” 이동했는지 이해시키는 신호가 된다.
- 지나치면 멀미/피로/배터리 소모가 커진다.

## 기본 원칙
- 목적이 있는 애니메이션만 사용. “멋있어서” 넣지 않는다.
- 짧고 부드럽게: 150~300ms 정도가 일반적. 맥락에 따라 조정.
- 일관된 곡선: 기본 시스템 이징/스프링을 사용해 플랫폼 느낌을 유지.

## 플랫폼 차이
- iOS/iPadOS: 제스처/내비게이션과 조화, 프로모션(120Hz) 고려.
- macOS: 마우스/트랙패드 포인터, 창 전환, Dock/Spaces와 어울리게.
- watchOS: 짧은, 간단한 애니메이션. 햅틱과 함께 사용.
- visionOS: 3D 공간/깊이/시선 입력. 멀미 방지를 위해 급격한 이동/회전 피함.
- tvOS: 포커스 엔진과 함께 강조/확대/패럴랙스.

## SwiftUI
- `withAnimation`/`animation(_:)`으로 상태 기반 애니메이션.
- `matchedGeometryEffect`로 뷰 이동/전환 맥락 제공.
- Transaction/Animation phases를 사용해 복잡한 시퀀스 제어.

## UIKit/AppKit
- UIView.animate/CAAnimation/CABasic/CAKeyframe/CASpring.
- Core Animation 레이어 속성(위치/불투명도/스케일/회전)을 변경해 GPU에서 수행.
- UIViewPropertyAnimator로 상호작용 애니메이션(스크롤/제스처 연동).

## 접근성/편안함
- Reduce Motion 설정을 존중. 대체(페이드/즉시 전환)를 제공.
- 색 번쩍임/빠른 깜빡임 피하기. 시야 밖에서 갑작스러운 요소 등장 금지.
- 시선/손 입력 환경(visionOS)에서는 목표를 크게, 움직임을 예측 가능하게.

## 성능
- 레이어 수/효과 최소화. Offscreen 렌더링을 줄인다.
- 텍스처/이미지 크기를 적절히. 애니메이션 중 데이터/네트워크 작업은 분리.
- Instruments(Core Animation), GPU Frame Capture로 프로파일링.

## 디자인 패턴 예
- 리스트→디테일: 확대/슬라이드/페이드 조합으로 맥락 제공.
- 드래그 앤 드롭: 원본→목적지로 따라가는 미리보기, 스냅/스프링 피드백.
- 진행 상태: 로딩/성공/실패 애니메이션을 짧게, 반복은 최소.

## 테스트 체크
- 다크/라이트, 프로모션/60Hz, Reduce Motion on/off, 저사양 기기.
- 멀티 윈도우/외장 디스플레이/공간 환경에서 자연스러운지.

## 링크
[[apple-ui-performance-guide]], [[apple-color-and-accessibility]], [[apple-rendering-and-media]], [[apple-performance-and-debug]], [[apple-visionos-design-patterns]].
