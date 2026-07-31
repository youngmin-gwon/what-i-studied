# get_it에서 Metro로 옮길 때의 매핑표

상위 노트: [[metro-di-get-it-guide]]

| get_it 코드/개념                                     | Metro에서의 대응                                                      |
|:-------------------------------------------------|:-----------------------------------------------------------------|
| `getIt.registerFactory<Foo>(() => Foo(getIt()))` | `@Inject class Foo(dep: Dep)`                                    |
| `getIt.registerSingleton<Api>(ApiImpl())`        | `@SingleIn(AppScope::class)` + `@Provides fun provideApi(): Api` |
| `getIt<Api>()`                                   | 생성자 파라미터 `class Foo(private val api: Api)`                       |
| `registerLazySingleton`                          | scoped binding. 처음 요청될 때 생성되어 graph 안에서 재사용                      |
| `reset()`                                        | graph 인스턴스를 버리고 새로 만들기                                           |
| `getIt.pushNewScope()`                           | 별도 graph/graph extension 생성                                      |
| `registerFactoryParam`                           | assisted injection 또는 graph factory parameter                    |
| test에서 `registerSingleton<FakeApi>`              | test graph 또는 factory parameter로 fake 주입                         |

---
