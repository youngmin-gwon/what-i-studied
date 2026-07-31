# Intent extras와 URI 인자는 명시적인 타입과 신뢰 경계가 필요하다

외부 앱이나 system에서 들어온 Intent는 내부 함수 호출과 같은 신뢰 수준이 아니다. `extras`, `data` URI, MIME type, `ClipData`, URI permission grant flag는 서로 다른 입력 경계이며 각각 타입과 출처를 확인해야 한다.

컴포넌트를 `exported=true`로 열거나 implicit intent를 받는다면 입력 검증은 선택 사항이 아니다. Parcelable/classloader 문제, oversized extras, 예상하지 않은 URI authority, 권한 없는 content URI 접근을 별도로 방어한다.

관련 노트: [exported boundary](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/exported-attribute-defines-external-component-boundary.md), [PendingIntent](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/pendingintent-is-delegated-future-intent-token.md), [URI validation](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/external-uri-must-be-validated-before-navigation.md).
