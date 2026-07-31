# Android Storage & Database 가이드

이 문서는 Android에서 자주 만나는 저장소 선택지인 **DataStore, Room, SQLite, MediaStore, App-specific files, Shared
storage**의 역할을 정리합니다.

현재 프로젝트에서 `sessionKey`는 DataStore에 저장하고, Room을 아직 도입하지 않은 이유도 함께 설명합니다.

---

## 1. 큰 그림

Android 저장소는 "DB를 쓸까 말까"보다 먼저 **무엇을 저장하는가**로 나누는 편이 안전합니다.

공식 Android storage overview는 앱 데이터 저장 선택지를 크게 다음처럼 나눕니다.

| 저장 대상             | 권장 저장소                   | 대표 예                                            |
|:------------------|:-------------------------|:------------------------------------------------|
| 작은 key-value 설정   | DataStore                | session flag, feature flag, user preference     |
| 구조화된 앱 내부 데이터     | Room                     | training record, measure history, offline cache |
| 앱 전용 파일           | App-specific files       | 앱 내부 캐시, 임시 다운로드, private export file           |
| 유저가 다른 앱에서도 볼 미디어 | MediaStore               | 사진, 동영상, 오디오                                    |
| 유저가 직접 고르는 문서     | Storage Access Framework | PDF, EPUB, CSV, 일반 파일 import/export             |

관련 공식 문서:

- [Data and file storage overview](https://developer.android.com/training/data-storage)
- [DataStore](https://developer.android.com/topic/libraries/architecture/datastore)
- [Save data in a local database using Room](https://developer.android.com/training/data-storage/room)
- [Access media files from shared storage](https://developer.android.com/training/data-storage/shared/media)

---

## 2. DataStore

DataStore는 작은 데이터를 비동기적이고 일관된 방식으로 저장하기 위한 Jetpack 저장소입니다.

주요 특징:

- Kotlin Coroutines와 Flow 기반
- key-value 저장에는 Preferences DataStore 사용
- typed object 저장에는 Proto DataStore 또는 custom serializer 사용
- SharedPreferences 대체재로 권장됨
- 작은 데이터에 적합

DataStore가 맞는 경우:

```text
sessionKey 존재 여부
앱 설정값
마지막 동기화 시각
feature flag
onboarding 완료 여부
```

DataStore가 맞지 않는 경우:

```text
목록 데이터
검색/정렬/필터링이 필요한 데이터
부분 업데이트가 많은 데이터
관계 무결성이 필요한 데이터
수천 개 이상의 row처럼 커지는 데이터
```

공식 문서도 large or complex dataset, partial update, referential integrity가 필요하면 DataStore 대신 Room을
고려하라고 설명합니다.

### 이 프로젝트의 sessionKey

현재 session 저장은 다음 구조입니다.

```text
sessionKey
 -> Android Keystore AES/GCM으로 암호화
 -> DataStore에 cipherText + iv 저장
```

이 데이터는 row가 쌓이는 도메인 데이터가 아닙니다.

```text
현재 로그인 세션 하나
읽기: 앱 시작 시 / request header 구성 시
쓰기: 로그인 성공 시
삭제: 로그아웃 / 인증 실패 시
```

따라서 Room보다 DataStore가 맞습니다.

---

## 3. Room

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

## 4. SQLite

SQLite는 Android에 내장된 관계형 데이터베이스 엔진입니다.

Room은 SQLite를 감싼 abstraction이고, raw SQLite API를 직접 쓰는 것도 가능합니다. 하지만 일반 앱 개발에서는 Room을 우선 선택하는 편이
좋습니다.

raw SQLite가 맞을 수 있는 경우:

```text
기존 SQLite DB를 그대로 마이그레이션해야 함
Room이 지원하지 않는 매우 특수한 low-level 기능이 필요함
라이브러리 또는 기존 C/C++ layer가 SQLite 파일을 직접 다룸
```

일반적인 앱 내부 DB는 Room을 쓰는 편이 낫습니다.

---

## 5. MediaStore

MediaStore는 앱 내부 DB가 아닙니다.

MediaStore는 Android 시스템이 제공하는 **공유 미디어 저장소의 인덱스와 접근 API**입니다. 사진, 동영상, 오디오, 다운로드 같은 사용자 미디어를 앱들이
공통으로 찾고 열 수 있게 해주는 system content provider라고 보는 편이 정확합니다.

중요한 점:

- 앱이 schema를 만들지 않습니다.
- 앱이 migration을 관리하지 않습니다.
- 앱 전용 데이터 저장소가 아닙니다.
- Android 시스템이 media collection을 관리합니다.
- 앱은 `ContentResolver`로 query/insert/update/delete 요청을 보냅니다.
- 반환되는 것은 파일 경로보다 `content://` URI 중심입니다.

MediaStore가 다루는 대표 collection:

| Collection             | 대상          |
|:-----------------------|:------------|
| `MediaStore.Images`    | 사진, 스크린샷    |
| `MediaStore.Video`     | 동영상         |
| `MediaStore.Audio`     | 음악, 녹음, 알림음 |
| `MediaStore.Downloads` | 다운로드 파일     |

MediaStore가 맞는 경우:

```text
사용자가 갤러리에서 볼 사진 저장
운동 자세 분석 결과 영상을 갤러리에 저장
사용자가 다른 앱에서도 열 수 있는 이미지/동영상 export
기기 내 사진/영상 목록에서 유저가 고른 미디어를 읽기
```

MediaStore가 맞지 않는 경우:

```text
sessionKey 저장
training record 저장
measure history 저장
앱 내부 캐시 저장
서버 응답 cache table 저장
```

즉 MediaStore는 "DB처럼 query할 수 있는 API"를 제공하지만, 우리가 앱 도메인 데이터를 넣는 database가 아닙니다.

### Photo Picker와의 관계

사용자가 기존 사진/동영상을 선택하기만 하면 Photo Picker가 더 나은 선택일 수 있습니다.

```text
Photo Picker
 -> 유저가 파일을 선택
 -> 앱은 선택된 URI에 접근
 -> 전체 미디어 라이브러리 권한을 요구하지 않음

MediaStore 직접 접근
 -> 앱이 media collection을 query
 -> use case에 따라 READ_MEDIA_IMAGES / READ_MEDIA_VIDEO 등이 필요할 수 있음
```

이 프로젝트에서 사용자가 프로필 사진이나 운동 영상을 선택하는 기능을 만들면, 먼저 Photo Picker를 검토합니다. 앱이 직접 만든 결과물을 갤러리에 저장해야 하면
MediaStore를 검토합니다.

---

## 6. App-specific Files

App-specific files는 앱만 사용하는 파일을 저장하는 영역입니다.

대표 API:

```kotlin
context.filesDir
context.cacheDir
context.getExternalFilesDir(...)
context.getExternalCacheDir()
```

여기서 `context`는 앱 저장소 위치를 OS에 물어보기 위한 Android `Context`입니다. 저장소 객체가 오래 살아야 한다면 Activity Context가 아니라
Application Context를 쓰는 편이 안전합니다. Context의 종류와 수명
차이는 [[android-context|android_context.md]]를
참조하세요.

특징:

- 앱 삭제 시 함께 제거됨
- 내부 저장소의 app-specific file은 다른 앱이 접근할 수 없음
- 이미지/영상이라도 사용자에게 공유할 목적이 없으면 MediaStore보다 app-specific directory가 맞을 수 있음

맞는 경우:

```text
임시 이미지 처리 파일
운동 분석 중간 산출물
네트워크 다운로드 캐시
앱 내부 export 준비 파일
```

---

## 7. Storage Access Framework

Storage Access Framework는 유저가 시스템 파일 picker를 통해 문서나 일반 파일을 직접 고르게 하는 방식입니다.

맞는 경우:

```text
PDF import/export
CSV export
EPUB 파일 열기
사용자가 특정 폴더나 문서를 직접 선택해야 하는 기능
```

MediaStore는 media 중심이고, SAF는 일반 문서/파일 중심입니다.

---

## 8. 이 프로젝트 적용 기준

현재 기준은 다음처럼 둡니다.

| 데이터                       | 저장소                                      | 이유                             |
|:--------------------------|:-----------------------------------------|:-------------------------------|
| sessionKey                | Encrypted DataStore                      | 단일 민감값, key-value 성격           |
| legacy apiToken migration | SharedPreferences -> Encrypted DataStore | 기존 앱 호환                        |
| password                  | 저장하지 않음                                  | 새 앱에서는 재로그인용 password 저장 정책 제거 |
| user profile 요약           | 우선 서버 source of truth                    | 필요 시 cache 전략 결정               |
| measure history           | Room 후보                                  | 목록/기간 조회 가능성                   |
| training record           | Room 후보                                  | 누적 데이터, offline/cache 가능성      |
| dashboard cache           | Room 후보                                  | 여러 feature 데이터 조합 cache 가능성    |
| 프로필 이미지 선택                | Photo Picker 우선                          | 권한 최소화                         |
| 앱이 생성한 공유 이미지/영상          | MediaStore 후보                            | 갤러리/다른 앱 접근 가능                 |
| 앱 내부 임시 파일                | App-specific files                       | 앱 삭제 시 제거되는 private file       |

---

## 9. 모듈 배치 기준

저장소 기술은 feature의 data/infra 영역에 둡니다.

```text
feature/session/api
 -> SessionRepository contract

feature/session/impl
 -> DataStoreSessionStorage
 -> AndroidKeystoreSessionCipher
 -> LegacySessionPreferences

feature/training/impl
 -> TrainingRecordDao
 -> TrainingDatabase or shared app database access

feature/measure/impl
 -> MeasureHistoryDao
```

Room을 도입할 때는 한 가지 결정을 먼저 해야 합니다.

```text
1. app-wide database 하나
   - 여러 feature entity를 한 DB에 둠
   - migration 관리가 중앙화됨
   - cross-feature query가 쉬움

2. feature별 database
   - feature 독립성이 높음
   - cross-feature query가 어려움
   - DB 파일과 migration이 분산됨
```

이 앱은 `dashboard`가 여러 feature 데이터를 모아 볼 가능성이 높으므로, Room을 도입한다면 처음에는 app-wide database 하나를 `core`에
두기보다, 별도 `:core:database` 또는 `:data:database` 모듈을 만드는 방식을 검토합니다.

단, 아직 local structured data가 없으므로 지금 Room 모듈을 먼저 만들 필요는 없습니다.

---

## 10. 선택 규칙

간단한 판단 기준은 다음입니다.

```text
값이 하나인가?
 -> DataStore

민감한 작은 값인가?
 -> Keystore + DataStore

row가 쌓이는가?
 -> Room

검색/정렬/기간 조회가 필요한가?
 -> Room

유저가 갤러리나 다른 앱에서 봐야 하는 미디어인가?
 -> MediaStore

유저가 직접 고르는 일반 파일인가?
 -> Storage Access Framework

앱 내부에서만 쓰는 파일인가?
 -> App-specific files
```

이 기준으로 보면 현재 session 저장에 Room이나 MediaStore를 쓰지 않은 것은 의도적으로 맞는 선택입니다.
