---
title: apple-build-and-distribution
tags: [apple, build, distribution, codesign, xcode, ci-cd]
aliases: []
date modified: 2025-12-17 22:20:00 +09:00
date created: 2025-12-16 16:10:06 +09:00
---

## Build, Signing & Distribution Deep Dive

"인증서 만료됨", "Profile doesn't match the entitlements".
iOS 개발자를 가장 괴롭히는 에러들입니다.
하지만 이 복잡한 서명(Code Signing) 과정이야말로 Apple 생태계의 **신뢰(Trust)**를 지탱하는 기둥입니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **배포 사고 예방**: 출시 당일에 인증서가 만료되거나, 개발용(Development) 인증서로 빌드해서 스토어 업로드가 막히는 일을 막아야 합니다.
- **CI/CD 구축**: Jenkins나 GitHub Actions에서 빌드를 돌리려면, Xcode가 자동으로 해주던 서명 과정을 수동으로 설정(`fastlane match` 등)해야 합니다.
- **해킹 방지**: 내 앱을 누군가 풀어서 악성코드를 심고 재배포하는 것(Repackaging)을 막는 유일한 장치입니다.

---

### ✍️ Code Signing Chain of Trust (신뢰 사슬)

서명은 3가지 요소의 결합입니다. 하나라도 틀리면 빌드가 안 됩니다.

#### 1. Certificate (Who am I?)
"내가 개발자 홍길동이다"라는 신분증입니다.
- **Private Key (.p12)**: 내 맥북 키체인에만 있는 비밀키. 절대 유출되면 안 됩니다.
- **Public Key (.cer)**: Apple에게 보내서 서명받은 공개키.

#### 2. App ID (Who is this app?)
"이 앱은 com.example.myapp이다"라는 앱의 주민등록번호입니다.
- **Entitlements**: 이 앱이 iCloud, Push 등을 쓸 수 있는지 명시된 "특수 면허"가 포함됩니다.

#### 3. Provisioning Profile (Permission to Run)
"홍길동(Cert)이 만든 이 앱(App ID)을 이 기기(Device ID)에서 실행해도 좋다"고 Apple이 도장을 찍어준 문서입니다.
- **Development Profile**: 등록된 테스트 기기(UDID) 목록이 들어있습니다. 여기에 없는 폰에서는 앱이 안 켜집니다.
- **Distribution Profile**: App Store 제출용. 기기 목록이 없고, 대신 Apple의 배포용 인증이 들어갑니다.

---

### 🏭 Build Process (Under the Hood)

Xcode에서 `Build` 버튼을 누르면 일어나는 일들입니다.

1. **Pre-processing**: Info.plist 가공, Asset Catalog 컴파일.
2. **Compiling**: `swiftc`(Swift)와 `clang`(Obj-C)이 소스 코드를 기계어(`Mach-O`)로 변환합니다.
3. **Linking**: `ld` 링커가 컴파일된 파일들과 시스템 프레임워크를 합쳐서 하나의 실행 파일을 만듭니다.
4. **Signing**: `codesign` 도구가 실행 파일에 디지털 서명을 입힙니다. 이때 Entitlement도 바이너리에 박제(Embed)됩니다.
5. **Packaging**: .app 폴더를 만들고 압축(.ipa)합니다.

---

### 🚀 Distribution & Validation

#### 1. Notarization (macOS 필수)
macOS 앱을 웹에서 배포하려면 **공증(Notarization)**을 받아야 합니다.
- 개발자가 앱을 Apple 서버에 보내면, Apple이 악성코드 검사를 하고 "깨끗함" 티켓을 발급해줍니다.
- 이 과정을 거치지 않으면 "확인되지 않은 개발자가 만듦" 경고가 뜨고 실행이 막힙니다.

#### 2. Bitcode (Deprecated)
과거에는 중간 언어(Bitcode)를 업로드해서 Apple이 재컴파일하게 했으나, Xcode 14부터는 기본적으로 꺼져 있습니다. 이제는 완성된 바이너리를 올립니다.

#### 3. dSYM (Debug Symbols)
앱이 크래시 났을 때 "메모리 주소 0x1234"가 아니라 "ViewController.swift 50번째 줄"이라고 알려면 **dSYM 파일**이 필요합니다.
- App Store Connect에 업로드할 때 체크하거나, Firebase Crashlytics에 별도로 올려야 합니다.

### 더 보기
- [[apple-sandbox-and-security]] - 서명이 완료된 앱이 실행될 때 일어나는 일
- [[apple-history-and-evolution]] - PowerPC에서 Apple Silicon까지의 아키텍처 변화
