---
title: apple-codable-json
tags: [apple, codable, json, performance, serialization, swift]
aliases: []
date modified: 2026-04-05 17:44:22 +09:00
date created: 2025-12-16 16:09:23 +09:00
---

## Codable & Serialization Deep Dive

Swift 4 의 기적, `Codable` 은 보일러플레이트 없는 JSON 파싱을 가능하게 했습니다.

하지만 컴파일러가 대신 해주는 이 마법에도 **비용(Cost)**이 따릅니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **성능 이슈**: 수만 개의 JSON 객체를 리스트로 렌더링할 때 버벅거린다면, `JSONDecoder` 가 범인일 확률이 높습니다. 자동 합성은 런타임에 **Reflection**과 유사한 메타데이터 검색 비용이 듭니다.
- **Any 타입 처리**: "서버에서 Int 로 올 때도 있고 String 으로 올 때도 있어요" -> `Codable` 의 지옥이 시작되는 지점입니다. `KeyedDecodingContainer` 를 열어서 직접 처리하는 법을 알아야 합니다.
- **날짜 포맷**: ISO8601 이 아닌 괴상한 날짜 포맷이 오면 `DateFormatter` 비용 때문에 파싱 속도가 10 배 느려질 수 있습니다.

---

### 🔍 내부 동작 원리 (How it works)

`Codable` 은 `Encodable` 과 `Decodable` 의 Type Alias 입니다.

컴파일러는 컴파일 타임에 `init(from decoder: Decoder)` 와 `encode(to encoder: Encoder)` 메서드를 자동으로 생성해줍니다.

#### 1. CodingKeys

구조체 프로퍼티 이름과 JSON 키가 다를 때 매핑해줍니다.

- 열거형(Enum)이므로 컴파일 타임에 오타를 잡을 수 있습니다.

#### 2. Container

인코딩/디코딩 과정은 `Container` 라는 추상화 위에서 일어납니다.

- **KeyedContainer**: 딕셔너리(`{}`) 형태.
- **UnkeyedContainer**: 배열(`[]`) 형태.
- **SingleValueContainer**: 단일 값(String, Int 등).

---

### 🛠️ 실무 패턴 및 문제 해결

#### 1. 유연한 타입 처리 (AnyDecodable)

서버가 어떤 타입의 값을 보낼지 모를 때, 제네릭 래퍼를 사용합니다.

```swift
struct AnyDecodable: Decodable {
    let value: Any
    
    init(from decoder: Decoder) throws {
        let container = try decoder.singleValueContainer()
        if let intVal = try? container.decode(Int.self) { value = intVal }
        else if let strVal = try? container.decode(String.self) { value = strVal }
        else { ... }
    }
}
```

#### 2. 날짜 성능 최적화 (Date Parsing)

`DateFormatter` 는 생성 비용이 매우 비쌉니다. (약 0.5ms ~ 1ms). 리스트 파싱할 때마다 생성하면 프레임 드랍이 생깁니다.

**해결책**:

1. `static` 인스턴스로 재사용.
2. iOS 10+ 에서는 `ISO8601DateFormatter` 가 더 빠릅니다.
3. 더 극한의 성능이 필요하면 `strptime` (C API)을 래핑해서 씁니다.

```swift
// ❌ Bad: 매번 생성
decoder.dateDecodingStrategy = .formatted(DateFormatter())

// ✅ Good: 재사용
decoder.dateDecodingStrategy = .formatted(DateFormatter.cachedISO8601)
```

#### 3. 성능 문제 시 수동 구현

자동 합성된 코드는 안전하지만 최적은 아닙니다. 수백만 건 처리 시에는 수동 구현이 더 빠를 수 있습니다.

```swift
// 수동 구현으로 키 검색 비용을 줄일 수 있음
init(from decoder: Decoder) throws {
    let container = try decoder.container(keyedBy: CodingKeys.self)
    // 키가 없으면 기본값을 넣어 실패 방지
    self.name = try container.decodeIfPresent(String.self, forKey: .name) ?? "Unknown"
    self.age = try container.decode(Int.self, forKey: .age)
}
```

### 📚 더 보기
- [apple-networking-and-cloud](apple-networking-and-cloud.md) - URLSession 과 Codable 연동
- [apple-coredata-deep-dive](apple-coredata-deep-dive.md) - `NSManagedObject` 를 Codable 로 만들기 (주의사항 많음)
