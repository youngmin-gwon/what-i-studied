---
title: android-app-components-deep-dive
tags: []
aliases: []
date modified: 2026-07-31 15:17:52 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [mobile-security](01_inbox/mobile/mobile-security.md) > [android-app-components-deep-dive](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components-deep-dive.md)

### App Components: System Architecture

안드로이드 앱의 4 대 핵심 컴포넌트(Activity, Service, BroadcastReceiver, ContentProvider)와 이들을 유기적으로 연결하는 시스템 아키텍처를 심층 분석합니다.

단순히 클래스를 상속받는 것을 넘어, 안드로이드 OS 가 앱 프로세스를 관리하고 컴포넌트 간 경계를 어떻게 유지하는지 이해하는 것이 목표입니다.

---

---

## 원자 노트

- [💡 Context: 4 대 컴포넌트의 역할](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components-deep-dive/01-context-4-%EB%8C%80-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8%EC%9D%98-%EC%97%AD%ED%95%A0.md)
- [Activity 생명주기 상세](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components-deep-dive/02-activity-%EC%83%9D%EB%AA%85%EC%A3%BC%EA%B8%B0-%EC%83%81%EC%84%B8.md)
- [Service 심화](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components-deep-dive/03-service-%EC%8B%AC%ED%99%94.md)
- [BroadcastReceiver 상세](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components-deep-dive/04-broadcastreceiver-%EC%83%81%EC%84%B8.md)
- [ContentProvider 심화](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components-deep-dive/05-contentprovider-%EC%8B%AC%ED%99%94.md)
- [컴포넌트 간 통신](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components-deep-dive/06-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8-%EA%B0%84-%ED%86%B5%EC%8B%A0.md)
- [백그라운드 작업 선택 가이드](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components-deep-dive/07-%EB%B0%B1%EA%B7%B8%EB%9D%BC%EC%9A%B4%EB%93%9C-%EC%9E%91%EC%97%85-%EC%84%A0%ED%83%9D-%EA%B0%80%EC%9D%B4%EB%93%9C.md)
- [성능 최적화](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components-deep-dive/08-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94.md)
- [디버깅](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components-deep-dive/android-app-components-deep-dive-09-%EB%94%94%EB%B2%84%EA%B9%85.md)
- [AndroidManifest.xml 상세](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components-deep-dive/10-androidmanifest-xml-%EC%83%81%EC%84%B8.md)
- [See Also](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components-deep-dive/android-app-components-deep-dive-11-see-also.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
