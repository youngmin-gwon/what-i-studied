---
title: android-large-screens
tags: []
aliases: []
date modified: 2026-04-05 17:43:10 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [[mobile-security]] > [[android-large-screens]]

### Large Screens: Adaptive Layouts

태블릿, 폴더블, 가로 모드 및 데스크톱 환경(Samsung DeX, ChromeOS)에 대응하는 **Adaptive Layout** 설계 기법을 분석합니다.

단순히 화면을 크게 보여주는 것을 넘어, **WindowSizeClass**를 기반으로 최적화된 사용자 경험(UX)을 제공하고, Android 15 에서 강화된 **데스크톱 윈도우(Desktop Windowing)** 환경에서의 앱 안정성을 확보하는 것이 목표입니다.

---

---

## 원자 노트

- [[01-context-대화면-지원의-필연성|💡 Context: 대화면 지원의 필연성]]
- [[02-화면-크기-분류|화면 크기 분류]]
- [[03-windowsizeclass|WindowSizeClass]]
- [[04-adaptive-layout|Adaptive Layout]]
- [[05-폴더블-지원|폴더블 지원]]
- [[06-멀티-윈도우|멀티 윈도우]]
- [[07-picture-in-picture-pip|Picture-in-Picture (PiP)]]
- [[08-드래그-앤-드롭|드래그 앤 드롭]]
- [[09-키보드-마우스-지원|키보드/마우스 지원]]
- [[10-데스크톱-모드-및-윈도우-desktop-windowing|데스크톱 모드 및 윈도우 (Desktop Windowing)]]
- [[11-반응형-레이아웃-패턴|반응형 레이아웃 패턴]]
- [[12-테스트|테스트]]
- [[13-베스트-프랙티스|베스트 프랙티스]]
- [[14-see-also|See Also]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
