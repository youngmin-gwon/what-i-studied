---
title: ZCL (Zigbee Cluster Library)
tags: [iot, protocol, zigbee, matter, data-model]
aliases: [Zigbee Cluster Library, Dotdot]
date created: 2025-12-09
---

## 🌐 개요 (Overview)
**ZCL (Zigbee Cluster Library)**는 기기가 **"무엇을 할 수 있는지"**를 정의하는 표준 애플리케이션 계층(Layer 7) 언어입니다.

> [!NOTE]
> [[Zigbee]]뿐만 아니라 **[[Matter]]**의 데이터 모델(Data Model)의 모태가 된 매우 중요한 표준입니다. Matter는 사실상 "IP 위의 ZCL"이라고 봐도 무방할 정도로 ZCL의 구조를 계승했습니다.

## 🏗️ 구조 (Structure)
ZCL은 기기의 기능을 **클러스터(Cluster)**라는 단위로 묶어서 관리합니다.

### 1. Cluster (클러스터)
특정 기능에 대한 속성과 명령의 집합입니다. 각 클러스터는 고유 ID를 가집니다.
- **예시**:
    - `0x0006` (On/Off): 켜고 끄는 기능.
    - `0x0008` (Level Control): 밝기나 볼륨 조절.
    - `0x0201` (Thermostat): 온도 조절.

### 2. Attribute (속성)
클러스터 내부의 **상태 값**입니다. 읽기(Read) 또는 쓰기(Write)가 가능합니다.
- **On/Off 클러스터의 예**:
    - `OnOff` (Boolean): 현재 켜져 있는지 꺼져 있는지 (True/False).
- **Level Control 클러스터의 예**:
    - `CurrentLevel` (Int8): 현재 밝기 값 (0~254).

### 3. Command (명령)
기기에게 특정 **행동**을 수행하도록 지시하는 메시지입니다.
- **On/Off 클러스터의 예**:
    - `TurnOn`: 켜라.
    - `TurnOff`: 꺼라.
    - `Toggle`: 상태를 반전시켜라.

## 🔄 진화 (Evolution): Zigbee에서 Matter로
ZCL은 단순한 Zigbee용 언어를 넘어 스마트홈 업계의 표준 모델로 자리 잡았습니다.

1.  **Zigbee PRO**: ZCL이 널리 사용됨 (Philips Hue, SmartThings 등).
2.  **Dotdot**: Thread Group과 Zigbee Alliance가 ZCL을 IP 네트워크에서도 쓰자고 만든 규격.
3.  **[[Matter]]**: Dotdot의 개념을 이어받아, ZCL을 현대적으로 다듬어(Interaction Model) Matter의 핵심 데이터 모델로 채택함.

> [!TIP]
> 개발자 입장에서 [[Zigbee]]를 다뤄봤다면 [[Matter]] 개발이 익숙하게 느껴지는 이유가 바로 이 **ZCL 기반의 공통된 DNA** 때문입니다.
