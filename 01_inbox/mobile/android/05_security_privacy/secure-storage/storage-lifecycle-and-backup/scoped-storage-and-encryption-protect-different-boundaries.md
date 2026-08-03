---
title: scoped-storage-and-encryption-protect-different-boundaries
tags: ["android", "android/security-privacy"]
aliases: []
date modified: 2026-08-03 18:14:41 +09:00
date created: 2026-07-31 17:04:40 +09:00
---

## Scoped Storage 와 암호화가 나누는 서로 다른 개인정보 경계

상위 문서: [저장소 수명과 백업 경계](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/storage-lifecycle-and-backup.md)

관련 노트: [Scoped Storage는 공유 저장소 직접 접근을 제한한다](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/scoped-storage-limits-direct-shared-storage-access.md), [Android 민감 데이터는 암호화와 키 소유권을 함께 설계한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/sensitive-data-requires-encryption-and-key-ownership.md)

### 한 문장 정의

Scoped Storage 는 누가 파일에 접근할 수 있는지를 제한하고, 암호화는 저장 매체에서 파일 내용을 읽기 어렵게 한다.

둘은 서로 대체 관계가 아니라 접근 주체와 데이터 노출 시점을 나누는 별개의 방어선이다.

### Scoped Storage 의 경계

- 앱 전용 디렉터리는 다른 앱의 일반적인 파일 접근에서 분리된다.
- 공유 미디어는 MediaStore 를 통해 유형과 소유권을 드러낸다.
- 사용자가 선택한 문서는 Storage Access Framework 가 접근 권한을 중개한다.
- 다른 앱의 샌드박스를 경로 문자열만으로 읽을 수 있다고 가정하지 않는다.
- 전체 공유 저장소 권한을 요구하는 설계는 필요한 파일 범위와 다시 비교한다.

Scoped Storage 는 파일의 위치와 API 접근 경로를 통제한다.

그 자체가 파일 내용을 암호화하거나 앱 프로세스의 평문 노출을 막지는 않는다.

### 암호화의 경계

FBE 는 저장 장치에 기록된 파일을 사용자 또는 기기 자격 증명과 연결한다.

CE 파일은 사용자 잠금 해제 뒤에 접근 가능하고, DE 파일은 부팅 직후 접근 가능하다.

파일이 앱 전용 영역에 있어도 잠금 해제 후 앱은 파일 내용을 읽는다.

화면, 로그, 분석 이벤트, 클립보드로 평문이 복제되면 저장 암호화만으로는 충분하지 않다.

추가 애플리케이션 암호화가 필요하면 키를 [Android Keystore](https://developer.android.com/privacy-and-security/keystore) 에 보관한다.

### 결합해서 적용하기

사용자 비밀 문서는 앱 전용 CE 영역에 저장하고, 필요하면 Keystore 키로 내용도 암호화한다.

사용자에게 내보내는 문서는 공유 저장소 또는 SAF 를 통해 명시적인 사용자 선택으로 이동시킨다.

내보낸 파일은 앱 샌드박스의 FBE 경계와 동일하지 않으므로 별도 파일 암호화나 공유 경고를 검토한다.

민감한 부팅 설정은 DE 에 두지 않고, 정말 필요한 비밀이 아닌 식별자나 실행 플래그만 둔다.

### 데이터 흐름 점검

파일이 생성되는 위치와 읽는 API 를 먼저 기록한다.

그 다음 잠금 상태, 다른 앱, 백업 시스템, 서버 동기화가 각각 무엇을 볼 수 있는지 표시한다.

암호화 전 평문이 임시 파일, 캐시, 로그에 복제되는 경로를 찾는다.

공유 저장소에 기록되는 파일은 사용자 의도와 파일 수명을 함께 정의한다.

### 점검 질문

- 이 경계는 접근 통제인가, 저장 암호화인가, 아니면 둘 다 필요한가?
- CE 와 DE 중 어느 시점에 데이터가 노출되어야 하는가?
- 파일 선택과 공유 과정에서 사용자 승인이 분명한가?
- 암호화 키와 암호문이 같은 백업 경계에 놓이지 않는가?
- 평문 사본이 캐시와 로그에 남지 않는가?
