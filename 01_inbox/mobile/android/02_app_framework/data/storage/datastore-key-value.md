---
title: datastore-key-value
tags: [android, android/data, android/persistence-contracts, android/storage]
aliases: ["DataStore는 작은 설정과 현재 상태를 저장한다"]
date modified: 2026-08-03 18:09:07 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## DataStore 는 작은 설정과 현재 상태를 저장한다

상위 문서: [영속 저장소 계약](persistence.md)

관련 노트: [Android Keystore 키는 비추출성으로 보호한다](../../../05_security_privacy/secure-storage/keystore-key-non-exportability.md)

DataStore 는 앱의 작은 데이터를 비동기적으로 저장하고 `Flow` 로 관찰하는 Jetpack 저장소다.

### 적합한 데이터

- 마지막 선택 탭
- 온보딩 완료 여부
- feature flag
- 마지막 동기화 시각
- 현재 로그인 세션의 암호화된 값

이 데이터들은 row 목록이 아니라 앱 동작을 결정하는 상태다.

### Preferences DataStore

Preferences DataStore 는 미리 정한 key 와 값을 저장한다.

```kotlin
val Context.dataStore: DataStore<Preferences> by preferencesDataStore(name = "settings")

private val userNameKey = stringPreferencesKey("user_name")

val userName: Flow<String> = context.dataStore.data
    .map { preferences -> preferences[userNameKey] ?: "" }

suspend fun updateUserName(name: String) {
    context.dataStore.edit { preferences ->
        preferences[userNameKey] = name
    }
}
```

읽기는 `Flow`, 쓰기는 `suspend` 함수로 노출한다.

이 구조는 호출자가 파일 I/O 나 동기 잠금을 직접 다루지 않게 한다.

### Proto DataStore

Proto DataStore 는 Protobuf 스키마로 여러 필드를 가진 typed object 를 저장한다.

필드 간 의미가 중요하거나 타입 안정성이 필요한 경우 Preferences 보다 적합하다.

대신 스키마와 serializer 를 관리해야 하므로 단순한 flag 에는 과하다.

### DataStore 의 경계

DataStore 는 대규모 목록, 검색, 정렬, 관계 무결성에 적합하지 않다.

부분 업데이트가 많거나 수천 개의 항목이 쌓이면 Room 을 검토한다.

여러 화면이 값을 공유하더라도 그 사실만으로 Room 이 필요한 것은 아니다.

### 이전 API 와의 관계

`SharedPreferences` 는 동기 접근과 오류 처리의 한계 때문에 새 기능의 기본 선택이 아니다.

기존 값을 옮길 때는 [SharedPreferencesMigration 공식 문서](https://developer.android.com/topic/libraries/architecture/datastore#sharedpreferences-migration) 를 사용한다.

DataStore 인스턴스는 같은 파일에 대해 앱 전체에서 하나만 만들도록 구성한다.

### 보안 상태

DataStore 자체를 비밀 저장소로 간주하지 않는다.

암호화 키는 [Android Keystore 공식 문서](https://developer.android.com/privacy-and-security/keystore) 에 두고, DataStore 에는 필요한 암호문과 메타데이터만 저장한다.

데이터 삭제 시점도 명시한다.

로그아웃은 세션 상태를 지우지만, 일반 설정까지 함께 지울지는 제품 정책으로 결정한다.
