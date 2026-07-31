---
title: android-jetpack-architecture
tags: []
aliases: []
date modified: 2026-04-05 17:43:08 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [mobile-security](01_inbox/mobile/mobile-security.md) > [android-jetpack-architecture](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture.md)

### Jetpack Architecture: Modern App Foundations

Google 이 권장하는 **안드로이드 앱 아키텍처 가이드**와 이를 지탱하는 **Jetpack** 라이브러리 모음을 분석합니다.

현대적인 안드로이드 개발은 단순히 기능을 구현하는 것을 넘어, **관심사 분리(Separation of Concerns)**와 **데이터 흐름의 단방향성(UDA)**을 유지하는 것이 핵심입니다.

---

---

## 원자 노트

- [💡 Context: 왜 Jetpack 아키텍처인가?](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture/01-context-%EC%99%9C-jetpack-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98%EC%9D%B8%EA%B0%80.md)
- [아키텍처 개요](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture/02-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98-%EA%B0%9C%EC%9A%94.md)
- [ViewModel](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture/03-viewmodel.md)
- [LiveData (Legacy API)](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture/04-livedata-legacy-api.md)
- [StateFlow (Kotlin Coroutines)](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture/05-stateflow-kotlin-coroutines.md)
- [Room Database](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture/06-room-database.md)
- [WorkManager](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture/07-workmanager.md)
- [Compose Navigation (Type-safe / Modern ✅)](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture/08-compose-navigation-type-safe-modern.md)
- [Hilt (Dependency Injection)](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture/09-hilt-dependency-injection.md)
- [Lifecycle](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture/10-lifecycle.md)
- [DataBinding (Legacy)](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture/11-databinding-legacy.md)
- [아키텍처 패턴](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture/12-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98-%ED%8C%A8%ED%84%B4.md)
- [더 보기](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture/13-%EB%8D%94-%EB%B3%B4%EA%B8%B0.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
