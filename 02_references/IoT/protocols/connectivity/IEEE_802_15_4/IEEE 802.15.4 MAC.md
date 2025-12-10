---
title: IEEE 802.15.4 MAC
tags: [frame, mac, security, standard]
aliases: []
date modified: 2025-12-10 00:13:12 +09:00
date created: 2025-12-10 00:09:24 +09:00
---

## 🌐 개요 (Overview)
**IEEE 802.15.4 MAC** 계층은 물리 계층 (PHY) 위에서 데이터의 신뢰성 있는 전송, 충돌 방지, 보안을 담당합니다. 상위 프로토콜 (Zigbee/Thread) 이 라디오 하드웨어를 제어하는 인터페이스 역할을 합니다.

## ⚙️ 주요 기능 (Key Functions)

1. **매체 접근 제어**:**[CSMA-CA](../../foundation/CSMA-CA.md)** 알고리즘을 사용하여 데이터 충돌을 방지합니다.
2. **비콘 관리 (Beacon Management)**: (비콘 모드 사용 시) 네트워크 동기화를 위한 비콘 신호를 생성하고 감지합니다.
3. **보안 (Security)**: AES-128 암호화 엔진을 하드웨어 레벨에서 지원합니다.
4. **ACK (Acknowledgement)**: 데이터가 잘 도착했는지 확인하는 응답 프레임 처리.

## 📦 프레임 구조 (Frame Structure)

MAC 프레임 (MPDU) 은 최대 127 바이트입니다.

| 필드 | 크기 | 설명 |
| :--- | :--- | :--- |
| **Frame Control** | 2 Bytes | 프레임 타입 (데이터/ACK/Command), 주소 모드, 보안 설정 등. |
| **Sequence Number** | 1 Byte | 패킷 순서 번호. |
| **Addressing** | 0~20 Bytes | PAN ID (네트워크 ID) 와 Source/Destination 주소 (16 비트 Short 또는 64 비트 Extended). |
| **Payload** | 가변 | 실제 데이터 (IP 패킷이나 Zigbee 명령). |
| **FCS** | 2 Bytes | 에러 검출용 체크섬 (CRC). |

## ⏲️ 슈퍼프레임 (Superframe) 구조

비콘 모드 네트워크에서는 시간을 "슈퍼프레임"이라는 단위로 쪼개서 관리합니다.

- **Active Period**: 기기들이 깨어 있는 시간.
- **Inactive Period**: 모두가 잠드는 (Sleep) 시간. (저전력의 핵심)
- **GTS (Guaranteed Time Slot)**: 특정 기기에게 우선권을 주는 예약된 시간 슬롯. (실시간성이 필요한 경우 사용)

>[!NOTE]
>현대적인 **Zigbee 3.0** 이나**Thread** 는 주로**Non-beacon 모드** 를 사용합니다. 즉, 주기적으로 깨어나서 "나한테 온 거 있어?" 하고 물어보코 (Polling) 다시 잡니다.
