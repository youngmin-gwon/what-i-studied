# Intent와 Manifest 계약

Intent와 Manifest는 OS가 앱 컴포넌트를 발견하고 실행하는 공개 계약이다. 앱 내부 화면 이동과 구분해서 읽어야 한다.

## 정본 노트

- [Intent는 컴포넌트 실행을 설명하는 메시지다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-describes-component-action-request.md)
- [명시적 Intent와 암시적 Intent는 공개 범위로 선택한다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/explicit-intent-targets-known-component-implicit-intent-declares-capability.md)
- [intent-filter는 컴포넌트의 수신 계약이다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-filter-is-component-receiving-contract.md)
- [action, category, data 매칭은 서로 다른 조건이다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-filter-matches-action-category-data.md)
- [AndroidManifest는 OS가 발견할 컴포넌트와 진입점을 선언한다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/android-manifest-declares-os-visible-components-and-entry-points.md)
- [exported 속성은 외부 컴포넌트 접근 경계를 정한다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/exported-attribute-defines-external-component-boundary.md)
- [package visibility는 앱이 조회할 수 있는 외부 앱 범위를 제한한다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/package-visibility-limits-which-apps-can-be-queried.md)
- [PendingIntent는 미래 실행 권한을 위임하는 토큰이다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/pendingintent-is-delegated-future-intent-token.md)

상위 지도: [Android Navigation 진입 계약](01_inbox/mobile/android/02_app_framework/navigation/navigation-contracts/navigation-contracts.md)
