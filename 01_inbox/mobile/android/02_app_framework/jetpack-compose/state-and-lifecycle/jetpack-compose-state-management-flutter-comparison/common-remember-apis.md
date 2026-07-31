# 자주 쓰는 `remember~` 계열

상위 노트: [jetpack-compose-state-management-flutter-comparison](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison.md)

Compose와 Jetpack 라이브러리에는 `remember`로 시작하는 API가 많습니다. 공통점은 "Composition 수명에 맞춰 어떤 객체를 기억한다"는 것입니다.

상태나 작업이 어떤 수명에 묶여야 하는지부터 판단해야 할
때는 [jetpack-compose-state-lifetime-api-selection](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection.md)를 먼저 봅니다.

| API                                 | 역할                                  | 주의점                                              |
|:------------------------------------|:------------------------------------|:-------------------------------------------------|
| `remember`                          | recomposition 사이에 값 유지              | 화면에서 제거되면 사라짐                                    |
| `rememberSaveable`                  | 저장 가능한 UI 상태 복원                     | 큰 데이터나 dependency 저장 금지                          |
| `rememberCoroutineScope`            | Composable 수명에 묶인 CoroutineScope 제공 | 화면 이벤트용. 장기 비즈니스 작업은 ViewModel이 더 적합             |
| `rememberUpdatedState`              | effect를 재시작하지 않고 최신 값/lambda 참조     | `LaunchedEffect(Unit)` 안에서 최신 callback이 필요할 때 유용 |
| `rememberScrollState`               | 일반 scroll 상태                        | 단순 scroll container용                             |
| `rememberLazyListState`             | `LazyColumn`, `LazyRow` scroll 상태   | list position 제어/관찰에 사용                          |
| `rememberPagerState`                | pager page 상태                       | foundation pager 사용 시                            |
| `rememberSaveableStateHolder`       | key별 saveable state 보관              | navigation, tab, custom back stack에서 유용          |
| `rememberLauncherForActivityResult` | Activity Result launcher 등록         | 권한 요청, 이미지 선택 등 platform result 처리               |
| `rememberModalBottomSheetState`     | Material3 bottom sheet 상태           | sheet 표시/숨김은 coroutine과 함께 다루는 경우가 많음            |
| `rememberDrawerState`               | Material drawer 상태                  | navigation drawer open/close 상태                  |
| `rememberDatePickerState`           | Material3 date picker 상태            | picker 내부 선택 상태                                  |
| `rememberTimePickerState`           | Material3 time picker 상태            | picker 내부 선택 상태                                  |
| `rememberInfiniteTransition`        | 무한 animation transition             | 화면에 있을 때만 의미 있음                                  |
| `rememberTransition`                | animation transition 상태             | state 기반 animation에 사용                           |

Navigation 3를 쓰는 경우에도 같은 원리입니다. back stack, entry decorator, saveable state holder 등은 Composition
안에서 기억해야 할 UI navigation state입니다.

---
