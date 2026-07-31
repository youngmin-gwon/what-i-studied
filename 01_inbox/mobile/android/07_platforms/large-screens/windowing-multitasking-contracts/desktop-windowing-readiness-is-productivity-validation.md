# 데스크톱 윈도잉 준비도는 작은 화면 호환성이 아니라 생산성 검증이다

상위 문서: [데스크톱 윈도잉과 멀티태스킹 계약](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/windowing-multitasking-contracts.md)

데스크톱 윈도잉 대응은 phone UI가 깨지지 않는 수준에서 끝나지 않는다. 사용자가 키보드, 포인터, 여러 창, 넓은 정보 공간을 사용해 더 빠르게 작업할 수 있는지 검증해야 한다.

## 체크 기준

- 창을 매우 좁게, 매우 넓게, 낮은 height로 바꿔도 핵심 과업이 유지된다.
- list-detail, supporting pane, 도구 패널처럼 넓은 창에서 정보 구조가 좋아진다.
- keyboard shortcut, right click, hover, drag-drop 같은 생산성 입력이 중요한 명령에 연결된다.
- 여러 instance에서 같은 데이터가 열릴 때 저장, 충돌, focus, notification routing이 예측 가능하다.
- Play large screen quality와 ChromeOS/desktop 테스트를 release checklist에 포함한다.

## 관련 문서

- [적응형 앱 준비도는 창, posture, 입력 테스트로 판단한다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/adaptive-app-readiness-requires-window-posture-input-testing.md)
- [테스트와 품질 계약](01_inbox/mobile/android/06_testing_performance/testing/testing-quality-contracts/testing-quality-contracts.md)
