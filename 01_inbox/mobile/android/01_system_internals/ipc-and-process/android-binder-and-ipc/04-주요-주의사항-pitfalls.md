# 🚨 주요 주의사항 (Pitfalls)

- **TransactionTooLargeException**: 1MB 제한을 초과하면 발생합니다. 비트맵과 같은 대용량 데이터는 Intent 에 직접 담지 말고 `ContentProvider` URI 나 `FileDescriptor` 를 활용해야 합니다.
- **Binder Thread Pool Starvation**: 모든 Binder 스레드(기본 16 개)가 작업 중이면 시스템의 호출에 응답하지 못해 **ANR**이 발생할 수 있습니다.
- **Deadlock**: 클라이언트와 서버가 서로의 응답이나 락(Lock) 해제를 기다리며 무한 대기에 빠지는 상황을 주의해야 합니다.

---
