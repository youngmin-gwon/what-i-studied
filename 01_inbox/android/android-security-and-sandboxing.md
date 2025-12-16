# Security & Sandboxing #android #android/security #android/sandbox

안드로이드가 사용자 데이터를 지키는 기본 규칙을 쉽게 정리했다. 모르는 단어는 [[android-glossary]].

## 기본 원칙
- 앱마다 [[android-glossary#uid|UID]]와 [[android-glossary#selinux|SELinux]] 도메인을 따로 둔다. 그래서 서로의 파일을 바로 만질 수 없다.
- 민감한 기능(카메라, 마이크, 위치 등)은 [[android-glossary#permission|권한]]을 받아야 쓸 수 있다.
- 시스템 서비스가 [[android-glossary#binder|Binder]] 호출을 받을 때마다 권한과 [[android-glossary#appops|AppOps]]로 확인한다.

## SELinux
- “누가 어떤 파일·소켓·Binder를 만질 수 있는가?”를 규칙으로 적어두고 강제로 지킨다.
- 허용되지 않은 접근은 `avc: denied`로 기록된다.

## 권한과 AppOps
- 위험 권한은 실행 중에 사용자에게 묻는다. 한 번만 허락하는 옵션도 있다.
- AppOps는 언제 사용됐는지 기록하고, 포그라운드일 때만 허용하는 식으로 더 세밀하게 조정한다.

## 저장소와 데이터
- [[android-glossary#scoped-storage|Scoped Storage]]로 외부 저장소를 앱별로 나눈다.
- [[android-glossary#fbe|파일 기반 암호화]]로 사용자 잠금과 연동해 데이터를 보호한다.
- [[android-glossary#rro|ContentProvider/SAF]] URI 권한으로 공유 범위를 제한한다.

## 네트워크 보안
- 기본은 TLS. 평문 통신은 Network Security Config로 따로 허용해야 한다.
- Private DNS(DoT)를 기본값으로, per-app 방화벽 규칙으로 차단이 가능하다.
- VPN/Work profile로 트래픽을 분리할 수 있다.

## 실행 시 보호
- [[android-glossary#verified-boot|Verified Boot]]로 부팅 파일이 변조되지 않았는지 본다.
- Play Integrity/SafetyNet으로 기기 상태를 점검해 앱이 대응하게 한다.
- 키는 Keystore/StrongBox에 저장해 밖으로 나오지 않게 한다.

## 개발자가 주의할 점
- Exported 컴포넌트는 명확히 선언하고, 필요한 경우 권한을 건다.
- PendingIntent는 immutable 기본값을 쓰고, 꼭 바꿔야 할 때만 mutable로 둔다.
- 로그에 개인정보를 남기지 말고, Clipboard/Notification 접근은 사용자에게 투명하게 알린다.

## 링크
[[android-activity-manager-and-system-services]], [[android-adb-and-images]], [[android-evolution-history]].
