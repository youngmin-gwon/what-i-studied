# Provider method는 외부 타입, 런타임 값, 설정된 객체를 만들 때 쓴다

`@Provides` 계열 함수는 DI framework가 생성자를 알 수 없거나 호출해서는 안 되는 객체를 graph에 넣기 위한 boundary다. Retrofit, Room database, DataStore, `Context`로 만드는 system-facing 객체, base URL 같은 configuration을 묶은 객체가 여기에 들어간다.

Provider method가 많아지면 graph가 service locator처럼 변한다. 먼저 constructor injection이 가능한 타입인지 확인하고, provider는 외부 library type이나 construction policy가 의미 있는 타입에 제한한다.

관련 노트: [Context boundaries](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context-boundaries.md).
