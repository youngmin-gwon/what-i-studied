---
title: agent-authorization-boundaries
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-03 18:13:13 +09:00
date created: 2026-07-31 17:42:24 +09:00
---

## Assistant 와 에이전트 호출은 앱 내부 권한 검사를 대체하지 않는다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../android-system-services-and-device-capabilities.md)

관련 지도: [Assistant와 에이전트 통합 계약](./assistant-agent.md)

### 신뢰 경계

외부 호출로 전달되는 음성 해석값, intent extra, URL parameter, 함수 argument 는 모두 신뢰할 수 없는 입력으로 취급한다.

Assistant 가 호출했다는 사실만으로 앱의 도메인 권한이나 사용자의 승인 상태가 충족되었다고 판단하지 않는다.

AppFunctions 의 외부 함수 실행에는 `EXECUTE_APP_FUNCTIONS` 또는 시스템 전용 권한이 필요하다.

이 권한은 일반 앱이 임의로 요청하는 런타임 권한이 아니라 privileged system app 또는 알려진 인증서 앱에 제한된다.

AppFunctionService 는 시스템만 bind 하도록 `BIND_APP_FUNCTION_SERVICE` 로 보호된다.

### 앱에서 반드시 검사할 것

- 입력 형식, 길이, 허용 목록, 소유자와 대상 리소스를 검사한다.
- 현재 로그인 사용자와 작업 대상의 권한을 확인한다.
- 결제·전송·삭제·공개처럼 부작용이 큰 작업은 사용자 확인 또는 재인증을 요구한다.
- 잠금 상태, 계정 상태, 네트워크 요구사항, 데이터 접근 권한을 확인한다.
- 민감한 결과를 함수 설명, 로그, 오류 메시지에 과도하게 포함하지 않는다.
- 재시도 시 중복 실행을 막고 취소와 타임아웃을 정의한다.

### Intent 보안

- 불필요한 Activity, Service, Receiver 를 export 하지 않는다.
- 외부에서 시작되는 Activity 는 `android:exported` 의도를 명시한다.
- 민감한 Service 시작에는 명시적 intent 를 사용한다.
- 필요한 extra 만 복사하고, 값과 flags 를 검증한다.
- 암묵적 intent 에 개인정보·토큰·변경 가능한 객체를 넣지 않는다.
- intent redirection 을 구현한다면 대상 component 와 URI grant flags 를 검증한다.

### 데이터 최소화

에이전트가 작업에 필요한 최소 데이터만 읽고 반환하도록 함수 계약을 좁힌다.

온디바이스 AI 나 AICore 의 존재가 앱의 접근제어를 대신하지 않는다.

앱 자체의 저장소, 네트워크, 계정, 도메인 정책은 별도의 보안 경계로 계속 보호한다.

공식 문서: [Manifest 권한 reference](https://developer.android.com/reference/android/Manifest.permission), [exported component 접근제어](https://developer.android.com/privacy-and-security/risks/access-control-to-exported-components), [intent 보안](https://developer.android.com/guide/components/intents-filters), [intent redirection](https://developer.android.com/privacy-and-security/risks/intent-redirection)

### 권한 설계의 결론

시스템 수준의 호출자 권한은 앱 내부의 리소스 권한을 대체하지 않는다.

예를 들어 메시지 발송 함수는 호출자가 허용된 assistant 인지 확인하는 것만으로 충분하지 않다.

로그인 계정, 수신자 선택, 발송 동의, 앱의 메시지 정책을 모두 별도로 확인해야 한다.

보안 검토에서는 정상 호출뿐 아니라 악의적으로 조작된 parameter 와 재전송을 가정한다.

테스트에는 비로그인 상태, 잠금 상태, 권한 철회 직후, 잘못된 식별자, 중복 요청을 포함한다.

검증일: 2026-08-03. API 36 의 `EXECUTE_APP_FUNCTIONS` 는 `internal|privileged|knownSigner`, `BIND_APP_FUNCTION_SERVICE` 는 `signature` 보호 수준임을 Manifest permission reference 에서 확인했다.
