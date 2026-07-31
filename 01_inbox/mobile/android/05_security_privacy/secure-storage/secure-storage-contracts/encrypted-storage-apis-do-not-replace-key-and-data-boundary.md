---
title: encrypted-storage-apis-do-not-replace-key-and-data-boundary
tags: []
aliases: []
date modified: 2026-07-31 18:18:45 +09:00
date created: 2026-07-31 17:04:40 +09:00
---

## EncryptedSharedPreferences, DataStore, Room 의 보안 경계를 구분한다

상위 문서: [보안 저장소 계약](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/secure-storage-contracts.md)

관련 정본: [DataStore는 작은 설정과 현재 상태를 저장한다](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/datastore-stores-small-settings-and-current-state.md), [Room은 누적되고 조회되는 로컬 데이터를 저장한다](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/room-stores-accumulated-queryable-local-data.md)

### 핵심 주장

저장소 API 는 데이터 모델과 접근 방식을 결정하지만, 모든 저장소가 같은 보안 수준을 제공하지는 않는다.

민감도, 검색 필요성, 트랜잭션 요구, 백업 정책을 기준으로 저장소를 선택해야 한다.

### EncryptedSharedPreferences

`EncryptedSharedPreferences` 는 키와 값의 저장을 암호화하는 고수준 선택지다.

암호화 키는 Android Keystore 에 보호되며 구현 복잡도를 줄여 준다.

하지만 API 의 사용 가능 버전과 유지보수 상태를 확인하고 새 설계에 무조건 의존하지 않는다.

토큰 같은 소량의 key-value 데이터에 적합하지만 검색이나 복잡한 관계 모델에는 맞지 않는다.

암호화된 파일도 백업, 로그, 메모리 노출 문제까지 자동으로 해결하지는 않는다.

### DataStore

DataStore 는 SharedPreferences 의 비동기 대안으로 설정과 작은 상태를 저장한다.

Preferences DataStore 와 Proto DataStore 모두 저장소 동시성·일관성 문제를 줄이는 데 초점이 있다.

DataStore 라는 이름만으로 민감 데이터 암호화가 보장되는 것은 아니다.

민감한 값을 넣을 때는 별도 암호화 계층과 키 관리, 백업 제외 정책을 함께 적용한다.

작은 설정값과 단일 상태에는 적합하지만, 임의 조건 검색이 핵심이면 다른 선택을 검토한다.

### Room

Room 은 SQLite 데이터베이스에 구조화된 데이터를 저장하고 쿼리·트랜잭션을 제공한다.

개인정보가 여러 행과 관계로 구성되거나 검색과 마이그레이션이 필요할 때 적합하다.

Room 도 기본적으로 데이터베이스 전체를 민감 정보 저장소로 만들어 주지는 않는다.

필요하면 컬럼별 암호화, 데이터베이스 암호화 라이브러리, 키 보호 계층을 별도로 설계한다.

검색해야 하는 컬럼을 암호화하면 평문 검색이 어려워질 수 있으므로 요구사항을 먼저 정한다.

### 선택 기준

- 소량의 비밀 key-value: Keystore 와 암호화 저장소 조합
- 앱 설정과 작은 상태: DataStore, 단 민감 값은 추가 보호
- 관계형 데이터와 쿼리: Room, 필요한 필드와 DB 보호 수준을 명시
- 재생성 가능한 캐시: 암호화보다 만료·삭제·백업 제외 정책을 우선 검토

### 공통 검증 목록

저장소를 고르기 전에 평문이 디스크에 남는지 확인한다.

암호키가 데이터베이스 파일이나 설정 파일에 함께 저장되지 않는지 확인한다.

백업과 기기 이전에서 데이터가 어떻게 이동하는지 확인한다.

마이그레이션 실패와 키 무효화 시 사용자에게 어떤 복구를 제공할지 정한다.

테스트 로그와 스냅샷에 실제 민감 데이터가 들어가지 않게 한다.

### 결론

저장소 선택은 편의 API 선택이 아니라 보안 경계 선택이다.

저장소의 기능과 암호화 보장을 구분하고, 필요한 경우 Keystore 기반 암호화 계층을 명시적으로 추가한다.
