# service option은 identity, resource, class, socket 계약을 고정한다

상위 문서: [init와 네이티브 서비스 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-service-contracts.md)

service option은 init service의 실행 사용자, 그룹, SELinux domain, capability, priority, class, socket, file descriptor, restart 동작을 고정한다. 이는 편의 설정이 아니라 서비스의 권한과 부팅 순서를 결정하는 계약이다.

## 실무 규칙

- `user`, `group`, `seclabel`, `capabilities`는 최소 권한 원칙으로 정한다.
- `class`는 `core`, `main`, `late_start`처럼 부팅 단계와 의존성을 드러내야 한다.
- `socket` option은 `/dev/socket/<name>` 생성과 권한을 init이 관리하게 한다.
- `task_profiles`, `ioprio`, `priority`, `rlimit`은 성능 문제가 아니라 resource isolation 정책으로 본다.

## 관련 문서

- [init 보안은 SELinux domain과 capability 경계로 정의된다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-security-is-selinux-domain-and-capability-boundary.md)
- [Zygote socket은 system_server가 앱 프로세스를 요청하는 factory interface다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-socket-is-system-server-process-factory-interface.md)
