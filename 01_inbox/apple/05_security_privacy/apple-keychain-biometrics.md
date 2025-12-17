---
title: apple-keychain-biometrics
tags: [apple, keychain, security, biometrics, sep, cryptography, cryptokit]
aliases: []
date modified: 2025-12-18 01:00:00 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Keychain, Biometrics, and Cryptography

비밀번호, 액세스 토큰, 암호화 키.
이 세 가지는 앱 개발자에게 가장 골치 아픈 존재입니다.
**UserDefaults**에 저장하면 털리고, 매번 입력받자니 사용자가 떠납니다. 이 딜레마를 해결하는 것이 KeyChain과 FaceID(SEP)입니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **UserDefaults는 공공재**: 탈옥된 기기에서 `UserDefaults.standard`는 XML 파일 하나일 뿐입니다. 누구나 열어서 'accessToken'을 복사해갈 수 있습니다. 절대 비밀 정보를 넣지 마세요.
- **삭제해도 남는다**: 앱을 지웠다 다시 깔았는데 로그인이 유지되는 경험 해보셨나요? Keychain은 앱 샌드박스 밖에 저장되므로 앱 삭제 후에도 살아남습니다. (사용자 경험 개선 포인트)
- **FaceID의 오해**: "내 얼굴 사진을 앱이 가져가나요?" 절대 아닙니다. 앱은 하드웨어(SEP)에게 "이 사람 맞아요?"라고 묻기만 할 수 있습니다.

---

### 🔐 Keychain Internals

Keychain은 단순한 `Dictionary` 저장이 아닙니다. OS 레벨에서 관리되는 암호화된 SQLite 데이터베이스입니다.

#### 1. 아키텍처 (Architecture)
- **securityd**: 키체인 접근을 관리하는 시스템 데몬입니다. 앱은 이 데몬하고만 대화할 수 있습니다.
- **SQLite Backing**: 실제 데이터는 `/private/var/Keychains` 경로의 DB에 저장되지만, 파일 시스템 레벨 암호화와 별개로, 키체인 항목별로 개별 암호화가 적용됩니다.

#### 2. Access Control Flags (언제 접근 가능한가?)
가장 중요한 설정입니다. "언제 이 데이터를 복호화할 수 있는가?"를 정의합니다.

- **kSecAttrAccessibleWhenUnlocked**: (권장) 기기가 잠금 해제된 상태에서만 접근 가능. 화면이 꺼지고 잠기면 키도 메모리에서 사라집니다(Wiping).
- **kSecAttrAccessibleAfterFirstUnlock**: (백그라운드용) 재부팅 후 한 번이라도 비번을 쳤다면, 그 뒤로는 화면이 잠겨도 접근 가능합니다. 백그라운드 네트워크 작업을 위해 토큰을 꺼내야 할 때 씁니다.

---

### 🛡️ Secure Enclave Processor (SEP) & Cryptography

앱 프로세서(AP) 옆에 붙어있는 **별도의 보안 칩**입니다.
메인 OS 커널이 해킹당해도, 이 칩 안에 있는 데이터는 안전합니다.

#### 1. CryptoKit & SEP
iOS 13부터는 `CryptoKit`을 통해 하드웨어 키를 쉽게 다룰 수 있습니다.

- **Key Generation**: RSA/ECC 키 쌍을 SEP **내부**에서 생성할 수 있습니다.
- **Extraction Impossible**: 생성된 Private Key는 하드웨어적으로 **절대 밖으로 나올 수 없습니다.**

```swift
import CryptoKit

// SEP에서 P256 키 쌍 생성 (Private Key는 밖으로 못 나옴)
let privateKey = try SecureEnclave.P256.Signing.PrivateKey()

// 서명 (Signing happens inside SEP)
let signature = try privateKey.signature(for: data)

// 공개키는 밖으로 내보낼 수 있음
let publicKeyData = privateKey.publicKey.compactRepresentation
```

---

### 🗄️ Data Protection Class (File System)

Keychain뿐만 아니라 일반 파일(`Documents` 폴더 등)에도 암호화 등급을 걸 수 있습니다.

- **Complete Protection (`NSFileProtectionComplete`)**: 기기가 잠기면 파일도 잠깁니다. 백그라운드에서 파일 읽기가 불가능합니다.
- **Complete Unless Open**: 파일이 열린 상태에서는 잠겨도 계속 읽을 수 있습니다. (다운로드 중 화면 꺼짐 등)

---

### 👆 Biometrics (Face ID / Touch ID)

생체 인증은 `LocalAuthentication` 프레임워크를 사용합니다.

#### 1. 정책 (Policy)
- `.deviceOwnerAuthenticationWithBiometrics`: 오직 생체 인증만 허용. 실패하면 끝.
- `.deviceOwnerAuthentication`: 생체 인증 5회 실패 시 **기기 비밀번호(Passcode)** 입력 화면으로 넘어감. (더 유연함)

#### 2. Access Control과 결합
FaceID를 통과해야만 키체인 아이템을 꺼낼 수 있도록 시스템 레벨에서 묶을 수 있습니다. 앱 로직으로 구현하는 것보다 훨씬 안전합니다.

```swift
let access = SecAccessControlCreateWithFlags(
    nil,
    kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly,
    .userPresence, // ⭐️ 유저 존재(FaceID/비번)가 확인되어야만 읽기 허용
    nil
)
// 이 access 객체를 Keychain 저장 시 함께 넘김
```

### 더 보기
- [[apple-sandbox-and-security]] - 앱 샌드박스 구조
- [[apple-ios-system]] - iOS 부팅 과정과 보안 체인
