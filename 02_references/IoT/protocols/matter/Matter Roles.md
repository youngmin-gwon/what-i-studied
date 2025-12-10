---
title: Matter Roles
tags: [iot, matter, roles]
aliases: [Matter Device Core Roles]
date modified: 2025-12-10 16:12:08 +09:00
date created: 2025-12-09 18:17:49 +09:00
---

## 🎭 Matter 프로토콜 주요 역할 (Roles)

Matter 네트워크 내에서 장치들은 다음과 같은 논리적 역할을 수행합니다.

| 역할 (Role) | 설명 | 주요 특징 / 기능 |
| :--- | :--- | :--- |
| **Controller** | 네트워크의 제어 중심 | - 기기 검색, 설정, 제어<br>- 예: 스마트폰 앱, AI 스피커, 홈 허브 |
| **Commissioner** | 기기를 네트워크에 등록(초대)하는 주체 | - **Onboarding**, 인증서 교환(PASE) 수행<br>- 일반적으로 Controller(스마트폰)가 이 역할을 겸임 |
| **Commissionee** | 네트워크에 등록되는 신규 기기 | - QR코드/블루투스 등으로 Onboarding 대기 중<br>- 등록 완료 후 **Operational Device**로 전환됨 |
| **Bridge** | Matter 미지원 기기를 연결 | - Zigbee, Z-Wave, BLE 기기를 Matter 네트워크에 논리적으로 매핑<br>- 예: Hue Bridge, SmartThings Hub |
| **Fabric Administrator** | 보안 도메인(Fabric) 관리자 | - ACL(Access Control Lists) 설정 및 권한 관리<br>- 멀티 어드민 환경에서 각 생태계별 관리자 역할 |
| **OCI** (Credentials Issuer) | 인증서 발급자 | - 기기에 **보안 인증서(NOC)** 발급 및 관리<br>- 안전한 통신을 위한 신원 보증 |

---

## 🔋 전력 및 연결 상태에 따른 구분 (ICD)

Matter는 배터리 기기의 효율성을 위해 **ICD (Intermittently Connected Device)** 개념을 도입했습니다.

| 역할 | 설명 | 특징 |
| :--- | :--- | :--- |
| **ICD** | 간헐적으로 연결되는 장치 | - 상시 연결되지 않음 (배터리/전력 절감)<br>- Controller는 기기가 잘 때를 대비해 메시지를 처리/버퍼링해야 함<br>- 예: 전동 블라인드, 스마트 도어락, 센서 |

### 🆚 비교: ICD (Matter) vs SED (Thread)

| 구분 | **SED** (Sleepy End Device) | **ICD** (Intermittently Connected Device) |
| :--- | :--- | :--- |
| **소속** | **[Thread](../thread/Thread.md)** 프로토콜 용어 | **[Matter](Matter.md)** 프로토콜 용어 (Wi-Fi 포함) |
| **동작 방식** | 주기적(Polling)으로 깨어나 부모에게 데이터 요청 | 필요할 때만 연결(LIT) 또는 주기적 연결(SIT) |
| **전력 소비** | 낮음 (주기적 깨어남으로 소량 소모) | **매우 낮음** (LIT 지원 시 극대화 가능) |
| **대기 시간** | 짧음~중간 (Polling 주기에 따름) | 높을 수 있음 (기기가 깨어날 때까지 대기 필요) |
| **적용 대상** | Thread 배터리 센서 | Wi-Fi 도어락, Thread 센서 등 포괄적 |

> [!NOTE]
> **ICD**는 Matter 1.2/1.3에서 정립된 개념으로, 기존 Thread의 **SED** 개념을 Wi-Fi 기기까지 확장하고, 휴면 시간(Idle Time)을 더 길게 가져갈 수 있도록 개선한 모델입니다.
