---
title: downloadable-fonts-contracts
tags: ["android", "android/app-framework"]
aliases: ["Downloadable Fonts 접근 계약"]
date modified: 2026-08-05 10:00:00 +09:00
date created: 2026-08-05 10:00:00 +09:00
---

## Downloadable Fonts 접근 계약

이 지도는 Downloadable Fonts API가 폰트를 APK에 번들하지 않고 폰트 제공자 앱(대표적으로 Google Play services의 Google Fonts provider)에게 요청 시점에 위임하는 계약을, 배달 모델(왜 요청 시점에 가져오는가)과 요청 API 형태·실패 처리(어떻게 요청하고 실패에 대비하는가) 두 가지로 나눈다.

### 읽는 순서

1. [Downloadable Fonts는 폰트를 APK에 번들하지 않고 폰트 제공자 앱에 요청 시점에 위임한다](./downloadable-fonts-defer-font-delivery-to-a-provider-app-instead-of-bundling-in-the-apk.md)에서 APK 크기 절감과 제공자 캐시 공유라는 이 API의 존재 이유를 먼저 본다.
2. [폰트 요청은 XML font-family 선언이나 FontRequest 코드 경로를 따르며 실패 시 폴백이 필요하다](./font-requests-go-through-xml-font-family-or-fontrequest-code-and-need-a-fallback-on-failure.md)에서 두 요청 경로와 `onTypefaceRequestFailed()` 실패 처리 계약을 본다.

### 문제 분류

| 증상 또는 질문 | 먼저 확인할 경계 |
| --- | --- |
| 특정 기기에서만 텍스트가 시스템 기본 폰트로 보인다 | Google Play services 미설치/구버전이거나 요청이 실패했는데 폴백 폰트를 준비하지 않았는지 |
| 첫 실행 시 잠깐 다른 폰트가 보였다가 원하는 폰트로 바뀐다 | 폰트가 비동기로 다운로드/캐싱되는 동안의 정상적인 전환인지 |
| release 빌드에서만 폰트 요청이 실패한다 | `fontProviderCerts`(또는 `FontRequest`의 `certs`)가 release 서명 인증서를 포함하는지 |
| APK 크기를 줄이려 폰트를 뺐더니 오프라인 최초 실행에서 텍스트가 깨진다 | 오프라인/실패 상황을 대비한 번들 폴백 폰트를 준비했는지 |

### 책임 경계

- 이 지도는 앱이 Downloadable Fonts API로 폰트를 요청·캐싱·폴백하는 접근 계약만 다룬다. 폰트 파일 자체의 hinting, 서브셋팅, 커스텀 폰트 제공자 서버 구현은 다루지 않는다.
- 시스템 UI 전반의 폰트 렌더링 파이프라인(글리프 래스터화, 텍스트 셰이핑)은 이 지도의 범위가 아니다. 이 지도는 "어떤 폰트 데이터를 어디서 가져오는가"라는 접근 계약만 다룬다.

### 노트 목록

- [Downloadable Fonts는 폰트를 APK에 번들하지 않고 폰트 제공자 앱에 요청 시점에 위임한다](./downloadable-fonts-defer-font-delivery-to-a-provider-app-instead-of-bundling-in-the-apk.md)
- [폰트 요청은 XML font-family 선언이나 FontRequest 코드 경로를 따르며 실패 시 폴백이 필요하다](./font-requests-go-through-xml-font-family-or-fontrequest-code-and-need-a-fallback-on-failure.md)

검증일: 2026-08-05. [Use downloadable fonts](https://developer.android.com/develop/ui/views/text-and-emoji/downloadable-fonts)를 기준으로 확인했다.
