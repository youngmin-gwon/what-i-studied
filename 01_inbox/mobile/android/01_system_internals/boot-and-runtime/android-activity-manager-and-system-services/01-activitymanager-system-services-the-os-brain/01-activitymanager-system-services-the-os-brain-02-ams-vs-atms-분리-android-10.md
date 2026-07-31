# 🧱 AMS vs ATMS 분리 (Android 10+)

안드로이드 10 이전에는 AMS 가 모든 기능을 담당하는 거대 클래스(3 만 줄 이상)였으나, 현재는 책임이 분리되었습니다.

- **ActivityTaskManagerService (ATMS)**: Activity, Task 스택, Window 관리 등 **사용자 인터페이스(UI) 중심**의 전환을 담당합니다.
- **ActivityManagerService (AMS)**: 프로세스 생성, Service/Broadcast 관리, 권한 검사 등 **백그라운드 중심**의 운영을 담당합니다.

---
