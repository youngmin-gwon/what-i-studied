# Init 과 Service Lifecycle

상위 노트: [[android-init-and-services]]

`init` 은 안드로이드 부팅 후 **가장 먼저 실행되는 프로세스**(PID 1)다. 모든 시스템 서비스를 시작하고, 파일시스템을 마운트하며, [[selinux]] 정책을 로드하고, property 시스템을 관리한다. Unix/Linux 전통의 init 프로세스 역할을 하면서도 안드로이드 고유의 요구사항을 반영한 독특한 구조를 가진다.

### 왜 init 이 중요한가

#### PID 1 의 특수성

Unix/Linux 에서 PID 1 은 특별한 의미를 가진다:

1. **커널이 직접 실행**: 부트로더 → 커널 → `/init` 실행
2. **절대 종료 불가**: PID 1 이 종료하면 커널 패닉
3. **고아 프로세스 수양**: 부모가 죽은 프로세스의 새 부모가 됨
4. **시그널 무시**: 일반 시그널로 종료 불가

#### 안드로이드 init 의 독특한 역할

**표준 Linux init** (systemd, SysV init):

- 서비스 시작/정지
- 런레벨 관리
- 의존성 해결

**Android init 추가 기능**:

- **Property 시스템**: key-value 저장소 (`setprop`/`getprop`)
- **Ueventd**: 커널 디바이스 이벤트 처리 (`/dev` 노드 생성)
- **[[selinux]] 강제**: 정책 로딩 및 컨텍스트 설정
- **파일 암호화**: FBE(File-Based Encryption) 조기 마운트
- **Vendor 분리**: [[android-hal-and-kernel#Treble 아키텍처|Treble]] 지원

---
