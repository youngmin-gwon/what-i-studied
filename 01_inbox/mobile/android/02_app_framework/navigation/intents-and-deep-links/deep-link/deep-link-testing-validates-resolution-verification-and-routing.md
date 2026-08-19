---
title: deep-link-testing-validates-resolution-verification-and-routing
tags: [android, android/navigation, android/deep-links, testing]
aliases: ["Deep link 테스트는 resolution, verification, routing을 함께 검증한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Deep link 테스트는 resolution, verification, routing 을 함께 검증한다

상위 문서: [Deep Link 계약](deep-link.md)

관련 계약: [App Link는 검증된 https deep link다](app-link-is-verified-https-deep-link.md)

---

### 개념과 필요성 (What & Why)

1. **개념 (What)**:
   - 딥링크 테스트는 단순히 UI가 열리는지 확인하는 것에 그치지 않고, (1) OS의 Intent Resolution, (2) Domain Verification(`assetlinks.json`), (3) 앱 내부 `NavKey` 라우팅 파이프라인의 3 단계를 통합적으로 검증하는 과정이다.
2. **필요성 (Why)**:
   - **단계별 실패 원인 격리**: 딥링크가 작동하지 않을 때 원인이 웹 서버의 `assetlinks.json` 서명 오류인지, Manifest의 `<intent-filter>` 미등록인지, 아니면 내부 URI 파서의 정규식 오류인지를 정확히 식별하기 위해 체계적인 검증 툴킷이 필요하다.

---

### 3단계 검증 CLI 및 테스트 기법 (How)

1. **OS Intent Resolution 검증 (ADB Command)**:
   ```bash
   adb shell am start -W -a android.intent.action.VIEW -d "https://example.com/product/123" com.example.myapp
   ```
2. **Domain Verification 상태 검증 (PM CLI)**:
   ```bash
   # 도메인 검증 상태 확인 (STATE_VERIFIED 여부 체크)
   adb shell pm get-app-links com.example.myapp
   
   # 재검증 강제 실행
   adb shell pm verify-app-links --re-verify com.example.myapp
   ```
3. **내부 URI-to-NavKey 단위 테스트 (JUnit)**:
   ```kotlin
   @Test
   fun verifyProductDeepLinkParsing() {
       val uri = Uri.parse("https://example.com/product/123")
       val key = DeepLinkParser.parse(uri)
       assertEquals(ProductDetailKey(id = "123"), key)
   }
   ```

---

### 관련 상위 및 연관 노트

- 상위 계약: [Deep Link 계약](deep-link.md)
- 연관 계약: [App Link는 검증된 https deep link다](app-link-is-verified-https-deep-link.md)
