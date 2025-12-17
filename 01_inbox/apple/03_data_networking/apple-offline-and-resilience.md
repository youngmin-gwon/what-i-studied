---
title: apple-offline-and-resilience
tags: [apple, network, offline, resilience, circuit-breaker, patterns]
aliases: []
date modified: 2025-12-18 01:50:00 +09:00
date created: 2025-12-16 16:09:23 +09:00
---

## Network Resilience Patterns

네트워크 코드는 "성공했을 때"가 아니라 "실패했을 때" 빛을 발합니다.
서버가 500 에러를 뱉거나, 와이파이가 1칸일 때 앱이 그냥 멈춰버린다면 그건 좋은 앱이 아닙니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **Circuit Breaker**: 서버가 아픈데 계속 요청을 날리면 서버는 더 빨리 죽습니다. 잠깐 요청을 멈춰주는 배려(Circuit Open)가 시스템 전체를 살립니다.
- **Exponential Backoff**: 실패했다고 바로 다시 시도하면 네트워크 폭주(Congestion)를 일으킵니다. 1초, 2초, 4초... 점진적으로 기다렸다가 재시도해야 합니다.
- **Idempotency**: "결제 요청"을 보냈는데 타임아웃이 났습니다. 다시 보내면 중복 결제가 될까요? (재시도해도 안전한가?)

---

### 🧱 Resilience Patterns (방어 기법)

#### 1. Retry with Exponential Backoff
가장 기본입니다. 실패 시 조금씩 더 오래 기다렸다가 재시도합니다.

```swift
func retry<T>(maxAttempts: Int, delay: Double, task: () async throws -> T) async throws -> T {
    for attempt in 1...maxAttempts {
        do {
            return try await task()
        } catch {
            if attempt == maxAttempts { throw error }
            let seconds = delay * pow(2.0, Double(attempt - 1)) // 1, 2, 4, 8...
            try await Task.sleep(nanoseconds: UInt64(seconds * 1_000_000_000))
        }
    }
    fatalError("Unreachable")
}
```

#### 2. Circuit Breaker (차단기)
집안에 누전이 되면 두꺼비집이 내려가서 불이 나는 걸 막죠. 앱도 마찬가지입니다.
- **구조**: `Closed`(정상) -> 에러 N회 -> `Open`(차단, 즉시 에러) -> 일정 시간 후 -> `Half-Open`(테스트) -> 성공 시 `Closed`.
- **효과**: 무의미한 네트워크/배터리 소모를 방지하고, 서버 회복 시간을 벌어줍니다.

#### 3. Idempotency Key (멱등성 키)
네트워크가 불안정할 때 POST 요청(생성/결제)이 두 번 들어갈 수 있습니다.
- 헤더에 `Idempotency-Key: UUID`를 담아 보냅니다.
- 서버는 "이미 처리된 키"라면 로직을 다시 실행하지 않고 저장된 결과를 리턴합니다.

---

### 🛤️ Offline Queue (Outbox)

"지금은 안 되지만 나중엔 되겠지."
사용자가 오프라인 상태에서 '좋아요'를 누르면, UI는 빨간색 하트로 바꾸고 요청은 큐에 넣습니다.

1. **Persist**: 큐는 메모리가 아니라 **디스크(Core Data/Realm)**에 저장해야 합니다. 앱이 꺼져도 날아가면 안 되니까요.
2. **Batch**: 연결이 돌아오면 하나씩 보내지 말고 배열에 담아서(`Bulk Insert`) 한 방에 보내는 게 효율적입니다.
3. **Sequence**: 좋아요 -> 취소 -> 좋아요 순서가 꼬이면 안 됩니다. 타임스탬프나 순차 ID로 순서를 보장해야 합니다.

### 더 보기
- [[apple-networking-and-cloud]] - 네트워크 기본 원리
- [[apple-cloud-sync-patterns]] - 데이터 동기화 아키텍처
