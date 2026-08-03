---
title: chromeos-distribution-requires-a-separate-play-console-declaration
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-03 18:15:25 +09:00
date created: 2026-08-03 17:30:11 +09:00
---

## ChromeOS 전용 배포는 Play 콘솔에서 Chromebook 지원 여부를 별도로 선언한다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](01_inbox/mobile/android/07_platforms/android-platforms-and-form-factors.md)

관련 지도: [ChromeOS 고유 계약](01_inbox/mobile/android/07_platforms/chromeos/chromeos-contracts/chromeos-contracts.md)

### 핵심 정의

Google Play 콘솔은 앱이 Chromebook 에서 사용 가능한지 여부를 별도 설정(기기 카탈로그의 Chromebook 포함/제외)으로 관리한다. 앱이 특정 하드웨어 기능(예: 카메라, 특정 센서)을 필수로 선언했는데 대상 Chromebook 에 그 하드웨어가 없으면, 해당 기기는 자동으로 배포 대상에서 제외된다.

### 메커니즘

매니페스트의 `<uses-feature>` 선언이 필수(`required="true"`)로 되어 있는 하드웨어가 Chromebook 에 없으면(예: 카메라 없는 Chromebook 모델), Play 는 이 조합을 호환 불가로 판단해 자동으로 배포 대상에서 뺀다. 반대로 앱이 특별히 문제 되는 API 를 사용하지 않으면 별도 선언 없이도 Chromebook 사용자가 Play 스토어에서 검색·설치할 수 있다. Play 콘솔은 "기기 카탈로그"에서 어떤 Chromebook 모델이 실제로 배포 대상에 포함/제외되는지, 제외 사유가 무엇인지 확인할 수 있는 화면을 제공한다.

### 판단 기준

- 앱이 실제로는 선택적으로만 사용하는 하드웨어 기능(카메라, 특정 센서)을 `required="true"` 로 과도하게 선언하지 않는다. 이는 Chromebook 뿐 아니라 해당 하드웨어가 없는 휴대폰/태블릿 배포에도 영향을 준다.
- Chromebook 전용 UX 검증이 필요한 기능(파일 시스템 접근, 외부 디스플레이 대응)이 있다면 출시 전 Play 콘솔의 기기 카탈로그에서 실제 배포 대상 목록을 확인한다.
- "큰 화면 지원" Play 정책 요구사항(품질 등급)이 Chromebook 에도 적용되므로, large-screen 적응형 레이아웃 완성도가 배포 노출과 검색 순위에도 영향을 줄 수 있다는 점을 인지한다.

### 경계

- 이 노트는 배포 심사와 기기 카탈로그 조건을 다룬다. 실행 환경 자체의 창 매핑 방식은 [ChromeOS는 Android 앱을 컨테이너에서 실행하고 창을 데스크톱 윈도우로 매핑한다](01_inbox/mobile/android/07_platforms/chromeos/chromeos-contracts/chromeos-runs-android-apps-in-a-container-mapped-to-desktop-windows.md) 가 다룬다.
- 일반적인 Play 콘솔 배포 절차(서명, 트랙 구성)는 `03_packaging_deployment` 가 다룬다.

### 관찰 가능한 신호

Play 콘솔의 "기기 카탈로그" 화면에서 특정 Chromebook 모델이 "제외됨"으로 표시되면, 옆에 표시되는 제외 사유(하드웨어 기능 불일치 등)로 원인을 바로 확인할 수 있다.

### 공식 문서

- https://developer.android.com/topic/arc
- https://support.google.com/googleplay/android-developer/answer/9844486
