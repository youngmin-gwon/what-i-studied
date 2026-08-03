---
title: contentprovider-publishes-uri-addressed-data-with-permission-boundary
tags: [android, android/app-components, android/architecture]
aliases: ["ContentProvider는 URI와 권한을 가진 데이터 공유 API다"]
date modified: 2026-08-03 17:27:01 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## ContentProvider 는 URI 와 권한을 가진 데이터 공유 API 다

ContentProvider 는 `content://` URI 를 통해 데이터를 노출하고 `ContentResolver` 로 접근되는 앱 컴포넌트다. 핵심은 SQLite 가 아니라 provider authority, URI shape, MIME type, CRUD method, permission 경계로 구성된 외부 또는 cross-process 데이터 계약이다.

현대 앱에서 내부 데이터 저장은 Room, DataStore, repository 로 충분한 경우가 많다. 그러나 다른 앱이나 시스템 surface 가 일정한 URI 계약으로 데이터를 읽고 써야 한다면 ContentProvider 가 여전히 맞는 선택이다.

Provider 는 내부 abstraction 으로도 쓸 수 있지만, 단지 repository 를 만들기 귀찮아서 쓰는 계층은 아니다. 프로세스 경계와 permission model 이 필요한지부터 판단한다.

관련 노트: [persistence 정본](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md), [FileProvider 정본](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/fileprovider-grants-narrow-uri-access-instead-of-file-path-sharing.md), [Android 권한 계약](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/permission-contracts.md).

공식 문서: [Content providers](https://developer.android.com/guide/topics/providers/content-providers)
