# Interprocess & XPC #apple #xpc #ipc

앱/시스템이 서로 대화하는 방법을 쉬운 말로 정리했다. 용어는 [[apple-glossary]].

## 왜 IPC가 필요한가
- 샌드박스 때문에 직접 메모리를 공유하지 못한다. 대신 메시지를 주고받아 기능을 나눈다.
- 민감 작업은 별도 데몬이 맡고, 앱은 요청만 한다(예: 네트워크, 푸시, 파일 접근 일부).

## XPC 기본
- 딕셔너리/바이너리 형태의 메시지를 보내고 받는 단순 IPC.
- 연결은 이름(서비스 번들 아이디) 또는 Mach 서비스로 만든다.
- 서비스는 별도 프로세스로, 크래시해도 메인 앱을 끌어내리지 않는다.

## Extension과 XPC
- 공유 시트, 위젯, 인텐트, Safari 확장 등은 모두 .appex이며 XPC로 주 앱과 통신한다.
- 데이터는 Encodable/Decodable 또는 NSCoding으로 직렬화해 전달.

## 보안
- 코드 서명/[[apple-glossary#Entitlement|Entitlement]]로 “누가 누구에게 연결 가능한지”가 정해진다.
- Audit token/UID/PID가 함께 전달되어 권한을 확인한다.

## 성능과 주의점
- 큰 데이터는 파일로 공유하고, XPC 메시지에는 경로나 토큰만 넣는다.
- 연결 끊김/재시작을 처리하는 에러 핸들링이 필수다.
- 백그라운드 제한이 있는 플랫폼(iOS/watchOS)은 서비스가 자주 종료될 수 있다.

## 대안/관련
- [[apple-glossary#Grand Central Dispatch(GCD)|GCD]]는 프로세스 내 작업 분배용.
- [[apple-glossary#Run Loop|Run Loop]]에서 포트 기반 입력을 받을 수도 있다.
- 네트워크 IPC는 URLSession/WebSocket/Bonjour 등으로 해결한다.

## 디버깅
- Console.app에서 XPC 로그 필터링.
- `launchctl print system/user`로 등록된 서비스 확인.
- Instruments System Trace로 프로세스/스레드/XPC 메시지 타임라인 보기.

## 링크
[[apple-sandbox-and-security]], [[apple-architecture-stack]], [[apple-app-lifecycle-and-ui]], [[apple-performance-and-debug]].
