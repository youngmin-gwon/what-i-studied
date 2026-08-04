---
title: background-restrictions-require-persistent-work-state
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-04 15:00:00 +09:00
date created: 2026-07-31 17:42:24 +09:00
---

## 백그라운드 제한은 작업 상태를 영속적으로 설계하게 만든다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)

관련 지도: [백그라운드 작업 계약](./background-work-contracts.md)

### 핵심 주장

- 백그라운드 앱은 포그라운드 앱보다 실행 시간과 네트워크 사용에서 불리한 조건을 받는다.
- Doze 와 앱 대기 상태는 기기가 유휴 상태일 때 작업과 네트워크를 지연시킬 수 있다.
- 배터리 최적화 예외를 요구하는 것은 일반적인 동기화 문제의 기본 해법이 아니다.
- 앱이 강제 종료되거나 프로세스가 회수되면 메모리에만 둔 작업 상태는 사라진다.
- 재시작되어야 하는 작업은 영속적인 요청과 복구 가능한 상태를 사용해야 한다.
- 백그라운드에서 브로드캐스트를 받았다는 사실은 긴 실행 시간을 제공하지 않는다.
- BroadcastReceiver 의 역할은 이벤트를 받고 짧게 처리하거나 다른 실행 수단으로 넘기는 것이다.
- 네트워크가 끊기거나 앱 프로세스가 재생성되어도 재시도 가능한 작업으로 설계해야 한다.

### 생명주기 설계

- UI 상태와 백그라운드 작업 상태를 같은 메모리 객체에만 저장하지 않는다.
- 작업의 입력은 재실행해도 의미가 유지되도록 식별자와 버전 정보를 포함한다.
- 중복 실행 가능성을 고려해 서버 요청과 로컬 반영을 멱등적으로 만든다.
- 실패 원인을 일시적 오류와 영구적 오류로 나누어 재시도 여부를 결정한다.
- 사용자가 취소할 수 있는 작업은 취소 상태와 실제 중단 시점을 모두 관찰한다.
- 제한된 환경에서는 정확한 완료 시각보다 최종 일관성과 복구 가능성을 우선한다.

### 정책 확인

- Android 버전별 백그라운드 시작 제한은 서비스와 액티비티 시작에 다르게 적용된다.
- target SDK 를 올리면 서비스 타입, 알림 권한, exact alarm 권한 등의 요구가 달라질 수 있다.
- Manifest 선언만으로 실행 권한이나 사용자에게 보이는 정당성이 확보되지는 않는다.
- 플랫폼 정책과 Google Play 정책은 별도로 검토한다.

### 관찰 가능한 상태

- 예약됨, 실행 중, 일시 중단, 재시도 중, 성공, 실패, 취소를 구분한다.
- 시스템이 작업을 지연한 것과 작업 자체가 실패한 것을 같은 상태로 기록하지 않는다.
- 사용자가 앱을 다시 열었을 때 마지막 상태와 다음 실행 가능 조건을 보여준다.
- 로그에는 작업 식별자와 시도 횟수만 남기고 민감한 입력 데이터는 남기지 않는다.
- 기기 제조사별 전원 관리가 강한 환경에서는 실제 기기 검증을 추가한다.
- 제한을 없애기 위해 배터리 최적화 예외를 기본 요청하면 안 된다.
- 실행 실패를 재현할 수 있도록 네트워크와 전원 상태를 테스트에서 제어한다.
- 상태 전이는 관찰 가능해야 하며 임의의 백그라운드 스레드에 숨겨서는 안 된다.

Doze 는 개발 중에 강제로 재현할 수 있다. 기기를 USB 에서 분리한 것처럼 만든 뒤 idle 상태로 강제 전환한다.

```sh
adb shell dumpsys battery unplug
adb shell dumpsys deviceidle force-idle
```

이 상태에서 네트워크 요청과 예약된 작업이 지연되는지 확인하고, 테스트가 끝나면 `adb shell dumpsys battery reset` 으로 원래 배터리 상태 보고로 되돌린다. 메모리에만 상태를 둔 구현은 이 구간에서 프로세스가 회수되면 작업 진행 상황을 잃는다.

### 공식 문서

- [백그라운드 실행 제한](https://developer.android.com/about/versions/oreo/background)
- [Doze 및 앱 대기](https://developer.android.com/training/monitoring-device-state/doze-standby)
- [BroadcastReceiver](https://developer.android.com/develop/background-work/background-tasks/broadcasts)
