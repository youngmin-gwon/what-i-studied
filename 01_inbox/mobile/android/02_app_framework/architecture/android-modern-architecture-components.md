# Android 4대 컴포넌트와 현대 아키텍처 가이드

이 문서는 안드로이드 앱의 전통적인 핵심 구성 요소였던 **Activity, Service, BroadcastReceiver, ContentProvider**를 바닥부터 설명하고,
왜 현대 Android 개발에서는 **Jetpack Compose, ViewModel, Kotlin Flow, WorkManager, App Functions,
Repository,
Room/DataStore** 중심의 구조로 이동했는지를 다룹니다.

---

## 원자 노트

- [[android-app-as-os-run-components|안드로이드 앱은 "OS가 실행하는 컴포넌트 묶음"이다]]
- [[android-four-components-overview|4대 컴포넌트 한눈에 보기]]
- [[activity-as-app-entry-boundary|Activity: 화면 그 자체에서 "앱의 대문"으로]]
- [[service-as-special-work-boundary|Service: 백그라운드 만능 도구에서 "특수 작업용 경계"로]]
- [[broadcastreceiver-as-boundary-event-handler|BroadcastReceiver: 시스템 방송 수신기에서 "경계 이벤트 처리기"로]]
- [[contentprovider-as-public-data-api|ContentProvider: 앱 간 데이터 공유 창구에서 "특수한 공개 API"로]]
- [[app-functions-as-modern-system-agent-boundary|App Functions: 시스템/AI agent에게 앱 기능을 공개하는 현대 경계]]
- [[why-android-architecture-became-modern|왜 현대 아키텍처로 바뀌었나?]]
- [[classic-components-to-modern-tools|전통 컴포넌트와 현대 도구 매핑]]
- [[android-practical-architecture-example|실무 아키텍처 예시]]
- [[when-to-use-classic-android-components-directly|언제 전통 컴포넌트를 직접 써야 하나?]]
- [[android-modern-architecture-flow-summary|전체 흐름 요약]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, 각 H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
