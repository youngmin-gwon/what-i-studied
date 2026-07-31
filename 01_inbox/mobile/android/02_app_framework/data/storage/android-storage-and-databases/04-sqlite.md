# SQLite

상위 노트: [android-storage-and-databases](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-databases.md)

SQLite는 Android에 내장된 관계형 데이터베이스 엔진입니다.

Room은 SQLite를 감싼 abstraction이고, raw SQLite API를 직접 쓰는 것도 가능합니다. 하지만 일반 앱 개발에서는 Room을 우선 선택하는 편이
좋습니다.

raw SQLite가 맞을 수 있는 경우:

```text
기존 SQLite DB를 그대로 마이그레이션해야 함
Room이 지원하지 않는 매우 특수한 low-level 기능이 필요함
라이브러리 또는 기존 C/C++ layer가 SQLite 파일을 직접 다룸
```

일반적인 앱 내부 DB는 Room을 쓰는 편이 낫습니다.

---
