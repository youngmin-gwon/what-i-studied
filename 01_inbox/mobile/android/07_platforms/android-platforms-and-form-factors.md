# Android 폼 팩터와 플랫폼 확장 지도

Android 앱은 더 이상 단일 휴대폰 화면만 대상으로 하지 않는다. 이 지도는 큰 화면, 폴더블, 데스크톱 윈도잉, XR처럼 앱 창과 입력 환경이 바뀌는 플랫폼 표면을 세 묶음으로 나눈다.

## 정본 노트
- [큰 화면 적응 계약](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md)
- [데스크톱 윈도잉과 멀티태스킹 계약](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/windowing-multitasking-contracts.md)
- [Android XR 계약](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md)

## 판단 순서

1. 먼저 기기 이름이 아니라 현재 앱 창의 크기와 비율을 본다.
2. 폴더블에서는 hinge, posture, display feature가 레이아웃을 나누는지 확인한다.
3. 데스크톱 윈도잉에서는 창 크기 변경, caption bar, 여러 작업 인스턴스를 검증한다.
4. XR에서는 2D 앱을 띄우는 것과 공간 UI를 설계하는 것을 분리한다.
5. 모든 폼 팩터에서 터치 외 입력과 접근성 경로를 테스트한다.
