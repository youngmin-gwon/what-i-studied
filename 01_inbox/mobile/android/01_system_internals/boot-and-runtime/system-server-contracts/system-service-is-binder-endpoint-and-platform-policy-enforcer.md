# system service는 Binder endpoint이자 플랫폼 정책 집행자다

상위 문서: [system_server와 ActivityManager 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md)

system service는 앱에 API를 노출하는 Binder endpoint인 동시에 권한, user/profile, process state, background restriction, device policy 같은 플랫폼 규칙을 집행한다. 그래서 앱 API 호출 실패를 볼 때는 public API뿐 아니라 system service가 어떤 정책 상태를 보고 거절했는지도 봐야 한다.

## 판단 기준

- Binder transaction은 기능 호출 경로이고, service 내부 정책은 허용 여부와 부작용을 결정한다.
- permission check, app op, foreground/background 상태, user restriction은 service마다 다르게 적용될 수 있다.
- framework service는 native daemon, HAL, kernel interface와 다시 연결되므로 한 계층의 로그만으로 결론을 내리지 않는다.
- service state는 `dumpsys`로 보고, 호출 흐름은 logcat, trace, Binder 관찰 지점과 함께 본다.

## 관련 문서

- [Android Binder와 IPC](01_inbox/mobile/android/01_system_internals/ipc-and-process/android-binder-and-ipc.md)
- [dumpsys는 system service의 현재 상태를 보는 inspection interface다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/dumpsys-is-system-service-state-inspection-interface.md)
- [Android 보안 샌드박스](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/android-security-sandbox.md)
