---
title: contentprovider-publishes-uri-addressed-data-with-permission-boundary
tags: [android, android/app-components, android/architecture]
aliases: ["ContentProvider는 URI 데이터와 권한 경계를 게시한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## ContentProvider는 URI 데이터와 권한 경계를 게시한다

**`ContentProvider` 는 앱이 가진 구조화된 데이터(SQLite DB, Room DB, 또는 파일)를 고유한 `Content URI` (예: `content://com.example.provider/items`) 표준 인터페이스 형태로 다른 프로세스에 정밀한 권한 통제(Read/Write Permission Boundary) 위에서 안전하게 게시(Publish)하는 컴포넌트**다.

---

### 1. 개념 및 핵심 구조 (What)

- **Content URI 인터페이스 표준**:
  외부 앱은 데이터베이스의 물리적 파일 경로나 구현 방식을 알 필요 없이, `ContentResolver` 를 통해 CRUD(`query`, `insert`, `update`, `delete`)를 표준 SQL 유사 인터페이스로 수행한다.
- **IPC 데이터 래핑 및 파셀 스트림**:
  쿼리 결과는 `Cursor` 파셀 객체로 래핑되어 프로세스 경계를 넘어 전송된다.

---

### 2. 관련 문서 및 참조

- 상위 문서: [App Component Contracts](./app-component-contracts.md)
- 관련 계약 문서:
  - [FileProvider는 파일 경로 공유 대신 좁은 URI 접근을 허용한다](./fileprovider-grants-narrow-uri-access-instead-of-file-path-sharing.md)
- 공식 가이드: [Content Providers](https://developer.android.com/guide/topics/providers/content-providers)

검증일: 2026-08-05. ContentProvider URI 데이터 공유 구조 확인 완료.
