---
title: authenticated-deep-links-require-pending-destination-and-back-stack
tags: [android, android/deep-links, android/navigation]
aliases: ["인증이 필요한 딥 링크의 pending destination 과 백 스택"]
date modified: 2026-08-03 18:11:25 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 인증이 필요한 딥 링크의 pending destination 과 백 스택

상위 문서: [Deep Link 계약](./deep-link-contracts.md)

관련 노트: [Navigation 3 deep link는 URI를 NavKey로 변환한다](../../navigation3/navigation3-contracts/navigation3-deep-link-converts-uri-to-navkey.md)

### 문제

딥 링크는 사용자를 특정 목적지로 바로 데려오지만 그 목적지가 로그인을 요구할 수 있다.

이때 URI 를 버리면 로그인 후 사용자가 원래 작업을 다시 찾아야 한다.

URI 를 무검증으로 저장하면 외부 입력이 임의의 내부 화면으로 전환될 수 있다.

따라서 인증 전 목적지와 인증 후 복귀 정책을 명시적으로 설계해야 한다.

### 안전한 처리 흐름

앱은 외부 URI 를 먼저 파싱하고 허용된 host 와 path 인지 검증한다.

그 다음 해당 리소스가 공개인지 인증이 필요한지 판정한다.

인증이 필요하면 전체 URI 를 무조건 저장하지 말고 검증된 목적지 모델로 변환한다.

예를 들어 `Product(productId)` 처럼 허용된 내부 타입으로 pending destination 을 표현한다.

로그인 성공 시 저장한 목적지를 한 번만 소비하고 정상적인 라우터를 통해 이동한다.

로그인 취소나 세션 만료 시에는 안전한 기본 화면으로 돌아간다.

### 백 스택 의미

딥 링크로 앱이 새로 시작될 때 사용자는 도착 화면에서 뒤로 가기를 기대한다.

그러나 실제 task 에 부모 화면이 없으면 뒤로 가기가 앱 종료로 이어질 수 있다.

필요한 경우 합성 백 스택을 만들어 홈이나 상위 목록을 부모로 제공한다.

Navigation 라이브러리를 사용한다면 외부 진입 시의 start destination 정책도 확인한다.

기존 task 가 살아 있을 때 새 Intent 를 어디에 전달할지도 launchMode 와 라우터가 결정한다.

백 스택은 편의를 위한 화면 나열이 아니라 사용자의 복귀 경로를 보장하는 계약이다.

### 상태와 데이터

딥 링크가 가리키는 리소스는 진입 순간 서버에서 다시 조회한다.

상품 삭제, 권한 변경, 만료된 초대처럼 URI 생성 시점과 현재 상태가 다를 수 있다.

조회 실패는 무한 리디렉션 대신 명확한 오류와 대안을 제공해야 한다.

민감한 토큰을 URI query 에 넣지 않고, 필요하면 짧은 수명의 교환 코드로 제한한다.

백그라운드에서 전달된 Intent 도 동일한 인증과 입력 검증을 적용한다.

### 구현 체크리스트

대상 URI 는 [Android 딥 링크는 외부 URI 계약이다](./deep-link-is-external-uri-contract.md) 의 규칙을 따른다.

검증된 HTTPS 연결은 [Android App Link는 검증된 HTTPS 딥 링크다](./app-link-is-verified-https-deep-link.md) 를 따른다.

공개 목적지와 인증 목적지를 구분한다.

pending destination 을 타입 안전한 값으로 저장하고 한 번만 소비한다.

로그인 취소, 만료, 잘못된 리소스, 뒤로 가기 동작을 각각 테스트한다.

### 결론

딥 링크의 목적지는 화면 하나가 아니라 사용자가 완수하려는 여정이다.

인증 경계와 합성 백 스택을 함께 설계해야 외부 진입이 내부 흐름을 깨뜨리지 않는다.
