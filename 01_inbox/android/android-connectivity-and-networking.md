# Connectivity & Networking #android #android/connectivity #android/net

[[android-activity-manager-and-system-services]] · [[android-hal-and-kernel]] · [[android-adb-and-images]]

## ConnectivityService 개요
- NetworkAgent(transport-specific)와 NetworkRequest 매칭으로 default network 선정. score 기반 우선순위.
- NetworkCapabilities로 transport/capabilities/bandwidth/validated 여부 표기. captive portal detection, Private DNS 결정.
- per-UID routing/table, VPN overlay, enterprise/work profile 분리.

## Wi-Fi 스택
- Wi-Fi HAL(Wifi HAL/Hostapd/Supplicant) + wificond + WifiService. firmware offload(Scan/PNO/roaming) 활용.
- Passpoint/Hotspot 2.0, WPA3/OWE, MAC randomization. Dual STA/SoftAP concurrency 제약.
- Wi-Fi Aware/RTT(IEEE 802.11mc), Wi-Fi Direct. regulatory domain 설정, 6GHz AFC.
- roaming: fast transition(802.11r/k/v), PMK caching, BSSID stickiness heuristics. RSSI thresholds/hysteresis 튜닝.
- power: Adaptive connectivity, wifi suspend optimizations, scan throttling, location gating.

## 셀룰러/IMS
- Radio HAL(1.x→AIDL) + RILJ + telephony framework. multi-SIM/DSDS/DSDA 정책, SIM/ESIM 관리(euicc/CarrierConfig).
- IMS stack for VoLTE/VoWiFi/SMSoIP, emergency call routing. Carrier provisioning via CarrierConfigManager.
- 5G NSA/SA indicators, NR availability callbacks, slicing 연구. signal strength/throughput/registration state dispatch.
- CBRS/PLMN selection, roaming policy, APN selection order(default/supl/mms/dun). Data throttling policy, data stall detection.

## VPN/프록시/방화벽
- VpnService 기반 앱 VPN, Platform VPN(Work profile/managed device). split tunneling, per-app VPN.
- Proxy settings(global/per-network). firewall via netd/iptables/ebpf. lockdown mode for work profile.
- Always-on/lockdown VPN, captive portal vs VPN interactions. DNS over TLS interplay.

## 네트워크 성능/품질 관리
- Multipath(TCP/QUIC) experiments, tethering offload(eBPF) for low CPU. TrafficStats UID tags, NetworkStatsService persistence.
- QOS APIs/QOS callback, bandwidth estimator. Congestion control(BBR/Cubic), QUIC adoption(Cronet).
- JobScheduler/WorkManager network constraints(METERED/UNMETERED/NOT_ROAMING). background data policy.
- LinkLayer stats: radio firmware metrics, wifi packet stats, cts/netd validation. TCP info(ssthresh, rtt, cwnd) via /proc/net.
- Connection migration experiments, HTTP3 zero-RTT, socket tagging for attribution. captive portal scoring/validation timers.\n

## 보안/프라이버시
- Private DNS/DoT default. Cleartext traffic opt-in via Network Security Config.
- per-app netd firewall rules; restricted networking mode. VPN bypass rules carefully controlled.
- Network permission: INTERNET(normal), CONNECTIVITY_INTERNAL/NETWORK_STACK signature-level. location gating for Wi-Fi/Bluetooth scans.
- Wi-Fi scanning/Probe MAC randomization by default. Bluetooth LE address rotation. network location provider privacy dashboard.

## BLE/Nearby
- BLE Central/Peripheral roles, advertising limits, background scan throttling. PHY 2M/long-range(Coded) modes.
- Nearby/ULP scanning, fast pair, hardware filters. permissions(BLUETOOTH_SCAN/CONNECT/ADVERTISE + location).

## Tethering/Hotspot
- tethering entitlement, carrier provisioning. USB/Wi-Fi/BT tethering paths.
- IPv6/IPv4 translation(clat464) with eBPF offload. per-interface quotas and stats.

## Debugging/도구
- `adb shell dumpsys connectivity`, `cmd connectivity`, `cmd wifi`, `cmd netpolicy`, `cmd network_score`.
- `adb shell ip rule/route`, `iptables -t mangle -L`, `ifconfig`/`ip addr`, `wpa_cli`/`hostapd_cli`.
- `adb bugreport`의 connectivity section, netstats history, tcpdump/pcap capture. perfetto nettrack(tracebox) slices.
- diag/logcat tags: ConnectivityService/WifiNative/WifiClientModeImpl/TelephonyRIL/IMS. `adb shell dumpsys wifi proto` for metrics.\n
- DNS debugging: `getprop | grep dns`, `resolv.conf` equivalent via netd resolver config, doh/dot settings. `adb shell cmd connectivity flush-caches`.
- Network Stack mainline module 업데이트 여부 확인(`adb shell dumpsys package com.android.networkstack`). Captive portal probe urls/strategy.
- Testing: cts/net tests, network stacking test app, iperf throughput tests, airplane/roaming toggles, failover scenarios.\n
- Field issues: flaky wifi caused by power saving/roaming; collect bugreport with kernel logs. telephony drop debug via modem logs/QXDM(if permitted).
- netpolicy: data saver, background restrict, network templates, billing cycle, quota. enterprise/work profile separate policies.\n

## 진화/전환
- netd iptables → eBPF datapath; tethering offload and stats via bpfloader/mainline network stack.
- Radio HAL HIDL → AIDL; multi-SIM and IMS modularization. wifi hal vendor interface stabilization.
- QUIC/HTTP3 adoption, DoH/DoT/Private DNS defaults, MAC randomization by default, per-app networking restrictions.

## Graph Links
- [[android-security-and-sandboxing]]: 권한/NetPolicy/SELinux 연계.
- [[android-performance-and-debug]]: 네트워크 프로파일링/효율. [[android-customization-and-oem]]: 캐리어/지역화 설정.
