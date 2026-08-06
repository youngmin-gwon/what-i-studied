---
title: networking-contracts
tags: [android, android/data, android/networking]
aliases: ["네트워크 클라이언트 계층 계약"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## 네트워크 클라이언트 계층 계약

배경 지식: [HTTP 프로토콜](../../../../../../computer-science/networking/http-protocol.md)

네트워크 클라이언트 계층은 "서버에 어떤 요청을 보낼지 선언하는 계약(Retrofit: 안드로이드 타입 세이프 HTTP 클라이언트 라이브러리)"과 "실제로 그 요청을 전송하는 엔진(OkHttp: TLS 핸드셰이크 및 커넥션 풀링을 직접 다루는 저수준 통신 엔진)"을 나눠서 다룬다. 그 사이에 interceptor 체인이 인증·로깅·재시도를 끼워 넣고, suspend 함수로 선언한 호출은 coroutine 취소와 실제로 연결된다. 이 계층의 실패 분류는 [Android Data Layer](../../android-data-layer-map.md)의 offline-first 로컬 우선 쓰기 모델과 맞닿아 있다.

### 정본 노트

- [Retrofit 인터페이스는 API 계약을 선언하고 OkHttp가 실제 전송을 담당한다](./retrofit-interface-declares-api-contract-while-okhttp-executes-transport.md)
- [Interceptor 체인은 인증, 로깅, 재시도를 요청·응답 파이프라인에 끼워 넣는다](./interceptor-chain-inserts-cross-cutting-concerns-into-request-response-pipeline.md)
- [suspend API 호출의 취소는 호출자의 coroutine scope를 따라간다](./suspend-api-call-cancellation-follows-the-callers-coroutine-scope.md)
- [Timeout·재시도 정책은 UI에 노출할 실패 상태를 결정하고 offline-first 로컬 쓰기와 연결된다](./network-failure-policy-must-expose-retry-timeout-and-offline-state-to-ui.md)
- [gRPC는 Protobuf 기반 강타입 스트리밍 계약을 선언하고 REST는 단발성 request-response 계약에 머문다](./grpc-declares-typed-streaming-contract-while-rest-stays-single-shot-request-response.md)

### 읽는 기준

API 선언과 전송 계층이 왜 분리돼 있는지 궁금하면 Retrofit/OkHttp 노트로 간다. 인증 헤더나 로깅을 어디에 끼워 넣어야 할지 궁금하면 interceptor 노트로 간다. 화면을 벗어났는데 네트워크 요청이 실제로 멈추는지 궁금하면 suspend 취소 노트로 간다. timeout 과 재시도가 offline-first 동기화와 어떻게 연결되는지 궁금하면 마지막 노트로 간다. REST 대신 gRPC 를 쓸지 판단하려면 마지막 gRPC 노트로 간다.

### 중복 방지 규칙

- coroutine 자체의 수명·취소·구조적 동시성 모델은 [Coroutine 계약](../../async-flow/coroutines/coroutine-contracts.md) 에 둔다. 이 클러스터는 그 계약이 네트워크 호출에 어떻게 적용되는지만 다룬다.
- 로컬 우선 쓰기, WorkManager 지연 동기화, 충돌 해결 정책은 [Learning Spine 8장](../../../../00_foundations/learning-spine/08-data-storage-network-and-offline-recovery.md)과 [영속 저장소 계약](../../storage/persistence-contracts/persistence-contracts.md) 에 둔다. 이 클러스터는 그 흐름 중 "네트워크 클라이언트 계층"만 담당한다.
- 시스템 연결성(`ConnectivityManager`, `NetworkCapabilities`)과 네트워크 정책 디버깅은 [Android 연결성과 네트워크 지도](../../../../01_system_internals/connectivity/android-connectivity.md) 에 둔다.

상위 지도: [Android Data Layer는 데이터 흐름과 영속 저장소 Paging을 분리한다](../../android-data-layer-map.md)
