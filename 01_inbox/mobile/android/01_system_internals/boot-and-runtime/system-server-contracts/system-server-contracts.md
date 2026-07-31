# system_server와 ActivityManager 계약

`system_server`는 framework service를 시작하고, ActivityManager 계층은 앱 process, component lifecycle, task, ANR, memory pressure 대응을 조율한다.

## 정본 노트
- [system_server는 framework service를 한 프로세스 안에서 시작한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-starts-framework-services-in-one-process.md)
- [system service는 Binder endpoint이자 플랫폼 정책 집행자다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-service-is-binder-endpoint-and-platform-policy-enforcer.md)
- [AMS는 앱 프로세스와 컴포넌트 lifecycle을 조율한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/ams-coordinates-app-process-and-component-lifecycle.md)
- [ATMS는 activity, task, back stack 전이를 담당한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/atms-owns-activity-task-and-back-stack-transitions.md)
- [프로세스 우선순위는 메모리 회수 정책 입력이지 앱 상태의 진실이 아니다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/process-priority-is-memory-reclaim-policy-input-not-app-state-truth.md)
- [ANR은 단일 timeout 숫자가 아니라 responsiveness 계약 위반이다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/anr-is-responsiveness-contract-violation-not-single-timeout.md)
- [Rescue Party는 반복되는 system failure를 단계적으로 복구한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/rescue-party-recovers-repeated-system-failures-in-stages.md)
- [dumpsys는 system service의 현재 상태를 보는 inspection interface다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/dumpsys-is-system-service-state-inspection-interface.md)
