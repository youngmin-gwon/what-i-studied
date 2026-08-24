---
title: room-local-database
tags: [android, android/data, android/persistence-contracts, android/storage]
aliases: ["Room은 누적되고 조회되는 로컬 데이터를 저장한다"]
date modified: 2026-08-03 18:09:10 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Room 은 누적되고 조회되는 로컬 데이터를 저장한다

상위 문서: [영속 저장소 계약](./persistence.md)

Room 은 SQLite 위에서 Entity, DAO, Database 를 제공하는 Jetpack persistence library 다.

실제 데이터는 SQLite database file 에 저장되며 Room 이 접근 코드를 생성한다.

### Room 을 선택할 신호

- 기록이 계속 쌓인다.
- 여러 row 를 검색하거나 정렬한다.
- 기간별 조회가 필요하다.
- 테이블 사이의 관계가 있다.
- 서버 데이터의 오프라인 사본이 필요하다.
- 부분 갱신과 트랜잭션이 중요하다.

운동 기록, 측정 이력, 대시보드 캐시, 동기화 큐가 대표적인 예다.

### 구성 요소

Entity 는 테이블의 row 모델이다.

DAO 는 query, insert, update, delete 의 경계를 정의한다.

RoomDatabase 는 database 와 DAO 를 연결하는 접근 지점이다.

```kotlin
@Entity(tableName = "users")
data class User(
    @PrimaryKey val id: String,
    val name: String,
    val age: Int,
)

@Dao
interface UserDao {
    @Query("SELECT * FROM users ORDER BY name")
    fun observeUsers(): Flow<List<User>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(user: User)
}
```

SQL query 는 컴파일 시점에 검증할 수 있다.

DAO 가 데이터베이스 접근을 캡슐화하므로 UI 가 SQL 이나 cursor 를 알 필요가 없다.

### Room 이 과한 경우

session 하나, Boolean 하나, 마지막 탭 하나에는 Entity 와 migration 이 불필요한 비용이다.

그런 값은 [DataStore 공식 문서](https://developer.android.com/topic/libraries/architecture/datastore) 에 맞춰 저장한다.

### 설계 시 주의점

Entity 를 화면 전용 모델로 그대로 노출하지 않는다.

Repository 에서 Entity 를 도메인 모델이나 UI 상태로 변환하면 스키마 변경의 영향이 줄어든다.

데이터베이스 버전은 schema 변경과 함께 올리고, 기존 설치본의 migration 경로를 테스트한다.

Room 은 저장소 선택의 이름이 아니라 누적 데이터의 조회 모델을 관리하는 경계다.
