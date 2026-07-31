# Android app sandbox는 UID와 프로세스 경계로 앱을 격리한다

Android app sandbox는 각 앱을 별도 Linux UID와 프로세스 경계 안에 둔다. 기본 상태에서 앱은 다른 앱의 private data directory, process memory, file descriptor에 직접 접근할 수 없다.

앱 간 협력은 직접 파일 접근이 아니라 Binder IPC, Intent, ContentProvider, permission 같은 명시적 경계를 통해 일어난다. 그래서 exported component, URI permission, signature permission 같은 설정은 sandbox를 안전하게 여는 문이 된다.

sandbox는 앱 데이터의 기본 격리 계층이지만 암호화나 서버 권한 검사를 대체하지 않는다. 같은 UID 안의 코드, backup, rooted/debug 환경, 사용자가 승인한 외부 공유 경계는 별도로 설계해야 한다.

관련 노트: [Permission protection level은 접근 승인 주체를 정의한다](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/permission-protection-level-defines-who-can-grant-access.md)
