# system_server 가 하는 일

- [[android-glossary#ams|AMS/ATMS]] 로 앱과 화면을 관리한다.
- WindowManager 로 창 위치/크기/회전/입력을 다룬다.
- PackageManager 로 앱 설치/권한 기록/[[android-glossary#dex|dexopt]] 를 조정한다.
- Power/BatteryStats 로 전원 상태와 사용량을 기록한다.
- Connectivity/Telephony 로 네트워크/통신 상태를 조정한다.
