# Activity가 직접 처리하던 일

과거의 Activity는 너무 많은 일을 떠안기 쉬웠습니다.

| 책임      | Activity에 몰렸던 코드                                        |
|:--------|:--------------------------------------------------------|
| 화면 렌더링  | XML layout inflate, View 찾기, TextView/Button 갱신         |
| 화면 이동   | `startActivity()`, `finish()`, intent extra 처리          |
| 상태 보관   | `onSaveInstanceState()`, 필드 변수, Bundle                  |
| 데이터 로딩  | API 호출, DB 조회, 로딩/에러 처리                                 |
| 생명주기 대응 | `onCreate()`, `onStart()`, `onResume()`, `onPause()` 분기 |

결과적으로 Activity는 **화면, 상태, 네트워크, DB, 네비게이션이 전부 섞인 거대한 클래스**가 되기 쉬웠습니다.
