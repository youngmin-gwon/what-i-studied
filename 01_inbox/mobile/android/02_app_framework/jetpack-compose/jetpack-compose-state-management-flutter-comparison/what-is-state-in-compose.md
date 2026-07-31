# Compose에서 상태란 무엇인가?

상위 노트: [[jetpack-compose-state-management-flutter-comparison]]

Compose에서 상태는 시간이 지나며 바뀔 수 있고, UI 결과에 영향을 주는 값입니다.

```text
입력창의 text
선택된 tab
체크박스 checked 여부
로그인 세션 상태
운동 기록 목록
로딩/성공/실패 상태
```

다만 모든 상태를 같은 곳에 두면 안 됩니다.

| 상태 종류                                    | 권장 위치                  |
|:-----------------------------------------|:-----------------------|
| 버튼 눌림, 임시 expanded 여부                    | `remember`             |
| 입력값, 선택 tab처럼 회전 후에도 유지할 작은 UI 상태        | `rememberSaveable`     |
| 화면 전체의 로딩/성공/실패, form validation, API 결과 | ViewModel              |
| 로그인 세션, 앱 설정                             | Repository + DataStore |
| 운동 기록, 측정 이력처럼 쌓이는 구조화 데이터               | Repository + Room      |

`remember`는 UI 함수 내부의 메모리입니다. 앱 데이터 저장소가 아닙니다.

---
