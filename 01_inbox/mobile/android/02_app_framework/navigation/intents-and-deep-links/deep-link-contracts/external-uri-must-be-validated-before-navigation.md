---
title: external-uri-must-be-validated-before-navigation
tags: [android, android/deep-links, android/navigation]
aliases: ["외부 URI는 navigation 전에 allowlist와 canonicalization을 거쳐야 한다"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 외부 URI 는 navigation 전에 allowlist 와 canonicalization 을 거쳐야 한다

Deep Link 나 App Link 로 들어온 URI 는 곧바로 내부 route 로 쓰지 않는다. scheme, host, path, query parameter 를 allowlist 로 검증하고, percent encoding, trailing slash, case, path traversal 처럼 route matching 을 흔드는 표현을 canonicalize 한다.

App Link verification 은 도메인 소유 관계를 확인하지만 앱 내부 권한이나 business rule 을 대신 검증하지 않는다. URI 를 `NavKey` 로 바꿀 때는 raw string 을 그대로 넘기지 말고 typed route argument 로 변환한다.

### 판단 기준

- 지원하는 scheme, host, path prefix 를 명시적으로 allowlist 로 둔다.
- query parameter 는 type, range, required/optional 여부를 검증한다.
- 인증이 필요한 destination 은 바로 push 하지 않고 pending destination 과 auth stack 을 분리한다.
- 잘못된 URI 는 crash 가 아니라 fallback destination 또는 명시적 오류로 수렴시킨다.

### 예시

`https://example.com/orders/../admin` 처럼 path traversal 이 섞인 URI 나 `%2e%2e%2f` 로 encoding 된 변형은 canonicalize 하지 않으면 allowlist 검사를 우회할 수 있다.

```kotlin
fun Uri.toOrderRouteOrNull(): NavKey? {
    if (scheme != "https" || host != "example.com") return null
    val segments = path.orEmpty().split("/").filter { it.isNotEmpty() }
    if (segments.firstOrNull() != "orders" || segments.contains("..")) return null
    val id = segments.getOrNull(1)?.toIntOrNull() ?: return null
    return OrderDetailRoute(id)
}
```

raw string 을 그대로 `backStack.add(RawUriRoute(uri.toString()))` 로 넣는 대신, 위처럼 실패 가능한 typed 변환을 거쳐야 잘못된 URI 가 앱 내부 임의 상태로 이어지지 않는다.

관련 노트: [Android 딥 링크는 외부 URI 계약이다](./deep-link-is-external-uri-contract.md), [Android App Link는 검증된 HTTPS 딥 링크다](./app-link-is-verified-https-deep-link.md), [Navigation 3 deep link는 URI를 NavKey로 변환한다](../../navigation3/navigation3-contracts/navigation3-deep-link-converts-uri-to-navkey.md)
