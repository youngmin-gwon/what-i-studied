## 프로그램 설치

```bash
brew install socat
brew install --cask xquartz
```
- xquartz(Xserver) 
<blockquote>
mac에서 작동하는 X Window System의 일종.<br>
일종의 가상 모니터.<br><br>

* X Window System: UNIX 계열의 OS에서 비트맵 화면을 띄우는 시스템
</blockquote>
- socat
<blockquote>
두 개의 데이터 채널을 연결해주는 중계기 역할.<br>
UNIX, IP4, UDP, TCP 등 다양한 통신규격을 지원.<br>
여기서는 도커에서 출력하는 TCP 통신을 받아 xquartz가 받고 있는 UNIX client로 전달해주는 역할
</blockquote>

xquartz -> settings -> security -> allow connections from network clients

![XQuartz Setting](https://raw.githubusercontent.com/youngmin-gwon/what-i-studied/main/assets/xquartz-setting.png)

## socat & xquartz setup

socat으로 xquartz 연결
(!xquartz 먼저 실행하면 socat[3563] E bind(5, {LEN=0 AF=2 0.0.0.0:6000}, 16): Address already in use 에러 발생)

```bash
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
```

```bash
open -a XQuartz
```

## docker container 생성

IP address 확인
```bash
ifconfig en0
```
>en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
        options=6463<RXCSUM,TXCSUM,TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
        ether ac:c9:06:1b:f2:52
        inet6 fe80::8c7:c5d7:66e0:540b%en0 prefixlen 64 secured scopeid 0xc
        inet <span style="color:yellow">192.168.1.49</span> netmask 0xffffff00 broadcast 192.168.1.255
        nd6 options=201<PERFORMNUD,DAD>
        media: autoselect
        status: active

확인한  IP <span style="color:yellow">X.X.X.X</span> 활용하여 컨테이너 실행

```bash
docker run -it --privileged --net=host --name={컨테이너 이름} -e DISPLAY=X.X.X.X:0 -p 8888:8888 -p 6006:6006 {docker image} /bin/bash
```

<span style="color:red">TODO: m1 환경에서 rviz, gazebo 사용 제한되는 경우가 있다하니 문제 해결하여 문서 작성</span>

## cf) 컨테이너의 ip 변경해야 하는 경우

```bash
export DISPLAY=X.X.X.X
```