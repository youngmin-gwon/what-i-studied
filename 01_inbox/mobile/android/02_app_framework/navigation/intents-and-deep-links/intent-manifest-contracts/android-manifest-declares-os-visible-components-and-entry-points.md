---
title: android-manifest-declares-os-visible-components-and-entry-points
tags: [android, android/navigation, android/manifest]
aliases: ["AndroidManifest는 OS에 노출되는 컴포넌트와 진입점을 선언한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## AndroidManifest 는 OS 에 노출되는 컴포넌트와 진입점을 선언한다

상위 문서: [Intent & Manifest 계약](intent-manifest-contracts.md)

---

### 개념과 필요성 (What & Why)

1. **개념 (What)**:
   - **`AndroidManifest.xml`**은 안드로이드 OS의 **ActivityManagerService(AMS)** 및 **PackageManagerService(PMS)**에게 애플리케이션의 4대 주요 컴포넌트(Activity, Service, BroadcastReceiver, ContentProvider)와 진입점, 권한 선언, 런타임 제약 조건을 전달하는 **최상위 청사진 선언 파일**이다.
2. **필요성 (Why)**:
   - **안드로이드 OS 진입점 등록**: 안드로이드 애플리케이션에는 C/C++나 Java의 전통적인 단일 `main()` 함수 진입점이 없다. 대신 OS가 Manifest에 등록된 컴포넌트 태그를 파싱하여 론처 아이콘 진입점, 푸시 수신점, 딥링크 진입점을 동적으로 구동한다.

---

### 주요 선언 구성 요소 (How)

- `<activity>`: UI 화면 컴포넌트.
- `<service>`: 백그라운드 작업 처리 컴포넌트.
- `<receiver>`: 시스템 이벤트(부팅 완료, 배터리 상태) 및 브로드캐스트 메시지 수신기.
- `<provider>`: 구조화된 파일/데이터베이스 공유 인터페이스.
- `<queries>`: Android 11+ 패키지 가시성 통제 구문.

---

### 관련 상위 및 연관 노트

- 상위 계약: [Intent & Manifest 계약](intent-manifest-contracts.md)
- 연관 계약: [Exported 속성은 외부 컴포넌트 경계를 정의한다](exported-attribute-defines-external-component-boundary.md)
