---
title: mDNS
tags: [discovery, dns, iot, network, zeroconf]
aliases: [Bonjour, DNS-SD, ZeroConf]
date modified: 2025-12-10 00:07:52 +09:00
date created: 2025-12-09 18:53:54 +09:00
---

## 🌐 개요 (Overview)

**mDNS (Multicast DNS)** 와 **DNS-SD (DNS Service Discovery)** 는 로컬 네트워크에서 별도의 설정 없이 기기들이 서로를 자동으로 찾아내는 기술입니다. 흔히 **ZeroConf** 또는 Apple 의 **Bonjour**로 알려져 있습니다.

>[!NOTE]
>[[../matter/Matter]] 기기는 처음 켜졌을 때나 IP 주소가 바뀌었을 때, "나 여기 있어요!"라고 네트워크 전체에 소리칩니다 (Multicast). 덕분에 사용자가 IP 주소를 몰라도 스마트폰 앱이 자동으로 기기를 감지할 수 있습니다.

## 🏗️ 작동 원리 (How it works)

### 1. mDNS (Multicast DNS)

- **이름 풀이**: `light-bulb.local` 같은 로컬 도메인 이름을 IP 주소 (`192.168.0.5` 또는 `fe80::…`) 로 변환합니다.
- **방식**: 네트워크 내의 모든 기기 (멀티캐스트 그룹) 에게 "light-bulb.local 누구니?"라고 물어보고, 해당 기기가 "저요!" 하고 답하는 방식입니다.

### 2. DNS-SD (Service Discovery)

- **서비스 검색**: 특정 **이름**이 아니라, **기능 (Service Type)** 으로 기기를 찾습니다.
- **예시**: "이 네트워크에 'Matter 기기 (`_matter._tcp`)'인 애들 다 나와봐."
    - 응답: "저요 (전구), 저요 (스위치), 저요 (센서)…"

## 🏠 Matter 에서의 역할

1. **초기 발견 (Commissioning Discovery)**: 아직 Wi-Fi/Thread 자격 증명이 없는 기기가 "나 설정 대기 중입니다"라고 광고할 때 사용합니다 (주로 BLE 를 쓰지만 IP 기반 발견도 지원).
2. **운영 중 발견 (Operational Discovery)**: 이미 네트워크에 붙은 기기들이 서로의 최신 IP 주소를 알아낼 때 사용합니다. (예: 허브가 전구의 바뀐 IP 를 찾을 때).

>[!TIP]
> **Thread** 네트워크 내부에서는 mDNS 패킷이 너무 시끄럽기 때문에 (트래픽 과다), **SRP (Service Registration Protocol)** 라는 더 효율적인 방식을 사용합니다. 하지만 **[Border Router](../thread/Border%20Router.md)** 가 이를 다시 mDNS 로 변환하여 Wi-Fi 네트워크에 뿌려주므로, 사용자 입장에서는 어디에 있든 똑같이 보입니다.
