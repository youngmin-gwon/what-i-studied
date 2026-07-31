---
title: android-app-components-deep-dive
tags: []
aliases: []
date modified: 2026-07-31 15:17:52 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [[mobile-security]] > [[android-app-components-deep-dive]]

### App Components: System Architecture

안드로이드 앱의 4 대 핵심 컴포넌트(Activity, Service, BroadcastReceiver, ContentProvider)와 이들을 유기적으로 연결하는 시스템 아키텍처를 심층 분석합니다.

단순히 클래스를 상속받는 것을 넘어, 안드로이드 OS 가 앱 프로세스를 관리하고 컴포넌트 간 경계를 어떻게 유지하는지 이해하는 것이 목표입니다.

---

---

## 원자 노트

- [[01-context-4-대-컴포넌트의-역할|💡 Context: 4 대 컴포넌트의 역할]]
- [[02-activity-생명주기-상세|Activity 생명주기 상세]]
- [[03-service-심화|Service 심화]]
- [[04-broadcastreceiver-상세|BroadcastReceiver 상세]]
- [[05-contentprovider-심화|ContentProvider 심화]]
- [[06-컴포넌트-간-통신|컴포넌트 간 통신]]
- [[07-백그라운드-작업-선택-가이드|백그라운드 작업 선택 가이드]]
- [[08-성능-최적화|성능 최적화]]
- [[android-app-components-deep-dive-09-디버깅|디버깅]]
- [[10-androidmanifest-xml-상세|AndroidManifest.xml 상세]]
- [[11-see-also|See Also]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
