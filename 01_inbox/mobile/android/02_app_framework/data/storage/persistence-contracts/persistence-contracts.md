# 영속 저장소 계약

영속 저장소는 앱 재시작 뒤에도 남아야 하는 데이터의 형태와 접근 방식을 정한다. DataStore와 Room은 대체재가 아니라 서로 다른 데이터 계약이다.

## 정본 노트

- [Android 저장소는 데이터 수명과 소유권으로 선택한다](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/choose-storage-by-data-lifetime-and-ownership.md)
- [DataStore는 작은 설정과 현재 상태를 저장한다](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/datastore-stores-small-settings-and-current-state.md)
- [Room은 누적되고 조회되는 로컬 데이터를 저장한다](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/room-stores-accumulated-queryable-local-data.md)
- [SQLite와 Room의 경계는 엔진과 애플리케이션 API의 차이다](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/sqlite-is-storage-engine-room-is-app-access-layer.md)
- [Repository는 Room과 DataStore를 Flow로 연결한다](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/repository-connects-room-and-datastore-as-flow.md)
- [DataStore와 Room 마이그레이션은 저장소 계약의 시간 경계다](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/datastore-and-room-migrations-are-time-boundaries.md)

상위 지도: [Android 저장소와 영속성](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-persistence.md)
