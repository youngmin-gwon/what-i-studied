---
title: appsearch-contracts
tags: ["android", "android/system-services"]
aliases: ["AppSearch 접근 계약"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-05 10:00:00 +09:00
---

## AppSearch 접근 계약

이 지도는 AndroidX **AppSearch**(앱의 구조화된 로컬 데이터를 색인하여 오프라인 전문 검색과 시스템 전역 통합 검색을 제공하는 온디바이스 검색 엔진 라이브러리)가 데이터를 색인해 오프라인 전문 검색과 시스템 전역 검색(설정 앱 검색, 향후 Assistant 연동)에 노출하는 계약을 저장소 선택과 스키마 마이그레이션 두 가지로 나눈다. AppSearch는 클라우드 검색 엔진이 아니라 온디바이스 검색 색인이며, 이 전제를 놓치면 저장소 선택과 스키마 변경 배포 모두 잘못된 모델을 기준으로 하게 된다.

### 읽는 순서

1. [AppSearch는 클라우드 검색 엔진이 아니라 온디바이스 검색 색인이다](./appsearch-is-an-on-device-search-index-not-a-cloud-search-engine.md)에서 `LocalStorage`(앱 전용 저장소), `PlatformStorage`(Android 12+ 시스템 전역 저장소), `PlayServicesStorage`(구형 기기용 전역 저장소) 선택과 System UI 노출 옵트인 계약을 먼저 본다.
2. [Document 스키마 변경은 명시적 마이그레이션이 없으면 호환되지 않는 데이터를 삭제한다](./document-schema-changes-require-explicit-migration-or-forceoverride-deletes-data.md)에서 `Migrator`와 `forceOverride`가 스키마 버전 변경을 어떻게 다르게 처리하는지 본다.

### 문제 분류

| 증상 또는 질문 | 먼저 확인할 경계 |
| --- | --- |
| 설정 앱 검색에 내 데이터가 안 뜬다 | `PlatformStorage`/`PlayServicesStorage`를 쓰고 있는지, 해당 스키마 타입에 `setSchemaTypeDisplayedBySystem(true)`를 켰는지 |
| 스키마를 바꿔 배포했더니 기존 데이터가 사라졌다 | `Migrator` 없이 비호환 변경을 `forceOverride(true)`로 배포했는지 |
| `setSchema()` 호출이 `AppSearchException`을 던진다 | 비호환 스키마 변경에 `Migrator`도 `forceOverride`도 지정하지 않았는지 |
| 앱 안에서만 쓰는 검색인데 시스템 전역 저장소를 골랐다 | `LocalStorage`로 충분한 요구사항인지 |

### 책임 경계

- 이 지도는 `AppSearch`를 통한 로컬 구조화 데이터의 색인·검색·스키마 계약만 다룬다. 검색 랭킹 알고리즘 내부(토크나이저, relevance scoring)나 쿼리 문법 세부는 다루지 않는다.
- AppSearch는 기기 안에서 색인을 관리하는 온디바이스 라이브러리이지 클라우드 동기화 서비스가 아니다. 여러 기기 간 데이터 동기화는 이 지도의 범위가 아니다.
- 일반적인 관계형/키-값 로컬 저장(Room, SQLite, DataStore)은 이 지도가 아니라 각 저장소 자체의 계약을 따른다. AppSearch는 그 데이터를 검색 가능하게 만드는 별도 색인 계층이다.

### 노트 목록

- [AppSearch는 클라우드 검색 엔진이 아니라 온디바이스 검색 색인이다](./appsearch-is-an-on-device-search-index-not-a-cloud-search-engine.md)
- [Document 스키마 변경은 명시적 마이그레이션이 없으면 호환되지 않는 데이터를 삭제한다](./document-schema-changes-require-explicit-migration-or-forceoverride-deletes-data.md)

검증일: 2026-08-05. [AppSearch overview](https://developer.android.com/guide/topics/search/appsearch), [SetSchemaResponse.MigrationFailure](https://developer.android.com/reference/androidx/appsearch/app/SetSchemaResponse.MigrationFailure)를 기준으로 확인했다.
