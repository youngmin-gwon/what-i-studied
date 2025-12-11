# 네트워크 설정

## 1. 네트워크 기본 개념

### 1.1 TCP/IP 모델

**계층 구조**:
```
응용 계층 (Application)    - HTTP, FTP, SSH, DNS
전송 계층 (Transport)       - TCP, UDP
인터넷 계층 (Internet)      - IP, ICMP, ARP
네트워크 접근 계층 (Link)   - Ethernet, Wi-Fi
```

### 1.2 IP 주소

**IPv4**:
- **형식**: 32비트, 점으로 구분된 4개 옥텟
- **예**: 192.168.1.100
- **클래스**:
  - A: 1.0.0.0 ~ 126.255.255.255 (/8)
  - B: 128.0.0.0 ~ 191.255.255.255 (/16)
  - C: 192.0.0.0 ~ 223.255.255.255 (/24)

**사설 IP**:
- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16

**특수 IP**:
- 127.0.0.1: 루프백 (localhost)
- 0.0.0.0: 모든 인터페이스
- 255.255.255.255: 브로드캐스트

**서브넷 마스크**:
```
/24 = 255.255.255.0     (256개 주소)
/16 = 255.255.0.0       (65,536개 주소)
/8  = 255.0.0.0         (16,777,216개 주소)
```

**IPv6**:
- **형식**: 128비트, 콜론으로 구분된 8개 그룹
- **예**: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
- **축약**: 2001:db8:85a3::8a2e:370:7334

## 2. 네트워크 인터페이스

### 2.1 인터페이스 확인

**ip 명령어** (권장):
```bash
ip addr                         # 모든 인터페이스
ip addr show eth0               # 특정 인터페이스
ip link                         # 링크 계층 정보
ip link show                    # 인터페이스 상태
ip -s link                      # 통계 정보
ip -4 addr                      # IPv4만
ip -6 addr                      # IPv6만
```

**ifconfig** (구식, 여전히 사용):
```bash
ifconfig                        # 활성 인터페이스
ifconfig -a                     # 모든 인터페이스
ifconfig eth0                   # 특정 인터페이스
```

**인터페이스 이름**:
- **전통적**: eth0, eth1, wlan0
- **예측 가능한 이름** (systemd):
  - `eno1`: 온보드 이더넷
  - `enp3s0`: PCI 슬롯 3, 포트 0
  - `wlp2s0`: 무선 PCI 슬롯 2

### 2.2 인터페이스 설정

**ip 명령어**:
```bash
# IP 주소 설정
ip addr add 192.168.1.100/24 dev eth0
ip addr del 192.168.1.100/24 dev eth0

# 인터페이스 활성화/비활성화
ip link set eth0 up
ip link set eth0 down

# MAC 주소 변경
ip link set eth0 address 00:11:22:33:44:55
```

**ifconfig**:
```bash
ifconfig eth0 192.168.1.100 netmask 255.255.255.0
ifconfig eth0 up
ifconfig eth0 down
ifconfig eth0 hw ether 00:11:22:33:44:55
```

## 3. 라우팅

### 3.1 라우팅 테이블

**확인**:
```bash
ip route                        # 라우팅 테이블
ip route show                   # 동일
route -n                        # 숫자 형식
netstat -rn                     # 숫자 형식
```

**출력 예**:
```
default via 192.168.1.1 dev eth0
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```

### 3.2 라우팅 설정

**ip 명령어**:
```bash
# 기본 게이트웨이
ip route add default via 192.168.1.1

# 특정 네트워크 라우트
ip route add 10.0.0.0/8 via 192.168.1.254
ip route add 172.16.0.0/12 dev eth1

# 라우트 삭제
ip route del default
ip route del 10.0.0.0/8
```

**route 명령어**:
```bash
route add default gw 192.168.1.1
route add -net 10.0.0.0/8 gw 192.168.1.254
route del default
route del -net 10.0.0.0/8
```

### 3.3 IP 포워딩

**일시적 활성화**:
```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
sysctl -w net.ipv4.ip_forward=1
```

**영구 설정**: `/etc/sysctl.conf`
```
net.ipv4.ip_forward = 1
```

**적용**:
```bash
sysctl -p                       # 설정 다시 로드
```

## 4. DNS 설정

### 4.1 /etc/resolv.conf

**DNS 서버 설정**:
```
nameserver 8.8.8.8
nameserver 8.8.4.4
search example.com
domain example.com
```

**필드**:
- `nameserver`: DNS 서버 IP (최대 3개)
- `search`: 검색 도메인 목록
- `domain`: 로컬 도메인

### 4.2 /etc/hosts

**정적 호스트 매핑**:
```
127.0.0.1   localhost localhost.localdomain
192.168.1.10 server1.example.com server1
192.168.1.20 server2.example.com server2
```

**우선순위**: `/etc/nsswitch.conf`
```
hosts: files dns
```
- `files`: /etc/hosts
- `dns`: DNS 서버

### 4.3 DNS 조회 도구

**host**:
```bash
host example.com                # A 레코드
host -t MX example.com          # MX 레코드
host -t NS example.com          # NS 레코드
host 8.8.8.8                    # 역방향 조회
```

**nslookup**:
```bash
nslookup example.com
nslookup example.com 8.8.8.8    # 특정 DNS 서버
```

**dig**:
```bash
dig example.com                 # 상세 정보
dig example.com +short          # 간단한 출력
dig @8.8.8.8 example.com        # 특정 DNS 서버
dig -x 8.8.8.8                  # 역방향 조회
dig example.com ANY             # 모든 레코드
```

## 5. 네트워크 진단

### 5.1 연결 테스트

**ping**:
```bash
ping 8.8.8.8                    # ICMP 에코
ping -c 4 8.8.8.8               # 4번만
ping -i 0.5 8.8.8.8             # 0.5초 간격
ping -s 1000 8.8.8.8            # 패킷 크기 1000바이트
```

**traceroute/tracepath**:
```bash
traceroute example.com          # 경로 추적
tracepath example.com           # traceroute 대안
```

**mtr** (My TraceRoute):
```bash
mtr example.com                 # 실시간 경로 추적
```

### 5.2 포트 및 연결

**netstat**:
```bash
netstat -tuln                   # TCP/UDP 리스닝 포트
netstat -tupn                   # TCP/UDP 연결 및 PID
netstat -rn                     # 라우팅 테이블
netstat -i                      # 인터페이스 통계
netstat -s                      # 프로토콜 통계
```

**ss** (socket statistics, 권장):
```bash
ss -tuln                        # TCP/UDP 리스닝
ss -tupn                        # TCP/UDP 연결 및 PID
ss -s                           # 요약 통계
ss -t state established         # ESTABLISHED TCP 연결
ss dst 192.168.1.100            # 특정 목적지
```

**lsof**:
```bash
lsof -i                         # 네트워크 연결
lsof -i :80                     # 포트 80
lsof -i TCP:22                  # TCP 22번 포트
lsof -i @192.168.1.100          # 특정 호스트
```

**nc (netcat)**:
```bash
nc -zv example.com 80           # 포트 스캔
nc -l 1234                      # 포트 1234 리스닝
nc example.com 1234             # 연결
```

**telnet**:
```bash
telnet example.com 80           # 포트 연결 테스트
```

### 5.3 대역폭 및 성능

**iperf**:
```bash
# 서버
iperf -s                        # 서버 모드

# 클라이언트
iperf -c server_ip              # 대역폭 테스트
```

**tcpdump**:
```bash
tcpdump -i eth0                 # 패킷 캡처
tcpdump -i eth0 port 80         # 포트 80
tcpdump -i eth0 host 192.168.1.100  # 특정 호스트
tcpdump -i eth0 -w capture.pcap # 파일로 저장
tcpdump -r capture.pcap         # 파일 읽기
```

## 6. 네트워크 설정 파일

### 6.1 RHEL/CentOS

**설정 파일**: `/etc/sysconfig/network-scripts/ifcfg-eth0`
```
DEVICE=eth0
BOOTPROTO=static
ONBOOT=yes
IPADDR=192.168.1.100
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=8.8.8.8
DNS2=8.8.4.4
```

**BOOTPROTO**:
- `static`: 고정 IP
- `dhcp`: DHCP
- `none`: 설정 없음

**네트워크 재시작**:
```bash
systemctl restart network       # RHEL 7
nmcli connection reload         # NetworkManager
nmcli connection up eth0
```

### 6.2 Debian/Ubuntu

**설정 파일**: `/etc/network/interfaces`
```
auto eth0
iface eth0 inet static
    address 192.168.1.100
    netmask 255.255.255.0
    gateway 192.168.1.1
    dns-nameservers 8.8.8.8 8.8.4.4

# DHCP
auto eth1
iface eth1 inet dhcp
```

**네트워크 재시작**:
```bash
systemctl restart networking
ifdown eth0 && ifup eth0
```

**Netplan** (Ubuntu 18.04+): `/etc/netplan/*.yaml`
```yaml
network:
  version: 2
  ethernets:
    eth0:
      addresses:
        - 192.168.1.100/24
      gateway4: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
```

**적용**:
```bash
netplan apply
```

## 7. NetworkManager

### 7.1 nmcli 명령어

**연결 관리**:
```bash
nmcli connection show              # 연결 목록
nmcli connection show eth0         # 연결 상세
nmcli connection up eth0           # 연결 활성화
nmcli connection down eth0         # 연결 비활성화
nmcli connection reload            # 설정 다시 로드
nmcli connection delete eth0       # 연결 삭제
```

**디바이스 관리**:
```bash
nmcli device status                # 디바이스 상태
nmcli device show eth0             # 디바이스 상세
nmcli device disconnect eth0       # 디바이스 연결 해제
nmcli device connect eth0          # 디바이스 연결
```

**연결 추가**:
```bash
# 고정 IP
nmcli connection add type ethernet \
  con-name eth0 ifname eth0 \
  ip4 192.168.1.100/24 gw4 192.168.1.1

# DHCP
nmcli connection add type ethernet \
  con-name eth0 ifname eth0 \
  ipv4.method auto
```

**연결 수정**:
```bash
nmcli connection modify eth0 ipv4.addresses 192.168.1.100/24
nmcli connection modify eth0 ipv4.gateway 192.168.1.1
nmcli connection modify eth0 ipv4.dns "8.8.8.8 8.8.4.4"
nmcli connection modify eth0 ipv4.method manual
```

### 7.2 nmtui

**텍스트 UI**:
```bash
nmtui                              # 대화형 인터페이스
```

## 8. 방화벽

### 8.1 firewalld (RHEL/CentOS)

**기본 명령**:
```bash
systemctl start firewalld
systemctl enable firewalld
firewall-cmd --state               # 상태 확인
```

**존(Zone) 관리**:
```bash
firewall-cmd --get-default-zone    # 기본 존
firewall-cmd --set-default-zone=public
firewall-cmd --get-active-zones    # 활성 존
firewall-cmd --list-all            # 현재 존 설정
firewall-cmd --list-all-zones      # 모든 존
```

**서비스 및 포트**:
```bash
firewall-cmd --add-service=http    # 서비스 추가 (임시)
firewall-cmd --add-service=http --permanent  # 영구
firewall-cmd --remove-service=http --permanent
firewall-cmd --add-port=8080/tcp --permanent
firewall-cmd --remove-port=8080/tcp --permanent
firewall-cmd --list-services       # 서비스 목록
firewall-cmd --list-ports          # 포트 목록
firewall-cmd --reload              # 설정 다시 로드
```

### 8.2 iptables

**기본 명령**:
```bash
iptables -L                        # 규칙 목록
iptables -L -n                     # 숫자 형식
iptables -L -v                     # 상세 정보
iptables -F                        # 모든 규칙 삭제
```

**규칙 추가**:
```bash
# 포트 허용
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# 특정 IP 차단
iptables -A INPUT -s 192.168.1.100 -j DROP

# 기본 정책
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT
```

**저장 및 복원**:
```bash
iptables-save > /etc/iptables.rules
iptables-restore < /etc/iptables.rules
```

## 9. 시험 대비 핵심 요약

### IP 주소
- **사설 IP**: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
- **루프백**: 127.0.0.1

### 인터페이스
- **확인**: `ip addr`, `ifconfig`
- **설정**: `ip addr add`, `ip link set up`

### 라우팅
- **확인**: `ip route`, `route -n`
- **기본 게이트웨이**: `ip route add default via`

### DNS
- **설정**: `/etc/resolv.conf`
- **정적**: `/etc/hosts`
- **조회**: `host`, `dig`, `nslookup`

### 진단
- **연결**: `ping`, `traceroute`
- **포트**: `netstat -tuln`, `ss -tuln`
- **패킷**: `tcpdump`

### 설정 파일
- **RHEL**: `/etc/sysconfig/network-scripts/ifcfg-*`
- **Debian**: `/etc/network/interfaces`

### NetworkManager
- **명령**: `nmcli`
- **연결**: `nmcli connection show`
- **디바이스**: `nmcli device status`

---

**이전 챕터**: [[07-package-management|패키지 관리]]  
**다음 챕터**: [[09-services-daemons|시스템 서비스 및 데몬]]
