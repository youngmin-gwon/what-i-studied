---
title: kernel
tags: [os, kernel, linux, operating-systems]
aliases: [커널, OS 커널, 운영체제 커널]
date modified: 2025-12-16 20:51:38 +09:00
date created: 2025-12-16 20:51:38 +09:00
---

## Kernel (커널) os kernel linux operating-systems

커널은 운영체제의 심장이다. 5살 아이에게 설명하자면 "컴퓨터의 교통경찰"이다. 여러 프로그램이 동시에 메모리를 쓰고, CPU를 나눠 쓰고, 파일을 읽고 쓸 때 충돌하지 않게 교통 정리를 해준다. 5년차 엔지니어에게는 "하드웨어 추상화 + 자원 중재 + 보안 경계"의 핵심 소프트웨어 계층이다.

### 커널이 왜 필요한가?

**5살 설명**: 만약 여러 친구가 한 장난감(하드웨어)을 동시에 쓰려고 하면 싸울 거야. 커널은 "너는 3분 쓰고, 너는 그 다음 3분"이라고 정해주는 선생님이야.

**엔지니어 설명**: 
- **자원 격리**: 프로세스 A가 프로세스 B의 메모리를 함부로 읽거나 쓰면 안 된다. 커널이 MMU(Memory Management Unit)를 설정해 가상 주소 공간을 분리한다.
- **공정한 스케줄링**: CPU는 하나인데 100개 프로세스가 돌면? 커널 스케줄러가 시간을 나눠준다. CFS(Completely Fair Scheduler)는 각 태스크의 실행 시간을 추적해 공정하게 배분한다.
- **하드웨어 추상화**: 디스크가 SSD든 HDD든, 앱은 read/write syscall만 쓰면 된다. 커널이 하드웨어 차이를 흡수한다.

---

### 커널의 핵심 구조

#### 1. 모놀리식(Monolithic) vs 마이크로(Micro) 커널

**5살 설명**: 
- **모놀리식**: 모든 일을 한 건물(커널 공간)에서 처리해. 빠르지만 한 곳이 무너지면 전부 무너질 수 있어.
- **마이크로**: 꼭 필요한 일만 작은 사무실(커널)에서 하고, 나머지는 밖에 있는 회사들(유저 공간 서버)이 해. 안전하지만 왔다갔다 하는게 좀 느려.

**엔지니어 설명**:
- **모놀리식(Linux, Android)**: 파일시스템, 네트워크 스택, 디바이스 드라이버가 모두 커널 공간에서 실행. 컨텍스트 스위칭이 적어 성능이 좋지만, 버그 하나가 커널 패닉을 유발할 수 있다.
- **마이크로커널(L4, Minix)**: 커널은 IPC, 스케줄링, 메모리 관리만 담당. 파일시스템/드라이버는 유저 공간 프로세스로 분리. 격리성이 좋지만 메시지 패싱 오버헤드가 있다.
- **하이브리드**: macOS(XNU)는 Mach 마이크로커널 + BSD 레이어를 합친 형태.

#### 2. 커널 모드 vs 유저 모드

**5살 설명**: 
- **커널 모드**: 선생님처럼 모든 걸 할 수 있는 특별한 권한이 있어.
- **유저 모드**: 학생처럼 정해진 것만 할 수 있고, 위험한 건 선생님께 부탁해야 해.

**엔지니어 설명**:
- **Ring 0(커널 모드)**: CPU의 모든 명령을 실행 가능. 메모리 전체 접근, I/O 포트 직접 제어.
- **Ring 3(유저 모드)**: 제한된 명령만 실행. 특권 명령(privileged instruction) 실행 시 General Protection Fault 발생.
- **시스템 콜로 전환**: 유저 프로그램이 `syscall` 명령(x86-64) 또는 `svc`(ARM)를 호출하면 CPU가 커널 모드로 전환. 커널은 트랩 핸들러로 진입해 요청된 작업을 처리하고 결과를 반환.

```
User space: write(fd, buf, count)
              ↓ syscall instruction
Kernel space: sys_write()
              ↓ VFS layer
              ↓ ext4 filesystem
              ↓ Block layer
              ↓ Device driver
              ↓ Hardware
```

---

### 커널의 주요 서브시스템

#### 1. 프로세스 관리

**5살 설명**: 커널은 프로그램들이 차례대로 일하게 해줘. A 프로그램이 잠깐 일하다가, B 프로그램에게 차례를 넘기고, 다시 A가 하고...

**엔지니어 설명**:
- **프로세스 디스크립터**: Linux는 `task_struct`로 프로세스 상태를 관리. PID, 메모리 맵, 파일 디스크립터 테이블, 스케줄링 정보, 시그널 핸들러 등을 저장.
- **스케줄러 클래스**: Linux는 CFS(일반 프로세스), Real-time(SCHED_FIFO/RR), Deadline 스케줄러를 지원.
  - **CFS**: 가상 런타임(vruntime)을 추적. Red-black tree로 다음 실행할 태스크를 O(log n)에 선택.
  - **RT**: 우선순위 기반 선점형. 높은 우선순위 태스크가 낮은 것을 즉시 선점.
- **컨텍스트 스위칭**: 레지스터 저장/복원, 페이지 테이블 교체(TLB flush), 캐시 오염 등의 비용. 너무 잦으면 성능 저하.

#### 2. 메모리 관리

**5살 설명**: 커널은 큰 종이(메모리)를 여러 친구에게 나눠줘. 친구들은 자기 칸만 쓸 수 있고, 남의 칸은 못 봐.

**엔지니어 설명**:
- **가상 메모리**: 각 프로세스는 독립된 가상 주소 공간을 가짐. MMU가 페이지 테이블을 통해 가상 → 물리 주소 변환.
- **페이징**: 메모리를 고정 크기 페이지(4KB)로 나눔. 페이지 폴트 시 커널이 디스크에서 로드하거나 swap.
- **Demand Paging**: 실제로 접근할 때 페이지를 할당. fork() 후 Copy-on-Write로 메모리 절약.
- **슬랩 할당자(SLAB/SLUB)**: 커널이 자주 쓰는 작은 객체(inode, task_struct)를 캐싱해 할당 속도 향상.
- **OOM Killer**: 메모리 부족 시 점수가 높은 프로세스를 종료. 점수는 메모리 사용량, nice 값, oom_score_adj 등으로 계산.

```
Virtual Address Space (per process)
┌──────────────────┐ 0xFFFFFFFF (kernel space start)
│ Kernel           │  
├──────────────────┤ 
│ Stack ↓          │  grows down
├──────────────────┤
│ ...              │
├──────────────────┤
│ Heap ↑           │  grows up (malloc)
├──────────────────┤
│ .bss (uninit)    │
│ .data (init)     │
│ .text (code)     │
└──────────────────┘ 0x00000000
```

#### 3. 파일 시스템

**5살 설명**: 커널은 파일을 정리해서 보여줘. 실제로는 디스크에 막 흩어져 있지만, 우린 예쁜 폴더로 볼 수 있어.

**엔지니어 설명**:
- **VFS(Virtual File System)**: 공통 인터페이스로 ext4, XFS, NFS, procfs 등을 추상화.
- **Inode**: 파일의 메타데이터(크기, 권한, 타임스탬프, 블록 포인터). 파일 이름은 디렉토리 엔트리에.
- **Page Cache**: 최근 읽은 파일 내용을 메모리에 캐싱. write-back으로 성능 향상하지만, fsync 없으면 데이터 손실 위험.
- **Journaling**: ext4, XFS는 메타데이터 변경을 저널에 먼저 기록. 크래시 후 복구 시간 단축.
- **File Descriptor**: 프로세스마다 fd 테이블. open()은 커널의 file 객체를 생성하고 fd를 반환. read/write는 이 fd로 작업.

#### 4. 디바이스 드라이버

**5살 설명**: 키보드, 마우스, 하드디스크... 이런 장치들과 이야기하려면 "통역사"가 필요해. 드라이버가 그 통역사야.

**엔지니어 설명**:
- **Character Device**: 스트림 방식(키보드, 시리얼). `read()`/`write()`로 접근.
- **Block Device**: 블록 단위(디스크). 버퍼링, 스케줄링(CFQ, deadline, noop) 지원.
- **Network Device**: 소켓 API로 추상화. 드라이버는 패킷을 송수신.
- **Module**: 커널 재컴파일 없이 동적으로 로드(`insmod`/`modprobe`). `MODULE_LICENSE`, `module_init/exit` 매크로 사용.
- **Interrupt Handling**: 하드웨어 인터럽트 발생 → CPU가 IRQ 핸들러 호출 → top half(빠른 처리) + bottom half(지연 처리, softirq/tasklet/workqueue).

#### 5. 네트워킹

**5살 설명**: 인터넷으로 다른 컴퓨터에 편지를 보내고 받아. 커널이 우체부 역할을 해줘.

**엔지니어 설명**:
- **프로토콜 스택**: 
  - **L2**: Ethernet 프레임 처리. ARP로 IP→MAC 변환.
  - **L3**: IP 라우팅. 라우팅 테이블 조회, TTL 감소, 체크섬 검증.
  - **L4**: TCP(연결 지향, 신뢰성) / UDP(비연결, 빠름). 포트 번호로 소켓 구분.
- **Socket Buffer(skb)**: 네트워크 패킷을 담는 커널 자료구조. 레이어 간 전달 시 헤더만 추가/제거해 zero-copy 최적화.
- **Netfilter/iptables**: 패킷 필터링, NAT, 방화벽. 훅 포인트(PREROUTING, FORWARD, POSTROUTING 등)에서 규칙 적용.
- **eBPF**: 커널 재컴파일 없이 네트워크 경로에 프로그램 삽입. XDP(eXpress Data Path)로 패킷을 드라이버 레벨에서 처리해 초고속 필터링.

---

### 시스템 콜(System Call)

**5살 설명**: 프로그램이 커널에게 "이거 좀 해줘!"라고 부탁하는 전화번호야. read(), write(), open() 같은 게 그 번호들이야.

**엔지니어 설명**:
- **Mechanism**: 유저 모드에서 `syscall` 명령 실행 → CPU가 특권 모드로 전환 → 커널의 시스템 콜 테이블(번호→함수 매핑) 참조 → 핸들러 실행 → 결과 반환 후 유저 모드 복귀.
- **매개변수 전달**: 레지스터(rdi, rsi, rdx, r10, r8, r9 on x86-64). 6개 이상이면 스택 사용.
- **오버헤드**: 컨텍스트 스위칭, TLB flush, 캐시 오염. vDSO(virtual Dynamic Shared Object)로 일부 콜(gettimeofday)을 유저 공간에서 처리해 최적화.
- **Examples**:
  - `fork()`: 새 프로세스 생성. task_struct 복사, CoW 페이지 테이블 설정.
  - `execve()`: 현재 프로세스를 새 프로그램으로 교체. ELF 파일 로드, 스택/힙 초기화.
  - `mmap()`: 파일을 메모리에 매핑하거나 익명 메모리 할당.

---

### 동기화와 락(Locking)

**5살 설명**: 두 친구가 동시에 같은 장난감을 바꾸려 하면 엉망이 돼. 그래서 "내가 쓸 때는 기다려줘"라는 규칙이 필요해.

**엔지니어 설명**:
- **Race Condition**: 여러 CPU 코어가 동시에 공유 데이터를 수정하면 불일치 발생.
- **Spinlock**: Busy-wait 방식. 짧은 임계 구역에 적합. 멀티코어에서 다른 CPU가 락을 잡으면 계속 polling.
- **Mutex**: Sleep 방식. 락을 못 얻으면 대기 큐에 들어가 스케줄 아웃. 긴 임계 구역에 적합.
- **Semaphore**: 카운팅 세마포어로 여러 스레드가 제한된 수만큼 접근 허용.
- **RCU(Read-Copy-Update)**: 읽기가 많은 경우 최적화. 읽기는 락 없이 진행, 쓰기는 복사본을 만들어 업데이트 후 포인터 교체.
- **Lock-Free**: Atomic 연산(CAS, compare-and-swap)으로 락 없이 동기화. 복잡하지만 고성능.

---

### 인터럽트와 예외(Exception)

**5살 설명**: 
- **인터럽트**: 하드웨어가 "급한 일 있어요!"라고 커널을 부르는 거야. 키보드 누르면 "키 눌렀어요!" 알려줘.
- **예외**: 프로그램이 잘못된 걸 하면(0으로 나누기) 커널이 "이건 안 돼!"라고 말해줘.

**엔지니어 설명**:
- **Hardware Interrupt**: 외부 장치(타이머, 디스크, 네트워크 카드)가 CPU에 신호. IRQ 번호로 구분. 인터럽트 컨트롤러(APIC)가 우선순위 관리.
- **Software Interrupt**: `int 0x80`(옛날 Linux 시스템 콜), 혹은 `syscall`/`sysenter`.
- **Exception**: CPU가 감지한 비정상 상황.
  - **Fault**: 복구 가능(페이지 폴트). 커널이 페이지 로드 후 명령 재실행.
  - **Trap**: 의도적(디버거 브레이크포인트). 다음 명령으로 진행.
  - **Abort**: 치명적(이중 폴트). 복구 불가능, 패닉.
- **Deferred Work**: 인터럽트 핸들러는 최소 작업만(top half), 나머지는 softirq/tasklet/workqueue로 연기(bottom half).

---

### 커널 보안

**5살 설명**: 나쁜 프로그램이 남의 비밀을 훔치거나 컴퓨터를 망가뜨리지 못하게 커널이 지켜줘.

**엔지니어 설명**:
- **권한 분리**: root(UID 0)는 모든 권한. 일반 유저는 자기 파일만 접근. Capabilities로 권한을 세분화(CAP_NET_ADMIN, CAP_SYS_ADMIN 등).
- **ASLR(Address Space Layout Randomization)**: 스택/힙/라이브러리 주소를 랜덤화해 버퍼 오버플로우 공격 어렵게.
- **DEP/NX(Data Execution Prevention)**: 데이터 영역을 실행 불가능하게 표시. 쉘코드 삽입 공격 방어.
- **KASLR(Kernel ASLR)**: 커널 코드 자체의 주소를 랜덤화.
- **Seccomp**: 프로세스가 사용할 시스템 콜을 제한. 샌드박스(Chrome, Docker)에서 활용.
- **SELinux/AppArmor**: Mandatory Access Control. "누가 어떤 객체에 무엇을 할 수 있는가"를 정책으로 정의.

---

### 커널 디버깅과 트레이싱

**5살 설명**: 커널이 이상하게 동작하면, 어디가 문제인지 찾아야 해. 마치 탐정처럼 단서를 모으는 거야.

**엔지니어 설명**:
- **printk**: 커널의 printf. 로그 레벨(KERN_ERR, KERN_INFO)로 중요도 분류. dmesg로 확인.
- **ftrace**: 함수 호출 추적. function tracer, function_graph로 콜 스택 시각화.
- **perf**: CPU 성능 카운터, 샘플링. 핫스팟 찾기, 캐시 미스 분석.
- **eBPF**: 프로브를 커널 함수에 삽입. bpftrace로 실시간 히스토그램, 지연 분석.
- **KGDB**: 커널 디버거. 브레이크포인트, 단계 실행, 변수 검사. 시리얼/USB로 연결.
- **Crash Dump**: 패닉 시 vmcore 덤프. crash 유틸리티로 사후 분석.

---

### 실전: 커널 컴파일과 모듈 개발

**5살 설명**: 커널을 직접 만들어 볼 수도 있어. 레고처럼 부품(모듈)을 끼워 넣거나 빼는 것도 가능해!

**엔지니어 설명**:

#### 커널 컴파일
```bash
# 소스 다운로드
wget https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.x.tar.xz
tar xf linux-6.x.tar.xz && cd linux-6.x

# 설정 (기존 config 복사 or make menuconfig)
cp /boot/config-$(uname -r) .config
make oldconfig  # 새 옵션 질문

# 빌드 (-j는 코어 수)
make -j$(nproc)

# 설치
sudo make modules_install
sudo make install
sudo update-grub  # 부트로더 업데이트
```

#### 간단한 커널 모듈
```c
// hello.c
#include <linux/module.h>
#include <linux/kernel.h>

static int __init hello_init(void) {
    printk(KERN_INFO "Hello, Kernel!\n");
    return 0;
}

static void __exit hello_exit(void) {
    printk(KERN_INFO "Goodbye, Kernel!\n");
}

module_init(hello_init);
module_exit(hello_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Your Name");
MODULE_DESCRIPTION("A simple Hello World module");
```

```makefile
# Makefile
obj-m += hello.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```

```bash
make
sudo insmod hello.ko
dmesg | tail  # "Hello, Kernel!" 확인
sudo rmmod hello
dmesg | tail  # "Goodbye, Kernel!" 확인
```

---

### 성능 최적화 팁

**5살 설명**: 커널을 빠르게 만들려면 쓸데없는 일을 줄이고, 자주 쓰는 걸 미리 준비해둬야 해.

**엔지니어 설명**:
1. **Tickless Kernel**: 타이머 인터럽트를 필요할 때만 발생시켜 전력 절약. `CONFIG_NO_HZ_FULL`.
2. **Huge Pages**: 4KB 대신 2MB/1GB 페이지 사용. TLB 미스 감소. `hugetlbfs` 마운트.
3. **CPU 친화성(Affinity)**: 특정 프로세스를 특정 코어에 고정. `taskset` 명령. 캐시 지역성 향상.
4. **I/O 스케줄러 선택**: 
   - **mq-deadline**: 일반적 워크로드.
   - **kyber**: SSD 최적화.
   - **none**: NVMe에서 오버헤드 최소화.
5. **Zero-Copy**: `sendfile()`, `splice()` 시스템 콜로 유저 공간 복사 생략.
6. **NUMA 인식**: `numactl`로 메모리를 가까운 노드에 할당. 원격 메모리 접근 비용 감소.

---

### 주요 커널 버전별 변화

**5살 설명**: 커널도 계속 발전해. 옛날엔 없던 편리한 기능들이 계속 추가돼.

**엔지니어 설명**:
- **Linux 2.6 (2003)**: O(1) 스케줄러, NPTL(스레드), 향상된 SMP 지원.
- **Linux 3.0 (2011)**: 버전 번호 리셋. 큰 변화보다는 점진적 개선.
- **Linux 4.0 (2015)**: Live kernel patching(kpatch, kGraft).
- **Linux 5.0 (2019)**: Energy-aware scheduling, CAKE qdisc.
- **Linux 6.0 (2022)**: Rust 지원 시작, io_uring 개선.

---

### 자주 묻는 질문

**Q: 커널과 운영체제의 차이는?**  
A: 운영체제는 커널 + 시스템 라이브러리 + 유틸리티의 총합. 커널은 그 중 하드웨어와 직접 소통하는 핵심 부분.

**Q: 커널 패닉이 뭔가요?**  
A: 커널이 복구 불가능한 오류를 만났을 때. 모든 걸 멈추고 화면에 에러 메시지 출력. Windows의 블루스크린과 비슷.

**Q: 왜 커널 개발이 어렵나요?**  
A: 디버깅이 힘들고(gdb가 안 됨), 버그 하나가 시스템 전체를 다운시키고, 하드웨어 의존적이고, 동시성 문제가 복잡해서.

**Q: 일반 개발자도 커널을 만질 일이 있나요?**  
A: 드물지만 있다. 임베디드 개발, 성능 튜닝, 디바이스 드라이버 개발, 컨테이너/가상화 작업 시 커널 이해가 필수.

---

### 더 공부하려면

**책**:
- *Linux Kernel Development* (Robert Love): 입문자 친화적.
- *Understanding the Linux Kernel* (Bovet, Cesati): 심화.
- *Linux Device Drivers* (Corbet et al.): 드라이버 개발.

**온라인**:
- [kernel.org](https://www.kernel.org/): 공식 소스.
- [LWN.net](https://lwn.net/): 커널 변경 사항 뉴스.
- [Linux Kernel Labs](https://linux-kernel-labs.github.io/): 실습 코스.

**커뮤니티**:
- LKML(Linux Kernel Mailing List): 패치 리뷰 과정 관찰.
- [Stack Overflow [linux-kernel]](https://stackoverflow.com/questions/tagged/linux-kernel)

---

### 마무리

커널은 복잡하지만, 계층별로 나눠 보면 논리가 명확하다. **"하드웨어를 추상화하고, 자원을 공정하게 나누고, 안전하게 격리한다"**는 세 원칙만 기억하면 된다. 5년차 엔지니어라면 시스템 콜 흐름, 메모리 관리, 스케줄링 알고리즘을 손으로 그려볼 수 있어야 하고, 5살 아이에게는 "커널은 컴퓨터의 교통경찰"이라고 비유하면 충분하다.

커널을 이해하면 성능 병목을 찾고, 디버깅 시간을 줄이고, 시스템 설계 시 올바른 트레이드오프를 선택할 수 있다. 안드로이드든 서버든, 결국 모든 소프트웨어는 커널 위에서 돌아간다.

---

### 연결 문서

[[android-kernel]] - 안드로이드 특화 커널 수정 사항  
[[android-hal-and-kernel]] - 안드로이드 HAL과 커널 관계  
[[android-architecture-stack]] - 안드로이드 전체 스택에서 커널의 위치
