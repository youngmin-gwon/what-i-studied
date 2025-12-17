---
title: apple-codable-json
tags: [apple, codable, json, serialization]
aliases: []
date modified: 2025-12-16 17:01:32 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Codable & JSON apple codable json serialization

Codable 을 사용한 JSON 처리. 기본은 [[apple-runtime-and-swift]] 참고.

### 기본 Codable

```swift
struct User: Codable {
    let id: Int
    let name: String
    let email: String
}

// 디코딩
let json = """
{
    "id": 1,
    "name": "John",
    "email": "john@example.com"
}
""".data(using: .utf8)!

let user = try JSONDecoder().decode(User.self, from: json)

// 인코딩
let encoder = JSONEncoder()
encoder.outputFormatting = .prettyPrinted
let data = try encoder.encode(user)
```

### CodingKeys

```swift
struct User: Codable {
    let id: Int
    let name: String
    let emailAddress: String
    
    enum CodingKeys: String, CodingKey {
        case id
        case name
        case emailAddress = "email" // JSON 의 "email" → emailAddress
    }
}
```

### 중첩 구조

```swift
struct Response: Codable {
    let data: UserData
    let meta: Meta
    
    struct UserData: Codable {
        let users: [User]
    }
    
    struct Meta: Codable {
        let total: Int
        let page: Int
    }
}
```

### 더 보기

[[apple-urlsession-deep-dive]], [[apple-runtime-and-swift]]
