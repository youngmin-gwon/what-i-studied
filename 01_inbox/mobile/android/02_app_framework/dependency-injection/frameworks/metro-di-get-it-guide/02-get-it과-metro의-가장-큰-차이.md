# get_it과 Metro의 가장 큰 차이

상위 노트: [metro-di-get-it-guide](01_inbox/mobile/android/02_app_framework/dependency-injection/frameworks/metro-di-get-it-guide.md)

Flutter `get_it`은 보통 **전역 서비스 로케이터**처럼 씁니다.

```dart
final getIt = GetIt.instance;

getIt.registerSingleton<Api>(ApiImpl());
getIt.registerFactory<BenefitRepository>(
  () => BenefitRepository(getIt<Api>()),
);

final repository = getIt<BenefitRepository>();
```

Metro는 보통 이렇게 생각합니다.

```text
객체를 전역 보관함에 등록한다
-> getIt 방식

객체들이 필요한 것을 생성자로 선언한다
-> Metro가 컴파일 시 그래프를 만들고 연결한다
```

| 개념      | get_it                | Metro                                      |
|:--------|:----------------------|:-------------------------------------------|
| 등록 위치   | `getIt.register...()` | `@DependencyGraph`, `@Provides`, `@Inject` |
| 가져오는 방식 | `getIt<T>()`로 직접 꺼냄   | 생성자 파라미터로 받음                               |
| 검증 시점   | 주로 런타임                | 컴파일 타임                                     |
| 누락된 의존성 | 실행 중 에러 가능            | 빌드 실패                                      |
| 전역성     | 전역 singleton으로 쓰기 쉬움  | graph 인스턴스 수명에 묶임                          |
| 사고방식    | service locator       | dependency graph                           |

> [!IMPORTANT]
> Metro에서는 `getIt<Api>()`처럼 아무 곳에서나 꺼내 쓰는 습관을 줄이는 것이 핵심입니다. 필요한 객체는 생성자에서 받고, Metro가 그 생성자를 호출하게
> 만듭니다.

---
