---
title: SQLite와 Room의 경계는 엔진과 애플리케이션 API의 차이다
tags: [android, android/data, android/storage, android/persistence-contracts]
aliases: ["SQLite와 Room의 경계는 엔진과 애플리케이션 API의 차이다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# SQLite와 Room의 경계는 엔진과 애플리케이션 API의 차이다

상위 문서: [영속 저장소 계약](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md)


SQLite는 Android에 내장된 관계형 데이터베이스 엔진이다.

Room은 SQLite를 대체하는 별도 저장 엔진이 아니라 SQLite 접근을 감싸는 추상화다.

## 직접 SQLite를 쓰는 경우

- 기존 SQLite 파일을 그대로 마이그레이션해야 한다.
- Room이 노출하지 않는 특수한 저수준 기능이 필요하다.
- 기존 라이브러리나 C/C++ 계층이 SQLite를 직접 소유한다.
- 이미 정해진 raw query와 스키마 계약을 유지해야 한다.

이런 경우에도 연결 수명, transaction, cursor 닫기, thread 규칙을 직접 관리해야 한다.

## 일반 앱의 기본 경계

새로운 앱 내부 데이터베이스라면 Room을 먼저 검토한다.

Entity와 DAO 선언으로 스키마와 쿼리 의도를 코드에 남길 수 있다.

컴파일 시점 query 검증과 generated code가 반복적인 오류를 줄인다.

`Flow`와의 통합도 기본 제공되어 변경된 결과를 관찰하기 쉽다.

## Room이 숨기지 않는 것

Room을 사용해도 SQL과 schema 설계가 사라지는 것은 아니다.

인덱스, primary key, foreign key, nullability, transaction 경계를 설계해야 한다.

migration을 누락하면 기존 사용자 데이터에서 앱이 실패할 수 있다.

Room의 편의성은 데이터 모델링 책임을 없애는 것이 아니라 접근 코드를 표준화한다.

## 선택 규칙

새 기능의 누적 데이터는 Room DAO로 시작한다.

기존 DB를 보존해야 한다면 먼저 현재 schema와 소유자를 확인한다.

외부 라이브러리가 DB 파일을 직접 관리한다면 Room과 임의로 공동 소유하지 않는다.

단순 설정값을 SQLite 테이블로 만든다고 해서 관계형 이점이 생기지는 않는다.
