# DataStore

상위 노트: [[android-storage-and-databases]]

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
