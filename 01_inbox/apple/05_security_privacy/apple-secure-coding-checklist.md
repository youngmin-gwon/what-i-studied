---
title: apple-secure-coding-checklist
tags: [apple, security, checklist, best-practice]
aliases: []
date modified: 2025-12-18 01:20:00 +09:00
date created: 2025-12-16 16:08:41 +09:00
---

## Secure Coding Checklist

보안은 "기능"이 아니라 "습관"입니다.
앱을 배포하기 전에 이 체크리스트를 훑어보는 것만으로도 치명적인 취약점의 90%를 막을 수 있습니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **Trust**: 한 번이라도 개인정보가 털린 앱은 사용자가 다시 찾지 않습니다.
- **Cost**: 출시 후 보안 패치를 하는 비용은 개발 단계에서 수정하는 비용의 100배입니다(긴급 배포, 사용자 공지, 법적 대응 등).

---

### 📋 입력과 출력 (Input & Output)

- [ ] **SQL Injection 방지**: SQLite 사용 시 문자열 합치기(`"SELECT * FROM users WHERE name = '" + name + "'`)를 절대 쓰지 마세요. 반드시 `?` 바인딩 파라미터를 사용하세요.
- [ ] **Log Sanitization**: `print(user)`를 남발하지 마세요. 사용자의 비밀번호, 토큰, 이메일이 Xcode 콘솔이나 디바이스 로그에 남으면 안 됩니다. `OSLog`의 `privacy: .private` 옵션을 쓰세요.
- [ ] **Clipboard**: 비밀번호나 인증 번호를 복사했을 때, `UIPasteboard`에 영구히 남지 않도록 `expireDate`를 설정하거나 사용 후 지우세요.

---

### 🔐 데이터 저장 (Data Storage)

- [ ] **Keychain**: `UserDefaults`에 비밀번호, API 토큰, 개인정보를 저장하지 않았는지 확인하세요. 암호화가 필요한 모든 것은 키체인으로 가야 합니다.
- [ ] **File Protection**: 중요한 파일을 저장할 때 `.completeFileProtection` 옵션을 켰나요? 기기가 잠기면 파일도 읽을 수 없어야 합니다.
- [ ] **Snapshot Caching**: 앱이 백그라운드로 갈 때 민감한 화면(계좌번호, 채팅)을 가리기 위해 `UIVisualEffectView`를 덮었나요? 스위처 스크린샷에 정보가 찍힐 수 있습니다.

---

### 🌐 네트워크 (Network)

- [ ] **ATS (App Transport Security)**: `Info.plist`에 `NSAllowsArbitraryLoads = YES`가 켜져 있지 않은지 확인하세요. 정말 필요한 예외 도메인만 등록해야 합니다.
- [ ] **Certificate Pinning**: 금융/결제 앱이라면 서버 인증서 피닝을 적용했나요? (Alamofire 등의 라이브러리 활용)
- [ ] **API Keys**: AWS Access Key나 Firebase Key가 소스코드에 하드코딩되어 있지 않나요? 환경 변수나 난독화, 혹은 서버 사이드 프록시를 사용하세요.

---

### 🆔 인증과 권한 (Auth & Authz)

- [ ] **Biometrics Fallback**: FaceID가 실패하거나 잠겼을 때, 비밀번호 입력으로 넘어가는 흐름(Fallback)이 구현되어 있나요?
- [ ] **Least Privilege**: 꼭 필요한 권한만 요청했나요? 위치 권한을 "항상 허용"으로 요청하면 거부율이 높습니다. "앱 사용 중에만"으로 충분한지 검토하세요.

---

### 🛠️ 배포와 설정 (Build & Distribute)

- [ ] **Debug Flags**: 릴리스 빌드에서 디버그용 기능(서버 주소 변경, 로그 보기)이 모두 꺼졌는지 `#if DEBUG` 블록을 확인하세요.
- [ ] **Strip Symbols**: 앱 바이너리에서 심볼이 제거(Strip)되었는지 Build Settings를 확인하세요. 심볼이 있으면 해커가 코드를 분석하기 너무 쉽습니다.

### 더 보기
- [apple-security-models](../../../../apple-security-models.md) - 보안 모델 개요
- [apple-sandbox-and-security](apple-sandbox-and-security.md) - 샌드박스와 권한 상세
