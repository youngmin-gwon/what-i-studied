# Play Feature Delivery는 동적 기능 모듈의 설치 시점을 정한다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [Play Delivery 계약](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/play-delivery-contracts.md)
관련 노트: [Dynamic Feature Module은 base module에 의존하는 선택 기능 단위다](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/dynamic-feature-module-is-optional-feature-unit-dependent-on-base.md), [Delivery mode는 기능 필수성, 조건, 런타임 요청으로 선택한다](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/delivery-mode-is-selected-by-necessity-condition-and-runtime-request.md)

## 한 문장 정의

Play Feature Delivery는 Android App Bundle을 Google Play가 기기별 split APK로
배포하는 구조 위에서, 동적 기능 모듈을 언제 설치할지 결정하는 체계다.

## 문제와 목적

- 기본 실행에 필요하지 않은 기능을 초기 설치에서 제외할 수 있다.
- 기능을 모듈 단위로 분리해 설치 크기와 첫 실행 시간을 관리한다.
- 모듈별로 설치 시 포함, 조건부 포함, 런타임 요청을 선택한다.
- 큰 바이너리나 드문 기능은 필요 시점에 다운로드하도록 사용자 여정을 설계한다.

## 구성 요소

| 구성 요소 | 책임 |
| --- | --- |
| base module | 앱의 공통 코드, 진입점, 필수 리소스 |
| dynamic feature module | 코드와 리소스를 담은 선택 기능 모듈 |
| Android App Bundle | Play에 업로드하는 단일 게시 아티팩트 |
| Play Feature Delivery Library | 런타임 모듈 요청과 상태 확인 |
| bundletool | 로컬 APK set 생성과 split 구조 검증 |

동적 기능 모듈은 base module에 의존한다.
공통 코드나 여러 기능이 반드시 공유하는 리소스는 base로 이동한다.
기능 모듈은 다른 기능 모듈의 존재를 전제로 설계하지 않는다.

## 배포 선택

1. `install-time`: 설치가 끝날 때 기능을 바로 사용할 수 있다.
2. conditional install-time: 국가, API, 하드웨어 등 조건을 만족할 때만 설치한다.
3. `on-demand`: 앱이 런타임에 요청한 뒤 다운로드하고 설치한다.

`fast-follow`는 동적 기능 모듈의 일반 선택지가 아니다.
설치 직후 자동으로 받는 모드는 Play Asset Delivery의 asset pack에서 사용한다.
따라서 실행 코드 기능과 대용량 게임 리소스를 같은 표로 섞지 않는다.

## 적용 순서

먼저 모듈 경계를 정하고 base에서 독립적으로 빌드되는지 확인한다.
그 다음 기본값인 install-time으로 기능을 출시해 모듈화 위험을 줄인다.
다운로드 UI와 실패 복구를 구현한 뒤 on-demand로 전환한다.
초기 설치에서 제외할 수 있는 지역·기기 전용 기능에는 conditional을 검토한다.

## 공식 문서

- [Overview of Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery)
- [Configure on-demand delivery](https://developer.android.com/guide/playcore/feature-delivery/on-demand)
- [Configure conditional delivery](https://developer.android.com/guide/playcore/feature-delivery/conditional)
