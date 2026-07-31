---
title: android-storage-systems
tags: []
aliases: []
date modified: 2026-04-05 17:42:48 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [[mobile-security]] > [[android-storage-systems]]

### Storage Systems: Data Persistence

안드로이드의 파일 시스템 구조와 현대적인 데이터 저장 프로토콜인 **Scoped Storage**, **MediaStore**, **SAF(Storage Access Framework)**를 심층 분석합니다.

데이터의 무결성을 보장하면서도 사용자 개인정보 보호를 위해 강화된 시스템 제약을 어떻게 준수하고, 효율적인 대용량 파일 처리 및 암호화 전략을 수립할지가 핵심 목표입니다.

---

---

## 원자 노트

- [[01-context-저장소-권한의-대변화|💡 Context: 저장소 권한의 대변화]]
- [[02-저장소-종류|저장소 종류]]
- [[03-scoped-storage-android-10|Scoped Storage (Android 10+)]]
- [[04-파일-시스템-구조|파일 시스템 구조]]
- [[05-데이터-저장-방법-선택|데이터 저장 방법 선택]]
- [[06-sharedpreferences|SharedPreferences]]
- [[07-datastore-권장|DataStore (권장)]]
- [[08-room-database|Room Database]]
- [[09-파일-암호화|파일 암호화]]
- [[10-저장소-공간-관리|저장소 공간 관리]]
- [[11-백업과-복원|백업과 복원]]
- [[12-성능-최적화|성능 최적화]]
- [[android-storage-systems-13-디버깅|디버깅]]
- [[android-storage-systems-14-see-also|See Also]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
