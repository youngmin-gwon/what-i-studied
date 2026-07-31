# Verified Boot는 기기 소프트웨어의 chain of trust를 만든다

Verified Boot는 bootloader, kernel, system partition 같은 기기 소프트웨어가 신뢰된 서명과 해시 체인을 따라 로드되었는지 확인한다. Android Verified Boot는 부팅 과정과 dm-verity 기반 검증으로 시스템 변조를 탐지한다.

앱 관점에서 Verified Boot는 앱 내부 보안 로직이 아니라 기기 신뢰도의 바탕이다. Play Integrity 같은 attestation 결과는 이 기기 상태를 포함한 신호를 서버가 판단할 수 있게 해준다.

Verified Boot가 앱의 authorization을 대신하지는 않는다. 기기가 green state에 가깝더라도 사용자의 서버 권한, 세션, 거래 위험은 별도로 검증해야 한다.

공식 문서: [Verified Boot](https://source.android.com/docs/security/features/verifiedboot)
