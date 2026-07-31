---
title: "드래그 앤 드롭은 창 사이 데이터 이동 계약이다"
tags: ["android", "android/platforms"]
---

# 드래그 앤 드롭은 창 사이 데이터 이동 계약이다

상위 문서: [큰 화면 적응 계약](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md)

큰 화면의 drag and drop은 단순 제스처가 아니라 앱 내부, 앱 간, 창 간 데이터 이동을 허용하는 계약이다. 특히 multi-window와 desktop 환경에서는 사용자가 파일, 이미지, 텍스트, 항목을 창 사이에서 옮길 수 있다고 기대한다.

## 실무 규칙

- 앱이 받을 수 있는 데이터 타입을 MIME type과 UI affordance로 명확히 한다.
- 외부 앱에서 들어온 항목은 권한과 URI 접근 수명을 확인한다.
- 앱 밖으로 내보낼 수 있는 항목은 민감 정보와 공유 범위를 먼저 검토한다.
- drag target은 hover/focus 상태를 명확히 표시하고 실패 이유를 조용히 삼키지 않는다.
- 같은 앱의 여러 window 또는 instance 사이 이동도 별도 시나리오로 테스트한다.

## 관련 문서

- [데스크톱 멀티 인스턴스는 작업 단위와 데이터 소유권을 먼저 정해야 한다](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/multi-instance-requires-task-and-data-ownership-boundaries.md)
- [키보드, 포인터, 스타일러스는 큰 화면의 기본 입력이다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/keyboard-pointer-and-stylus-are-primary-large-screen-inputs.md)

공식 문서: [Input compatibility on large screens](https://developer.android.com/develop/ui/views/touch-and-input/input-compatibility-on-large-screens)
