# vi/vim 에디터 및 추가 필수 개념

## 1. vi/vim 에디터

### 1.1 vi 개요

**특징**:
- 리눅스 표준 텍스트 에디터
- 모든 리눅스 시스템에 기본 설치
- 모드 기반 에디터
- 시험 필수 출제 항목

### 1.2 vi 모드

**세 가지 모드**:
1. **명령 모드 (Command Mode)**: 기본 모드, 커서 이동 및 편집
2. **입력 모드 (Insert Mode)**: 텍스트 입력
3. **라인 모드 (Line Mode)**: 명령 실행 (`:` 시작)

**모드 전환**:
```
명령 모드 → 입력 모드: i, a, o, I, A, O
입력 모드 → 명령 모드: ESC
명령 모드 → 라인 모드: :, /, ?
```

### 1.3 기본 명령어

**파일 열기/저장/종료**:
```bash
vi filename             # 파일 열기
:w                      # 저장
:w filename             # 다른 이름으로 저장
:q                      # 종료
:q!                     # 강제 종료 (저장 안 함)
:wq                     # 저장 후 종료
:x                      # 변경사항 있으면 저장 후 종료
ZZ                      # :wq와 동일 (명령 모드)
```

**입력 모드 진입**:
```
i       # 커서 위치에 삽입
a       # 커서 다음에 삽입
o       # 아래 줄에 삽입
I       # 줄 맨 앞에 삽입
A       # 줄 맨 뒤에 삽입
O       # 위 줄에 삽입
```

**커서 이동**:
```
h       # 왼쪽
j       # 아래
k       # 위
l       # 오른쪽

0       # 줄 맨 앞
$       # 줄 맨 뒤
^       # 줄의 첫 문자
w       # 다음 단어
b       # 이전 단어
e       # 단어 끝

gg      # 파일 맨 앞
G       # 파일 맨 뒤
:n      # n번째 줄로 (예: :10)
nG      # n번째 줄로 (예: 10G)

Ctrl+f  # 한 페이지 아래
Ctrl+b  # 한 페이지 위
Ctrl+d  # 반 페이지 아래
Ctrl+u  # 반 페이지 위
```

**삭제**:
```
x       # 한 문자 삭제
dw      # 한 단어 삭제
dd      # 한 줄 삭제
ndd     # n줄 삭제 (예: 3dd)
d$      # 커서부터 줄 끝까지
d0      # 커서부터 줄 시작까지
dG      # 커서부터 파일 끝까지
dgg     # 커서부터 파일 시작까지
```

**복사 및 붙여넣기**:
```
yy      # 한 줄 복사
nyy     # n줄 복사 (예: 3yy)
yw      # 한 단어 복사
p       # 커서 아래/뒤에 붙여넣기
P       # 커서 위/앞에 붙여넣기
```

**실행 취소 및 재실행**:
```
u       # 실행 취소 (undo)
Ctrl+r  # 재실행 (redo)
.       # 마지막 명령 반복
```

**검색 및 치환**:
```
/pattern        # 아래 방향 검색
?pattern        # 위 방향 검색
n               # 다음 검색 결과
N               # 이전 검색 결과

:s/old/new/     # 현재 줄에서 첫 번째 매칭 치환
:s/old/new/g    # 현재 줄에서 모든 매칭 치환
:%s/old/new/g   # 전체 파일에서 모든 매칭 치환
:%s/old/new/gc  # 확인하며 치환
:10,20s/old/new/g  # 10~20줄에서 치환
```

**기타 유용한 명령**:
```
r       # 한 문자 교체
R       # 덮어쓰기 모드
J       # 다음 줄과 합치기
~       # 대소문자 변환
>>      # 들여쓰기
<<      # 내어쓰기
:set nu         # 줄 번호 표시
:set nonu       # 줄 번호 숨김
:set ai         # 자동 들여쓰기
:syntax on      # 문법 강조
```

### 1.4 vim 추가 기능

**비주얼 모드**:
```
v       # 문자 단위 선택
V       # 줄 단위 선택
Ctrl+v  # 블록 선택
```

**다중 파일**:
```
:e filename     # 다른 파일 열기
:bn             # 다음 버퍼
:bp             # 이전 버퍼
:split          # 수평 분할
:vsplit         # 수직 분할
Ctrl+w w        # 창 전환
```

## 2. 디스크 쿼터 (Quota)

### 2.1 쿼터 개요

**목적**:
- 사용자/그룹별 디스크 사용량 제한
- 시스템 리소스 관리
- 공정한 디스크 공간 배분

**쿼터 유형**:
- **사용자 쿼터**: 개별 사용자 제한
- **그룹 쿼터**: 그룹 단위 제한

**제한 방식**:
- **블록 쿼터**: 디스크 공간 (KB 단위)
- **inode 쿼터**: 파일 개수

**제한 레벨**:
- **Soft Limit**: 경고 한계 (유예 기간 있음)
- **Hard Limit**: 절대 한계 (초과 불가)

### 2.2 쿼터 설정

**1. 파일시스템 마운트 옵션 추가**:

`/etc/fstab` 수정:
```
/dev/sda1  /home  ext4  defaults,usrquota,grpquota  1  2
```

**옵션**:
- `usrquota`: 사용자 쿼터 활성화
- `grpquota`: 그룹 쿼터 활성화

**재마운트**:
```bash
mount -o remount /home
```

**2. 쿼터 데이터베이스 생성**:
```bash
quotacheck -cug /home       # 쿼터 파일 생성
quotacheck -avug            # 모든 파일시스템
```

**옵션**:
- `-c`: 새로 생성
- `-u`: 사용자 쿼터
- `-g`: 그룹 쿼터
- `-a`: 모든 파일시스템
- `-v`: 상세 출력
- `-m`: 언마운트하지 않고 실행

**생성되는 파일**:
- `aquota.user`: 사용자 쿼터 DB
- `aquota.group`: 그룹 쿼터 DB

**3. 쿼터 활성화**:
```bash
quotaon /home               # /home 쿼터 활성화
quotaon -a                  # 모든 파일시스템
quotaon -avug               # 모든 쿼터 활성화
quotaoff /home              # 쿼터 비활성화
```

### 2.3 쿼터 설정 및 관리

**edquota** - 쿼터 편집:
```bash
edquota -u username         # 사용자 쿼터 설정
edquota -g groupname        # 그룹 쿼터 설정
edquota -t                  # 유예 기간 설정
edquota -p user1 user2      # user1 설정을 user2에 복사
```

**쿼터 편집 화면**:
```
Disk quotas for user john (uid 1000):
Filesystem  blocks  soft    hard    inodes  soft  hard
/dev/sda1   10000   50000   60000   100     500   600
```

**필드**:
- **blocks**: 현재 사용 중인 블록 (KB)
- **soft**: 소프트 제한 (KB)
- **hard**: 하드 제한 (KB)
- **inodes**: 현재 파일 개수
- **soft/hard**: inode 제한

**setquota** - 명령줄에서 설정:
```bash
setquota -u username 50000 60000 500 600 /home
# 사용자 쿼터: 블록 soft 50MB, hard 60MB, inode soft 500, hard 600
```

### 2.4 쿼터 확인

**quota** - 개인 쿼터 확인:
```bash
quota                       # 자신의 쿼터
quota -u username           # 특정 사용자 (root)
quota -g groupname          # 그룹 쿼터
quota -v                    # 상세 정보
```

**repquota** - 전체 쿼터 리포트:
```bash
repquota /home              # /home 쿼터 리포트
repquota -a                 # 모든 파일시스템
repquota -aug               # 모든 사용자/그룹
repquota -s                 # 사람이 읽기 쉬운 형식
```

**출력 예**:
```
Block limits                File limits
User    used  soft  hard  grace  used  soft  hard  grace
john    10000 50000 60000        100   500   600
```

**warnquota** - 쿼터 초과 경고 메일:
```bash
warnquota                   # 초과 사용자에게 메일 발송
```

## 3. 커널 모듈 관리

### 3.1 커널 모듈 개요

**모듈이란**:
- 동적으로 로드/언로드 가능한 커널 코드
- 재부팅 없이 기능 추가/제거
- 주로 디바이스 드라이버

**모듈 위치**:
- `/lib/modules/$(uname -r)/`: 커널 모듈 디렉토리
- `/lib/modules/$(uname -r)/kernel/`: 커널 모듈
- `/lib/modules/$(uname -r)/kernel/drivers/`: 드라이버

### 3.2 모듈 확인

**lsmod** - 로드된 모듈 목록:
```bash
lsmod                       # 로드된 모듈
lsmod | grep module_name    # 특정 모듈 검색
```

**출력**:
```
Module                  Size  Used by
e1000                  100000  0
```

**modinfo** - 모듈 정보:
```bash
modinfo module_name         # 모듈 상세 정보
modinfo -p module_name      # 모듈 파라미터
modinfo -F filename module_name  # 파일 경로만
```

### 3.3 모듈 로드/언로드

**insmod** - 모듈 삽입 (저수준):
```bash
insmod /path/to/module.ko   # 전체 경로 필요
insmod module.ko param=value  # 파라미터 지정
```

**rmmod** - 모듈 제거:
```bash
rmmod module_name           # 모듈 제거
rmmod -f module_name        # 강제 제거
```

**modprobe** - 모듈 관리 (권장):
```bash
modprobe module_name        # 모듈 로드 (의존성 자동)
modprobe -r module_name     # 모듈 제거
modprobe -a mod1 mod2       # 여러 모듈 로드
modprobe -c                 # 설정 확인
modprobe -l                 # 사용 가능한 모듈 목록
```

**modprobe 장점**:
- 의존성 자동 해결
- 모듈 이름만으로 로드 가능
- 설정 파일 사용

### 3.4 모듈 설정

**모듈 파라미터 설정**: `/etc/modprobe.d/*.conf`

**예제**: `/etc/modprobe.d/sound.conf`
```
options snd-hda-intel model=auto
```

**모듈 블랙리스트**: `/etc/modprobe.d/blacklist.conf`
```
blacklist nouveau           # nouveau 모듈 로드 금지
```

**부팅 시 자동 로드**: `/etc/modules` 또는 `/etc/modules-load.d/*.conf`
```
# /etc/modules
e1000
nfs
```

### 3.5 depmod

**의존성 업데이트**:
```bash
depmod                      # 현재 커널 모듈 의존성 생성
depmod -a                   # 모든 모듈
depmod kernel_version       # 특정 커널 버전
```

**생성 파일**:
- `/lib/modules/$(uname -r)/modules.dep`: 의존성 정보

## 4. 링크 및 파일 찾기 추가

### 4.1 심볼릭 링크 추가 정보

**깨진 링크 찾기**:
```bash
find /path -type l -xtype l     # 깨진 심볼릭 링크
find /path -type l ! -exec test -e {} \; -print
```

**링크 대상 확인**:
```bash
readlink linkname               # 링크 대상
readlink -f linkname            # 절대 경로로 확인
```

### 4.2 파일 속성

**chattr** - 파일 속성 변경:
```bash
chattr +i file.txt              # 불변 (삭제/수정 불가)
chattr -i file.txt              # 불변 해제
chattr +a file.txt              # 추가만 가능
chattr +A file.txt              # atime 업데이트 안 함
```

**lsattr** - 파일 속성 확인:
```bash
lsattr file.txt                 # 속성 확인
lsattr -d dir/                  # 디렉토리 속성
```

**속성**:
- `i`: immutable (불변)
- `a`: append only (추가만)
- `A`: no atime update
- `c`: compressed
- `s`: secure deletion

## 5. 시험 대비 핵심 요약

### vi/vim
- **모드**: 명령(ESC), 입력(i,a,o), 라인(:)
- **저장/종료**: `:w`, `:q`, `:wq`, `:q!`
- **이동**: `h,j,k,l`, `gg`, `G`, `:n`
- **삭제**: `x`, `dd`, `dw`
- **복사**: `yy`, `p`
- **검색**: `/pattern`, `n`
- **치환**: `:%s/old/new/g`

### 디스크 쿼터
- **설정**: `/etc/fstab`에 `usrquota,grpquota`
- **생성**: `quotacheck -cug`
- **활성화**: `quotaon -avug`
- **편집**: `edquota -u username`
- **확인**: `quota`, `repquota -a`
- **제한**: soft (경고), hard (절대)

### 커널 모듈
- **목록**: `lsmod`
- **정보**: `modinfo module_name`
- **로드**: `modprobe module_name`
- **제거**: `modprobe -r module_name`
- **의존성**: `depmod -a`
- **설정**: `/etc/modprobe.d/`
- **블랙리스트**: `/etc/modprobe.d/blacklist.conf`

### 파일 속성
- **설정**: `chattr +i file` (불변)
- **확인**: `lsattr file`

---

**메인으로**: [리눅스마스터 1급 자격증 학습 가이드](../bash-scripting-summary/README.md)
