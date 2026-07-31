# Android history는 기능 목록이 아니라 platform contract 변화 지도다

Android version history는 새 기능 암기표가 아니라 어떤 contract가 바뀌었는지 보는 timeline이다. runtime, permission, storage, distribution, update, UI, form factor, security boundary가 언제 바뀌었는지가 중요하다.

예를 들어 Android 6의 runtime permission, Android 8의 Treble/background limit, Android 10의 scoped storage/Mainline, Android 12의 Material You와 ART module update, Android 13 이후 notification/media 권한 분리는 앱 설계 기준을 바꿨다.

따라서 오래된 version별 세부 설명은 정본으로 유지하지 않고, 주요 contract 변화와 관련 정본 링크로 압축한다.

관련 노트: [permissions](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/android-security-permissions.md), [file/storage](01_inbox/mobile/android/02_app_framework/data/storage/file-access-contracts/file-access-contracts.md), [platform modularity](01_inbox/mobile/android/01_system_internals/platform-modularity/android-platform-modularity.md), [Compose runtime](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md).
