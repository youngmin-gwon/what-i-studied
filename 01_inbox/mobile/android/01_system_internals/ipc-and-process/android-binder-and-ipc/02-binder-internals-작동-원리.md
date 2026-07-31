# ⚙️ Binder Internals: 작동 원리

Binder 는 단순한 직렬화 도구가 아닌, 핵심 **커널 드라이버(`/dev/binder`)**입니다.

1. **Client**: `transact()` 를 호출하고 응답이 올 때까지 스레드가 블로킹(Blocking)됩니다.
2. **Kernel Driver**: 데이터를 발신자의 메모리에서 수신자의 주소 공간에 매핑된 **Binder Buffer**로 복사합니다.
3. **Server**: 미리 구성된 **Binder Thread Pool** 내의 스레드가 깨어나 `onTransact()` 를 통해 요청을 처리하고 결과를 반환합니다.

---
