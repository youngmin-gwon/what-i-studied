---
title: apple-accessibility-and-internationalization
tags: [a11y, apple, i18n, localization, quality, color, sf-symbols]
aliases: []
date modified: 2025-12-18 02:10:00 +09:00
date created: 2025-12-16 16:11:46 +09:00
---

## Accessibility & Internationalization

"장애인용 기능"이나 "해외 출시용 번역" 정도로 생각하면 오산입니다.
이 두 가지는 **앱의 품질(Quality)**과 **구조(Architecture)**를 검증하는 가장 강력한 리트머스 시험지입니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **코드 품질의 척도**: VoiceOver가 읽기 좋은 앱은 코드 구조도 깔끔합니다. 뷰가 논리적으로 그룹화되어 있고, 커스텀 컨트롤이 표준 프로토콜을 따르고 있다는 증거이기 때문입니다.
- **시장 확장**: 한국어만 지원하면 5천만 시장이지만, 영어와 스페인어만 추가해도 10억 시장이 됩니다. 처음부터 다국어 구조(`NSLocalizedString`)를 잡지 않으면 나중에 모든 코드를 뜯어고쳐야 합니다.
- **자동화 테스트**: 접근성 식별자(`accessibilityIdentifier`)는 UI 테스트 자동화의 핵심 키워드입니다.

---

### 🎨 Color & Visual Accessibility

#### 1. Color Contrast (대비)
예쁜 회색 글씨가 누군가에게는 '안 보이는' 글씨일 수 있습니다.
- **WCAG 권장**: 텍스트 대비율 **4.5:1** 이상을 지켜야 합니다.
- **Semantic Colors**: 시스템 색상(`systemBackground`, `label`)을 쓰면 다크 모드와 고대비 모드(High Contrast)가 자동으로 지원됩니다. `UIColor.white` 같은 고정 색상을 피하세요.

#### 2. SF Symbols (아이콘)
Apple이 제공하는 벡터 아이콘 세트입니다.
- **Dynamic Type**: 글자 크기에 맞춰 아이콘 크기도 자동으로 커집니다.
- **Scale**: `Small`, `Medium`, `Large` 굵기(Weight)를 폰트와 맞출 수 있어 시각적 일관성이 높습니다.

---

### ♿️ Accessibility (VoiceOver & Structure)

#### 1. VoiceOver와 UI 구조
시각 장애인은 화면을 볼 수 없으므로, 운영체제가 UI 트리를 읽어줍니다.
- **Label**: "재생" (이게 뭐야?)
- **Value**: "3분 20초" (현재 값이 뭐야?)
- **Trait**: "버튼" (뭐 할 수 있어?)
- **Hint**: "두 번 탭 하여 음악을 재생합니다" (어떻게 해?)

👉 **개발 팁**: 커스텀 뷰를 만들 때 `isAccessibilityElement = true`로 설정하고 위 속성들을 채워주면, 복잡한 뷰도 하나의 의미 있는 단위로 인식됩니다.

#### 2. Dynamic Type (가변 글꼴)
사용자가 시스템 글자 크기를 키우면 앱도 커져야 합니다.
- 고정 높이(`height: 50`)를 피하세요. 글자가 커지면 레이아웃이 깨집니다.
- **Intrinsic Content Size**: 오토 레이아웃이 내부 컨텐츠 크기에 맞춰 늘어나도록 제약을 잡아야 합니다.

#### 3. Automation (자동화)
QA 팀이나 CI/CD 파이프라인에서 UI 테스트를 돌릴 때, 버튼을 찾는 가장 안전한 방법은 접근성 ID를 쓰는 것입니다.
```swift
button.accessibilityIdentifier = "login_button" // 사용자에게는 안 보이고, 테스트 스크립트만 봄
```

---

### 🌏 Internationalization (국제화)

#### 1. 하드코딩 금지
"취소", "확인" 같은 문자열을 코드에 직접 박지 마세요.
```swift
// ❌ Bad
let title = "설정"

// ✅ Good (UIKit)
let title = NSLocalizedString("settings_title", comment: "설정 화면 타이틀")
```

#### 2. RTL (Right-to-Left)
아랍어나 히브리어권은 글자를 오른쪽에서 왼쪽으로 씁니다.
- `leftAnchor`, `rightAnchor` 대신 **`leadingAnchor`, `trailingAnchor`**를 써야 하는 결정적인 이유입니다.
- SwiftUI `HStack`은 자동으로 순서가 뒤집히지만, 절대 좌표를 쓰는 경우 주의해야 합니다.

#### 3. Locale-Aware Formatting
날짜, 숫자, 통화는 절대 문자열 템플릿(`"\(price)원"`)으로 조립하지 마세요.
```swift
let formatter = NumberFormatter()
formatter.numberStyle = .currency
formatter.locale = Locale.current // 시스템 설정을 따름 ($10, 10 €, 10원 자동 변환)
```

### 📚 더 보기
- [apple-platform-differences](../00_foundations/apple-platform-differences.md) - 플랫폼별 접근성 특징 (watchOS 탭틱 등)
- [apple-testing-and-quality](../06_testing_performance/apple-testing-and-quality.md) - UI 테스트 자동화
