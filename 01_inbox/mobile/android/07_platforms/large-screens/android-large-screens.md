---
title: android-large-screens
tags: []
aliases: []
date modified: 2026-04-05 17:43:10 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [mobile-security](01_inbox/mobile/mobile-security.md) > [android-large-screens](01_inbox/mobile/android/07_platforms/large-screens/android-large-screens.md)

### Large Screens: Adaptive Layouts

태블릿, 폴더블, 가로 모드 및 데스크톱 환경(Samsung DeX, ChromeOS)에 대응하는 **Adaptive Layout** 설계 기법을 분석합니다.

단순히 화면을 크게 보여주는 것을 넘어, **WindowSizeClass**를 기반으로 최적화된 사용자 경험(UX)을 제공하고, Android 15 에서 강화된 **데스크톱 윈도우(Desktop Windowing)** 환경에서의 앱 안정성을 확보하는 것이 목표입니다.

---

---

## 원자 노트

- [💡 Context: 대화면 지원의 필연성](01_inbox/mobile/android/07_platforms/large-screens/android-large-screens/01-context-%EB%8C%80%ED%99%94%EB%A9%B4-%EC%A7%80%EC%9B%90%EC%9D%98-%ED%95%84%EC%97%B0%EC%84%B1.md)
- [화면 크기 분류](01_inbox/mobile/android/07_platforms/large-screens/android-large-screens/02-%ED%99%94%EB%A9%B4-%ED%81%AC%EA%B8%B0-%EB%B6%84%EB%A5%98.md)
- [WindowSizeClass](01_inbox/mobile/android/07_platforms/large-screens/android-large-screens/03-windowsizeclass.md)
- [Adaptive Layout](01_inbox/mobile/android/07_platforms/large-screens/android-large-screens/04-adaptive-layout.md)
- [폴더블 지원](01_inbox/mobile/android/07_platforms/large-screens/android-large-screens/05-%ED%8F%B4%EB%8D%94%EB%B8%94-%EC%A7%80%EC%9B%90.md)
- [멀티 윈도우](01_inbox/mobile/android/07_platforms/large-screens/android-large-screens/06-%EB%A9%80%ED%8B%B0-%EC%9C%88%EB%8F%84%EC%9A%B0.md)
- [Picture-in-Picture (PiP)](01_inbox/mobile/android/07_platforms/large-screens/android-large-screens/07-picture-in-picture-pip.md)
- [드래그 앤 드롭](01_inbox/mobile/android/07_platforms/large-screens/android-large-screens/08-%EB%93%9C%EB%9E%98%EA%B7%B8-%EC%95%A4-%EB%93%9C%EB%A1%AD.md)
- [키보드/마우스 지원](01_inbox/mobile/android/07_platforms/large-screens/android-large-screens/09-%ED%82%A4%EB%B3%B4%EB%93%9C-%EB%A7%88%EC%9A%B0%EC%8A%A4-%EC%A7%80%EC%9B%90.md)
- [데스크톱 모드 및 윈도우 (Desktop Windowing)](01_inbox/mobile/android/07_platforms/large-screens/android-large-screens/10-%EB%8D%B0%EC%8A%A4%ED%81%AC%ED%86%B1-%EB%AA%A8%EB%93%9C-%EB%B0%8F-%EC%9C%88%EB%8F%84%EC%9A%B0-desktop-windowing.md)
- [반응형 레이아웃 패턴](01_inbox/mobile/android/07_platforms/large-screens/android-large-screens/11-%EB%B0%98%EC%9D%91%ED%98%95-%EB%A0%88%EC%9D%B4%EC%95%84%EC%9B%83-%ED%8C%A8%ED%84%B4.md)
- [테스트](01_inbox/mobile/android/07_platforms/large-screens/android-large-screens/12-%ED%85%8C%EC%8A%A4%ED%8A%B8.md)
- [베스트 프랙티스](01_inbox/mobile/android/07_platforms/large-screens/android-large-screens/13-%EB%B2%A0%EC%8A%A4%ED%8A%B8-%ED%94%84%EB%9E%99%ED%8B%B0%EC%8A%A4.md)
- [See Also](01_inbox/mobile/android/07_platforms/large-screens/android-large-screens/android-large-screens-14-see-also.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
