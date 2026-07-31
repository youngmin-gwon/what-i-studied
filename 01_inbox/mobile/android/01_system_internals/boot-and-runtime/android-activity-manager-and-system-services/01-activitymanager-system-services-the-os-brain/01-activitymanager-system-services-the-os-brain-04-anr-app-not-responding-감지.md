# 🛡️ ANR (App Not Responding) 감지

시스템 서비스는 앱이 제시간에 반응하지 않을 경우 사용자에게 알리고 앱을 종료시킬 수 있는 Watchdog 기능을 수행합니다.

- **Input Timeout**: 5 초간 입력 이벤트에 응답하지 않는 경우.
- **Broadcast Timeout**: 포그라운드 10 초, 백그라운드 60 초 내에 처리가 완료되지 않는 경우.
- **Service Timeout**: 20 초 내에 서비스 시작 절차가 완료되지 않는 경우.

---
