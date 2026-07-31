---
title: android-modular-system
tags: []
aliases: []
date modified: 2026-04-05 17:43:11 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [mobile-security](01_inbox/mobile/mobile-security.md) > [android-modular-system](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system.md)

### Modular System: Mainline & APEX

안드로이드 OS 의 핵심 컴포넌트를 파편화 없이 업데이트할 수 있게 돕는 **Project Mainline**과 이를 가능케 하는 **APEX(Android Pony EXpress)** 모듈 시스템을 분석합니다.

제조사(OEM)의 OS 업데이트 주기와 관계없이 Google Play 를 통해 보안 패치와 신규 기능을 실시간으로 배포하는 원리를 이해하는 것이 목표입니다.

---

---

## 원자 노트

- [💡 Context: 파편화 방지와 보안 패치](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system/01-context-%ED%8C%8C%ED%8E%B8%ED%99%94-%EB%B0%A9%EC%A7%80%EC%99%80-%EB%B3%B4%EC%95%88-%ED%8C%A8%EC%B9%98.md)
- [Mainline 이란](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system/02-mainline-%EC%9D%B4%EB%9E%80.md)
- [APEX (Android Pony EXpress)](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system/03-apex-android-pony-express.md)
- [Mainline 모듈 목록](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system/04-mainline-%EB%AA%A8%EB%93%88-%EB%AA%A9%EB%A1%9D.md)
- [APEX 구조](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system/05-apex-%EA%B5%AC%EC%A1%B0.md)
- [APEX 빌드 (AOSP)](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system/06-apex-%EB%B9%8C%EB%93%9C-aosp.md)
- [APEX 설치 흐름](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system/07-apex-%EC%84%A4%EC%B9%98-%ED%9D%90%EB%A6%84.md)
- [APEX 확인](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system/08-apex-%ED%99%95%EC%9D%B8.md)
- [앱에서 모듈 버전 확인](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system/09-%EC%95%B1%EC%97%90%EC%84%9C-%EB%AA%A8%EB%93%88-%EB%B2%84%EC%A0%84-%ED%99%95%EC%9D%B8.md)
- [모듈 호환성](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system/10-%EB%AA%A8%EB%93%88-%ED%98%B8%ED%99%98%EC%84%B1.md)
- [SDK Extensions](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system/11-sdk-extensions.md)
- [모듈 업데이트 정책](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system/12-%EB%AA%A8%EB%93%88-%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8-%EC%A0%95%EC%B1%85.md)
- [롤백](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system/13-%EB%A1%A4%EB%B0%B1.md)
- [개발자 고려사항](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system/14-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EA%B3%A0%EB%A0%A4%EC%82%AC%ED%95%AD.md)
- [Treble](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system/15-treble.md)
- [GKI (Generic Kernel Image)](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system/16-gki-generic-kernel-image.md)
- [See Also](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-modular-system/17-see-also.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
