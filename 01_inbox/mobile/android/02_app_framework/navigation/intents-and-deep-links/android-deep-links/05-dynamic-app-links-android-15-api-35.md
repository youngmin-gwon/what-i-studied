# Dynamic App Links (Android 15 / API 35+)

Android 15 부터는 `assetlinks.json` 파일을 통해 **앱 업데이트 없이** 딥링크 라우팅 규칙을 동적으로 구성할 수 있습니다. 시스템은 약 일주일 단위로 이 파일을 재검층(Periodic Re-verification)하여 규칙을 갱신합니다.

##### 주요 특징
- **Exclusions (제외)**: 특정 경로(예: `/private/*`)가 앱에서 열리지 않도록 서버에서 즉시 차단 가능.
- **Query & Fragment Matching**: 특정 쿼리 파라미터가 포함된 경우에만 앱을 열도록 세분화된 필터링 제공.
- **Refinement Only**: 동적 규칙은 **이미 Manifest 에 선언된 호스트**에 대해서만 적용 가능하며, 새로운 호스트를 승인할 수는 없습니다.

##### `assetlinks.json` 예시
```json
[{
  "relation": ["delegate_permission/common.handle_all_urls"],
  "target": {
    "namespace": "android_app",
    "package_name": "com.example.app",
    "sha256_cert_fingerprints": ["..."]
  },
  "dynamic_app_deep_link_components": [
    {
      "intent_filter": {
        "action": "android.intent.action.VIEW",
        "category": ["android.intent.category.BROWSABLE", "android.intent.category.DEFAULT"],
        "data": [
          { "scheme": "https", "host": "www.example.com", "pathPrefix": "/product" },
          { "pathPrefix": "/special-offer", "query": "campaign=summer2025" }
        ]
      },
      "exclusion_patterns": [
        { "pathPrefix": "/product/test" }
      ]
    }
  ]
}]
```
