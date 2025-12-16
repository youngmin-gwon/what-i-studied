# Runtime & Swift/ObjC #apple #runtime #swift #objc

앱 코드가 실제로 실행되는 길을 쉬운 말로 정리했다. 용어는 [[apple-glossary]].

## 실행 준비
- [[apple-glossary#dyld|dyld]]가 [[apple-glossary#Mach-O|Mach-O]]를 읽고 의존 라이브러리를 맵핑한다.
- 코드 서명/[[apple-glossary#Entitlement|Entitlement]]/[[apple-glossary#Sandbox|샌드박스]] 프로필을 검증한다.
- Swift 런타임이 타입/제네릭 메타데이터를, ObjC 런타임이 클래스/메서드를 등록한다.

## Swift vs Objective-C
- Swift: 값 타입, 안전한 기본값(옵셔널), ABI 안정화(iOS 12+/macOS 10.14+).
- ObjC: 동적 디스패치/메시지 전송, 카테고리/런타임 스위즐. 오래된 API와 깊게 연결.
- 대부분 앱은 Swift로 작성하고, 필요한 곳에 ObjC 브리징을 사용한다.

## 메모리 모델
- ARC가 참조 카운트를 관리한다. 강/약 참조, 순환 참조를 피하기 위해 weak/unowned를 사용.
- Swift Concurrency(actors, async/await)는 데이터 경합을 줄인다. actor는 내부 상태를 직렬화한다.

## 모듈과 프레임워크
- Swift 모듈(.swiftmodule)과 프레임워크(.framework/.xcframework)로 코드/리소스를 묶는다.
- Static vs Dynamic 프레임워크: 링크 방식과 앱 크기/시작 속도에 영향.

## 런타임 특징
- dynamic replacement(테스트/프리뷰), function inlining/optimizations, resilience(ABI 안정).
- ObjC KVO/KVC는 동적 특성을 사용하므로 Swift에서 사용 시 주의.

## 예외/에러
- Swift Error는 do/try/catch로 잡는다. ObjC 예외(NSException)는 논리 에러/프로그래밍 오류에 가깝다.
- fatalError/assert는 개발 중 버그를 드러내기 위해 사용.

## 진단/디버깅
- `po`/`lldb`로 런타임 객체를 본다. Swift 리플렉션으로 타입 확인 가능.
- `malloc_history`, `leaks`, Instruments(Allocations/Leaks), Address Sanitizer, Thread Sanitizer로 안정성을 확인.
- Swift Concurrency Runtime은 `Tasks`/`Actors` 상태를 표시하는 디버그 지원을 제공한다.

## 성능 포인트
- 값 타입 구조체로 불필요한 힙 할당을 줄이고, Copy-on-Write로 복사 비용을 완화.
- async/await에서 불필요한 hop 최소화, Task.priority로 QoS 조율.
- ObjC 메시지 전송은 동적이라 약간 느리지만 유연; 성능이 중요한 루프에는 Swift/구조체 사용 권장.

## 링크
[[apple-architecture-stack]], [[apple-interprocess-and-xpc]], [[apple-performance-and-debug]], [[apple-build-and-distribution]].
