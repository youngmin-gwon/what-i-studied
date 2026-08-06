---
title: binds-connects-interface-to-implementation-without-construction-code
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Binds 는 interface 와 implementation 을 연결하고 생성 코드는 추가하지 않는다

Interface 를 dependency 로 받으면 graph 는 어떤 implementation 을 넣어야 하는지 알아야 한다. `@Binds` 계열 binding 은 이미 constructor injection 으로 만들 수 있는 implementation 을 interface 타입으로 노출하는 선언이다.

생성 로직이 필요하면 provider가 맞고, 단순히 `DataStoreSessionStorage`를 `SessionStorage` key로 노출하는 일이라면 binds가 맞다.

### 최소 예시

```kotlin
interface SessionStorage

class DataStoreSessionStorage @Inject constructor(
    private val dataStore: DataStore<Preferences>,
) : SessionStorage

@Module
@InstallIn(SingletonComponent::class)
interface StorageBindings {
    @Binds fun bindSessionStorage(impl: DataStoreSessionStorage): SessionStorage
}
```

`@Binds` 메서드에는 구현 body가 없다. parameter type은 return type에 대입 가능해야 하고, 구현의 constructor binding도 graph 안에 있어야 한다.

### 실패와 관찰 신호

- `DataStoreSessionStorage : SessionStorage` 관계가 없으면 compiler가 binds parameter를 return type에 assign할 수 없다고 실패한다.
- 같은 qualifier의 `SessionStorage` binding을 둘 이상 만들면 duplicate binding diagnostic이 난다.
- 단순 `return impl`만 하는 `@Provides`가 보이면 `@Binds`로 표현 가능한지 확인한다.

상위 문서: [DI 계약](./di-contracts.md)

공식 문서: [Dagger basic usage — module bindings](https://dagger.dev/dev-guide/basic-usage)
