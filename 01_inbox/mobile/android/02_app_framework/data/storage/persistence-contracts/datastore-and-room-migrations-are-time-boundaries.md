---
title: "DataStore와 Room 마이그레이션은 저장소 계약의 시간 경계다"
tags: [android, android/data, android/storage, android/persistence-contracts]
aliases: ["DataStore와 Room 마이그레이션은 저장소 계약의 시간 경계다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# DataStore와 Room 마이그레이션은 저장소 계약의 시간 경계다

상위 문서: [영속 저장소 계약](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md)
관련 노트: [백업과 복원은 데이터 경계를 명시적으로 설계해야 한다](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/backup-restore-requires-explicit-data-boundaries.md)

저장소를 선택하면 새 설치만 고려해서는 안 된다. 이미 배포된 앱의 기존 값, 스키마 변경, 복원 시점의 데이터 호환성까지 저장소 계약에 포함된다.

## DataStore 마이그레이션

`SharedPreferences`에서 DataStore로 옮길 때는 일회성 migration을 명시한다.

- 기존 key 이름과 새 key 이름을 대응시킨다.
- 타입 변환과 기본값을 정한다.
- migration 완료 뒤 두 저장소를 동시에 source of truth로 두지 않는다.
- 실패했을 때 기본값으로 진행할지 사용자 조치가 필요한지 정한다.

Preferences DataStore는 작은 key-value 상태에 적합하지만, migration을 거쳤다는 이유만으로 장기 도메인 데이터 저장소가 되지는 않는다.

## Room 마이그레이션

Room은 schema version을 기준으로 database 구조 변화를 관리한다. Entity나 column을 바꾸면 version을 올리고, 기존 데이터를 보존해야 하면 명시적 `Migration`을 작성한다.

- column 추가 시 nullability와 기본값을 기존 row 기준으로 결정한다.
- 삭제나 rename은 데이터 손실 가능성을 리뷰한다.
- schema export와 migration test를 빌드에 포함한다.
- 자동 migration은 단순 변경에만 사용하고 결과를 검토한다.

## 백업과 분리해서 생각할 것

Migration은 같은 앱이 시간에 따라 저장소 구조를 바꾸는 문제다. Backup/restore는 데이터가 기기와 계정 경계를 넘어 이동하는 문제다.

두 문제는 연결되지만 같은 책임은 아니다. Room schema가 migration 가능하다고 해서 그 database를 백업해도 된다는 뜻은 아니다. 반대로 백업 제외 대상이어도 현재 설치 안에서는 migration이 필요할 수 있다.

## 점검 질문

- 이 변경은 기존 설치 사용자의 값을 보존해야 하는가?
- 기본값으로 대체해도 제품 의미가 유지되는가?
- schema 변경을 테스트로 재현할 수 있는가?
- 백업 복원 뒤에도 같은 migration 경로가 안전한가?

마이그레이션은 저장소 구현의 부수 작업이 아니라 배포된 데이터 계약을 유지하는 작업이다.
