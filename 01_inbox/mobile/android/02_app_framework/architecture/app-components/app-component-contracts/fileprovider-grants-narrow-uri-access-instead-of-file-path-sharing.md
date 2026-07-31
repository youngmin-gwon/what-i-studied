---
title: "FileProvider는 파일 경로 대신 제한된 content URI 접근권을 준다"
tags: [android, android/architecture, android/app-components]
aliases: ["FileProvider는 파일 경로 대신 제한된 content URI 접근권을 준다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# FileProvider는 파일 경로 대신 제한된 content URI 접근권을 준다

FileProvider는 파일을 직접 path로 넘기는 대신 `content://` URI와 임시 URI permission을 통해 공유하게 해 주는 특수 ContentProvider다. 받는 쪽은 앱 내부 파일 경로를 알 필요가 없고, 허용된 path와 grant flag 범위 안에서만 접근한다.

FileProvider는 일반 CRUD provider나 storage architecture가 아니다. 어떤 파일을 공유할지 path allow-list를 정하고, `FLAG_GRANT_READ_URI_PERMISSION` 같은 권한을 Intent에 실어 일시적으로 접근을 위임하는 보안 경계다.

앱 데이터의 소유와 보존 정책은 storage 정본에서 결정하고, 외부 공유가 필요한 파일에 대해서만 FileProvider를 연결한다.

관련 노트: [file access 정본](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/file-access-contracts.md), [ContentProvider 정본](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/contentprovider-publishes-uri-addressed-data-with-permission-boundary.md), [Android 권한 계약](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/permission-contracts.md).

공식 문서: [FileProvider reference](https://developer.android.com/reference/androidx/core/content/FileProvider)
