# Foreground Service vs WorkManager vs JobScheduler 선택 기준

| 상황                                | 선택                                | 이유                               |
|:----------------------------------|:----------------------------------|:---------------------------------|
| 음악 재생처럼 앱을 내려도 바로 계속 재생되어야 함      | Foreground Service + MediaSession | 유저가 지금 듣고 있고 알림/미디어 컨트롤이 필요      |
| 운동 기록, 길안내처럼 실시간으로 계속 추적해야 함      | Foreground Service                | 중단되면 UX가 망가지고 유저가 작업을 인지해야 함     |
| 사진 업로드, 로그 전송, 서버 동기화처럼 결국 완료되면 됨 | WorkManager                       | 네트워크/충전 조건, 재시도, 앱 재시작 이후 보장에 적합 |
| OS 프레임워크 수준에서 직접 작업 스케줄을 제어해야 함   | JobScheduler                      | Jetpack 추상화보다 낮은 레벨 제어가 필요할 때    |
| 정확한 시각에 알림을 울려야 함                 | AlarmManager                      | 작업 처리보다 "정확한 시간" 자체가 핵심          |
| 화면이 보이는 동안만 API 호출/계산하면 됨         | Kotlin Coroutine                  | 앱이 화면 밖으로 나가면 취소되어도 되는 작업        |

> [!IMPORTANT]
> WorkManager는 Service의 단순 대체품이 아닙니다. "지금 즉시 계속 돌아야 하는 작업"은 Foreground Service가 맞고, **조건이 맞을 때 OS가
안전하게 실행해도 되는 보장 작업**은 WorkManager가 맞습니다.

---
