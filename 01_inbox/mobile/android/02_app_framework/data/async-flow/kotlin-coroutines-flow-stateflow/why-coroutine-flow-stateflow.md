# 왜 Coroutine, Flow, StateFlow가 필요해졌나?

상위 노트: [[kotlin-coroutines-flow-stateflow]]

안드로이드 앱은 대부분 기다림의 연속입니다.

* 서버 API 응답 기다리기
* 로컬 DB 조회 기다리기
* 파일 읽기/쓰기 기다리기
* 위치 정보 업데이트 기다리기
* 유저 입력 기다리기
* 화면 생명주기 변화 기다리기

이 기다림을 메인 스레드에서 그대로 처리하면 앱이 멈춥니다. 안드로이드에서 메인 스레드는 유저 터치, 화면 렌더링, 애니메이션을 처리하는 가장 중요한 통로이기 때문입니다.

```kotlin
// 나쁜 예: 메인 스레드에서 오래 걸리는 작업을 직접 실행
val products = api.fetchProducts()
productTextView.text = products.first().name
```

그래서 오래 걸리는 작업은 메인 스레드 밖에서 처리하고, 결과만 다시 UI로 가져와야 합니다.

과거에는 이를 위해 `Thread`, `Handler`, `AsyncTask`, RxJava 같은 도구를 많이 사용했습니다. 현대 Kotlin/Android에서는 이 역할을 *
*Coroutine + Flow**가 맡습니다.

| 문제                       | 현대 해법                            |
|:-------------------------|:---------------------------------|
| 오래 걸리는 작업을 메인 스레드 밖에서 실행 | Coroutine                        |
| 비동기 작업을 순차 코드처럼 읽기 쉽게 작성 | `suspend` 함수                     |
| 시간이 지나며 여러 번 바뀌는 데이터 관찰  | Flow                             |
| 화면의 현재 상태를 항상 최신값으로 보관   | StateFlow                        |
| 앱 내부 상태/이벤트를 여러 곳으로 전달   | StateFlow / SharedFlow / Channel |

---
