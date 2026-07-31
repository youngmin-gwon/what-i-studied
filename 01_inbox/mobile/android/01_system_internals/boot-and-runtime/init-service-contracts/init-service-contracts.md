# init와 네이티브 서비스 계약

`init`은 Android userspace의 첫 프로세스이며, `.rc` 선언을 읽어 파일시스템, property, SELinux, native daemon, Zygote 시작 순서를 조율한다.

## 정본 노트
- [init는 PID 1이자 Android userspace의 부트스트랩 정책 엔진이다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-is-pid1-and-userspace-bootstrap-policy-engine.md)
- [First stage init은 second stage가 읽을 최소 파일시스템을 만든다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/first-stage-init-builds-minimal-filesystem-for-second-stage.md)
- [init rc 언어는 actions, services, options, imports를 선언한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-rc-language-declares-actions-services-options-and-imports.md)
- [init trigger는 event와 property 조건을 결합하는 실행 gate다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-triggers-are-event-and-property-gates.md)
- [init service는 재시작 정책을 가진 supervised process다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-service-is-supervised-process-with-explicit-lifecycle.md)
- [service option은 identity, resource, class, socket 계약을 고정한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/service-options-fix-identity-resource-class-and-socket-contracts.md)
- [property service는 전역 상태 저장소이자 제한된 제어 plane이다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/property-service-is-global-state-store-and-restricted-control-plane.md)
- [ueventd는 kernel uevent를 dev node 권한으로 변환한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/ueventd-turns-kernel-uevents-into-dev-node-permissions.md)
- [fstab은 mount와 검증 플래그를 묶은 부팅 계약이다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/fstab-is-boot-time-mount-and-verification-contract.md)
- [init 보안은 SELinux domain과 capability 경계로 정의된다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-security-is-selinux-domain-and-capability-boundary.md)
- [init 디버깅은 로그, property, service 상태를 함께 본다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-debugging-uses-logs-properties-and-service-state.md)
