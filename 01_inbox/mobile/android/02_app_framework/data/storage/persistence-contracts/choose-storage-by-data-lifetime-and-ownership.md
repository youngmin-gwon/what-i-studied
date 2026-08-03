---
title: Android 저장소는 데이터 수명과 소유권으로 선택한다
tags: [android, android/data, android/storage, android/persistence-contracts]
aliases: ["Android 저장소는 데이터 수명과 소유권으로 선택한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Android 저장소는 데이터 수명과 소유권으로 선택한다

상위 문서: [Android 저장소와 영속성](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-persistence.md)
관련 노트: [저장소 선택은 파일의 소유권과 공개 목적을 먼저 묻는다](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/file-storage-is-selected-by-owner-and-public-purpose.md), [Android 민감 데이터는 암호화와 키 소유권을 함께 설계한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/sensitive-data-requires-encryption-and-key-ownership.md)


Android 저장소 선택은 API 이름보다 데이터의 수명과 소유권을 먼저 묻는 문제다.

## 먼저 확인할 질문

- 앱 프로세스가 끝나도 남아야 하는가?
- 앱을 삭제해도 사용자나 다른 앱이 보존해야 하는가?
- 값 하나를 읽는가, row가 계속 쌓이는가?
- 검색, 정렬, 기간 조회, 관계 무결성이 필요한가?
- 민감한 값인가?

## 기본 매핑

| 데이터 성격 | 우선 선택 |
| --- | --- |
| 현재 세션, 설정, 작은 상태 | DataStore |
| 민감한 작은 값 | Android Keystore + DataStore |
| 누적되는 구조화 데이터 | Room |
| 기존 DB나 특수 저수준 제어 | SQLite 직접 접근 |
| 앱 전용 바이너리나 임시 파일 | app-specific files |
| 사용자가 고르고 다른 앱과 공유할 파일 | Storage Access Framework |
| 사용자 갤러리와 연결되는 미디어 | MediaStore |

## 수명으로 나누기

메모리 상태는 화면이나 프로세스 수명에만 속한다.

DataStore는 앱 재시작 뒤에도 필요한 작은 설정과 현재 상태를 보존한다.

Room은 여러 번의 동기화와 사용자 행동으로 계속 증가하는 로컬 사본을 보존한다.

파일은 데이터베이스 row보다 큰 콘텐츠나 앱이 직접 다루는 바이트에 적합하다.

## 소유권으로 나누기

앱만 읽고 쓰는 데이터라면 내부 저장소를 우선 검토한다.

사용자나 다른 앱이 소유해야 하는 파일은 공유 저장소 API를 사용한다.

저장 위치가 바뀌면 권한, 백업, 삭제 정책도 함께 바뀐다.

## 실전 판단 순서

1. 값이 하나 또는 소수인가?
2. 값의 구조가 key-value로 충분한가?
3. row가 쌓이거나 부분 조회가 필요한가?
4. 외부 앱과 파일을 공유해야 하는가?
5. 데이터가 비밀인가?

값 하나이고 목록·검색·관계가 없다면 Room을 도입할 이유가 약하다.

반대로 값이 작더라도 여러 항목을 필터링하고 갱신해야 한다면 Room이 맞다.

## 예시

`sessionKey`는 현재 로그인 세션 하나이므로 DataStore의 책임이다.

암호문과 초기화 벡터가 민감하다면 키는 [Android Keystore 공식 문서](https://developer.android.com/privacy-and-security/keystore)에 두고 DataStore에는 암호화된 결과만 둔다.

운동 기록, 측정 이력, 오프라인 캐시는 row가 누적되므로 Room의 책임이다.

이 기준은 저장소를 많이 도입하는 것보다 각 데이터의 소유권을 명확히 하는 데 목적이 있다.
