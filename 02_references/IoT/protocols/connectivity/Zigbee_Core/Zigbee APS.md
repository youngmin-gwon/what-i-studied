---
title: Zigbee APS
tags: [application, binding, zigbee]
aliases: [Application Support Sub-layer]
date modified: 2025-12-10 00:13:51 +09:00
date created: 2025-12-10 00:11:26 +09:00
---

## 🌐 개요 (Overview)

**Zigbee APS (Application Support Sub-layer)** 는 네트워크 계층 (NWK) 과 실제 기능 (ZCL Application) 사이를 이어주는 접착제 역할을 합니다. "어느 전구의 어떤 기능"을 제어할지 교통정리를 해줍니다.

## 🎯 주요 기능 (Key Functions)

1. **바인딩 (Binding)**:
    - **논리적 연결**을 생성합니다. 스위치 (Source) 와 전구 (Destination) 를 "묶어 (Bind)" 줍니다.
    - 스위치는 "전구 1 번 켜"라고 하지 않고, 그냥 "나 켜졌어"라고 APS 에 던지면, APS 가 바인딩 테이블 (Binding Table) 을 보고 알아서 대상 전구들에게 메시지를 쏩니다.
2. **그룹 (Groups)**:
    - 여러 전구를 하나의 **Group ID**로 묶어서 동시에 제어할 때 사용합니다. (거실 전등 전체 끄기 등)
3. **엔드포인트 매핑 (Endpoint Mapping)**:
    - 하나의 하드웨어 안에 여러 기능이 있을 때 (예: 2 구 스위치), 각각을 **Endpoint** (1 번, 2 번…) 로 구분하여 전달합니다.
    - 마치 IP 주소 뒤에 붙는 **Port 번호**와 유사한 개념입니다.
4. **신뢰성 (Reliability)**:
    - **APS ACK**: 목적지 앱까지 진짜 도착했는지 확인하는 최종 응답입니다. (MAC ACK 는 옆집까지만 갔다는 뜻이고, APS ACK 는 최종 목적지 도달 확인입니다.)

## 📦 데이터 구조

- **Cluster ID**: 명령의 종류 (예: On/Off 클러스터 `0x0006`, 레벨 제어 `0x0008`).
- **Profile ID**: 응용 분야 (예: 홈 오토메이션 `0x0104`).
- **Endpoint**: 기기 내의 세부 장치 번호.
