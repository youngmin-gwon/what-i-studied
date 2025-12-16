# Cloud & Sync Patterns #apple #cloud #sync #common

클라우드/동기화 기능을 쉽게 설계하기 위한 가이드를 모았다. 용어는 [[apple-glossary]].

## 왜 동기화가 어려울까?
- 여러 기기에서 동시에 데이터를 바꾸면 충돌이 생길 수 있다.
- 네트워크가 불안정하면 요청이 실패하거나 중복될 수 있다.
- 프라이버시/보안 규칙을 지키면서 최소 데이터만 보내야 한다.

## 기본 원칙
- 오프라인 먼저: 모든 변경을 로컬에 기록하고, 나중에 서버로 보낸다.
- 충돌 정책 명시: 최종 작성자 우선, 타임스탬프 병합, 필드 단위 병합 등.
- 작은 단위 전송: delta/패치로 보내고, 큰 자산은 별도 업로드(URLSession background).

## 도구/서비스
- CloudKit: iCloud 데이터베이스. 공개/비공개 영역, 구독(Push)으로 변경 알림.
- iCloud Drive/FileProvider: 파일 동기화. 사용자가 고른 파일만 접근.
- Core Data + CloudKit: 로컬 DB를 자동으로 CloudKit과 맞춘다.
- CloudKit Share: 사용자가 다른 iCloud 사용자와 데이터를 공유.
- Non-Apple 백엔드: REST/gRPC/GraphQL 등. 동일 원칙 적용.

## 설계 패턴
- Outbox/Inbox: 보낼 일/받은 일을 나눠 기록. 실패 시 재시도.
- 버전/토큰: 레코드에 버전/etag를 둬서 충돌 감지.
- 타임라인/로그: 이벤트 로그를 저장해 재생성 가능하게 설계.
- 배치/스로틀링: 지나친 요청을 막고 배터리/서버 비용을 관리.

## 사진/미디어
- 썸네일/미리보기/원본을 나눠 저장. 네트워크 상태에 따라 품질 선택.
- 업로드는 백그라운드 세션, 재개 토큰을 활용.
- 프라이버시: 사진 라이브러리 전체 접근 대신 Photos picker/limited library.

## 푸시/변경 알림
- CloudKit 구독이나 APNs 푸시로 변경 알림을 받는다.
- 백그라운드 업데이트는 제한된 시간 내에 끝내야 하며, 너무 잦으면 시스템이 제한.

## 암호화/프라이버시
- 민감 데이터는 서버/클라이언트 모두 암호화. iCloud의 경우 end-to-end 옵션 검토.
- 개인 정보/위치/연락처 등은 최소화하고, 사용자 동의를 명확히 받는다.
- 키/토큰은 [[apple-glossary#Keychain|Keychain]]에 저장.

## 테스트 시나리오
- 오프라인 편집 후 동기화, 중복 요청, 충돌, 대량 업로드, 만료된 토큰.
- 다른 타임존/언어/기기/OS 버전 간 상호 운용성.
- 낮은 저장 공간/Low Power/Low Data/배터리 부족 상태.

## 운영/모니터링
- 성공률/지연/충돌 횟수/재시도 비율을 추적.
- CloudKit 대역폭/요금, API 한도 모니터링.
- 오류 메시지를 사용자 친화적으로 표시, 재시도 버튼 제공.

## 링크
[[apple-network-basics]], [[apple-networking-and-cloud]], [[apple-sandbox-and-security]], [[apple-storage-and-filesystems]].
