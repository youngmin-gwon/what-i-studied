# State는 가장 낮은 공통 owner에 둔다

상위 노트: [jetpack-compose-automatic-state-observation-for-flutter-developers](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/jetpack-compose-automatic-state-observation-for-flutter-developers.md)

상태를 무조건 ViewModel로 올리는 것은 Flutter에서 모든 값을 전역 Provider로 만드는 것과 비슷한 안티패턴입니다.

```text
SearchBar 안에서만 쓰는 expanded/query
-> SearchBar 내부 remember 또는 rememberSaveable

SearchBar와 ResultList가 함께 알아야 하는 query
-> 둘의 가장 낮은 공통 parent로 hoist

검색 정책, debounce, API 호출, loading/error
-> ViewModel

앱 재시작 후에도 남아야 하는 검색 이력
-> Repository + DataStore/Room
```

Compose의 state hoisting은 "가능한 한 위로 올린다"가 아니라 "읽고 쓰는 범위의 가장 낮은 공통 owner로 올린다"에 가깝습니다.

---
