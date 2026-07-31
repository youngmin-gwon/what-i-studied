# APEX activation은 boot-time mount, version selection, rollback 경계다

APEX update는 설치 즉시 running system을 임의로 바꾸는 모델이 아니다. updated APEX는 기존 built-in package를 shadow할 수 있고, activation은 boot 과정에서 apexd가 version을 선택하고 mount하면서 이루어진다.

Mainline module update는 필요한 module 묶음이 원자적으로 적용되거나 rollback될 수 있어야 한다. 일부만 적용되어 system component set이 어긋나는 상태를 피하는 것이 핵심이다.

Compressed APEX는 업데이트 후 built-in APEX가 차지하는 저장 공간 문제를 줄이기 위한 포맷이다. 성능 최적화 포맷이라기보다 system partition과 `/data` update copy 사이의 storage tradeoff를 다루는 장치다.

관련 노트: [APEX package 경계](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apex-packages-lower-level-system-modules-that-apk-cannot-model-well.md), [boot/runtime 정본](01_inbox/mobile/android/01_system_internals/boot-and-runtime/android-boot-and-runtime.md), [platform-modularity hub](01_inbox/mobile/android/01_system_internals/platform-modularity/android-platform-modularity.md).

공식 문서: [APEX file format](https://source.android.com/docs/core/ota/apex)
