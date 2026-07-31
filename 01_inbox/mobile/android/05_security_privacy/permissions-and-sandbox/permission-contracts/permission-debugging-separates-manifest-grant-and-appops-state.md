# 권한 디버깅은 manifest, grant state, AppOps를 분리해 확인한다

권한 문제를 디버깅할 때는 manifest 선언, runtime grant state, AppOps 또는 설정 기반 차단을 분리해서 확인한다. 셋 중 하나만 봐서는 실제 API 실패 원인을 알기 어렵다.

manifest에 권한이 없으면 요청 자체가 성립하지 않는다. runtime grant가 없으면 dangerous permission으로 보호된 API는 사용할 수 없다. AppOps나 특수 설정이 꺼져 있으면 권한이 있어도 operation이 막힐 수 있다.

릴리스 전에는 권한 허용, 거부, 영구 거부, 설정에서 회수, OS 자동 회수, 특수 접근 해제 케이스를 대표 기기에서 확인한다.
