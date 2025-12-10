---
title: Thread Roles
tags: [iot, roles, thread]
aliases: [Thread Device Types]
date modified: 2025-12-10 15:34:04 +09:00
date created: 2025-12-09 18:18:05 +09:00
---

## 🕸️ Thread 네트워크 주요 역할 (Roles)

[Thread](Thread.md) 네트워크를 구성하는 장치들의 물리적/논리적 역할입니다.

| 역할 (Role)                               | 설명                            | 주요 특징 / 기능                                                                                                                    |
| :-------------------------------------- | :---------------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| **[Border Router](Border%20Router.md)**|** Thread ↔ IP 네트워크**간 라우팅 역할 | - Thread(저전력) 와 Wi-Fi/이더넷 (고속) 네트워크 간의** IP 브리지**<br>- 외부 인터넷 연결 또는 로컬망 내 다른 Matter 기기와의 통신 중계<br>- 예: HomePod mini, Nest Hub |
| **Leader**                              | 네트워크 관리자                      | - 네트워크 파라미터 (PAN ID 등) 관리<br>- 라우터 중 한 대가 동적으로 선출됨 (고장 시 자동 승계)                                                               |
| **Router**| 메시지 중계자                       | - 상시 전원 (Mains Powered) 기기<br>- 패킷을 다른 노드로 전달하여** Mesh** 네트워크 확장                                                              |
| **Proxy Device**                        | 메시지 중계 대행                     | - Border Router 역할을 일부 보조하거나 메시지 중계<br>- 네트워크 경계 (Border) 는 아니지만 확장성 향상에 기여                                                   |
| **End Device**                          | 말단 장치                         | - 라우팅 (중계) 기능 없음. 주로 데이터의 최종 목적지/생성지.                                                                                         |

### 🆚 비교: Router vs Border Router

많은 분들이 헷갈려하는 두 역할의 차이점입니다.

| 구분        | **Router**(라우터)                       |** Border Router** (보더 라우터)                     |
| :-------- | :------------------------------------- | :--------------------------------------------- |
| **핵심 역할**|**[Thread](Thread.md)** 네트워크**내부** 확장 |**[Thread](Thread.md)** 와**외부 (Wi-Fi/LAN)** 연결 |
| **통신 대상** | Thread 기기끼리만 통신                        | Thread 기기 ↔ 스마트폰/클라우드 통신                       |
| **비유**| 아파트 단지 내** 도로 확장 공사**| 아파트 단지와 고속도로를 잇는** 톨게이트**                      |
| **필수 여부**| 집이 넓으면 필수 (커버리지 확장)                    | 외부 제어 (Siri, HomeKit 등) 를 위해** 필수**            |
| **하드웨어**  | 전구, 플러그 등 상시 전원 기기                     | AI 스피커 (HomePod), Hub (Nest Hub) 등             |

---

## 💤 전력/기능에 따른 구분 (Device Types)

### 1. FTD (Full Thread Device)

- **항상 켜져 있음** (상시 전원).
- **Router** 역할을 수행할 수 있는 잠재력이 있음. (Router Eligible End Device =**REED**)
- 주변 기기의 부모 (Parent) 가 되어 데이터를 중계해 줄 수 있음.

### 2. MTD (Minimal Thread Device)

- 라우팅 (중계) 기능이 삭제된 가벼운 스택.
- **SED (Sleepy End Device)**:
    - **Thread 기반 저전력 디바이스**.
    - 대부분 수면 (Sleep) 상태로 있다가 **주기적** 으로 깨어나 (Polling) 부모 (Router) 에게 메시지를 확인.
    - 예: 배터리 구동 센서, 버튼.
- **SSED (Synchronized SED)**: Thread 1.2+ 더 정밀하게 동기화되어 깨어남 (반응 속도 개선).
