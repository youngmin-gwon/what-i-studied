---
title: apple-urlsession-deep-dive
tags: [apple, async-await, http, networking, urlsession]
aliases: []
date modified: 2026-04-05 17:45:04 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## URLSession Cookbook

`URLSession` 은 iOS 네트워킹의 표준입니다.

Alamofire 같은 라이브러리도 훌륭하지만, **Swift Concurrency (`async/await`)**가 도입된 이후로는 순정 `URLSession` 만으로도 충분히 간결하고 강력한 코드를 짤 수 있습니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **Dependency 줄이기**: 서드파티 라이브러리 없이 네트워킹 레이어를 구축하면 앱 용량이 줄고 빌드 속도가 빨라집니다.
- **Async/Await 의 맛**: 콜백 지옥 없이 `let data = try await session.data(…)` 한 줄로 끝나는 쾌감을 느껴보세요.
- **Task Cancellation**: 화면을 나가면 네트워크 요청도 취소되어야 합니다. Swift Concurrency 는 이를 구조적으로 지원합니다.

---

### 📡 실무 구현 패턴 (Recipes)

#### 1. GET Request (Async/Await)

기본적인 데이터 요청입니다.

```swift
func fetchData() async throws -> UserData {
    let url = URL(string: "https://api.example.com/user")!
    
    // 1. 요청 시작 (Suspension Point: 여기서 스레드를 차단하지 않고 대기)
    let (data, response) = try await URLSession.shared.data(from: url)
    
    // 2. 응답 검증
    guard let httpResponse = response as? HTTPURLResponse,
          (200...299).contains(httpResponse.statusCode) else {
        throw NetworkError.invalidResponse
    }
    
    // 3. 디코딩
    return try JSONDecoder().decode(UserData.self, from: data)
}
```

#### 2. POST Upload (JSON)

`URLRequest` 에 헤더와 바디를 담아 보냅니다.

```swift
func uploadUser(user: UserData) async throws {
    var request = URLRequest(url: URL(string: "https://api.example.com/user")!)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    
    // 인코딩
    let bodyData = try JSONEncoder().encode(user)
    
    // 업로드
    let (_, response) = try await URLSession.shared.upload(for: request, from: bodyData)
    
    guard let httpResponse = response as? HTTPURLResponse,
          httpResponse.statusCode == 201 else {
        throw NetworkError.uploadFailed
    }
}
```

#### 3. Task Cancellation (취소 처리)

SwiftUI 의 `.task` 나 `Task { … }` 블록이 해제되면, 내부의 URLSession 요청도 자동으로 취소됩니다. 별도의 `cancel()` 호출이 필요 없습니다.

```swift
// ViewModel
func load() async {
    // 뷰가 사라지면 이 Task가 취소(Cancel)됨 -> URLSession도 자동 취소 에러(URLError.cancelled) 발생
    let data = try await session.data(from: url)
}
```

#### 4. Authentication (Interceptor Pattern)

토큰이 만료되었을 때 자동으로 갱신(Refresh)하고 재시도하는 로직은 `Delegate` 나 `Actor` 를 활용해 구현해야 합니다.

```swift
// 간단한 예시: 401 발생 시 재로그인 로직은 별도 Actor에서 처리 권장
if httpResponse.statusCode == 401 {
    try await authManager.refreshToken()
    return try await fetchData() // 재시도
}
```

### 더 보기
- [apple-networking-and-cloud](apple-networking-and-cloud.md) - URLSession 의 내부 구조와 보안
- [apple-codable-json](apple-codable-json.md) - JSON 파싱 성능 최적화
