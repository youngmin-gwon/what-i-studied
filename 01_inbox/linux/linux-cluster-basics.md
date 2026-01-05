---
title: Linux Cluster Basics
tags: [linux, cluster, high-availability, hpc, load-balancing]
aliases: [클러스터링, 리눅스 클러스터]
date modified: 2026-01-06 00:02:44 +09:00
date created: 2026-01-06 00:02:44 +09:00
---

## 🌐 개요 (Overview)

**클러스터링(Clustering)**은 여러 대의 독립된 컴퓨터(노드)를 유기적으로 연결하여 하나의 시스템처럼 동작하게 만드는 기술입니다. 목적에 따라 크게 3가지 유형으로 나뉩니다.

## 🔑 클러스터의 3대 유형

### 1. 고가용성 클러스터 (High Availability Cluster, HA)

**지속적인 서비스 제공** 이 제1목적인 클러스터입니다.

*   **동작 원리**: 특정 노드에 에러가 발생하여 서비스가 중단될 경우, 대기하고 있던 **백업 노드가 즉시 해당 역할을 대신 수행(Failover)** 합니다.
*   **특징**: 서비스 가동 시간(Uptime)을 극대화하여 비즈니스 연속성을 보장합니다.
*   **주요 도구**: Keepalived, Pacemaker, Heartbeat.

### 2. 고계산용 클러스터 (High Performance Computing, HPC)

**강력한 계산 능력**이 목적인 클러스터입니다.

*   **동작 원리**: 하나의 거대한 작업을 여러 노드에 나누어 병렬로 처리합니다. (슈퍼컴퓨터 구축 시 사용)
*   **특징**: 기상 예보, 유전자 분석, 시뮬레이션 등 방대한 연산이 필요한 분야에 사용됩니다.
*   **주요 도구**: Beowulf Cluster, MPI(Message Passing Interface).

### 3. 부하분산 클러스터 (Load Balancing Cluster, LVS)

**사용자 요청을 분산**하여 과부하를 방지하는 클러스터입니다.

*   **동작 원리**: 중앙의 로드 밸런서가 대량의 사용자 요청을 받아 여러 대의 백엔드 서버로 골고루 분산시킵니다.
*   **특징**: 특정 서버에 트래픽이 몰리는 것을 방지하고 전체 시스템의 처리 용량을 늘립니다.
*   **주요 도구**: LVS (Linux Virtual Server), Nginx, HAProxy.

---

## 📊 클러스터 유형 비교 요약

| 유형 | 핵심 목적 | 키워드 | 활용 예 |
| :--- | :--- | :--- | :--- |
| **HA (고가용성)** | 가용성 보장 | Failover, 백업 노드 | 금융 시스템, DB 서버 |
| **HPC (고계산용)** | 연산력 극대화 | 병렬 처리, 슈퍼컴퓨터 | 기상청, 과학 분석 |
| **LVS (부하분산)** | 트래픽 분산 | Load Balancer, 성능 확장 | 대규모 웹 서비스 |

---

## 🔗 연결 문서 (Related Documents)

- [[process-states-lifecycle]] - 병렬 처리와 프로세스 관리
- [[service-management-commands]] - 클러스터 노드 내 서비스 관리
- [[network-commands]] - 로드 밸런싱을 위한 네트워크 설정
