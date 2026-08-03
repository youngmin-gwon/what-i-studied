---
title: deep-link-is-external-uri-contract
tags: [android, android/deep-links, android/navigation]
aliases: ["Android 딥 링크는 외부 URI 계약이다"]
date modified: 2026-08-03 18:11:26 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android 딥 링크는 외부 URI 계약이다

상위 문서: [Deep Link 계약](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-contracts.md)

관련 노트: [Intent는 컴포넌트 실행을 설명하는 메시지다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-describes-component-action-request.md)

### 핵심

딥 링크는 외부에서 전달된 URI 를 앱 내부의 특정 목적지로 연결하는 계약이다.

이 계약의 입력은 보통 `Intent.ACTION_VIEW` 와 URI 의 조합이다.

URI 는 화면 이름이 아니라 사용자가 도달하려는 리소스나 작업을 표현한다.

예를 들어 `https://www.example.com/product/42` 는 상품 42 를 가리킨다.

앱은 URI 를 받았을 때 해당 목적지를 찾고 필요한 상태를 준비해야 한다.

딥 링크의 성공은 앱이 실행되는 것보다 목적지 의미가 보존되는지로 판단한다.

### URI 계약의 구성

URI 계약에는 scheme, host, path, query, fragment 의 의미가 포함된다.

scheme 은 `https` 처럼 전송 방식과 외부 진입 표면을 정한다.

host 는 서비스의 소유 경계를 나타낸다.

path 는 리소스 종류와 계층을 표현한다.

query 는 필터나 캠페인 같은 부가 조건에 사용할 수 있다.

fragment 는 서버에 전달되지 않으므로 앱 내부 표시 상태에만 신중하게 사용한다.

각 구성 요소가 어떤 입력을 허용하고 거부하는지 문서화해야 한다.

### 선언과 라우팅의 분리

매니페스트의 `intent-filter` 는 앱이 어떤 외부 Intent 를 받을 수 있는지 선언한다.

실제 화면 선택과 매개변수 검증은 앱의 라우팅 계층이 담당한다.

따라서 필터가 매칭되었다고 해서 URI 가 유효한 목적지라는 뜻은 아니다.

라우터는 path 변수의 형식, query 의 허용 목록, 로그인 요구를 검사해야 한다.

알 수 없는 경로는 오류 화면이나 웹 fallback 으로 명시적으로 처리한다.

라우팅 결과는 외부 입력에 의해 임의의 내부 명령이 실행되지 않도록 제한한다.

### 설계 원칙

URI 는 안정적인 공개 계약이므로 내부 클래스명이나 화면 구현명을 넣지 않는다.

리소스 식별자는 서버와 앱이 함께 해석할 수 있는 형식을 사용한다.

동일 URI 를 여러 번 열어도 같은 의미의 목적지에 도달하도록 멱등성을 고려한다.

앱이 설치되지 않은 경우에도 웹 URL 이 유효한 페이지로 동작하도록 설계한다.

웹 URL 을 앱에서 처리할 때도 웹의 접근 권한과 앱의 인증 상태를 다시 확인한다.

### 관련 주제

검증된 HTTPS 계약은 [Android App Link는 검증된 HTTPS 딥 링크다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/app-link-is-verified-https-deep-link.md) 에서 다룬다.

외부 URI 선언과 서버 검증 파일의 경계는 [매니페스트 선언과 assetlinks.json의 역할](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/manifest-and-assetlinks-have-distinct-roles.md) 에 정리한다.

공식 개요는 [Android App Links 개요](https://developer.android.com/training/app-links/about) 를 참고한다.

### 판단 기준

새 딥 링크를 추가할 때 먼저 공개 URI 와 목적지 의미를 정의한다.

그 다음 허용할 scheme, host, path 범위를 매니페스트에 선언한다.

마지막으로 인증, 오류, 미설치, 뒤로 가기 동작을 테스트 시나리오에 넣는다.

딥 링크는 화면 이동 단축키가 아니라 외부 시스템과 앱 사이의 장기 계약이다.
