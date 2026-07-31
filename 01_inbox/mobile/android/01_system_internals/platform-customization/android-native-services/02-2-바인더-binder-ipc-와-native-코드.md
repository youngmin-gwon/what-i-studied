# 🧪 2. 바인더(Binder) IPC 와 Native 코드

프레임워크(Java/Kotlin)에서 Native 서비스를 호출하는 과정:

1. **ServiceManager**: 모든 시스템 서비스의 이름과 위치를 관리하는 허브.
2. **BpInterface / BnInterface**:
   - **Bp (Binder Proxy)**: 클라이언트 측 프록시 (Framework 에서 호출).
   - **Bn (Binder Native)**: 실제 서비스 구현체 (Native 서비스 프로세스 내부).
3. **AIDL for Native**: C++ 에서도 서비스 인터페이스를 정의하기 위해 AIDL 을 사용합니다. (최신 버전은 NDK Backend 지원)

---
