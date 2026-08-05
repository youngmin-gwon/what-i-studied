---
title: fileprovider-grants-narrow-uri-access-instead-of-file-path-sharing
tags: [android, android/app-components, android/architecture]
aliases: ["FileProvider는 파일 경로 대신 제한된 content URI 접근권을 준다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## FileProvider 는 파일 경로 대신 제한된 content URI 접근권을 준다

상위 문서: [App Component Contracts](./app-component-contracts.md)
FileProvider 는 파일을 직접 path 로 넘기는 대신 `content://` URI 와 임시 URI permission 을 통해 공유하게 해 주는 특수 ContentProvider 다. 받는 쪽은 앱 내부 파일 경로를 알 필요가 없고, 허용된 path 와 grant flag 범위 안에서만 접근한다.

FileProvider 는 일반 CRUD provider 나 storage architecture 가 아니다. 어떤 파일을 공유할지 path allow-list 를 정하고, `FLAG_GRANT_READ_URI_PERMISSION` 같은 권한을 Intent 에 실어 일시적으로 접근을 위임하는 보안 경계다.

앱 데이터의 소유와 보존 정책은 storage 정본에서 결정하고, 외부 공유가 필요한 파일에 대해서만 FileProvider 를 연결한다.

`file://` URI 를 FileProvider 없이 그대로 다른 앱에 노출하면(targetSdkVersion 24 이상) `FileUriExposedException` 이 발생한다. 이 예외 자체가 "raw file 경로를 외부에 넘겼다"는 관찰 가능한 신호다.

관련 노트: [file access 정본](../../../data/storage/file-access-contracts/file-access-contracts.md), [ContentProvider 정본](./contentprovider-publishes-uri-addressed-data-with-permission-boundary.md), [Android 권한 계약](../../../../05_security_privacy/permissions-and-sandbox/permission-contracts/permission-contracts.md).

공식 문서: [FileProvider reference](https://developer.android.com/reference/androidx/core/content/FileProvider)
