# 런타임 디버깅은 profile, compile filter, JIT 상태를 분리해서 본다

상위 문서: [Zygote와 ART 런타임 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-runtime-contracts.md)

앱 실행 성능을 볼 때 ART 상태를 하나의 흑상자로 취급하면 원인을 놓친다. profile 데이터가 있는지, 어떤 compile filter로 컴파일됐는지, JIT가 켜져 있는지, compiled artifact가 남아 있는지 분리해서 확인해야 한다.

## 점검 기준

- `cmd package compile`로 profile 기반 또는 full compilation 상태를 재현한다.
- Android 14 이상에서는 local profile clear와 compiled code reset의 차이를 구분한다.
- JIT logging이나 JIT disable은 개발/디버깅 조건에서만 사용한다.
- startup benchmark는 profile 설치 전후, clear 후, force compile 후를 따로 측정한다.

## 관련 문서

- [Macrobenchmark는 실제 디바이스에서 사용자 시나리오의 성능 회귀를 수치로 검증한다](01_inbox/mobile/android/06_testing_performance/performance/benchmark-baseline-contracts/macrobenchmark-measures-real-user-journeys.md)
- [Profile guided compilation은 설치, 실행, idle compile 비용을 나눈다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/profile-guided-compilation-splits-install-runtime-and-idle-costs.md)

공식 문서: [Implement ART JIT compiler](https://source.android.com/docs/core/runtime/jit-compiler)
