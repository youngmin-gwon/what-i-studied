# Android Storage & Database 가이드

이 문서는 Android에서 자주 만나는 저장소 선택지인 **DataStore, Room, SQLite, MediaStore, App-specific files, Shared
storage**의 역할을 정리합니다.

현재 프로젝트에서 `sessionKey`는 DataStore에 저장하고, Room을 아직 도입하지 않은 이유도 함께 설명합니다.

---

---

## 원자 노트

- [큰 그림](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-databases/android-storage-and-databases-01-%ED%81%B0-%EA%B7%B8%EB%A6%BC.md)
- [DataStore](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-databases/02-datastore.md)
- [Room](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-databases/03-room.md)
- [SQLite](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-databases/04-sqlite.md)
- [MediaStore](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-databases/05-mediastore.md)
- [App-specific Files](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-databases/06-app-specific-files.md)
- [Storage Access Framework](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-databases/07-storage-access-framework.md)
- [이 프로젝트 적용 기준](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-databases/08-%EC%9D%B4-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%A0%81%EC%9A%A9-%EA%B8%B0%EC%A4%80.md)
- [모듈 배치 기준](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-databases/09-%EB%AA%A8%EB%93%88-%EB%B0%B0%EC%B9%98-%EA%B8%B0%EC%A4%80.md)
- [선택 규칙](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-databases/10-%EC%84%A0%ED%83%9D-%EA%B7%9C%EC%B9%99.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
