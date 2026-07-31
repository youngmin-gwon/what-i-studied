# AndroidManifest는 OS가 발견할 컴포넌트와 권한 경계를 선언한다

AndroidManifest는 OS와 build tool이 앱의 component, permission, feature, intent-filter, metadata를 발견하는 선언 파일이다. Activity, Service, Receiver, Provider는 런타임에 아무 클래스나 스캔되어 노출되는 것이 아니라 Manifest와 관련 metadata를 통해 OS-visible surface가 된다.

Manifest는 navigation 문서만의 주제가 아니다. 외부 앱이 호출할 수 있는 entry point, 필요한 permission, package visibility, provider authority, foreground service type 같은 OS 계약이 여기서 시작된다.

다만 deep link나 intent-filter matching의 세부 규칙은 navigation/intent 정본이 담당한다. 이 노트는 app component 관점에서 Manifest가 왜 아키텍처 경계인지 설명한다.

관련 노트: [Manifest/entry point 정본](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/android-manifest-declares-os-visible-components-and-entry-points.md), [intent/manifest 정본](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md), [exported/permission 경계](01_inbox/mobile/android/02_app_framework/architecture/app-components/app-component-contracts/exported-and-permission-boundaries-decide-external-component-access.md).

공식 문서: [App Manifest overview](https://developer.android.com/guide/topics/manifest/manifest-intro)
