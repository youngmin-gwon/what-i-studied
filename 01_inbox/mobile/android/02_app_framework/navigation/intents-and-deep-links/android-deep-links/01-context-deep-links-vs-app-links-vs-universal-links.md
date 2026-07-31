# 💡 Context: Deep Links vs App Links vs Universal Links

안드로이드의 딥링크 시스템은 보안성과 사용자 경험을 개선하기 위해 진화해왔습니다. 특히 **App Links**는 iOS 의 **Universal Links**와 동일하게 웹 도메인 인증을 기반으로 동작하여 보안 위협을 방지합니다.

>[!NOTE] **상호 참조**
>iOS 의 유사 기능 및 구현 방식은 [apple-deep-links](01_inbox/mobile/apple/04_system_services/apple-deep-links.md) 를 참고하세요.

---
> - **iOS**: Associated Domains Entitlement + `apple-app-site-association` (AASA) 파일
> - **Android**: Intent Filter + `assetlinks.json` 파일
>두 플랫폼 모두 **HTTPS 도메인 소유 검증**을 통해 앱과 웹사이트의 신뢰 관계를 증명한다.
>iOS 의 URL Scheme (`myapp://`) 은 Android 의 Custom Scheme Deep Link 와 동일한 레거시 패턴이며, 두 플랫폼 모두 검증된 HTTPS 기반 방식을 권장한다.
