---
title: android-storage-systems
tags: []
aliases: []
date modified: 2026-04-05 17:42:48 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [mobile-security](01_inbox/mobile/mobile-security.md) > [android-storage-systems](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems.md)

### Storage Systems: Data Persistence

안드로이드의 파일 시스템 구조와 현대적인 데이터 저장 프로토콜인 **Scoped Storage**, **MediaStore**, **SAF(Storage Access Framework)**를 심층 분석합니다.

데이터의 무결성을 보장하면서도 사용자 개인정보 보호를 위해 강화된 시스템 제약을 어떻게 준수하고, 효율적인 대용량 파일 처리 및 암호화 전략을 수립할지가 핵심 목표입니다.

---

---

## 원자 노트

- [💡 Context: 저장소 권한의 대변화](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems/01-context-%EC%A0%80%EC%9E%A5%EC%86%8C-%EA%B6%8C%ED%95%9C%EC%9D%98-%EB%8C%80%EB%B3%80%ED%99%94.md)
- [저장소 종류](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems/02-%EC%A0%80%EC%9E%A5%EC%86%8C-%EC%A2%85%EB%A5%98.md)
- [Scoped Storage (Android 10+)](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems/03-scoped-storage-android-10.md)
- [파일 시스템 구조](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems/04-%ED%8C%8C%EC%9D%BC-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EA%B5%AC%EC%A1%B0.md)
- [데이터 저장 방법 선택](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems/05-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%80%EC%9E%A5-%EB%B0%A9%EB%B2%95-%EC%84%A0%ED%83%9D.md)
- [SharedPreferences](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems/06-sharedpreferences.md)
- [DataStore (권장)](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems/07-datastore-%EA%B6%8C%EC%9E%A5.md)
- [Room Database](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems/08-room-database.md)
- [파일 암호화](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems/09-%ED%8C%8C%EC%9D%BC-%EC%95%94%ED%98%B8%ED%99%94.md)
- [저장소 공간 관리](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems/10-%EC%A0%80%EC%9E%A5%EC%86%8C-%EA%B3%B5%EA%B0%84-%EA%B4%80%EB%A6%AC.md)
- [백업과 복원](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems/11-%EB%B0%B1%EC%97%85%EA%B3%BC-%EB%B3%B5%EC%9B%90.md)
- [성능 최적화](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems/12-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94.md)
- [디버깅](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems/android-storage-systems-13-%EB%94%94%EB%B2%84%EA%B9%85.md)
- [See Also](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-systems/android-storage-systems-14-see-also.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
