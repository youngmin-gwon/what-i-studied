# FBE에서 CE와 DE를 나누는 저장소 경계

상위 문서: [저장소 수명과 백업 경계](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/storage-lifecycle-and-backup.md)
관련 정본: [Android 민감 데이터는 암호화와 키 소유권을 함께 설계한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/sensitive-data-requires-encryption-and-key-ownership.md)


## 한 문장 정의

File-Based Encryption(FBE)은 파일을 암호화하는 동시에 사용자 인증 전후의 접근 시점을 나눈다.

CE와 DE의 선택은 암호화 강도보다 앱 기능이 필요한 부팅 시점을 먼저 결정하는 문제다.

## 핵심 구분

- CE는 Credential Encrypted 저장소다.
- 사용자가 기기 잠금을 해제한 뒤에 접근할 수 있다.
- 대부분의 앱 파일, 데이터베이스, 사용자별 민감 데이터가 기본적으로 CE에 놓인다.
- DE는 Device Encrypted 저장소다.
- 기기 부팅 직후, 사용자가 아직 잠금을 풀기 전에도 접근할 수 있다.
- 알람 예약 정보처럼 부팅 직후 동작에 정말 필요한 최소 데이터만 DE에 둔다.

## 기본 선택 규칙

앱 데이터는 먼저 CE를 기본값으로 삼는다.

잠금 해제 전에도 반드시 실행되어야 하는 기능이 있을 때만 DE를 검토한다.

DE에 둔다는 사실이 데이터를 공개 저장소에 둔다는 뜻은 아니다.

DE도 앱의 보호된 저장소 영역이지만, 사용자 인증 전 접근 가능 시간이 더 길다.

따라서 DE에는 토큰, 개인 기록, 메시지 본문, 복호화 키를 넣지 않는다.

## 구현 경계

```kotlin
val deContext = context.createDeviceProtectedStorageContext()
val bootConfig = File(deContext.filesDir, "boot_config.json")
```

일반 `context.filesDir`는 CE 영역을 가리키는 것으로 취급한다.

DE를 사용하는 컴포넌트는 해당 `Context`를 명시적으로 전달받아야 한다.

CE와 DE 파일을 같은 Repository에서 무심코 섞으면 수명과 접근 조건이 흐려진다.

DE 데이터베이스를 열 때는 사용하는 라이브러리와 초기화 순서가 Direct Boot 조건을 만족하는지 확인한다.

## 보안 판단

FBE는 저장 매체에서 파일 내용을 보호하지만, 앱의 접근 제어 정책을 대신하지 않는다.

파일이 CE에 있어도 앱 프로세스가 잠금 해제 뒤 평문을 로그에 남기면 보호가 무너진다.

추가 암호화가 필요하면 키를 파일 옆에 두지 말고 [Android Keystore](https://developer.android.com/privacy-and-security/keystore)에 맡긴다.

Keystore 키와 암호문 파일의 수명, 백업 여부, 복원 가능성을 별도로 설계한다.

## 점검 질문

- 이 데이터는 잠금 해제 전에 반드시 필요한가?
- DE에 남아도 되는 최소 정보인가?
- DE 데이터가 CE 데이터의 식별자나 민감 내용을 추론하게 하지 않는가?
- 재부팅 직후 해당 파일을 읽는 코드가 실제로 존재하는가?
- 사용자가 잠금을 풀기 전 실패해도 기능이 안전하게 제한되는가?
