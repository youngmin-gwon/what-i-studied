# init rc 언어는 actions, services, options, imports를 선언한다

상위 문서: [init와 네이티브 서비스 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-service-contracts.md)

Android init language는 shell script가 아니다. `.rc` 파일은 actions, commands, services, options, imports를 줄 단위로 선언하고, `init` parser가 이를 boot action queue와 service table로 해석한다.

## 실무 규칙

- `/system/etc/init/`은 core system 항목, `/vendor/etc/init/`은 SoC/vendor daemon, `/odm/etc/init/`은 ODM 항목에 둔다.
- service 이름은 유일해야 하며 중복 정의는 무시되고 로그에 오류가 남는다.
- section 밖 command나 option은 의미가 없으므로 parser 오류와 boot log를 반드시 확인한다.
- property expansion은 `${property.name}` 형식이며 import path에도 쓰일 수 있다.

## 관련 문서

- [init trigger는 event와 property 조건을 결합하는 실행 gate다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-triggers-are-event-and-property-gates.md)
- [init service는 재시작 정책을 가진 supervised process다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-service-is-supervised-process-with-explicit-lifecycle.md)

공식 문서: [Android Init Language](https://android.googlesource.com/platform/system/core/+/master/init/README.md)
