# Flow operator는 stream 변환과 취소 규칙을 드러낸다

Flow operator는 값 목록을 편의상 가공하는 문법이 아니라 stream의 변환, 결합, 취소 규칙을 선언하는 위치다. `map`과 `filter`는 각 값을 변환하거나 걸러내고, `combine`은 여러 source의 최신값을 묶고, `flatMapLatest`는 새 입력이 오면 이전 작업을 취소한다.

검색어 입력처럼 최신 요청만 의미 있는 흐름에는 `flatMapLatest`가 맞다. 사용자 정보와 설정처럼 서로 다른 source의 최신 조합이 화면 상태를 만들면 `combine`이 맞다.

operator를 선택할 때는 "어떤 값이 필요한가"보다 "이전 작업을 유지할 것인가, 취소할 것인가, 여러 source 중 어느 시점의 값을 합칠 것인가"를 먼저 본다. 이 규칙이 화면 버그와 중복 요청을 줄인다.

관련 노트: [flatMapLatest는 새 입력이 오면 이전 작업을 취소한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/flatmaplatest-cancels-obsolete-work-for-new-input.md), [combine은 여러 source의 최신값으로 화면 상태를 만든다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/combine-builds-screen-state-from-latest-source-values.md)
