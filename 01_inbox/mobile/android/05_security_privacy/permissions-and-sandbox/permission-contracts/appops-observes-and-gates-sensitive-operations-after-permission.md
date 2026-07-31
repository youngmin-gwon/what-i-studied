# AppOps는 권한 이후의 민감 작업 실행 상태를 관찰하고 제어한다

AppOps는 permission과 별개로 특정 민감 operation의 실제 사용 상태를 기록하거나 제한하는 Android 내부 제어 계층이다. 권한이 허용되어도 operation이 정책, 사용자 설정, privacy dashboard, 자동 회수 상태에 의해 제한될 수 있다.

권한 디버깅에서 manifest와 runtime grant만 확인하면 부족하다. 카메라, 마이크, 위치처럼 민감한 operation은 시스템 UI의 privacy indicator, dashboard, AppOps 상태와 함께 봐야 한다.

앱 설계 관점에서 AppOps는 "권한을 받았으니 항상 가능하다"는 가정을 깨는 계층이다. 민감 API 호출 직전마다 현재 상태를 확인하고 실패를 정상 경로로 처리한다.
