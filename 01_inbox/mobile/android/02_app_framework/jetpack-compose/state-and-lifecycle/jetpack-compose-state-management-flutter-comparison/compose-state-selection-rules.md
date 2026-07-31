# 판단 규칙

상위 노트: [jetpack-compose-state-management-flutter-comparison](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison.md)

Compose 상태 위치는 다음 순서로 판단하면 됩니다.

```text
1. recomposition 동안만 유지되면 충분한가?
   -> remember

2. 화면 회전이나 프로세스 복원 후에도 작은 UI 값이 살아야 하는가?
   -> rememberSaveable

3. API 호출, validation, loading/error, screen policy가 있는가?
   -> ViewModel

4. 앱 재시작 후에도 남아야 하는 데이터인가?
   -> DataStore 또는 Room

5. 여러 feature가 알아야 하는 contract인가?
   -> api module에 interface/model

6. Android 저장소/네트워크/암호화 같은 실제 구현인가?
   -> impl module
```

Flutter식으로 요약하면 다음과 같습니다.

```text
setState로 충분한 로컬 UI 상태
-> remember / rememberSaveable

Riverpod/Cubit이 필요할 정도의 화면 상태
-> ViewModel + StateFlow

Bloc처럼 Event -> State 전이 규칙이 많아진 화면
-> ViewModel + 선택적 Reducer로 MVI에 가까운 구조 구성

SharedPreferences/secure storage/database에 넣을 데이터
-> DataStore / Room / Repository
```
