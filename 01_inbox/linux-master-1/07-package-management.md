---
title: 07-package-management
tags: []
aliases: []
date modified: 2025-12-29 10:33:01 +09:00
date created: 2025-12-10 19:31:27 +09:00
---

## 패키지 관리

### 1. 패키지 관리 개요

#### 1.1 패키지란?
- **정의**: 소프트웨어와 메타데이터를 포함한 아카이브
- **구성**: 바이너리, 라이브러리, 설정 파일, 문서, 의존성 정보
- **형식**: RPM (Red Hat), DEB (Debian)

#### 1.2 패키지 관리자 종류

**저수준 도구**:
- **rpm**: RPM 패키지 관리
- **dpkg**: DEB 패키지 관리
- 의존성 자동 해결 안 함

**고수준 도구**:
- **yum/dnf**: RHEL/CentOS/Fedora
- **apt**: Debian/Ubuntu
- 의존성 자동 해결

### 2. RPM 패키지 관리

#### 2.1 RPM 기본

**패키지 명명 규칙**:
```
package-version-release.architecture.rpm
httpd-2.4.6-97.el7.x86_64.rpm
│     │     │   │    └─ 아키텍처
│     │     │   └─ 배포판 버전
│     │     └─ 릴리스 번호
│     └─ 버전
└─ 패키지 이름
```

**아키텍처**:
- `x86_64`: 64 비트
- `i386`, `i686`: 32 비트
- `noarch`: 아키텍처 독립적
- `src`: 소스 RPM

#### 2.2 rpm 명령어

**설치**:
```bash
rpm -ivh package.rpm            # 설치 (install, verbose, hash)
rpm -Uvh package.rpm            # 업그레이드 (없으면 설치)
rpm -Fvh package.rpm            # 업데이트 (있을 때만)
rpm -ivh --nodeps package.rpm   # 의존성 무시 (비권장)
rpm -ivh --force package.rpm    # 강제 설치
```

**제거**:
```bash
rpm -e package                  # 제거 (erase)
rpm -e --nodeps package         # 의존성 무시 제거
```

**쿼리**:
```bash
rpm -qa                         # 모든 설치된 패키지
rpm -qa | grep httpd            # httpd 검색
rpm -qi package                 # 패키지 정보
rpm -ql package                 # 파일 목록
rpm -qc package                 # 설정 파일 목록
rpm -qd package                 # 문서 파일 목록
rpm -qf /path/to/file           # 파일이 속한 패키지
rpm -qp package.rpm             # 미설치 패키지 정보
rpm -qpi package.rpm            # 미설치 패키지 상세 정보
rpm -qpl package.rpm            # 미설치 패키지 파일 목록
rpm -q --scripts package        # 스크립트 확인
rpm -q --changelog package      # 변경 로그
```

**검증**:
```bash
rpm -V package                  # 패키지 검증
rpm -Va                         # 모든 패키지 검증
```

**검증 출력**:
```
S.5....T.  c /etc/httpd/conf/httpd.conf
│││││││││  │ └─ 파일 경로
│││││││││  └─ 파일 타입 (c=설정)
│││││││└─ 시간 (T)
││││││└─ 모드 (M)
│││││└─ 그룹 (G)
││││└─ 사용자 (U)
│││└─ 디바이스 (D)
││└─ 링크 (L)
│└─ MD5 체크섬 (5)
└─ 크기 (S)
```

**데이터베이스**:
```bash
rpm --rebuilddb                 # RPM DB 재구축
rpm --initdb                    # RPM DB 초기화
```

### 3. YUM (Yellowdog Updater Modified)

#### 3.1 YUM 기본

**특징**:
- 자동 의존성 해결
- 네트워크 저장소 사용
- 트랜잭션 기반
- RHEL 7 이하 기본

#### 3.2 yum 명령어

**패키지 관리**:
```bash
yum install package             # 설치
yum install -y package          # 확인 없이 설치
yum update package              # 업데이트
yum update                      # 모든 패키지 업데이트
yum remove package              # 제거
yum reinstall package           # 재설치
yum downgrade package           # 다운그레이드
yum localinstall package.rpm    # 로컬 RPM 설치
```

**정보 확인**:
```bash
yum list                        # 모든 패키지 목록
yum list installed              # 설치된 패키지
yum list available              # 설치 가능한 패키지
yum list updates                # 업데이트 가능한 패키지
yum info package                # 패키지 정보
yum search keyword              # 키워드 검색
yum provides /path/to/file      # 파일을 제공하는 패키지
yum deplist package             # 의존성 목록
```

**그룹 관리**:
```bash
yum grouplist                   # 그룹 목록
yum groupinfo "Group Name"      # 그룹 정보
yum groupinstall "Group Name"   # 그룹 설치
yum groupremove "Group Name"    # 그룹 제거
```

**히스토리**:
```bash
yum history                     # 트랜잭션 히스토리
yum history info <ID>           # 트랜잭션 상세
yum history undo <ID>           # 트랜잭션 취소
yum history redo <ID>           # 트랜잭션 재실행
```

**캐시 및 정리**:
```bash
yum makecache                   # 캐시 생성
yum clean packages              # 패키지 캐시 삭제
yum clean metadata              # 메타데이터 캐시 삭제
yum clean all                   # 모든 캐시 삭제
```

#### 3.3 저장소 관리

**저장소 파일**: `/etc/yum.repos.d/*.repo`

**저장소 설정 예**:
```ini
[base]
name=CentOS-$releasever - Base
baseurl=http://mirror.centos.org/centos/$releasever/os/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
enabled=1
```

**필드**:
- `[repo_id]`: 저장소 ID
- `name`: 저장소 이름
- `baseurl`: 저장소 URL
- `mirrorlist`: 미러 목록 URL
- `gpgcheck`: GPG 서명 확인 (0 또는 1)
- `gpgkey`: GPG 키 경로
- `enabled`: 활성화 여부 (0 또는 1)

**저장소 명령**:
```bash
yum repolist                    # 활성화된 저장소
yum repolist all                # 모든 저장소
yum repolist enabled            # 활성화된 저장소
yum repolist disabled           # 비활성화된 저장소
yum-config-manager --add-repo URL  # 저장소 추가
yum-config-manager --enable repo   # 저장소 활성화
yum-config-manager --disable repo  # 저장소 비활성화
```

### 4. DNF (Dandified YUM)

#### 4.1 DNF 개요

**특징**:
- YUM 의 차세대 버전
- 더 빠른 성능
- 향상된 의존성 해결
- RHEL 8+, Fedora 기본

#### 4.2 dnf 명령어

**기본 사용** (yum 과 유사):
```bash
dnf install package             # 설치
dnf update                      # 업데이트
dnf remove package              # 제거
dnf search keyword              # 검색
dnf info package                # 정보
dnf list installed              # 설치된 패키지
```

**DNF 전용 기능**:
```bash
dnf autoremove                  # 불필요한 의존성 제거
dnf check                       # 문제 확인
dnf distro-sync                 # 배포판 동기화
dnf module list                 # 모듈 목록
dnf module install module:stream  # 모듈 설치
```

### 5. APT (Advanced Package Tool)

#### 5.1 APT 개요

**특징**:
- Debian/Ubuntu 패키지 관리자
- DEB 패키지 형식
- 자동 의존성 해결

#### 5.2 apt 명령어

**패키지 관리**:
```bash
apt update                      # 패키지 목록 업데이트
apt upgrade                     # 업그레이드
apt full-upgrade                # 전체 업그레이드 (패키지 제거 포함)
apt install package             # 설치
apt install -y package          # 확인 없이 설치
apt remove package              # 제거 (설정 파일 유지)
apt purge package               # 완전 제거 (설정 파일 포함)
apt autoremove                  # 불필요한 패키지 제거
apt autoclean                   # 오래된 패키지 파일 삭제
```

**정보 확인**:
```bash
apt list                        # 모든 패키지
apt list --installed            # 설치된 패키지
apt list --upgradable           # 업그레이드 가능
apt search keyword              # 검색
apt show package                # 패키지 정보
apt depends package             # 의존성
apt rdepends package            # 역의존성
```

**캐시**:
```bash
apt-cache search keyword        # 검색
apt-cache show package          # 정보
apt-cache depends package       # 의존성
apt-cache policy package        # 정책 및 버전
```

#### 5.3 dpkg 명령어

**패키지 관리**:
```bash
dpkg -i package.deb             # 설치
dpkg -r package                 # 제거
dpkg -P package                 # 완전 제거
dpkg -l                         # 설치된 패키지 목록
dpkg -l | grep package          # 패키지 검색
dpkg -L package                 # 파일 목록
dpkg -S /path/to/file           # 파일이 속한 패키지
dpkg -s package                 # 패키지 상태
dpkg -c package.deb             # DEB 파일 내용
dpkg --configure -a             # 설정되지 않은 패키지 설정
```

#### 5.4 저장소 관리

**저장소 파일**: `/etc/apt/sources.list`, `/etc/apt/sources.list.d/*.list`

**저장소 형식**:
```
deb http://archive.ubuntu.com/ubuntu/ focal main restricted
deb-src http://archive.ubuntu.com/ubuntu/ focal main restricted
│   │                                     │     └─ 컴포넌트
│   │                                     └─ 배포판
│   └─ URL
└─ 타입 (deb 또는 deb-src)
```

**컴포넌트**:
- `main`: 공식 지원
- `restricted`: 제한적 라이선스
- `universe`: 커뮤니티 지원
- `multiverse`: 제한적 라이선스, 커뮤니티

**저장소 관리**:
```bash
add-apt-repository ppa:user/repo  # PPA 추가
add-apt-repository --remove ppa:user/repo  # PPA 제거
apt-add-repository "deb URL"      # 저장소 추가
apt update                        # 저장소 목록 업데이트
```

### 6. 소스 컴파일

#### 6.1 컴파일 과정

**일반적인 절차**:
```bash
# 1. 소스 다운로드 및 압축 해제
wget https://example.com/source.tar.gz
tar -xzvf source.tar.gz
cd source/

# 2. 설정
./configure                     # 기본 설정
./configure --prefix=/usr/local # 설치 경로 지정
./configure --help              # 옵션 확인

# 3. 컴파일
make                            # 컴파일
make -j4                        # 4개 코어 사용

# 4. 설치
sudo make install               # 설치
sudo make uninstall             # 제거 (지원하는 경우)
```

**필수 도구**:
```bash
# Debian/Ubuntu
apt install build-essential

# RHEL/CentOS
yum groupinstall "Development Tools"
```

#### 6.2 checkinstall

**패키지로 설치**:
```bash
# 컴파일 후
sudo checkinstall               # DEB/RPM 생성 및 설치
```

**장점**:
- 패키지 관리자로 제거 가능
- 의존성 추적
- 업그레이드 용이

### 7. 시험 대비 핵심 요약

#### RPM 명령어

- **설치**: `rpm -ivh package.rpm`
- **제거**: `rpm -e package`
- **쿼리**: `rpm -qa`, `rpm -qi`, `rpm -ql`
- **파일 검색**: `rpm -qf /path/to/file`

#### YUM/DNF

- **설치**: `yum install package`
- **업데이트**: `yum update`
- **제거**: `yum remove package`
- **검색**: `yum search keyword`
- **정보**: `yum info package`
- **저장소**: `/etc/yum.repos.d/`

#### APT

- **업데이트**: `apt update`
- **업그레이드**: `apt upgrade`
- **설치**: `apt install package`
- **제거**: `apt remove package`
- **완전 제거**: `apt purge package`
- **저장소**: `/etc/apt/sources.list`

#### DPKG

- **설치**: `dpkg -i package.deb`
- **제거**: `dpkg -r package`
- **목록**: `dpkg -l`
- **파일 목록**: `dpkg -L package`

#### 패키지 형식

- **RPM**: Red Hat, CentOS, Fedora
- **DEB**: Debian, Ubuntu

---

**이전 챕터**: [프로세스 및 작업 관리](06-process-management.md)
**다음 챕터**: [네트워크 설정](08-network-config.md)
