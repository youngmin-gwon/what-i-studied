---
title: android-modular-system
tags: []
aliases: []
date modified: 2026-04-05 17:43:11 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [[mobile-security]] > [[android-modular-system]]

### Modular System: Mainline & APEX

안드로이드 OS 의 핵심 컴포넌트를 파편화 없이 업데이트할 수 있게 돕는 **Project Mainline**과 이를 가능케 하는 **APEX(Android Pony EXpress)** 모듈 시스템을 분석합니다.

제조사(OEM)의 OS 업데이트 주기와 관계없이 Google Play 를 통해 보안 패치와 신규 기능을 실시간으로 배포하는 원리를 이해하는 것이 목표입니다.

---

---

## 원자 노트

- [[01-context-파편화-방지와-보안-패치|💡 Context: 파편화 방지와 보안 패치]]
- [[02-mainline-이란|Mainline 이란]]
- [[03-apex-android-pony-express|APEX (Android Pony EXpress)]]
- [[04-mainline-모듈-목록|Mainline 모듈 목록]]
- [[05-apex-구조|APEX 구조]]
- [[06-apex-빌드-aosp|APEX 빌드 (AOSP)]]
- [[07-apex-설치-흐름|APEX 설치 흐름]]
- [[08-apex-확인|APEX 확인]]
- [[09-앱에서-모듈-버전-확인|앱에서 모듈 버전 확인]]
- [[10-모듈-호환성|모듈 호환성]]
- [[11-sdk-extensions|SDK Extensions]]
- [[12-모듈-업데이트-정책|모듈 업데이트 정책]]
- [[13-롤백|롤백]]
- [[14-개발자-고려사항|개발자 고려사항]]
- [[15-treble|Treble]]
- [[16-gki-generic-kernel-image|GKI (Generic Kernel Image)]]
- [[17-see-also|See Also]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
