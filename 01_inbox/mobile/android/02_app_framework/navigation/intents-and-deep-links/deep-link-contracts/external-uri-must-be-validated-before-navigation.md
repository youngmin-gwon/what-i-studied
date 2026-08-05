---
title: external-uri-must-be-validated-before-navigation
tags: [android, android/navigation, android/deep-links, security]
aliases: ["External URI는 navigation 전에 검증되어야 한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## External URI 는 navigation 전에 검증되어야 한다

상위 문서: [Deep Link 계약](deep-link-contracts.md)

관련 계약: [Deep link는 외부 URI 계약이다](deep-link-is-external-uri-contract.md)

---

### 개념과 필요성 (What & Why)

1. **개념 (What)**:
   - 외부 딥링크 Intent를 통해 수신된 `Uri` 객체는 탐색 백스택(`NavBackStack`)에 추가되거나 라우터로 넘어가기 직전에 **형식 검증, 인자 범위 검증, 도메인 세이프가드 검증(Sanitization & Validation)**을 반드시 거쳐야 한다는 원칙이다.
2. **필요성 (Why)**:
   - **Open Redirect 및 자바스크립트 인젝션 차단**: 파싱되지 않은 외부 URI 쿼리(예: `?redirect_url=http://malicious.com`)를 인앱 브라우저나 WebView, 내부 라우터에 그대로 넘기면 피싱 사이트로 유도되거나 내부 컴포넌트가 오작동할 위험이 발생한다.

---

### 검증 체크리스트 및 코드

- **Host/Scheme 허용 목록 검증**: 허용된 HTTPS 도메인만 통과.
- **파라미터 정규식 필터링**: ID 파라미터가 숫자인지 정규식 검증.
- **Null / 예외 처리**: 파싱 실패 시 앱 덤프(Crash) 대신 안전한 렌더링 폴백 적용.

```kotlin
fun safeParseProductId(uri: Uri): String? {
    val rawId = uri.getQueryParameter("id") ?: return null
    return if (rawId.matches(Regex("^[0-9]{1,10}$"))) rawId else null
}
```

---

### 관련 상위 및 연관 노트

- 상위 계약: [Deep Link 계약](deep-link-contracts.md)
- 연관 계약: [Deep link는 외부 URI 계약이다](deep-link-is-external-uri-contract.md)
