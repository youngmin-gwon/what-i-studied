# Android Keystore 시스템 아키텍처

- **하드웨어 격리**: 키는 **TEE(Trusted Execution Environment)** 또는 **StrongBox(보안 칩)** 내부에서 생성 및 관리되며, 운영체제(Android)로 키 원본이 유출되지 않습니다.
- **Keymaster / KeyMint**: 하드웨어 측에서 암호화 연산을 수행하는 인터페이스입니다.
