---
title: android-process-and-memory
tags: []
aliases: []
date modified: 2026-04-05 17:42:46 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [[mobile-security]] > [[android-process-and-memory]]

### Process & Memory Management: Systems Architecture

안드로이드의 고유한 프로세스 생성 매커니즘과 효율적인 메모리 관리 기법을 상세히 다룹니다. 시스템의 아키텍처적 배경은 [[android-architecture-stack]] 및 [[android-foundations]] 를 참고하시기 바랍니다.

---

#### 💡 Context: 왜 모바일 전용 관리가 필요한가?

모바일 기기는 배터리와 RAM 자원이 매우 한정적입니다. 안드로이드는 이를 최적화하기 위해 리눅스 커널 위에 독자적인 레이어(Zygote, LMKD 등)를 구축했습니다.

- **Fast App Launch**: 모든 앱을 처음부터 새로 시작하는 대신, 공통 라이브러리가 미리 로드된 부모 프로세스(**Zygote**)에서 복제(fork)하여 시작 시간을 단축합니다.
- **Efficient Memory Sharing**: **Copy-on-Write (COW)** 방식을 통해 여러 앱이 동일한 시스템 리소스를 메모리 상에서 공유하도록 하여 전체 메모리 사용량을 절감합니다.
- **Predictable Performance**: **LMKD(Low Memory Killer Daemon)**가 시스템 전반의 메모리 압력을 감시하며, 우선순위가 낮은 프로세스부터 선제적으로 종료하여 시스템의 반응성을 유지합니다.

---

#### 🏗️ 프로세스 생성: Zygote Fork

Zygote 는 안드로이드 모든 앱 프로세스의 시조입니다.

1. **Preload**: 부팅 시 핵심 프레임워크 클래스와 리소스를 메모리에 적재합니다.
2. **Socket Listen**: 새로운 프로세스 생성 요청을 대기합니다.
3. **Fork**: 요청이 오면 자신을 복제하여 새로운 앱 프로세스를 만듭니다. 이때 자식 프로세스는 부모의 메모리 상태를 그대로 이어받습니다.

---

#### ⚖️ 프로세스 우선순위 (oom_adj)

시스템은 가용 메모리가 부족해지면 `oom_adj` 점수가 높은 프로세스부터 종료합니다.

- **Foreground (ADJ 0)**: 사용자가 현재 상호작용 중인 앱. 절대로 종료되지 않아야 합니다.
- **Visible (ADJ 100)**: 화면에 보이지만 포커스는 없는 앱. (예: 반투명 다이얼로그 뒤의 Activity)
- **Service (ADJ 200~500)**: 포그라운드 서비스 등이 실행 중인 중요 프로세스.
- **Cached (ADJ 900~999)**: 백그라운드에 있는 앱. 메모리가 필요할 때 가장 먼저 정리되는 대상입니다.

---

#### 🛡️ 보안: 프로세스 격리와 샌드박스

- **UID Isolation**: 각 앱은 설치 시 부여받은 고유한 **UID**를 기반으로 샌드박스화됩니다. 다른 앱의 데이터나 프로세스에 직접 접근할 수 없습니다.
- **Isolated Process**: 극도의 보안이 필요한 작업(예: 웹 브라우저 렌더링)을 위해 권한이 거의 없는 특수 프로세스(`isolatedProcess="true"`)를 생성할 수 있습니다.

---

#### 📚 연관 문서 및 심화 학습
- [[android-zygote-and-runtime]] - Zygote 와 ART 런타임 상세
- [[android-activity-manager-and-system-services]] - 프로세스의 생사여탈권을 쥔 AMS/ATMS
- [[android-binder-and-ipc]] - 멀티 프로세스 앱 간의 통신 기술
- [[android-performance-and-debug]] - 메모리 누수 진단 및 프로파일링 실전
- [[mobile-android-foundation-security]] - 샌드박싱과 유저 ID 기반 보안 아키텍처
