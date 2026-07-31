# 🐧 The Kernel: Androidisms

안드로이드 커널은 "Google Common Kernel"에서 파생됩니다. 주요 수정 사항은 **모바일 환경 (배터리, 터치, 메모리 부족)** 을 위해 추가되었습니다.

##### 1. Binder (IPC Driver)
- **Standard Linux**: System V IPC, Socket, DBus.
- **Android**: 프로세스 간 통신 (IPC) 이 너무 빈번해서 (Activity 실행, 센서 데이터 수신 등), 성능을 위해 커널 드라이버인 **Binder**를 만들었습니다.
    - **특징**: 데이터를 커널 공간에서 한 번만 복사합니다 (1-copy).
    - **보안**: 수신 측에서 `getCallingUid()` 로 발신자를 확실히 식별할 수 있습니다.

##### 2. Low Memory Killer Daemon (LMKD)
- **Standard Linux**: OOM Killer 는 시스템이 멈추기 직전에 가장 무거운 놈을 죽입니다.
- **Android**: 사용자 경험 (UX) 이 중요합니다. 메모리가 부족해지기 **전에** 우선순위가 낮은 앱 (Cached App) 부터 정리합니다.
    - `oom_adj_score`: 포그라운드 앱 (-1000) vs 백그라운드 앱 (900+). 점수가 높은 순으로 죽습니다.

##### 3. Wakelocks (Power Management)
- **Philosophy**: 안드로이드는 화면이 꺼지면 CPU 도 재웁니다 (Deep Sleep).
- **Problem**: 음악 앱은 화면이 꺼져도 노래를 틀어야 합니다.
- **Solution**: **Wakelock**을 잡아서 CPU 가 잠들지 못하게 막습니다. (배터리 소모의 주범)

---
