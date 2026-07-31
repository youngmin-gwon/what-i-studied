# ContentProvider는 URI와 권한을 가진 데이터 공유 API다

ContentProvider는 `content://` URI를 통해 데이터를 노출하고 `ContentResolver`로 접근되는 앱 컴포넌트다. 핵심은 SQLite가 아니라 provider authority, URI shape, MIME type, CRUD method, permission 경계로 구성된 외부 또는 cross-process 데이터 계약이다.

현대 앱에서 내부 데이터 저장은 Room, DataStore, repository로 충분한 경우가 많다. 그러나 다른 앱이나 시스템 surface가 일정한 URI 계약으로 데이터를 읽고 써야 한다면 ContentProvider가 여전히 맞는 선택이다.

Provider는 내부 abstraction으로도 쓸 수 있지만, 단지 repository를 만들기 귀찮아서 쓰는 계층은 아니다. 프로세스 경계와 permission model이 필요한지부터 판단한다.

관련 정본: [persistence 정본](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md), [FileProvider 정본](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/fileprovider-grants-narrow-uri-access-instead-of-file-path-sharing.md), [permissions 정본](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/android-security-permissions.md).

공식 문서: [Content providers](https://developer.android.com/guide/topics/providers/content-providers)
