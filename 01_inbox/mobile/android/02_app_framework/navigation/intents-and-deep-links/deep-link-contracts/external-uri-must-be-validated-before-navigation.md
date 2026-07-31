# 외부 URI는 navigation 전에 allowlist와 canonicalization을 거쳐야 한다

Deep Link나 App Link로 들어온 URI는 곧바로 내부 route로 쓰지 않는다. scheme, host, path, query parameter를 allowlist로 검증하고, percent encoding, trailing slash, case, path traversal처럼 route matching을 흔드는 표현을 canonicalize한다.

App Link verification은 도메인 소유 관계를 확인하지만 앱 내부 권한이나 business rule을 대신 검증하지 않는다. URI를 `NavKey`로 바꿀 때는 raw string을 그대로 넘기지 말고 typed route argument로 변환한다.

관련 노트: [Deep Link](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-is-external-uri-contract.md), [App Link](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/app-link-is-verified-https-deep-link.md), [Navigation 3 deep link](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navigation3-deep-link-converts-uri-to-navkey.md), [authenticated deep link](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/authenticated-deep-links-require-pending-destination-and-back-stack.md).
