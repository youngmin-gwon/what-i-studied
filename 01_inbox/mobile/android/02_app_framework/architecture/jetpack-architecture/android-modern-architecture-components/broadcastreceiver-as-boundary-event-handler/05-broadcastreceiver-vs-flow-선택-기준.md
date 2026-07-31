# BroadcastReceiver vs Flow 선택 기준

| 상황                             | 선택                                         |
|:-------------------------------|:-------------------------------------------|
| OS가 보내는 부팅 완료 이벤트를 받아야 함       | BroadcastReceiver                          |
| 알림의 "답장", "삭제", "확인" 액션을 받아야 함 | BroadcastReceiver 또는 PendingIntent 대상 컴포넌트 |
| 앱 내부 로그인 상태 변경을 여러 화면이 알아야 함   | StateFlow/SharedFlow                       |
| DB 변경을 화면이 자동 반영해야 함           | Room + Flow                                |
| 네트워크 연결 상태를 UI가 구독해야 함         | callbackFlow + StateFlow                   |
| 다른 앱이 내 데이터를 조회해야 함            | ContentProvider                            |

> [!TIP]
> Receiver는 "앱 밖에서 들어온 방송을 받는 문"입니다. 앱 안에서 컴포넌트끼리 대화하려고 Receiver를 쓰면 구조가 불필요하게 무거워집니다.

---
