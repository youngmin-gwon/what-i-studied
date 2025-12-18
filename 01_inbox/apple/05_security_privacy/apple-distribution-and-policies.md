---
title: apple-distribution-and-policies
tags: [apple, appstore, policy, rejection, iap, gdpr]
aliases: []
date modified: 2025-12-17 22:30:00 +09:00
date created: 2025-12-16 16:14:32 +09:00
---

## App Store Guidelines & Policies

"Guideline 3.1.1 - In-App Purchase"
이 메일을 받는 순간 심장이 철렁합니다.
App Store는 단순한 마켓이 아니라, 엄격한 법률이 지배하는 국가입니다. 이 법(Guideline)을 모르면 앱은 영원히 출시되지 못합니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **리젝(Rejection) 방지**: 기껏 개발 다 해놨는데 "회원가입 기능이 애플 로그인(Sign in with Apple)을 지원하지 않아서 거절"당하면 오픈 일정이 2주 밀립니다.
- **수익 모델**: 넷플릭스처럼 외부 결제를 유도하면 앱이 잘립니다. **In-App Purchase(IAP)** 정책은 타협이 불가능한 영역입니다.
- **Minimum Functionality**: "웹사이트를 그냥 앱으로 감싼 것(Wrapper App)"은 거절됩니다. 앱만의 네이티브 기능이 있어야 합니다.

---

### 🏛️ 주요 반려 사유 (Common Rejections)

#### 1. Guideline 4.8 - Sign in with Apple
타사 소셜 로그인(구글, 페이스북, 카카오)을 지원한다면, **반드시** Apple 로그인도 동등한 크기로 붙여야 합니다.
- 예외: 자체 아이디/비번 로그인만 있는 경우, 기업 전용 앱 등.

#### 2. Guideline 3.1.1 - In-App Purchase
디지털 콘텐츠(이모티콘, 멤버십, 강의 등)는 무조건 Apple IAP를 써야 합니다.
- **금지**: "웹에서 결제하세요"라고 링크를 걸거나, 결제 유도 문구를 넣는 행위.
- **허용**: 넷플릭스처럼 "리더(Reader) 앱" 권한을 받으면 외부 링크 허용(매우 까다로움).

#### 3. Guideline 5.1.1 - Data Collection
"앱을 켜자마자 회원가입 강요"는 거절 사유입니다.
- 둘러보기(Guest Mode)를 허용해야 합니다. (단, 기능상 가입이 필수인 SNS 등은 예외)
- 필요한 권한(카메라 등)은 기능을 사용할 때 요청해야지, 켜자마자 요청하면 안 됩니다.

---

### 🌍 글로벌 규제 (Regulations)

#### 1. GDPR (유럽)
"잊혀질 권리". 사용자가 원하면 **"계정 탈퇴" 버튼**이 앱 내에 있어야 하고, 서버의 모든 데이터가 즉시 삭제되어야 합니다. "고객센터에 문의하세요"는 더 이상 통하지 않습니다.

#### 2. Export Compliance (암호화)
HTTPS(TLS)만 써도 암호화 기술 수출로 간주됩니다.
- App Store Connect에서 "표준 암호화만 사용함"이라고 체크해야 제출이 가능합니다. Info.plist에 `ITSAppUsesNonExemptEncryption` 키를 `NO`로 설정하면 매번 묻는 걸 스킵할 수 있습니다.

---

### 🏢 Enterprise & Custom Apps

App Store가 유일한 길은 아닙니다.

#### 1. Apple Business Manager (ABM)
특정 회사 임직원용 앱이나 B2B 앱은 **비공개 배포(Custom App)**를 해야 합니다.
- App Store 심사는 받지만, 일반 사용자에게 노출되지 않고 특정 조직의 VPP(Volume Purchase Program) 계정으로만 다운로드 가능합니다.

#### 2. Enterprise Program ($299/년)
심사 없이 내부 배포가 가능하지만, 인증서 관리가 지옥입니다.
- 인증서가 만료되면 전 직원의 앱이 즉시 실행 불가 상태가 됩니다.
- Apple이 남용(도박 앱 배포 등)을 감시하여 계정을 영구 정지시키기도 합니다.

### 더 보기
- [apple-build-and-distribution](apple-build-and-distribution.md) - 심사 통과 후 기술적인 배포 과정
- [apple-app-tracking-privacy](apple-app-tracking-privacy.md) - 심사의 또 다른 벽, 개인정보 정책
