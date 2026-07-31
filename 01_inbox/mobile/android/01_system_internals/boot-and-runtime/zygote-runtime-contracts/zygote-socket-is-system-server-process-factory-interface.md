# Zygote socket은 system_server가 앱 프로세스를 요청하는 factory interface다

상위 문서: [Zygote와 ART 런타임 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-runtime-contracts.md)

Zygote는 임의 앱이 직접 호출하는 API가 아니다. `system_server`의 ActivityManager 계층이 Unix domain socket으로 Zygote에 fork와 specialization을 요청하고, Zygote는 새 process의 UID, GID, capability, runtime args를 설정한다.

## 판단 기준

- Zygote socket 권한은 init rc의 `socket` option과 SELinux 정책으로 보호된다.
- USAP pool이 활성화된 기기에서는 일부 앱 프로세스 준비 비용을 미리 지불할 수 있다.
- fork 요청 경로는 Binder 호출과 다르며, 앱 process가 뜬 뒤 framework attach가 이어진다.
- Zygote crash는 앱 프로세스 전반과 system service 안정성에 큰 영향을 준다.

## 관련 문서

- [AMS는 앱 프로세스와 컴포넌트 lifecycle을 조율한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/ams-coordinates-app-process-and-component-lifecycle.md)
- [service option은 identity, resource, class, socket 계약을 고정한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/service-options-fix-identity-resource-class-and-socket-contracts.md)

공식 문서: [About the Zygote processes](https://source.android.com/docs/core/runtime/zygote)
