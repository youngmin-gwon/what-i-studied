---
title: IEEE 802.11 MAC
tags: [csma, frame, mac, wifi]
aliases: []
date modified: 2025-12-10 00:11:52 +09:00
date created: 2025-12-10 00:10:33 +09:00
---

## 🌐 개요 (Overview)

**IEEE 802.11 MAC** 계층은 유선 이더넷과 유사한 사용자 경험을 무선에서 제공하기 위해 설계되었습니다.**[CSMA/CA](../../foundation/CSMA-CA.md)** 를 사용하여 여러 기기가 공기를 공평하게 나눠 쓰도록 관리합니다.

## 🚦 매체 접근 제어 (Access Control)

1. **DCF (Distributed Coordination Function)**:
    - 기본적인 경쟁 방식입니다. 서로 눈치보다가 (CSMA/CA) 빈틈이 보이면 보냅니다.
2. **PCF (Point Coordination Function)**:
    - AP 가 "너 지금 말해"라고 순서를 정해주는 방식 (Polling) 이지만, 실제로는 거의 안 쓰입니다.

## 📦 프레임 유형 (Frame Types)

Wi-Fi 패킷은 크게 세 가지 종류가 있습니다.

1. **Management Frames (관리 프레임)**:
    - 네트워크의 연결/해제를 담당합니다. (데이터 전송 X)
    - 예: **Beacon**(나 여기 있어),** Probe Request**(공유기 찾기),** Association** (비밀번호 치고 연결하기).
2. **Control Frames (제어 프레임)**:
    - 데이터 전송을 돕는 신호입니다.
    - 예: **RTS/CTS**(교통 정리),** ACK** (잘 받았어).
3. **Data Frames (데이터 프레임)**:
    - 실제 IP 패킷 (유튜브 영상, 웹페이지 등) 을 실어 나릅니다.

## 🔋 전력 관리 (Power Save)

Wi-Fi 는 전력을 많이 먹기 때문에 절전 기능이 필수입니다.

- **DTIM (Delivery Traffic Indication Map)**: AP 가 "자고 있는 애들아, 너네 줄 데이터 쌓여있으니 일어나라"고 비콘에 실어 보내는 신호입니다.
- **TWT (Target Wake Time)**:** Wi-Fi 6 (802.11ax)** 의 핵심 기능. 기기가 "나는 새벽 3 시에만 깰 거야"라고 AP 와 미리 약속해서 배터리를 아낍니다. (IoT 에 매우 중요)
