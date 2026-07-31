# ☕️ Java API Framework

앱 개발자가 주로 상호작용하는 계층입니다.

- **System Server**: `ActivityManager`, `WindowManager` 등 100 여 개의 시스템 서비스가 이 **하나의 거대 프로세스** 안에서 스레드로 돌아갑니다.
    - 앱이 죽어도 시스템은 살아야 하므로 별도로 존재합니다.
    - Binder 를 통해 앱과 통신합니다.

---
