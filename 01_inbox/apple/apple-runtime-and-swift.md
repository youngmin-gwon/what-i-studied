---
title: apple-runtime-and-swift
tags: [apple, objc, runtime, swift]
aliases: []
date modified: 2025-12-16 16:15:46 +09:00
date created: 2025-12-16 16:08:12 +09:00
---

## Runtime & Swift/ObjC apple runtime swift objc

앱 코드가 실제로 실행되는 길을 쉬운 말로 정리했다. 용어는 [[apple-glossary]].

### 실행 준비
- [[apple-glossary#dyld|dyld]] 가 [[apple-glossary#Mach-O|Mach-O]] 를 읽고 의존 라이브러리를 맵핑한다.
- 코드 서명/[[apple-glossary#Entitlement|Entitlement]]/[[apple-glossary#Sandbox|샌드박스]] 프로필을 검증한다.
- Swift 런타임이 타입/제네릭 메타데이터를, ObjC 런타임이 클래스/메서드를 등록한다.

### Swift vs Objective-C
- Swift: 값 타입, 안전한 기본값 (옵셔널), ABI 안정화 (iOS 12+/macOS 10.14+).
- ObjC: 동적 디스패치/메시지 전송, 카테고리/런타임 스위즐. 오래된 API 와 깊게 연결.
- 대부분 앱은 Swift 로 작성하고, 필요한 곳에 ObjC 브리징을 사용한다.

### 메모리 모델
- ARC 가 참조 카운트를 관리한다. 강/약 참조, 순환 참조를 피하기 위해 weak/unowned 를 사용.
- Swift Concurrency(actors, async/await) 는 데이터 경합을 줄인다. actor 는 내부 상태를 직렬화한다.

### 모듈과 프레임워크
- Swift 모듈 (.swiftmodule) 과 프레임워크 (.framework/.xcframework) 로 코드/리소스를 묶는다.
- Static vs Dynamic 프레임워크: 링크 방식과 앱 크기/시작 속도에 영향.
- XCFramework 는 여러 아키텍처/플랫폼을 하나로 묶은 포맷. SPM 패키지는 소스 기반 배포를 돕는다.
- dyld cache 에 포함되면 시작이 빠르지만, 앱 번들에 포함된 동적 프레임워크가 많으면 시작이 느려질 수 있다.

### 런타임 특징
- dynamic replacement(테스트/프리뷰), function inlining/optimizations, resilience(ABI 안정).
- ObjC KVO/KVC 는 동적 특성을 사용하므로 Swift 에서 사용 시 주의.
- Swift 리플렉션은 런타임 비용이 있으므로 로깅/디버깅 용도로 제한. Codable 은 런타임 메타데이터를 활용한다.
- @objc 노출은 브리징을 위해 필요하지만, 남용 시 바이너리 크기/성능에 영향.

### 예외/에러
- Swift Error 는 do/try/catch 로 잡는다. ObjC 예외 (NSException) 는 논리 에러/프로그래밍 오류에 가깝다.
- fatalError/assert 는 개발 중 버그를 드러내기 위해 사용.
- Result/async throws 를 통해 비동기 에러를 일관되게 표현. Task.cancelled 도 에러 흐름으로 처리.

### 진단/디버깅
- `po`/`lldb` 로 런타임 객체를 본다. Swift 리플렉션으로 타입 확인 가능.
- `malloc_history`, `leaks`, Instruments(Allocations/Leaks), Address Sanitizer, Thread Sanitizer 로 안정성을 확인.
- Swift Concurrency Runtime 은 `Tasks`/`Actors` 상태를 표시하는 디버그 지원을 제공한다.
- `DYLD_PRINT_STATISTICS` 로 로더 시간 측정, `OS_ACTIVITY_MODE=disable` 로 로그 노이즈 줄이기.
- Swift backtrace 는 `bt all` + 디버그 심볼로 확인. release 빌드는 최적화로 줄줄이 인라인될 수 있다.

### 성능 포인트
- 값 타입 구조체로 불필요한 힙 할당을 줄이고, Copy-on-Write 로 복사 비용을 완화.
- async/await 에서 불필요한 hop 최소화, Task.priority 로 QoS 조율.
- ObjC 메시지 전송은 동적이라 약간 느리지만 유연; 성능이 중요한 루프에는 Swift/구조체 사용 권장.
- @inlinable/@usableFromInline 로 모듈 경계 최적화 제어. Whole-module optimization 빌드 사용.
- String/Collection 은 값 타입이지만 내부 버퍼 공유를 통해 성능을 유지한다. 무거운 조작은 Substring/indices 로 신중히.

### 링크

[[apple-architecture-stack]], [[apple-interprocess-and-xpc]], [[apple-performance-and-debug]], [[apple-build-and-distribution]].
