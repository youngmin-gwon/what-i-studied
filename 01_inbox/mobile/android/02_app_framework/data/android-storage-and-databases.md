# Android Storage & Database 가이드

이 문서는 Android에서 자주 만나는 저장소 선택지인 **DataStore, Room, SQLite, MediaStore, App-specific files, Shared
storage**의 역할을 정리합니다.

현재 프로젝트에서 `sessionKey`는 DataStore에 저장하고, Room을 아직 도입하지 않은 이유도 함께 설명합니다.

---

---

## 원자 노트

- [[01-큰-그림|큰 그림]]
- [[02-datastore|DataStore]]
- [[03-room|Room]]
- [[04-sqlite|SQLite]]
- [[05-mediastore|MediaStore]]
- [[06-app-specific-files|App-specific Files]]
- [[07-storage-access-framework|Storage Access Framework]]
- [[08-이-프로젝트-적용-기준|이 프로젝트 적용 기준]]
- [[09-모듈-배치-기준|모듈 배치 기준]]
- [[10-선택-규칙|선택 규칙]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
