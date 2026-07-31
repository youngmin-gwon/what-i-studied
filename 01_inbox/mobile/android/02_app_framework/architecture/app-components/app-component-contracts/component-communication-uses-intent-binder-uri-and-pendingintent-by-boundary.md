# 컴포넌트 통신은 Intent, Binder, URI, PendingIntent 경계로 나눈다

Android component communication은 하나의 event bus가 아니다. Activity, Service, Receiver 시작은 Intent가 맡고, bound service 호출은 Binder가 맡으며, provider 데이터 접근은 URI와 `ContentResolver`가 맡고, 미래의 system-mediated 실행 위임은 PendingIntent가 맡는다.

통신 수단은 수명과 신뢰 경계로 고른다. 같은 앱 화면 상태 변경은 ViewModel/Flow로 충분하고, 앱 외부 entry point는 Intent/Manifest 계약이 필요하며, cross-process method call은 Binder/AIDL 부담을 받아들여야 한다.

특히 Service 시작에는 explicit Intent를 선호해야 한다. implicit Intent는 resolution과 hijacking 위험이 있고, 공개 component와 권한 경계를 명확히 하지 못하면 보안 문제가 된다.

관련 노트: [intent/manifest 정본](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md), [Binder/IPC 정본](01_inbox/mobile/android/01_system_internals/ipc-and-process/android-binder-and-ipc.md), [PendingIntent 정본](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/pendingintent-is-delegated-future-intent-token.md).

공식 문서: [Application fundamentals](https://developer.android.com/guide/components/fundamentals)
