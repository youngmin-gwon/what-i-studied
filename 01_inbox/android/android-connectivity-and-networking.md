---
title: android-connectivity-and-networking
tags: [android, android/connectivity, android/net]
aliases: []
date modified: 2025-12-16 20:46:57 +09:00
date created: 2025-12-16 15:35:13 +09:00
---

## Connectivity & Networking android android/connectivity android/net

기기가 인터넷과 통신하는 과정을 쉽게 풀었다. 용어는 [[android-glossary]].

### 전체 그림
- ConnectivityService 가 "어떤 네트워크를 누구에게 줄지" 결정한다.
- 네트워크 특성 (와이파이/셀룰러/VPN/블루투스) 과 점수, 비용 (무제한/과금) 을 보고 고른다.

### Wi‑Fi
- wificond + supplicant/hostapd + HAL 이 무선 칩과 대화한다.
- WPA3/OWE 같은 암호, MAC 랜덤화로 보안을 높인다.
- 빠른 로밍 (802.11r/k/v) 과 절전 (스캔 억제) 으로 체감 품질과 배터리를 동시에 잡는다.

### 셀룰러/IMS
- Radio HAL 과 Telephony framework 가 모뎀을 제어한다.
- 통화/문자/데이터는 IMS(VoLTE/VoWiFi 등) 를 통해 IP 기반으로 전달될 수 있다.
- eSIM/DSDS(듀얼 SIM) 정책, 5G/NR 상태를 관리한다.

### VPN/방화벽
- VpnService 로 앱이 직접 VPN 을 만들 수 있다. 기업/개인 프로필을 분리하는 플랫폼 VPN 도 있다.
- netd/eBPF 가 방화벽과 트래픽 계측을 처리한다. Data Saver 나 제한 모드도 여기서 동작한다.

### 품질 관리
- 캡티브 포털 감지로 로그인 페이지를 알려준다.
- NetworkCapabilities 에 대역폭/비용/검증 여부를 표시해 앱이 판단하도록 한다.
- JobScheduler/WorkManager 가 네트워크 조건을 보고 작업을 미룬다.

### 프라이버시/보안
- Private DNS(DoT) 를 기본값으로 켠다.
- 위치 권한이 있어야 스캔 결과를 볼 수 있다. BLE/Wi‑Fi 스캔은 백그라운드에서 제한된다.
- VPN 이 켜진 앱은 다른 네트워크를 우회해 데이터를 보낸다 (Always‑on/Lockdown).

### 디버깅
- `adb shell dumpsys connectivity/wifi/netpolicy` 로 상태를 본다.
- `ip rule/route`, `iptables -t mangle -L` 로 실제 라우팅/방화벽을 확인한다.
- tcpdump/pcap, perfetto nettrack 으로 패킷과 지연을 본다.

### 링크

[[android-activity-manager-and-system-services]], [[android-hal-and-kernel]], [[android-adb-and-images]], [[android-security-and-sandboxing]].
