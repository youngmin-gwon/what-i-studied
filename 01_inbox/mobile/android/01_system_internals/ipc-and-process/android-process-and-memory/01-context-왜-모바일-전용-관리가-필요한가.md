# 💡 Context: 왜 모바일 전용 관리가 필요한가?

모바일 기기는 배터리와 RAM 자원이 매우 한정적입니다. 안드로이드는 이를 최적화하기 위해 리눅스 커널 위에 독자적인 레이어(Zygote, LMKD 등)를 구축했습니다.

- **Fast App Launch**: 모든 앱을 처음부터 새로 시작하는 대신, 공통 라이브러리가 미리 로드된 부모 프로세스(**Zygote**)에서 복제(fork)하여 시작 시간을 단축합니다.
- **Efficient Memory Sharing**: **Copy-on-Write (COW)** 방식을 통해 여러 앱이 동일한 시스템 리소스를 메모리 상에서 공유하도록 하여 전체 메모리 사용량을 절감합니다.
- **Predictable Performance**: **LMKD(Low Memory Killer Daemon)**가 시스템 전반의 메모리 압력을 감시하며, 우선순위가 낮은 프로세스부터 선제적으로 종료하여 시스템의 반응성을 유지합니다.

---
