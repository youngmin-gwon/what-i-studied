# Init & Service Lifecycle #android #android/init #android/boot

부팅 후 가장 먼저 달리는 프로그램이 init다. 서비스가 언제 켜지고 꺼지는지 아주 쉽게 적었다. 용어는 [[android-glossary]].

## init이 하는 일
- 커널이 넘겨준 장치 트리를 보고, 필요한 파일 시스템을 마운트한다.
- [[android-glossary#selinux|SELinux]] 규칙을 읽어 강제한다.
- rc 스크립트를 읽어 서비스와 트리거(조건)를 정의한다.

## rc 문법 간단 보기
- `on <trigger>`: 특정 순간에 실행할 명령 묶음. 예) `on boot`, `on property:sys.boot_completed=1`.
- `service <이름> <실행경로>`: 어떤 프로그램을 어떤 권한/클래스로 돌릴지 적는다.
- `import /apex/.../init/*.rc`: APEX 모듈이 자신의 서비스를 추가한다.

## 서비스 그룹과 타이밍
- class core: 가장 먼저 필요한 것들(property, ueventd, vold 등).
- class main: [[android-glossary#zygote|zygote]], surface, media 같은 핵심.
- class late_start: 부팅 후 조금 늦게 켜도 되는 것.

## property 시스템
- `setprop key value`로 값을 세팅하면 init이 저장/전파한다.
- `ro.*`는 읽기 전용, `persist.*`는 재부팅 후에도 남는다.
- `ctl.start/stop <서비스>` 특수 키로 서비스를 제어할 수 있다.

## 저장소·암호화
- fstab에 어떤 파티션을 어떻게 마운트할지 적는다.
- [[android-glossary#fbe|FBE]]를 쓰면 사용자 잠금에 따라 데이터가 열린다.
- adoptable/external 저장소는 vold가 이어서 처리한다.

## SELinux 통합
- first stage에서 정책을 올리고, enforcing 모드로 전환한다.
- property_contexts/file_contexts/서비스별 seclabel이 맞지 않으면 거부된다.

## ueventd
- 커널이 보내는 장치 이벤트를 듣고 `/dev` 노드의 권한과 라벨을 맞춘다.
- 카메라/모뎀 같은 디바이스 노드 권한이 틀리면 HAL이 실패한다.

## 데몬 운영 팁
- `oneshot`은 한 번만 돌고 끝난다. crash loop 시 `restart_period`로 재시도를 늦출 수 있다.
- 중요한 서비스는 `onrestart` 블록을 써서 복구 행동(예: 네트워크 리셋)을 건다.
- `writepid`로 cgroup/OOM 점수를 기록해 메모리 관리와 연결한다.

## 최적화 아이디어
- 부팅을 막는 서비스는 최대한 뒤로 미루거나 조건부로 켠다.
- bootchart/Perfetto로 어느 트리거가 오래 걸리는지 살핀다.

## 디버깅 포인트
- `init.svc.<name>` property로 서비스 상태를 본다.
- `dmesg`/`logcat`/`pstore`/`last_kmsg`로 초기 로그를 모은다.
- rc 파서 로그와 `avc: denied`를 함께 확인한다.

## Zygote 연계
- zygote(32/64)가 init.rc에 정의되어 있어야 앱을 만들 수 있다.
- [[android-glossary#system-server|system_server]]는 zygote가 띄운 뒤 Java 쪽에서 서비스들을 켠다.

## 체크리스트
- 부팅 루프? 무결성(AVB)/fstab/selinux 거부/서비스 크래시를 먼저 본다.
- property가 안 바뀐다? contexts/권한/SELinux를 확인한다.
- HAL이 안 뜬다? ueventd 권한과 binder 등록 상태를 본다.

## 링크
[[android-boot-flow]], [[android-hal-and-kernel]], [[android-architecture-stack]].
