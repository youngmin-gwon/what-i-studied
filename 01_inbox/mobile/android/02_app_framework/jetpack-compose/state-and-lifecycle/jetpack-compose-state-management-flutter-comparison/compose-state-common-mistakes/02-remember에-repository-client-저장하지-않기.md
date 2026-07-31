# `remember`에 repository/client 저장하지 않기

```kotlin
val repository = remember { SessionRepository(...) }
```

DI로 조립할 객체를 UI 기억 장치에 넣으면 수명과 테스트 경계가 흐려집니다. Repository, HTTP client, DataStore, cipher 같은
dependency는 DI에서 만들고 주입하는 편이 맞습니다.
