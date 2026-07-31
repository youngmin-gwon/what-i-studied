# Room

상위 노트: [android-storage-and-databases](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-databases.md)

Room은 SQLite 위에 있는 Jetpack persistence library입니다.

Room은 "그냥 interface"가 아닙니다. 개발자가 DAO interface와 entity를 선언하면, Room이 compile time에 SQLite 접근 코드를
생성합니다. 실제 저장소는 SQLite database file입니다.

Room의 구성 요소:

| 구성 요소        | 역할                                |
|:-------------|:----------------------------------|
| Entity       | SQLite table의 row 모델              |
| DAO          | query, insert, update, delete API |
| RoomDatabase | database와 DAO 접근 지점               |

Room의 장점:

- SQL query compile-time 검증
- DAO/entity annotation 기반 boilerplate 감소
- migration 경로 관리
- Flow/Paging 등 Android data layer와 잘 맞음
- KMP 지원도 제공됨

Room이 맞는 경우:

```text
training record 목록
measure history
dashboard cache
offline-first 데이터
서버 동기화가 필요한 로컬 사본
기간별 조회, 정렬, 검색, pagination이 필요한 데이터
```

Room이 과한 경우:

```text
sessionKey 하나
Boolean flag 하나
마지막 선택 탭
단순 설정값
```

이런 값 때문에 Room을 만들면 entity, DAO, database, migration이 생기지만 실제 이점은 거의 없습니다.

---
