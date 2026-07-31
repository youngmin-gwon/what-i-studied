# property service는 전역 상태 저장소이자 제한된 제어 plane이다

상위 문서: [init와 네이티브 서비스 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-service-contracts.md)

Android property는 system-wide key-value 상태이며, 단순 환경변수가 아니다. `ro.*`, `persist.*`, `sys.*`, `vendor.*` 같은 namespace와 property context가 읽기/쓰기 권한과 수명을 결정한다.

## 실무 규칙

- `ro.*`는 부팅 중 확정되는 읽기 전용 값으로 취급한다.
- `persist.*`는 재부팅 후에도 남으므로 user data와 정책 영향을 함께 본다.
- `sys.*`는 runtime system state를 표현하지만 임의 앱이 쓸 수 있는 채널이 아니다.
- property write 권한은 SELinux property context로 제한한다.
- property 값에 기능 상태를 숨겨 앱 API처럼 쓰면 versioning과 보안 문제가 생긴다.

## 관련 문서

- [init trigger는 event와 property 조건을 결합하는 실행 gate다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-triggers-are-event-and-property-gates.md)
- [init 보안은 SELinux domain과 capability 경계로 정의된다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-security-is-selinux-domain-and-capability-boundary.md)

공식 문서: [Android Init Language](https://android.googlesource.com/platform/system/core/+/master/init/README.md)
