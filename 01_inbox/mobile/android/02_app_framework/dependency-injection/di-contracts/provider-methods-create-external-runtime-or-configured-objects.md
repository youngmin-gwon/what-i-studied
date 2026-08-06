---
title: provider-methods-create-external-runtime-or-configured-objects
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Provider method 는 외부 타입, 런타임 값, 설정된 객체를 만들 때 쓴다

`@Provides` 계열 함수는 DI framework 가 생성자를 알 수 없거나 호출해서는 안 되는 객체를 graph 에 넣기 위한 boundary 다. Retrofit, Room database, DataStore, `Context` 로 만드는 system-facing 객체, base URL 같은 configuration 을 묶은 객체가 여기에 들어간다.

**Provider method**(`@Provides` — 외부 라이브러리 타입이나 런타임 설정 객체의 생성 로직을 명시하는 모듈 메서드) 가 많아지면 graph 가 service locator 처럼 변한다. 먼저 constructor injection 이 가능한 타입인지 확인하고, provider 는 외부 library type 이나 construction policy 가 의미 있는 타입에 제한한다.

### 최소 예시

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {
    @Provides
    @Singleton
    fun provideUserApi(client: OkHttpClient, @ApiBaseUrl baseUrl: String): UserApi =
        Retrofit.Builder()
            .client(client)
            .baseUrl(baseUrl)
            .build()
            .create(UserApi::class.java)
}
```

provider의 parameter는 graph dependency이고 return type과 qualifier는 제공하는 binding key다. provider body가 던지는 잘못된 URL·파일·초기화 예외는 graph compile이 아니라 해당 binding이 실제 생성되는 런타임에 드러난다.

### 실패와 관찰 신호

- `@ApiBaseUrl String`이 없으면 compile-time graph는 qualified missing binding으로 실패한다.
- 같은 key의 provider를 둘 등록하면 duplicate binding이 된다.
- provider body에 환경 분기와 전역 lookup이 쌓이면 생성 정책이 숨겨진 service locator가 되므로 configuration value를 factory parameter나 별도 binding으로 끌어낸다.

관련 노트: [Context boundaries](../../architecture/context-and-modularity/android-context-boundaries.md)

상위 문서: [DI 계약](./di-contracts.md)

공식 문서: [Dagger basic usage — `@Provides`](https://dagger.dev/dev-guide/basic-usage)
