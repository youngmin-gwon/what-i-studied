# DataStore는 작은 설정과 현재 상태를 저장한다

상위 문서: [영속 저장소 계약](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md)
관련 정본: [Android Keystore 키는 비추출성으로 보호한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/android-keystore-protects-keys-by-non-exportability.md)


DataStore는 앱의 작은 데이터를 비동기적으로 저장하고 `Flow`로 관찰하는 Jetpack 저장소다.

## 적합한 데이터

- 마지막 선택 탭
- 온보딩 완료 여부
- feature flag
- 마지막 동기화 시각
- 현재 로그인 세션의 암호화된 값

이 데이터들은 row 목록이 아니라 앱 동작을 결정하는 상태다.

## Preferences DataStore

Preferences DataStore는 미리 정한 key와 값을 저장한다.

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

이 구조는 호출자가 파일 I/O나 동기 잠금을 직접 다루지 않게 한다.

## Proto DataStore

Proto DataStore는 Protobuf 스키마로 여러 필드를 가진 typed object를 저장한다.

필드 간 의미가 중요하거나 타입 안정성이 필요한 경우 Preferences보다 적합하다.

대신 스키마와 serializer를 관리해야 하므로 단순한 flag에는 과하다.

## DataStore의 경계

DataStore는 대규모 목록, 검색, 정렬, 관계 무결성에 적합하지 않다.

부분 업데이트가 많거나 수천 개의 항목이 쌓이면 Room을 검토한다.

여러 화면이 값을 공유하더라도 그 사실만으로 Room이 필요한 것은 아니다.

## 이전 API와의 관계

`SharedPreferences`는 동기 접근과 오류 처리의 한계 때문에 새 기능의 기본 선택이 아니다.

기존 값을 옮길 때는 [SharedPreferencesMigration 공식 문서](https://developer.android.com/topic/libraries/architecture/datastore#sharedpreferences-migration)를 사용한다.

DataStore 인스턴스는 같은 파일에 대해 앱 전체에서 하나만 만들도록 구성한다.

## 보안 상태

DataStore 자체를 비밀 저장소로 간주하지 않는다.

암호화 키는 [Android Keystore 공식 문서](https://developer.android.com/privacy-and-security/keystore)에 두고, DataStore에는 필요한 암호문과 메타데이터만 저장한다.

데이터 삭제 시점도 명시한다.

로그아웃은 세션 상태를 지우지만, 일반 설정까지 함께 지울지는 제품 정책으로 결정한다.
